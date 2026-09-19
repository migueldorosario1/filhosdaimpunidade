from __future__ import annotations

import hashlib
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .composer import ContractComposer
from .loader import DirectiveLoader
from .llm_decisions import LLMRouterDecision, V4LLMDecisionStore
from .llm_healthcheck import V4LLMHealthcheck
from .llm_orchestrator import LLMSelection, V4LLMOrchestrator
from .llm_validator import LLMTierValidator
from .model_router import V4ModelRouter
from .pricing import V4Pricing
from .schema import EditorialContract


DEFAULT_ADAPTER_CONTRACT = "diretrizes/v4_llm_adapter_v1.json"


@dataclass(frozen=True)
class LLMRequest:
    editoria: str
    funcao: str
    titulo: str
    conteudo: str
    idempotency_key: str
    previous_provider: str | None = None


@dataclass(frozen=True)
class LLMResponse:
    mode: str
    provider: str
    model: str
    content: str
    prompt_hash: str
    route_context: str
    route_tiers: list[str]
    selected_tier: str
    selection_strategy: str
    selection_reason: str
    tokens_in: int = 0
    tokens_out: int = 0
    duration_ms_llm: int = 0
    cost_usd_estimated: float = 0.0
    pricing_table_version: str = "pending"
    error_class: str | None = None

    def as_dict(self) -> dict[str, Any]:
        return {
            "mode": self.mode,
            "provider": self.provider,
            "model": self.model,
            "content": self.content,
            "prompt_hash": self.prompt_hash,
            "route_context": self.route_context,
            "route_tiers": self.route_tiers,
            "selected_tier": self.selected_tier,
            "selection_strategy": self.selection_strategy,
            "selection_reason": self.selection_reason,
            "tokens_in": self.tokens_in,
            "tokens_out": self.tokens_out,
            "duration_ms_llm": self.duration_ms_llm,
            "cost_usd_estimated": self.cost_usd_estimated,
            "pricing_table_version": self.pricing_table_version,
            "error_class": self.error_class,
        }


class V4LLMAdapter:
    """Adaptador LLM V4 sem modelo nem diretriz hardcoded."""

    def __init__(self, root: str | Path = ".", contract_path: str = DEFAULT_ADAPTER_CONTRACT) -> None:
        self.loader = DirectiveLoader(root)
        self.root = self.loader.root
        self.contract_path = contract_path
        self.contract = self.loader.read_json(contract_path)
        self.composer = ContractComposer(self.root)
        self.validator = LLMTierValidator(self.root)
        self.healthcheck = V4LLMHealthcheck(self.root, adapter_contract=contract_path)
        self.orchestrator = V4LLMOrchestrator(self.root)
        self.model_router = V4ModelRouter(self.root)
        self.decision_store = V4LLMDecisionStore(self.root)
        self.pricing = V4Pricing(self.root)

    def generate(self, request: LLMRequest, mode: str | None = None) -> LLMResponse:
        selected_mode = mode or self.contract.get("mode_default", "mock")
        editorial_contract = self.composer.compose(request.editoria, request.funcao)
        validation = self.validator.validate(request.editoria, request.funcao)
        if not validation.ok:
            issues = "; ".join(issue.message for issue in validation.issues)
            raise RuntimeError(f"Rotas LLM V4 invalidas: {issues}")

        prompt_hash = self._prompt_hash(editorial_contract, request)
        recommendation = self.model_router.recommend(
            request.editoria,
            request.funcao,
            request.idempotency_key,
            exclude_provider=request.previous_provider,
        )
        selection = recommendation.selected.selection
        decision_result = self.decision_store.record(
            LLMRouterDecision(
                editoria=request.editoria,
                funcao=request.funcao,
                idempotency_key=request.idempotency_key,
                prompt_hash=prompt_hash,
                selected_provider=selection.provider,
                selected_model=selection.model,
                selected_tier=selection.tier,
                selection_strategy="quality_cost_router",
                selection_reason=recommendation.selected.reason,
                candidate_count=len(recommendation.candidates),
                mode=recommendation.selected.mode,
                expected_cost_usd=recommendation.selected.expected_cost_usd,
            ),
            execute=True,
        )
        if not decision_result["ok"]:
            raise RuntimeError(f"Decisao LLM V4 nao auditada: {decision_result.get('errors', [])}")
        if selected_mode == "mock":
            started = datetime.now(timezone.utc)
            content = self._mock_content(request, editorial_contract, selection)
            duration_ms = int((datetime.now(timezone.utc) - started).total_seconds() * 1000)
            cost = self.pricing.estimate(selection.model, request.conteudo, content)
            return LLMResponse(
                mode="mock",
                provider=selection.provider,
                model=selection.model,
                content=content,
                prompt_hash=prompt_hash,
                route_context=selection.route_context,
                route_tiers=selection.route_tiers,
                selected_tier=selection.tier,
                selection_strategy="quality_cost_router",
                selection_reason=recommendation.selected.reason,
                tokens_in=cost.tokens_in,
                tokens_out=cost.tokens_out,
                duration_ms_llm=duration_ms,
                cost_usd_estimated=cost.cost_usd_estimated,
                pricing_table_version=cost.pricing_table_version,
            )

        if selected_mode == "real":
            health = self.healthcheck.check(request.editoria, request.funcao)
            if not health.ok:
                raise RuntimeError(f"Modo real V4 bloqueado: {'; '.join(health.issues)}")
            raise NotImplementedError("Modo real validado localmente, mas chamada externa ainda nao foi implementada.")

        raise NotImplementedError("Modo real ainda nao implementado neste bloco.")

    @staticmethod
    def _prompt_hash(contract: EditorialContract, request: LLMRequest) -> str:
        raw = "\n".join(
            [
                contract.nucleo.sha256,
                contract.diretriz.sha256,
                request.editoria,
                request.funcao,
                request.titulo,
                request.conteudo,
                request.idempotency_key,
            ]
        )
        return hashlib.sha256(raw.encode("utf-8")).hexdigest()

    @staticmethod
    def _mock_content(request: LLMRequest, contract: EditorialContract, selection: LLMSelection) -> str:
        return (
            f"[MOCK V4/{selection.provider}/{selection.model}/{contract.editoria}/{request.funcao}] "
            f"{request.titulo}. "
            f"Texto tecnico simulado a partir de material auditado: {request.conteudo}"
        )
