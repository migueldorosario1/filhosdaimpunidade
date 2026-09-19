from __future__ import annotations

import fcntl
import json
import os
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .loader import DirectiveLoader


DEFAULT_LLM_DECISIONS_CONTRACT = "diretrizes/v4_llm_decisions_v1.json"


@dataclass(frozen=True)
class LLMRouterDecision:
    editoria: str
    funcao: str
    idempotency_key: str
    prompt_hash: str
    selected_provider: str
    selected_model: str
    selected_tier: str
    selection_strategy: str
    selection_reason: str
    candidate_count: int
    mode: str
    expected_cost_usd: float
    timestamp: str | None = None
    schema_version: str = "v1"

    def as_dict(self) -> dict[str, Any]:
        return {
            "schema_version": self.schema_version,
            "timestamp": self.timestamp or datetime.now(timezone.utc).isoformat(),
            "editoria": self.editoria,
            "funcao": self.funcao,
            "idempotency_key": self.idempotency_key,
            "prompt_hash": self.prompt_hash,
            "selected_provider": self.selected_provider,
            "selected_model": self.selected_model,
            "selected_tier": self.selected_tier,
            "selection_strategy": self.selection_strategy,
            "selection_reason": self.selection_reason,
            "candidate_count": self.candidate_count,
            "mode": self.mode,
            "expected_cost_usd": self.expected_cost_usd,
        }


class V4LLMDecisionStore:
    """Trilha append-only das decisoes do roteador LLM."""

    def __init__(self, root: str | Path = ".", contract_path: str = DEFAULT_LLM_DECISIONS_CONTRACT) -> None:
        self.loader = DirectiveLoader(root)
        self.root = self.loader.root
        self.contract_path = contract_path
        self.contract = self.loader.read_json(contract_path)

    def record(self, decision: LLMRouterDecision, execute: bool = False) -> dict[str, Any]:
        payload = decision.as_dict()
        errors = self._validate(payload)
        path = self._path(payload["timestamp"])
        if errors:
            return {"ok": False, "mode": "invalid", "path": str(path.relative_to(self.root)), "errors": errors}
        if not execute:
            return {"ok": True, "mode": "dry_run", "path": str(path.relative_to(self.root)), "decision": payload}

        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a", encoding="utf-8") as handle:
            fcntl.flock(handle.fileno(), fcntl.LOCK_EX)
            handle.write(json.dumps(payload, ensure_ascii=False, sort_keys=True) + "\n")
            handle.flush()
            os.fsync(handle.fileno())
            fcntl.flock(handle.fileno(), fcntl.LOCK_UN)
        return {"ok": True, "mode": "appended", "path": str(path.relative_to(self.root)), "decision": payload}

    def _validate(self, payload: dict[str, Any]) -> list[str]:
        errors: list[str] = []
        for field_name in self.contract.get("required_fields", []):
            if field_name not in payload:
                errors.append(f"campo obrigatorio ausente na decisao LLM: {field_name}")
        try:
            datetime.fromisoformat(str(payload.get("timestamp", "")).replace("Z", "+00:00"))
        except ValueError:
            errors.append("timestamp deve ser ISO8601")
        return errors

    def _path(self, timestamp: str) -> Path:
        parsed = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
        day = parsed.date().isoformat().replace("-", "")
        return self.root / self.contract["store"]["path"] / f"decisions_{day}.jsonl"
