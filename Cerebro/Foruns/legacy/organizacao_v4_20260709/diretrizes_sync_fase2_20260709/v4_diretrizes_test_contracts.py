from __future__ import annotations

import json
import hashlib
import os
import sqlite3
import tempfile
import threading
from pathlib import Path

from .fluxo import V4DryRunFlow
from .curadoria_tese import V4CuradoriaTese
from .ab_experiment import V4CuradoriaABExperiment
from .content_ingestion import V4ContentIngestion
from .feedback import V4EditorFeedbackStore
from .imagem_destacada import MediaCandidate, V4FeaturedImageEvaluator
from .llm_dashboard import V4LLMDashboard
from .llm_decisions import LLMRouterDecision, V4LLMDecisionStore
from .media_audit import V4AuditedMediaStore
from .media_sources import V4MediaSourceCollector
from .pricing import V4Pricing
from .operational_dashboard import V4OperationalDashboard
from .recompute_costs import V4CostRecomputer
from .model_router import V4ModelRouter
from .redator_shadow import V4ShadowRedator
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
        test_recompute_costs_append_only_recalcula_pendente,
        test_feedback_ranking_usa_custo_recomputado,
        test_model_router_recomenda_por_qualidade_custo,
        test_model_router_respeita_exclude_provider,
        test_llm_decision_store_grava_jsonl,
        test_llm_decision_faltando_required_retorna_ok_false,
        test_llm_dashboard_grava_json_e_markdown,
        test_llm_dashboard_markdown_contem_ranking_e_decisoes,
        test_curadoria_cria_tres_teses_e_frame_visual,
        test_curadoria_tem_consequencia_material_e_collection_request,
        test_curadoria_dict_vazio_em_required_bloqueia,
        test_curadoria_fatos_travados_preservam_atribuicao,
        test_curadoria_sem_fonte_leitura_corrente_bloqueia,
        test_producao_sem_curadoria_bloqueia,
        test_modo_experimento_sem_curadoria_somente_dry_run,
        test_publicacao_real_bloqueia_fonte_manual,
        test_redator_shadow_gera_prompt_sem_chamada_externa,
        test_collection_recommended_bloqueia_no_estagio_indicado,
        test_espelho_diretrizes_reconciliado_com_fonte_viva,
        test_fluxo_dry_run_executa_curadoria_antes_da_producao,
        test_ab_261439_grava_pacote_cego_sem_publicacao,
        test_imagem_destacada_aprova_candidato_com_direitos_e_entidade,
        test_imagem_destacada_rejeita_thumbnail_sem_direitos,
        test_imagem_destacada_grava_decisao_append_only,
        test_media_source_ouro_sqlite_normaliza_candidato,
        test_media_source_ouro_sqlite_indisponivel_nao_quebra,
        test_media_source_path_exists_trata_oserror,
        test_media_audit_promove_aprovada_e_busca_por_entidade,
        test_media_audit_bloqueia_avaliacao_reprovada,
        test_fluxo_publicacao_bloqueia_sem_midia_auditada,
        test_fluxo_publicacao_anexa_midia_auditada,
        test_wordpress_publicador_dry_run_grava_tentativa,
        test_wordpress_publicador_real_bloqueado_por_contrato,
        test_wordpress_publicador_bloqueia_sem_featured_media,
        test_wordpress_publicador_bloqueia_sem_curadoria_id,
        test_wordpress_publicador_real_bloqueia_ascii_sem_acentos,
        test_wordpress_media_mapping_append_lookup,
        test_wordpress_publicador_usa_mapping_wp_media_id,
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
        assert estimate.pricing_table_version == "2026-07-08-local-ratings"


def test_recompute_costs_append_only_recalcula_pendente() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        contract = _copy_recompute_contract(tmp)
        _copy_pricing_contract(tmp)
        receipt_dir = Path(tmp, "agent_data/v4/receipts")
        receipt_dir.mkdir(parents=True, exist_ok=True)
        receipt_path = receipt_dir / "v4_test_20260708.jsonl"
        original = json.dumps(_old_pending_receipt(), ensure_ascii=False, sort_keys=True) + "\n"
        receipt_path.write_text(original, encoding="utf-8")
        production_path = Path(tmp, "v4_data/producao/item_old.producao.json")
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
        assert Path(tmp, "v4_data/producao_shadow/v4_real_001.shadow_redacao.json").exists()


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


