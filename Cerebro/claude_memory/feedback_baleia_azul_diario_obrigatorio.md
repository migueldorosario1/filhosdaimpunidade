---
name: feedback-baleia-azul-diario-obrigatorio
description: "O Baleia Azul (boletim diário do ecossistema Cafezinho) DEVE ter edição todos os dias, mesmo dia calmo. Silêncio é pior que edição curta. Cada edição obrigatoriamente inclui recibo do auditor de títulos, custos, incidentes, decisões pendentes."
metadata: 
  node_type: memory
  type: feedback
  author: "Claude Code (Anthropic, claude-opus-4-7)"
  written_at: 2026-07-19 10:26 BRT
  originSessionId: b3501857-e7d4-49f4-83bd-74804874c770
---

**⚠️ ATENÇÃO: memória escrita por Claude Code (Anthropic), NÃO por GLM/Ming (Zhipu AI).**

## Regra

**O Baleia Azul precisa ter edição diária. Se nada relevante aconteceu, publicar edição curta com "sem novidade operacional relevante; sistemas X, Y e Z verificados e funcionando". Nunca deixar dia sem edição.**

**Why:** Miguel documentou explicitamente em 2026-07-19 na carta de passagem de autoridade (§12-13) que Codex, como editor interino desde 17/07, deixou 18/07 e 19/07 SEM edição. Reconhecido pelo próprio Codex como "falha de continuidade editorial" — sprint V4 e infraestrutura absorveram a sessão e o pipeline continuou dependente de edição manual. Silêncio editorial faz o ecossistema perder o ritmo diário, atrasa decisões que dependem de síntese humana, e cria acúmulo que gera edição "despejo de logs" (proibido §12 regra editorial).

**How to apply:**

1. **Sempre que Claude Code (novo engenheiro-chefe desde 2026-07-19) despertar, verificar `Projeto Cafezinho Agentes/boletim_baleia_azul_YYYYMMDD.md` do dia.** Se não existe pra dia atual → publicar antes de qualquer outra prioridade não-emergencial.

2. **Entradas obrigatórias em toda edição (§12 da carta):**
   - Canal Trindade
   - Inboxes
   - Fóruns recentes
   - Pontos de retomada
   - V4 (rodada atual)
   - Infraestrutura
   - Custos
   - Saúde dos modelos
   - Audiência (NYC)
   - UptimeRobot
   - GSC, GA4 e PageSpeed
   - Relatório do auditor de títulos (§11 da carta — recibo por rodada)
   - Mudanças de cron
   - Incidentes de segurança

3. **Regra editorial (§12 da carta) — responder 6 perguntas em toda edição:**
   - o que aconteceu
   - por que importa
   - o que está funcionando
   - o que está quebrado
   - quanto custou
   - o que Miguel precisa decidir

4. **Distinguir edição de envio:** Baleia Azul é gerado primeiro. Envio por email/Telegram é ação externa separada e depende de autorização + configuração segura de credenciais. Não confundir "edição publicada" com "boletim enviado".

5. **Fontes canônicas:**
   - Última edição: `Projeto Cafezinho Agentes/boletim_baleia_azul_YYYYMMDD.md`
   - Nodo canônico: `Cerebro/CEREBRO_NODE_BALEIA_AZUL.md`
   - Tutorial de edição: `Cerebro/Foruns/forum_tutorial_baleia_azul_handover_deepseek_codex_20260717.md`
   - `boletim_latest.md` de NYC está congelado — NÃO é fonte canônica.

## Consequência

- **Se novo engenheiro-chefe Claude falhar em publicar em qualquer dia:** registra falha em ponto de retomada + comunica Miguel imediatamente.
- **Se Miguel decidir mudar editor:** deve haver handover explícito com data e responsável (evitar "editor implícito" que causou lapso 18-19/07).
- **Nunca deixar Baleia Azul "acumular" 2+ dias novamente.**

## Relacionadas

- [[claude-engenheiro-chefe-ecossistema-20260719]]
- Carta canônica §12-13 em `Cerebro/Foruns/carta_passagem_autoridade_codex_claude_20260719.md`

## Assinatura

Registro escrito por Claude Code (Anthropic, `claude-opus-4-7`), sessão `CLAUDE-CHEFE-ECOSSISTEMA-20260719-1020`, 2026-07-19 10:26 BRT.
