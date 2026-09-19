from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .feedback import V4EditorFeedbackStore
from .loader import DirectiveLoader
from .llm_orchestrator import LLMSelection, V4LLMOrchestrator
from .pricing import V4Pricing


DEFAULT_MODEL_ROUTER_CONTRACT = "diretrizes/v4_model_router_v1.json"


@dataclass(frozen=True)
class ModelCandidateScore:
    selection: LLMSelection
    samples: int
    avg_score: float | None
    expected_cost_usd: float
    quality_component: float
    cost_component: float
    route_component: float
    final_score: float
    mode: str
    reason: str

    def as_dict(self) -> dict[str, Any]:
        return {
            "provider": self.selection.provider,
            "model": self.selection.model,
            "tier": self.selection.tier,
            "route_context": self.selection.route_context,
            "route_tiers": self.selection.route_tiers,
            "samples": self.samples,
            "avg_score": self.avg_score,
            "expected_cost_usd": self.expected_cost_usd,
            "quality_component": self.quality_component,
            "cost_component": self.cost_component,
            "route_component": self.route_component,
            "final_score": self.final_score,
            "mode": self.mode,
            "reason": self.reason,
        }


@dataclass(frozen=True)
class ModelRecommendation:
    selected: ModelCandidateScore
    candidates: list[ModelCandidateScore]
    editoria: str
    funcao: str
    contract_version: str

    def as_dict(self) -> dict[str, Any]:
        return {
            "editoria": self.editoria,
            "funcao": self.funcao,
            "contract_version": self.contract_version,
            "selection": self.selected.as_dict(),
            "candidates": [candidate.as_dict() for candidate in self.candidates],
        }


class V4ModelRouter:
    """Escolhe modelo por contrato externo, feedback do editor e custo estimado."""

    def __init__(self, root: str | Path = ".", contract_path: str = DEFAULT_MODEL_ROUTER_CONTRACT) -> None:
        self.loader = DirectiveLoader(root)
        self.root = self.loader.root
        self.contract_path = contract_path
        self.contract = self.loader.read_json(contract_path)
        self.orchestrator = V4LLMOrchestrator(self.root)
        self.feedback = V4EditorFeedbackStore(self.root)
        self.pricing = V4Pricing(self.root)

    def recommend(
        self,
        editoria: str,
        funcao: str,
        idempotency_key: str,
        exclude_provider: str | None = None,
    ) -> ModelRecommendation:
        del idempotency_key  # A recomendacao e deterministica por dados externos, nao por rotacao.
        candidates = self.orchestrator.valid_candidates(editoria, funcao)
        if exclude_provider:
            candidates = [candidate for candidate in candidates if candidate.provider != exclude_provider]
        if not candidates:
            raise RuntimeError(f"Nenhum candidato V4 valido para {editoria}/{funcao}")

        feedback_index = self._feedback_index()
        expected_costs = [self._expected_cost(candidate.model, funcao) for candidate in candidates]
        positive_costs = [cost for cost in expected_costs if cost > 0]
        min_cost = min(positive_costs) if positive_costs else 0.0
        scored: list[ModelCandidateScore] = []

        for index, candidate in enumerate(candidates):
            feedback_operation = self.contract.get("feedback_operation_map", {}).get(funcao, funcao)
            feedback = feedback_index.get((editoria, candidate.provider, candidate.model, feedback_operation), {})
            samples = int(feedback.get("samples", 0) or 0)
            avg_score = feedback.get("avg_score")
            expected_cost = expected_costs[index]
            scored.append(
                self._score_candidate(
                    candidate=candidate,
                    index=index,
                    total=len(candidates),
                    samples=samples,
                    avg_score=float(avg_score) if avg_score is not None else None,
                    expected_cost=expected_cost,
                    min_cost=min_cost,
                )
            )

        scored.sort(key=lambda item: (-item.final_score, -item.quality_component, item.expected_cost_usd, item.route_component))
        return ModelRecommendation(
            selected=scored[0],
            candidates=scored,
            editoria=editoria,
            funcao=funcao,
            contract_version=str(self.contract.get("_version", "unknown")),
        )

    def select(
        self,
        editoria: str,
        funcao: str,
        idempotency_key: str,
        exclude_provider: str | None = None,
    ) -> LLMSelection:
        recommendation = self.recommend(editoria, funcao, idempotency_key, exclude_provider)
        selected = recommendation.selected.selection
        return LLMSelection(
            provider=selected.provider,
            tier=selected.tier,
            model=selected.model,
            route_context=selected.route_context,
            route_tiers=selected.route_tiers,
            quality=selected.quality,
            strategy="quality_cost_router",
            reason=recommendation.selected.reason,
        )

    def _score_candidate(
        self,
        candidate: LLMSelection,
        index: int,
        total: int,
        samples: int,
        avg_score: float | None,
        expected_cost: float,
        min_cost: float,
    ) -> ModelCandidateScore:
        recommendation = self.contract["recommendation"]
        min_samples = int(recommendation["min_samples_for_feedback_priority"])
        weights = recommendation["weights"]
        mode = "feedback_priority" if samples >= min_samples else "exploration"
        if avg_score is not None:
            quality_component = max(0.0, min(1.0, avg_score / 5.0))
        else:
            quality_component = max(0.0, min(1.0, float(candidate.quality) / 5.0))
        cost_component = round(min_cost / expected_cost, 6) if min_cost > 0 and expected_cost > 0 else 0.0
        route_component = 1.0 if total <= 1 else round(1.0 - (index / (total - 1)), 6)
        final_score = round(
            float(weights["quality"]) * quality_component
            + float(weights["cost_efficiency"]) * cost_component
            + float(weights["route_order"]) * route_component,
            6,
        )
        reason = (
            f"{mode}: qualidade={quality_component:.3f}, custo={cost_component:.3f}, "
            f"rota={route_component:.3f}, samples={samples}"
        )
        return ModelCandidateScore(
            selection=candidate,
            samples=samples,
            avg_score=avg_score,
            expected_cost_usd=expected_cost,
            quality_component=round(quality_component, 6),
            cost_component=cost_component,
            route_component=route_component,
            final_score=final_score,
            mode=mode,
            reason=reason,
        )

    def _expected_cost(self, model: str, funcao: str) -> float:
        expected = self.contract.get("expected_tokens", {}).get(funcao, {})
        tokens_in = int(expected.get("tokens_in", 1000))
        tokens_out = int(expected.get("tokens_out", 500))
        estimate = self.pricing.estimate(model, "x" * (tokens_in * 4), "x" * (tokens_out * 4))
        return estimate.cost_usd_estimated

    def _feedback_index(self) -> dict[tuple[str, str, str, str], dict[str, Any]]:
        return {
            (item["vertical"], item["provider"], item["model"], item["operation"]): item
            for item in self.feedback.ranking()
        }
