from __future__ import annotations

import json
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .loader import DirectiveLoader


DEFAULT_MEMORY_CONTRACT = "diretrizes/v4_memoria_autocura_v1.json"


@dataclass(frozen=True)
class MemoryEvent:
    event_type: str
    severity: str
    source: str
    summary: str
    tags: list[str] = field(default_factory=list)
    payload: dict[str, Any] = field(default_factory=dict)
    timestamp: str | None = None

    def as_dict(self) -> dict[str, Any]:
        return {
            "timestamp": self.timestamp or datetime.now(timezone.utc).isoformat(),
            "event_type": self.event_type,
            "severity": self.severity,
            "source": self.source,
            "summary": self.summary,
            "tags": self.tags,
            "payload": self.payload,
        }


class V4MemoryStore:
    """Memoria append-only do V4."""

    def __init__(self, root: str | Path = ".", contract_path: str = DEFAULT_MEMORY_CONTRACT) -> None:
        self.loader = DirectiveLoader(root)
        self.root = self.loader.root
        self.contract_path = contract_path
        self.contract = self.loader.read_json(contract_path)
        self.path = self.root / self.contract["store"]["path"]

    def validate_event(self, event: MemoryEvent) -> list[str]:
        errors: list[str] = []
        payload = event.as_dict()
        for field_name in self.contract.get("required_fields", []):
            if field_name not in payload:
                errors.append(f"campo obrigatorio ausente: {field_name}")
        if event.event_type not in set(self.contract.get("event_types", [])):
            errors.append(f"event_type invalido: {event.event_type}")
        if event.severity not in set(self.contract.get("severities", [])):
            errors.append(f"severity invalida: {event.severity}")
        return errors

    def append(self, event: MemoryEvent, execute: bool = False) -> dict[str, Any]:
        errors = self.validate_event(event)
        payload = event.as_dict()
        if errors:
            return {"ok": False, "mode": "invalid", "errors": errors, "event": payload}
        if not execute:
            return {"ok": True, "mode": "dry_run", "path": str(self.path.relative_to(self.root)), "event": payload}
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(payload, ensure_ascii=False, sort_keys=True) + "\n")
        return {"ok": True, "mode": "appended", "path": str(self.path.relative_to(self.root)), "event": payload}

    def tail(self, limit: int = 10) -> list[dict[str, Any]]:
        if not self.path.exists():
            return []
        lines = self.path.read_text(encoding="utf-8").splitlines()[-limit:]
        return [json.loads(line) for line in lines if line.strip()]
