from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .loader import DirectiveLoader


DEFAULT_REVIEW_CONTRACT = "contratos/v4_revisao_v1.json"


class V4ReviewAgent:
    """Revisor V4 local: checa promessa, curadoria e cheiro de prompt sem reescrever."""

    def __init__(self, root: str | Path = ".", contract_path: str = DEFAULT_REVIEW_CONTRACT) -> None:
        self.loader = DirectiveLoader(root)
        self.root = self.loader.root
        self.contract_path = contract_path
        self.contract = self.loader.read_json(contract_path)

    def review(self, producao: dict[str, Any], execute: bool = False) -> dict[str, Any]:
        text = self._text(producao)
        issues = self.validate(producao, text)
        payload = dict(producao)
        payload.update(
            {
                "schema_version_revisao": self.contract.get("_version", "v1"),
                "timestamp_revisao": datetime.now(timezone.utc).isoformat(),
                "texto_revisado": text,
                "manifesto_revisao": {
                    "ok": not issues,
                    "agent": "revisor",
                    "contract": self.contract_path,
                    "curadoria_id": producao.get("curadoria_id"),
                    "promessa_ao_leitor": producao.get("promessa_ao_leitor"),
                    "issues": issues,
                },
                "status": "revisao_aprovada" if not issues else "revisao_bloqueada",
                "issues": list(producao.get("issues", [])) + issues,
            }
        )
        if execute:
            path = self.output_path(payload)
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        return payload

    def validate(self, producao: dict[str, Any], text: str | None = None) -> list[str]:
        issues: list[str] = []
        for field_name in self.contract["source"]["required_fields"]:
            if self._missing(producao.get(field_name)):
                issues.append(f"revisao_source_campo_ausente:{field_name}")
        text_value = text if text is not None else self._text(producao)
        if self._missing(text_value):
            issues.append("revisao_texto_ausente")
        min_chars = int(self.contract.get("gates", {}).get("min_text_chars", 0) or 0)
        if min_chars and len(text_value or "") < min_chars:
            issues.append(f"revisao_texto_curto:{len(text_value or '')}<{min_chars}")
        if self.contract.get("gates", {}).get("block_meta_language"):
            lowered = (text_value or "").lower()
            for fragment in self.contract.get("forbidden_text_fragments", []):
                if str(fragment).lower() in lowered:
                    issues.append(f"revisao_meta_linguagem:{fragment}")
        return issues

    def output_path(self, payload: dict[str, Any]) -> Path:
        item_id = str(payload.get("item_id") or "sem_item")
        suffix = self.contract["output"]["suffix"]
        return self.root / self.contract["output"]["path"] / f"{item_id}.{suffix}.json"

    def _text(self, payload: dict[str, Any]) -> str:
        for field_name in self.contract["source"].get("text_fields_any", []):
            value = payload.get(field_name)
            if isinstance(value, str) and value.strip():
                return value.strip()
        return ""

    @staticmethod
    def _missing(value: Any) -> bool:
        return value in (None, "", []) or value == {}
