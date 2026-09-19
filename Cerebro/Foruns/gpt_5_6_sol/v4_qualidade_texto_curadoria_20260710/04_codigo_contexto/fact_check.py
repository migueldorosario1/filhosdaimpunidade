from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .loader import DirectiveLoader


DEFAULT_FACT_CHECK_CONTRACT = "contratos/v4_fact_check_v1.json"


class V4FactCheckAgent:
    """Fact-check V4 local: valida fatos travados, fontes e pendencias declaradas."""

    def __init__(self, root: str | Path = ".", contract_path: str = DEFAULT_FACT_CHECK_CONTRACT) -> None:
        self.loader = DirectiveLoader(root)
        self.root = self.loader.root
        self.contract_path = contract_path
        self.contract = self.loader.read_json(contract_path)

    def check(self, producao: dict[str, Any], execute: bool = False) -> dict[str, Any]:
        issues, warnings = self.validate(producao)
        payload = dict(producao)
        payload.update(
            {
                "schema_version_fact_check": self.contract.get("_version", "v1"),
                "timestamp_fact_check": datetime.now(timezone.utc).isoformat(),
                "manifesto_fact_check": {
                    "ok": not issues,
                    "agent": "fact_checker",
                    "contract": self.contract_path,
                    "check_type": self.contract.get("check_type"),
                    "curadoria_id": producao.get("curadoria_id"),
                    "required_facts": self._required_fact_count(producao),
                    "warnings": warnings,
                    "issues": issues,
                },
                "status": "fact_check_aprovado" if not issues else "fact_check_bloqueado",
                "issues": list(producao.get("issues", [])) + issues,
                "warnings": list(producao.get("warnings", [])) + warnings,
            }
        )
        if execute:
            path = self.output_path(payload)
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        return payload

    def validate(self, producao: dict[str, Any]) -> tuple[list[str], list[str]]:
        issues: list[str] = []
        warnings: list[str] = []
        for field_name in self.contract["source"]["required_fields"]:
            if self._missing(producao.get(field_name)):
                issues.append(f"fact_check_source_campo_ausente:{field_name}")
        facts = producao.get("fatos_travados") or []
        min_required = int(self.contract.get("gates", {}).get("min_required_facts", 0) or 0)
        required_facts = [fact for fact in facts if fact.get("obrigatorio_no_texto") is True]
        if len(required_facts) < min_required:
            issues.append(f"fact_check_fatos_obrigatorios_insuficientes:{len(required_facts)}<{min_required}")
        if self.contract.get("gates", {}).get("required_fact_must_have_source_ref"):
            for fact in required_facts:
                if self._missing(fact.get("fonte_ref")):
                    issues.append(f"fact_check_fato_sem_fonte_ref:{fact.get('idx', 'sem_idx')}")
        if self.contract.get("gates", {}).get("required_fact_must_appear_in_text"):
            text = self._text(producao)
            for fact in required_facts:
                if not self._fact_present(fact, text):
                    issues.append(f"fact_check_fato_obrigatorio_ausente_no_texto:{fact.get('idx', 'sem_idx')}")
        collection = producao.get("collection_request") or {}
        if collection.get("status") in {"recommended", "required"}:
            message = f"fact_check_collection_pendente:{collection.get('required_before', 'sem_estagio')}"
            if self.contract.get("gates", {}).get("block_collection_required_for_publication"):
                issues.append(message)
            elif self.contract.get("gates", {}).get("collection_required_generates_warning"):
                warnings.append(message)
        return issues, warnings

    def output_path(self, payload: dict[str, Any]) -> Path:
        item_id = str(payload.get("item_id") or "sem_item")
        suffix = self.contract["output"]["suffix"]
        return self.root / self.contract["output"]["path"] / f"{item_id}.{suffix}.json"

    @staticmethod
    def _required_fact_count(payload: dict[str, Any]) -> int:
        return sum(1 for fact in payload.get("fatos_travados") or [] if fact.get("obrigatorio_no_texto") is True)

    def _text(self, payload: dict[str, Any]) -> str:
        for field_name in self.contract.get("source", {}).get("text_fields_any", []):
            value = payload.get(field_name)
            if isinstance(value, str) and value.strip():
                return value
        return ""

    def _fact_present(self, fact: dict[str, Any], text: str) -> bool:
        cfg = self.contract.get("text_presence_heuristic", {})
        if cfg.get("enabled") is not True:
            return True
        fact_tokens = set(self._tokens(str(fact.get("fato", ""))))
        text_tokens = set(self._tokens(text))
        if not fact_tokens:
            return False
        numeric_tokens = {token for token in fact_tokens if token.isdigit()}
        if cfg.get("numeric_tokens_must_match") is True and not numeric_tokens.issubset(text_tokens):
            return False
        matches = fact_tokens.intersection(text_tokens)
        min_matched = int(cfg.get("min_matched_tokens", 3) or 3)
        min_ratio = float(cfg.get("min_overlap_ratio", 0.35) or 0.35)
        return len(matches) >= min_matched and (len(matches) / len(fact_tokens)) >= min_ratio

    def _tokens(self, text: str) -> list[str]:
        cfg = self.contract.get("text_presence_heuristic", {})
        min_len = int(cfg.get("min_token_len", 4) or 4)
        stopwords = set(cfg.get("stopwords", []))
        tokens = re.findall(r"[0-9A-Za-zÀ-ÿ]+", text.lower())
        preserve_numeric = cfg.get("numeric_tokens_always_preserved") is True
        return [
            token
            for token in tokens
            if (preserve_numeric and token.isdigit()) or (len(token) >= min_len and token not in stopwords)
        ]

    @staticmethod
    def _missing(value: Any) -> bool:
        return value in (None, "", []) or value == {}
