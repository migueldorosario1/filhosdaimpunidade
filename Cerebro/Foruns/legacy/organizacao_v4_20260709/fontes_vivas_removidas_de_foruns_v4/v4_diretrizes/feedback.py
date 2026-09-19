from __future__ import annotations

import fcntl
import json
import os
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .loader import DirectiveLoader
from .memoria import MemoryEvent, V4MemoryStore


DEFAULT_FEEDBACK_CONTRACT = "diretrizes/v4_feedback_editor_v1.json"


@dataclass(frozen=True)
class EditorFeedback:
    item_id: str
    vertical: str
    editor: str
    score: int
    sentiment: str
    comment: str
    correction_class: str
    provider: str
    model: str
    operation: str
    timestamp: str | None = None
    schema_version: str = "v1"

    def as_dict(self) -> dict[str, Any]:
        return {
            "schema_version": self.schema_version,
            "timestamp": self.timestamp or datetime.now(timezone.utc).isoformat(),
            "item_id": self.item_id,
            "vertical": self.vertical,
            "editor": self.editor,
            "score": self.score,
            "sentiment": self.sentiment,
            "comment": self.comment,
            "correction_class": self.correction_class,
            "provider": self.provider,
            "model": self.model,
            "operation": self.operation,
        }


class V4EditorFeedbackStore:
    """Feedback do editor e ranking por modelo a partir de recibos JSONL."""

    def __init__(self, root: str | Path = ".", contract_path: str = DEFAULT_FEEDBACK_CONTRACT) -> None:
        self.loader = DirectiveLoader(root)
        self.root = self.loader.root
        self.contract_path = contract_path
        self.contract = self.loader.read_json(contract_path)
        self.memory = V4MemoryStore(self.root)

    def record(
        self,
        item_id: str,
        vertical: str,
        editor: str,
        score: int,
        sentiment: str,
        comment: str,
        correction_class: str,
        operation: str = "produzir_dry_run",
        provider: str | None = None,
        model: str | None = None,
        execute: bool = False,
    ) -> dict[str, Any]:
        if provider is None or model is None:
            llm = self._find_llm_for_item(item_id, vertical, operation)
            provider = provider or llm.get("provider", "unknown")
            model = model or llm.get("model", "unknown")

        feedback = EditorFeedback(
            item_id=item_id,
            vertical=vertical,
            editor=editor,
            score=score,
            sentiment=sentiment,
            comment=comment,
            correction_class=correction_class,
            provider=provider,
            model=model,
            operation=operation,
        )
        payload = feedback.as_dict()
        errors = self._validate(payload)
        if errors:
            return {"ok": False, "mode": "invalid", "errors": errors, "feedback": payload}
        path = self.root / self.contract["store"]["path"]
        if not execute:
            return {"ok": True, "mode": "dry_run", "path": str(path.relative_to(self.root)), "feedback": payload}

        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a", encoding="utf-8") as handle:
            fcntl.flock(handle.fileno(), fcntl.LOCK_EX)
            handle.write(json.dumps(payload, ensure_ascii=False, sort_keys=True) + "\n")
            handle.flush()
            os.fsync(handle.fileno())
            fcntl.flock(handle.fileno(), fcntl.LOCK_UN)

        self.memory.append(
            MemoryEvent(
                event_type="comentario_editor",
                severity="info" if score >= 3 else "warning",
                source="v4_editor_feedback",
                summary=f"Feedback editor {editor}: {score}/5 para {provider}:{model}",
                tags=["v4", "feedback_editor", vertical, provider, model],
                payload=payload,
            ),
            execute=True,
        )
        return {"ok": True, "mode": "appended", "path": str(path.relative_to(self.root)), "feedback": payload}

    def ranking(self) -> list[dict[str, Any]]:
        feedbacks = self._read_feedbacks()
        receipts = self._receipt_index()
        groups: dict[tuple[str, str, str, str], list[dict[str, Any]]] = {}
        for item in feedbacks:
            key = (item["vertical"], item["provider"], item["model"], item["operation"])
            groups.setdefault(key, []).append(item)

        ranked: list[dict[str, Any]] = []
        for (vertical, provider, model, operation), items in groups.items():
            avg = sum(float(item["score"]) for item in items) / len(items)
            costs = [
                float(receipts.get((item["vertical"], item["item_id"], item["operation"]), {}).get("cost_usd_estimated", 0.0))
                for item in items
            ]
            total_cost = round(sum(costs), 8)
            avg_cost = round(total_cost / len(items), 8) if items else 0.0
            score_per_usd = round(avg / avg_cost, 3) if avg_cost > 0 else None
            ranked.append(
                {
                    "vertical": vertical,
                    "provider": provider,
                    "model": model,
                    "operation": operation,
                    "samples": len(items),
                    "avg_score": round(avg, 3),
                    "total_cost_usd_estimated": total_cost,
                    "avg_cost_usd_estimated": avg_cost,
                    "score_per_usd_estimated": score_per_usd,
                    "correction_classes": self._count_by(items, "correction_class"),
                }
            )
        return sorted(ranked, key=lambda item: (-item["avg_score"], -item["samples"], item["provider"], item["model"]))

    def _validate(self, payload: dict[str, Any]) -> list[str]:
        errors: list[str] = []
        for field_name in self.contract.get("required_fields", []):
            if field_name not in payload:
                errors.append(f"campo obrigatorio ausente no feedback: {field_name}")
        score_cfg = self.contract.get("score", {})
        if not (int(score_cfg.get("min", 1)) <= int(payload.get("score", 0)) <= int(score_cfg.get("max", 5))):
            errors.append("score fora da faixa permitida")
        if payload.get("sentiment") not in set(self.contract.get("sentiments", [])):
            errors.append("sentiment invalido")
        if payload.get("correction_class") not in set(self.contract.get("correction_classes", [])):
            errors.append("correction_class invalida")
        return errors

    def _find_llm_for_item(self, item_id: str, vertical: str, operation: str) -> dict[str, Any]:
        for receipt in reversed(self._read_receipts(vertical)):
            if receipt.get("item_id") != item_id:
                continue
            if receipt.get("operation") != operation:
                continue
            return dict(receipt.get("llm", {}))
        return {}

    def _read_receipts(self, vertical: str) -> list[dict[str, Any]]:
        receipt_dir = self.root / "agent_data/v4/receipts"
        receipts: list[dict[str, Any]] = []
        for path in sorted(receipt_dir.glob(f"{vertical}_*.jsonl")):
            receipts.extend(self._read_jsonl(path))
        return receipts

    def _receipt_index(self) -> dict[tuple[str, str, str], dict[str, Any]]:
        receipt_dir = self.root / "agent_data/v4/receipts"
        index: dict[tuple[str, str, str], dict[str, Any]] = {}
        for path in sorted(receipt_dir.glob("*.jsonl")):
            for receipt in self._read_jsonl(path):
                key = (receipt.get("vertical", ""), receipt.get("item_id", ""), receipt.get("operation", ""))
                index[key] = receipt
        for result in self._read_recomputed_costs():
            if result.get("status") != "recomputed":
                continue
            key = (result.get("vertical", ""), result.get("item_id", ""), result.get("operation", ""))
            if key not in index:
                continue
            index[key] = {
                **index[key],
                "cost_usd_estimated": result.get("new_cost_usd_estimated", 0.0),
                "pricing_table_version": result.get("new_pricing_table_version", "pending"),
            }
        return index

    def _read_recomputed_costs(self) -> list[dict[str, Any]]:
        recomputed_dir = self.root / "agent_data/v4/receipts/recomputed"
        results: list[dict[str, Any]] = []
        for path in sorted(recomputed_dir.glob("*.jsonl")):
            results.extend(self._read_jsonl(path))
        return results

    def _read_feedbacks(self) -> list[dict[str, Any]]:
        return self._read_jsonl(self.root / self.contract["store"]["path"])

    @staticmethod
    def _read_jsonl(path: Path) -> list[dict[str, Any]]:
        if not path.exists():
            return []
        return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]

    @staticmethod
    def _count_by(items: list[dict[str, Any]], field_name: str) -> dict[str, int]:
        counts: dict[str, int] = {}
        for item in items:
            key = str(item.get(field_name, "unknown"))
            counts[key] = counts.get(key, 0) + 1
        return counts
