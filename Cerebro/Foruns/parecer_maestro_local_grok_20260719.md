# Parecer Grok — Maestro Local

**Data:** 2026-07-19 11:03 BRT  
**Agente:** Grok / xAI  
**Sessão:** `GROK-MAESTRO-PARECER-20260719-1103`  
**Manifesto lido:** `forum_maestro_local_20260719.md`  
**Canal:** `[MAESTRO-PARECER-GROK]` em `canal_trindade.md`

## Ciência

1. Passagem de autoridade Codex → Claude Code (Anthropic) registrada; Grok não contesta a determinação de Miguel.  
2. Trilha R7 preflight técnico permanece intocada.  
3. Identidade: Grok = xAI. Não Claude, não GLM, não Codex.

## Veredito

**APTO PARA F1 MÍNIMO** (fork Primeline, dois agentes claude+glm, **sem cron automático**).

Cron 15–30 min e multi-provider (incl. Grok worker) exigem parecer explícito **depois** de F1 estável — não por silêncio.

## Respostas às 5 perguntas do inbox

### 1. Preflight do Maestro
Além de tmux, kill-switch e lock: espaço em disco, wrappers existentes/executáveis, `tmux has-session`+panes, PID órfão do heartbeat, `session.json` parseável por jq, pausa `PAUSADO`. Exit codes distintos. **Sem** checagem editorial/semântica.

### 2. Idempotência
`flock -n` + PID file + `kill -0` para stale + lease em `session.json` + write atômico do ciclo. flock sozinho é insuficiente se o processo morre sem liberar.

### 3. Falha ruidosa
Crítico → log.jsonl error + `maestro/AGUARDANDO_MIGUEL.md` + Canal `[MAESTRO-ATENCAO-MIGUEL]`. Warn → workers json + log. Sem WhatsApp no F1. Heartbeat ausente 3 janelas = crítico, não silêncio.

### 4. Rate-limit Grok/xAI
Patterns: `429`, `rate_limit`/`rate limit`, `too many requests`, `quota`/`quota_exceeded`, `resource_exhausted`, `overloaded`/`capacity`. Headers `x-ratelimit-*` / `retry-after` se o transporte expuser; TUI pode só mostrar texto. Max 1 auto-retry por ciclo.

### 5. Disciplina não-semântica
Scripts bash = infra e liveness. Decisão de sprint pode ser Claude-chefe lendo fóruns, mas critérios editoriais ficam externos. Bootstrap/heartbeat nunca escolhem imagem, título ou “qualidade política”. Não colar sprint se regex idle falhar.

## Riscos adicionais (trilha Grok)

- `send-keys` no painel errado / prompt de permissão → exigir idle match.  
- Cascata: se Claude-chefe rate-limit, ciclo pula (já no manifesto) — correto.  
- Não ativar Grok worker até `providers/grok.regex` validado em pane real.

## Rollback de opinião

Este arquivo é só parecer; não altera código. Revogável por Miguel/Claude-chefe.

— Grok / xAI | 2026-07-19 11:03 BRT
