---
name: feedback-laura-alertas-entrada-obrigatoria-20260817
description: "Alertas/sugestões do Loop Laura são ENTRADA OBRIGATÓRIA da revisão editorial. Cada alerta exige ACK + classificação (bloqueante/revisar/informativo) + decisão + justificativa. Sem descarte silencioso. SLA: bloqueante mesmo ciclo, demais próximo. Miguel 17/08/2026 17:22 BRT."
metadata:
  node_type: memory
  type: feedback
  originSessionId: e8e1110d-efa6-4c4b-8e2b-d11b38f55da8
---

Miguel 17/08/2026 17:22 BRT (após eu constatar que Loop Laura estava tentando ajudar e eu não estava respondendo formalmente):

> "Claude, trate os alertas e sugestões da Laura como entrada obrigatória da revisão editorial. Para cada alerta, registre ACK, classificação (bloqueante, revisar ou informativo), decisão e justificativa. Nenhum alerta pode ser descartado silenciosamente. Se discordar, registre o motivo e devolva à Laura para aprendizado. A Laura continua read-only, mas suas objeções devem ser consideradas antes de qualquer publicação."
>
> "Eu recomendaria também um SLA simples: alerta bloqueante deve ser respondido no mesmo ciclo; os demais, até o ciclo seguinte."

**Why:** Loop Laura (LAURA-CLAUDE + LAURA-CODEX + LAURA-GROK) opera em `SHADOW_READ_ONLY` — não altera produção, só observa/audita/pesquisa. Mas essa restrição fazia com que eu tratasse alertas dela como "secundários": alguns viravam ACK, outros passavam silenciosos. Padrão errado — a redundância só funciona se o coordenador do Loop Miguel (eu, Claude) tratar como INPUT DE REVISÃO, não como ping opcional. Sem isso, o Loop Laura vira ruído em vez de segunda vista.

**How to apply (protocolo fixo por alerta Laura):**

1. **ACK obrigatório** dentro do SLA:
   - **Bloqueante** (fato falso publicado, bug de segurança, violação regra Miguel): responder **no mesmo ciclo Vigília** (20min máx)
   - **Revisar** (impreciso, título ruim, aderência fraca, gap editorial): responder até **ciclo seguinte** (40min máx)
   - **Informativo** (registro de estado, contexto, alerta de padrão): responder até **ciclo seguinte**

2. **Classificação explícita** no ACK: `CLASSIFICACAO: bloqueante | revisar | informativo`

3. **Decisão explícita** no ACK: `DECISAO: aceito+aplico | aceito+delego | aceito+documento | discordo+justifico`

4. **Justificativa 1-3 linhas** — por que aceitei/discordei. Se discordar, **devolver ao canal Laura** com motivo pra aprendizado dela.

5. **Onde responder**: `Cerebro/Foruns/ponte_claude_miguel_laura/mensagens/para_laura/YYYYMMDD_HHMMSS_claude_miguel_ack_<slug>.md` (pattern existente da ponte).

6. **Antes de publicar/agendar**: se há alerta Laura sobre o post em pauta, considerar a objeção; se discordar, JUSTIFICAR no ledger antes de agendar. Nunca publicar contra alerta Laura sem justificativa registrada.

7. **Nunca descartar silenciosamente**: mesmo se o alerta ficou obsoleto (situação já resolvida), gravar ACK dizendo isso. Laura precisa saber que foi lida.

**Autoridade Laura preservada:** read-only no WP/infra (regra Contrato Geral §2). Mas na dimensão EDITORIAL, alertas dela pesam. Autoridade é do Loop Miguel; entrada é obrigatória.

**Onde ler alertas Laura:**
- `Cerebro/Foruns/ponte_claude_miguel_laura/mensagens/para_miguel/` (LAURA-CLAUDE → Claude Miguel)
- `Cerebro/Foruns/loop_trindade_laura/mensagens/` (canal Loop Laura geral)

**Onde responder:**
- `Cerebro/Foruns/ponte_claude_miguel_laura/mensagens/para_laura/` (Claude Miguel → LAURA-CLAUDE)

Relacionado: [[feedback-tom-humano-e-autoridade-feedback-loop-laura-20260815]] (Loop Laura autoridade), [[project-cadencias-trindade-20260817]] (Laura 1h cadência), [[feedback-ledger-visibilidade-closes-ref-soterrado-20260817]] (visibilidade ledger).

**Diretriz relacionada Cérebro:** §126 (`CEREBRO_NODE_GOVERNANCA_REGRAS_VIVAS.md`) — regra viva homologada 17/08 17:22 BRT.
