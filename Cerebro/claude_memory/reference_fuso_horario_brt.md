---
name: fuso-horario-brt
description: "Fuso do workspace é BRT (America/Sao_Paulo, UTC-3). Miguel está em Brasil. Logs do NYC vêm em UTC (somar -3 p/ BRT). WP mostra datas em BRT (timezone configurada). SQLite banco NYC grava em UTC."
metadata: 
  node_type: memory
  type: reference
  author: glm
  written_at: 2026-07-17
  originSessionId: 48912c77-8e3a-4cfa-80ef-44561d329133
---

⚠️ **MEMÓRIA DO GLM/MING** — Diretório `~/.claude/projects/.../memory/` é compartilhado entre todos agentes CLI do workspace (Claude Code puro, GLM via wrapper, futuros Codex/Kimi). Se você é outra sessão, saiba que esta memória é do GLM/Ming.

# Fuso horário do workspace = BRT (UTC-3, America/Sao_Paulo)

**Regra:** Horário de referência em todas as comunicações com Miguel é **BRT (Brasília Time, UTC-3)**. Miguel está no Brasil.

**Why:** Miguel 17/07/2026 10:12 BRT: "escuta, ajuste o seu relógio, horário aqui do brasil. são 10:12 am 17 jul de 2026. e bote esse relogio e fuso na sua memoria". Eu estava tratando timestamps UTC do NYC como se fossem BRT, dando horários errados nas tabelas (mostrava "12:27 coleta" quando na verdade era 09:27 BRT).

**How to apply:**
- Servidor NYC (198.199.121.136) roda em **UTC**. Logs `/root/agent_data/*.log` são UTC. Banco SQLite `/root/agent_data/*.db` grava `datetime("now")` em UTC.
- Para reportar horário ao Miguel: **converter UTC → BRT subtraindo 3 horas**. Ex: log mostra `12:27:13` → reportar como `09:27 BRT`.
- WordPress `post_date` no `cafezinho-wp` já vem em BRT (Timezone WP = America/Sao_Paulo). Mostra direto sem converter.
- Servidor Tencent (43.156.151.165) — silenciado, mas também UTC.
- Quando algo relativo a "hoje", "últimas 24h", "1h atrás" — sempre em BRT.
- Datas podem aparecer com sufixo `-03:00` em JSON ou ISO — ignorar o offset, é só BRT confirmado.
- Pra checar horário atual num console: `date -u` (UTC) ou `TZ=America/Sao_Paulo date` (BRT).
-巴西 não tem horário de verão desde 2019, então UTC-3 é fixo o ano todo.

**Irmãs:** [[reference-wrapper-glm-exclusivo-20260717]], [[feedback-ponto-retomada-checkpoints]]
