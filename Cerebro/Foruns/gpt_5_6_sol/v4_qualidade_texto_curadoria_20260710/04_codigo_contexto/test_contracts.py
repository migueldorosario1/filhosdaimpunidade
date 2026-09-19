from __future__ import annotations

import json
import hashlib
import os
import sqlite3
import tempfile
import threading
from contextlib import contextmanager
from pathlib import Path

from .fluxo import V4DryRunFlow
from .curadoria_tese import V4CuradoriaTese
from .coerencia_editorial import V4EditorialCoherenceGate
from .ab_experiment import V4CuradoriaABExperiment
from .agentes import TechnicalAgentFactory
from .auditoria_final import V4FinalAuditAgent
from .content_ingestion import V4ContentIngestion
from .fact_check import V4FactCheckAgent
from .feedback import V4EditorFeedbackStore
from .imagem_destacada import MediaCandidate, V4FeaturedImageEvaluator
from .llm_dashboard import V4LLMDashboard
from .llm_decisions import LLMRouterDecision, V4LLMDecisionStore
from .llm_adapter import V4LLMAdapter, V4LLMRealCallError
from .media_audit import V4AuditedMediaStore
from .media_sources import V4MediaSourceCollector
from .pricing import V4Pricing
from .operational_dashboard import V4OperationalDashboard
from .promocao import V4PromotionPreflight
from .recompute_costs import V4CostRecomputer
from .model_router import V4ModelRouter
from .multi_item import V4MultiItemLabRunner
from .redator_shadow import V4ShadowRedator
from .redator_real import V4RealRedator
from .revisao import V4ReviewAgent
from .telemetry import LLMCallDetail, TelemetryReceipt, V4Telemetry
from .wordpress_publicador import V4WordPressPublisher
from .wordpress_media import V4WordPressMediaMapper, WordPressMediaMapping


def main() -> int:
    tests = [
        test_recibo_com_todos_required_fields_grava_ok,
        test_recibo_faltando_required_field_retorna_ok_false,
        test_prometheus_com_label_proibido_retorna_ok_false,
        test_dry_run_nao_grava_arquivo,
        test_dois_writers_simultaneos_nao_corrompem_jsonl,
        test_timestamp_formato_invalido_erra_cedo,
        test_vertical_com_slash_erra_cedo,
        test_publicacao_bloqueada_quando_record_receipt_ok_false,
        test_feedback_score_invalido_retorna_ok_false,
        test_feedback_ranking_agrega_provider_model,
        test_pricing_estima_custo_versionado,
        test_pricing_usa_tokens_reais_quando_disponiveis,
        test_recompute_costs_append_only_recalcula_pendente,
        test_recompute_costs_recalcula_versao_antiga_com_custo_positivo,
        test_feedback_ranking_usa_custo_recomputado,
        test_model_router_recomenda_por_qualidade_custo,
        test_model_router_respeita_exclude_provider,
        test_llm_decision_store_grava_jsonl,
        test_llm_decision_faltando_required_retorna_ok_false,
        test_llm_dashboard_grava_json_e_markdown,
        test_llm_dashboard_markdown_contem_ranking_e_decisoes,
        test_curadoria_cria_tres_teses_e_frame_visual,
        test_curadoria_tem_consequencia_material_e_collection_request,
        test_curadoria_reconhece_pauta_industrial_ibge,
        test_curadoria_reconhece_pauta_judicial_politica_internacional,
        test_fluxo_produtor_inclui_fatos_travados_no_contexto,
        test_curadoria_dict_vazio_em_required_bloqueia,
        test_curadoria_fatos_travados_preservam_atribuicao,
        test_curadoria_sem_fonte_leitura_corrente_bloqueia,
        test_producao_sem_curadoria_bloqueia,
        test_modo_experimento_sem_curadoria_somente_dry_run,
        test_publicacao_real_bloqueia_fonte_manual,
        test_redator_shadow_gera_prompt_sem_chamada_externa,
        test_collection_recommended_bloqueia_no_estagio_indicado,
        test_redator_real_preflight_nao_bloqueia_collection_resolvida_por_decisao_editorial,
        test_redator_real_preflight_bloqueia_collection_redator_real,
        test_redator_real_preflight_bloqueia_adapter_real_desligado,
        test_redator_real_bloqueia_saida_curta_ou_interrompida,
        test_redator_real_fallback_tenta_proximo_modelo_quando_primeiro_falha,
        test_deepseek_v4_pro_fica_fallback_por_rota_externa_sem_hardcode,
        test_adapter_obedece_temperature_flag_do_modelo,
        test_sanitize_error_cobre_chaves_nao_sk,
        test_redator_real_grava_recibo_jsonl_sem_prompt_ou_texto,
        test_foruns_v4_nao_contem_fontes_vivas_e_v4_labs_existe,
        test_fluxo_dry_run_executa_curadoria_antes_da_producao,
        test_agentes_revisor_fact_checker_e_auditor_final_existem,
        test_revisao_bloqueia_meta_linguagem_e_texto_curto,
        test_fact_check_bloqueia_fato_obrigatorio_sem_fonte,
        test_fact_check_bloqueia_fato_obrigatorio_ausente_do_texto,
        test_fact_check_preserva_tokens_numericos_e_bloqueia_percentual_errado,
        test_auditoria_final_exige_revisao_e_fact_check_aprovados,
        test_fluxo_dry_run_inclui_revisao_fact_check_auditoria,
        test_fluxo_dry_run_detecta_saida_bloqueada_ou_incompleta,
        test_fluxo_producao_nao_regenera_artefato_bloqueado,
        test_editorial_coherence_gate_flagra_template_industrial_em_cultura,
        test_editorial_coherence_gate_aprova_tese_cultural_com_eixo_formal,
        test_editorial_coherence_gate_tese_ausente_vira_warning,
        test_multi_item_lab_congela_curadoria_e_grava_relatorio,
        test_multi_item_lab_detecta_curadoria_alterada,
        test_rascunho_primeiro_contrato_diferencia_rascunho_de_promocao,
        test_ab_261439_grava_pacote_cego_sem_publicacao,
        test_imagem_destacada_aprova_candidato_com_direitos_e_entidade,
        test_imagem_destacada_rejeita_thumbnail_sem_direitos,
        test_imagem_destacada_grava_decisao_append_only,
        test_media_source_ouro_sqlite_normaliza_candidato,
        test_media_source_ouro_sqlite_indisponivel_nao_quebra,
        test_media_source_path_exists_trata_oserror,
        test_media_audit_promove_aprovada_e_busca_por_entidade,
        test_media_audit_bloqueia_avaliacao_reprovada,
        test_fluxo_publicacao_sem_midia_auditada_segue_com_warning,
        test_fluxo_publicacao_anexa_midia_auditada,
        test_wordpress_publicador_dry_run_grava_tentativa,
        test_wordpress_publicador_real_bloqueado_por_contrato,
        test_wordpress_publicador_rascunho_sem_featured_media_vira_warning,
        test_wordpress_publicador_rascunho_sem_curadoria_id_vira_warning,
        test_wordpress_publicador_real_bloqueia_ascii_sem_acentos,
        test_wordpress_publicador_real_bloqueia_collection_request_ausente,
        test_wordpress_publicador_real_bloqueia_collection_request_publicacao_real,
        test_wordpress_publicador_real_draft_bloqueia_campos_criticos,
        test_wordpress_publicador_real_draft_bloqueia_collection_request_publicacao_real,
        test_wordpress_publicador_collection_request_fail_closed_valores_desconhecidos,
        test_wordpress_publicador_collection_request_nao_string_vira_issue,
        test_promocao_preflight_collection_request_fail_closed_valores_desconhecidos,
        test_promocao_preflight_collection_request_nao_string_vira_issue,
        test_wordpress_media_mapping_append_lookup,
        test_wordpress_publicador_usa_mapping_wp_media_id,
        test_promocao_preflight_bloqueia_pendencias_de_promocao,
        test_promocao_preflight_aprova_fixture_limpa_ratificada,
        test_promocao_preflight_detecta_sk_generico,
        test_promocao_preflight_exige_evidencia_para_decisao_true,
        test_operational_dashboard_grava_json_markdown,
        test_content_ingestion_cria_bruto_intermediario_auditado,
        test_content_ingestion_coletor_nao_escreve_auditado,
    ]
    failures: list[str] = []
    for test in tests:
        try:
            test()
        except Exception as exc:  # noqa: BLE001 - runner minimalista de contrato
            failures.append(f"{test.__name__}: {exc}")
    if failures:
        for failure in failures:
            print(f"FAIL {failure}")
        return 2
    print(f"OK {len(tests)} contract tests")
    return 0


def test_recibo_com_todos_required_fields_grava_ok() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        telemetry = V4Telemetry(root=tmp, contract_path=_copy_contract(tmp))
        result = telemetry.record_receipt(_sample_receipt(), execute=True)
        assert result["ok"] is True
        assert Path(tmp, result["path"]).exists()


def test_recibo_faltando_required_field_retorna_ok_false() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        telemetry = V4Telemetry(root=tmp, contract_path=_copy_contract(tmp))
        payload = _sample_receipt().as_dict()
        del payload["schema_version"]
        errors = telemetry._validate_receipt(payload)
        assert errors


def test_prometheus_com_label_proibido_retorna_ok_false() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        telemetry = V4Telemetry(root=tmp, contract_path=_copy_contract(tmp))
        result = telemetry.push_prometheus_counter("v4_llm_calls_total", {"provider": "mock", "post_id": "1"})
        assert result["ok"] is False


def test_dry_run_nao_grava_arquivo() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        telemetry = V4Telemetry(root=tmp, contract_path=_copy_contract(tmp))
        result = telemetry.record_receipt(_sample_receipt(), execute=False)
        assert result["ok"] is True
        assert not Path(tmp, result["path"]).exists()


def test_dois_writers_simultaneos_nao_corrompem_jsonl() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        telemetry = V4Telemetry(root=tmp, contract_path=_copy_contract(tmp))

        def write(index: int) -> None:
            receipt = _sample_receipt(item_id=f"item_{index}")
            result = telemetry.record_receipt(receipt, execute=True)
            assert result["ok"] is True

        threads = [threading.Thread(target=write, args=(index,)) for index in range(20)]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        receipt_path = Path(tmp, "agent_data/v4/receipts/v4_test_20260708.jsonl")
        lines = receipt_path.read_text(encoding="utf-8").splitlines()
        assert len(lines) == 20
        for line in lines:
            json.loads(line)


def test_timestamp_formato_invalido_erra_cedo() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        telemetry = V4Telemetry(root=tmp, contract_path=_copy_contract(tmp))
        receipt = _sample_receipt(timestamp="08/07/2026")
        result = telemetry.record_receipt(receipt, execute=True)
        assert result["ok"] is False
        assert "timestamp deve ser ISO8601" in result["errors"][0]


def test_vertical_com_slash_erra_cedo() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        telemetry = V4Telemetry(root=tmp, contract_path=_copy_contract(tmp))
        receipt = _sample_receipt(vertical="../../etc/passwd")
        result = telemetry.record_receipt(receipt, execute=True)
        assert result["ok"] is False
        assert "vertical invalida" in result["errors"][0]


def test_publicacao_bloqueada_quando_record_receipt_ok_false() -> None:
    class BadTelemetry:
        def record_receipt(self, receipt: TelemetryReceipt, execute: bool = False) -> dict[str, object]:
            return {"ok": False, "errors": ["falha simulada"]}

    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        source = root / "source.json"
        target = root / "target.json"
        source.write_text('{"item_id":"x"}', encoding="utf-8")
        flow = V4DryRunFlow.__new__(V4DryRunFlow)
        flow.root = root
        flow.telemetry = BadTelemetry()
        flow._check_access = lambda role, source_layer, target_layer: []  # type: ignore[method-assign]
        flow._target_path = lambda step_name, layer, item_id: target  # type: ignore[method-assign]
        flow._read_json = lambda path: {"item_id": "x"}  # type: ignore[method-assign]
        flow._build_output = lambda step, source_payload, editoria, idem: {  # type: ignore[method-assign]
            "item_id": "x",
            "editoria": "v4_test",
            "status": "auditar_final_dry_run",
            "source_status": "produzir_dry_run",
        }
        step = {"name": "auditar_final_dry_run", "role": "auditor", "from": "producao", "to": "auditado"}
        result = flow._run_step(step, source, "x", "v4_test", execute=True)
        assert result.mode == "blocked_receipt"
        assert result.issues
        assert not target.exists()


