from __future__ import annotations

import re
import unicodedata
from pathlib import Path
from typing import Any

from .loader import DirectiveLoader


DEFAULT_EDITORIAL_COHERENCE_CONTRACT = "contratos/v4_editoria_coerencia_v1.json"


class V4EditorialCoherenceGate:
    """Gate lab de coerencia tese x editoria, sem tentar substituir revisao editorial."""

    def __init__(self, root: str | Path = ".", contract_path: str = DEFAULT_EDITORIAL_COHERENCE_CONTRACT) -> None:
        self.loader = DirectiveLoader(root)
        self.root = self.loader.root
        self.contract_path = contract_path
        self.contract = self.loader.read_json(contract_path)

    def evaluate(self, curadoria: dict[str, Any]) -> dict[str, Any]:
        editoria = str(curadoria.get("editoria", "")).strip()
        config = self.contract.get("editorias", {}).get(editoria, self.contract.get("default", {}))
        if config.get("enabled") is not True:
            return {
                "schema_version": self.contract.get("_version", "v1"),
                "status": "not_applicable",
                "editoria": editoria,
                "warnings": [],
                "issues": [],
                "human_review_required": False,
            }

        chosen = self._chosen_tese(curadoria)
        tese = str(chosen.get("tese", ""))
        claim = self._claim_segment(tese)
        if not claim:
            warning_id = str(self.contract.get("missing_tese_warning_id", "tese_ausente"))
            return {
                "schema_version": self.contract.get("_version", "v1"),
                "status": "warning",
                "editoria": editoria,
                "claim_text": "",
                "positive_claim_hits": [],
                "negative_template_hits": [],
                "warnings": [warning_id],
                "issues": [],
                "human_review_required": config.get("human_review_required_when_warning") is True,
                "gate_kind": "keyword_first_line_warning",
                "contract": self.contract_path,
            }
        negative_text = " ".join(
            [
                tese,
                str(chosen.get("quem_ganha", "")),
                str(chosen.get("quem_perde", "")),
                str((curadoria.get("consequencia_material") or {}).get("descricao", "")),
            ]
        )
        positive_hits = self._hits(claim, config.get("positive_claim_terms", []))
        negative_hits = self._hits(negative_text, config.get("negative_template_terms", []))
        min_positive = int(config.get("min_positive_claim_hits", 1))
        warnings: list[str] = []
        issues: list[str] = []

        if negative_hits and len(positive_hits) < min_positive:
            warning_id = str(config.get("warning_id", "tese_desalinhada_com_editoria"))
            if config.get("severity") == "issue":
                issues.append(warning_id)
            else:
                warnings.append(warning_id)

        human_review_required = bool(warnings or issues) and config.get("human_review_required_when_warning") is True
        status = "ok"
        if issues:
            status = "issue"
        elif warnings:
            status = "warning"
        return {
            "schema_version": self.contract.get("_version", "v1"),
            "status": status,
            "editoria": editoria,
            "claim_text": claim,
            "positive_claim_hits": positive_hits,
            "negative_template_hits": negative_hits,
            "warnings": warnings,
            "issues": issues,
            "human_review_required": human_review_required,
            "gate_kind": "keyword_first_line_warning",
            "contract": self.contract_path,
        }

    def evaluate_path(self, path: str | Path) -> dict[str, Any]:
        payload = self.loader.read_json(str(path) if not isinstance(path, Path) else str(path.relative_to(self.root)))
        return self.evaluate(payload)

    @staticmethod
    def _chosen_tese(curadoria: dict[str, Any]) -> dict[str, Any]:
        chosen_idx = curadoria.get("tese_escolhida_idx")
        for item in curadoria.get("teses_candidatas") or []:
            if item.get("idx") == chosen_idx or item.get("status") == "escolhida":
                return item
        return {}

    @staticmethod
    def _claim_segment(tese: str) -> str:
        match = re.search(r"revela-se que\s+(.+)$", tese, flags=re.IGNORECASE)
        if match:
            return match.group(1).strip()
        return tese.strip()

    @classmethod
    def _hits(cls, text: str, terms: list[Any]) -> list[str]:
        normalized_text = cls._normalize(text)
        hits: list[str] = []
        for raw_term in terms:
            term = cls._normalize(str(raw_term))
            if not term:
                continue
            if cls._term_present(normalized_text, term):
                hits.append(str(raw_term))
        return sorted(set(hits))

    @staticmethod
    def _term_present(text: str, term: str) -> bool:
        if " " in term:
            return term in text
        return bool(re.search(rf"\b{re.escape(term)}\b", text))

    @staticmethod
    def _normalize(text: str) -> str:
        decomposed = unicodedata.normalize("NFKD", text.lower())
        ascii_text = "".join(char for char in decomposed if not unicodedata.combining(char))
        return re.sub(r"\s+", " ", ascii_text).strip()
