from __future__ import annotations

import fcntl
import json
import os
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .imagem_destacada import DEFAULT_FEATURED_IMAGE_CONTRACT, MediaEvaluation
from .loader import DirectiveLoader


@dataclass(frozen=True)
class AuditedMediaRecord:
    image_id: str
    source: str
    url: str
    title: str
    credit: str
    license: str
    rights_status: str
    width: int
    height: int
    entity: str
    final_score: float
    visual_confidence: float
    reason_class: str
    safe_to_publish: bool
    caption: str = ""
    content_type: str = "image/jpeg"
    timestamp: str | None = None
    schema_version: str = "v1"

    @classmethod
    def from_evaluation(cls, evaluation: MediaEvaluation) -> "AuditedMediaRecord":
        candidate = evaluation.candidate
        return cls(
            image_id=candidate.image_id,
            source=candidate.source,
            url=candidate.url,
            title=candidate.title,
            credit=candidate.credit,
            license=candidate.license,
            rights_status=candidate.rights_status,
            width=candidate.width,
            height=candidate.height,
            entity=candidate.entity,
            final_score=evaluation.final_score,
            visual_confidence=evaluation.visual_confidence,
            reason_class=evaluation.reason_class,
            safe_to_publish=evaluation.safe_to_publish,
            caption=candidate.caption,
            content_type=candidate.content_type,
        )

    def as_dict(self) -> dict[str, Any]:
        return {
            "schema_version": self.schema_version,
            "timestamp": self.timestamp or datetime.now(timezone.utc).isoformat(),
            "image_id": self.image_id,
            "source": self.source,
            "url": self.url,
            "title": self.title,
            "credit": self.credit,
            "license": self.license,
            "rights_status": self.rights_status,
            "width": self.width,
            "height": self.height,
            "entity": self.entity,
            "final_score": self.final_score,
            "visual_confidence": self.visual_confidence,
            "reason_class": self.reason_class,
            "safe_to_publish": self.safe_to_publish,
            "caption": self.caption,
            "content_type": self.content_type,
        }


class V4AuditedMediaStore:
    """Acervo auditado local. O publicador V4 deve ler esta camada, nao candidatos."""

    def __init__(self, root: str | Path = ".", contract_path: str = DEFAULT_FEATURED_IMAGE_CONTRACT) -> None:
        self.loader = DirectiveLoader(root)
        self.root = self.loader.root
        self.contract_path = contract_path
        self.contract = self.loader.read_json(contract_path)

    def promote(self, evaluation: MediaEvaluation, execute: bool = False) -> dict[str, Any]:
        if not evaluation.ok:
            return {
                "ok": False,
                "mode": "blocked",
                "errors": ["avaliacao_nao_aprovada"],
                "evaluation": evaluation.as_dict(),
            }
        record = AuditedMediaRecord.from_evaluation(evaluation)
        payload = record.as_dict()
        path = self._path(payload["timestamp"])
        if not execute:
            return {"ok": True, "mode": "dry_run", "path": str(path.relative_to(self.root)), "record": payload}
        path.parent.mkdir(parents=True, exist_ok=True)
        if self._already_exists(record.image_id):
            return {"ok": True, "mode": "already_exists", "path": str(path.relative_to(self.root)), "record": payload}
        with path.open("a", encoding="utf-8") as handle:
            fcntl.flock(handle.fileno(), fcntl.LOCK_EX)
            handle.write(json.dumps(payload, ensure_ascii=False, sort_keys=True) + "\n")
            handle.flush()
            os.fsync(handle.fileno())
            fcntl.flock(handle.fileno(), fcntl.LOCK_UN)
        return {"ok": True, "mode": "appended", "path": str(path.relative_to(self.root)), "record": payload}

    def search(self, entity: str, limit: int = 5) -> list[dict[str, Any]]:
        wanted = self._normalize(entity)
        matches = [
            record
            for record in self._read_records()
            if wanted and wanted in self._normalize(str(record.get("entity", ""))) and record.get("safe_to_publish") is True
        ]
        matches.sort(key=lambda item: (-float(item.get("final_score", 0.0)), -float(item.get("visual_confidence", 0.0))))
        return matches[:limit]

    def _already_exists(self, image_id: str) -> bool:
        return any(record.get("image_id") == image_id for record in self._read_records())

    def _read_records(self) -> list[dict[str, Any]]:
        audit_dir = self.root / self.contract["stores"]["audit_dir"]
        records: list[dict[str, Any]] = []
        for path in sorted(audit_dir.glob("*.jsonl")):
            records.extend(self._read_jsonl(path))
        return records

    def _path(self, timestamp: str) -> Path:
        day = datetime.fromisoformat(timestamp.replace("Z", "+00:00")).date().isoformat().replace("-", "")
        return self.root / self.contract["stores"]["audit_dir"] / f"audited_media_{day}.jsonl"

    @staticmethod
    def _read_jsonl(path: Path) -> list[dict[str, Any]]:
        if not path.exists():
            return []
        return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]

    @staticmethod
    def _normalize(text: str) -> str:
        return " ".join((text or "").strip().lower().split())
