# Memória — GLM PRÉ-PAGO: chave nova testada, ZCode configurado, cofres espelhados (19/09/2026)

**Quem:** ZCode/Kimi K3 · **Fórum gêmeo:** Foruns/forum_glm_prepago_config_zcode_20260919.md · **Monitor:** ZM-GLM-PREPAGO-20260919

## Log técnico completo

### Contexto

Miguel migrou a Z.ai de assinatura (Coding Plan Max, US$ 144/mês — EXPIROU) para **pré-pago** (saldo em conta) e gerou chave nova. Pedido: testar + configurar no ZCode.

### Chave nova (NUNCA expor valor — sha8 `d0f53631`, len 49, formato `<hex32>.<alnum16>`)

Depositada em (todos com backup `.bak_pre_glm_prepago_20260919_1547/1548`):

| Onde | Arquivo | Variável |
|---|---|---|
| Dell | `Projeto Cafezinho Agentes/root/.env.unificado` | `ZAI_PREPAGO_API_KEY` + `ZAI_PREPAGO_BASE_URL` |
| Dell | `Outros/chaves/agentes_labs/.env.unificado` | idem |
| Tencent | `/root/.env.unificado` | idem |
| Tencent | `/root/.env` | `ZAI_API_KEY`/`GLM_API_KEY` = nova; `ZAI_BASE_URL`/`GLM_BASE_URL` = `/api/paas/v4` |
| Tencent | `/home/ubuntu/cafezinho/redes/.env_redes` | `ZAI_API_KEY` = nova; `ZAI_BASE_URL` = `/api/paas/v4` |
| ZCode | `~/.zcode/v2/config.json` | provider `e488030c` options.apiKey |

### Provas (19/09, curl)

1. `POST https://api.z.ai/api/paas/v4/chat/completions` c/ chave nova: **200** em `glm-4.5-flash`, `glm-4.6`, `glm-5.3` (Dell) e `glm-5.3-flash` (Tencent via .env_redes)
2. `POST https://api.z.ai/api/anthropic/v1/messages` c/ chave nova: **429/1309** "GLM Coding Plan package has expired" → endpoint Anthropic é só da assinatura
3. Chaves antigas (builtin:zai, builtin:zai-coding-plan, ZAI_API_KEY/GLM_API_KEY 4d8ae2...): **401 Authentication Failed** → deprecadas `_DEPRECADA_20260919` nos cofres de referência (Dell ×2 + tencent unificado)

### Config ZCode aplicada

- `provider["e488030c-d773-4049-9aa9-dd06950f94c7"]` → name "Z.ai API — PRÉ-PAGO", baseURL `https://api.z.ai/api/paas/v4`, models GLM-5.3 (ctx 1M/out 128k), GLM-4.6 (200k/128k), GLM-4.5-Flash (128k/16k) — estrutura copiada do builtin:zai (reasoning variants low/max/high, default max)
- `builtin:zai` e `builtin:zai-coding-plan` → `enabled:false` (chaves mortas preservadas no arquivo)
- JSON validado após escrita

### Lições / receitas

- **Pré-pago Z.ai = SÓ OpenAI-compatible `/api/paas/v4`**; Anthropic-native `/api/anthropic` exige Coding Plan ativo (1309)
- glm-5.3 existe e funciona no pré-pago (não é exclusivo da assinatura)
- `.env_redes` do tencent tinha base URL `/api/coding/paas/v4` (endpoint do plano) — trocada junto com a chave, senão chave viva + endpoint morto = continua quebrado
- Script de rotação remota: escrever local (`/tmp/fix_glm_prepago.py`) + scp + `sudo python3` — heredoc python via ssh quebra
- Esteira de fios: perna ZAI da curadoria revivida (estava suspensa desde a expiração do plano)

### Pendências

- Vigília de crédito (`~/.zcode/hooks/credito_vigilia.py`) lia quota do coding plan — sem endpoint de quota no pré-pago conhecido; adaptar quando houver
- Se Miguel renovar a assinatura: reativar `builtin:zai*` (enabled:true) e reaproveitar endpoint Anthropic
