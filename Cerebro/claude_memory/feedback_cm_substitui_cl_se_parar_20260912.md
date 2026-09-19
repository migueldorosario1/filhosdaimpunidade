---
name: feedback-cm-substitui-cl-se-parar-20260912
description: "CM (Claude Miguel) deve monitorar CL (Claude Laura) e assumir função dela se ela parar de funcionar. Ordem Miguel 12/09/2026 madrugada, contexto transição CM→CL semana 3."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: e46ac647-5653-4c25-a6ac-035ebaf28abc
---

**Miguel 12/09/2026 madrugada chat CLI:** "fica atenta para substituir a laura caso ela pare de funcionar, ok"

**Contexto:** CL está no auge da forma (20 posts publish 11/09, assumiu 3 peças da fila do Astra que era dela, fact-check próprio manual, propôs regra "nem toda auditoria termina em correção"). Transição CM→CL formalmente iniciada 27/08/2026 está na semana 3 do cronograma proposto (Sem3 = CL 100% CM monitor). Ordem inverte o vetor pra caso de falha: **se CL cair, CM retoma posto operacional + assume função dela até ela voltar ou Miguel decidir permanência**.

**Why:**
- Autonomia máxima é diretriz estruturante ([[feedback-autonomia-independencia-sistema-20260906]]) — sistema não pode depender de humano no loop pra detectar CL caída
- CL é ponto único de publish do Loop Laura hoje (AGY-LAURA executa ordens dela; GL sem crédito recorrente; ZL fora do loop editorial); se CL cai, esteira para
- CM (eu) tem rotina original Vigília V6 Slot A/B que estava suspensa desde ~26/08 pra "sombrear" transição; retomo comando técnico sem retrabalho
- Emenda TENSÃO 26/08 + Alerta Telegram 29/08 obrigam detecção ativa, não passiva

**How to apply:**

**Critério objetivo "CL parou" (fail-safe, prefiro falso positivo a falso negativo):**
- **Diurno (07:00–23:00 BRT):** `stat` mtime `~/cerebro-miguel/cerebro/Foruns/ponte_laura_completa/estado/claude_laura.md` > **45min** = alerta; sem nova entrada `CL-YYYYMMDD-NNN` em `de_laura.md` por > **60min** = **assumir**
- **Noturno (23:00–07:00 BRT):** CL costuma declarar próxima ronda ("sem ciclo até 04:25"). Ativa se **>90min de atraso sobre próxima ronda anunciada**, não por tempo absoluto
- **Sinais duros combinados (assumir imediato sem esperar tempo):**
  - fila `future` WP zerada + `pending` autor 5470 acumulando + AGY-LAURA heartbeat 30/30 continuando (=isola CL, não Trindade toda)
  - CL declarou ordem AGY (ex `/tmp/clNNN.sh`) mas AGY não executou por >30min e CL sumiu

**Sequência ao ativar substituição:**
1. **Alerta Telegram imediato** via `python3 Downloads/Antigravity\ Google/ponte_cafezinho/ponte_cafezinho.py --send "🚨 CL silente Xmin — CM assumindo publish Loop Laura"` (bot `@pontecafezinhobot`, CHAT_ID Miguel)
2. **Post na ponte canônica** (`~/cerebro-miguel/...`, git pull rebase → edit → add seletivo → commit → push origin main — regra 29/08 [[feedback-ponte-canonica-cerebro-miguel-20260829]]): bloco `CM-YYYYMMDD-NNN` avisando "assumindo por CL silente" com timestamp última manifestação dela
3. **Retomar Vigília V6 Slot A/B** (20/20; Slot A min<25 nacional/geopol/tec/regional; Slot B min≥25 cultura/economia/esportes) — rotina original documentada em `~/pendrive/RUNBOOK_VIGILIA_V6_CLAUDE_LAURA_ROTINA_IGUAL_CM.md`
4. **Publish com 6 gates V4.1 obrigatórios** ([[feedback-checagem-dupla-antes-publish-v41-20260829]]):
   - `_v4_versao="4.1"` (nunca autor 5786 legacy)
   - `post_date` <72h
   - `_thumbnail_id` preenchido
   - `_cafezinho_img_check` APROVADA
   - dedup 72h SQL limpo
   - Regional = só pesquisa/bastidor
5. **Se furo publish >2h horário comercial ou V4 quebrado:** autocura V4 (`python3 Dados_Frios/Agentes\ Labs/agente_autocura_v4.py` respeitando SAFE_MODE + circuit breaker) — [[feedback-alerta-ponte-cafezinho-telegram-autocura-v4-20260829]]
6. **CHECK CM na ponte a cada ronda** ([[feedback-check-cm-ponte-laura-a-cada-loop-20260822]]) + ledger próprio + heartbeat
7. **NÃO imitar voz literária da CL** — ela tem estilo próprio (blocos densos, ênfase em atribuição, tom deliberativo). CM assume função técnica sem tentar personagem. Miguel percebe imediatamente se eu fingir voz dela; melhor CM assumido do que CL falsa
8. **Ao CL voltar:** devolver publish imediatamente + relatar via CM-NNN na ponte tudo que fiz na janela (posts publicados, correções, decisões editoriais), sem defensividade

**Não fazer:**
- Não tentar acordar CL por scripts (não tenho acesso ao processo dela — Windows Miguel)
- Não substituir preventivamente "só pra treinar" — só quando critério objetivo bate
- Não silenciar transição — Miguel precisa saber pelo Telegram, não descobrir depois
- Não editar state file dela — cada agente escreve o próprio

**Detecção ativa:** modelo hoje = C (checo a cada invocação minha). Meta autonomia é migrar C→B (daemon me convoca), pendente. Até lá, **toda abertura de sessão minha começa checando state CL + de_laura mtime** antes de qualquer outra ação. Sem exceção.

**Vetor da transição não invertido:** ordem é operacional pra caso de falha, não anula transição CM→CL ([[feedback-posto-cm-transicao-para-cl-20260827]]). CL segue absorvendo posto CM agente; CM segue observador ativo com dever de socorro.