def test_feedback_score_invalido_retorna_ok_false() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        contract = _copy_feedback_contract(tmp)
        store = V4EditorFeedbackStore(root=tmp, contract_path=contract)
        result = store.record(
            item_id="x",
            vertical="v4_test",
            editor="miguel",
            score=9,
            sentiment="positivo",
            comment="score invalido",
            correction_class="nenhuma",
        )
        assert result["ok"] is False


def test_feedback_ranking_agrega_provider_model() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        contract = _copy_feedback_contract(tmp)
        store = V4EditorFeedbackStore(root=tmp, contract_path=contract)
        for score in [4, 5]:
            result = store.record(
                item_id=f"x{score}",
                vertical="v4_test",
                editor="miguel",
                score=score,
                sentiment="positivo",
                comment="bom",
                correction_class="nenhuma",
                provider="mock",
                model="v4-mock-local",
                execute=True,
            )
            assert result["ok"] is True
        ranking = store.ranking()
        assert ranking[0]["provider"] == "mock"
        assert ranking[0]["model"] == "v4-mock-local"
        assert ranking[0]["samples"] == 2
        assert ranking[0]["avg_score"] == 4.5


def test_pricing_estima_custo_versionado() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        contract = _copy_pricing_contract(tmp)
        pricing = V4Pricing(root=tmp, contract_path=contract)
        estimate = pricing.estimate("gpt-5.5", "a" * 400, "b" * 400)
        assert estimate.tokens_in == 100
        assert estimate.tokens_out == 100
        assert estimate.cost_usd_estimated > 0
        assert estimate.pricing_table_version == "2026-07-09-official-deepseek"


def test_pricing_usa_tokens_reais_quando_disponiveis() -> None:
    pricing = V4Pricing(root=".")
    estimate = pricing.estimate_by_tokens("deepseek-v4-pro", 5206, 2339)
    expected = round(((5206 * 0.435) + (2339 * 0.87)) / 1_000_000, 8)
    assert estimate.tokens_in == 5206
    assert estimate.tokens_out == 2339
    assert estimate.cost_usd_estimated == expected
    assert estimate.cost_usd_estimated > 0.004


def test_recompute_costs_append_only_recalcula_pendente() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        contract = _copy_recompute_contract(tmp)
        _copy_pricing_contract(tmp)
        receipt_dir = Path(tmp, "agent_data/v4/receipts")
        receipt_dir.mkdir(parents=True, exist_ok=True)
        receipt_path = receipt_dir / "v4_test_20260708.jsonl"
        original = json.dumps(_old_pending_receipt(), ensure_ascii=False, sort_keys=True) + "\n"
        receipt_path.write_text(original, encoding="utf-8")
        production_path = Path(tmp, "dados/producao/item_old.producao.json")
        production_path.parent.mkdir(parents=True, exist_ok=True)
        production_path.write_text(
            json.dumps(
                {
                    "item_id": "item_old",
                    "conteudo": "Texto auditado de entrada para recomputar custo.",
                    "texto_dry_run": "Texto produzido antigo para recomputar custo.",
                },
                ensure_ascii=False,
            ),
            encoding="utf-8",
        )

        recomputer = V4CostRecomputer(root=tmp, contract_path=contract)
        result = recomputer.run(execute=True)
        assert result["ok"] is True
        recomputed = [item for item in result["results"] if item["status"] == "recomputed"]
        assert recomputed
        assert recomputed[0]["new_cost_usd_estimated"] > 0
        assert receipt_path.read_text(encoding="utf-8") == original
        output_files = list(Path(tmp, "agent_data/v4/receipts/recomputed").glob("*.jsonl"))
        assert output_files
        second_run = recomputer.run(execute=True)
        assert second_run["appended_count"] == 0
        assert second_run["results"][0]["status"] == "skipped_already_recorded"


def test_recompute_costs_recalcula_versao_antiga_com_custo_positivo() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        contract = _copy_recompute_contract(tmp)
        _copy_pricing_contract(tmp)
        receipt_dir = Path(tmp, "agent_data/v4/receipts")
        receipt_dir.mkdir(parents=True, exist_ok=True)
        receipt = _old_pending_receipt()
        receipt["pricing_table_version"] = "2026-07-08-local-ratings"
        receipt["cost_usd_estimated"] = 0.00165447
        receipt["llm"]["model"] = "deepseek-v4-pro"
        receipt["llm"]["provider"] = "deepseek"
        receipt["llm"]["tokens_in"] = 5206
        receipt["llm"]["tokens_out"] = 2339
        receipt_path = receipt_dir / "v4_test_20260709.jsonl"
        original = json.dumps(receipt, ensure_ascii=False, sort_keys=True) + "\n"
        receipt_path.write_text(original, encoding="utf-8")

        result = V4CostRecomputer(root=tmp, contract_path=contract).run(execute=True)

        recomputed = [item for item in result["results"] if item["status"] == "recomputed"]
        assert recomputed
        assert recomputed[0]["old_cost_usd_estimated"] == 0.00165447
        assert recomputed[0]["new_pricing_table_version"] == "2026-07-09-official-deepseek"
        assert recomputed[0]["new_cost_usd_estimated"] > recomputed[0]["old_cost_usd_estimated"]
        assert receipt_path.read_text(encoding="utf-8") == original


def test_feedback_ranking_usa_custo_recomputado() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        contract = _copy_feedback_contract(tmp)
        receipt_dir = Path(tmp, "agent_data/v4/receipts")
        receipt_dir.mkdir(parents=True, exist_ok=True)
        receipt_path = receipt_dir / "v4_test_20260708.jsonl"
        receipt_path.write_text(json.dumps(_old_pending_receipt(), sort_keys=True) + "\n", encoding="utf-8")
        recomputed_dir = receipt_dir / "recomputed"
        recomputed_dir.mkdir(parents=True, exist_ok=True)
        recomputed_dir.joinpath("recomputed_20260708.jsonl").write_text(
            json.dumps(
                {
                    "schema_version": "v1",
                    "timestamp": "2026-07-08T00:00:00+00:00",
                    "source_receipt_file": "agent_data/v4/receipts/v4_test_20260708.jsonl",
                    "item_id": "item_old",
                    "vertical": "v4_test",
                    "operation": "produzir_dry_run",
                    "provider": "openai",
                    "model": "gpt-5.5",
                    "old_cost_usd_estimated": 0.0,
                    "new_cost_usd_estimated": 0.001,
                    "old_pricing_table_version": "pending",
                    "new_pricing_table_version": "2026-07-08-local-ratings",
                    "tokens_in": 100,
                    "tokens_out": 100,
                    "status": "recomputed",
                },
                sort_keys=True,
            )
            + "\n",
            encoding="utf-8",
        )
        store = V4EditorFeedbackStore(root=tmp, contract_path=contract)
        result = store.record(
            item_id="item_old",
            vertical="v4_test",
            editor="miguel",
            score=5,
            sentiment="positivo",
            comment="bom",
            correction_class="nenhuma",
            provider="openai",
            model="gpt-5.5",
            execute=True,
        )
        assert result["ok"] is True
        ranking = store.ranking()
        assert ranking[0]["avg_cost_usd_estimated"] == 0.001
        assert ranking[0]["score_per_usd_estimated"] == 5000.0


def test_model_router_recomenda_por_qualidade_custo() -> None:
    router = V4ModelRouter()
    recommendation = router.recommend("v4_ciencia_tecnologia_ia", "redacao", "contract-test")
    assert recommendation.selected.selection.provider == "gemini"
    assert recommendation.selected.selection.model == "gemini-3.5-flash"
    assert recommendation.selected.expected_cost_usd > 0


def test_model_router_respeita_exclude_provider() -> None:
    router = V4ModelRouter()
    recommendation = router.recommend(
        "v4_ciencia_tecnologia_ia",
        "redacao",
        "contract-test",
        exclude_provider="gemini",
    )
    assert recommendation.selected.selection.provider != "gemini"


def test_llm_decision_store_grava_jsonl() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        contract = _copy_llm_decisions_contract(tmp)
        store = V4LLMDecisionStore(root=tmp, contract_path=contract)
        result = store.record(_sample_decision(), execute=True)
        assert result["ok"] is True
        assert Path(tmp, result["path"]).exists()


def test_llm_decision_faltando_required_retorna_ok_false() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        contract = _copy_llm_decisions_contract(tmp)
        store = V4LLMDecisionStore(root=tmp, contract_path=contract)
        payload = _sample_decision().as_dict()
        del payload["prompt_hash"]
        errors = store._validate(payload)
        assert errors


def test_llm_dashboard_grava_json_e_markdown() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        contract = _copy_dashboard_contract(tmp)
        _seed_dashboard_data(tmp)
        dashboard = V4LLMDashboard(root=tmp, contract_path=contract)
        result = dashboard.build(execute=True)
        assert result["ok"] is True
        assert Path(tmp, result["json_path"]).exists()
        assert Path(tmp, result["markdown_path"]).exists()
        assert result["report"]["summary"]["router_decisions"] == 1


def test_llm_dashboard_markdown_contem_ranking_e_decisoes() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        contract = _copy_dashboard_contract(tmp)
        _seed_dashboard_data(tmp)
        dashboard = V4LLMDashboard(root=tmp, contract_path=contract)
        result = dashboard.build()
        markdown = dashboard.to_markdown(result["report"])
        assert "Ranking Qualidade/Custo" in markdown
        assert "gemini/gemini-3.5-flash" in markdown


def test_curadoria_cria_tres_teses_e_frame_visual() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        _copy_curadoria_contract(tmp)
        curadoria = V4CuradoriaTese(root=tmp)
        source = _sample_auditado_payload()
        source["conteudo"] = (
            "A Associated Press informou que Flavio enviou documento ao USTR defendendo adiamento da tarifa. "
            "O El Pais destacou a disputa sobre o Pix."
        )
        source["fontes"] = ["https://apnews.com/example", "https://elpais.com/example"]
        payload = curadoria.create(source, _sample_leitura_corrente())
        assert payload["status"] == "curadoria_dry_run"
        assert payload["curadoria_id"].startswith("cur_")
        assert len(payload["fatos_travados"]) >= 2
        assert payload["consequencia_material"]["nivel_concretude"] >= 3
        assert len(payload["teses_candidatas"]) == 3
        assert payload["teses_candidatas"][payload["tese_escolhida_idx"]]["status"] == "escolhida"
        assert payload["frame_visual"]["entidade_principal"] == "Flavio Bolsonaro"
        assert curadoria.validate(payload).ok is True


def test_curadoria_tem_consequencia_material_e_collection_request() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        _copy_curadoria_contract(tmp)
        curadoria = V4CuradoriaTese(root=tmp)
        source = _sample_auditado_payload()
        source["conteudo"] = (
            "A Associated Press informou que Flavio enviou documento ao USTR defendendo adiamento da tarifa. "
            "O El Pais destacou a disputa sobre o Pix."
        )
        source["fontes"] = ["https://apnews.com/example", "https://elpais.com/example"]
        payload = curadoria.create(source, _sample_leitura_corrente())
        consequencia = payload["consequencia_material"]
        assert consequencia["tipo"] == "economica_eleitoral"
        assert "Pix" in consequencia["descricao"]
        assert payload["collection_request"]["status"] == "recommended"
        assert payload["collection_request"]["required_before"] == "redator_real_llm"


def test_curadoria_reconhece_pauta_industrial_ibge() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        _copy_curadoria_contract(tmp)
        curadoria = V4CuradoriaTese(root=tmp)
        source = _sample_auditado_payload()
        source["titulo"] = "IBGE mostra avanço do setor produtivo industrial"
        source["conteudo"] = (
            "O IBGE informou que a produção industrial cresceu e que o setor produtivo segue acima do patamar pré-pandemia. "
            "A leitura principal envolve indústria, valor agregado e política econômica."
        )
        payload = curadoria.create(source, _sample_leitura_corrente())
        assert payload["status"] == "curadoria_dry_run"
        assert payload["consequencia_material"]["tipo"] == "economica"
        assert "setor produtivo" in payload["consequencia_material"]["descricao"]
        assert payload["collection_request"]["status"] == "none"
        assert "pressao tarifaria" not in payload["teses_candidatas"][0]["tese"]
        assert "pressao externa" not in payload["teses_candidatas"][0]["tese"]


