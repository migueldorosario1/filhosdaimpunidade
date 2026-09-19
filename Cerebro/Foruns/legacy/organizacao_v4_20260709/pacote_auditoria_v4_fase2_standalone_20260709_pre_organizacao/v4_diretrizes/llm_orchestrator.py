from __future__ import annotations

import hashlib
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .loader import DirectiveLoader
from .llm_validator import FUNC_MAP, LLMTierValidator
from .registry import V4Registry


DEFAULT_ORCHESTRATION_CONTRACT = "diretrizes/v4_orquestracao_llm_v1.json"
DEFAULT_PROVIDERS = "Projeto Cafezinho Agentes/root/config/llm_providers.json"
DEFAULT_RATINGS = "Projeto Cafezinho Agentes/root/config/llm_ratings.json"


@dataclass(frozen=True)
class LLMSelection:
    provider: str
    tier: str
    model: str
    route_context: str
    route_tiers: list[str]
    quality: int
    strategy: str
    reason: str

    def as_dict(self) -> dict[str, Any]:
        return {
            "provider": self.provider,
            "tier": self.tier,
            "model": self.model,
            "route_context": self.route_context,
            "route_tiers": self.route_tiers,
            "quality": self.quality,
            "strategy": self.strategy,
            "reason": self.reason,
        }


class V4LLMOrchestrator:
    """Seleciona modelo V4 por contrato externo, rotacao e validacao local."""

    def __init__(
        self,
        root: str | Path = ".",
        contract_path: str = DEFAULT_ORCHESTRATION_CONTRACT,
        providers_path: str = DEFAULT_PROVIDERS,
        ratings_path: str = DEFAULT_RATINGS,
    ) -> None:
        self.loader = DirectiveLoader(root)
        self.root = self.loader.root
        self.contract = self.loader.read_json(contract_path)
        self.registry = V4Registry(self.root)
        self.validator = LLMTierValidator(self.root, providers_path=providers_path, ratings_path=ratings_path)
        self.providers = self.loader.read_json(providers_path).get("providers", {})
        self.models = self.loader.read_json(ratings_path).get("modelos", {})

    def select(
        self,
        editoria: str,
        funcao: str,
        idempotency_key: str,
        exclude_provider: str | None = None,
    ) -> LLMSelection:
        resolved = self.registry.resolve_editoria(editoria)
        contexto = self.registry.resolve_contexto(resolved, funcao)
        route_tiers = self.registry.get_context_tiers(contexto)
        strategy = self.contract.get("funcoes", {}).get(funcao, {}).get(
            "selection_strategy",
            "rotate_valid_by_idempotency",
        )
        candidates = self.valid_candidates(resolved, funcao)
        if exclude_provider:
            candidates = [candidate for candidate in candidates if candidate.provider != exclude_provider]
        if not candidates:
            raise RuntimeError(f"Nenhum candidato LLM valido para {resolved}/{funcao}")

        index = self._stable_index(idempotency_key, len(candidates)) if strategy == "rotate_valid_by_idempotency" else 0
        selected = candidates[index]
        return LLMSelection(
            provider=selected.provider,
            tier=selected.tier,
            model=selected.model,
            route_context=contexto,
            route_tiers=route_tiers,
            quality=selected.quality,
            strategy=strategy,
            reason=f"selecionado por {strategy}; exclude_provider={exclude_provider!r}",
        )

    def valid_candidates(self, editoria: str, funcao: str) -> list[LLMSelection]:
        resolved = self.registry.resolve_editoria(editoria)
        contexto = self.registry.resolve_contexto(resolved, funcao)
        canonical_func = FUNC_MAP.get(funcao, funcao)
        quality_floor = self.validator._quality_floor(resolved, funcao)
        route_tiers = self.registry.get_context_tiers(contexto)
        candidates: list[LLMSelection] = []

        for entry in self.registry.get_context_entries(contexto):
            tier = entry["tier"]
            provider_name, provider_tier = self.validator._split_tier(tier)
            provider = self.providers.get(provider_name)
            if not provider or provider.get("enabled") is not True:
                continue
            model_names = entry.get("models") or provider.get("fallback_models", {}).get(provider_tier, [])
            for model_name in model_names:
                model = self.models.get(model_name)
                if not model:
                    continue
                if model.get("status") != "ativo":
                    continue
                if model.get("provider") != provider_name:
                    continue
                quality = model.get("qualidade", 0)
                if not isinstance(quality, int) or quality < quality_floor:
                    continue
                if canonical_func not in set(model.get("funcoes_permitidas", [])):
                    continue
                candidates.append(
                    LLMSelection(
                        provider=provider_name,
                        tier=tier,
                        model=model_name,
                        route_context=contexto,
                        route_tiers=route_tiers,
                        quality=quality,
                        strategy="candidate",
                        reason="candidato valido pelas rotas limpas e ratings locais",
                    )
                )
        return candidates

    @staticmethod
    def _stable_index(value: str, size: int) -> int:
        digest = hashlib.sha256(value.encode("utf-8")).hexdigest()
        return int(digest[:8], 16) % size
