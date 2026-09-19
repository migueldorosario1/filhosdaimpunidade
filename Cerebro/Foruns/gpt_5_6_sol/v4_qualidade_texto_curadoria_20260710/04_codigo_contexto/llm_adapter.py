from __future__ import annotations

import hashlib
import os
import time
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


DEFAULT_ADAPTER_CONTRACT = "contratos/v4_llm_adapter_v1.json"


@dataclass(frozen=True)
class LLMRequest:
    editoria: str
    funcao: str
    titulo: str
    conteudo: str
    idempotency_key: str
    previous_provider: str | None = None
    previous_model: str | None = None


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
    temperature: float | None = None
    max_tokens: int | None = None
    thinking_budget: int | None = None
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
            "model_parameters": {
                "temperature": self.temperature,
                "max_tokens": self.max_tokens,
                "thinking_budget": self.thinking_budget,
            },
            "error_class": self.error_class,
        }


class V4LLMRealCallError(RuntimeError):
    """Falha de chamada real com provider/model preservados para fallback auditavel."""

    def __init__(self, provider: str, model: str, message: str) -> None:
        super().__init__(message)
        self.provider = provider
        self.model = model


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
        exclude_providers = self._exclude_providers(request.previous_provider)
        exclude_models = self._exclude_models(request.previous_model)
        recommendation = self.model_router.recommend(
            request.editoria,
            request.funcao,
            request.idempotency_key,
            exclude_provider=None,
        )
        candidates = recommendation.candidates
        if exclude_providers or exclude_models:
            candidates = [
                candidate
                for candidate in candidates
                if candidate.selection.provider not in exclude_providers
                and candidate.selection.model not in exclude_models
            ]
            if not candidates:
                raise RuntimeError(
                    "Nenhum candidato V4 valido apos exclusoes: "
                    f"providers={sorted(exclude_providers)}, models={sorted(exclude_models)}"
                )
        selected_candidate = self._select_candidate(candidates, selected_mode)
        selection = selected_candidate.selection
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
                selection_reason=selected_candidate.reason,
                candidate_count=len(candidates),
                mode=selected_candidate.mode,
                expected_cost_usd=selected_candidate.expected_cost_usd,
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
                selection_reason=selected_candidate.reason,
                tokens_in=cost.tokens_in,
                tokens_out=cost.tokens_out,
                duration_ms_llm=duration_ms,
                cost_usd_estimated=cost.cost_usd_estimated,
                pricing_table_version=cost.pricing_table_version,
                temperature=None,
                max_tokens=None,
                thinking_budget=None,
            )

        if selected_mode == "real":
            health = self.healthcheck.check(request.editoria, request.funcao)
            if not health.ok:
                raise RuntimeError(f"Modo real V4 bloqueado: {'; '.join(health.issues)}")
            started = time.monotonic()
            try:
                content, tokens_in, tokens_out, model_parameters = self._real_content(request, editorial_contract, selection)
            except Exception as exc:  # noqa: BLE001 - fronteira de rede precisa carregar provider/model
                raise V4LLMRealCallError(selection.provider, selection.model, str(exc)) from exc
            duration_ms = int((time.monotonic() - started) * 1000)
            if tokens_in or tokens_out:
                cost = self.pricing.estimate_by_tokens(selection.model, tokens_in, tokens_out)
            else:
                cost = self.pricing.estimate(selection.model, request.conteudo, content)
            return LLMResponse(
                mode="real",
                provider=selection.provider,
                model=selection.model,
                content=content,
                prompt_hash=prompt_hash,
                route_context=selection.route_context,
                route_tiers=selection.route_tiers,
                selected_tier=selection.tier,
                selection_strategy="quality_cost_router",
                selection_reason=selected_candidate.reason,
                tokens_in=tokens_in or cost.tokens_in,
                tokens_out=tokens_out or cost.tokens_out,
                duration_ms_llm=duration_ms,
                cost_usd_estimated=cost.cost_usd_estimated,
                pricing_table_version=cost.pricing_table_version,
                temperature=model_parameters["temperature"],
                max_tokens=model_parameters["max_tokens"],
                thinking_budget=model_parameters["thinking_budget"],
            )

        raise NotImplementedError("Modo real ainda nao implementado neste bloco.")

    def _real_content(
        self,
        request: LLMRequest,
        contract: EditorialContract,
        selection: LLMSelection,
    ) -> tuple[str, int, int, dict[str, int | float]]:
        provider = self.healthcheck.providers.get(selection.provider)
        if not provider:
            raise RuntimeError(f"Provider selecionado ausente no registry: {selection.provider}")
        api_key = self._api_key(provider)
        if not api_key:
            raise RuntimeError(f"Provider selecionado sem env key disponivel: {selection.provider}")
        engine = provider.get("engine")
        system_prompt, user_prompt = self._messages(contract, request)
        max_tokens = int(self.contract.get("real", {}).get("max_tokens", 2200))
        temperature = self._temperature_for_model(selection.model, float(self.contract.get("real", {}).get("temperature", 0.7)))
        thinking_budget = int(self.contract.get("real", {}).get("thinking_budget", 0))
        model_parameters: dict[str, int | float] = {
            "temperature": temperature,
            "max_tokens": max_tokens,
            "thinking_budget": thinking_budget,
        }

        if engine in {"openai_native", "openai_compatible"}:
            content, tokens_in, tokens_out = self._call_openai_like(
                provider=provider,
                api_key=api_key,
                model=selection.model,
                system_prompt=system_prompt,
                user_prompt=user_prompt,
                max_tokens=max_tokens,
                temperature=temperature,
            )
            return content, tokens_in, tokens_out, model_parameters
        if engine == "anthropic_native":
            content, tokens_in, tokens_out = self._call_anthropic(
                api_key=api_key,
                model=selection.model,
                system_prompt=system_prompt,
                user_prompt=user_prompt,
                max_tokens=max_tokens,
                temperature=temperature,
            )
            return content, tokens_in, tokens_out, model_parameters
        if engine == "gemini_native":
            content, tokens_in, tokens_out = self._call_gemini(
                api_key=api_key,
                model=selection.model,
                system_prompt=system_prompt,
                user_prompt=user_prompt,
                max_tokens=max_tokens,
                temperature=temperature,
                thinking_budget=thinking_budget,
            )
            return content, tokens_in, tokens_out, model_parameters
        raise RuntimeError(f"Engine LLM V4 sem executor real implementado: {engine}")

    @staticmethod
    def _select_candidate(candidates: list[Any], selected_mode: str) -> Any:
        if selected_mode == "real":
            # A ordem vem dos contratos externos de rota. O codigo nao conhece provider/modelo especifico.
            return sorted(
                candidates,
                key=lambda item: (-item.route_component, -item.quality_component, item.expected_cost_usd),
            )[0]
        return candidates[0]

    @staticmethod
    def _api_key(provider: dict[str, Any]) -> str | None:
        for key_name in provider.get("env_keys", []):
            value = os.environ.get(key_name)
            if value:
                return value
        return None

    @staticmethod
    def _exclude_providers(previous_provider: str | None) -> set[str]:
        if not previous_provider:
            return set()
        return {item.strip() for item in previous_provider.split(",") if item.strip()}

    @staticmethod
    def _exclude_models(previous_model: str | None) -> set[str]:
        if not previous_model:
            return set()
        return {item.strip() for item in previous_model.split(",") if item.strip()}

    def _temperature_for_model(self, model_name: str, default: float) -> float:
        model = self.healthcheck.models.get(model_name, {})
        flags = model.get("flags", {}) if isinstance(model, dict) else {}
        if flags.get("exige_temperature_01") is True:
            return 0.1
        return default

    @staticmethod
    def _messages(contract: EditorialContract, request: LLMRequest) -> tuple[str, str]:
        blocks = "\n\n".join(f"## {name}\n{content}" for name, content in contract.as_prompt_blocks())
        system_prompt = (
            "Voce e um redator jornalistico do V4. Siga estritamente os contratos editoriais externos, "
            "preserve fatos travados, nao invente informacao e escreva em portugues brasileiro vivo.\n\n"
            f"{blocks}"
        )
        user_prompt = (
            f"Titulo de trabalho: {request.titulo}\n"
            f"Editoria: {request.editoria}\n"
            f"Funcao: {request.funcao}\n"
            f"Idempotency key: {request.idempotency_key}\n\n"
            f"{request.conteudo}"
        )
        return system_prompt, user_prompt

    @staticmethod
    def _call_openai_like(
        provider: dict[str, Any],
        api_key: str,
        model: str,
        system_prompt: str,
        user_prompt: str,
        max_tokens: int,
        temperature: float,
    ) -> tuple[str, int, int]:
        from openai import OpenAI

        client_kwargs: dict[str, Any] = {"api_key": api_key}
        if provider.get("engine") == "openai_compatible" and provider.get("base_url"):
            client_kwargs["base_url"] = provider["base_url"]
        client = OpenAI(**client_kwargs)
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=temperature,
            max_tokens=max_tokens,
        )
        content = response.choices[0].message.content or ""
        usage = getattr(response, "usage", None)
        tokens_in = int(getattr(usage, "prompt_tokens", 0) or 0)
        tokens_out = int(getattr(usage, "completion_tokens", 0) or 0)
        return content.strip(), tokens_in, tokens_out

    @staticmethod
    def _call_anthropic(
        api_key: str,
        model: str,
        system_prompt: str,
        user_prompt: str,
        max_tokens: int,
        temperature: float,
    ) -> tuple[str, int, int]:
        import anthropic

        client = anthropic.Anthropic(api_key=api_key)
        response = client.messages.create(
            model=model,
            max_tokens=max_tokens,
            temperature=temperature,
            system=system_prompt,
            messages=[{"role": "user", "content": user_prompt}],
        )
        parts = [getattr(part, "text", "") for part in response.content if getattr(part, "type", "") == "text"]
        usage = getattr(response, "usage", None)
        tokens_in = int(getattr(usage, "input_tokens", 0) or 0)
        tokens_out = int(getattr(usage, "output_tokens", 0) or 0)
        return "\n".join(part for part in parts if part).strip(), tokens_in, tokens_out

    @staticmethod
    def _call_gemini(
        api_key: str,
        model: str,
        system_prompt: str,
        user_prompt: str,
        max_tokens: int,
        temperature: float,
        thinking_budget: int,
    ) -> tuple[str, int, int]:
        from google import genai
        from google.genai import types

        client = genai.Client(api_key=api_key)
        config_kwargs: dict[str, Any] = {
            "max_output_tokens": max_tokens,
            "temperature": temperature,
        }
        if thinking_budget >= 0:
            config_kwargs["thinking_config"] = types.ThinkingConfig(thinking_budget=thinking_budget)
        response = client.models.generate_content(
            model=model,
            contents=f"{system_prompt}\n\n{user_prompt}",
            config=types.GenerateContentConfig(**config_kwargs),
        )
        content = getattr(response, "text", "") or ""
        usage = getattr(response, "usage_metadata", None)
        tokens_in = int(getattr(usage, "prompt_token_count", 0) or 0)
        tokens_out = int(getattr(usage, "candidates_token_count", 0) or 0)
        return content.strip(), tokens_in, tokens_out

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
        base = (
            f"[MOCK V4/{selection.provider}/{selection.model}/{contract.editoria}/{request.funcao}] "
            f"{request.titulo}. "
        )
        paragraphs = [
            (
                "O texto de laboratorio abre pela tese escolhida e evita transformar a pauta em simples resumo. "
                f"A curadoria entregue ao produtor informa: {request.conteudo}"
            ),
            (
                "A segunda passagem organiza o fato principal, a consequencia material e os atores envolvidos. "
                "O objetivo do mock e exercitar gates tecnicos de revisao, fact-check e auditoria final, sem chamada externa."
            ),
            (
                "A terceira passagem preserva prudencia factual: fatos sem fonte primaria ficam marcados como pendencia, "
                "enquanto fatos travados seguem atribuidos ao material auditado."
            ),
            (
                "A quarta passagem testa ritmo e tamanho minimo para o revisor local. O texto nao e amostra editorial final, "
                "mas precisa ter corpo suficiente para nao mascarar erro de pipeline."
            ),
            (
                "A conclusao tecnica reafirma que o V4 deve publicar menos, com mais tese, checagem e rastreabilidade. "
                "Se qualquer gate posterior falhar, o fluxo deve bloquear e registrar o motivo."
            ),
        ]
        return base + "\n\n".join(f"<p>{paragraph}</p>" for paragraph in paragraphs)