def test_curadoria_reconhece_pauta_judicial_politica_internacional() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        _copy_curadoria_contract(tmp)
        curadoria = V4CuradoriaTese(root=tmp)
        source = _sample_auditado_payload()
        source["primary_entity"] = "Jason Miller"
        source["titulo"] = "Documentos judiciais expõem operador ligado a Trump"
        source["conteudo"] = (
            "Documentos judiciais nos Estados Unidos citam Jason Miller e a Gettr. "
            "O caso conecta Washington, Trump e a eleição brasileira."
        )
        payload = curadoria.create(source, _sample_leitura_corrente())
        assert payload["status"] == "curadoria_dry_run"
        assert payload["consequencia_material"]["tipo"] == "institucional"
        assert "Washington" in payload["consequencia_material"]["descricao"]


def test_fluxo_produtor_inclui_fatos_travados_no_contexto() -> None:
    source_payload = {
        "briefing_produtor": "Abrir pela contradicao.",
        "fatos_travados": [
            {"fato": "O IBGE informou alta de 0,7% da producao industrial."},
            {"fato": "A industria ficou 12,9% abaixo do recorde."},
        ],
        "collection_request": {"status": "none", "reason": "sem pendencia"},
    }
    context = V4DryRunFlow._producer_context(source_payload, {"conteudo": ""})
    assert "Fatos travados obrigatorios" in context
    assert "0,7%" in context
    assert "12,9%" in context


def test_curadoria_dict_vazio_em_required_bloqueia() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        _copy_curadoria_contract(tmp)
        curadoria = V4CuradoriaTese(root=tmp)
        payload = curadoria.create(_sample_auditado_payload(), _sample_leitura_corrente())
        payload["consequencia_material"] = {}
        validation = curadoria.validate(payload)
        assert validation.ok is False
        assert "campo_curadoria_ausente:consequencia_material" in validation.issues


def test_curadoria_fatos_travados_preservam_atribuicao() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        _copy_curadoria_contract(tmp)
        source = _sample_auditado_payload()
        source["conteudo"] = (
            "A Associated Press informou que Lula e Flavio Bolsonaro entraram em confronto politico. "
            "A reportagem registra que Flavio enviou documento ao USTR defendendo adiamento da medida. "
            "O El Pais informou que o Pix virou ponto sensivel da discussao."
        )
        source["fontes"] = ["https://apnews.com/example", "https://elpais.com/example"]
        payload = V4CuradoriaTese(root=tmp).create(source, _sample_leitura_corrente())
        fatos = payload["fatos_travados"]
        assert "Associated Press registra que Flavio enviou documento ao USTR" in fatos[1]["fato"]
        assert fatos[1]["fonte_ref"] == ["https://apnews.com/example"]
        assert "El Pais" in fatos[2]["fato"]
        assert fatos[2]["fonte_ref"] == ["https://elpais.com/example"]


def test_curadoria_sem_fonte_leitura_corrente_bloqueia() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        _copy_curadoria_contract(tmp)
        curadoria = V4CuradoriaTese(root=tmp)
        leitura = _sample_leitura_corrente()
        del leitura["fonte"]
        payload = curadoria.create(_sample_auditado_payload(), leitura)
        assert payload["status"] == "curadoria_invalida"
        assert "leitura_corrente_campo_ausente:fonte" in payload["issues"]


def test_producao_sem_curadoria_bloqueia() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        _copy_curadoria_contract(tmp)
        curadoria = V4CuradoriaTese(root=tmp)
        result = curadoria.validate_gate(_sample_auditado_payload(), mode="dry_run")
        assert result.ok is False
        assert "curadoria_id_obrigatorio" in result.issues


def test_modo_experimento_sem_curadoria_somente_dry_run() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        _copy_curadoria_contract(tmp)
        curadoria = V4CuradoriaTese(root=tmp)
        payload = _sample_auditado_payload()
        dry = curadoria.validate_gate(payload, mode="dry_run_ab_261439", modo_experimento=True)
        real = curadoria.validate_gate(payload, mode="real", modo_experimento=True, real_wordpress_draft=True)
        assert dry.ok is True
        assert real.ok is False


def test_publicacao_real_bloqueia_fonte_manual() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        _copy_curadoria_contract(tmp)
        curadoria = V4CuradoriaTese(root=tmp)
        payload = curadoria.create(_sample_auditado_payload(), _sample_leitura_corrente())
        result = curadoria.validate_gate(payload, mode="real", real_wordpress_draft=True)
        assert result.ok is False
        assert "leitura_corrente_manual_bloqueada_publicacao_real" in result.issues


def test_redator_shadow_gera_prompt_sem_chamada_externa() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        _copy_curadoria_contract(tmp)
        _copy_redator_shadow_contract(tmp)
        curadoria = V4CuradoriaTese(root=tmp).create(_sample_auditado_payload(), _sample_leitura_corrente())
        result = V4ShadowRedator(root=tmp).create(curadoria, execute=True)
        assert result["status"] == "shadow_redacao_pronta"
        assert result["external_call"] is False
        assert result["wordpress_real"] is False
        assert result["selected_route"]["route_context"] == "v4_super_luxo_redacao"
        assert "Fatos travados obrigatorios" in result["prompt_shadow"]
        assert Path(tmp, "dados/producao_shadow/v4_real_001.shadow_redacao.json").exists()


def test_collection_recommended_bloqueia_no_estagio_indicado() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        _copy_redator_shadow_contract(tmp)
        redator = V4ShadowRedator(root=tmp)
        collection = {
            "status": "recommended",
            "reason": "fonte primaria pendente",
            "queries": ["USTR Brazil tariff"],
            "required_before": "redator_real_llm",
        }
        assert redator.collection_blocks_stage(collection, "shadow_redacao") is False
        assert redator.collection_blocks_stage(collection, "redator_real_llm") is True
        assert redator.collection_blocks_stage(collection, "publicacao_real") is True


def test_redator_real_preflight_nao_bloqueia_collection_resolvida_por_decisao_editorial() -> None:
    curadoria = json.loads(Path("dados/curadoria/v4_real_001.curadoria.json").read_text(encoding="utf-8"))
    result = V4RealRedator(root=".").preflight(curadoria)
    assert "real_collection_request_bloqueia_redator_real" not in result["issues"]
    assert result["collection_request"]["status"] == "resolved"
    assert result["collection_request"]["required_before"] == "none"
    assert result["collection_request"]["resolved_by"] == "Miguel"


def test_redator_real_preflight_bloqueia_collection_redator_real() -> None:
    curadoria = json.loads(Path("dados/curadoria/v4_real_001.curadoria.json").read_text(encoding="utf-8"))
    curadoria["collection_request"] = {
        "status": "recommended",
        "reason": "fonte primaria pendente",
        "queries": ["USTR Brazil tariff"],
        "required_before": "redator_real_llm",
    }
    result = V4RealRedator(root=".").preflight(curadoria)
    assert "real_collection_request_bloqueia_redator_real" in result["issues"]


def test_redator_real_preflight_bloqueia_adapter_real_desligado() -> None:
    curadoria = json.loads(Path("dados/curadoria/v4_real_001.curadoria.json").read_text(encoding="utf-8"))
    result = V4RealRedator(root=".").preflight(curadoria)
    assert result["status"] == "redator_real_llm_bloqueado"
    assert any(issue.startswith("adapter_real_bloqueado:") for issue in result["issues"])
    assert result["external_call_executed"] is False
    assert result["wordpress_real"] is False


def test_redator_real_bloqueia_saida_curta_ou_interrompida() -> None:
    redator = V4RealRedator(root=".")
    assert "real_output_curto" in redator._real_text_issues("texto curto")[0]
    issues = redator._real_text_issues("x" * 4000 + "-")
    assert "real_output_interrompido" in issues


def test_redator_real_fallback_tenta_proximo_modelo_quando_primeiro_falha() -> None:
    class FakeHealthReport:
        ok = True
        issues: list[str] = []

        def as_dict(self) -> dict[str, object]:
            return {"ok": True, "issues": []}

    class FakeHealth:
        def check(self, editoria: str, funcao: str) -> FakeHealthReport:
            return FakeHealthReport()

    class FakeResponse:
        provider = "anthropic"
        model = "claude-sonnet-4-6"
        route_context = "v4_super_luxo_redacao"
        selected_tier = "anthropic_luxo"
        selection_reason = "fake fallback intra-provider success"
        content = "Texto completo com tese, fato e consequência material. " * 90

        def as_dict(self) -> dict[str, object]:
            return {
                "provider": self.provider,
                "model": self.model,
                "content": self.content,
                "route_context": self.route_context,
                "selected_tier": self.selected_tier,
                "selection_reason": self.selection_reason,
            }

    class FakeAdapter:
        def __init__(self) -> None:
            self.previous_providers: list[str | None] = []
            self.previous_models: list[str | None] = []

        def generate(self, request: object, mode: str | None = None) -> FakeResponse:
            previous_provider = getattr(request, "previous_provider")
            previous_model = getattr(request, "previous_model")
            self.previous_providers.append(previous_provider)
            self.previous_models.append(previous_model)
            if len(self.previous_providers) == 1:
                raise V4LLMRealCallError("anthropic", "claude-opus-4-8", "erro fake")
            assert previous_provider is None
            assert previous_model == "claude-opus-4-8"
            assert mode == "real"
            return FakeResponse()

    redator = V4RealRedator(root=".")
    fake_adapter = FakeAdapter()
    redator.healthcheck = FakeHealth()  # type: ignore[assignment]
    redator._make_adapter = lambda: fake_adapter  # type: ignore[method-assign]
    redator.validate = lambda curadoria: []  # type: ignore[method-assign]
    redator.contract["fallback"]["max_attempts"] = 2
    redator.contract["fallback"]["retry_on_error"] = True
    curadoria = json.loads(Path("dados/curadoria/v4_real_001.curadoria.json").read_text(encoding="utf-8"))

    result = redator.call_real(curadoria)

    assert result["status"] == "redator_real_llm_pronto"
    assert result["selected_route"]["provider"] == "anthropic"
    assert result["selected_route"]["model"] == "claude-sonnet-4-6"
    assert result["fallback_attempts"][0]["provider"] == "anthropic"
    assert result["fallback_attempts"][0]["model"] == "claude-opus-4-8"
    assert result["fallback_attempts"][0]["outcome"] == "error"
    assert result["fallback_attempts"][1]["outcome"] == "success"
    assert result["fallback_excluded_providers_final"] == []
    assert result["fallback_excluded_models_final"] == ["claude-opus-4-8"]


def test_deepseek_v4_pro_fica_fallback_por_rota_externa_sem_hardcode() -> None:
    routes = json.loads(Path("contratos/v4_rotas_llm_limpas_v1.json").read_text(encoding="utf-8"))
    ratings = json.loads(Path("config/llm_ratings.json").read_text(encoding="utf-8"))
    providers = json.loads(Path("config/llm_providers.json").read_text(encoding="utf-8"))
    redacao = routes["contexts"]["v4_super_luxo_redacao"]
    assert [entry["tier"] for entry in redacao] == [
        "openai_luxo",
        "anthropic_luxo",
        "gemini_luxo",
        "deepseek_luxo",
    ]
    assert redacao[-1]["models"] == ["deepseek-v4-pro"]
    assert "redacao" in ratings["modelos"]["deepseek-v4-pro"]["funcoes_permitidas"]
    assert providers["providers"]["deepseek"]["fallback_models"]["luxo"] == ["deepseek-v4-pro"]
    adapter = V4LLMAdapter(root=".")
    recommendation = adapter.model_router.recommend("v4_politica_economia", "redacao", "deepseek-route-test")
    selected_real = adapter._select_candidate(recommendation.candidates, "real")
    assert selected_real.selection.provider == "openai"
    assert selected_real.selection.model == "gpt-5.5"
    operational_code = "\n".join(
        path.read_text(encoding="utf-8")
        for path in Path("codigo").glob("*.py")
        if path.name != "test_contracts.py"
    )
    assert "deepseek-v4-pro" not in operational_code


def test_adapter_obedece_temperature_flag_do_modelo() -> None:
    adapter = V4LLMAdapter(root=".")
    assert adapter._temperature_for_model("deepseek-v4-pro", 0.7) == 0.1
    assert adapter._temperature_for_model("gemini-3.5-flash", 0.7) == 0.7


def test_sanitize_error_cobre_chaves_nao_sk() -> None:
    raw = (
        "falha com sk-proj-abc123DEF_456 "
        "AIzaSyA1234567890abcdefghijklmnopqrstuvwxyz "
        "gsk_abcDEF123456 "
        "pplx-abcDEF123456"
    )
    sanitized = V4RealRedator._sanitize_error(raw)
    assert "sk-proj-" not in sanitized
    assert "AIza" not in sanitized
    assert "gsk_" not in sanitized
    assert "pplx-" not in sanitized
    assert sanitized.count("[REDACTED_API_KEY]") == 4


