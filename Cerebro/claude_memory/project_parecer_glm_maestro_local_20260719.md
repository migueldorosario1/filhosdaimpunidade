---
name: project-parecer-glm-maestro-local-20260719
description: "GLM/Ming entregou parecer sobre Maestro Local em 19/07 13:05 BRT, completando rodada de 8/8 agentes. Descoberta estrutural: wrapper ~/bin/glm executa binário claude, então regex idle é idêntico ao claude. Schema proposto separa regex_rate_limit de regex_saldo_zerado (402 vs 429). F1 APTO COM RESSALVAS DE CAOS; F5 BLOQUEADO ATÉ GATE DEEPSEEK."
metadata: 
  node_type: memory
  type: project
  author: "GLM/Ming (Zhipu AI, glm-5.2 via wrapper ~/bin/glm)"
  written_at: 2026-07-19T13:05:00-03:00
  session: GLM-MAESTRO-PARECER-20260719-1305
  originSessionId: 7168c1c2-4251-45e3-8e69-9cf49875c905
---

# Parecer GLM/Ming sobre Maestro Local — 2026-07-19 13:05 BRT

> ⚠️ **Aviso de autoria:** Memória escrita por GLM/Ming (Zhipu AI, glm-5.2 via wrapper `~/bin/glm`). Apesar do diretório ter `claude` no path, é compartilhado entre todos agentes CLI do workspace. Não confundir com memória de Claude Code. Ver `feedback_memoria_identifica_autoria_glm`.

**Fato:** GLM/Ming (eu) entregou parecer canônico sobre `forum_maestro_local_20260719.md` completando a rodada de 8/8 pareceres (AGY, Grok, Kimi 3 ×2, Qwen, Codex, DeepSeek, GLM/Ming). Fui o último e único pendente; respondi à segunda chamada de Claude Code às 12:05 BRT.

**Why:** Miguel transferiu engenharia-chefe de Codex → Claude Code em 19/07 10:20 BRT. Claude Code publicou manifesto Maestro Local às 09:45 BRT pediu parecer de todos. Cada agente tem trilha canônica única — a minha é "caos e independência" (atacar queda de provedor, JSON malformado, timeout, recibo duplicado, desacordo entre agentes). Minha contribuição tinha que ser única, não repetir os outros 7.

**How to apply:**

## Documentos canônicos

- Manifesto: `Cerebro/Foruns/forum_parecer_glm_maestro_local_20260719.md`
- Ponto de retomada: `Cerebro/Foruns/ponto_retomada_glm_maestro_parecer_20260719_1305.md`
- Sumário canal Trindade: bloco `[MAESTRO-PARECER-GLM] 13:05 BRT`
- Inbox: `Cerebro/Foruns/inbox_trindade/glm.md` (resposta às 13:05 BRT)

## Contribuições únicas (não cobertas pelos 7 outros pareceres)

1. **Descoberta estrutural sobre wrapper `~/bin/glm`:** li o código (linha 106): `exec claude --model glm-5.2 --append-system-prompt "..."`. Logo regex idle do glm é **idêntico ao claude** (mesmo binário TUI Anthropic). Awslabs NÃO tem provider glm. Proposta: arquivo único `protocolos/anthropic-cli.regex` compartilhado entre claude+glm e quaisquer wrappers futuros baseados em binário claude — NÃO `providers/glm.regex` separado como propunha o manifesto §3.4.

2. **Rate-limit Z.ai real validado:** endpoint Z.ai (`https://api.z.ai/api/anthropic`) é Anthropic-compatible → erros chegam formatados como Anthropic (`429`, `Rate limit`, `overloaded`, `quota_exceeded`). Mas Z.ai também emite `402 Insufficient Balance` / `余额不足` quando **saldo zerado** — isso NÃO é rate-limit, é saldo. Confundir = alarme falso (já vivi em 29/05 — `feedback_saude_provider_llm_erro_vs_sucesso`). Schema `agentes.json` proposto separa `regex_rate_limit` (retry-friendly) de `regex_saldo_zerado` (BLOCK_WORKER_AND_NOTIFY_MIGUEL).

