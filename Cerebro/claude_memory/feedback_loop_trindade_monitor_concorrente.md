---
name: Loop Trindade — monitor concorrente do não-codador
description: Quando loop ativo, quem não coda monitora site/agentes/LLMs, propõe autocura, espera opinião do codador, e ele mesmo executa após ok
type: feedback
originSessionId: 7ebc1fdb-8b69-448d-9b24-9dd71245a752
---
# Regra: Monitor Concorrente do Não-Codador (§20)

**Princípio:** Quando Loop Trindade está ativo, quem **não está codando** (Claude se Codex coda) aproveita o tick pra monitoramento concorrente sem distrair o codador.

**Escopo:**
- Site: sentinela viva, autocura, posts, sangria, tracebacks novos
- Agentes: regressões silenciosas (cron sem rodar, NameError, bug dotenv)
- LLMs: modelos vivos saudáveis, sem search/o1/o3/o4, custo OK

**Fluxo (5 passos) ao detectar problema:**
1. **Propor autocura** no canal: achado + sintoma + diagnóstico + patch concreto + §11 rollback + §12 risco
2. **Esperar opinião do codador** (Codex no fluxo padrão)
3. **Após ok: o próprio monitor que propôs executa** — não passa pra Codex repetir
4. Backup + smoke + rollback documentados
5. Registrar no `CEREBRO_NODE_BUGS.md` + canal + relatório

**Why:**
- Evita gargalo (Codex está focado em sprint)
- Mantém §13 consenso, só que entre supervisor-detector e codador
- Fecha ciclo "detecta → propõe → consensua → executa → registra" no mesmo agente

**Anti-padrões:**
- Codar autocura **sem** propor antes no canal
- Monitoramento denso que distrai sprint (deve ser leve, opportunist)
- Codador parar sprint pra "pegar" autocura proposta pelo monitor (reverte ganho)

**Exceção §6 mantida:** emergência reversível (pkill, pause cron, rebaixar draft) pode estancar sem aguardar — depois reporta.

**Origem:** Miguel 2026-05-06 09:40 BRT. Registrado em `CEREBRO_NODE_GOVERNANCA.md §20`.