def test_redator_real_grava_recibo_jsonl_sem_prompt_ou_texto() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        _copy_contract(tmp)
        redator = V4RealRedator.__new__(V4RealRedator)
        redator.root = Path(tmp)
        payload = {
            "item_id": "v4_real_001",
            "curadoria_id": "cur_test",
            "editoria": "v4_politica_economia",
            "status": "redator_real_llm_pronto",
            "external_call_executed": True,
            "wordpress_real": False,
            "selected_route": {"provider": "deepseek", "model": "deepseek-v4-pro"},
            "fallback_attempts": [{"attempt": 1, "outcome": "success"}],
            "prompt_real": "PROMPT NAO DEVE ENTRAR NO RECIBO",
            "texto_real": "TEXTO COMPLETO NAO DEVE ENTRAR NO RECIBO",
            "issues": [],
            "llm_response": {
                "provider": "deepseek",
                "model": "deepseek-v4-pro",
                "selected_tier": "deepseek_luxo",
                "tokens_in": 100,
                "tokens_out": 200,
                "duration_ms_llm": 1234,
                "prompt_hash": "abc",
                "cost_usd_estimated": 0.001,
                "pricing_table_version": "test",
                "model_parameters": {
                    "temperature": 0.1,
                    "max_tokens": 4000,
                    "thinking_budget": 0,
                },
            },
        }
        result = redator._record_telemetry(payload)
        assert result["ok"] is True
        receipt_path = Path(tmp, result["path"])
        receipt = json.loads(receipt_path.read_text(encoding="utf-8").splitlines()[0])
        assert receipt["llm"]["provider"] == "deepseek"
        assert receipt["llm"]["temperature"] == 0.1
        assert receipt["idempotency_key"].endswith(":1:deepseek:deepseek-v4-pro")
        assert receipt["payload"]["model_parameters"]["temperature"] == 0.1
        assert receipt["payload"]["text_chars"] == len(payload["texto_real"])
        serialized = json.dumps(receipt, ensure_ascii=False)
        assert "PROMPT NAO DEVE ENTRAR" not in serialized
        assert "TEXTO COMPLETO NAO DEVE ENTRAR" not in serialized


def test_foruns_v4_nao_contem_fontes_vivas_e_v4_labs_existe() -> None:
    assert not Path("Cerebro/Foruns/v4").exists(), "diretorio Cerebro/Foruns/v4 gera confusao com root/v4"
    for forbidden in ["diretrizes", "codigo", "dados"]:
        assert not Path("Cerebro/Foruns/v4", forbidden).exists(), f"fonte viva duplicada em Foruns/v4: {forbidden}"
    for required in ["contratos", "codigo", "dados"]:
        assert Path(required).exists(), f"fonte viva ausente: {required}"
    lab_path = Path("Projeto Cafezinho Agentes/root/v4_labs")
    running_inside_lab = Path("README_V4_LABS.md").exists()
    assert lab_path.exists() or running_inside_lab, "v4_labs ausente"
    final_path = Path("Projeto Cafezinho Agentes/root/v4")
    assert final_path.exists() or running_inside_lab, "diretorio final v4 ausente"
    flow = json.loads(Path("contratos/v4_fluxo_dry_run_v1.json").read_text(encoding="utf-8"))
    assert flow["steps"][0]["name"] == "curadoria_dry_run"
    assert flow["steps"][1]["from"] == "curadoria"
    agents = json.loads(Path("contratos/v4_agentes_tecnicos_v1.json").read_text(encoding="utf-8"))
    assert "curador" in agents["agents"]
    assert agents["agents"]["produtor"]["default_read_layers"] == ["curadoria"]
    assert agents["agents"]["imagem"]["default_read_layers"] == ["curadoria"]


def test_fluxo_dry_run_executa_curadoria_antes_da_producao() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        _copy_layers_contract(tmp)
        _copy_flow_contract(tmp)
        _copy_curadoria_contract(tmp)
        _copy_quality_agent_contracts(tmp)
        _copy_imagem_destacada_contract(tmp)
        _copy_adapter_contract(tmp)
        _copy_context_map(tmp)
        _copy_llm_routes_contract(tmp)
        _copy_llm_orchestration_contract(tmp)
        _copy_llm_decisions_contract(tmp)
        _copy_pricing_contract(tmp)
        _copy_feedback_contract(tmp)
        _copy_contract(tmp)
        flow = V4DryRunFlow(root=tmp)
        result = flow.run(execute=False)
        steps = [item["step"] for item in result["steps"]]
        assert steps[:2] == ["curadoria_dry_run", "produzir_dry_run"]
        assert result["steps"][0]["source_layer"] == "auditado"
        assert result["steps"][0]["target_layer"] == "curadoria"
        assert result["steps"][1]["source_layer"] == "curadoria"


def test_agentes_revisor_fact_checker_e_auditor_final_existem() -> None:
    agents = json.loads(Path("contratos/v4_agentes_tecnicos_v1.json").read_text(encoding="utf-8"))
    assert "revisor" in agents["agents"]
    assert "fact_checker" in agents["agents"]
    assert "promotor" in agents["agents"]
    assert agents["agents"]["revisor"]["default_read_layers"] == ["curadoria", "producao"]
    assert agents["agents"]["fact_checker"]["default_write_layers"] == ["producao", "quarentena"]
    factory = TechnicalAgentFactory(root=".")
    assert factory.build("revisor").valid is True
    assert factory.build("fact_checker").valid is True
    assert factory.build("promotor").valid is True
    invalid = [spec.as_dict() for spec in factory.validate_all() if not spec.valid]
    assert invalid == []


def test_revisao_bloqueia_meta_linguagem_e_texto_curto() -> None:
    payload = _sample_quality_payload(text="Essa é a promessa editorial que o texto precisa entregar.")
    result = V4ReviewAgent(root=".").review(payload)
    assert result["manifesto_revisao"]["ok"] is False
    assert "revisao_meta_linguagem:promessa editorial" in result["issues"]
    assert any(issue.startswith("revisao_texto_curto") for issue in result["issues"])


def test_fact_check_bloqueia_fato_obrigatorio_sem_fonte() -> None:
    payload = _sample_quality_payload()
    payload["texto_revisado"] = payload["texto_dry_run"]
    payload["fatos_travados"][0]["fonte_ref"] = []
    result = V4FactCheckAgent(root=".").check(payload)
    assert result["manifesto_fact_check"]["ok"] is False
    assert "fact_check_fato_sem_fonte_ref:1" in result["issues"]


def test_fact_check_bloqueia_fato_obrigatorio_ausente_do_texto() -> None:
    payload = _sample_quality_payload(text=("Texto longo sobre politica brasileira sem USTR, Federal Register ou Pix. " * 25))
    payload["texto_revisado"] = payload["texto_dry_run"]
    result = V4FactCheckAgent(root=".").check(payload)
    assert result["manifesto_fact_check"]["ok"] is False
    assert result["manifesto_fact_check"]["check_type"] == "metadata_plus_text_presence_heuristic"
    assert "fact_check_fato_obrigatorio_ausente_no_texto:1" in result["issues"]
    assert "fact_check_fato_obrigatorio_ausente_no_texto:2" in result["issues"]


def test_fact_check_preserva_tokens_numericos_e_bloqueia_percentual_errado() -> None:
    payload = _sample_quality_payload(
        text=(
            "O USTR informou tarifa de 35 por cento na Section 301. "
            "O Federal Register publicou notice em 2026 sobre Pix. "
        )
        * 20
    )
    payload["texto_revisado"] = payload["texto_dry_run"]
    payload["fatos_travados"] = [
        {
            "idx": 1,
            "fato": "O USTR informou tarifa de 25 por cento na Section 301.",
            "fonte_ref": ["https://ustr.gov/"],
            "obrigatorio_no_texto": True,
        },
        {
            "idx": 2,
            "fato": "O Federal Register publicou notice em 2026 sobre Pix.",
            "fonte_ref": ["https://www.federalregister.gov/"],
            "obrigatorio_no_texto": True,
        },
    ]
    result = V4FactCheckAgent(root=".").check(payload)
    assert result["manifesto_fact_check"]["ok"] is False
    assert "fact_check_fato_obrigatorio_ausente_no_texto:1" in result["issues"]
    assert "fact_check_fato_obrigatorio_ausente_no_texto:2" not in result["issues"]


def test_auditoria_final_exige_revisao_e_fact_check_aprovados() -> None:
    payload = _sample_quality_payload()
    reviewed = V4ReviewAgent(root=".").review(payload)
    checked = V4FactCheckAgent(root=".").check(reviewed)
    audited = V4FinalAuditAgent(root=".").audit(checked)
    assert audited["manifesto_auditoria_final"]["ok"] is True
    broken = dict(checked)
    broken["manifesto_fact_check"] = {"ok": False}
    blocked = V4FinalAuditAgent(root=".").audit(broken)
    assert blocked["manifesto_auditoria_final"]["ok"] is False
    assert "auditoria_final_fact_check_nao_aprovado" in blocked["issues"]


def test_fluxo_dry_run_inclui_revisao_fact_check_auditoria() -> None:
    flow = json.loads(Path("contratos/v4_fluxo_dry_run_v1.json").read_text(encoding="utf-8"))
    steps = [step["name"] for step in flow["steps"]]
    assert steps == [
        "curadoria_dry_run",
        "produzir_dry_run",
        "revisar_dry_run",
        "fact_check_dry_run",
        "auditar_final_dry_run",
        "publicar_dry_run",
    ]
    assert flow["steps"][2]["role"] == "revisor"
    assert flow["steps"][3]["role"] == "fact_checker"


def test_fluxo_dry_run_detecta_saida_bloqueada_ou_incompleta() -> None:
    step = {
        "name": "produzir_dry_run",
        "requires": ["curadoria_id", "manifesto_producao", "idempotency_key"],
    }
    output = {
        "item_id": "x",
        "status": "revisao_bloqueada",
        "issues": ["revisao_texto_curto:10<900"],
        "manifesto": {"manifesto_producao": True},
    }
    issues = V4DryRunFlow._output_issues(step, output)
    assert "revisao_texto_curto:10<900" in issues
    assert "status_bloqueado:revisao_bloqueada" in issues
    assert "saida_sem_required:curadoria_id" in issues
    assert "saida_sem_required:idempotency_key" in issues


def test_fluxo_producao_nao_regenera_artefato_bloqueado() -> None:
    flow = json.loads(Path("contratos/v4_fluxo_dry_run_v1.json").read_text(encoding="utf-8"))
    promotion = flow["promocao_para_producao"]
    assert flow["principios"]["regenera_artefato_fixture_invalido"] is True
    assert promotion["regenera_artefato_fixture_invalido_deve_ser_false"] is True
    assert promotion["artefato_bloqueado_evidencia_append_only"] is True
    assert promotion["producao_nao_sobrescreve_bloqueio"] is True


def test_multi_item_lab_congela_curadoria_e_grava_relatorio() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        _prepare_multi_item_lab_fixture(tmp)
        result = V4MultiItemLabRunner(tmp).run(execute=True)
        assert result["issues"] == []
        assert result["aggregate"]["total_items"] == 3
        assert result["aggregate"]["ok_items"] == 3
        assert result["aggregate"]["curadoria_frozen"] is True
        assert len(result["aggregate"]["editorias"]) >= 3
        assert result["aggregate"]["editorial_review_required_items"] == ["v4_real_006", "v4_real_007"]
        assert all(item["ok"] for item in result["items"])
        assert all(state["unchanged"] for state in result["frozen_sources"])
        by_id = {item["item_id"]: item for item in result["items"]}
        assert "tese_cultura_desalinhada_com_objeto" in by_id["v4_real_007"]["warnings"]
        assert "tese_ia_desalinhada_com_objeto" in by_id["v4_real_006"]["warnings"]
        assert Path(tmp, "dados/promocao/v4_labs_fase7_multi_item_lab_20260710.json").exists()


