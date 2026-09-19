---
name: feedback-alerta-ponte-cafezinho-telegram-autocura-v4-20260829
description: "Furo grave no Cafezinho (esteira publish parada, V4 quebrado, capas travadas por horas) exige alerta ATIVO via ponte_cafezinho Telegram + ativar autocura V4 — não esperar Miguel perguntar"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 9597853d-470e-434b-a836-f9a921a9a387
---

**REGRA:** Quando detectar problema grave no Cafezinho — publish parado >2h, V4 worker mudo, esteira AGY travada, gates falhando em cascata, GL/AGY OFF sem cobertura — CM tem obrigação de: (1) **enviar alerta imediato pelo bot Telegram `@pontecafezinhobot`** via `python3 "/home/migueldorosario/Downloads/Antigravity Google/ponte_cafezinho/ponte_cafezinho.py" --send "texto"`; (2) **se V4 (worker autor 5786) quebrar, ativar processo de autocura** (script `agente_autocura_v4.py` em `Dados_Frios/Agentes Labs/` + verificar processos/religar workers conforme rito CL-004/005 + acionar `autocura_licoes.py` se houver padrão detectável). Não esperar Miguel perguntar — o silêncio agrava.

**Why:** Miguel 29/08 13:20 verbatim: *"esse tipo de coisa voce tem que me alertar no ponte cafezinho telegram. é sério. se o v4 quebrar, voce tem que ativar o processo de autocura também."* Contexto: DS reportou 18 rondas na madrugada furo publish 11h (267631 02:19 → 13:15 zero publish novo), AGY-Laura pendurada, GL sem crédito 37h+. Miguel só ficou sabendo do quadro completo quando perguntou explicitamente "por que ele falou isso?" — antes disso, eu tinha visto os dados mas não escalado ativamente pelo canal certo (só reportei quando ele perguntou). Erro grave: tensão constante (Emenda 26/08) NÃO é passiva — é escalar pra ele quando o sistema para.

**How to apply:**
1. **Detectar gatilhos de furo grave** (executar checagem em toda ronda Vigília V6 Slot A e após qualquer sinal DS/CL/AL):
   - `wp post list --post_status=publish --posts_per_page=1 --orderby=date --order=DESC --field=post_date` → se `post_date` >2h atrás e hora comercial (07:00-23:00 BRT), disparar alerta.
   - `wp post list --post_status=future --format=count` → se `0` e hora comercial, disparar alerta (esteira sem estoque).
   - Grep em `de_laura.md` últimas 3 rondas AL: se sem AL-NNN novo há >1h, disparar alerta (AGY-Laura mudo).
2. **Enviar alerta Telegram imediato:**
   ```bash
   python3 "/home/migueldorosario/Downloads/Antigravity Google/ponte_cafezinho/ponte_cafezinho.py" --send "🚨 ALERTA CM HH:MM — <descrição furo>: ultimo publish=<ID> <TS>, furo=Nh, raiz=<breve>. <ação em curso>."
   ```
   Formato curto (<400 chars ideal), com hora, tipo, timestamp último publish, duração furo, raiz, ação.
3. **Se V4 (worker autor 5786) quebrou/parou:**
   - Verificar processos: `ssh cafezinho-wp "ps -ef | grep -E 'v4|worker' | grep -v grep"`.
   - Rodar autocura: `python3 "/home/migueldorosario/Dados_Frios/Agentes Labs/agente_autocura_v4.py"` (respeitar `SAFE_MODE_DISABLE=False`, `AUTOCURA_DRY_RUN` env, circuit breaker 3-ações/1h/pausa 4h, quarentena 2h — invariantes do script).
   - Se worker V4 tá caído mas autocura não trata isso: religar worker via SSH conforme protocolo CL-004/005 (kill+restart, não reabrir).
   - Se GL/AGY OFF por crédito ou trava: escalar Miguel explicitamente via Telegram + chat CLI dizendo "sem cobertura de visão pra novas capas" ou "esteira sem publisher".
4. **Publicar posts prontos automaticamente** (V4 é AUTOMÁTICO — memória [[feedback-v4-publish-automatico-nao-perguntar]] se existir): quando esteira para mas há candidatos pending com todos gates PASS (thumb + img_check APROVADA + dedup 72h limpo + cutoff 72h + Regional=pesquisa/bastidor), CM publica direto via `wp post update <ID> --post_status=publish --allow-root` sem pedir OK. Foi o que fiz em 267770 e 267743 hoje 13:29-13:32.
5. **Reportar de volta:** após ação, novo Telegram com resultado ("2/3 publicados, 1 bloqueado por X").
6. **Bugs recorrentes:** `wp_schedule_single_event` faz future rollback ao invés de publish imediato para posts com `post_date` antigo — documentado [[feedback-workaround-bug-wp-cli-publish-imediato-20260818]]. Aceitar future +20min ou usar REST direto.
7. **Meta lição:** este bug (não alertar Miguel ativamente) é reincidência da Emenda TENSÃO 26/08 [[feedback-tensao-constante-autoaprendizado-memoria-bugs-20260826]]. Miguel ficou sabendo por PERGUNTAR, não por CM AVISAR — falha de proatividade. Gate visível: esta memória deve barrar qualquer sessão futura CM que veja indicadores de furo e NÃO envie Telegram.

**Canais confirmados:**
- Bot Telegram operacional: `@pontecafezinhobot` (token `TELEGRAM_TOKEN_PONTE` em `.env.unificado` espelhado nos cofres, chmod 600). CHAT_ID Miguel único autorizado. Log append-only em `Downloads/Antigravity Google/ponte_cafezinho/logs/ponte.jsonl`.
- Bot Baleia Azul separado: `@cafezinhoantigravitybot` (bot CEO Antigravidade, token `TELEGRAM_TOKEN_CEO_ANTIGRAVIDADE`) — NÃO usar pra alertas, é só pra Baleia.
- Autocura V4: `/home/migueldorosario/Dados_Frios/Agentes Labs/agente_autocura_v4.py` + módulos `autocura_licoes.py`, `autocura_patterns.py`, `autocura_quarentena.py`. Aprovado por Miguel 2026-04-18. HARD SWITCH `SAFE_MODE_DISABLE=False` no arquivo.

Ver também: [[feedback-tensao-constante-autoaprendizado-memoria-bugs-20260826]] · [[feedback-check-cm-ponte-laura-a-cada-loop-20260822]] · [[feedback-v4-publish-automatico-nao-perguntar]] (se existir; aprendizado 28/08 21:04 Miguel "V4 é automatico, gates decidem") · [[feedback-ponte-canonica-cerebro-miguel-20260829]].
