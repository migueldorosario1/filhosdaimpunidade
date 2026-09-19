from __future__ import annotations

import json
import fcntl
import os
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .loader import DirectiveLoader


DEFAULT_FEATURED_IMAGE_CONTRACT = "diretrizes/v4_imagem_destacada_v1.json"


@dataclass(frozen=True)
class MediaCandidate:
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
    score: float
    content_type: str = "image/jpeg"
    caption: str = ""
    metadata: dict[str, Any] | None = None

    def as_dict(self) -> dict[str, Any]:
        return {
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
            "score": self.score,
            "content_type": self.content_type,
            "caption": self.caption,
            "metadata": self.metadata or {},
        }


@dataclass(frozen=True)
class MediaEvaluation:
    candidate: MediaCandidate
    ok: bool
    final_score: float
    reason_class: str
    issues: list[str]
    visual_confidence: float
    safe_to_publish: bool

    def as_dict(self) -> dict[str, Any]:
        return {
            "candidate": self.candidate.as_dict(),
            "ok": self.ok,
            "final_score": self.final_score,
            "reason_class": self.reason_class,
            "issues": self.issues,
            "visual_confidence": self.visual_confidence,
            "safe_to_publish": self.safe_to_publish,
        }


class V4FeaturedImageEvaluator:
    """Avaliador tecnico V4 de imagem destacada, sem chamada externa por padrao."""

    def __init__(self, root: str | Path = ".", contract_path: str = DEFAULT_FEATURED_IMAGE_CONTRACT) -> None:
        self.loader = DirectiveLoader(root)
        self.root = self.loader.root
        self.contract_path = contract_path
        self.contract = self.loader.read_json(contract_path)

    def evaluate(
        self,
        candidate: MediaCandidate,
        title: str,
        primary_entity: str,
        requires_person: bool = True,
    ) -> MediaEvaluation:
        issues: list[str] = []
        issues.extend(self._required_field_issues(candidate))
        issues.extend(self._rights_issues(candidate))
        issues.extend(self._deterministic_issues(candidate, requires_person))
        visual = self._mock_visual(candidate, title, primary_entity, requires_person)
        issues.extend(visual["issues"])
        final_score = self._final_score(candidate, visual["confidence"], issues)
        ok = (
            not issues
            and visual["safe_to_publish"] is True
            and final_score >= float(self.contract["selection"]["min_final_score"])
        )
        return MediaEvaluation(
            candidate=candidate,
            ok=ok,
            final_score=final_score,
            reason_class=visual["reason_class"],
            issues=issues,
            visual_confidence=visual["confidence"],
            safe_to_publish=ok,
        )

    def select(
        self,
        candidates: list[MediaCandidate],
        title: str,
        primary_entity: str,
        requires_person: bool = True,
        execute: bool = False,
    ) -> dict[str, Any]:
        evaluations = self.evaluate_candidates(candidates, title, primary_entity, requires_person)
        approved = [item for item in evaluations if item.ok]
        approved.sort(key=self._sort_key)
        selected = approved[0] if approved else None
        payload = {
            "schema_version": self.contract.get("_version", "v1"),
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "title": title,
            "primary_entity": primary_entity,
            "requires_person": requires_person,
            "selected": selected.as_dict() if selected else None,
            "evaluations": [item.as_dict() for item in evaluations],
            "blocked": selected is None and self.contract["failure_policy"]["no_audited_image_blocks_publication"],
        }
        if execute:
            self._write_decision(payload)
        return {"ok": selected is not None, "mode": "written" if execute else "dry_run", "decision": payload}

    def evaluate_candidates(
        self,
        candidates: list[MediaCandidate],
        title: str,
        primary_entity: str,
        requires_person: bool = True,
    ) -> list[MediaEvaluation]:
        return [self.evaluate(candidate, title, primary_entity, requires_person) for candidate in candidates]

    def _required_field_issues(self, candidate: MediaCandidate) -> list[str]:
        payload = candidate.as_dict()
        return [
            f"campo obrigatorio ausente: {field_name}"
            for field_name in self.contract.get("candidate_required_fields", [])
            if payload.get(field_name) in (None, "")
        ]

    def _rights_issues(self, candidate: MediaCandidate) -> list[str]:
        rights = self.contract["rights"]
        issues: list[str] = []
        if candidate.rights_status not in set(rights["accepted_statuses"]):
            issues.append(f"rights_status_inaceitavel:{candidate.rights_status}")
        if rights["credit_required"] and not candidate.credit.strip():
            issues.append("credito_ausente")
        if rights["license_required"] and not candidate.license.strip():
            issues.append("licenca_ausente")
        if rights["source_url_required"] and not candidate.url.strip():
            issues.append("url_ausente")
        return issues

    def _deterministic_issues(self, candidate: MediaCandidate, requires_person: bool) -> list[str]:
        filters = self.contract["deterministic_filters"]
        issues: list[str] = []
        if candidate.width < int(filters["min_width"]):
            issues.append("largura_baixa")
        if candidate.height < int(filters["min_height"]):
            issues.append("altura_baixa")
        ratio = candidate.width / max(1, candidate.height)
        if ratio < float(filters["min_aspect_ratio"]) or ratio > float(filters["max_aspect_ratio"]):
            issues.append("aspect_ratio_ruim")
        lower_url = candidate.url.lower()
        for pattern in filters["reject_url_patterns"]:
            if pattern in lower_url:
                issues.append(f"padrao_url_rejeitado:{pattern}")
        if candidate.content_type in set(filters["reject_content_types"]):
            issues.append(f"content_type_rejeitado:{candidate.content_type}")
        min_score = float(filters["person_min_score"] if requires_person else filters["generic_min_score"])
        if candidate.score < min_score:
            issues.append(f"score_baixo:{candidate.score}")
        return issues

    def _mock_visual(
        self,
        candidate: MediaCandidate,
        title: str,
        primary_entity: str,
        requires_person: bool,
    ) -> dict[str, Any]:
        haystack = self._normalize(" ".join([candidate.entity, candidate.title, candidate.caption, candidate.url]))
        entity = self._normalize(primary_entity)
        title_norm = self._normalize(title)
        issues: list[str] = []
        entity_match = bool(entity and (entity in haystack or entity in title_norm and entity in self._normalize(candidate.entity)))
        if requires_person and not entity_match:
            issues.append("entidade_principal_nao_confirmada")
        visual_confidence = 0.92 if entity_match else 0.35
        reason_class = "person_central" if requires_person and entity_match else "theme_clear"
        if requires_person and not self._looks_like_person_photo(candidate):
            issues.append("foto_pessoa_nao_central_ou_nao_grande")
            visual_confidence = min(visual_confidence, 0.45)
        return {
            "confidence": round(visual_confidence, 3),
            "reason_class": reason_class,
            "safe_to_publish": not issues,
            "issues": issues,
        }

    def _looks_like_person_photo(self, candidate: MediaCandidate) -> bool:
        text = self._normalize(" ".join([candidate.title, candidate.caption, json.dumps(candidate.metadata or {}, ensure_ascii=False)]))
        bad = {"multidao", "plenario", "plenário", "documento", "print", "tv", "logo", "montagem"}
        if any(token in text for token in bad):
            return False
        good = {"retrato", "perfil", "presidente", "ministro", "senador", "deputado", "governador", "foto"}
        return any(token in text for token in good) or bool(candidate.entity.strip())

    def _final_score(self, candidate: MediaCandidate, visual_confidence: float, issues: list[str]) -> float:
        penalty = 12.0 * len(issues)
        score = (candidate.score * 0.65) + (visual_confidence * 100.0 * 0.35) - penalty
        return round(max(0.0, min(100.0, score)), 3)

    def _sort_key(self, evaluation: MediaEvaluation) -> tuple[float, float, int]:
        source_priority = self._source_priority(evaluation.candidate.source)
        return (-evaluation.final_score, -evaluation.visual_confidence, source_priority)

    def _source_priority(self, source: str) -> int:
        preferred = self.contract["selection"]["prefer_sources"]
        return preferred.index(source) if source in preferred else len(preferred)

    def _write_decision(self, payload: dict[str, Any]) -> None:
        decision_dir = self.root / self.contract["stores"]["decision_dir"]
        decision_dir.mkdir(parents=True, exist_ok=True)
        day = datetime.now(timezone.utc).date().isoformat().replace("-", "")
        path = decision_dir / f"featured_image_decisions_{day}.jsonl"
        with path.open("a", encoding="utf-8") as handle:
            fcntl.flock(handle.fileno(), fcntl.LOCK_EX)
            handle.write(json.dumps(payload, ensure_ascii=False, sort_keys=True) + "\n")
            handle.flush()
            os.fsync(handle.fileno())
            fcntl.flock(handle.fileno(), fcntl.LOCK_UN)

    @staticmethod
    def _normalize(text: str) -> str:
        return re.sub(r"\s+", " ", (text or "").strip().lower())