def test_editorial_coherence_gate_flagra_template_industrial_em_cultura() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        _copy_editorial_coherence_contract(tmp)
        gate = V4EditorialCoherenceGate(tmp)
        result = gate.evaluate(
            {
                "editoria": "v4_cultura",
                "tese_escolhida_idx": 0,
                "consequencia_material": {
                    "descricao": "os dados do setor produtivo deslocam a pauta de indicador isolado para debate sobre industria, valor agregado e politica economica"
                },
                "teses_candidatas": [
                    {
                        "idx": 0,
                        "status": "escolhida",
                        "tese": "Quando os fatos auditados sobre audiovisual brasileiro saem do placar declaratorio, revela-se que os dados do setor produtivo deslocam a pauta de indicador isolado para debate sobre industria, valor agregado e politica economica.",
                        "quem_ganha": "leitor",
                        "quem_perde": "leitura que reduz industria a numero mensal",
                    }
                ],
            }
        )
        assert result["status"] == "warning"
        assert result["issues"] == []
        assert result["warnings"] == ["tese_cultura_desalinhada_com_objeto"]
        assert result["human_review_required"] is True


def test_editorial_coherence_gate_aprova_tese_cultural_com_eixo_formal() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        _copy_editorial_coherence_contract(tmp)
        gate = V4EditorialCoherenceGate(tmp)
        result = gate.evaluate(
            {
                "editoria": "v4_cultura",
                "tese_escolhida_idx": 0,
                "consequencia_material": {
                    "descricao": "o debate sobre streaming ganha densidade quando a obra e a dramaturgia organizam a disputa por memoria cultural"
                },
                "teses_candidatas": [
                    {
                        "idx": 0,
                        "status": "escolhida",
                        "tese": "Quando a serie transforma o suspense em rotina domestica, revela-se que a montagem e a dramaturgia fazem da familia o verdadeiro campo de conflito.",
                        "quem_ganha": "leitor",
                        "quem_perde": "resumo industrial generico",
                    }
                ],
            }
        )
        assert result["status"] == "ok"
        assert result["warnings"] == []
        assert result["human_review_required"] is False


def test_editorial_coherence_gate_tese_ausente_vira_warning() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        _copy_editorial_coherence_contract(tmp)
        gate = V4EditorialCoherenceGate(tmp)
        result = gate.evaluate({"editoria": "v4_cultura", "teses_candidatas": []})
        assert result["status"] == "warning"
        assert result["warnings"] == ["tese_ausente"]
        assert result["issues"] == []
        assert result["human_review_required"] is True


def test_multi_item_lab_detecta_curadoria_alterada() -> None:
    class MutatingRunner(V4MultiItemLabRunner):
        def _run_item(self, item: dict[str, object], execute: bool) -> dict[str, object]:
            Path(self.root, "codigo/curadoria_tese.py").write_text("alterado\n", encoding="utf-8")
            return {
                "item_id": item["item_id"],
                "editoria": item["editoria"],
                "ok": True,
                "fixture_path": "",
                "steps": [],
                "warnings": [],
                "issues": [],
            }

    with tempfile.TemporaryDirectory() as tmp:
        Path(tmp, "codigo").mkdir(parents=True)
        Path(tmp, "contratos").mkdir(parents=True)
        Path(tmp, "codigo/curadoria_tese.py").write_text("original\n", encoding="utf-8")
        Path(tmp, "contratos/v4_curadoria_tese_v1.json").write_text("{}", encoding="utf-8")
        _copy_flow_contract(tmp)
        _copy_multi_item_contract(tmp)
        _copy_editorial_coherence_contract(tmp)
        result = MutatingRunner(tmp).run(execute=False)
        assert "frozen_source_changed:codigo/curadoria_tese.py" in result["issues"]


def test_rascunho_primeiro_contrato_diferencia_rascunho_de_promocao() -> None:
    policy = json.loads(Path("contratos/v4_rascunho_primeiro_v1.json").read_text(encoding="utf-8"))
    wordpress = json.loads(Path("contratos/v4_wordpress_publicador_v1.json").read_text(encoding="utf-8"))
    flow = json.loads(Path("contratos/v4_fluxo_dry_run_v1.json").read_text(encoding="utf-8"))
    promotion = json.loads(Path("contratos/v4_promocao_preflight_v1.json").read_text(encoding="utf-8"))
    assert policy["principios"]["rascunho_primeiro"] is True
    assert policy["principios"]["pendencias_de_rascunho_viram_warnings"] is True
    assert policy["escopo_atual"]["wordpress_real_draft_pending_publish"] == "gates_duros_ate_ratificacao_explicita_do_forum"
    assert policy["politicas"]["sem_midia_auditada"]["rascunho"] == "seguir_sem_midia_com_warning"
    assert policy["politicas"]["collection_request_aberto"]["wordpress_real"] == "exigir_resolucao_ou_decisao_editorial_explicita"
    assert "promocao_para_root_v4" in policy["hard_blocks_permitidos"]
    assert wordpress["principios"]["rascunho_pode_seguir_sem_featured_media_com_relatorio"] is True
    assert wordpress["principios"]["wordpress_real_draft_pending_mantem_gates_duros"] is True
    assert "pending" not in wordpress["real_publish"]["draft_statuses"]
    assert flow["principios"]["imagem_pendente_nao_bloqueia_rascunho"] is True
    assert promotion["principios"]["nao_e_gate_de_rascunho_editorial"] is True


def test_ab_261439_grava_pacote_cego_sem_publicacao() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        _copy_curadoria_contract(tmp)
        auditado_path = Path(tmp, "dados/auditado/v4_real_001.json")
        auditado_path.parent.mkdir(parents=True, exist_ok=True)
        auditado_path.write_text(json.dumps(_sample_auditado_payload(), ensure_ascii=False), encoding="utf-8")
        producao_path = Path(tmp, "dados/producao/v4_real_001.producao.json")
        producao_path.parent.mkdir(parents=True, exist_ok=True)
        producao_path.write_text(
            json.dumps(
                {
                    "item_id": "v4_real_001",
                    "editoria": "v4_politica_economia",
                    "titulo": "Tarifa dos EUA vira disputa entre Lula e Flavio antes da eleicao",
                    "texto_dry_run": "Texto A original sem curadoria.",
                },
                ensure_ascii=False,
            ),
            encoding="utf-8",
        )
        result = V4CuradoriaABExperiment(root=tmp).run_261439(execute=True)
        assert result["ok"] is True
        assert result["package"]["external_publish"] is False
        assert result["package"]["real_wordpress_draft"] is False
        assert result["package"]["variants"][0]["curadoria_id"] is None
        assert result["package"]["variants"][1]["curadoria_id"].startswith("cur_")
        assert Path(tmp, result["paths"]["package"]).exists()


def test_imagem_destacada_aprova_candidato_com_direitos_e_entidade() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        contract = _copy_imagem_destacada_contract(tmp)
        evaluator = V4FeaturedImageEvaluator(root=tmp, contract_path=contract)
        result = evaluator.select(
            [_sample_media_candidate()],
            title="Flavio Bolsonaro critica decisao do STF",
            primary_entity="Flavio Bolsonaro",
            requires_person=True,
        )
        assert result["ok"] is True
        assert result["decision"]["selected"]["candidate"]["image_id"] == "img1"


def test_imagem_destacada_rejeita_thumbnail_sem_direitos() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        contract = _copy_imagem_destacada_contract(tmp)
        evaluator = V4FeaturedImageEvaluator(root=tmp, contract_path=contract)
        bad = _sample_media_candidate(
            image_id="bad",
            url="https://example.com/thumb/flavio_150x150.jpg",
            credit="",
            license="",
            rights_status="desconhecido",
            width=150,
            height=150,
            score=20,
        )
        result = evaluator.select([bad], "Flavio Bolsonaro critica decisao", "Flavio Bolsonaro", requires_person=True)
        assert result["ok"] is False
        issues = result["decision"]["evaluations"][0]["issues"]
        assert "credito_ausente" in issues
        assert "licenca_ausente" in issues


def test_imagem_destacada_grava_decisao_append_only() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        contract = _copy_imagem_destacada_contract(tmp)
        evaluator = V4FeaturedImageEvaluator(root=tmp, contract_path=contract)
        result = evaluator.select(
            [_sample_media_candidate()],
            title="Flavio Bolsonaro critica decisao do STF",
            primary_entity="Flavio Bolsonaro",
            requires_person=True,
            execute=True,
        )
        assert result["ok"] is True
        files = list(Path(tmp, "agent_data/v4/media/decisions").glob("*.jsonl"))
        assert files
        assert len(files[0].read_text(encoding="utf-8").splitlines()) == 1


def test_media_source_ouro_sqlite_normaliza_candidato() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        contract = _copy_imagem_destacada_contract(tmp)
        db_path = Path(tmp, "ouro.db")
        _create_ouro_fixture_db(db_path)
        old_env = os.environ.get("BANCO_MIDIA_OURO_DB")
        os.environ["BANCO_MIDIA_OURO_DB"] = str(db_path)
        try:
            collector = V4MediaSourceCollector(root=tmp, contract_path=contract)
            result = collector.collect_ouro_sqlite("Flavio Bolsonaro critica decisao", primary_entity="Flavio Bolsonaro")
        finally:
            if old_env is None:
                os.environ.pop("BANCO_MIDIA_OURO_DB", None)
            else:
                os.environ["BANCO_MIDIA_OURO_DB"] = old_env
        assert result["ok"] is True
        assert result["candidates"][0]["entity"] == "Flavio Bolsonaro"
        assert result["candidates"][0]["rights_status"] == "fonte_oficial"


def test_media_source_ouro_sqlite_indisponivel_nao_quebra() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        contract = _copy_imagem_destacada_contract(tmp)
        old_env = os.environ.get("BANCO_MIDIA_OURO_DB")
        os.environ["BANCO_MIDIA_OURO_DB"] = str(Path(tmp, "missing.db"))
        try:
            collector = V4MediaSourceCollector(root=tmp, contract_path=contract)
            result = collector.collect_ouro_sqlite("Teste")
        finally:
            if old_env is None:
                os.environ.pop("BANCO_MIDIA_OURO_DB", None)
            else:
                os.environ["BANCO_MIDIA_OURO_DB"] = old_env
        assert result["ok"] is False
        assert result["reason"] == "db_unavailable"


def test_media_source_path_exists_trata_oserror() -> None:
    assert V4MediaSourceCollector._path_exists("\x00") is False


def test_media_audit_promove_aprovada_e_busca_por_entidade() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        contract = _copy_imagem_destacada_contract(tmp)
        evaluator = V4FeaturedImageEvaluator(root=tmp, contract_path=contract)
        evaluation = evaluator.evaluate(
            _sample_media_candidate(),
            title="Flavio Bolsonaro critica decisao",
            primary_entity="Flavio Bolsonaro",
            requires_person=True,
        )
        store = V4AuditedMediaStore(root=tmp, contract_path=contract)
        result = store.promote(evaluation, execute=True)
        assert result["ok"] is True
        records = store.search("Flavio Bolsonaro")
        assert len(records) == 1
        assert records[0]["image_id"] == "img1"


def test_media_audit_bloqueia_avaliacao_reprovada() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        contract = _copy_imagem_destacada_contract(tmp)
        evaluator = V4FeaturedImageEvaluator(root=tmp, contract_path=contract)
        evaluation = evaluator.evaluate(
            _sample_media_candidate(rights_status="desconhecido"),
            title="Flavio Bolsonaro critica decisao",
            primary_entity="Flavio Bolsonaro",
            requires_person=True,
        )
        result = V4AuditedMediaStore(root=tmp, contract_path=contract).promote(evaluation, execute=True)
        assert result["ok"] is False
        assert result["mode"] == "blocked"


def test_fluxo_publicacao_sem_midia_auditada_segue_com_warning() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        contract = _copy_imagem_destacada_contract(tmp)
        flow = V4DryRunFlow.__new__(V4DryRunFlow)
        flow.media_store = V4AuditedMediaStore(root=tmp, contract_path=contract)
        output = {"primary_entity": "Flavio Bolsonaro", "manifesto": {}, "publicacao_dry_run": {}}
        issues = flow._attach_required_media({"name": "publicar_dry_run"}, output)
        assert not issues
        assert output["manifesto"]["imagem_destacada_validada"] is False
        assert output["publicacao_dry_run"]["featured_media_id"] is None
        assert any("imagem_destacada_pendente" in warning for warning in output["warnings"])


def test_fluxo_publicacao_anexa_midia_auditada() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        contract = _copy_imagem_destacada_contract(tmp)
        evaluator = V4FeaturedImageEvaluator(root=tmp, contract_path=contract)
        evaluation = evaluator.evaluate(
            _sample_media_candidate(),
            title="Flavio Bolsonaro critica decisao",
            primary_entity="Flavio Bolsonaro",
            requires_person=True,
        )
        store = V4AuditedMediaStore(root=tmp, contract_path=contract)
        store.promote(evaluation, execute=True)
        flow = V4DryRunFlow.__new__(V4DryRunFlow)
        flow.media_store = store
        output = {"primary_entity": "Flavio Bolsonaro", "manifesto": {}, "publicacao_dry_run": {}}
        issues = flow._attach_required_media({"name": "publicar_dry_run"}, output)
        assert not issues
        assert output["manifesto"]["imagem_destacada_validada"] is True
        assert output["featured_media"]["image_id"] == "img1"


