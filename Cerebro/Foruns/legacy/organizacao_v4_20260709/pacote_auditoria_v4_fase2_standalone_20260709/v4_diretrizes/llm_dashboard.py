from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .feedback import V4EditorFeedbackStore
from .loader import DirectiveLoader


DEFAULT_LLM_DASHBOARD_CONTRACT = "diretrizes/v4_llm_dashboard_v1.json"


@dataclass(frozen=True)
class LLMReportPaths:
    json_path: Path
    markdown_path: Path


class V4LLMDashboard:
    """Painel local V4 para comparar qualidade, custo, recibos e decisoes LLM."""

    def __init__(self, root: str | Path = ".", contract_path: str = DEFAULT_LLM_DASHBOARD_CONTRACT) -> None:
        self.loader = DirectiveLoader(root)
        self.root = self.loader.root
        self.contract_path = contract_path
        self.contract = self.loader.read_json(contract_path)
        self.feedback = V4EditorFeedbackStore(self.root)

    def build(self, execute: bool = False) -> dict[str, Any]:
        quality_ranking = self.feedback.ranking()
        decisions = self._read_decisions()
        receipts = self._read_receipts_with_recomputed_costs()
        report = {
            "schema_version": self.contract.get("_version", "v1"),
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "summary": self._summary(quality_ranking, decisions, receipts),
            "quality_ranking": quality_ranking,
            "decision_counts": self._decision_counts(decisions),
            "receipt_costs": self._receipt_costs(receipts),
            "open_gaps": self._open_gaps(quality_ranking, decisions, receipts),
        }
        paths = self._paths()
        if execute:
            paths.json_path.parent.mkdir(parents=True, exist_ok=True)
            paths.json_path.write_text(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
            paths.markdown_path.write_text(self.to_markdown(report), encoding="utf-8")
        return {
            "ok": True,
            "mode": "written" if execute else "dry_run",
            "json_path": str(paths.json_path.relative_to(self.root)),
            "markdown_path": str(paths.markdown_path.relative_to(self.root)),
            "report": report,
        }

    def to_markdown(self, report: dict[str, Any]) -> str:
        lines = [
            "# V4 LLM Dashboard",
            "",
            f"Gerado em: {report['generated_at']}",
            "",
            "## Resumo",
            "",
        ]
        for key, value in report["summary"].items():
            lines.append(f"- {key}: {value}")
        lines.extend(["", "## Ranking Qualidade/Custo", ""])
        if report["quality_ranking"]:
            lines.append("| editoria | provider | model | samples | avg_score | avg_cost_usd | score_per_usd |")
            lines.append("| --- | --- | --- | ---: | ---: | ---: | ---: |")
            for item in report["quality_ranking"]:
                lines.append(
                    "| {vertical} | {provider} | {model} | {samples} | {avg_score} | {avg_cost_usd_estimated} | {score_per_usd_estimated} |".format(
                        **item
                    )
                )
        else:
            lines.append("Sem feedback registrado.")
        lines.extend(["", "## Decisoes do Roteador", ""])
        for item in report["decision_counts"]:
            lines.append(
                f"- {item['editoria']}/{item['funcao']} -> {item['provider']}/{item['model']}: {item['count']} decisoes"
            )
        if not report["decision_counts"]:
            lines.append("Sem decisoes registradas.")
        lines.extend(["", "## Custos por Recibo", ""])
        for item in report["receipt_costs"]:
            lines.append(
                f"- {item['vertical']} {item['provider']}/{item['model']}: count={item['count']}, total_usd={item['total_cost_usd_estimated']}"
            )
        if not report["receipt_costs"]:
            lines.append("Sem recibos LLM com custo.")
        lines.extend(["", "## Lacunas", ""])
        for gap in report["open_gaps"]:
            lines.append(f"- {gap}")
        if not report["open_gaps"]:
            lines.append("Sem lacunas abertas.")
        return "\n".join(lines) + "\n"

    def _summary(
        self,
        quality_ranking: list[dict[str, Any]],
        decisions: list[dict[str, Any]],
        receipts: list[dict[str, Any]],
    ) -> dict[str, Any]:
        total_cost = round(sum(float(item.get("cost_usd_estimated", 0.0)) for item in receipts), 8)
        return {
            "models_with_feedback": len(quality_ranking),
            "router_decisions": len(decisions),
            "llm_receipts": len([item for item in receipts if item.get("llm")]),
            "total_cost_usd_estimated": total_cost,
        }

    def _decision_counts(self, decisions: list[dict[str, Any]]) -> list[dict[str, Any]]:
        counts: dict[tuple[str, str, str, str], int] = {}
        for item in decisions:
            key = (
                str(item.get("editoria", "")),
                str(item.get("funcao", "")),
                str(item.get("selected_provider", "")),
                str(item.get("selected_model", "")),
            )
            counts[key] = counts.get(key, 0) + 1
        return [
            {"editoria": key[0], "funcao": key[1], "provider": key[2], "model": key[3], "count": count}
            for key, count in sorted(counts.items())
        ]

    def _receipt_costs(self, receipts: list[dict[str, Any]]) -> list[dict[str, Any]]:
        groups: dict[tuple[str, str, str], dict[str, Any]] = {}
        for item in receipts:
            llm = item.get("llm", {})
            if not llm:
                continue
            key = (str(item.get("vertical", "")), str(llm.get("provider", "")), str(llm.get("model", "")))
            group = groups.setdefault(
                key,
                {
                    "vertical": key[0],
                    "provider": key[1],
                    "model": key[2],
                    "count": 0,
                    "total_cost_usd_estimated": 0.0,
                },
            )
            group["count"] += 1
            group["total_cost_usd_estimated"] += float(item.get("cost_usd_estimated", 0.0))
        return [
            {**item, "total_cost_usd_estimated": round(float(item["total_cost_usd_estimated"]), 8)}
            for item in sorted(groups.values(), key=lambda entry: (entry["vertical"], entry["provider"], entry["model"]))
        ]

    def _open_gaps(
        self,
        quality_ranking: list[dict[str, Any]],
        decisions: list[dict[str, Any]],
        receipts: list[dict[str, Any]],
    ) -> list[str]:
        gaps: list[str] = []
        few_threshold = int(self.contract["open_gap_rules"]["few_feedback_samples_lt"])
        for item in quality_ranking:
            if int(item.get("samples", 0)) < few_threshold:
                gaps.append(
                    f"Poucas amostras de feedback para {item['vertical']} {item['provider']}/{item['model']}: {item['samples']}/{few_threshold}"
                )
        feedback_models = {(item["vertical"], item["provider"], item["model"]) for item in quality_ranking}
        for item in decisions:
            key = (item.get("editoria", ""), item.get("selected_provider", ""), item.get("selected_model", ""))
            if key not in feedback_models:
                gaps.append(f"Decisao sem feedback ainda: {key[0]} {key[1]}/{key[2]}")
        for item in receipts:
            if item.get("llm") and float(item.get("cost_usd_estimated", 0.0)) <= 0:
                llm = item.get("llm", {})
                gaps.append(f"Recibo LLM sem custo positivo: {item.get('item_id', '')} {llm.get('provider', '')}/{llm.get('model', '')}")
        return sorted(set(gaps))

    def _read_decisions(self) -> list[dict[str, Any]]:
        decision_dir = self.root / "agent_data/v4/llm_decisions"
        decisions: list[dict[str, Any]] = []
        for path in sorted(decision_dir.glob("*.jsonl")):
            decisions.extend(self._read_jsonl(path))
        return decisions

    def _read_receipts_with_recomputed_costs(self) -> list[dict[str, Any]]:
        receipt_dir = self.root / "agent_data/v4/receipts"
        receipts: list[dict[str, Any]] = []
        index: dict[tuple[str, str, str], int] = {}
        for path in sorted(receipt_dir.glob("*.jsonl")):
            for receipt in self._read_jsonl(path):
                key = (str(receipt.get("vertical", "")), str(receipt.get("item_id", "")), str(receipt.get("operation", "")))
                index[key] = len(receipts)
                receipts.append(receipt)
        for result in self._read_recomputed_costs():
            if result.get("status") != "recomputed":
                continue
            key = (str(result.get("vertical", "")), str(result.get("item_id", "")), str(result.get("operation", "")))
            if key in index:
                receipts[index[key]] = {
                    **receipts[index[key]],
                    "cost_usd_estimated": result.get("new_cost_usd_estimated", 0.0),
                    "pricing_table_version": result.get("new_pricing_table_version", "pending"),
                }
        return receipts

    def _read_recomputed_costs(self) -> list[dict[str, Any]]:
        recomputed_dir = self.root / "agent_data/v4/receipts/recomputed"
        results: list[dict[str, Any]] = []
        for path in sorted(recomputed_dir.glob("*.jsonl")):
            results.extend(self._read_jsonl(path))
        return results

    def _paths(self) -> LLMReportPaths:
        output = self.contract["outputs"]
        output_dir = self.root / output["dir"]
        return LLMReportPaths(json_path=output_dir / output["json"], markdown_path=output_dir / output["markdown"])

    @staticmethod
    def _read_jsonl(path: Path) -> list[dict[str, Any]]:
        if not path.exists():
            return []
        return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
