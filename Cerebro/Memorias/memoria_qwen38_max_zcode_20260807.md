# Memória — Qwen 3.8 Max no ZCode (fix 401/403) — 2026-08-07 ~00:40 BRT

**Sessão:** ZCode (Kimi K3), chat direto, workspace ZCodeProject
**Fórum irmão:** `Foruns/forum_qwen38_max_zcode_20260807.md`

## Sintoma

Provider "Qwen 3.8 Max" (`1b950583-9598-4848-a561-a2f26e4d3b8c`) no ZCode falhava:
`401 invalid_api_key — provider_code=invalid_api_key model=qwen-max-latest reason=auth_failed`.

## Diagnóstico (testes com curl, sem expor segredos)

| Teste | Resultado |
|---|---|
| Chave do provider ZCode (sha8 `820805fa`) | 401 invalid_api_key — **chave errada/morta** (não é a canônica) |
| Chave canônica cofre (sha8 `85ecbfc0`) + `qwen-max-latest` no MaaS workspace | **403 access_denied** — modelo não existe no workspace |
| Chave canônica + `GET /models` no MaaS workspace | 200 — lista viva obtida; **`qwen3.8-max` existe**; `qwen-max-latest` **ausente** |
| Chave canônica + `qwen3.8-max` chat | **200 OK** (com `reasoning_content` — modelo com reasoning) |
| Chave canônica + tool-calling (`tools`/`tool_choice`) | 200, `finish_reason=tool_calls`, formato function-call correto |
| Chave canônica + streaming SSE | 200, chunks SSE normais |
| Chave canônica + `dashscope-intl.aliyuncs.com/compatible-mode/v1` + `qwen-max` | **200 OK** — endpoint público funciona como fallback |

Fontes da chave canônica (ambas sha8 `85ecbfc0`, len 116, `sk-ws-...`):
- `Projeto Cafezinho Agentes/root/.env.unificado`
- `Outros/chaves/agentes_labs/.env.unificado`

## Fix aplicado

Arquivo: `~/.zcode/v2/config.json` (backup `config.json.bak_pre_qwen38_fix_20260807`)
- `provider.1b950583.options.apiKey` ← chave canônica `85ecbfc0` (via script, valor nunca impresso)
- `models`: `qwen-max-latest` → **`qwen3.8-max`** (context 200K mantido, estrutura do entry preservada)
- baseURL inalterado: `https://ws-x4x2zxwucryw1pr6.ap-southeast-1.maas.aliyuncs.com/compatible-mode/v1`
- Chave também deixada no clipboard (xclip) para o Miguel colar na UI se o app sobrescrever o JSON ao fechar.

## Lições

1. **401 ≠ 403:** 401 = chave errada; 403 no workspace MaaS = chave ok mas modelo/ação negada. O par de erros aqui contava a história inteira.
2. **IDs `-latest` nem sempre existem no endpoint de workspace** — conferir com `GET /models` antes de cadastrar provider.
3. **`qwen3.8-max` é o novo topo Qwen** (07/08/2026) e tem reasoning — para pipelines Cafezinho, medir custo/latência do reasoning antes de adotar (caso-escola: `qwen3.7-max` = 34,5s, "não usar").
4. Endpoint público `dashscope-intl` aceita a mesma chave de workspace — fallback válido em emergência.