def test_espelho_diretrizes_reconciliado_com_fonte_viva() -> None:
    pairs = [
        ("diretrizes/v4_fluxo_dry_run_v1.json", "Cerebro/Foruns/diretrizes/v4_fluxo_dry_run_v1.json"),
        ("diretrizes/v4_agentes_tecnicos_v1.json", "Cerebro/Foruns/diretrizes/v4_agentes_tecnicos_v1.json"),
        ("diretrizes/v4_feedback_casos_editoriais_v1.json", "Cerebro/Foruns/diretrizes/v4_feedback_casos_editoriais_v1.json"),
        ("diretrizes/v4_bancos_camadas_v1.json", "Cerebro/Foruns/diretrizes/v4_bancos_camadas_v1.json"),
        ("diretrizes/v4_wordpress_publicador_v1.json", "Cerebro/Foruns/diretrizes/v4_wordpress_publicador_v1.json"),
        ("diretrizes/v4_curadoria_tese_v1.json", "Cerebro/Foruns/diretrizes/v4_curadoria_tese_v1.json"),
        ("diretrizes/v4_redator_shadow_v1.json", "Cerebro/Foruns/diretrizes/v4_redator_shadow_v1.json"),
    ]
    for canonical, mirror in pairs:
        canonical_path = Path(canonical)
        mirror_path = Path(mirror)
        assert canonical_path.exists(), canonical
        assert mirror_path.exists(), mirror
        assert _sha256(canonical_path) == _sha256(mirror_path), f"espelho divergente: {mirror}"
    flow = json.loads(Path("Cerebro/Foruns/diretrizes/v4_fluxo_dry_run_v1.json").read_text(encoding="utf-8"))
    assert flow["steps"][0]["name"] == "curadoria_dry_run"
    assert flow["steps"][1]["from"] == "curadoria"
    agents = json.loads(Path("Cerebro/Foruns/diretrizes/v4_agentes_tecnicos_v1.json").read_text(encoding="utf-8"))
    assert "curador" in agents["agents"]
    assert agents["agents"]["produtor"]["default_read_layers"] == ["curadoria"]
    assert agents["agents"]["imagem"]["default_read_layers"] == ["curadoria"]


def test_fluxo_dry_run_executa_curadoria_antes_da_producao() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        _copy_layers_contract(tmp)
        _copy_flow_contract(tmp)
        _copy_curadoria_contract(tmp)
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


def test_ab_261439_grava_pacote_cego_sem_publicacao() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        _copy_curadoria_contract(tmp)
        auditado_path = Path(tmp, "v4_data/auditado/v4_real_001.json")
        auditado_path.parent.mkdir(parents=True, exist_ok=True)
        auditado_path.write_text(json.dumps(_sample_auditado_payload(), ensure_ascii=False), encoding="utf-8")
        producao_path = Path(tmp, "v4_data/producao/v4_real_001.producao.json")
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


def test_fluxo_publicacao_bloqueia_sem_midia_auditada() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        contract = _copy_imagem_destacada_contract(tmp)
        flow = V4DryRunFlow.__new__(V4DryRunFlow)
        flow.media_store = V4AuditedMediaStore(root=tmp, contract_path=contract)
        output = {"primary_entity": "Flavio Bolsonaro", "manifesto": {}, "publicacao_dry_run": {}}
        issues = flow._attach_required_media({"name": "publicar_dry_run"}, output)
        assert issues
        assert output["manifesto"]["imagem_destacada_validada"] is False


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


def test_wordpress_publicador_bloqueia_sem_featured_media() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        _copy_wordpress_media_contract(tmp)
        contract = _copy_wordpress_contract(tmp)
        publisher = V4WordPressPublisher(root=tmp, contract_path=contract)
        payload = _sample_publication_payload()
        del payload["featured_media"]
        result = publisher.publish_payload(payload)
        assert result["ok"] is False
        assert "campo_publicacao_ausente:featured_media" in result["attempt"]["issues"]


