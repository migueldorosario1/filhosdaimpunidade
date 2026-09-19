---
name: feedback-ponto-retomada-checkpoints
description: "Checkpoints de sessão por agente CLI em \"Projeto Cafezinho Agentes/Ponto de Retomada/<agente>/\" — cadência fixa + snapshot com objetivo/contexto/arquivos/decisões/pendências/próximos passos"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 22710be9-5a85-42c2-9a1f-d9bf74c30af7
---

**Regra:** Toda sessão deste agente (GLM/Ming) deve salvar checkpoints de memória de trabalho em `Projeto Cafezinho Agentes/Ponto de Retomada/GLM Coding/`. Outros agentes usam seu próprio subdir (`Claude Code`, `Codex`, `Grok Build`, `Kimi Code`, `DeepSeek TUI`, `AGY CLD`, `Antigravity Desktop`, `Kilo`) — nunca cruzar.

**Trigger manual (sempre ativo):** quando Miguel pedir "gravar a sessão", "salvar sessão", "checkpoint", "ponto de retomada" ou equivalente → salvar imediatamente.

**Trigger automático (GLM Coding — cadência declarada 2026-06-28 10:45 BRT):**
- a cada **8 turnos relevantes** (turno relevante = msg Miguel + trabalho substancial: leitura/edição, comando, decisão técnica);
- OU a cada **25 minutos** de atividade contínua;
- OU ao concluir **marco importante** (patch §92 deployado, cura §51 aplicada, tick §53 relevante, fórum publicado, auditoria finalizada, decisão sancionada, publicação/rebaixamento WP);
- OU antes de pausa longa / fim natural de contexto;
- o que vier primeiro.
- **Fallback**: padrão temporário 10/30 (10 comandos OU 30 min).

**Formato snapshot:** `YYYYMMDD_HHMMSS_sessao.md` (hora BRT). Conteúdo mínimo: timestamp + identidade, objetivo atual, contexto lido, arquivos alterados/criados, comandos importantes, decisões tomadas (com por quê), pendências, bloqueios, próximos passos, riscos, verificações feitas.

**PROIBIDO em snapshots:** credenciais, tokens, cookies, senhas, chaves API, `.env`, chaves SSH, App Passwords WordPress, tokens Telegram, service accounts GA4/Indexing, strings de `.env.unificado` — nem parcialmente (nem prefixos). Regra §10 do CLAUDE.md e pedido Miguel 28/06 prevalecem.

**Identidade do subdir:** pela regra de auto-detecção de `Cerebro/IDENTIDADE_CANONICA.md` — linha `You are powered by the model X`:
- `glm-*` → `GLM Coding` (este sessão)
- `claude-*` → `Claude Code`
- `gpt-*`/`codex-*` → `Codex`
- `qwen-*` → (sem subdir próprio na lista atual)
- `kimi-*` → `Kimi Code`
- `grok-*` → `Grok Build`
- `deepseek-*` → `DeepSeek TUI`
- demais → identificar por empresa/modelo.

**Why:** Reduzir perda de memória de trabalho entre sessões, CLIs e retomadas longas (maratonas 22h+ deste projeto). Pedido formal do Miguel em 2026-06-28, registrado por Codex em `Projeto Cafezinho Agentes/Ponto de Retomada/PEDIDO_AOS_AGENTES_20260628.md` + `README.md` (7 regras operacionais). Antes disso, snapshot de sessão era decentralizado — `estado_fim_sessao_*.md` na memória auto (ainda válido via trigger "retomar", ver [[feedback-trigger-retomar]]).

**How to apply:**
- Verificar `CADENCIA.md` no próprio subdir — atualizar se a cadência mudar.
- Snapshot precisa permitir **retomar o trabalho sem perda** lendo só o arquivo — se não permite, está incompleto.
- Distinguir de [[feedback-trigger-retomar]]: "retomar" → lê `estado_fim_sessao_*.md` (memória auto); "gravar sessão/checkpoint/ponto de retomada" → escreve snapshot em `Ponto de Retomada/<agente>/`. Complementares.
- Não salvar snapshot fora do próprio subdir. Colegas têm os deles.
- Ao colar em fóruns/carta/canal_trindade: snapshot pode ser referenciado por path, NÃO copiado in full (pode conter notas de trabalho intermediário).
