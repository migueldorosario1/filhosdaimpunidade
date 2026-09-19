from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from .loader import DirectiveLoader
from .llm_validator import FUNC_MAP, LLMTierValidator
from .registry import V4Registry


DEFAULT_ADAPTER_CONTRACT = "diretrizes/v4_llm_adapter_v1.json"
DEFAULT_PROVIDERS = "Projeto Cafezinho Agentes/root/config/llm_providers.json"
DEFAULT_RATINGS = "Projeto Cafezinho Agentes/root/config/llm_ratings.json"


@dataclass(frozen=True)
class LLMCandidate:
    provider: str
    tier: str
    model: str
    env_keys: list[str]
    available_env_keys: list[str]
    quality: int
    status: str

    def as_dict(self) -> dict[str, Any]:
        return {
            "provider": self.provider,
            "tier": self.tier,
            "model": self.model,
            "env_keys": self.env_keys,
            "available_env_keys": self.available_env_keys,
            "quality": self.quality,
            "status": self.status,
        }


@dataclass(frozen=True)
class LLMHealthcheckReport:
    ok: bool
    real_enabled: bool
    allow_real_calls: bool
    network_call: bool
    editoria: str
    funcao: str
    contexto_llm: str
    candidate: LLMCandidate | None
    issues: list[str] = field(default_factory=list)

    def as_dict(self) -> dict[str, Any]:
        return {
            "ok": self.ok,
            "real_enabled": self.real_enabled,
            "allow_real_calls": self.allow_real_calls,
            "network_call": self.network_call,
            "editoria": self.editoria,
            "funcao": self.funcao,
            "contexto_llm": self.contexto_llm,
            "candidate": self.candidate.as_dict() if self.candidate else None,
            "issues": self.issues,
        }


class V4LLMHealthcheck:
    """Healthcheck local para modo real V4, sem chamada de rede."""

    def __init__(
        self,
        root: str | Path = ".",
        adapter_contract: str = DEFAULT_ADAPTER_CONTRACT,
        providers_path: str = DEFAULT_PROVIDERS,
        ratings_path: str = DEFAULT_RATINGS,
    ) -> None:
        self.loader = DirectiveLoader(root)
        self.root = self.loader.root
        self.adapter_contract = self.loader.read_json(adapter_contract)
        self.registry = V4Registry(self.root)
        self.validator = LLMTierValidator(self.root, providers_path=providers_path, ratings_path=ratings_path)
        self.providers = self.loader.read_json(providers_path).get("providers", {})
        self.models = self.loader.read_json(ratings_path).get("modelos", {})

    def check(self, editoria: str, funcao: str = "redacao") -> LLMHealthcheckReport:
        resolved = self.registry.resolve_editoria(editoria)
        contexto = self.registry.resolve_contexto(resolved, funcao)
        validation = self.validator.validate(resolved, funcao)
        issues: list[str] = []
        if not validation.ok:
            issues.extend(issue.message for issue in validation.issues)

        candidate = self._select_candidate(resolved, funcao)
        if candidate is None:
            issues.append("nenhum candidato real valido encontrado nas rotas V4 limpas")
        elif not candidate.available_env_keys:
            issues.append(f"sem env key disponivel para provider {candidate.provider}")

        real = self.adapter_contract.get("real", {})
        real_enabled = real.get("enabled") is True
        allow_real_calls = self.adapter_contract.get("allow_real_calls") is True
        network_call = real.get("healthcheck", {}).get("network_call") is True
        if not real_enabled:
            issues.append("real.enabled=false no contrato do adapter")
        if not allow_real_calls:
            issues.append("allow_real_calls=false no contrato do adapter")
        if network_call:
            issues.append("network_call=true nao e permitido neste healthcheck local")

        ok = bool(candidate and candidate.available_env_keys and real_enabled and allow_real_calls and not network_call and not issues)
        return LLMHealthcheckReport(
            ok=ok,
            real_enabled=real_enabled,
            allow_real_calls=allow_real_calls,
            network_call=network_call,
            editoria=resolved,
            funcao=funcao,
            contexto_llm=contexto,
            candidate=candidate,
            issues=issues,
        )

    def _select_candidate(self, editoria: str, funcao: str) -> LLMCandidate | None:
        contexto = self.registry.resolve_contexto(editoria, funcao)
        canonical_func = FUNC_MAP.get(funcao, funcao)
        quality_floor = self.validator._quality_floor(editoria, funcao)
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
                if model.get("qualidade", 0) < quality_floor:
                    continue
                if canonical_func not in set(model.get("funcoes_permitidas", [])):
                    continue
                env_keys = list(provider.get("env_keys", []))
                available = [key for key in env_keys if os.environ.get(key)]
                return LLMCandidate(
                    provider=provider_name,
                    tier=tier,
                    model=model_name,
                    env_keys=env_keys,
                    available_env_keys=available,
                    quality=int(model.get("qualidade", 0)),
                    status=str(model.get("status")),
                )
        return None
