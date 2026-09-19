from __future__ import annotations

import fcntl
import json
import os
import re
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .loader import DirectiveLoader


DEFAULT_TELEMETRY_CONTRACT = "diretrizes/v4_telemetria_v1.json"


@dataclass(frozen=True)
class LLMCallDetail:
    provider: str
    model: str
    tier: str
    tokens_in: int = 0
    tokens_out: int = 0
    duration_ms_llm: int = 0
    prompt_hash: str = ""
    error_class: str | None = None

    def as_dict(self) -> dict[str, Any]:
        return {
            "provider": self.provider,
            "model": self.model,
            "tier": self.tier,
            "tokens_in": self.tokens_in,
            "tokens_out": self.tokens_out,
            "duration_ms_llm": self.duration_ms_llm,
            "prompt_hash": self.prompt_hash,
            "error_class": self.error_class,
        }


@dataclass(frozen=True)
class TelemetryReceipt:
    event_type: str
    item_id: str
    vertical: str
    agent: str
    operation: str
    status: str
    idempotency_key: str
    llm: LLMCallDetail | None = None
    duration_ms: int = 0
    cost_usd_estimated: float = 0.0
    pricing_table_version: str = "pending"
    payload: dict[str, Any] = field(default_factory=dict)
    timestamp: str | None = None
    schema_version: str = "v1"

    def as_dict(self) -> dict[str, Any]:
        return {
            "schema_version": self.schema_version,
            "timestamp": self.timestamp or datetime.now(timezone.utc).isoformat(),
            "event_type": self.event_type,
            "item_id": self.item_id,
            "vertical": self.vertical,
            "agent": self.agent,
            "operation": self.operation,
            "status": self.status,
            "llm": self.llm.as_dict() if self.llm is not None else {},
            "idempotency_key": self.idempotency_key,
            "duration_ms": self.duration_ms,
            "cost_usd_estimated": self.cost_usd_estimated,
            "pricing_table_version": self.pricing_table_version,
            "payload": self.payload,
        }


class V4Telemetry:
    """Telemetria V4: recibo JSONL obrigatorio e Prometheus agregado opcional."""

    def __init__(self, root: str | Path = ".", contract_path: str = DEFAULT_TELEMETRY_CONTRACT) -> None:
        self.loader = DirectiveLoader(root)
        self.root = self.loader.root
        self.contract_path = contract_path
        self.contract = self.loader.read_json(contract_path)

    def record_receipt(self, receipt: TelemetryReceipt, execute: bool = False) -> dict[str, Any]:
        payload = receipt.as_dict()
        errors = self._validate_receipt(payload)
        if errors:
            return {"ok": False, "mode": "invalid", "errors": errors, "receipt": payload}
        try:
            path = self._receipt_path(receipt.vertical, payload["timestamp"])
        except ValueError as exc:
            return {"ok": False, "mode": "invalid", "errors": [str(exc)], "receipt": payload}
        if not execute:
            return {"ok": True, "mode": "dry_run", "path": str(path.relative_to(self.root)), "receipt": payload}
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a", encoding="utf-8") as handle:
            fcntl.flock(handle.fileno(), fcntl.LOCK_EX)
            handle.write(json.dumps(payload, ensure_ascii=False, sort_keys=True) + "\n")
            handle.flush()
            os.fsync(handle.fileno())
            fcntl.flock(handle.fileno(), fcntl.LOCK_UN)
        return {"ok": True, "mode": "appended", "path": str(path.relative_to(self.root)), "receipt": payload}

    def validate_prometheus_labels(self, labels: dict[str, str]) -> list[str]:
        forbidden = set(self.contract.get("prometheus", {}).get("forbidden_labels", []))
        allowed = set(self.contract.get("prometheus", {}).get("allowed_labels", []))
        errors: list[str] = []
        for label in labels:
            if label in forbidden:
                errors.append(f"label proibido no Prometheus: {label}")
            if allowed and label not in allowed:
                errors.append(f"label fora do vocabulario permitido: {label}")
        return errors

    def push_prometheus_counter(self, metric: str, labels: dict[str, str], value: float = 1.0) -> dict[str, Any]:
        errors = self.validate_prometheus_labels(labels)
        if errors:
            return {"ok": False, "mode": "invalid", "errors": errors}
        enabled = self.contract.get("prometheus", {}).get("enabled") is True
        if not enabled:
            return {"ok": True, "mode": "disabled", "metric": metric, "labels": labels, "value": value}
        return {"ok": True, "mode": "not_implemented", "metric": metric, "labels": labels, "value": value}

    def _validate_receipt(self, payload: dict[str, Any]) -> list[str]:
        errors: list[str] = []
        for field_name in self.contract.get("receipts", {}).get("required_fields", []):
            if field_name not in payload:
                errors.append(f"campo obrigatorio ausente no recibo: {field_name}")
        llm = payload.get("llm", {})
        if llm:
            for field_name in self.contract.get("receipts", {}).get("llm_required_fields", []):
                if field_name not in llm:
                    errors.append(f"campo obrigatorio ausente em llm: {field_name}")
        return errors

    def _receipt_path(self, vertical: str, timestamp: str) -> Path:
        self._validate_vertical(vertical)
        try:
            parsed = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
        except ValueError as exc:
            raise ValueError(f"timestamp deve ser ISO8601, veio: {timestamp!r}") from exc
        yyyymmdd = parsed.date().isoformat().replace("-", "")
        base_dir = self.contract["receipts"]["base_dir"]
        filename = self.contract["receipts"]["filename_pattern"].format(vertical=vertical, yyyymmdd=yyyymmdd)
        return self.root / base_dir / filename

    @staticmethod
    def _validate_vertical(vertical: str) -> None:
        if not re.fullmatch(r"[A-Za-z0-9_]+", vertical):
            raise ValueError(f"vertical invalida: {vertical!r}")