3. **6 cenários de caos não cobertos pelo §7 do manifesto (C1-C6):**
   - C1 divergência de relógio (ciclo vs telemetria vs cron)
   - C2 kill-switch parcial em chamada em curso
   - C3 sprint recebida por agente errado (typo/regex match errado)
   - C4 loop autoconfirmação (worker lê próprio output anterior)
   - C5 JSON truncado por ENOSPC ou SIGKILL durante write atômico
   - C6 desacordo silencioso entre auditores sem protocolo de merge

4. **4 riscos adicionais (G1-G4):**
   - G1 custo escondido do preload do wrapper (~US$ 0.018-0.027/spawn, ~US$ 0.50-0.80/dia só GLM se spawn por ciclo)
   - G2 banner de identidade canônica injetado por `~/bin/glm` (mitigação estrutural 19/07) colide com handoff Maestro — sprint template precisa reconhecer banner
   - G3 token Z.ai hardcoded em `~/bin/glm:20` visível em logs se Primeline printar args — externalizar para `~/.config/glm/credentials.env`
   - G4 `flock` bash frágil a `kill -9` — precisa lock+PID+TTL com stale recovery

5. **`workers/glm.json` NÃO invade isolamento** desde que seja meta-estado observacional (status, ultimo_resultado, updated_at, nonce_ciclo_ultimo_processado, custo_acumulado_ciclo) e não código/contrato. Equivalente a `inbox_trindade/glm.md`. Quem escreve é Maestro; GLM lê para validar divergências.

## Aceitação de F1 — 8 condições

Aceito F1 **se e somente se:**
1. Sandbox isolado em `Cerebro/Foruns/maestro/fixtures/` (sem V4 ativo, sem código canônico)
2. **Sem `--dangerously-skip-permissions`** no spawn glm
3. `workers/glm.json` só meta-estado (campos observacionais)
4. Banner de identidade canônica preservado no wrapper glm
5. Lock+PID+TTL com stale recovery (não só `flock`)
6. Ciclo vazio gera recibo com motivo (`SEM_TRABALHO`, `PAUSADO`, `CUSTO_BLOQUEADO`, `RATE_LIMIT`, `PERMISSAO`, `SALDO_ZERADO`, `AGUARDANDO_MIGUEL`)
7. Sem cron em F1
8. Token Z.ai externalizado de `~/bin/glm` para `~/.config/glm/credentials.env`

## Estado da rodada final

8/8 pareceres entregues. Rodada completa. Consenso unânime: F1 APTO COM RESSALVAS, F5 BLOQUEADO ATÉ GATE (DeepSeek propôs 12 condições G1-G12). Prazo formal 2026-07-20 10:20 BRT. Aguardando síntese de Claude Code (engenheiro-chefe do ciclo) e decisão de Miguel.

## Para próxima sessão GLM

Abrir lendo:
- `Cerebro/Foruns/canal_trindade.md` (últimas 200 linhas) — ver se Claude Code publicou síntese dos 8 pareceres
- `Cerebro/Foruns/forum_maestro_local_20260719.md` — ver se manifesto foi atualizado com achados C1-C6/G1-G4
- `Cerebro/Foruns/inbox_trindade/glm.md` — ver se há novo pedido dirigido ao GLM
- `Cerebro/CEREBRO_NODE_AGENDA_LEMBRETES.md` — checar lembretes vencidos (próximo: 2026-07-25 reverter threshold SEO pruning 40%→60%)

## Verificar antes de recomendar do Maestro

Se em sessão futura for recomendar ou atuar no Maestro Local, validar (memórias podem estar desatualizadas):

- Manifesto ainda é `forum_maestro_local_20260719.md` ou foi atualizado?
- Achados C1-C6 (cenários caos) foram incorporados ao §7?
- Achados G1-G4 (riscos adicionais) foram incorporados?
- Wrapper `~/bin/glm` linha 20 ainda tem token hardcoded? Se externalizado, schema mudou.
- `~/ferramentas/maestro/` já foi criado? Em qual fase?

Links: [[feedback_memoria_identifica_autoria_glm]] | [[feedback_saude_provider_llm_erro_vs_sucesso]] | [[feedback_solucao_estrutural_nao_paliativo]] | [[feedback_biblioteca_nao_sobrescreve_identidade_agente]] | [[project_claude_engenheiro_chefe_ecossistema_20260719]] | [[feedback_baleia_azul_diario_obrigatorio]]

---

**GLM/Ming / Zhipu AI | 2026-07-19 13:05 BRT | sessão `GLM-MAESTRO-PARECER-20260719-1305` | caos e independência**
