---
name: controle.ocafezinho.com lento — Server Doin (provedor do Miguel)
description: Backend admin WP (IP 190.89.239.65) com TTFB até 3.96s e picos acima de 30s. Dados técnicos coletados, texto pronto pra reclamação com Server Doin.
type: project
originSessionId: 47c65b42-a2a7-4314-a9db-56d574d902d2
---
**IP:** 190.89.239.65 (Server Doin — provedor do Miguel, contrato ativo)

**Papel crítico:** `controle.ocafezinho.com` é o endpoint REAL do WordPress (admin + REST API). Usado por:
- `agente_observador.py:10` (V3) — lista posts pra auditar
- `motor_publicador.py:33` — publica matérias
- Link público é reescrito `controle → www.ocafezinho.com` em `motor_publicador.py:1186`

**Sintoma:** quando backend satura, V3 trava com `Pane WP: Read timed out`. Timeout antigo 30s (elevado pra 60s como mitigação em 2026-04-19 08:38).

**Diagnóstico coletado 2026-04-19 08:47-08:51 BRT (15 amostras):**
- TTFB: 0.67s a **3.96s** (variação 6×)
- 26.6% das amostras com TTFB > 1.5s
- Total médio: 4.08s vs 0.91s no frontend `ocafezinho.com` (~4.5× mais lento)
- Endpoint V3 `/wp-json/wp/v2/posts`: 3.81s total, 1.61s TTFB, 264KB
- Ping: 219ms 0% perda (rede OK — problema é backend PHP/MySQL)
- Server header: `nginx` (versão escondida)

**Hipóteses:** shared hosting com vizinhos barulhentos, PHP-FPM saturado, MySQL slow queries, disputa de recursos. **Rede e DNS descartados.**

**Texto pronto pra reclamação:** entregue ao Miguel em chat 2026-04-19. Formal, técnico, dados mensuráveis, pede diagnóstico de CPU/RAM/IO/slow-query ou upgrade de plano. Miguel ainda não mandou (aguardando decisão dele).

**Mitigação corrente:** timeout V3 60s. Funciona na prática — sem nova pane desde 08:30.

**NÃO fazer:** V3 ler via `ocafezinho.com/wp-json` (frontend cacheado). Perde `?context=edit` e reintroduz bug do ciclo fantasma (`&#038;`). Deal-breaker.
