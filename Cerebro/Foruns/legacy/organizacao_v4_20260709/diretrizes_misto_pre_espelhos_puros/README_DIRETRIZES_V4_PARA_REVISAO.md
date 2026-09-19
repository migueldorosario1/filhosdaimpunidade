# Diretrizes V4 para revisao externa

Criado em: 2026-07-08 23:19 BRT

Este diretorio e um espelho das diretrizes V4 para revisao por Fable, AGY e demais pareceristas.

Importante:

```text
Fonte viva original:
/home/migueldorosario/Downloads/Antigravity Google/diretrizes/

Espelho para revisao:
/home/migueldorosario/Downloads/Antigravity Google/Cerebro/Foruns/v4/diretrizes/
```

Nao editar este espelho como fonte de execucao sem reconciliar depois com `diretrizes/`.

## Objetivo da revisao

Avaliar se as diretrizes do V4 estao:

```text
- externas aos agentes;
- limpas;
- sem hardcode editorial;
- suficientemente fortes para gerar textos com tese;
- leves o bastante para nao virarem burocracia;
- conectadas a memoria de bugs e feedback do editor;
- adequadas ao lema do V4: limpeza, ordem, organizacao, leveza, automacao.
```

## Forum canonico da discussao

```text
/home/migueldorosario/Downloads/Antigravity Google/Cerebro/Foruns/v4/foruns/forum_v4_curadoria_tese_editorial_20260708.md
```

## Forum de producao da implementacao

```text
/home/migueldorosario/Downloads/Antigravity Google/Cerebro/Foruns/v4/foruns/forum_producao_v4_curadoria_tese_20260709.md
```

## Arquivos espelhados

```text
mapa_v4_contexto_llm.json
v4_agentes_tecnicos_v1.json
v4_bancos_camadas_v1.json
v4_ciencia_tecnologia_ia_v1.md
v4_cultura_v1.md
v4_curadoria_tese_v1.json
v4_feedback_editor_v1.json
v4_feedback_casos_editoriais_v1.json
v4_fluxo_dry_run_v1.json
v4_freios_llm_v1.json
v4_gsn_espelho_ingles_v1.md
v4_imagem_destacada_v1.json
v4_ingestao_conteudo_v1.json
v4_internacional_v1.md
v4_llm_adapter_v1.json
v4_llm_dashboard_v1.json
v4_llm_decisions_v1.json
v4_memoria_autocura_v1.json
v4_model_router_v1.json
v4_nucleo_editorial_comum_v1.md
v4_operacao_limpeza_ordem_backup_v1.json
v4_operational_dashboard_v1.json
v4_orquestracao_llm_v1.json
v4_politica_economia_v1.md
v4_pricing_llm_v1.json
v4_recompute_costs_v1.json
v4_repetidor_v1.md
v4_redator_shadow_v1.json
v4_rotas_llm_limpas_v1.json
v4_telemetria_v1.json
v4_wordpress_media_v1.json
v4_wordpress_publicador_v1.json
```

## Artefatos da fatia fina Fase 1

```text
MANIFESTO_RECONCILIACAO_ESPELHO_V4_20260709.md
ab_261439_artigos_para_auditoria.md
ab_261439_julgamento_cego_miguel.md
v4_real_001.variant_a_original.producao.json
v4_real_001.curadoria.json
v4_real_001.variant_b.producao.json
ab_261439_curadoria_v4_fase_1.json
v4_real_001.shadow_redacao.json
```

Esses arquivos sao para auditoria do smoke test A/B do post 261439. Eles nao sao publicacao real e nao devem ser tratados como fonte canonica de execucao.

## Codigo espelhado para auditoria

```text
v4_diretrizes_curadoria_tese.py
v4_diretrizes_ab_experiment.py
v4_diretrizes_test_contracts.py
v4_diretrizes_fluxo.py
v4_diretrizes_redator_shadow.py
v4_diretrizes_redator_shadow_cli.py
v4_diretrizes_wordpress_publicador.py
```

Esses arquivos `.py` sao copia de auditoria. A fonte viva continua em `v4_diretrizes/`.

## Validacao do espelho

`v4_diretrizes_test_contracts.py` inclui `test_espelho_diretrizes_reconciliado_com_fonte_viva`.

Validacao atual:

```text
OK 52 contract tests
```

Pacote executavel para auditoria externa:

```text
/home/migueldorosario/Downloads/Antigravity Google/Cerebro/Foruns/v4/pacotes/pacote_auditoria_v4_fase2_standalone_20260709.tar.gz
```

## Pedido aos pareceristas

Ler os arquivos como arquitetura editorial e operacional do V4, nao como documentos isolados.

Responder:

```text
1. O que esta bom e deve ser preservado?
2. O que esta redundante?
3. O que esta burocratico demais?
4. O que falta para a curadoria de tese?
5. O que falta para memoria viva de feedback editorial?
6. O que falta para imagem destacada e banco de midia?
7. O que falta para telemetria/custos/auditoria?
8. Quais arquivos deveriam ser fundidos, divididos ou renomeados?
9. Qual e o minimo que devemos codar primeiro?
```

Regra de comunicacao:

```text
Responder no forum canonico.
Pontuar curto no Canal da Trindade.
Manter inbox limpo e curto.
Deixar carta humanizada para Miguel.
Declarar escopo: o que leu e o que nao leu.
```
