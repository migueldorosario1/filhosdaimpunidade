# Fórum V4 — Correção de healthcheck Vision e continuidade da retomada (16/07/2026)

Objetivo: corrigir o diagnóstico do healthcheck Vision (casos inválidos sem chaves), preservar evidências no cérebro e manter continuidade dos testes de rascunhos.

## Ajuste aplicado

- Criei o novo runner canônico de healthcheck Vision: `codigo/vision_healthcheck_cli.py`
- O runner passa a montar cada cenário por override isolado do ambiente (`clean clone + set/remove`), sem apagar variáveis não relacionadas.
- Isso elimina falsos `media_vision_api_key_missing` em cenários que ainda tinham mídia disponível.

## Resultados Vision (run11)

Arquivo: `v4_memoria/foruns/healthcheck_vision_v4_20260716_run11.json`

- `case_count`: 7
- `ok_count`: 0
- `status`: `degraded`

Situações observadas:

- `current_env`: `media_vision_all_providers_failed`
- `no_media_keys`: `media_vision_api_key_missing`
- `with_invalid_das`: `media_vision_all_providers_failed`
- `with_invalid_gemini`: `gemini_request_failed`
- `with_invalid_qwen`: `qwen_http_status:401`
- `with_qwen_2_only`: `qwen_http_status:400`
- `without_qwen`: `gemini_request_failed`

Interpretação:

- O healthcheck ainda não alcança status `healthy` por indisponibilidade de respostas válidas dos provedores Vision na chave/base atual.
- O problema de “degradado por cenário com chaves ausentes em cadeia” foi corrigido no relatório: os cenários estão coerentes com a configuração por cenário.

## Rascunhos com imagem destacada

As 8 execuções de draft (2 por editoria) já foram geradas e validadas em etapas anteriores:

- `v4_memoria/foruns/forum_retomada_v4_imagens_drafts_20260716.md`
- `v4_memoria/foruns/forum_retomada_v4_imagens_drafts_20260716_run9.md`

Posts confirmados em `draft`:

- `261601`, `261602`, `261603`, `261604`, `261605`, `261606`, `261607`, `261608`
- links e `featured_media` em: `forum_retomada_v4_imagens_drafts_20260716_run9.md`

## Continuidade

Próximo passo recomendado antes de novo pacote de produção:

1. Manter `healthcheck` Vision como parte da rotina (usar `codigo/vision_healthcheck_cli.py`).
2. Revalidar chave/provedor Vision com ambiente novo (ex.: rodar com `--strict` e chave que retorne OK para reduzir `qwen_http_status`).
3. Com provedor Vision saudável, repetir fluxo de 8 rascunhos e build conforme autorização em `publication_authorizations`.
