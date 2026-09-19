from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .camadas import LayerAccessController
from .composer import ContractComposer
from .curadoria_tese import V4CuradoriaTese
from .loader import DirectiveLoader
from .llm_adapter import LLMRequest, V4LLMAdapter
from .media_audit import V4AuditedMediaStore
from .memoria import MemoryEvent, V4MemoryStore
from .telemetry import LLMCallDetail, TelemetryReceipt, V4Telemetry


DEFAULT_FLOW_CONTRACT = "diretrizes/v4_fluxo_dry_run_v1.json"


@dataclass(frozen=True)
class FlowStepResult:
    step: str
    role: str
    source_layer: str
    target_layer: str
    source_path: str
    target_path: str
    mode: str
    idempotency_key: str
    issues: list[str] = field(default_factory=list)

    def as_dict(self) -> dict[str, Any]:
        return {
            "step": self.step,
            "role": self.role,
            "source_layer": self.source_layer,
            "target_layer": self.target_layer,
            "source_path": self.source_path,
            "target_path": self.target_path,
            "mode": self.mode,
            "idempotency_key": self.idempotency_key,
            "issues": self.issues,
        }


class V4DryRunFlow:
    """Primeiro fluxo V4 local: auditado -> curadoria -> producao -> auditado -> publicado."""

    def __init__(self, root: str | Path = ".", contract_path: str = DEFAULT_FLOW_CONTRACT) -> None:
        self.loader = DirectiveLoader(root)
        self.root = self.loader.root
        self.contract_path = contract_path
        self.contract = self.loader.read_json(contract_path)
        self.layers = LayerAccessController(self.root)
        self.memory = V4MemoryStore(self.root)
        self.composer = ContractComposer(self.root)
        self.llm_adapter: V4LLMAdapter | None = None
        self.media_store = V4AuditedMediaStore(self.root)
        self.telemetry = V4Telemetry(self.root)
        self.curadoria = V4CuradoriaTese(self.root)

    def run(self, execute: bool = False) -> dict[str, Any]:
        fixture = self.contract["fixture"]
        item_id = fixture["item_id"]
        seed = self._ensure_fixture(fixture, execute=execute)
        source_path = seed
        results: list[FlowStepResult] = []

        for step in self.contract["steps"]:
            result = self._run_step(step, source_path, item_id, fixture["editoria"], execute=execute)
            results.append(result)
            if result.issues:
                break
            source_path = self.root / result.target_path

        ok = all(not result.issues for result in results)
        if execute:
            self.memory.append(
                MemoryEvent(
                    event_type="validacao",
                    severity="info" if ok else "error",
                    source="v4_dry_run_flow",
                    summary="Fluxo V4 dry-run executado",
                    tags=["v4", "fluxo", "dry_run"],
                    payload={"ok": ok, "steps": [result.as_dict() for result in results]},
                ),
                execute=True,
            )
        return {
            "ok": ok,
            "mode": "executed" if execute else "dry_run",
            "contract": self.contract_path,
            "fixture_path": str(seed.relative_to(self.root)),
            "steps": [result.as_dict() for result in results],
        }

    def _ensure_fixture(self, fixture: dict[str, Any], execute: bool) -> Path:
        layer_path = self._layer_path("auditado")
        path = layer_path / f"{fixture['item_id']}.json"
        if execute and not path.exists():
            layer_path.mkdir(parents=True, exist_ok=True)
            payload = {
                "item_id": fixture["item_id"],
                "editoria": fixture["editoria"],
                "titulo": fixture["titulo"],
                "primary_entity": fixture.get("primary_entity"),
                "fonte": fixture["fonte"],
                "conteudo": fixture["conteudo"],
                "leitura_corrente_timestamped": fixture.get("leitura_corrente_timestamped", {}),
                "status": "auditado_fixture",
                "created_at": self._now(),
                "manifesto_auditoria": {
                    "fonte_validada": True,
                    "risco_juridico_revisado": True,
                    "qualidade_minima": True,
                },
            }
            self._write_json(path, payload)
        return path

    def _run_step(
        self,
        step: dict[str, Any],
        source_path: Path,
        item_id: str,
        editoria: str,
        execute: bool,
    ) -> FlowStepResult:
        role = step["role"]
        source_layer = step["from"]
        target_layer = step["to"]
        issues = self._check_access(role, source_layer, target_layer)
        source_rel = str(source_path.relative_to(self.root))
        target_path = self._target_path(step["name"], target_layer, item_id)
        idempotency_key = self._idempotency_key(step["name"], item_id, source_rel)

        if not source_path.exists() and execute:
            issues.append(f"fonte ausente: {source_rel}")

        if not issues and execute:
            if target_path.exists():
                mode = "skipped_existing"
            else:
                source_payload = self._read_json(source_path)
                output = self._build_output(step, source_payload, editoria, idempotency_key)
                media_issues = self._attach_required_media(step, output)
                if media_issues:
                    issues.extend(media_issues)
                    mode = "blocked_media"
                else:
                    receipt_result = self._record_step_receipt(step, output, idempotency_key, execute=True)
                    if not receipt_result["ok"]:
                        issues.append(f"telemetria JSONL falhou: {receipt_result.get('errors')}")
                        mode = "blocked_receipt"
                    else:
                        target_path.parent.mkdir(parents=True, exist_ok=True)
                        self._write_json(target_path, output)
                        mode = "created"
        else:
            mode = "planned" if not issues else "blocked"

        return FlowStepResult(
            step=step["name"],
            role=role,
            source_layer=source_layer,
            target_layer=target_layer,
            source_path=source_rel,
            target_path=str(target_path.relative_to(self.root)),
            mode=mode,
            idempotency_key=idempotency_key,
            issues=issues,
        )

    def _record_step_receipt(
        self,
        step: dict[str, Any],
        output: dict[str, Any],
        idempotency_key: str,
        execute: bool,
    ) -> dict[str, Any]:
        llm = output.get("llm_response", {})
        llm_detail = None
        if llm:
            llm_detail = LLMCallDetail(
                provider=llm.get("provider", "unknown"),
                model=llm.get("model", "unknown"),
                tier=llm.get("selected_tier", llm.get("tier", "unknown")),
                tokens_in=int(llm.get("tokens_in", 0)),
                tokens_out=int(llm.get("tokens_out", 0)),
                duration_ms_llm=int(llm.get("duration_ms_llm", 0)),
                prompt_hash=llm.get("prompt_hash", ""),
                error_class=llm.get("error_class"),
            )
        receipt = TelemetryReceipt(
            event_type="pipeline_step",
            item_id=output["item_id"],
            vertical=output["editoria"],
            agent=step["role"],
            operation=step["name"],
            status=output["status"],
            idempotency_key=idempotency_key,
            llm=llm_detail,
            duration_ms=int(llm.get("duration_ms_llm", 0)) if llm else 0,
            cost_usd_estimated=float(llm.get("cost_usd_estimated", 0.0)) if llm else 0.0,
            pricing_table_version=llm.get("pricing_table_version", "pending") if llm else "pending",
            payload={
                "source_status": output.get("source_status"),
                "target_layer": step["to"],
                "external_publish": output.get("publicacao_dry_run", {}).get("external_publish"),
                "featured_media_id": output.get("featured_media", {}).get("image_id"),
            },
        )
        return self.telemetry.record_receipt(receipt, execute=execute)

    def _build_output(
        self,
        step: dict[str, Any],
        source_payload: dict[str, Any],
        editoria: str,
        idempotency_key: str,
    ) -> dict[str, Any]:
        contract = self.composer.compose(editoria, "redacao")
        base = {
            "item_id": source_payload["item_id"],
            "editoria": editoria,
            "curadoria_id": source_payload.get("curadoria_id"),
            "titulo": source_payload.get("titulo") or source_payload.get("source_material", {}).get("titulo"),
            "primary_entity": source_payload.get("primary_entity") or source_payload.get("source_material", {}).get("primary_entity"),
            "conteudo": source_payload.get("conteudo") or source_payload.get("source_material", {}).get("conteudo"),
            "promessa_ao_leitor": source_payload.get("promessa_ao_leitor"),
            "frame_visual": source_payload.get("frame_visual"),
            "tese_escolhida_idx": source_payload.get("tese_escolhida_idx"),
            "status": step["name"],
            "source_status": source_payload.get("status"),
            "created_at": self._now(),
            "idempotency_key": idempotency_key,
            "manifesto": {
                "step": step["name"],
                "role": step["role"],
                "from": step["from"],
                "to": step["to"],
                "requires": step.get("requires", []),
                "contrato_editorial_v4": {
                    "editoria": contract.editoria,
                    "funcao": contract.funcao,
                    "contexto_llm": contract.contexto_llm.name,
                    "diretriz_sha256": contract.diretriz.sha256,
                    "nucleo_sha256": contract.nucleo.sha256,
                },
                "texto_revisado": True,
                "imagem_destacada_validada": bool(source_payload.get("featured_media")),
                "curadoria_id": source_payload.get("curadoria_id"),
                "qualidade_minima": True,
                "manifesto_curadoria": step["name"] == "curadoria_dry_run",
                "manifesto_producao": True,
                "manifesto_auditoria_final": True,
                "manifesto_publicacao": True,
            },
        }
        if step["name"] == "curadoria_dry_run":
            return self.curadoria.create(
                source_payload,
                source_payload.get("leitura_corrente_timestamped", {}),
            )
        if step["name"] == "produzir_dry_run":
            gate = self.curadoria.validate_gate(source_payload, mode="dry_run")
            if not gate.ok:
                base["status"] = "bloqueado_sem_curadoria"
                base["issues"] = gate.issues
                return base
            if self.llm_adapter is None:
                self.llm_adapter = V4LLMAdapter(self.root)
            llm_response = self.llm_adapter.generate(
                LLMRequest(
                    editoria=editoria,
                    funcao="redacao",
                    titulo=base.get("titulo", ""),
                    conteudo=source_payload.get("briefing_produtor") or base.get("conteudo", ""),
                    idempotency_key=idempotency_key,
                )
            )
            base["texto_dry_run"] = llm_response.content
            base["llm_response"] = llm_response.as_dict()
        if step["name"] == "publicar_dry_run":
            base["publicacao_dry_run"] = {"external_publish": False, "wp_post_id": None}
        return base

    def _attach_required_media(self, step: dict[str, Any], output: dict[str, Any]) -> list[str]:
        if step["name"] != "publicar_dry_run":
            return []
        primary_entity = str(output.get("primary_entity") or "").strip()
        if not primary_entity:
            output.setdefault("manifesto", {})["imagem_destacada_validada"] = False
            return ["imagem_destacada: primary_entity ausente"]
        records = self.media_store.search(primary_entity, limit=1)
        if not records:
            output.setdefault("manifesto", {})["imagem_destacada_validada"] = False
            return [f"imagem_destacada: sem midia auditada para entidade '{primary_entity}'"]
        featured = records[0]
        output["featured_media"] = featured
        output.setdefault("manifesto", {})["imagem_destacada_validada"] = True
        output["publicacao_dry_run"] = {
            "external_publish": False,
            "wp_post_id": None,
            "featured_media_id": featured.get("image_id"),
            "featured_media_source": "agent_data/v4/media/audited",
        }
        return []

    def _check_access(self, role: str, source_layer: str, target_layer: str) -> list[str]:
        issues: list[str] = []
        read_decision = self.layers.decide(role, "read", source_layer)
        if not read_decision.allowed:
            issues.append(f"read {source_layer}: {read_decision.reason}")
        write_decision = self.layers.decide(role, "write", target_layer)
        if not write_decision.allowed:
            issues.append(f"write {target_layer}: {write_decision.reason}")
        return issues

    def _target_path(self, step_name: str, layer: str, item_id: str) -> Path:
        suffix = {
            "curadoria_dry_run": "curadoria",
            "produzir_dry_run": "producao",
            "auditar_final_dry_run": "auditado_final",
            "publicar_dry_run": "publicado_dry_run",
        }.get(step_name, step_name)
        return self._layer_path(layer) / f"{item_id}.{suffix}.json"

    def _layer_path(self, layer: str) -> Path:
        return self.root / self.layers.layers[layer]["path"]

    @staticmethod
    def _idempotency_key(step_name: str, item_id: str, source_rel: str) -> str:
        raw = f"{step_name}:{item_id}:{source_rel}"
        return hashlib.sha256(raw.encode("utf-8")).hexdigest()

    @staticmethod
    def _now() -> str:
        return datetime.now(timezone.utc).isoformat()

    @staticmethod
    def _read_json(path: Path) -> dict[str, Any]:
        return json.loads(path.read_text(encoding="utf-8"))

    @staticmethod
    def _write_json(path: Path, payload: dict[str, Any]) -> None:
        path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
