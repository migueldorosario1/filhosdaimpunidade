from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .loader import DirectiveLoader


DEFAULT_SHADOW_REDACTOR_CONTRACT = "diretrizes/v4_redator_shadow_v1.json"


class V4ShadowRedator:
    """Redator shadow V4: prepara pacote super_luxo sem chamada externa."""

    def __init__(self, root: str | Path = ".", contract_path: str = DEFAULT_SHADOW_REDACTOR_CONTRACT) -> None:
        self.loader = DirectiveLoader(root)
        self.root = self.loader.root
        self.contract_path = contract_path
        self.contract = self.loader.read_json(contract_path)

    def create(self, curadoria: dict[str, Any], execute: bool = False) -> dict[str, Any]:
        issues = self.validate(curadoria)
        payload = {
            "schema_version": self.contract.get("_version", "v1"),
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "mode": self.contract["routing"]["mode"],
            "external_call": False,
            "wordpress_real": False,
            "item_id": curadoria.get("item_id"),
            "curadoria_id": curadoria.get("curadoria_id"),
            "editoria": curadoria.get("editoria"),
            "selected_route": {
                "funcao": self.contract["routing"]["funcao"],
                "route_context": self.contract["routing"]["route_context"],
                "external_call": False,
                "real_call_requires_human_approval": True,
            },
            "titulo_shadow": self._title(curadoria),
            "prompt_shadow": self._prompt(curadoria),
            "texto_shadow": self._text(curadoria),
            "fatos_travados": curadoria.get("fatos_travados", []),
            "consequencia_material": curadoria.get("consequencia_material", {}),
            "collection_request": curadoria.get("collection_request", {}),
            "gates": {
                "requires_blind_review": True,
                "requires_audit_before_publish": True,
                "allow_wordpress_real": False,
                "allow_external_llm_call": False,
            },
            "issues": issues,
            "status": "shadow_redacao_bloqueada" if issues else "shadow_redacao_pronta",
        }
        if execute:
            path = self.output_path(payload)
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        return payload

    def validate(self, curadoria: dict[str, Any]) -> list[str]:
        issues: list[str] = []
        for field_name in self.contract["source"]["required_fields"]:
            if self._missing(curadoria.get(field_name)):
                issues.append(f"shadow_source_campo_ausente:{field_name}")
        advogado = (curadoria.get("validacoes") or {}).get("advogado_do_obvio") or {}
        if self.contract["gates"].get("block_if_advogado_obvio_rejected") and advogado.get("status") != "aprovada":
            issues.append("shadow_advogado_do_obvio_nao_aprovado")
        consequencia = curadoria.get("consequencia_material") or {}
        if self.contract["gates"].get("block_if_consequencia_material_generic"):
            if int(consequencia.get("nivel_concretude", 0) or 0) < 3:
                issues.append("shadow_consequencia_material_generica")
        collection = curadoria.get("collection_request") or {}
        if (
            self.contract["gates"].get("block_if_collection_required_before_shadow")
            and self.collection_blocks_stage(collection, "shadow_redacao")
        ):
            issues.append("shadow_collection_request_obrigatoria")
        return issues

    def collection_blocks_stage(self, collection: dict[str, Any], stage: str) -> bool:
        status = collection.get("status")
        required_before = collection.get("required_before")
        if status == "none" or required_before in (None, "none"):
            return False
        stage_order = self.contract.get("collection_request_semantics", {}).get("stage_order", [])
        if stage not in stage_order or required_before not in stage_order:
            return False
        return stage_order.index(stage) >= stage_order.index(required_before) and status in {"recommended", "required"}

    def output_path(self, payload: dict[str, Any]) -> Path:
        item_id = str(payload.get("item_id") or "sem_item")
        suffix = self.contract["output"]["suffix"]
        return self.root / self.contract["output"]["path"] / f"{item_id}.{suffix}.json"

    @staticmethod
    def _title(curadoria: dict[str, Any]) -> str:
        entity = (curadoria.get("frame_visual") or {}).get("entidade_principal") or "o caso"
        consequencia = (curadoria.get("consequencia_material") or {}).get("descricao", "muda a leitura politica")
        if "pix" in consequencia.lower():
            return f"{entity} enfrenta o custo político da pressão dos EUA sobre tarifa e Pix"
        return f"{entity} enfrenta o custo político da pressão dos EUA"

    @staticmethod
    def _prompt(curadoria: dict[str, Any]) -> str:
        fatos = "\n".join(f"- {item['fato']}" for item in curadoria.get("fatos_travados", []))
        consequencia = curadoria.get("consequencia_material", {})
        collection = curadoria.get("collection_request", {})
        return (
            "Escreva uma materia jornalistica V4 em portugues brasileiro, com tese clara e prosa viva.\n\n"
            f"Promessa ao leitor: {curadoria.get('promessa_ao_leitor')}\n"
            f"Briefing: {curadoria.get('briefing_produtor')}\n"
            f"Consequencia material: {consequencia.get('descricao')}\n"
            f"Quem ganha: {consequencia.get('quem_ganha')}\n"
            f"Quem perde: {consequencia.get('quem_perde')}\n\n"
            "Fatos travados obrigatorios:\n"
            f"{fatos}\n\n"
            f"Collection request: {collection.get('status')} — {collection.get('reason')}\n"
            "Nao invente fatos. Se um fato primario estiver pendente, escreva com prudencia ou marque lacuna."
        )

    @staticmethod
    def _text(curadoria: dict[str, Any]) -> str:
        entity = (curadoria.get("frame_visual") or {}).get("entidade_principal") or "O personagem central"
        consequencia = curadoria.get("consequencia_material", {})
        fatos = curadoria.get("fatos_travados", [])
        fato_base = fatos[0]["fato"] if fatos else curadoria.get("fato_novo", "")
        pix_fact = next((item["fato"] for item in fatos if "Pix" in item.get("fato", "") or "pix" in item.get("fato", "")), "")
        paragraphs = [
            (
                f"{entity} entrou na disputa das tarifas americanas em um ponto delicado: "
                f"{consequencia.get('descricao', 'a pressao externa mudou o custo politico da pauta')}."
            ),
            fato_base,
        ]
        if pix_fact:
            paragraphs.append(
                f"O Pix torna a contradição mais concreta. {pix_fact} "
                "A pauta deixa de ser apenas disputa verbal e passa a tocar infraestrutura financeira, soberania e custo eleitoral."
            )
        paragraphs.append(
            f"Esse deslocamento favorece {consequencia.get('quem_ganha')}. "
            f"Ao mesmo tempo, expõe {consequencia.get('quem_perde')} ao custo de uma pressão externa que já não cabe apenas na guerra de narrativas."
        )
        return "\n\n".join(f"<p>{paragraph}</p>" for paragraph in paragraphs if paragraph)

    @staticmethod
    def _missing(value: Any) -> bool:
        return value in (None, "", []) or value == {}
