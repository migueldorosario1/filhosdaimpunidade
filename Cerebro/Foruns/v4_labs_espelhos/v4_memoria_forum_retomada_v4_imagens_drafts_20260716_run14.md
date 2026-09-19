# Fórum V4 — Correção do healthcheck Vision (16/07/2026)

Objetivo: eliminar falso `degraded` causado por fixture de imagem inválida e manter a retomada com evidências centralizadas.

## Correção aplicada

- Arquivo alterado: `codigo/vision_healthcheck_cli.py`
  - Ajustado `sample_image` de 1×1 px para PNG real de 64×64.
  - Ajustado o `request.image` do healthcheck para `width`/`height` de 64.
- Resultado principal:
  - `v4_memoria/foruns/healthcheck_vision_v4_20260716_run14.json`

## Resultado Vision run14

- `case_count`: 7
- `ok_count`: 3
- `status`: `degraded`

### Por cenário

- `current_env`: ✅ `OK` (primeiro retorno válido com fallback Qwen)
- `with_invalid_das`: ✅ `OK`
- `with_qwen_2_only`: ✅ `OK`
- `no_media_keys`: `media_vision_api_key_missing`
- `with_invalid_gemini`: `gemini_request_failed`
- `with_invalid_qwen`: `qwen_http_status:401`
- `without_qwen`: `gemini_request_failed`

### Interpretação técnica

- O bloqueio estrutural de Vision foi removido: o stack não está mais falhando por fixture de imagem inválida.
- A falha remanescente é operacional nos cenários de Gemini/invalidação de chaves:
  - `gemini_request_failed` e `qwen_http_status:401` continuam sem recuperação com as chaves atuais.
- Os cenários de produção (`current_env`) e fallback via Qwen voltaram a responder.

## Continuidade de memória

- Fórum canônico anterior de retomada com links dos 8 drafts e `featured_media`: `v4_memoria/foruns/forum_retomada_v4_imagens_drafts_20260716_run9.md`
- `CEREBRO_NODE_CHECKUPS.md` atualizado para registrar a nova run e o ajuste de amostra de fixture.

## Próximo passo recomendado

1. Decidir se atualizamos chaves/provedor Gemini nesta janela.
2. Se Gemini vier estável, reexecutar `vision_healthcheck_cli.py` e validar se `ok_count` sobe conforme cenário esperado.
3. Repetir ciclo de build/publish guardado com a mesma retenção (somente draft) no pacote autorizado.
