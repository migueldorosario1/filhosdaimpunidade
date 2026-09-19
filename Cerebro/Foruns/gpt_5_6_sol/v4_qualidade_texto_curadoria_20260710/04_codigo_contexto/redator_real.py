from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .loader import DirectiveLoader
from .llm_adapter import LLMRequest, V4LLMAdapter, V4LLMRealCallError
from .llm_healthcheck import V4LLMHealthcheck
from .redator_shadow import V4ShadowRedator
from .telemetry import LLMCallDetail, TelemetryReceipt, V4Telemetry


DEFAULT_REAL_REDACTOR_CONTRACT = "contratos/v4_redator_real_v1.json"


class V4RealRedator:
    """Preflight do redator real V4, sem executar chamada externa."""

    def __init__(self, root: str | Path = ".", contract_path: str = DEFAULT_REAL_REDACTOR_CONTRACT) -> None:
        self.loader = DirectiveLoader(root)
        self.root = self.loader.root
        self.contract_path = contract_path
        self.contract = self.loader.read_json(contract_path)
        self.shadow_gate = V4ShadowRedator(root)
        adapter_contract = self.contract["routing"].get("adapter_contract", "contratos/v4_llm_adapter_v1.json")
        self.healthcheck = V4LLMHealthcheck(root, adapter_contract=adapter_contract)

    def preflight(self, curadoria: dict[str, Any], execute: bool = False) -> dict[str, Any]:
        issues = self.validate(curadoria)
        health = self.healthcheck.check(
            curadoria.get("editoria") or "v4_politica_economia",
            self.contract["routing"].get("funcao", "redacao"),
        )
        if self.contract["gates"].get("block_if_adapter_real_unavailable") and not health.ok:
            issues.extend(f"adapter_real_bloqueado:{issue}" for issue in health.issues)

        payload = {
            "schema_version": self.contract.get("_version", "v1"),
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "mode": self.contract["routing"]["mode"],
            "external_call_executed": False,
            "wordpress_real": False,
            "item_id": curadoria.get("item_id"),
            "curadoria_id": curadoria.get("curadoria_id"),
            "editoria": curadoria.get("editoria"),
            "selected_route": {
                "funcao": self.contract["routing"]["funcao"],
                "route_context": self.contract["routing"]["route_context"],
                "external_call": False,
                "external_call_requires_human_approval": True,
            },
            "prompt_real_preflight": self._prompt(curadoria),
            "fatos_travados": curadoria.get("fatos_travados", []),
            "consequencia_material": curadoria.get("consequencia_material", {}),
            "collection_request": curadoria.get("collection_request", {}),
            "healthcheck": health.as_dict(),
            "issues": issues,
            "status": "redator_real_llm_bloqueado" if issues else "redator_real_llm_preflight_pronto",
        }
        if execute:
            path = self.output_path(payload)
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        return payload

    def call_real(self, curadoria: dict[str, Any], execute: bool = False, exclude_provider: str | None = None) -> dict[str, Any]:
        issues = self.validate(curadoria)
        health = self.healthcheck.check(
            curadoria.get("editoria") or "v4_politica_economia",
            self.contract["routing"].get("funcao", "redacao"),
        )
        if self.contract["gates"].get("block_if_adapter_real_unavailable") and not health.ok:
            issues.extend(f"adapter_real_bloqueado:{issue}" for issue in health.issues)
        if issues:
            payload = self._payload_base(curadoria, health.as_dict(), issues)
            payload["status"] = "redator_real_llm_bloqueado"
            payload["external_call_executed"] = False
            if execute:
                self._write_real_output(payload)
            return payload

        adapter = self._make_adapter()
        excluded_providers = self._provider_exclusions(exclude_provider)
        excluded_models: set[str] = set()
        attempts: list[dict[str, Any]] = []
        response = None
        text_issues: list[str] = []
        last_issues: list[str] = []
        fallback = self.contract.get("fallback", {})
        max_attempts = max(1, int(fallback.get("max_attempts", 1) or 1))
        retry_on_error = fallback.get("retry_on_error") is True
        retry_on_incomplete = fallback.get("retry_on_incomplete") is True

        for attempt_index in range(1, max_attempts + 1):
            previous_provider = ",".join(sorted(excluded_providers)) or None
            previous_model = ",".join(sorted(excluded_models)) or None
            try:
                candidate_response = adapter.generate(
                    LLMRequest(
                        editoria=curadoria.get("editoria") or "v4_politica_economia",
                        funcao=self.contract["routing"].get("funcao", "redacao"),
                        titulo=(curadoria.get("source_material") or {}).get("titulo") or "Materia V4",
                        conteudo=self._prompt(curadoria),
                        idempotency_key=f"{curadoria.get('curadoria_id')}:redator_real_llm:v1:{attempt_index}",
                        previous_provider=previous_provider,
                        previous_model=previous_model,
                    ),
                    mode="real",
                )
            except V4LLMRealCallError as exc:
                issue = f"llm_real_error:{type(exc).__name__}:{self._sanitize_error(str(exc))}"
                attempts.append(
                    {
                        "attempt": attempt_index,
                        "outcome": "error",
                        "provider": exc.provider,
                        "model": exc.model,
                        "excluded_before": sorted(excluded_providers),
                        "excluded_models_before": sorted(excluded_models),
                        "issues": [issue],
                    }
                )
                last_issues = [issue]
                if retry_on_error and exc.model and attempt_index < max_attempts:
                    excluded_models.add(exc.model)
                    continue
                break
            except Exception as exc:  # noqa: BLE001 - falha externa vira artefato auditavel
                issue = f"llm_real_error:{type(exc).__name__}:{self._sanitize_error(str(exc))}"
                attempts.append(
                    {
                        "attempt": attempt_index,
                        "outcome": "error",
                        "provider": None,
                        "model": None,
                        "excluded_before": sorted(excluded_providers),
                        "excluded_models_before": sorted(excluded_models),
                        "issues": [issue],
                    }
                )
                last_issues = [issue]
                break

            candidate_issues = self._real_text_issues(candidate_response.content)
            attempts.append(
                {
                    "attempt": attempt_index,
                    "outcome": "incomplete" if candidate_issues else "success",
                    "provider": candidate_response.provider,
                    "model": candidate_response.model,
                    "tier": candidate_response.selected_tier,
                    "excluded_before": sorted(excluded_providers),
                    "excluded_models_before": sorted(excluded_models),
                    "content_chars": len(candidate_response.content or ""),
                    "issues": candidate_issues,
                }
            )
            response = candidate_response
            text_issues = candidate_issues
            last_issues = candidate_issues
            if not candidate_issues:
                break
            if retry_on_incomplete and attempt_index < max_attempts:
                excluded_models.add(candidate_response.model)
                continue
            break

        payload = self._payload_base(curadoria, health.as_dict(), last_issues)
        payload["fallback_attempts"] = attempts
        payload["fallback_excluded_providers_final"] = sorted(excluded_providers)
        payload["fallback_excluded_models_final"] = sorted(excluded_models)
        if response is None:
            payload["status"] = "redator_real_llm_falhou"
            payload["external_call_executed"] = True
            if execute:
                self._write_real_output(payload)
            return payload

        payload.update(
            {
                "status": "redator_real_llm_incompleto" if text_issues else "redator_real_llm_pronto",
                "external_call_executed": True,
                "selected_route": {
                    "funcao": self.contract["routing"]["funcao"],
                    "route_context": response.route_context,
                    "external_call": True,
                    "external_call_requires_human_approval": True,
                    "provider": response.provider,
                    "model": response.model,
                    "tier": response.selected_tier,
                    "selection_reason": response.selection_reason,
                },
                "texto_real": response.content,
                "llm_response": response.as_dict(),
            }
        )
        if execute:
            self._write_real_output(payload)
        return payload

    def validate(self, curadoria: dict[str, Any]) -> list[str]:
        issues: list[str] = []
        for field_name in self.contract["source"]["required_fields"]:
            if self._missing(curadoria.get(field_name)):
                issues.append(f"real_source_campo_ausente:{field_name}")

        collection = curadoria.get("collection_request") or {}
        if (
            self.contract["gates"].get("block_if_collection_blocks_redator_real")
            and self.shadow_gate.collection_blocks_stage(collection, "redator_real_llm")
        ):
            issues.append("real_collection_request_bloqueia_redator_real")

        advogado = (curadoria.get("validacoes") or {}).get("advogado_do_obvio") or {}
        if self.contract["gates"].get("block_if_advogado_obvio_rejected") and advogado.get("status") != "aprovada":
            issues.append("real_advogado_do_obvio_nao_aprovado")

        consequencia = curadoria.get("consequencia_material") or {}
        if self.contract["gates"].get("block_if_consequencia_material_generic"):
            if int(consequencia.get("nivel_concretude", 0) or 0) < 3:
                issues.append("real_consequencia_material_generica")
        return issues

    def output_path(self, payload: dict[str, Any]) -> Path:
        item_id = str(payload.get("item_id") or "sem_item")
        suffix = self.contract["output"]["suffix"]
        return self.root / self.contract["output"]["path"] / f"{item_id}.{suffix}.json"

    def real_output_path(self, payload: dict[str, Any]) -> Path:
        item_id = str(payload.get("item_id") or "sem_item")
        suffix = self.contract["output"].get("real_suffix", "redator_real")
        return self.root / self.contract["output"]["path"] / f"{item_id}.{suffix}.json"

    def _write_real_output(self, payload: dict[str, Any]) -> None:
        path = self.real_output_path(payload)
        path.parent.mkdir(parents=True, exist_ok=True)
        attempts_path = path.with_name(f"{path.stem}_attempts.jsonl")
        payload["telemetry_receipt"] = self._record_telemetry(payload)
        if payload["telemetry_receipt"].get("ok") is not True:
            payload.setdefault("issues", []).append("telemetry_receipt_failed")
        with attempts_path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(payload, ensure_ascii=False, sort_keys=True) + "\n")
        path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    def _make_adapter(self) -> V4LLMAdapter:
        return V4LLMAdapter(self.root, self.contract["routing"].get("adapter_contract", "contratos/v4_llm_adapter_v1.json"))

    def _payload_base(self, curadoria: dict[str, Any], health: dict[str, Any], issues: list[str]) -> dict[str, Any]:
        return {
            "schema_version": self.contract.get("_version", "v1"),
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "mode": "real_super_luxo",
            "external_call_executed": False,
            "wordpress_real": False,
            "item_id": curadoria.get("item_id"),
            "curadoria_id": curadoria.get("curadoria_id"),
            "editoria": curadoria.get("editoria"),
            "selected_route": {
                "funcao": self.contract["routing"]["funcao"],
                "route_context": self.contract["routing"]["route_context"],
                "external_call": False,
                "external_call_requires_human_approval": True,
            },
            "prompt_real": self._prompt(curadoria),
            "fatos_travados": curadoria.get("fatos_travados", []),
            "consequencia_material": curadoria.get("consequencia_material", {}),
            "collection_request": curadoria.get("collection_request", {}),
            "healthcheck": health,
            "issues": issues,
        }

    def _record_telemetry(self, payload: dict[str, Any]) -> dict[str, Any]:
        llm_response = payload.get("llm_response") or {}
        llm = None
        if llm_response:
            model_parameters = llm_response.get("model_parameters") or {}
            llm = LLMCallDetail(
                provider=str(llm_response.get("provider", "")),
                model=str(llm_response.get("model", "")),
                tier=str(llm_response.get("selected_tier", "")),
                tokens_in=int(llm_response.get("tokens_in", 0) or 0),
                tokens_out=int(llm_response.get("tokens_out", 0) or 0),
                duration_ms_llm=int(llm_response.get("duration_ms_llm", 0) or 0),
                prompt_hash=str(llm_response.get("prompt_hash", "")),
                temperature=model_parameters.get("temperature"),
                max_tokens=model_parameters.get("max_tokens"),
                thinking_budget=model_parameters.get("thinking_budget"),
                error_class=llm_response.get("error_class"),
            )
        receipt = TelemetryReceipt(
            event_type="llm_call",
            item_id=str(payload.get("item_id") or "sem_item"),
            vertical=str(payload.get("editoria") or "v4_sem_editoria"),
            agent="redator_real",
            operation="redator_real_llm",
            status=str(payload.get("status") or "unknown"),
            idempotency_key=self._receipt_idempotency_key(payload),
            llm=llm,
            duration_ms=int(llm_response.get("duration_ms_llm", 0) or 0),
            cost_usd_estimated=float(llm_response.get("cost_usd_estimated", 0.0) or 0.0),
            pricing_table_version=str(llm_response.get("pricing_table_version", "pending")),
            payload={
                "external_call_executed": payload.get("external_call_executed"),
                "wordpress_real": payload.get("wordpress_real"),
                "selected_route": payload.get("selected_route"),
                "issues": payload.get("issues", []),
                "fallback_attempts": payload.get("fallback_attempts", []),
                "fallback_excluded_models_final": payload.get("fallback_excluded_models_final", []),
                "text_chars": len(payload.get("texto_real") or ""),
                "model_parameters": llm_response.get("model_parameters", {}),
            },
        )
        return V4Telemetry(self.root).record_receipt(receipt, execute=True)

    @staticmethod
    def _prompt(curadoria: dict[str, Any]) -> str:
        fatos = "\n".join(f"- {item['fato']}" for item in curadoria.get("fatos_travados", []))
        consequencia = curadoria.get("consequencia_material", {})
        collection = curadoria.get("collection_request", {})
        return (
            "Redija a materia final V4 com tese clara, prosa humana e rigor factual.\n\n"
            f"Promessa ao leitor: {curadoria.get('promessa_ao_leitor')}\n"
            f"Briefing: {curadoria.get('briefing_produtor')}\n"
            f"Tese escolhida: {self_tese(curadoria)}\n\n"
            f"Consequencia material: {consequencia.get('descricao')}\n"
            f"Quem ganha: {consequencia.get('quem_ganha')}\n"
            f"Quem perde: {consequencia.get('quem_perde')}\n\n"
            "Fatos travados obrigatorios:\n"
            f"{fatos}\n\n"
            f"Collection request: {collection.get('status')} — {collection.get('reason')}\n"
            "Nao invente fatos. Preserve atribuicoes de fonte. Se houver lacuna para publicacao real, mantenha atribuição prudente.\n\n"
            "Entregue uma materia completa, entre 700 e 1000 palavras, com titulo, subtitulo e corpo. "
            "Nao pare no meio de frase. Nao entregue resumo, nota ou esqueleto. "
            "O texto deve ser publicavel como rascunho editorial apos revisao humana."
        )

    @staticmethod
    def _missing(value: Any) -> bool:
        return value in (None, "", []) or value == {}

    @staticmethod
    def _sanitize_error(message: str) -> str:
        message = re.sub(r"sk-proj-[A-Za-z0-9_*\\-]+", "[REDACTED_API_KEY]", message)
        message = re.sub(r"sk-ant-[A-Za-z0-9_*\\-]+", "[REDACTED_API_KEY]", message)
        message = re.sub(r"sk-[A-Za-z0-9_*\\-]+", "[REDACTED_API_KEY]", message)
        message = re.sub(r"AIza[0-9A-Za-z_\\-]{20,}", "[REDACTED_API_KEY]", message)
        message = re.sub(r"gsk_[0-9A-Za-z_\\-]+", "[REDACTED_API_KEY]", message)
        message = re.sub(r"pplx-[0-9A-Za-z_\\-]+", "[REDACTED_API_KEY]", message)
        return message

    @staticmethod
    def _provider_exclusions(raw: str | None) -> set[str]:
        if not raw:
            return set()
        return {item.strip() for item in raw.split(",") if item.strip()}

    @staticmethod
    def _receipt_idempotency_key(payload: dict[str, Any]) -> str:
        attempts = payload.get("fallback_attempts") or []
        attempt_count = len(attempts)
        selected = payload.get("selected_route") or {}
        provider = selected.get("provider") or "sem_provider"
        model = selected.get("model") or "sem_modelo"
        return f"{payload.get('curadoria_id')}:redator_real_llm:{attempt_count}:{provider}:{model}"

    def _real_text_issues(self, content: str) -> list[str]:
        quality = self.contract.get("real_output_quality", {})
        issues: list[str] = []
        text = (content or "").strip()
        min_chars = int(quality.get("min_chars", 0) or 0)
        if min_chars and len(text) < min_chars:
            issues.append(f"real_output_curto:{len(text)}<{min_chars}")
        endings = tuple(quality.get("block_if_ends_with", []) or [])
        if endings and text.endswith(endings):
            issues.append("real_output_interrompido")
        return issues


def self_tese(curadoria: dict[str, Any]) -> str:
    idx = curadoria.get("tese_escolhida_idx")
    for tese in curadoria.get("teses_candidatas", []):
        if tese.get("idx") == idx:
            return str(tese.get("tese", ""))
    return ""
