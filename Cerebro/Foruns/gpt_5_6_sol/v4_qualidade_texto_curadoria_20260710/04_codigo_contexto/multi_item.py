from __future__ import annotations

import hashlib
import json
import tempfile
from copy import deepcopy
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .coerencia_editorial import V4EditorialCoherenceGate
from .fluxo import V4DryRunFlow
from .loader import DirectiveLoader


DEFAULT_MULTI_ITEM_CONTRACT = "contratos/v4_multi_item_lab_v1.json"


@dataclass(frozen=True)
class FrozenSourceState:
    path: str
    sha256_before: str
    sha256_after: str
    unchanged: bool

    def as_dict(self) -> dict[str, Any]:
        return {
            "path": self.path,
            "sha256_before": self.sha256_before,
            "sha256_after": self.sha256_after,
            "unchanged": self.unchanged,
        }


class V4MultiItemLabRunner:
    """Gerencia lotes V4 em laboratorio com curadoria congelada."""

    def __init__(self, root: str | Path = ".", contract_path: str = DEFAULT_MULTI_ITEM_CONTRACT) -> None:
        self.loader = DirectiveLoader(root)
        self.root = self.loader.root
        self.contract_path = contract_path
        self.contract = self.loader.read_json(contract_path)
        self.base_flow = self.loader.read_json(self.contract["base_flow_contract"])
        self.coherence_gate = V4EditorialCoherenceGate(
            self.root,
            self.contract.get("editorial_coherence_contract", "contratos/v4_editoria_coerencia_v1.json"),
        )

    def run(self, execute: bool = False) -> dict[str, Any]:
        frozen_before = self._frozen_hashes()
        item_results = []

        for item in self.contract.get("items", []):
            item_results.append(self._run_item(item, execute=execute))

        frozen_after = self._frozen_hashes()
        frozen_states = [
            FrozenSourceState(
                path=path,
                sha256_before=frozen_before.get(path, ""),
                sha256_after=frozen_after.get(path, ""),
                unchanged=frozen_before.get(path) == frozen_after.get(path),
            )
            for path in sorted(set(frozen_before) | set(frozen_after))
        ]
        issues = self._batch_issues(item_results, frozen_states)
        report = {
            "schema_version": self.contract.get("_version", "v1"),
            "status": "multi_item_lab_ok" if not issues else "multi_item_lab_com_issues",
            "batch_id": self.contract["batch_id"],
            "contract": self.contract_path,
            "created_at": self._now(),
            "mode": "executed" if execute else "dry_run",
            "wordpress_real": False,
            "external_publish": False,
            "promocao_real_executada": False,
            "frozen_sources": [state.as_dict() for state in frozen_states],
            "aggregate": {
                "total_items": len(item_results),
                "ok_items": sum(1 for item in item_results if item["ok"]),
                "failed_items": sum(1 for item in item_results if not item["ok"]),
                "editorias": sorted({str(item.get("editoria", "")) for item in item_results}),
                "curadoria_frozen": all(state.unchanged for state in frozen_states),
                "editorial_review_required_items": sorted(
                    str(item.get("item_id"))
                    for item in item_results
                    if (item.get("editorial_coherence") or {}).get("human_review_required") is True
                ),
            },
            "issues": issues,
            "items": item_results,
        }
        if execute:
            output_path = self.root / self.contract["output_path"]
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
            report["output_path"] = str(output_path.relative_to(self.root))
        return report

    def _run_item(self, item: dict[str, Any], execute: bool) -> dict[str, Any]:
        flow_contract = deepcopy(self.base_flow)
        flow_contract["fixture"] = item
        flow_contract["_doc"] = "Contrato temporario gerado pelo V4MultiItemLabRunner; nao e fonte viva."
        flow_contract["modo_experimento"]["external_publish"] = False
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".json", delete=False) as handle:
            json.dump(flow_contract, handle, ensure_ascii=False, indent=2, sort_keys=True)
            temp_contract = Path(handle.name)
        try:
            result = V4DryRunFlow(self.root, temp_contract).run(execute=execute)
        finally:
            temp_contract.unlink(missing_ok=True)

        steps = result.get("steps", [])
        editorial_coherence = self._editorial_coherence(steps)
        coherence_warnings = [str(warning) for warning in editorial_coherence.get("warnings", []) if str(warning)]
        coherence_issues = [str(issue) for issue in editorial_coherence.get("issues", []) if str(issue)]
        return {
            "item_id": item["item_id"],
            "editoria": item["editoria"],
            "ok": bool(result.get("ok")) and not coherence_issues,
            "fixture_path": result.get("fixture_path"),
            "editorial_coherence": editorial_coherence,
            "steps": [
                {
                    "step": step.get("step"),
                    "mode": step.get("mode"),
                    "issues": step.get("issues", []),
                    "warnings": step.get("warnings", []),
                    "target_path": step.get("target_path"),
                }
                for step in steps
            ],
            "warnings": sorted({warning for step in steps for warning in step.get("warnings", [])} | set(coherence_warnings)),
            "issues": sorted({issue for step in steps for issue in step.get("issues", [])} | set(coherence_issues)),
        }

    def _editorial_coherence(self, steps: list[dict[str, Any]]) -> dict[str, Any]:
        if self.contract.get("gates", {}).get("editorial_coherence", {}).get("enabled") is not True:
            return {"status": "disabled", "warnings": [], "issues": [], "human_review_required": False}
        curadoria_step = next((step for step in steps if step.get("step") == "curadoria_dry_run"), None)
        if not curadoria_step or not curadoria_step.get("target_path"):
            return {"status": "not_evaluated", "reason": "curadoria_step_ausente", "warnings": [], "issues": [], "human_review_required": False}
        target_path = self.root / str(curadoria_step["target_path"])
        if not target_path.exists():
            return {"status": "not_evaluated", "reason": "curadoria_artifact_ausente", "warnings": [], "issues": [], "human_review_required": False}
        return self.coherence_gate.evaluate_path(target_path)

    def _batch_issues(self, item_results: list[dict[str, Any]], frozen_states: list[FrozenSourceState]) -> list[str]:
        issues: list[str] = []
        if self.contract.get("gates", {}).get("fail_if_frozen_source_changes") is True:
            for state in frozen_states:
                if not state.unchanged:
                    issues.append(f"frozen_source_changed:{state.path}")
        if len(item_results) < int(self.contract.get("expected_new_items_min", 1)):
            issues.append("multi_item_count_below_min")
        editorias = {str(item.get("editoria", "")) for item in item_results}
        if len(editorias) < int(self.contract.get("required_editorias_min", 1)):
            issues.append("multi_item_editorias_below_min")
        for item in item_results:
            if not item.get("ok"):
                issues.append(f"item_failed:{item.get('item_id')}")
        return sorted(set(issues))

    def _frozen_hashes(self) -> dict[str, str]:
        hashes: dict[str, str] = {}
        for rel_path in self.contract.get("frozen_sources", []):
            path = self.root / rel_path
            hashes[rel_path] = self._sha256(path)
        return hashes

    @staticmethod
    def _sha256(path: Path) -> str:
        return hashlib.sha256(path.read_bytes()).hexdigest()

    @staticmethod
    def _now() -> str:
        return datetime.now(timezone.utc).isoformat()
