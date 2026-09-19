---
name: feedback-settings-json-reseta-env-apos-wrapper
description: "Bloco `env` em ~/.claude/settings.json global re-seta env vars APÓS wrapper fazer unset+exec — auditar sempre esse arquivo ao diagnosticar env vars persistentes"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 141bed6a-4940-4b62-9bb0-9f852e87cb66
---

🔧 **`~/.claude/settings.json` (global user-level) tem bloco `env` que Claude Code aplica APÓS o `exec` do wrapper de shell.** Isso significa que `unset` feito em wrapper bash (`~/bin/claude` ou similar) é sobrescrito microssegundos depois pelo próprio processo Claude Code quando lê o settings.json e chama `os.environ.update(env)` (ou equivalente) no bootstrap. Nenhum `unset` prévio protege contra config declarativa que reseta env no startup.

**Why:** Caso fundador 27/07/2026 16:27 BRT — bug env vars GLM (`ANTHROPIC_DEFAULT_(HAIKU|SONNET|OPUS)_MODEL=glm-*`) persistiu por 2+ dias mesmo após 3 tentativas de fix: (1) 26/07 16:20 bashrc PATH pra ordem correta `~/bin` antes `~/.local/bin`, (2) 27/07 05:35 wrapper `~/bin/claude` fazer `unset ANTHROPIC_DEFAULT_*` antes do `exec`, (3) wrapper mover `.claude/settings.local.json` do PROJETO se detectar padrão GLM. Nenhum dos três tocava o `~/.claude/settings.json` GLOBAL — que era a fonte real. Fix real: remover chaves GLM do bloco `env` no arquivo global (preservar chaves não-GLM tipo `API_TIMEOUT_MS`, `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC`).

**How to apply:** Quando diagnosticar env var contaminante persistente em Claude Code (ou qualquer app com config declarativa): auditar TRÊS camadas antes de mexer em shell/wrapper — (a) `~/.claude/settings.json` GLOBAL, (b) `.claude/settings.local.json` PROJETO, (c) `.claude/settings.json` PROJETO. Grep `grep -rE "VAR_NAME" ~/.claude/ .claude/ 2>/dev/null`. Só depois auditar bashrc/profile/wrapper. Bandeira vermelha genérica: "wrapper faz unset mas env var reaparece" = quase sempre config declarativa do app re-setando após exec, NÃO é bug de shell. Vale pro Kimi CLI (`~/.kimi-code/`), Antigravity, qualquer app que leia settings JSON no bootstrap. Sessão atual NUNCA descontamina (env herdada do processo pai) — precisa restart limpo pra validar. Registro completo em [[bug-env-glm-vazando-settings-global-20260727]] no `CEREBRO_NODE_BUGS_RESOLVIDOS.md`. Regra irmã: [[feedback_autocura_protocolo_registro_com_solucao_e_rollback]] (backup pré-patch com SHA-256 obrigatório).
