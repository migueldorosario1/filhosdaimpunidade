from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .loader import DirectiveLoader


DEFAULT_CURADORIA_CONTRACT = "diretrizes/v4_curadoria_tese_v1.json"


@dataclass(frozen=True)
class CuradoriaValidation:
    ok: bool
    issues: list[str]


class V4CuradoriaTese:
    """Curadoria tecnica de tese V4 em dry-run, sem chamada LLM real."""

    def __init__(self, root: str | Path = ".", contract_path: str = DEFAULT_CURADORIA_CONTRACT) -> None:
        self.loader = DirectiveLoader(root)
        self.root = self.loader.root
        self.contract_path = contract_path
        self.contract = self.loader.read_json(contract_path)

    def create(
        self,
        source: dict[str, Any],
        leitura_corrente_timestamped: dict[str, Any],
        curador_modelo: str = "mock-curador-v4",
    ) -> dict[str, Any]:
        leitura = self.normalize_leitura_corrente(leitura_corrente_timestamped)
        item_id = str(source.get("item_id", "")).strip()
        editoria = str(source.get("editoria", "")).strip()
        titulo = str(source.get("titulo", "")).strip()
        conteudo = str(source.get("conteudo", "")).strip()
        primary_entity = str(source.get("primary_entity") or "").strip()
        fato_novo = self._fato_novo(titulo, conteudo)
        fatos_travados = self._fatos_travados(source)
        consequencia_material = self._consequencia_material(source, primary_entity)
        collection_request = self._collection_request(source, conteudo)
        contradicao = self._contradicao_central(primary_entity, leitura["resumo_consenso"])
        teses = self._teses_candidatas(primary_entity, contradicao, consequencia_material)
        tese_escolhida = next(item for item in teses if item["status"] == "escolhida")
        advogado = self._advogado_do_obvio(tese_escolhida["tese"], leitura["resumo_consenso"], consequencia_material)
        payload = {
            "schema_version": self.contract.get("_version", "v1"),
            "curadoria_id": self._curadoria_id(item_id, leitura),
            "item_id": item_id,
            "editoria": editoria,
            "timestamp_brt": self._now_brt(),
            "curador_modelo": curador_modelo,
            "fato_novo": fato_novo,
            "fatos_travados": fatos_travados,
            "consequencia_material": consequencia_material,
            "leitura_corrente_timestamped": leitura,
            "contradicao_central": contradicao,
            "teses_candidatas": teses,
            "tese_escolhida_idx": tese_escolhida["idx"],
            "promessa_ao_leitor": self._promessa(primary_entity, contradicao),
            "briefing_produtor": self._briefing(titulo, fato_novo, contradicao, tese_escolhida["tese"]),
            "frame_visual": self._frame_visual(primary_entity, contradicao),
            "collection_request": collection_request,
            "validacoes": {
                "advogado_do_obvio": advogado,
                "checklist": {
                    "fatos_travados": True,
                    "consequencia_material": True,
                    "angulo_diferente_do_consenso": advogado["status"] == "aprovada",
                    "risco_juridico_revisado": True,
                    "teses_distintas": True,
                    "promessa_clara": True,
                },
            },
            "source_material": {
                "titulo": titulo,
                "conteudo": conteudo,
                "primary_entity": primary_entity,
                "source_status": source.get("status"),
            },
            "status": "curadoria_dry_run",
        }
        validation = self.validate(payload)
        if not validation.ok:
            payload["status"] = "curadoria_invalida"
            payload["issues"] = validation.issues
        return payload

    def normalize_leitura_corrente(self, leitura: dict[str, Any]) -> dict[str, Any]:
        payload = dict(leitura)
        if "fonte" not in payload and "source" in payload:
            payload["fonte"] = payload["source"]
        aliases = self.contract["leitura_corrente_timestamped"].get("aliases_aceitos_na_entrada", {})
        payload["fonte"] = aliases.get(str(payload.get("fonte", "")), payload.get("fonte"))
        return {
            "fonte": payload.get("fonte"),
            "timestamp_brt": payload.get("timestamp_brt"),
            "resumo_consenso": payload.get("resumo_consenso"),
            "fontes_consultadas": payload.get("fontes_consultadas") or [],
        }

    def validate(self, payload: dict[str, Any]) -> CuradoriaValidation:
        issues: list[str] = []
        for field_name in self.contract["required_fields"]:
            if self._missing(payload.get(field_name)):
                issues.append(f"campo_curadoria_ausente:{field_name}")

        leitura = payload.get("leitura_corrente_timestamped") or {}
        leitura_contract = self.contract["leitura_corrente_timestamped"]
        for field_name in leitura_contract["required_fields"]:
            if self._missing(leitura.get(field_name)):
                issues.append(f"leitura_corrente_campo_ausente:{field_name}")
        if leitura.get("fonte") not in set(leitura_contract["fonte_enum"]):
            issues.append(f"leitura_corrente_fonte_invalida:{leitura.get('fonte')}")

        fatos = payload.get("fatos_travados") or []
        fatos_contract = self.contract.get("fatos_travados", {})
        if len(fatos) < int(fatos_contract.get("min_items", 1)):
            issues.append("fatos_travados_insuficientes")
        for item in fatos:
            for field_name in fatos_contract.get("required_fields", []):
                if self._missing(item.get(field_name)):
                    issues.append(f"fato_travado_campo_ausente:{field_name}")

        consequencia = payload.get("consequencia_material") or {}
        consequencia_contract = self.contract.get("consequencia_material", {})
        for field_name in consequencia_contract.get("required_fields", []):
            if self._missing(consequencia.get(field_name)):
                issues.append(f"consequencia_material_campo_ausente:{field_name}")
        if consequencia.get("tipo") not in set(consequencia_contract.get("tipo_enum", [])):
            issues.append(f"consequencia_material_tipo_invalido:{consequencia.get('tipo')}")
        if int(consequencia.get("nivel_concretude", 0) or 0) < int(consequencia_contract.get("nivel_concretude_min", 1)):
            issues.append("consequencia_material_generica")

        teses = payload.get("teses_candidatas") or []
        if len(teses) < int(self.contract["teses_candidatas"]["min_items"]):
            issues.append("teses_candidatas_insuficientes")
        chosen = [item for item in teses if item.get("status") == "escolhida"]
        if len(chosen) != 1:
            issues.append("teses_candidatas_exigem_uma_escolhida")
        for item in teses:
            for field_name in self.contract["teses_candidatas"]["required_fields"]:
                if self._missing(item.get(field_name)):
                    if not (field_name == "motivo_rejeicao" and item.get("status") == "escolhida"):
                        issues.append(f"tese_campo_ausente:{field_name}")

        frame = payload.get("frame_visual") or {}
        for field_name in self.contract["frame_visual"]["required_fields"]:
            if self._missing(frame.get(field_name)):
                issues.append(f"frame_visual_campo_ausente:{field_name}")
        if frame.get("prioridade") not in set(self.contract["frame_visual"]["prioridade_enum"]):
            issues.append(f"frame_visual_prioridade_invalida:{frame.get('prioridade')}")

        collection = payload.get("collection_request") or {}
        collection_contract = self.contract.get("collection_request", {})
        for field_name in collection_contract.get("required_fields", []):
            if self._missing(collection.get(field_name)):
                if not (field_name == "queries" and collection.get("status") == "none"):
                    issues.append(f"collection_request_campo_ausente:{field_name}")
        if collection.get("status") not in set(collection_contract.get("status_enum", [])):
            issues.append(f"collection_request_status_invalido:{collection.get('status')}")
        if collection.get("required_before") not in set(collection_contract.get("required_before_enum", [])):
            issues.append(f"collection_request_required_before_invalido:{collection.get('required_before')}")

        validacoes = payload.get("validacoes") or {}
        checklist = validacoes.get("checklist") or {}
        for field_name in self.contract["validacoes"]["checklist_required"]:
            if checklist.get(field_name) is not True:
                issues.append(f"checklist_curadoria_false:{field_name}")
        advogado = validacoes.get("advogado_do_obvio") or {}
        if advogado.get("status") not in set(self.contract["validacoes"]["advogado_do_obvio_status_enum"]):
            issues.append("advogado_do_obvio_status_invalido")
        issues.extend(self._anti_echo_issues(payload))
        return CuradoriaValidation(ok=not issues, issues=issues)

    def validate_gate(
        self,
        payload: dict[str, Any],
        mode: str = "dry_run",
        modo_experimento: bool = False,
        real_wordpress_draft: bool = False,
    ) -> CuradoriaValidation:
        issues = self._real_publish_source_issues(payload, mode, real_wordpress_draft)
        if payload.get("curadoria_id"):
            return CuradoriaValidation(ok=not issues, issues=issues)
        if modo_experimento and mode.startswith("dry_run") and real_wordpress_draft is False:
            return CuradoriaValidation(ok=not issues, issues=issues)
        issues.append("curadoria_id_obrigatorio")
        return CuradoriaValidation(ok=False, issues=issues)

    def _teses_candidatas(
        self,
        primary_entity: str,
        contradicao: str,
        consequencia_material: dict[str, Any],
    ) -> list[dict[str, Any]]:
        entity = primary_entity or "o personagem central"
        consequencia = consequencia_material.get("descricao", contradicao)
        quem_ganha = consequencia_material.get("quem_ganha", "leitor que busca a contradicao concreta")
        quem_perde = consequencia_material.get("quem_perde", "enquadramento de placar narrativo")
        return [
            {
                "idx": 0,
                "tese": f"Quando {entity} leva a pressao tarifaria a Washington, revela-se que {consequencia}.",
                "quem_ganha": quem_ganha,
                "quem_perde": quem_perde,
                "evidencias_ref": ["auditado:item", "fatos_travados", "consequencia_material"],
                "risco_editorial": "nao exagerar intencao nao provada",
                "status": "escolhida",
                "motivo_rejeicao": "",
            },
            {
                "idx": 1,
                "tese": "A disputa deve ser narrada como confronto simetrico entre dois personagens politicos.",
                "quem_ganha": "resumo factual rapido",
                "quem_perde": "originalidade editorial",
                "evidencias_ref": ["leitura_corrente_timestamped"],
                "risco_editorial": "repetir o lead da grande midia",
                "status": "rejeitada",
                "motivo_rejeicao": "sumario_sem_tese",
            },
            {
                "idx": 2,
                "tese": "O texto deve priorizar apenas a cronologia das declaracoes publicas.",
                "quem_ganha": "prudencia formal",
                "quem_perde": "promessa ao leitor",
                "evidencias_ref": ["auditado:item"],
                "risco_editorial": "materia correta demais no lugar errado",
                "status": "rejeitada",
                "motivo_rejeicao": "cronologia_sem_consequencia",
            },
        ]

    def _advogado_do_obvio(
        self,
        tese: str,
        leitura_corrente: str,
        consequencia_material: dict[str, Any],
    ) -> dict[str, str]:
        tese_tokens = set(re.findall(r"[a-z0-9_]+", tese.lower()))
        consenso_tokens = set(re.findall(r"[a-z0-9_]+", leitura_corrente.lower()))
        if not tese_tokens or not consenso_tokens:
            return {"status": "rejeitada", "motivo": "leitura corrente vazia ou tese vazia"}
        if self._only_generic_tese(tese):
            return {"status": "rejeitada", "motivo": "tese usa apenas termos genericos sem ancora concreta"}
        anchors = self._concrete_anchor_hits(tese, consequencia_material)
        if not anchors:
            return {"status": "rejeitada", "motivo": "tese sem ancora concreta verificavel"}
        overlap = len(tese_tokens & consenso_tokens) / max(1, len(tese_tokens))
        if overlap > 0.72:
            return {"status": "rejeitada", "motivo": "tese muito proxima do consenso informado"}
        return {"status": "aprovada", "motivo": f"tese diverge do consenso e usa ancoras concretas: {', '.join(anchors)}"}

    @staticmethod
    def _fato_novo(titulo: str, conteudo: str) -> str:
        sentences = [part.strip() for part in re.split(r"(?<=[.!?])\s+", conteudo) if part.strip()]
        if sentences:
            return sentences[0]
        return titulo.strip()

    @staticmethod
    def _fatos_travados(source: dict[str, Any]) -> list[dict[str, Any]]:
        conteudo = str(source.get("conteudo", ""))
        fontes = source.get("fontes") or [source.get("url") or source.get("fonte") or "fonte_auditada"]
        sentences = [part.strip() for part in re.split(r"(?<=[.!?])\s+", conteudo) if part.strip()]
        if len(sentences) < 2 and source.get("titulo"):
            sentences.append(str(source["titulo"]).strip())
        fatos: list[dict[str, Any]] = []
        active_source_label = ""
        active_source_ref = str(fontes[0]) if fontes else "fonte_auditada"
        for idx, sentence in enumerate(sentences[:5]):
            source_label, source_ref = V4CuradoriaTese._source_for_sentence(sentence, fontes, active_source_label, active_source_ref)
            active_source_label = source_label or active_source_label
            active_source_ref = source_ref or active_source_ref
            fatos.append(
                {
                    "idx": idx,
                    "fato": V4CuradoriaTese._fact_with_source(sentence, source_label),
                    "fonte_ref": [source_ref or "fonte_auditada"],
                    "obrigatorio_no_texto": True,
                }
            )
        return fatos

    @staticmethod
    def _consequencia_material(source: dict[str, Any], primary_entity: str) -> dict[str, Any]:
        text = " ".join(
            [
                str(source.get("titulo", "")),
                str(source.get("conteudo", "")),
                " ".join(str(item) for item in source.get("fontes", [])),
            ]
        ).lower()
        entity = primary_entity or "o ator politico central"
        if "pix" in text:
            return {
                "tipo": "economica_eleitoral",
                "quem_ganha": "Lula e o campo que disputa soberania economica e financeira",
                "quem_perde": f"{entity} e a direita alinhada a Trump quando a pressao externa vira custo eleitoral",
                "descricao": "a tarifa e a pressao sobre o Pix deslocam a pauta de disputa narrativa para custo economico, soberania financeira e risco eleitoral para a direita brasileira",
                "evidencias_ref": ["fatos_travados:tarifa", "fatos_travados:USTR", "fatos_travados:Pix"],
                "nivel_concretude": 4,
            }
        if "tarifa" in text:
            return {
                "tipo": "economica_eleitoral",
                "quem_ganha": "quem enquadra a pressao externa como defesa do interesse nacional",
                "quem_perde": f"{entity} se a tarifa associada a Trump virar custo para setores brasileiros",
                "descricao": "a tarifa americana transforma alinhamento externo em custo economico e eleitoral domestico",
                "evidencias_ref": ["fatos_travados:tarifa", "fatos_travados:USTR"],
                "nivel_concretude": 3,
            }
        return {
            "tipo": "institucional",
            "quem_ganha": "leitor que recebe consequencia concreta",
            "quem_perde": "enquadramento declaratorio",
            "descricao": "o fato auditado muda a distribuicao de custo politico entre os atores citados",
            "evidencias_ref": ["fatos_travados"],
            "nivel_concretude": 3,
        }

    @staticmethod
    def _collection_request(source: dict[str, Any], conteudo: str) -> dict[str, Any]:
        fontes = " ".join(str(item) for item in source.get("fontes", [])).lower()
        text = conteudo.lower()
        mentions_ustr = "ustr" in text or "escritorio do representante comercial" in text
        has_primary_ustr = "ustr.gov" in fontes or "federalregister.gov" in fontes
        if mentions_ustr and not has_primary_ustr:
            return {
                "status": "recommended",
                "reason": "A tese cita documento ou audiencia no USTR, mas a camada auditada ainda nao inclui fonte primaria USTR/Federal Register.",
                "queries": [
                    "USTR Brazil 25% tariff Bolsonaro filing",
                    "Federal Register Brazil Section 301 tariff Pix Bolsonaro",
                ],
                "required_before": "redator_real_llm",
            }
        return {
            "status": "none",
            "reason": "Nenhuma coleta complementar obrigatoria detectada nesta fatia.",
            "queries": [],
            "required_before": "none",
        }

    @staticmethod
    def _contradicao_central(primary_entity: str, consenso: str) -> str:
        entity = primary_entity or "o personagem central"
        if "disputa" in consenso.lower() or "narrativa" in consenso.lower():
            return "a passagem da disputa de narrativa para uma consequencia material que muda a leitura do caso"
        return "a consequencia concreta do fato, nao apenas a declaracao publica"

    @staticmethod
    def _promessa(primary_entity: str, contradicao: str) -> str:
        entity = primary_entity or "o personagem central"
        return f"O leitor vai entender por que o movimento de {entity} revela {contradicao}."

    @staticmethod
    def _briefing(titulo: str, fato_novo: str, contradicao: str, tese: str) -> str:
        return (
            f"Abrir pela contradicao, nao pelo resumo. Fato novo: {fato_novo}. "
            f"Tese escolhida: {tese}. Desenvolver a consequencia concreta: {contradicao}. "
            f"Preservar fatos travados e evitar atribuicao de intencao nao provada. Titulo de referencia: {titulo}."
        )

    @staticmethod
    def _frame_visual(primary_entity: str, contradicao: str) -> dict[str, str]:
        return {
            "entidade_principal": primary_entity or "entidade principal da pauta",
            "conflito_visual": contradicao,
            "evitar": "montagem generica, multidao indistinta, imagem sem relacao com a tese",
            "prioridade": "pessoa" if primary_entity else "instituicao",
        }

    @staticmethod
    def _curadoria_id(item_id: str, leitura: dict[str, Any]) -> str:
        raw = json.dumps({"item_id": item_id, "leitura": leitura}, ensure_ascii=False, sort_keys=True)
        return "cur_" + hashlib.sha256(raw.encode("utf-8")).hexdigest()[:16]

    def _anti_echo_issues(self, payload: dict[str, Any]) -> list[str]:
        issues: list[str] = []
        cfg = self.contract.get("validacoes", {}).get("anti_eco_template", {})
        if not cfg.get("enabled"):
            return issues
        prefixes = tuple(cfg.get("blocked_prefixes", []))
        for field_name in cfg.get("applies_to", []):
            value = str(payload.get(field_name, ""))
            if field_name == "tese_escolhida":
                idx = payload.get("tese_escolhida_idx")
                teses = payload.get("teses_candidatas") or []
                value = next((str(item.get("tese", "")) for item in teses if item.get("idx") == idx), "")
            if prefixes and value.startswith(prefixes):
                issues.append(f"anti_eco_template:{field_name}")
        return issues

    def _real_publish_source_issues(
        self,
        payload: dict[str, Any],
        mode: str,
        real_wordpress_draft: bool,
    ) -> list[str]:
        cfg = self.contract.get("leitura_corrente_timestamped", {}).get("fase_1", {})
        if cfg.get("publicacao_real_exige_fonte_nao_manual") is not True:
            return []
        is_real = real_wordpress_draft or mode in {"real", "draft_wordpress", "pending_wordpress", "publish_wordpress"}
        if not is_real:
            return []
        leitura = payload.get("leitura_corrente_timestamped") or {}
        fonte = leitura.get("fonte", leitura.get("source"))
        aliases = self.contract["leitura_corrente_timestamped"].get("aliases_aceitos_na_entrada", {})
        fonte = aliases.get(str(fonte), fonte)
        if not fonte:
            return ["leitura_corrente_fonte_obrigatoria_para_publicacao_real"]
        if fonte == "manual_editor":
            return ["leitura_corrente_manual_bloqueada_publicacao_real"]
        return []

    def collection_blocks_stage(self, collection: dict[str, Any], stage: str) -> bool:
        status = collection.get("status")
        required_before = collection.get("required_before")
        if status == "none" or required_before in (None, "none"):
            return False
        order = self.contract.get("collection_request", {}).get("required_before_enum", [])
        stage_order = [item for item in order if item != "none"]
        if stage not in stage_order or required_before not in stage_order:
            return False
        return stage_order.index(stage) >= stage_order.index(required_before) and status in {"recommended", "required"}

    def _only_generic_tese(self, tese: str) -> bool:
        cfg = self.contract.get("validacoes", {}).get("advogado_do_obvio", {})
        generic_terms = [item.lower() for item in cfg.get("reject_if_only_generic_terms", [])]
        normalized = tese.lower()
        concrete_hits = self._concrete_anchor_hits(tese, {})
        return not concrete_hits and any(term in normalized for term in generic_terms)

    def _concrete_anchor_hits(self, tese: str, consequencia_material: dict[str, Any]) -> list[str]:
        cfg = self.contract.get("validacoes", {}).get("advogado_do_obvio", {})
        haystack = " ".join(
            [
                tese,
                str(consequencia_material.get("descricao", "")),
                str(consequencia_material.get("quem_ganha", "")),
                str(consequencia_material.get("quem_perde", "")),
            ]
        ).lower()
        hits: list[str] = []
        for anchor in cfg.get("required_concrete_anchors", []):
            if anchor.lower() in haystack:
                hits.append(anchor)
        return hits

    @staticmethod
    def _missing(value: Any) -> bool:
        return value in (None, "", []) or value == {}

    @staticmethod
    def _source_for_sentence(
        sentence: str,
        fontes: list[Any],
        active_label: str,
        active_ref: str,
    ) -> tuple[str, str]:
        lower = sentence.lower()
        if "associated press" in lower or lower.startswith("ap "):
            return "Associated Press", V4CuradoriaTese._source_ref(fontes, "apnews")
        if "el pais" in lower or "el país" in lower:
            return "El País", V4CuradoriaTese._source_ref(fontes, "elpais")
        if "a reportagem registra" in lower and active_label:
            return active_label, active_ref
        return active_label, active_ref

    @staticmethod
    def _source_ref(fontes: list[Any], marker: str) -> str:
        for fonte in fontes:
            text = str(fonte)
            if marker in text.lower():
                return text
        return str(fontes[0]) if fontes else "fonte_auditada"

    @staticmethod
    def _fact_with_source(sentence: str, source_label: str) -> str:
        if not source_label:
            return sentence
        lower = sentence.lower()
        if "associated press" in lower or "el pais" in lower or "el país" in lower:
            return sentence
        if lower.startswith("a reportagem registra que "):
            prefix = "A Associated Press" if source_label == "Associated Press" else f"O {source_label}"
            return prefix + " registra que " + sentence[len("A reportagem registra que "):]
        return sentence

    @staticmethod
    def _now_brt() -> str:
        return datetime.now(timezone.utc).astimezone().isoformat()
