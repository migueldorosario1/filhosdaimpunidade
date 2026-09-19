---
name: wrapper-glm-exclusivo
description: "Comando terminal exclusivo `glm` em ~/bin — wrapper Claude Code CLI apontando pra Z.ai/glm-5.2 com auto-preload de snapshot + fóruns + lembretes vencidos"
metadata: 
  node_type: memory
  type: reference
  originSessionId: ff302e2b-ddd7-460c-9ae1-9c5facf683e9
---

> ⚠️ **Autoria:** Esta memória foi escrita por **GLM/Ming** (model ID `glm-*` conforme `Cerebro/IDENTIDADE_CANONICA.md` L26). O diretório `~/.claude/projects/.../memory/` é compartilhado entre agentes CLI que operam neste workspace, MAS o conteúdo aqui reflete perspectiva e contexto de quem assina. Sessões Claude Code puras (sem wrapper `glm`) que lerem este arquivo devem tratar as referências e decisões como **do contexto GLM/Ming**, não suas.

Existe wrapper bash exclusivo GLM/Ming em `/home/migueldorosario/bin/glm` (chmod +x, no PATH via `~/bin`). Diferencial vs `claude-glm.sh` legado: (1) auto-preload de contexto antes de iniciar sessão — snapshot mais recente em `Projeto Cafezinho Agentes/Ponto de Retomada/GLM Coding/`, últimos 5 fóruns em `Cerebro/Foruns/` (mtime -7 dias), lembretes vencidos/até hoje de `Cerebro/CEREBRO_NODE_AGENDA_LEMBRETES.md` via awk com filtro que pula seções `## 📜 Histórico` e linhas `✅|CONCLUÍDO`; (2) já aponta pra `glm-5.2` (sancionado 15/07/2026, modelo Zhipu AI lançado 13/06/2026 com 1M de contexto); (3) inicia sessão com prompt inicial `"retomar pelo ponto de retomada"` automático.

**Como invocar:** digitar `glm` de qualquer diretório (não precisa `./`).

**Variáveis exportadas:**
- `ANTHROPIC_BASE_URL=https://api.z.ai/api/anthropic`
- `ANTHROPIC_AUTH_TOKEN` (em `.env` do wrapper, gitignored)
- `ANTHROPIC_DEFAULT_OPUS_MODEL=glm-5.2`
- `ANTHROPIC_DEFAULT_SONNET_MODEL=glm-5-turbo`
- `ANTHROPIC_DEFAULT_HAIKU_MODEL=glm-4.5-air`

**Calibragem do awk filter (receita):** o filtro de lembretes vencidos checa 3 condições em sequência — (a) sai do loop se entrar na seção `## 📜 Histórico` (já concluídos), (b) pula linha se tiver `✅` ou `CONCLUÍDO`, (c) só imprime se a data ISO na linha for ≤ hoje.

**Por que existe:** Miguel pediu um comando seguro que não fosse confundido com `claude` (ele é GLM/Ming, só usa o wrapper Claude Code CLI pra conveniência). Antes dependia do `./claude-glm.sh` que ficava no diretório do projeto — agora `glm` é global e já carrega contexto automaticamente.

**Como aplicar:** se uma futura sessão acordar via `glm` (em vez de `claude` direto), o system prompt vai ter o model ID `glm-5.2` — auto-detecção pela regra `glm-*` → GLM/Ming continua válida. Sessões Claude Code puras (sem wrapper) ainda podem usar `claude` direto se precisarem inspecionar o workspace sem assumir identidade GLM.

**Status do legado:** `claude-glm.sh` na raiz do projeto ainda funciona mas está desatualizado (hardcoded `glm-5.1`). Atualização pendente — Miguel não decidiu se mantém os dois ou aposenta o legado.

Irmã: [[feedback-ponto-retomada-checkpoints]] (cadência de snapshots), [[ponto-de-retomada-canônico]] (diretório de snapshots por agente).

---

*— GLM/Ming (glm-5.1 via wrapper Claude Code CLI), 2026-07-17. Identidade canônica em `Cerebro/IDENTIDADE_CANONICA.md` L26.*
