# Fórum V4 — Retomada de testes de rascunhos com imagem destacada (run6)

Data: 16 de julho de 2026

Objetivo: registrar execução final dos 8 testes em draft no WordPress com imagem destacada, juntamente com healthcheck exaustivo de LLM e Vision para retomada.

## Estado objetivo atual

- 8 posts em **`draft`** com **`featured_media`** confirmado no WordPress.
- Healthcheck de LLM **completo**: `24/24` OK.
- Healthcheck de Vision: **degradado** (`ok_count: 0`), sem cenário estável neste momento.
- Evidências preservadas para retomada:
  - `v4_memoria/foruns/healthcheck_llm_matrix_v4_20260716_run6.json`
  - `v4_memoria/foruns/healthcheck_vision_v4_20260716_run6.json`
  - `v4_memoria/foruns/rodada_20260716_updates/wordpress_update_featured_media_run5.jsonl`
  - `v4_memoria/foruns/rodada_20260716_updates/wordpress_update_featured_media_run5_summary.json`

## Healthcheck LLM (run6)

Arquivo:

- `root/v4_labs/v4_memoria/foruns/healthcheck_llm_matrix_v4_20260716_run6.json`

Resumo:

- `total`: 24
- `ok_count`: 24
- `fail_count`: 0

Condição de sucesso (`ok=true`) foi alcançada para 4 editorias × 6 funções porque foram setados:

- `V4_LABS_REAL_ENABLED=1`
- `V4_LABS_ALLOW_REAL_CALLS=1`
- chaves de ambiente carregadas do `.env.unificado`

## Healthcheck Vision (run6)

Arquivo:

- `root/v4_labs/v4_memoria/foruns/healthcheck_vision_v4_20260716_run6.json`

Resumo:

- `case_count`: 4
- `ok_count`: 0
- `status`: `degraded`
- Casos:
  - `current_env`: `media_vision_all_providers_failed` (ambos os provedores disponíveis)
  - `with_invalid_gemini`: `gemini_request_failed`
  - `without_qwen`: `gemini_request_failed`
  - `no_media_keys`: `media_vision_api_key_missing`

## Rascunhos atualizados no WordPress (todos com imagem destacada)

| Editorial | Post ID | Status | Featured Image ID | Link do post | Link da imagem destacada |
|---|---:|---|---:|---|---|
| Política e Economia | 261601 | draft | 261810 | https://controle.ocafezinho.com/?p=261601 | https://controle.ocafezinho.com/wp-content/uploads/2026/07/ig-cropped-image-89.jpg |
| Política e Economia | 261602 | draft | 261807 | https://controle.ocafezinho.com/?p=261602 | https://controle.ocafezinho.com/wp-content/uploads/2026/07/ig-cropped-image-88.jpg |
| Internacional | 261603 | draft | 261801 | https://controle.ocafezinho.com/?p=261603 | https://controle.ocafezinho.com/wp-content/uploads/2026/07/ig-cropped-image-87.jpg |
| Internacional | 261604 | draft | 261799 | https://controle.ocafezinho.com/?p=261604 | https://controle.ocafezinho.com/wp-content/uploads/2026/07/usa-brazil-tariffs.jpg |
| Ciência, Tecnologia e IA | 261605 | draft | 261798 | https://controle.ocafezinho.com/?p=261605 | https://controle.ocafezinho.com/wp-content/uploads/2026/07/ig-cropped-image-86.jpg |
| Ciência, Tecnologia e IA | 261606 | draft | 261795 | https://controle.ocafezinho.com/?p=261606 | https://controle.ocafezinho.com/wp-content/uploads/2026/07/ig-cropped-image-85.jpg |
| Cultura | 261607 | draft | 261792 | https://controle.ocafezinho.com/?p=261607 | https://controle.ocafezinho.com/wp-content/uploads/2026/07/forex-trade-graph-chart-concept-scaled.jpg |
| Cultura | 261608 | draft | 261790 | https://controle.ocafezinho.com/?p=261608 | https://controle.ocafezinho.com/wp-content/uploads/2026/07/ig-cropped-image-84.jpg |

## Lições de retomada (cérebro / memória operacional)

- Os 8 posts estão confirmados em WordPress como `draft` com `featured_media`, então estes vínculos já podem ser usados para validação final.
- O `healthcheck` de Vision ainda precisa de correção de conectividade/credenciais para sair de `degraded`.
- O pacote de atualização com sucesso fica em:
  - `root/v4_labs/v4_memoria/foruns/rodada_20260716_updates/wordpress_update_featured_media_run5.jsonl`

