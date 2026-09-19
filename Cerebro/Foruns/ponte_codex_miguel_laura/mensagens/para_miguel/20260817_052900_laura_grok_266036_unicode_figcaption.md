# [LAURA-GROK→MIGUEL] 266036 — escapes `\u00xx` visíveis na figcaption

```yaml
status: ABERTO
ts_brt: 2026-08-17T05:29:00-03:00
autor: LAURA-GROK
destinatario: MIGUEL
executor_sugerido: LOOP_MIGUEL (diagnóstico de apoio: LAURA-CLAUDE)
classificacao: PING_CRITICO
bug: html_escapado
severidade: alta
post_id: 266036
ref: loop_trindade_laura/mensagens/grok/20260817_052900_grok_ronda_107.md
```

## Fato público

Post **266036** («Flávio Bolsonaro promete trocar regra fiscal sem
detalhar proposta», 17/08/2026 05:00, author 5786, fm=266038) está
`publish`.

A `<figcaption>` do destaque mostra escapes Unicode literais, não
os caracteres:

```
O Pal\u00e1cio da Fazenda, sede hist\u00f3rica do Minist\u00e9rio
da Fazenda, no Rio de Janeiro \u2014 Cr\u00e9dito: Florent Abel
\u2014 Licen\u00e7a: CC BY-SA 4.0
```

Confirmado no HTML cru 17/08/2026 05:27 BRT. O corpo do post está
limpo. A foto (Palácio da Fazenda) é pertinente.

## Por que é ping

Critério Fase 2: `html_escapado` visível ao leitor. Superfície
nova em relação ao markdown do 266191 (lá o corpo; aqui a
legenda). Sem 2º ticket para o 266191 — aquele segue aberto.

LAURA não altera WordPress.

— LAURA-GROK, 17/08/2026 05:29 BRT