def test_wordpress_publicador_bloqueia_sem_curadoria_id() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        _copy_wordpress_media_contract(tmp)
        contract = _copy_wordpress_contract(tmp)
        publisher = V4WordPressPublisher(root=tmp, contract_path=contract)
        payload = _sample_publication_payload()
        del payload["curadoria_id"]
        result = publisher.publish_payload(payload)
        assert result["ok"] is False
        assert "campo_publicacao_ausente:curadoria_id" in result["attempt"]["issues"]


def test_wordpress_publicador_real_bloqueia_ascii_sem_acentos() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        _copy_wordpress_media_contract(tmp)
        contract = _copy_wordpress_contract(tmp)
        publisher = V4WordPressPublisher(root=tmp, contract_path=contract)
        payload = _sample_publication_payload()
        payload["texto_dry_run"] = "Texto de politica sem acentos " * 20
        payload["featured_media"]["credit"] = "Agencia Senado"
        payload["featured_media"]["license"] = "Fonte oficial"
        result = publisher.publish_payload(payload, real=True)
        assert "encoding_portugues_ascii_sem_acentos" in result["attempt"]["issues"]


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


def test_operational_dashboard_grava_json_markdown() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        contract = _copy_operational_dashboard_contract(tmp)
        Path(tmp, "v4_data/auditado").mkdir(parents=True)
        Path(tmp, "v4_data/auditado/item.json").write_text("{}", encoding="utf-8")
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
        assert Path(tmp, "v4_data/bruto/v4_ingest_001.bruto.json").exists()
        assert Path(tmp, "v4_data/intermediario/v4_ingest_001.intermediario.json").exists()
        audited = Path(tmp, "v4_data/auditado/v4_ingest_001.json")
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
    source = Path("diretrizes/v4_telemetria_v1.json")
    target = Path(tmp, "diretrizes/v4_telemetria_v1.json")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
    return "diretrizes/v4_telemetria_v1.json"


def _copy_layers_contract(tmp: str) -> str:
    source = Path("diretrizes/v4_bancos_camadas_v1.json")
    target = Path(tmp, "diretrizes/v4_bancos_camadas_v1.json")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
    return "diretrizes/v4_bancos_camadas_v1.json"


def _copy_flow_contract(tmp: str) -> str:
    source = Path("diretrizes/v4_fluxo_dry_run_v1.json")
    target = Path(tmp, "diretrizes/v4_fluxo_dry_run_v1.json")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
    return "diretrizes/v4_fluxo_dry_run_v1.json"


def _copy_curadoria_contract(tmp: str) -> str:
    source = Path("diretrizes/v4_curadoria_tese_v1.json")
    target = Path(tmp, "diretrizes/v4_curadoria_tese_v1.json")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
    return "diretrizes/v4_curadoria_tese_v1.json"


def _copy_redator_shadow_contract(tmp: str) -> str:
    source = Path("diretrizes/v4_redator_shadow_v1.json")
    target = Path(tmp, "diretrizes/v4_redator_shadow_v1.json")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
    return "diretrizes/v4_redator_shadow_v1.json"


def _copy_ingestion_contract(tmp: str) -> str:
    source = Path("diretrizes/v4_ingestao_conteudo_v1.json")
    target = Path(tmp, "diretrizes/v4_ingestao_conteudo_v1.json")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
    return "diretrizes/v4_ingestao_conteudo_v1.json"


def _copy_feedback_contract(tmp: str) -> str:
    source = Path("diretrizes/v4_feedback_editor_v1.json")
    target = Path(tmp, "diretrizes/v4_feedback_editor_v1.json")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
    memory_source = Path("diretrizes/v4_memoria_autocura_v1.json")
    memory_target = Path(tmp, "diretrizes/v4_memoria_autocura_v1.json")
    memory_target.write_text(memory_source.read_text(encoding="utf-8"), encoding="utf-8")
    return "diretrizes/v4_feedback_editor_v1.json"


