---
name: reference-ponto-de-retomada-canonico
description: "Diretório canônico de Ponto de Retomada para snapshots de sessão do Claude Code, regras, cadência declarada e lista negra de segredos."
metadata: 
  node_type: memory
  type: reference
  originSessionId: c6c1efc3-9035-46e2-a05f-6b3f83fe0ea4
---

# Ponto de Retomada — Diretório Canônico de Snapshots

**Regra permanente Miguel 2026-06-28.** Substitui qualquer convenção anterior de gravação de "memória de trabalho" fora da auto-memória `.claude/projects/.../memory/`.

## Caminhos

- **Raiz canônica:** `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/Ponto de Retomada/`
- **Meu subdiretório (Claude Code):** `Ponto de Retomada/Claude Code/`
- **Outros agentes (não usar):** `AGY CLD`, `Antigravity Desktop`, `Codex`, `DeepSeek TUI`, `GLM Coding`, `Grok Build`, `Kilo`, `Kimi Code` — cada um tem seu silo, NÃO escrever nos outros.
- **Arquivos de governança da pasta raiz:**
  - `README.md` — regras gerais (Miguel + Codex)
  - `PEDIDO_AOS_AGENTES_20260628.md` — pedido formal datado
- **Meus arquivos fixos:**
  - `Claude Code/INSTRUCAO_RETOMADA.md` — instrução base (já existia)
  - `Claude Code/CADENCIA.md` — cadência que eu declarei (criado 2026-06-28 10:44)

## Cadência declarada (resumo do meu `CADENCIA.md`)

Gravo snapshot quando QUALQUER uma destas condições se atinge primeiro:

1. **10 turnos relevantes** do Miguel desde último snapshot (pedido novo / decisão / mudança de rumo — NÃO conta "ok"/"vai"/"continue").
2. **30 minutos** desde último snapshot, se houve atividade no período.
3. **Etapa importante concluída** (deploy efetivado, decisão estratégica, fim de sprint, bloqueio crítico, sessão prestes a encerrar).
4. **Pedido explícito** ("gravar a sessão", "salvar sessão", "checkpoint", "ponto de retomada", "snapshot", "grava aí") — instantâneo.

## Formato do snapshot

- Nome: `YYYYMMDD_HHMMSS_sessao.md` (timestamp BRT).
- Conteúdo obrigatório (sem segredos jamais):
  1. Cabeçalho (data/hora BRT, modelo, tipo do snapshot)
  2. Objetivo atual
  3. Contexto já lido (arquivos, MEMORY.md consultadas, URLs)
  4. Arquivos alterados (paths absolutos + 1 linha cada)
  5. Comandos importantes executados
  6. Decisões tomadas
  7. Pendências
  8. Bloqueios
  9. Próximos passos
  10. Riscos identificados
  11. Verificações feitas (PASS/FAIL/inconclusivo)

## Lista negra — NUNCA gravar em snapshot

- Senhas / App passwords / tokens (Anthropic, OpenAI, WP `Redator`, Telegram, etc).
- Conteúdo de `.env`, `.env.unificado`, `chaves_novas.env`, `.env_bot`.
- Cookies, headers Auth, chaves SSH, conteúdo de `id_rsa*`, `id_ed25519*`.
- Strings com prefixos sensíveis: `sk-`, `Bearer `, `xai-`, `pplx-`, `gsk_`, `xoxb-`, `ghp_`, etc.
- Senha sudo do `ubuntu@` Tencent, mesmo que apareça em log meu.

Quando precisar referenciar segredo, escrever apenas o nome lógico ("usei `ANTHROPIC_API_KEY` do `.env.unificado`"), **nunca** o valor.

## Disciplina ao iniciar sessão nova

Toda sessão Claude Code nova DEVE:

1. Executar `ls -lt "/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/Ponto de Retomada/Claude Code/"` no início.
2. Ler o snapshot mais recente.
3. Se Miguel der instrução genérica ("continue", "vai", "retoma"), o snapshot mais recente é o contexto base.
4. Se já se passaram horas/dias desde último snapshot, ainda assim ler — é o ponto de partida menos enviesado que existe.

## Política de retenção

- **Manter todos** os snapshots. Miguel limpa se quiser.
- Cada snapshot é **autocontido** — não vira diff acumulativo, não vira índice.
- Não criar pasta de "antigos" ou "arquivados" — mantém tudo na raiz do `Claude Code/`.

## Diferença vs. auto-memória `.claude/projects/.../memory/`

| Aspecto | Auto-memória (`memory/`) | Snapshots (`Ponto de Retomada/Claude Code/`) |
|---|---|---|
| **Escopo temporal** | Cross-sessão, perene (fatos/decisões/regras que valem sempre) | Sessão específica, ponto-no-tempo (estado operacional momentâneo) |
| **Conteúdo** | "Quem é o Miguel", "qual a regra de título", "qual o servidor real" | "O que eu fiz hoje 14:30", "que arquivos toquei", "o que faltava fazer às 15:00" |
| **Discoverability** | `MEMORY.md` carregado automaticamente em toda sessão | Só carregado se eu explicitamente `ls` + `Read` no início |
| **Quem mantém** | Eu (Claude Code) escrevendo `feedback_*`, `project_*`, `user_*`, `reference_*` | Eu, sob gatilho de cadência ou pedido |
| **Conflito?** | NÃO. São complementares. Snapshot pode citar memória `[[name]]`. | NÃO. Memória pode mencionar diretório como referência. |

## Histórico

- **2026-06-28** — Regra criada por Miguel via instrução textual permanente. Diretório `Ponto de Retomada/` já existia, criado por Codex em data anterior, com 9 subdirs prontos. Eu (Claude Code) criei `CADENCIA.md` e primeiro snapshot `20260628_104425_sessao.md`. Esta memória cataloga a regra para sessões futuras.
