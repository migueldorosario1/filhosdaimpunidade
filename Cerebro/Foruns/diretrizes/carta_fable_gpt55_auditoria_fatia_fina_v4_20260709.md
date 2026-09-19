# Carta para Fable e GPT 5.5 Pro — auditoria da fatia fina V4

Ver arquivo canonico no forum:

```text
/home/migueldorosario/Downloads/Antigravity Google/Cerebro/Foruns/carta_fable_gpt55_auditoria_fatia_fina_v4_20260709.md
```

Arquivos a auditar neste diretorio:

```text
v4_curadoria_tese_v1.json
v4_feedback_casos_editoriais_v1.json
v4_agentes_tecnicos_v1.json
v4_bancos_camadas_v1.json
v4_fluxo_dry_run_v1.json
v4_wordpress_publicador_v1.json
v4_imagem_destacada_v1.json
v4_real_001.curadoria.json
v4_real_001.variant_b.producao.json
ab_261439_curadoria_v4_fase_1.json
```

Resumo: Codex implementou a fatia fina da curadoria V4 em dry-run, com `curadoria_id` como gate, `modo_experimento` restrito a A/B dry-run, leitura corrente com fonte, produtor lendo curadoria, publicador bloqueando sem curadoria, e A/B 261439 gerado localmente. Depois do probe do Fable, `manual_editor` em modo real foi bloqueado no `validate_gate`. Depois da reauditoria externa, entrou teste de reconciliacao do espelho. Na Fase 2, `collection_request` ganhou semantica formal, o redator shadow foi criado e os artefatos do 261439 foram ressincronizados. Testes: `OK 52 contract tests`.