def test_wordpress_publicador_dry_run_grava_tentativa() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        _copy_wordpress_media_contract(tmp)
        contract = _copy_wordpress_contract(tmp)
        publisher = V4WordPressPublisher(root=tmp, contract_path=contract)
        result = publisher.publish_payload(_sample_publication_payload(), execute=True)
        assert result["ok"] is True
        files = list(Path(tmp, "agent_data/v4/publication").glob("*.jsonl"))
        assert files
        assert json.loads(files[0].read_text(encoding="utf-8").splitlines()[0])["outcome"] == "dry_run"


def test_wordpress_publicador_real_bloqueado_por_contrato() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        _copy_wordpress_media_contract(tmp)
        contract = _copy_wordpress_contract(tmp)
        publisher = V4WordPressPublisher(root=tmp, contract_path=contract)
        payload = _sample_publication_payload()
        payload["featured_media"]["wp_media_id"] = 123
        result = publisher.publish_payload(payload, real=True, execute=True)
        assert result["ok"] is False
        assert "publicacao_real_desabilitada_no_contrato" in result["attempt"]["issues"]


def test_wordpress_publicador_rascunho_sem_featured_media_vira_warning() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        _copy_wordpress_media_contract(tmp)
        contract = _copy_wordpress_contract(tmp)
        publisher = V4WordPressPublisher(root=tmp, contract_path=contract)
        payload = _sample_publication_payload()
        del payload["featured_media"]
        result = publisher.publish_payload(payload)
        assert result["ok"] is True
        assert result["attempt"]["outcome"] == "dry_run_with_warnings"
        assert "campo_publicacao_ausente:featured_media" in result["attempt"]["warnings"]
        assert not result["attempt"]["issues"]


def test_wordpress_publicador_rascunho_sem_curadoria_id_vira_warning() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        _copy_wordpress_media_contract(tmp)
        contract = _copy_wordpress_contract(tmp)
        publisher = V4WordPressPublisher(root=tmp, contract_path=contract)
        payload = _sample_publication_payload()
        del payload["curadoria_id"]
        result = publisher.publish_payload(payload)
        assert result["ok"] is True
        assert result["attempt"]["outcome"] == "dry_run_with_warnings"
        assert "campo_publicacao_ausente:curadoria_id" in result["attempt"]["warnings"]
        assert not result["attempt"]["issues"]


def test_wordpress_publicador_real_bloqueia_ascii_sem_acentos() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        _copy_wordpress_media_contract(tmp)
        contract = _copy_wordpress_contract(tmp)
        publisher = V4WordPressPublisher(root=tmp, contract_path=contract)
        payload = _sample_publication_payload()
        payload["texto_dry_run"] = "Texto de politica sem acentos " * 20
        payload["featured_media"]["credit"] = "Agencia Senado"
        payload["featured_media"]["license"] = "Fonte oficial"
        result = publisher.publish_payload(payload, status="publish", real=True)
        assert "encoding_portugues_ascii_sem_acentos" in result["attempt"]["issues"]


def test_wordpress_publicador_real_bloqueia_collection_request_ausente() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        _copy_wordpress_media_contract(tmp)
        contract = _copy_wordpress_contract(tmp)
        publisher = V4WordPressPublisher(root=tmp, contract_path=contract)
        payload = _sample_publication_payload()
        payload["featured_media"]["wp_media_id"] = 123
        result = publisher.publish_payload(payload, status="publish", real=True)
        assert "collection_request_ausente_para_publicacao_real" in result["attempt"]["issues"]


def test_wordpress_publicador_real_bloqueia_collection_request_publicacao_real() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        _copy_wordpress_media_contract(tmp)
        contract = _copy_wordpress_contract(tmp)
        publisher = V4WordPressPublisher(root=tmp, contract_path=contract)
        payload = _sample_publication_payload()
        payload["featured_media"]["wp_media_id"] = 123
        payload["collection_request"] = {
            "status": "recommended",
            "required_before": "publicacao_real",
            "reason": "confirmar docket antes de publicacao final",
        }
        result = publisher.publish_payload(payload, status="publish", real=True)
        assert "collection_request_bloqueia_publicacao_real:publicacao_real" in result["attempt"]["issues"]


def test_wordpress_publicador_real_draft_bloqueia_campos_criticos() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        _copy_wordpress_media_contract(tmp)
        contract = _copy_wordpress_contract(tmp)
        _enable_wordpress_real_for_test(tmp, contract)
        publisher = V4WordPressPublisher(root=tmp, contract_path=contract)
        called: list[bool] = []
        publisher._post_wordpress = lambda wp_payload: called.append(True) or {"ok": True}  # type: ignore[method-assign]
        payload = _sample_publication_payload()
        payload["collection_request"] = {"status": "resolved", "required_before": "none"}
        del payload["curadoria_id"]
        del payload["featured_media"]
        del payload["manifesto"]
        with _temporary_wordpress_env():
            result = publisher.publish_payload(payload, status="draft", real=True)
        assert result["ok"] is False
        assert called == []
        assert "campo_publicacao_ausente:curadoria_id" in result["attempt"]["issues"]
        assert "campo_publicacao_ausente:featured_media" in result["attempt"]["issues"]
        assert "campo_publicacao_ausente:manifesto" in result["attempt"]["issues"]
        assert "featured_media_wp_id_ausente" in result["attempt"]["issues"]


def test_wordpress_publicador_real_draft_bloqueia_collection_request_publicacao_real() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        _copy_wordpress_media_contract(tmp)
        contract = _copy_wordpress_contract(tmp)
        _enable_wordpress_real_for_test(tmp, contract)
        publisher = V4WordPressPublisher(root=tmp, contract_path=contract)
        called: list[bool] = []
        publisher._post_wordpress = lambda wp_payload: called.append(True) or {"ok": True}  # type: ignore[method-assign]
        payload = _sample_publication_payload()
        payload["featured_media"]["wp_media_id"] = 123
        payload["collection_request"] = {
            "status": "required",
            "required_before": "publicacao_real",
            "reason": "confirmar docket antes de chamada real ao WordPress",
        }
        with _temporary_wordpress_env():
            result = publisher.publish_payload(payload, status="draft", real=True)
        assert result["ok"] is False
        assert called == []
        assert "collection_request_bloqueia_publicacao_real:publicacao_real" in result["attempt"]["issues"]


def test_wordpress_publicador_collection_request_fail_closed_valores_desconhecidos() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        _copy_wordpress_media_contract(tmp)
        contract = _copy_wordpress_contract(tmp)
        _enable_wordpress_real_for_test(tmp, contract)
        publisher = V4WordPressPublisher(root=tmp, contract_path=contract)
        called: list[bool] = []
        publisher._post_wordpress = lambda wp_payload: called.append(True) or {"ok": True}  # type: ignore[method-assign]
        payload = _sample_publication_payload()
        payload["featured_media"]["wp_media_id"] = 123
        payload["collection_request"] = {
            "status": "em_analise",
            "required_before": "publicacao_real",
            "reason": "valor desconhecido deve falhar fechado",
        }
        with _temporary_wordpress_env():
            result = publisher.publish_payload(payload, status="draft", real=True)
        assert result["ok"] is False
        assert called == []
        assert "collection_request_status_desconhecido:em_analise" in result["attempt"]["issues"]

        payload["collection_request"] = {
            "status": "required",
            "required_before": "publicacao_final",
            "reason": "estagio desconhecido deve falhar fechado",
        }
        with _temporary_wordpress_env():
            result = publisher.publish_payload(payload, status="draft", real=True)
        assert result["ok"] is False
        assert called == []
        assert "collection_request_required_before_desconhecido:publicacao_final" in result["attempt"]["issues"]


def test_wordpress_publicador_collection_request_nao_string_vira_issue() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        _copy_wordpress_media_contract(tmp)
        contract = _copy_wordpress_contract(tmp)
        _enable_wordpress_real_for_test(tmp, contract)
        publisher = V4WordPressPublisher(root=tmp, contract_path=contract)
        called: list[bool] = []
        publisher._post_wordpress = lambda wp_payload: called.append(True) or {"ok": True}  # type: ignore[method-assign]
        payload = _sample_publication_payload()
        payload["featured_media"]["wp_media_id"] = 123
        payload["collection_request"] = {
            "status": "required",
            "required_before": ["publicacao_real"],
            "reason": "tipo invalido deve virar issue, nao crash",
        }
        with _temporary_wordpress_env():
            result = publisher.publish_payload(payload, status="draft", real=True)
        assert result["ok"] is False
        assert called == []
        assert "collection_request_invalido_para_publicacao_real" in result["attempt"]["issues"]

        payload["collection_request"] = {
            "status": ["required"],
            "required_before": "publicacao_real",
            "reason": "tipo invalido deve virar issue, nao crash",
        }
        with _temporary_wordpress_env():
            result = publisher.publish_payload(payload, status="draft", real=True)
        assert result["ok"] is False
        assert called == []
        assert "collection_request_invalido_para_publicacao_real" in result["attempt"]["issues"]


def test_wordpress_media_mapping_append_lookup() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        contract = _copy_wordpress_media_contract(tmp)
        mapper = V4WordPressMediaMapper(root=tmp, contract_path=contract)
        result = mapper.add_mapping(_sample_wp_mapping(), execute=True)
        assert result["ok"] is True
        found = mapper.lookup("img1")
        assert found is not None
        assert found["wp_media_id"] == 260961


def test_wordpress_publicador_usa_mapping_wp_media_id() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        _copy_wordpress_media_contract(tmp)
        contract = _copy_wordpress_contract(tmp)
        mapper = V4WordPressMediaMapper(root=tmp)
        mapper.add_mapping(_sample_wp_mapping(), execute=True)
        publisher = V4WordPressPublisher(root=tmp, contract_path=contract)
        result = publisher.publish_payload(_sample_publication_payload())
        assert result["ok"] is True
        assert result["attempt"]["payload"]["featured_media"] == 260961


def test_promocao_preflight_bloqueia_pendencias_de_promocao() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        contract = _prepare_promotion_fixture(tmp, ratified=False, collection_status="recommended")
        result = V4PromotionPreflight(root=tmp, contract_path=contract).run()
        assert result["ok"] is False
        assert "recommended_required_policy_ratified" in result["issues"]
        assert "collection_request_publicacao_real_resolvida" in result["issues"]
        assert result["wordpress_real"] is False
        assert result["promocao_real_executada"] is False


def test_promocao_preflight_aprova_fixture_limpa_ratificada() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        contract = _prepare_promotion_fixture(tmp, ratified=True, collection_status="resolved", gpt55=True)
        result = V4PromotionPreflight(root=tmp, contract_path=contract).run(execute=True)
        assert result["ok"] is True
        assert result["issues"] == []
        assert Path(tmp, "dados/promocao/v4_labs.promocao_preflight.json").exists()


def test_promocao_preflight_detecta_sk_generico() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        contract = _prepare_promotion_fixture(tmp, ratified=True, collection_status="resolved", gpt55=True)
        secret_path = Path(tmp, "dados/leak.json")
        secret_path.parent.mkdir(parents=True, exist_ok=True)
        secret_path.write_text('{"token":"sk-a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6"}', encoding="utf-8")
        result = V4PromotionPreflight(root=tmp, contract_path=contract).run()
        assert result["ok"] is False
        assert "no_secret_patterns" in result["issues"]


def test_promocao_preflight_exige_evidencia_para_decisao_true() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        contract = _prepare_promotion_fixture(tmp, ratified=True, collection_status="resolved", gpt55=True)
        contract_path = Path(tmp, contract)
        payload = json.loads(contract_path.read_text(encoding="utf-8"))
        del payload["decision_evidence"]["recommended_required_policy_ratified"]
        contract_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")
        result = V4PromotionPreflight(root=tmp, contract_path=contract).run()
        assert result["ok"] is False
        assert "decision_evidence:recommended_required_policy_ratified" in result["issues"]