def _copy_pricing_contract(tmp: str) -> str:
    source = Path("diretrizes/v4_pricing_llm_v1.json")
    target = Path(tmp, "diretrizes/v4_pricing_llm_v1.json")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
    return "diretrizes/v4_pricing_llm_v1.json"


def _copy_recompute_contract(tmp: str) -> str:
    source = Path("diretrizes/v4_recompute_costs_v1.json")
    target = Path(tmp, "diretrizes/v4_recompute_costs_v1.json")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
    return "diretrizes/v4_recompute_costs_v1.json"


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
    source = Path("diretrizes/v4_llm_decisions_v1.json")
    target = Path(tmp, "diretrizes/v4_llm_decisions_v1.json")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
    return "diretrizes/v4_llm_decisions_v1.json"


def _copy_adapter_contract(tmp: str) -> str:
    source = Path("diretrizes/v4_llm_adapter_v1.json")
    target = Path(tmp, "diretrizes/v4_llm_adapter_v1.json")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
    return "diretrizes/v4_llm_adapter_v1.json"


def _copy_context_map(tmp: str) -> str:
    source = Path("diretrizes/mapa_v4_contexto_llm.json")
    target = Path(tmp, "diretrizes/mapa_v4_contexto_llm.json")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
    for doc in [
        "v4_nucleo_editorial_comum_v1.md",
        "v4_politica_economia_v1.md",
        "v4_freios_llm_v1.json",
        "v4_rotas_llm_limpas_v1.json",
        "v4_orquestracao_llm_v1.json",
        "v4_model_router_v1.json",
    ]:
        source_doc = Path("diretrizes", doc)
        target_doc = Path(tmp, "diretrizes", doc)
        target_doc.write_text(source_doc.read_text(encoding="utf-8"), encoding="utf-8")
    return "diretrizes/mapa_v4_contexto_llm.json"


def _copy_llm_routes_contract(tmp: str) -> str:
    source = Path("diretrizes/v4_rotas_llm_limpas_v1.json")
    target = Path(tmp, "diretrizes/v4_rotas_llm_limpas_v1.json")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
    return "diretrizes/v4_rotas_llm_limpas_v1.json"


def _copy_llm_orchestration_contract(tmp: str) -> str:
    source = Path("diretrizes/v4_orquestracao_llm_v1.json")
    target = Path(tmp, "diretrizes/v4_orquestracao_llm_v1.json")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
    return "diretrizes/v4_orquestracao_llm_v1.json"


def _copy_dashboard_contract(tmp: str) -> str:
    source = Path("diretrizes/v4_llm_dashboard_v1.json")
    target = Path(tmp, "diretrizes/v4_llm_dashboard_v1.json")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
    _copy_feedback_contract(tmp)
    return "diretrizes/v4_llm_dashboard_v1.json"


def _copy_imagem_destacada_contract(tmp: str) -> str:
    source = Path("diretrizes/v4_imagem_destacada_v1.json")
    target = Path(tmp, "diretrizes/v4_imagem_destacada_v1.json")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
    return "diretrizes/v4_imagem_destacada_v1.json"


def _copy_wordpress_contract(tmp: str) -> str:
    source = Path("diretrizes/v4_wordpress_publicador_v1.json")
    target = Path(tmp, "diretrizes/v4_wordpress_publicador_v1.json")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
    return "diretrizes/v4_wordpress_publicador_v1.json"


def _copy_wordpress_media_contract(tmp: str) -> str:
    source = Path("diretrizes/v4_wordpress_media_v1.json")
    target = Path(tmp, "diretrizes/v4_wordpress_media_v1.json")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
    return "diretrizes/v4_wordpress_media_v1.json"


def _copy_operational_dashboard_contract(tmp: str) -> str:
    source = Path("diretrizes/v4_operational_dashboard_v1.json")
    target = Path(tmp, "diretrizes/v4_operational_dashboard_v1.json")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
    return "diretrizes/v4_operational_dashboard_v1.json"


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
