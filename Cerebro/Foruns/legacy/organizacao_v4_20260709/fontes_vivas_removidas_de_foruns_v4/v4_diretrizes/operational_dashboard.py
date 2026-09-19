from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .loader import DirectiveLoader


DEFAULT_OPERATIONAL_DASHBOARD_CONTRACT = "diretrizes/v4_operational_dashboard_v1.json"


class V4OperationalDashboard:
    """Painel operacional local consolidado do V4."""

    def __init__(self, root: str | Path = ".", contract_path: str = DEFAULT_OPERATIONAL_DASHBOARD_CONTRACT) -> None:
        self.loader = DirectiveLoader(root)
        self.root = self.loader.root
        self.contract = self.loader.read_json(contract_path)

    def build(self, execute: bool = False) -> dict[str, Any]:
        report = {
            "schema_version": self.contract.get("_version", "v1"),
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "layers": self._layer_counts(),
            "telemetry": self._telemetry_summary(),
            "media": self._media_summary(),
            "wordpress": self._wordpress_summary(),
            "memory": self._memory_summary(),
            "health": [],
        }
        report["health"] = self._health(report)
        paths = self._paths()
        if execute:
            paths["json"].parent.mkdir(parents=True, exist_ok=True)
            paths["json"].write_text(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
            paths["markdown"].write_text(self.to_markdown(report), encoding="utf-8")
        return {
            "ok": True,
            "mode": "written" if execute else "dry_run",
            "json_path": str(paths["json"].relative_to(self.root)),
            "markdown_path": str(paths["markdown"].relative_to(self.root)),
            "report": report,
        }

    def to_markdown(self, report: dict[str, Any]) -> str:
        lines = ["# V4 Operational Dashboard", "", f"Gerado em: {report['generated_at']}", ""]
        lines.extend(["## Camadas", ""])
        for layer, count in report["layers"].items():
            lines.append(f"- {layer}: {count}")
        lines.extend(["", "## Telemetria", ""])
        for key, value in report["telemetry"].items():
            lines.append(f"- {key}: {value}")
        lines.extend(["", "## Midia", ""])
        for key, value in report["media"].items():
            lines.append(f"- {key}: {value}")
        lines.extend(["", "## WordPress", ""])
        for key, value in report["wordpress"].items():
            lines.append(f"- {key}: {value}")
        lines.extend(["", "## Saude", ""])
        if report["health"]:
            for item in report["health"]:
                lines.append(f"- {item['severity']}: {item['message']}")
        else:
            lines.append("- info: sem alertas")
        return "\n".join(lines) + "\n"

    def _layer_counts(self) -> dict[str, int]:
        base = self.root / "v4_data"
        return {
            path.name: len([item for item in path.glob("*.json") if item.is_file()])
            for path in sorted(base.iterdir())
            if path.is_dir()
        } if base.exists() else {}

    def _telemetry_summary(self) -> dict[str, int]:
        receipts = self._read_glob("agent_data/v4/receipts/*.jsonl")
        recomputed = self._read_glob("agent_data/v4/receipts/recomputed/*.jsonl")
        decisions = self._read_glob("agent_data/v4/llm_decisions/*.jsonl")
        return {
            "receipts": len(receipts),
            "recomputed_costs": len(recomputed),
            "llm_decisions": len(decisions),
        }

    def _media_summary(self) -> dict[str, int]:
        audited = self._read_glob("agent_data/v4/media/audited/*.jsonl")
        mappings = self._read_glob("agent_data/v4/media/wp_mappings/*.jsonl")
        mapped_ids = {item.get("image_id") for item in mappings}
        return {
            "audited": len(audited),
            "wp_mappings": len(mappings),
            "audited_without_wp_mapping": len([item for item in audited if item.get("image_id") not in mapped_ids]),
        }

    def _wordpress_summary(self) -> dict[str, int]:
        attempts = self._read_glob("agent_data/v4/publication/*.jsonl")
        return {
            "attempts": len(attempts),
            "dry_run": len([item for item in attempts if item.get("outcome") == "dry_run"]),
            "blocked": len([item for item in attempts if str(item.get("outcome", "")).startswith("blocked")]),
            "posted": len([item for item in attempts if item.get("outcome") == "posted"]),
        }

    def _memory_summary(self) -> dict[str, int]:
        events = self._read_jsonl(self.root / "v4_memoria/eventos.jsonl")
        return {"events": len(events)}

    def _health(self, report: dict[str, Any]) -> list[dict[str, str]]:
        health: list[dict[str, str]] = []
        if report["wordpress"]["blocked"] > int(self.contract["health_rules"]["wordpress_blocked_attempts_warning_gt"]):
            health.append({"severity": "warning", "message": f"tentativas WordPress bloqueadas: {report['wordpress']['blocked']}"})
        if report["media"]["audited_without_wp_mapping"] > 0:
            health.append({"severity": "warning", "message": f"midias auditadas sem wp_media_id: {report['media']['audited_without_wp_mapping']}"})
        return health

    def _paths(self) -> dict[str, Path]:
        output = self.contract["outputs"]
        base = self.root / output["dir"]
        return {"json": base / output["json"], "markdown": base / output["markdown"]}

    def _read_glob(self, pattern: str) -> list[dict[str, Any]]:
        records: list[dict[str, Any]] = []
        for path in sorted(self.root.glob(pattern)):
            records.extend(self._read_jsonl(path))
        return records

    @staticmethod
    def _read_jsonl(path: Path) -> list[dict[str, Any]]:
        if not path.exists():
            return []
        return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