def test_promocao_preflight_collection_request_fail_closed_valores_desconhecidos() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        contract = _prepare_promotion_fixture(tmp, ratified=True, collection_status="resolved", gpt55=True)
        curadoria_path = Path(tmp, "dados/curadoria/item.curadoria.json")
        payload = json.loads(curadoria_path.read_text(encoding="utf-8"))
        payload["collection_request"] = {"status": "em_analise", "required_before": "publicacao_real"}
        curadoria_path.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")
        result = V4PromotionPreflight(root=tmp, contract_path=contract).run()
        assert result["ok"] is False
        assert "collection_request_valores_conhecidos" in result["issues"]

        payload["collection_request"] = {"status": "required", "required_before": "publicacao_final"}
        curadoria_path.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")
        result = V4PromotionPreflight(root=tmp, contract_path=contract).run()
        assert result["ok"] is False
        assert "collection_request_valores_conhecidos" in result["issues"]


def test_promocao_preflight_collection_request_nao_string_vira_issue() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        contract = _prepare_promotion_fixture(tmp, ratified=True, collection_status="resolved", gpt55=True)
        curadoria_path = Path(tmp, "dados/curadoria/item.curadoria.json")
        payload = json.loads(curadoria_path.read_text(encoding="utf-8"))
        payload["collection_request"] = {"status": "required", "required_before": ["publicacao_real"]}
        curadoria_path.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")
        result = V4PromotionPreflight(root=tmp, contract_path=contract).run()
        assert result["ok"] is False
        assert "collection_request_valores_conhecidos" in result["issues"]

        payload["collection_request"] = {"status": ["required"], "required_before": "publicacao_real"}
        curadoria_path.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")
        result = V4PromotionPreflight(root=tmp, contract_path=contract).run()
        assert result["ok"] is False
        assert "collection_request_valores_conhecidos" in result["issues"]


def test_operational_dashboard_grava_json_markdown() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        contract = _copy_operational_dashboard_contract(tmp)
        Path(tmp, "dados/auditado").mkdir(parents=True)
        Path(tmp, "dados/auditado/item.json").write_text("{}", encoding="utf-8")
        dashboard = V4OperationalDashboard(root=tmp, contract_path=contract)
        result = dashboard.build(execute=True)
        assert result["ok"] is True
        assert Path(tmp, result["json_path"]).exists()
        assert Path(tmp, result["markdown_path"]).exists()
        assert result["report"]["layers"]["auditado"] == 1


def test_content_ingestion_cria_bruto_intermediario_auditado() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        _copy_layers_contract(tmp)
        contract = _copy_ingestion_contract(tmp)
        ingestion = V4ContentIngestion(root=tmp, contract_path=contract)
        result = ingestion.run_fixture(execute=True)
        assert result["ok"] is True
        assert Path(tmp, "dados/bruto/v4_ingest_001.bruto.json").exists()
        assert Path(tmp, "dados/intermediario/v4_ingest_001.intermediario.json").exists()
        audited = Path(tmp, "dados/auditado/v4_ingest_001.json")
        assert audited.exists()
        data = json.loads(audited.read_text(encoding="utf-8"))
        assert data["manifesto_auditoria"]["fonte_validada"] is True


def test_content_ingestion_coletor_nao_escreve_auditado() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        _copy_layers_contract(tmp)
        contract = _copy_ingestion_contract(tmp)
        ingestion = V4ContentIngestion(root=tmp, contract_path=contract)
        issues = ingestion._check_write("coletor", "auditado")
        assert issues


def _sample_receipt(
    item_id: str = "item",
    vertical: str = "v4_test",
    timestamp: str = "2026-07-08T00:00:00+00:00",
) -> TelemetryReceipt:
    return TelemetryReceipt(
        event_type="test",
        item_id=item_id,
        vertical=vertical,
        agent="test",
        operation="test",
        status="ok",
        idempotency_key=item_id,
        llm=LLMCallDetail(
            provider="mock",
            model="v4-mock-local",
            tier="mock",
            tokens_in=1,
            tokens_out=1,
            duration_ms_llm=1,
            prompt_hash="abc",
        ),
        duration_ms=1,
        cost_usd_estimated=0.0,
        pricing_table_version="pending",
        timestamp=timestamp,
    )


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _copy_contract(tmp: str) -> str:
    source = Path("contratos/v4_telemetria_v1.json")
    target = Path(tmp, "contratos/v4_telemetria_v1.json")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
    return "contratos/v4_telemetria_v1.json"


def _copy_layers_contract(tmp: str) -> str:
    source = Path("contratos/v4_bancos_camadas_v1.json")
    target = Path(tmp, "contratos/v4_bancos_camadas_v1.json")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
    return "contratos/v4_bancos_camadas_v1.json"


def _copy_flow_contract(tmp: str) -> str:
    source = Path("contratos/v4_fluxo_dry_run_v1.json")
    target = Path(tmp, "contratos/v4_fluxo_dry_run_v1.json")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
    return "contratos/v4_fluxo_dry_run_v1.json"


def _copy_multi_item_contract(tmp: str) -> str:
    source = Path("contratos/v4_multi_item_lab_v1.json")
    target = Path(tmp, "contratos/v4_multi_item_lab_v1.json")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
    return "contratos/v4_multi_item_lab_v1.json"


def _copy_editorial_coherence_contract(tmp: str) -> str:
    source = Path("contratos/v4_editoria_coerencia_v1.json")
    target = Path(tmp, "contratos/v4_editoria_coerencia_v1.json")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
    return "contratos/v4_editoria_coerencia_v1.json"


def _copy_curadoria_contract(tmp: str) -> str:
    source = Path("contratos/v4_curadoria_tese_v1.json")
    target = Path(tmp, "contratos/v4_curadoria_tese_v1.json")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
    return "contratos/v4_curadoria_tese_v1.json"


def _copy_redator_shadow_contract(tmp: str) -> str:
    source = Path("contratos/v4_redator_shadow_v1.json")
    target = Path(tmp, "contratos/v4_redator_shadow_v1.json")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
    return "contratos/v4_redator_shadow_v1.json"


def _copy_rascunho_primeiro_contract(tmp: str) -> str:
    source = Path("contratos/v4_rascunho_primeiro_v1.json")
    target = Path(tmp, "contratos/v4_rascunho_primeiro_v1.json")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
    return "contratos/v4_rascunho_primeiro_v1.json"


def _copy_promotion_preflight_contract(tmp: str) -> str:
    source = Path("contratos/v4_promocao_preflight_v1.json")
    target = Path(tmp, "contratos/v4_promocao_preflight_v1.json")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
    return "contratos/v4_promocao_preflight_v1.json"


def _prepare_promotion_fixture(
    tmp: str,
    ratified: bool,
    collection_status: str,
    gpt55: bool = False,
) -> str:
    contract = _copy_promotion_preflight_contract(tmp)
    for copier in [
        _copy_flow_contract,
        _copy_curadoria_contract,
        _copy_redator_shadow_contract,
        _copy_wordpress_contract,
        _copy_rascunho_primeiro_contract,
    ]:
        copier(tmp)
    _copy_quality_agent_contracts(tmp)

    for rel_path in [
        "README_V4_LABS.md",
        "AUDITOR_NOTE_FASE4_AGENTS_PIPELINE_20260709.md",
        "codigo/test_contracts.py",
    ]:
        source = Path(rel_path)
        target = Path(tmp, rel_path)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")

    contract_path = Path(tmp, contract)
    payload = json.loads(contract_path.read_text(encoding="utf-8"))
    payload["decisions"]["recommended_required_policy_ratified"] = ratified
    payload["decisions"]["gpt55_auditfix2_approved"] = gpt55
    evidence = payload.setdefault("decision_evidence", {})
    if ratified:
        evidence["recommended_required_policy_ratified"] = {
            "by": "Miguel",
            "at": "2026-07-09",
            "forum_doc": "Cerebro/Foruns/forum_v4_fase5_ratificacao_promocao_preflight_20260709.md",
        }
    if gpt55:
        evidence["gpt55_auditfix2_approved"] = {
            "by": "GPT 5.5 Pro",
            "at": "2026-07-09",
            "audit_doc": "Cerebro/Foruns/carta_gpt55_auditoria_fase5_20260709.md",
        }
    contract_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")

    collection = {"status": collection_status, "required_before": "publicacao_real"}
    if collection_status == "resolved":
        collection["required_before"] = "none"
    curadoria_path = Path(tmp, "dados/curadoria/item.curadoria.json")
    curadoria_path.parent.mkdir(parents=True, exist_ok=True)
    curadoria_path.write_text(json.dumps({"item_id": "item", "collection_request": collection}), encoding="utf-8")
    return contract


def _copy_quality_agent_contracts(tmp: str) -> None:
    for rel_path in [
        "contratos/v4_revisao_v1.json",
        "contratos/v4_fact_check_v1.json",
        "contratos/v4_auditoria_final_v1.json",
    ]:
        source = Path(rel_path)
        target = Path(tmp, rel_path)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")


def _copy_ingestion_contract(tmp: str) -> str:
    source = Path("contratos/v4_ingestao_conteudo_v1.json")
    target = Path(tmp, "contratos/v4_ingestao_conteudo_v1.json")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
    return "contratos/v4_ingestao_conteudo_v1.json"


def _copy_feedback_contract(tmp: str) -> str:
    source = Path("contratos/v4_feedback_editor_v1.json")
    target = Path(tmp, "contratos/v4_feedback_editor_v1.json")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
    memory_source = Path("contratos/v4_memoria_autocura_v1.json")
    memory_target = Path(tmp, "contratos/v4_memoria_autocura_v1.json")
    memory_target.write_text(memory_source.read_text(encoding="utf-8"), encoding="utf-8")
    return "contratos/v4_feedback_editor_v1.json"


def _copy_pricing_contract(tmp: str) -> str:
    source = Path("contratos/v4_pricing_llm_v1.json")
    target = Path(tmp, "contratos/v4_pricing_llm_v1.json")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
    return "contratos/v4_pricing_llm_v1.json"


def _copy_recompute_contract(tmp: str) -> str:
    source = Path("contratos/v4_recompute_costs_v1.json")
    target = Path(tmp, "contratos/v4_recompute_costs_v1.json")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
    return "contratos/v4_recompute_costs_v1.json"


def _old_pending_receipt() -> dict[str, object]:
    return {
        "schema_version": "v1",
        "timestamp": "2026-07-08T00:00:00+00:00",
        "event_type": "llm_call",
        "item_id": "item_old",
        "vertical": "v4_test",
        "agent": "v4_produtor",
        "operation": "produzir_dry_run",
        "status": "ok",
        "idempotency_key": "item_old:produzir",
        "duration_ms": 100,
        "cost_usd_estimated": 0.0,
        "pricing_table_version": "pending",
        "llm": {
            "provider": "openai",
            "model": "gpt-5.5",
            "tier": "super_luxo",
            "tokens_in": 0,
            "tokens_out": 0,
            "duration_ms_llm": 100,
            "prompt_hash": "abc",
        },
    }


def _copy_llm_decisions_contract(tmp: str) -> str:
    source = Path("contratos/v4_llm_decisions_v1.json")
    target = Path(tmp, "contratos/v4_llm_decisions_v1.json")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
    return "contratos/v4_llm_decisions_v1.json"


def _copy_adapter_contract(tmp: str) -> str:
    source = Path("contratos/v4_llm_adapter_v1.json")
    target = Path(tmp, "contratos/v4_llm_adapter_v1.json")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
    return "contratos/v4_llm_adapter_v1.json"


def _copy_context_map(tmp: str) -> str:
    source = Path("contratos/mapa_v4_contexto_llm.json")
    target = Path(tmp, "contratos/mapa_v4_contexto_llm.json")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
    for doc in [
        "v4_nucleo_editorial_comum_v1.md",
        "v4_politica_economia_v1.md",
        "v4_cultura_v1.md",
        "v4_internacional_v1.md",
        "v4_ciencia_tecnologia_ia_v1.md",
        "v4_repetidor_v1.md",
        "v4_gsn_espelho_ingles_v1.md",
        "v4_freios_llm_v1.json",
        "v4_rotas_llm_limpas_v1.json",
        "v4_orquestracao_llm_v1.json",
        "v4_model_router_v1.json",
    ]:
        source_doc = Path("contratos", doc)
        target_doc = Path(tmp, "contratos", doc)
        target_doc.write_text(source_doc.read_text(encoding="utf-8"), encoding="utf-8")
    return "contratos/mapa_v4_contexto_llm.json"


def _copy_llm_routes_contract(tmp: str) -> str:
    source = Path("contratos/v4_rotas_llm_limpas_v1.json")
    target = Path(tmp, "contratos/v4_rotas_llm_limpas_v1.json")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
    return "contratos/v4_rotas_llm_limpas_v1.json"


