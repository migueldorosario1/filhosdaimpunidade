# Fórum — Qwen 3.8 Max configurado no ZCode (fix 401/403) — 2026-08-07 ~00:40 BRT

**Sessão:** ZCode (Kimi K3), chat direto, workspace ZCodeProject
**Pedido do Miguel:** "me ajuda a configurar aqui no ZCode o QWEN, tá dando erro" — provider "Qwen 3.8 Max" com 401 `invalid_api_key`.

## Decisões resumidas

1. **Causa dupla do erro:** (a) a chave gravada no provider do ZCode (sha8 `820805fa`) é **inválida** — não era a canônica do cofre; (b) o modelo `qwen-max-latest` **não existe no workspace MaaS** (403 access_denied) — ID defasado.
2. **Chave correta aplicada:** canônica `QWEN_API_KEY` sha8 `85ecbfc0` ("chave-site-ocafezinho", conta migueldorosario2), lida do cofre local e gravada direto no `~/.zcode/v2/config.json` (backup `.bak_pre_qwen38_fix_20260807`) — **sem expor valor em chat**.
3. **Modelo certo:** `qwen3.8-max` — confirmado na listagem viva do workspace e testado com HTTP 200 (chat, tool-calling e streaming SSE). É um modelo **com reasoning** (retorna `reasoning_content`).
4. **Descoberta útil:** a chave canônica também responde 200 no endpoint público `dashscope-intl.aliyuncs.com/compatible-mode/v1` (testado com `qwen-max`) — alternativa de emergência se o endpoint MaaS do workspace cair.
5. **Modelos disponíveis no workspace hoje:** topo = `qwen3.8-max`; também `qwen3.7-max(-preview)`, `qwen3.6-max-preview`, `glm-5.2`, `deepseek-v4-pro`, `kimi-k2.7-code`, `qvq-max`, família `qwen3.5-*`. `qwen-max-latest` **NÃO** está na lista — não usar esse ID.

**Log técnico completo:** `Memorias/memoria_qwen38_max_zcode_20260807.md`
