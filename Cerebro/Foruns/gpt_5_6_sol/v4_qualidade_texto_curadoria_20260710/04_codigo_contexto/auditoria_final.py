from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .loader import DirectiveLoader


DEFAULT_FINAL_AUDIT_CONTRACT = "contratos/v4_auditoria_final_v1.json"


class V4FinalAuditAgent:
    """Auditoria final V4 local: consolida revisao e fact-check antes da camada auditada."""

    def __init__(self, root: str | Path = ".", contract_path: str = DEFAULT_FINAL_AUDIT_CONTRACT) -> None:
        self.loader = DirectiveLoader(root)
        self.root = self.loader.root
        self.contract_path = contract_path
        self.contract = self.loader.read_json(contract_path)

    def audit(self, producao: dict[str, Any], execute: bool = False) -> dict[str, Any]:
        issues = self.validate(producao)
        payload = dict(producao)
        payload.update(
            {
                "schema_version_auditoria_final": self.contract.get("_version", "v1"),
                "timestamp_auditoria_final": datetime.now(timezone.utc).isoformat(),
                "wordpress_real": False,
                "manifesto_auditoria_final": {
                    "ok": not issues,
                    "agent": "auditor",
                    "contract": self.contract_path,
                    "curadoria_id": producao.get("curadoria_id"),
                    "revisao_ok": (producao.get("manifesto_revisao") or {}).get("ok") is True,
                    "fact_check_ok": (producao.get("manifesto_fact_check") or {}).get("ok") is True,
                    "publication_real": False,
                    "issues": issues,
                },
                "status": "auditado_final" if not issues else "auditoria_final_bloqueada",
                "issues": list(producao.get("issues", [])) + issues,
            }
        )
        if execute:
            path = self.output_path(payload)
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        return payload

    def validate(self, producao: dict[str, Any]) -> list[str]:
        issues: list[str] = []
        for field_name in self.contract["source"]["required_fields"]:
            if self._missing(producao.get(field_name)):
                issues.append(f"auditoria_final_source_campo_ausente:{field_name}")
        gates = self.contract.get("gates", {})
        if gates.get("block_if_revisao_not_ok") and (producao.get("manifesto_revisao") or {}).get("ok") is not True:
            issues.append("auditoria_final_revisao_nao_aprovada")
        if gates.get("block_if_fact_check_not_ok") and (producao.get("manifesto_fact_check") or {}).get("ok") is not True:
            issues.append("auditoria_final_fact_check_nao_aprovado")
        return issues

    def output_path(self, payload: dict[str, Any]) -> Path:
        item_id = str(payload.get("item_id") or "sem_item")
        suffix = self.contract["output"]["suffix"]
        return self.root / self.contract["output"]["path"] / f"{item_id}.{suffix}.json"

    @staticmethod
    def _missing(value: Any) -> bool:
        return value in (None, "", []) or value == {}
