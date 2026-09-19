from __future__ import annotations

from pathlib import Path
from typing import Any

from .registry import V4Registry
from .schema import LLMValidationIssue, LLMValidationReport


FUNC_MAP = {
    "imagem": "tribunal_visual",
    "repetidor": "redacao",
}


class LLMTierValidator:
    """Valida as rotas LLM externas usadas pelo contrato V4."""

    def __init__(
        self,
        root: str | Path = ".",
        providers_path: str = "Projeto Cafezinho Agentes/root/config/llm_providers.json",
        ratings_path: str = "Projeto Cafezinho Agentes/root/config/llm_ratings.json",
    ) -> None:
        self.registry = V4Registry(root)
        self.loader = self.registry.loader
        self.providers = self.loader.read_json(providers_path).get("providers", {})
        self.ratings = self.loader.read_json(ratings_path)
        self.models = self.ratings.get("modelos", {})
        self.blocked_models = set(self.ratings.get("modelos_bloqueados_globais", []))

    def validate(self, editoria: str, funcao: str = "redacao") -> LLMValidationReport:
        resolved = self.registry.resolve_editoria(editoria)
        contexto = self.registry.resolve_contexto(resolved, funcao)
        entries = self.registry.get_context_entries(contexto)
        qualidade_minima = self._quality_floor(resolved, funcao)
        canonical_func = FUNC_MAP.get(funcao, funcao)

        issues: list[LLMValidationIssue] = []
        for entry in entries:
            tier = entry["tier"]
            provider_name, provider_tier = self._split_tier(tier)
            provider = self.providers.get(provider_name)
            if provider is None:
                issues.append(
                    LLMValidationIssue(
                        severity="error",
                        code="provider_missing",
                        message=f"Tier {tier} aponta para provedor ausente em llm_providers.json.",
                        tier=tier,
                        provider=provider_name,
                    )
                )
                continue

            if provider.get("enabled") is not True:
                issues.append(
                    LLMValidationIssue(
                        severity="error",
                        code="provider_disabled",
                        message=f"Provedor {provider_name} esta desligado para o tier {tier}.",
                        tier=tier,
                        provider=provider_name,
                    )
                )

            explicit_models = entry.get("models")
            fallback_models = explicit_models or provider.get("fallback_models", {}).get(provider_tier)
            if not fallback_models:
                issues.append(
                    LLMValidationIssue(
                        severity="error",
                        code="tier_fallback_missing",
                        message=f"Provedor {provider_name} nao tem fallback_models.{provider_tier}.",
                        tier=tier,
                        provider=provider_name,
                    )
                )
                continue

            tier_has_valid_model = False
            for model_name in fallback_models:
                model = self.models.get(model_name)
                if model is None:
                    issues.append(
                        LLMValidationIssue(
                            severity="error",
                            code="model_missing_rating",
                            message=f"Modelo {model_name} esta no fallback {tier}, mas nao existe em llm_ratings.json.",
                            tier=tier,
                            provider=provider_name,
                            model=model_name,
                        )
                    )
                    continue

                model_issues = self._validate_model(
                    tier=tier,
                    provider=provider_name,
                    model_name=model_name,
                    model=model,
                    funcao=canonical_func,
                    qualidade_minima=qualidade_minima,
                )
                issues.extend(model_issues)
                if not any(issue.severity == "error" for issue in model_issues):
                    tier_has_valid_model = True

            if not tier_has_valid_model:
                issues.append(
                    LLMValidationIssue(
                        severity="error",
                        code="tier_without_valid_model",
                        message=f"Tier {tier} nao tem nenhum modelo plenamente valido para {canonical_func}.",
                        tier=tier,
                        provider=provider_name,
                    )
                )

        return LLMValidationReport(
            editoria=resolved,
            funcao=funcao,
            contexto_llm=contexto,
            qualidade_minima=qualidade_minima,
            issues=issues,
        )

    def _validate_model(
        self,
        tier: str,
        provider: str,
        model_name: str,
        model: dict[str, Any],
        funcao: str,
        qualidade_minima: int,
    ) -> list[LLMValidationIssue]:
        issues: list[LLMValidationIssue] = []
        if model_name in self.blocked_models:
            issues.append(
                LLMValidationIssue(
                    severity="error",
                    code="model_globally_blocked",
                    message=f"Modelo {model_name} esta em modelos_bloqueados_globais.",
                    tier=tier,
                    provider=provider,
                    model=model_name,
                )
            )

        status = model.get("status")
        if status != "ativo":
            issues.append(
                LLMValidationIssue(
                    severity="error",
                    code="model_not_active",
                    message=f"Modelo {model_name} tem status {status!r}; V4 exige status 'ativo'.",
                    tier=tier,
                    provider=provider,
                    model=model_name,
                )
            )

        qualidade = model.get("qualidade", 0)
        if not isinstance(qualidade, int) or qualidade < qualidade_minima:
            issues.append(
                LLMValidationIssue(
                    severity="error",
                    code="model_quality_below_floor",
                    message=(
                        f"Modelo {model_name} tem qualidade {qualidade}; "
                        f"minimo V4 para esta funcao e {qualidade_minima}."
                    ),
                    tier=tier,
                    provider=provider,
                    model=model_name,
                )
            )

        if model.get("provider") != provider:
            issues.append(
                LLMValidationIssue(
                    severity="error",
                    code="model_provider_mismatch",
                    message=f"Modelo {model_name} declara provider {model.get('provider')!r}, nao {provider!r}.",
                    tier=tier,
                    provider=provider,
                    model=model_name,
                )
            )

        funcoes = set(model.get("funcoes_permitidas", []))
        if funcao not in funcoes:
            issues.append(
                LLMValidationIssue(
                    severity="error",
                    code="model_function_not_allowed",
                    message=f"Modelo {model_name} nao permite funcao {funcao}.",
                    tier=tier,
                    provider=provider,
                    model=model_name,
                )
            )

        return issues

    def _quality_floor(self, editoria: str, funcao: str) -> int:
        config = self.registry.get_editoria_config(editoria)
        if config.get("nobre") is False and funcao == "redacao":
            return int(self.registry.mapa.get("funcoes", {}).get("repetidor", {}).get("qualidade_minima", 4))
        return int(self.registry.mapa.get("funcoes", {}).get(funcao, {}).get("qualidade_minima", 5))

    @staticmethod
    def _split_tier(tier: str) -> tuple[str, str]:
        if "_" not in tier:
            return tier, "luxo"
        return tier.rsplit("_", 1)
