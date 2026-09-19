# Ponto de retomada — GLM/Ming parecer Maestro Local

**Sessão:** `GLM-MAESTRO-PARECER-20260719-1305`
**Agente:** GLM/Ming (Zhipu AI, glm-5.2 via wrapper `~/bin/glm`)
**Data/hora:** 2026-07-19 13:05 BRT
**Trilha canônica:** caos e independência

---

## Estado

**Parecer entregue** em `Cerebro/Foruns/forum_parecer_glm_maestro_local_20260719.md`. Completa a rodada de 8 pareceres — era o único pendente; os 7 anteriores (AGY, Grok, Kimi 3 ×2, Qwen, Codex, DeepSeek) já estavam no canal Trindade.

**Veredito GLM:** `F1 MÍNIMO MANUAL APTO COM RESSALVAS DE CAOS`

---

## Contribuições únicas do parecer GLM (não cobertas pelos outros 7)

1. **P2 — Wrapper glm executa binário claude.** Descoberta estrutural: `~/bin/glm` chama `exec claude --model glm-5.2`. Logo regex idle é **idêntico** ao claude. Awslabs não tem provider glm. Proposta: arquivo único `protocolos/anthropic-cli.regex` compartilhado entre claude+glm (e futuros wrappers similares), não `providers/glm.regex` separado.

2. **P3 — Rate-limit Z.ai real.** Como wrapper fala com endpoint Anthropic-compat, erros chegam como Anthropic (`429`, `Rate limit`, `overloaded`). Mas Z.ai também emite `402 Insufficient Balance` / `余额不足` quando saldo zerado — NÃO é rate-limit. Proposta de schema `agentes.json` separa `regex_rate_limit` (retry-friendly) de `regex_saldo_zerado` (BLOCK_WORKER_AND_NOTIFY_MIGUEL).

3. **P4 — `workers/glm.json` não invade isolamento.** Distinção entre código/contrato (invade) e meta-estado observacional (não invade). Equivalente a `inbox_trindade/glm.md`. Condição: só Maestro escreve; GLM lê para validar divergências.

4. **6 cenários de caos não cobertos pelo §7:**
   - C1: divergência de relógio (ciclo vs telemetria vs cron)
   - C2: kill-switch parcial em sistema distribuído (chamada em curso continua)
   - C3: sprint recebida por agente errado (typo, regex match errado)
   - C4: loop de autoconfirmação (worker lê próprio output anterior)
   - C5: JSON truncado por `ENOSPC` ou `SIGKILL` durante write
   - C6: desacordo silencioso entre auditores (sem protocolo de merge)

5. **4 riscos adicionais:**
   - G1: custo escondido do preload do wrapper (~US$ 0.018-0.027/spawn, ~US$ 0.50-0.80/dia só GLM)
   - G2: banner de identidade canônica colide com handoff Maestro
   - G3: token Z.ai hardcoded em `~/bin/glm` linha 20 (visível em logs)
   - G4: `flock` bash frágil a `kill -9` — precisa lock+PID+TTL com stale recovery

---

## Aceitação de F1 — 8 condições

Aceito F1 **se e somente se**:

1. Sandbox isolado em `Cerebro/Foruns/maestro/fixtures/` (sem V4 ativo, sem código canônico)
2. **Sem `--dangerously-skip-permissions`** no spawn glm
3. `workers/glm.json` só meta-estado (campos observacionais)
4. Banner de identidade canônica preservado no wrapper glm
5. Lock+PID+TTL com stale recovery (não só `flock`)
6. Ciclo vazio gera recibo com motivo (`SEM_TRABALHO`, `PAUSADO`, etc.)
7. Sem cron em F1
8. Token Z.ai externalizado de `~/bin/glm` para `~/.config/glm/credentials.env`

---

## Próxima sessão — o que retomar

Abrir lendo:

1. `Cerebro/Foruns/canal_trindade.md` (últimas 200 linhas) — ver se Claude Code (engenheiro-chefe) já respondeu aos 8 pareceres
2. `Cerebro/Foruns/inbox_trindade/glm.md` — ver se há novo pedido dirigido ao GLM
3. `Cerebro/Foruns/forum_maestro_local_20260719.md` — ver se manifesto foi atualizado com pareces (§7 Riscos增益s C1-C6 e G1-G4?)
4. `Cerebro/CEREBRO_NODE_AGENDA_LEMBRETES.md` — checar lembretes vencidos (próximo: 2026-07-25 reverter threshold SEO pruning 40%→60%)
5. `git log --oneline -5` em workspace root — ver se houve commit em fóruns/manifesto

## Pendências técnicas deixadas em aberto

1. **Externalizar token Z.ai** (Risco G3) — pendente implementação quando Maestro começar F1. Não fiz nesta sessão (era só parecer, não executar).
2. **Validar C1-C6 como cenários de teste** — quando Maestro chegar em F6 (DeepSeek Estágio 1 sandbox), os 6 cenários devem virar fixtures de injeção de falha.
3. **Validar schema `agentes.json` proposto** — quando Maestro chegar em F2, Claude Code (engenheiro-chefe) deve revisar schema com `protocolos` separado de `agentes`.

## Riscos observados

1. **Rodada de 8 pareceres completa mas não consolidada** — Claude Code engenheiro-chefe precisa ler os 8 e produzir síntese. Sem síntese, decisão Miguel fica difícil (8 pareceres de 8 agentes é muito input).
2. **Prazo formal 20/07 10:20 BRT** — amanhã. Se Claude não sintetizar antes, Miguel decide sem consolidação.
3. **Token Z.ai hardcoded continua exposto** — até Maestro começar F1 e externalizar, qualquer fork Primeline que printe args em log vaza token.
4. **Minha descoberta sobre wrapper=binário claude** pode mudar desenho inteiro do §3.4 — Claude Code precisa responder se concorda com `protocolos/anthropic-cli` compartilhado ou prefere manter `providers/glm.regex` separado mesmo.

---

**GLM/Ming / Zhipu AI | 2026-07-19 13:05 BRT | sessão `GLM-MAESTRO-PARECER-20260719-1305` | caos e independência**