def _copy_llm_orchestration_contract(tmp: str) -> str:
    source = Path("contratos/v4_orquestracao_llm_v1.json")
    target = Path(tmp, "contratos/v4_orquestracao_llm_v1.json")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
    return "contratos/v4_orquestracao_llm_v1.json"


def _prepare_multi_item_lab_fixture(tmp: str) -> None:
    for copier in [
        _copy_layers_contract,
        _copy_flow_contract,
        _copy_multi_item_contract,
        _copy_editorial_coherence_contract,
        _copy_curadoria_contract,
        _copy_quality_agent_contracts,
        _copy_imagem_destacada_contract,
        _copy_adapter_contract,
        _copy_context_map,
        _copy_llm_routes_contract,
        _copy_llm_orchestration_contract,
        _copy_llm_decisions_contract,
        _copy_llm_runtime_config,
        _copy_pricing_contract,
        _copy_feedback_contract,
        _copy_contract,
    ]:
        copier(tmp)
    source = Path("codigo/curadoria_tese.py")
    target = Path(tmp, "codigo/curadoria_tese.py")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")


def _copy_llm_runtime_config(tmp: str) -> str:
    for rel_path in [
        "config/llm_providers.json",
        "config/llm_ratings.json",
    ]:
        source = Path(rel_path)
        target = Path(tmp, rel_path)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
    return "config/llm_providers.json"


def _copy_dashboard_contract(tmp: str) -> str:
    source = Path("contratos/v4_llm_dashboard_v1.json")
    target = Path(tmp, "contratos/v4_llm_dashboard_v1.json")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
    _copy_feedback_contract(tmp)
    return "contratos/v4_llm_dashboard_v1.json"


def _copy_imagem_destacada_contract(tmp: str) -> str:
    source = Path("contratos/v4_imagem_destacada_v1.json")
    target = Path(tmp, "contratos/v4_imagem_destacada_v1.json")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
    return "contratos/v4_imagem_destacada_v1.json"


def _copy_wordpress_contract(tmp: str) -> str:
    source = Path("contratos/v4_wordpress_publicador_v1.json")
    target = Path(tmp, "contratos/v4_wordpress_publicador_v1.json")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
    return "contratos/v4_wordpress_publicador_v1.json"


def _enable_wordpress_real_for_test(tmp: str, contract: str) -> None:
    path = Path(tmp, contract)
    payload = json.loads(path.read_text(encoding="utf-8"))
    payload["real_publish"]["enabled"] = True
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")


@contextmanager
def _temporary_wordpress_env():
    keys = {
        "V4_WORDPRESS_URL": "https://example.invalid",
        "V4_WORDPRESS_USER": "tester",
        "V4_WORDPRESS_APP_PASSWORD": "app-password",
    }
    old = {key: os.environ.get(key) for key in keys}
    os.environ.update(keys)
    try:
        yield
    finally:
        for key, value in old.items():
            if value is None:
                os.environ.pop(key, None)
            else:
                os.environ[key] = value


def _copy_wordpress_media_contract(tmp: str) -> str:
    source = Path("contratos/v4_wordpress_media_v1.json")
    target = Path(tmp, "contratos/v4_wordpress_media_v1.json")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
    return "contratos/v4_wordpress_media_v1.json"


def _copy_operational_dashboard_contract(tmp: str) -> str:
    source = Path("contratos/v4_operational_dashboard_v1.json")
    target = Path(tmp, "contratos/v4_operational_dashboard_v1.json")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
    return "contratos/v4_operational_dashboard_v1.json"


def _sample_media_candidate(**overrides: object) -> MediaCandidate:
    payload: dict[str, object] = {
        "image_id": "img1",
        "source": "ouro_sqlite",
        "url": "https://cdn.example.com/flavio-bolsonaro-retrato.jpg",
        "title": "Foto de Flavio Bolsonaro em retrato oficial",
        "credit": "Agencia Senado",
        "license": "Fonte oficial - uso editorial com credito",
        "rights_status": "fonte_oficial",
        "width": 1200,
        "height": 800,
        "entity": "Flavio Bolsonaro",
        "score": 90.0,
        "content_type": "image/jpeg",
        "caption": "Senador Flavio Bolsonaro em foto oficial",
        "metadata": {"tipo": "retrato"},
    }
    payload.update(overrides)
    return MediaCandidate(**payload)  # type: ignore[arg-type]


def _sample_publication_payload() -> dict[str, object]:
    featured = _sample_media_candidate().as_dict()
    featured.update(
        {
            "safe_to_publish": True,
            "final_score": 90.7,
            "visual_confidence": 0.92,
            "reason_class": "person_central",
        }
    )
    return {
        "item_id": "pub1",
        "curadoria_id": "cur_pub1",
        "editoria": "v4_politica_economia",
        "titulo": "Titulo de teste",
        "texto_dry_run": "Texto de teste",
        "primary_entity": "Flavio Bolsonaro",
        "manifesto": {"imagem_destacada_validada": True},
        "featured_media": featured,
    }


def _sample_quality_payload(text: str | None = None) -> dict[str, object]:
    body = text or (
        "Flavio Bolsonaro testemunhou no USTR em 7 de julho de 2026 e pediu que Washington nao imponha tarifas "
        "ao Brasil nem medidas contra o Pix. "
        "A fala desloca a pauta de uma disputa verbal para uma consequencia concreta sobre empresas, consumidores, "
        "soberania financeira e custo eleitoral para a direita brasileira. "
        "O Federal Register registrou a investigacao Section 301 e a transcricao oficial do Dia 2 listou o senador "
        "no Painel 8. "
        "O texto preserva a atribuicao das fontes e trata a publicacao real como pendente ate confirmacao adicional "
        "do comentario escrito no docket USTR-2026-0331. "
    ) * 4
    return {
        "item_id": "v4_quality_001",
        "curadoria_id": "cur_quality_001",
        "editoria": "v4_politica_economia",
        "promessa_ao_leitor": "Explicar por que tarifa e Pix viraram problema eleitoral para a direita brasileira.",
        "texto_dry_run": body,
        "fatos_travados": [
            {
                "idx": 1,
                "fato": "O USTR publicou transcricao oficial do Dia 2 com Flavio Bolsonaro no Painel 8.",
                "fonte_ref": ["https://ustr.gov/"],
                "obrigatorio_no_texto": True,
            },
            {
                "idx": 2,
                "fato": "O Federal Register publicou notice da investigacao Section 301.",
                "fonte_ref": ["https://www.federalregister.gov/"],
                "obrigatorio_no_texto": True,
            },
        ],
        "collection_request": {
            "status": "recommended",
            "required_before": "publicacao_real",
            "reason": "confirmar comentario escrito antes de publicar",
        },
    }


def _sample_auditado_payload() -> dict[str, object]:
    return {
        "item_id": "v4_real_001",
        "editoria": "v4_politica_economia",
        "titulo": "Tarifa dos EUA transforma Trump em problema eleitoral para Flavio Bolsonaro",
        "conteudo": "Material auditado sobre tarifa dos EUA, disputa politica, Pix e setores produtivos.",
        "primary_entity": "Flavio Bolsonaro",
        "status": "auditado_fixture",
    }


def _sample_leitura_corrente() -> dict[str, object]:
    return {
        "fonte": "manual_editor",
        "timestamp_brt": "2026-07-09T00:00:00-03:00",
        "resumo_consenso": "A cobertura corrente trata a pauta como disputa de narrativa entre Lula e Flavio Bolsonaro sobre tarifas.",
        "fontes_consultadas": ["fixture_manual"],
    }


def _sample_wp_mapping() -> WordPressMediaMapping:
    return WordPressMediaMapping(
        image_id="img1",
        wp_media_id=260961,
        source="manual_fixture",
        url="https://cdn.example.com/flavio-bolsonaro-retrato.jpg",
        credit="Agencia Senado",
        license="Fonte oficial",
    )


def _create_ouro_fixture_db(path: Path) -> None:
    conn = sqlite3.connect(path)
    try:
        conn.executescript(
            """
            CREATE TABLE midia_ouro_indice (
              hash_sha256 TEXT PRIMARY KEY,
              entidade TEXT,
              tema TEXT,
              titulo TEXT,
              descricao TEXT,
              legenda TEXT,
              texto_busca TEXT,
              score REAL
            );
            CREATE TABLE midia_ouro (
              hash_sha256 TEXT PRIMARY KEY,
              r2_key TEXT,
              r2_url TEXT,
              r2_portal_key TEXT,
              r2_portal_url TEXT,
              largura_portal INTEGER,
              altura_portal INTEGER,
              bytes_portal INTEGER,
              content_type_portal TEXT,
              credito TEXT,
              licenca TEXT,
              status_direitos TEXT,
              metadados_json TEXT,
              uso_automatico INTEGER
            );
            """
        )
        conn.execute(
            """
            INSERT INTO midia_ouro_indice
            VALUES ('hash1','Flavio Bolsonaro','politica','Foto de Flavio Bolsonaro','Retrato oficial','Senador em foto oficial','flavio bolsonaro politica retrato',90)
            """
        )
        conn.execute(
            """
            INSERT INTO midia_ouro
            VALUES ('hash1','midia/flavio.jpg','https://r2.example/flavio.jpg','portal/flavio.webp','https://r2.example/flavio.webp',1200,800,100000,'image/jpeg','Agencia Senado','Fonte oficial','fonte_oficial','{"tipo":"retrato"}',1)
            """
        )
        conn.commit()
    finally:
        conn.close()


def _seed_dashboard_data(tmp: str) -> None:
    feedback_path = Path(tmp, "agent_data/v4/feedback/editor_feedback.jsonl")
    feedback_path.parent.mkdir(parents=True, exist_ok=True)
    feedback_path.write_text(
        json.dumps(
            {
                "schema_version": "v1",
                "timestamp": "2026-07-08T00:00:00+00:00",
                "item_id": "item_old",
                "vertical": "v4_test",
                "editor": "miguel",
                "score": 5,
                "sentiment": "positivo",
                "comment": "bom",
                "correction_class": "nenhuma",
                "provider": "gemini",
                "model": "gemini-3.5-flash",
                "operation": "produzir_dry_run",
            },
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    receipt_path = Path(tmp, "agent_data/v4/receipts/v4_test_20260708.jsonl")
    receipt_path.parent.mkdir(parents=True, exist_ok=True)
    receipt = _old_pending_receipt()
    receipt["vertical"] = "v4_test"
    receipt["llm"] = {
        "provider": "gemini",
        "model": "gemini-3.5-flash",
        "tier": "gemini_luxo",
        "tokens_in": 10,
        "tokens_out": 20,
        "duration_ms_llm": 1,
        "prompt_hash": "abc",
    }
    receipt_path.write_text(json.dumps(receipt, sort_keys=True) + "\n", encoding="utf-8")
    recomputed_path = Path(tmp, "agent_data/v4/receipts/recomputed/recomputed_20260708.jsonl")
    recomputed_path.parent.mkdir(parents=True, exist_ok=True)
    recomputed_path.write_text(
        json.dumps(
            {
                "schema_version": "v1",
                "timestamp": "2026-07-08T00:00:00+00:00",
                "source_receipt_file": "agent_data/v4/receipts/v4_test_20260708.jsonl",
                "item_id": "item_old",
                "vertical": "v4_test",
                "operation": "produzir_dry_run",
                "provider": "gemini",
                "model": "gemini-3.5-flash",
                "old_cost_usd_estimated": 0.0,
                "new_cost_usd_estimated": 0.001,
                "old_pricing_table_version": "pending",
                "new_pricing_table_version": "2026-07-08-local-ratings",
                "tokens_in": 10,
                "tokens_out": 20,
                "status": "recomputed",
            },
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    decision_path = Path(tmp, "agent_data/v4/llm_decisions/decisions_20260708.jsonl")
    decision_path.parent.mkdir(parents=True, exist_ok=True)
    decision_path.write_text(json.dumps(_sample_decision().as_dict(), sort_keys=True) + "\n", encoding="utf-8")


def _sample_decision() -> LLMRouterDecision:
    return LLMRouterDecision(
        editoria="v4_test",
        funcao="redacao",
        idempotency_key="item",
        prompt_hash="abc",
        selected_provider="gemini",
        selected_model="gemini-3.5-flash",
        selected_tier="gemini_luxo",
        selection_strategy="quality_cost_router",
        selection_reason="teste",
        candidate_count=3,
        mode="exploration",
        expected_cost_usd=0.001,
        timestamp="2026-07-08T00:00:00+00:00",
    )


if __name__ == "__main__":
    raise SystemExit(main())
