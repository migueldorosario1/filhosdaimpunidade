# 🧠 MEMÓRIA — Config técnico: DeepSeek Flash + Vision no ZCode Miguel ("JPSC")

**Data:** 2026-08-30 ~08:40 BRT · **Autor:** ZCode/Qwen 3.8 (Dell)
**Fórum irmão:** `Foruns/forum_config_jpsc_deepseek_flash_vision_zcode_20260830.md`

## Contexto
Miguel pediu para configurar "JPSC Flash" e "JPSC Vision" no ZCode Miguel. Sigla não batia com nada → identificado como **DeepSeek** (transcrição de voz). Config alvo: `~/.zcode/v2/config.json`.

## Passos executados (comandos/receita)

1. **Backup:** `cp ~/.zcode/v2/config.json ~/.zcode/v2/config.json.bak_pre_deepseek_flash_vision_20260830_084005`
2. **Edição via script Python** (lê o JSON, reaproveita `apiKey` do provider DeepSeek existente sem expor, escreve de volta):
   - Provider DeepSeek existente `397f633c-73af-424a-a8fa-552e7818e123` (kind `anthropic`, baseURL `https://api.deepseek.com/anthropic`): acrescentado `deepseek-v4-flash` (reasoning off/high/max, contexto 1M, saída 384k, input texto).
   - Criado provider novo `ac5ddbd3-1f43-4c6b-9003-c8f4810941e3` = **"DeepSeek Vision"**, kind `openai-compatible`, baseURL `https://api.deepseek.com`, `enabled:true`, modelo `deepseek-v4-flash-vision-exp` (input `["text","image"]`, output texto, contexto 1M/saída 384k, `zcode.modalitiesConfigured:true`).
3. **Validação JSON:** `json.load` passou; total de providers 13.

## Testes na API real (chave lida do config, não exposta)

- `deepseek-v4-flash` via `https://api.deepseek.com/chat/completions` → HTTP 200, respondeu `FLASH-OK` (finish_reason stop).
- `deepseek-v4-flash-vision-exp` via `https://api.deepseek.com/chat/completions` → HTTP 200, respondeu "OK".
- `deepseek-v4-flash` via endpoint Anthropic `https://api.deepseek.com/anthropic/v1/messages` (header `x-api-key`, `anthropic-version:2023-06-01`) → HTTP 200, respondeu `ANTHROPIC-OK`. (Confirma o caminho configurado no provider anthropic.)

## Observações técnicas
- O catálogo embutido do app (`/opt/ZCode/resources/model-providers/models_catalog_china_llm_zcode_2026-06-03.json`) lista DeepSeek com `baseURL https://api.deepseek.com`, paths `anthropic:/anthropic/v1/messages` e `openai-compatible:/chat/completions`, defaultKind `anthropic` — usado como referência.
- O Vision ficou em provider `openai-compatible` separado porque o formato de imagem provado (missão das capas) é o `chat/completions`.
- Não se criou/alterou chave nova (Regra 4 ok): reutilizada a `DEEPSEEK_API_KEY` já espelhada nos cofres.

## Pendência
- Nenhuma técnica. Se o seletor do app não listar na hora, reiniciar o ZCode. Se "JPSC" não for DeepSeek, aguardando Miguel passar o provedor/endpoint/chave corretos.
