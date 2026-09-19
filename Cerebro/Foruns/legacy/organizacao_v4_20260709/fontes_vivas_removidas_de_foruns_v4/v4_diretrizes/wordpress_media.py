from __future__ import annotations

import fcntl
import json
import os
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .loader import DirectiveLoader


DEFAULT_WORDPRESS_MEDIA_CONTRACT = "diretrizes/v4_wordpress_media_v1.json"


@dataclass(frozen=True)
class WordPressMediaMapping:
    image_id: str
    wp_media_id: int
    source: str
    url: str
    credit: str
    license: str
    operator: str = "codex"
    timestamp: str | None = None
    schema_version: str = "v1"

    def as_dict(self) -> dict[str, Any]:
        return {
            "schema_version": self.schema_version,
            "timestamp": self.timestamp or datetime.now(timezone.utc).isoformat(),
            "image_id": self.image_id,
            "wp_media_id": self.wp_media_id,
            "source": self.source,
            "url": self.url,
            "credit": self.credit,
            "license": self.license,
            "operator": self.operator,
        }


class V4WordPressMediaMapper:
    """Mapeia imagens auditadas V4 para IDs da biblioteca de midia WordPress."""

    def __init__(self, root: str | Path = ".", contract_path: str = DEFAULT_WORDPRESS_MEDIA_CONTRACT) -> None:
        self.loader = DirectiveLoader(root)
        self.root = self.loader.root
        self.contract_path = contract_path
        self.contract = self.loader.read_json(contract_path)

    def add_mapping(self, mapping: WordPressMediaMapping, execute: bool = False) -> dict[str, Any]:
        payload = mapping.as_dict()
        errors = self._validate(payload)
        path = self._path(payload["timestamp"])
        if errors:
            return {"ok": False, "mode": "invalid", "errors": errors, "mapping": payload}
        if not execute:
            return {"ok": True, "mode": "dry_run", "path": str(path.relative_to(self.root)), "mapping": payload}
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a", encoding="utf-8") as handle:
            fcntl.flock(handle.fileno(), fcntl.LOCK_EX)
            handle.write(json.dumps(payload, ensure_ascii=False, sort_keys=True) + "\n")
            handle.flush()
            os.fsync(handle.fileno())
            fcntl.flock(handle.fileno(), fcntl.LOCK_UN)
        return {"ok": True, "mode": "appended", "path": str(path.relative_to(self.root)), "mapping": payload}

    def lookup(self, image_id: str) -> dict[str, Any] | None:
        found: dict[str, Any] | None = None
        for item in self._read_all():
            if item.get("image_id") == image_id:
                found = item
        return found

    def _validate(self, payload: dict[str, Any]) -> list[str]:
        errors: list[str] = []
        for field_name in self.contract["required_fields"]:
            if payload.get(field_name) in (None, ""):
                errors.append(f"campo_mapping_ausente:{field_name}")
        if not isinstance(payload.get("wp_media_id"), int) or int(payload.get("wp_media_id", 0)) <= 0:
            errors.append("wp_media_id_invalido")
        return errors

    def _read_all(self) -> list[dict[str, Any]]:
        base = self.root / self.contract["store"]["path"]
        records: list[dict[str, Any]] = []
        for path in sorted(base.glob("*.jsonl")):
            records.extend(self._read_jsonl(path))
        return records

    def _path(self, timestamp: str) -> Path:
        day = datetime.fromisoformat(timestamp.replace("Z", "+00:00")).date().isoformat().replace("-", "")
        return self.root / self.contract["store"]["path"] / f"{self.contract['store']['filename_prefix']}_{day}.jsonl"

    @staticmethod
    def _read_jsonl(path: Path) -> list[dict[str, Any]]:
        if not path.exists():
            return []
        return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
