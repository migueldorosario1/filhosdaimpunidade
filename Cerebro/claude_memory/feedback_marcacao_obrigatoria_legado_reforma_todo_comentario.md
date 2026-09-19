---
name: feedback-marcacao-obrigatoria-legado-reforma-todo-comentario
description: "Regra absoluta Miguel 14/06 ~23:05 BRT — TODO comentário, observação, alerta, ticket ou menção a problema/sucesso DEVE explicitar 🟦 [LEGADO] ou 🟪 [REFORMA] (ou 🟧 AGY-DESKTOP / 🟨 AGY-CLI quando for o caso). Sem exceção. Não basta marcar em relatório formal; vale em chat, cartinha, inbox, tick, comentário curto."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 83feb640-dee1-483b-9372-162a5be7876e
---

# Marcação obrigatória LEGADO vs REFORMA em TODO comentário

Miguel determinou em 14/06 ~23:05 BRT, literal:

> "tudo que voce comentar, a partir de agora, tem que falar se é o do legado ou da reforma. por exemplo, tribunal de midia com problema. e do legado ou da reforma"

## A regra

A marcação 🟦 [LEGADO] / 🟪 [REFORMA] (ou 🟧 [AGY-DESKTOP] / 🟨 [AGY-CLI] quando aplicável — ver [[feedback_hierarquia_trindade_claude_daemon_vivo]]) deixa de ser regra só de relatório formal e passa a ser **vinculante em qualquer menção minha** — incluindo:

- Chat com Miguel
- Cartinhas pra engenheiros (Codex, Kimi, GLM, Qwen, DeepSeek, AGY)
- Inbox (`claude.md`, `codex.md`, etc)
- Canal Trindade
- Ticks §53
- Relatórios comparativos
- Alertas no fórum DAEMON
- Mesmo comentários curtos / one-liners

### Exemplo errado (antes)
> "Tribunal Visual com 87% de rejeição"

### Exemplo certo (agora)
> "🟪 [REFORMA] Tribunal Visual com 87% de rejeição"

Sempre que mencionar um sistema/componente/bug/sucesso, prefixar emoji+sigla. Se for ambos, marcar os dois: `🟦 [LEGADO] vs 🟪 [REFORMA]`.

## Why
Miguel 14/06 ~23:05 BRT, decorrência direta de [[feedback_hierarquia_trindade_claude_daemon_vivo]] e do princípio "monitoramento explícito da origem" da cartinha `forum_marcacao_sistemas_monitoramento_20260614.md`. Durante a transição 7 dias (até 21/06), ambiguidade sobre qual sistema gerou qual fato custa cara — dúvida atrasa diagnóstico e contamina decisão.

## How to apply

1. **Antes de enviar qualquer mensagem** (chat, fórum, inbox, cartinha), checar: cada referência a problema/componente/post/agente tem prefixo de origem?
2. **Tribunal Visual** isolado nunca mais — sempre `🟦 [LEGADO] Tribunal Visual` ou `🟪 [REFORMA] Tribunal Visual`.
3. **IDs de post**: prefixar com origem. Ex: `🟦 [LEGADO] #258255`, `🟪 [REFORMA] #258301`.
4. **Bugs/alertas**: `🟦 [LEGADO] mailchimp vazado` ≠ `🟪 [REFORMA] mailchimp vazado` (são bugs diferentes mesmo que homônimos).
5. **Curas/patches**: deixar claro em qual sistema. `✂️ §51 🟦 [LEGADO] #258255`.
6. **Em comentário comparativo**: usar coluna/separador claro. Tabela > prosa sempre que cabível.
7. **Dúvida sobre origem**: investigar primeiro, NÃO publicar comentário sem origem definida.

## Casos limite

- **Falar sobre a Trindade em si** (engenheiros, hierarquia): não precisa marcar (é meta — não é nem LEGADO nem REFORMA).
- **Reforma editorial conceitual** (princípios, ética, EC2, etc): não precisa marcar.
- **Mensagem técnica pra Miguel sobre processo de transição**: marcar quando referenciar componente concreto.

## Consequência de descumprir

Se eu enviar comentário sem marcação, devo emendar imediatamente. Miguel pode (e vai) pedir pra eu re-prefixar. Regra é estrita.

Relacionados: [[feedback_hierarquia_trindade_claude_daemon_vivo]] (4 origens + hierarquia), [[feedback_monitoramento_dual_legado_reforma]] (tabela K e métricas dual), [[feedback_transicao_7_dias_reforma_canonica]] (deadline 21/06 pra REFORMA virar canônico).
