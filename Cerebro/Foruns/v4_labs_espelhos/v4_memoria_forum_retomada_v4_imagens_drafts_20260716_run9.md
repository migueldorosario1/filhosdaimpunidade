# Fórum V4 — Retomada de testes de rascunhos com imagem destacada (16/07/2026)

Objetivo: consolidar estado final após correção de inconsistência do relatório anterior, garantindo os 8 testes de draft com imagem destacada, healthcheck completo de LLM e Vision, e indexação em memória operacional.

## Estado objetivo final

- Foram validados 8 itens (2 por editoria), todos persistidos no WordPress como `draft` com `featured_media`.
- Healthcheck LLM: `24/24` OK.
- Healthcheck Vision: `0/7` OK (`degraded`).

Evidências base:

- `v4_memoria/foruns/healthcheck_llm_matrix_v4_20260716_run9.json`
- `v4_memoria/foruns/healthcheck_vision_v4_20260716_run9.json`
- `v4_memoria/foruns/rodada_20260716_updates/wordpress_update_featured_media_run5_summary.json`
- `v4_memoria/foruns/rodada_20260716_updates/wordpress_update_featured_media_run5.jsonl`
- Receipts individuais em `dados/rodada_v4_20260714/delivery_receipts/update_2616*.json`

## Healthcheck LLM (run9)

Arquivo: `v4_memoria/foruns/healthcheck_llm_matrix_v4_20260716_run9.json`

- `editorias`: 4 (`v4_politica_economia`, `v4_internacional`, `v4_ciencia_tecnologia_ia`, `v4_cultura`)
- `funcs`: 6 (`auditoria`, `curadoria`, `fact_check`, `imagem`, `redacao`, `revisao`)
- `total`: 24
- `ok_count`: 24
- `fail_count`: 0
- `status`: `healthy` (em termos de configuração de LLMs e ambiente, com `real` e `allow_real` habilitados)

Condições de sucesso usadas no run:

- `V4_LABS_REAL_ENABLED=1`
- `V4_LABS_ALLOW_REAL_CALLS=1`

## Healthcheck Vision (run9 — exaustivo)

Arquivo: `v4_memoria/foruns/healthcheck_vision_v4_20260716_run9.json`

- `case_count`: 7
- `ok_count`: 0
- `status`: `degraded`

Casos e resultado:

- `current_env`: `media_vision_all_providers_failed` (Qwen + Gemini presentes; falha de retorno em cadeia)
- `no_media_keys`: `media_vision_api_key_missing`
- `with_invalid_gemini`: `gemini_request_failed`
- `without_qwen`: `gemini_request_failed`
- `with_qwen_2_only`: `qwen_http_status:400`
- `with_invalid_das`: `qwen_base_url_invalid`
- `with_invalid_qwen`: `qwen_api_key_missing`

Nota operacional:

- Nenhum cenário de produção automática foi aprovado em Vision; a pipeline visual permanece em bloqueio controlado para não registrar metadados de destaque inválidos.

## Prova de publicação em rascunho com imagem destacada (WordPress)

Links já confirmados via API autenticada (`/wp/v2/posts/{id}` + `/wp/v2/media/{featured_media}`):

| Editoria | Post ID | Slug | Status | featured_media | Post | Imagem destacada |
|---|---:|---|---|---:|---|---|
| Política e Economia | 261601 | politica_20260714_03_emprego_qualidade | draft | 261810 | https://controle.ocafezinho.com/?p=261601 | https://controle.ocafezinho.com/wp-content/uploads/2026/07/ig-cropped-image-89.jpg |
| Política e Economia | 261602 | politica_20260714_05_brasil_soberano | draft | 261807 | https://controle.ocafezinho.com/?p=261602 | https://controle.ocafezinho.com/wp-content/uploads/2026/07/ig-cropped-image-88.jpg |
| Internacional | 261603 | internacional_20260714_01 | draft | 261801 | https://controle.ocafezinho.com/?p=261603 | https://controle.ocafezinho.com/wp-content/uploads/2026/07/ig-cropped-image-87.jpg |
| Internacional | 261604 | internacional_20260714_02 | draft | 261799 | https://controle.ocafezinho.com/?p=261604 | https://controle.ocafezinho.com/wp-content/uploads/2026/07/usa-brazil-tariffs.jpg |
| Ciência, Tecnologia e IA | 261605 | ciencia_20260714_01 | draft | 261798 | https://controle.ocafezinho.com/?p=261605 | https://controle.ocafezinho.com/wp-content/uploads/2026/07/ig-cropped-image-86.jpg |
| Ciência, Tecnologia e IA | 261606 | ciencia_20260714_02 | draft | 261795 | https://controle.ocafezinho.com/?p=261606 | https://controle.ocafezinho.com/wp-content/uploads/2026/07/ig-cropped-image-85.jpg |
| Cultura | 261607 | cultura_20260714_streaming | draft | 261792 | https://controle.ocafezinho.com/?p=261607 | https://controle.ocafezinho.com/wp-content/uploads/2026/07/forex-trade-graph-chart-concept-scaled.jpg |
| Cultura | 261608 | cultura_20260714_patrimonio_clima | draft | 261790 | https://controle.ocafezinho.com/?p=261608 | https://controle.ocafezinho.com/wp-content/uploads/2026/07/ig-cropped-image-84.jpg |

## Lições e continuidade para retomada

- Os 8 rascunhos permanecem íntegros e verificáveis; a divergência anterior ficou encerrada nesta rodada.
- O gargalo atual não está em LLM nem em publicação de WP, e sim em Vision (rede/provedores), onde os cenários reais permanecem reprovados.
- Para nova retomada:
  1. Corrigir credenciais/provedor Vision e reexecutar `healthcheck_vision_v4_20260716_run10.json`.
  2. Executar novo pacote de atualização se houver mudança de política (não necessário para este batch já publicado em draft).
  3. Registrar no mesmo padrão de fórum e adicionar link em `CEREBRO_NODE_CHECKUPS.md`.

