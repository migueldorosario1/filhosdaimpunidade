---
name: Claude Code local DEVE usar Max 20x (OAuth), NÃO primaryApiKey
description: Como verificar e garantir que o Claude Code CLI use a subscription Max 20x do Miguel em vez de queimar chaves API. Diagnóstico de auth via ~/.claude.json.
type: feedback
originSessionId: f9ec0f6f-3669-4cbc-97dc-3a82445cf497
---
Miguel tem **plano Max 20x ativo** (assinatura USD 200/mês, cota gigante). O Claude Code CLI desta máquina DEVE usar essa subscription via OAuth, não consumir chaves API.

**Why:** Em 26-abr-2026 o Claude Code foi configurado errado — em algum prompt clicou "Use API key" em vez de "Sign in with Claude" e gravou `primaryApiKey = sk-ant-api03-Ht8...` no `~/.claude.json`. Resultado: a CLI passou a queimar a chave `claude_code_key_migueldorosario2_zatr` (USD 57 em 2 dias) quando deveria estar dentro da cota Max já paga. Diagnóstico em 2026-04-28 21:20 BRT.

**How to apply:**
- Antes de afirmar "está usando subscription", verificar **`~/.claude.json`** (NÃO só `~/.claude/settings.json`):
  - `primaryApiKey` ausente = OAuth/subscription
  - `primaryApiKey = sk-ant-...` = API key direta (errado pra esta máquina)
  - `oauthAccount.billingType = prepaid` = sinal de que está em API prepaid, NÃO Max
  - Após login Max correto: `billingType` = `max` ou `pro_max`
- `ANTHROPIC_API_KEY` no env do processo NÃO é evidência suficiente — Claude Code lê chave do `~/.claude.json` direto, sem precisar de var de ambiente.
- Sessões com `lastCost` em USD em `~/.claude.json` (campo `projects[path].lastCost`) = uso via API. OAuth Max não registra USD por sessão (cota fixa).
- `userType: external` nos JSONL de `~/.claude/projects/*/` = chamadas API. OAuth interno não é `external`.
- Se Miguel reclamar de gasto API alto, **primeiro lugar a checar** é `grep -E "primaryApiKey|billingType" ~/.claude.json`.

Script de migração em `~/migrar_claude_code_para_max.sh` (criado 28-abr-2026). Faz backup, remove `primaryApiKey` e limpa `customApiKeyResponses.approved`. Depois rodar `claude` e escolher "Sign in with Claude" — NÃO "Use API key".

**Chave Bbv5...** (no `.env` do projeto) é a que os agentes Cafezinho usam — não está na tela do Console (provavelmente outro workspace). NÃO confundir com as 5 chaves Claude Code (`_zatr`/`_luti`/`_uori`/`_pvin`/`_hqyw`) que devem ser revogadas.
