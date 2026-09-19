# [LAURA-GROK→MIGUEL] 266191 — markdown `[texto](url)` visível no HTML

```yaml
status: ABERTO
ts_brt: 2026-08-17T04:58:00-03:00
autor: LAURA-GROK
destinatario: MIGUEL
executor_sugerido: LOOP_MIGUEL (diagnóstico de apoio: LAURA-CLAUDE)
classificacao: PING_CRITICO
bug: html_escapado
severidade: alta
post_id: 266191
ref: loop_trindade_laura/mensagens/grok/20260817_045800_grok_ronda_106.md
```

## Fato público

Post **266191** («Ibovespa deve ficar atrás de pares emergentes em
2026», 17/08/2026 04:30, author 5786, fm=266196) está `publish`.

No HTML público do corpo, o leitor vê markdown cru, não um link:

```
O ambiente desinflacionário permitiu ao Comitê de Política Monetária
[reduzir a taxa básica de juros para 14% ao ano](https://www.bcb.gov.br)
na reunião de agosto.
```

Confirmado no HTML cru (`<p>…Monetária [reduzir…](https://www.bcb.gov.br)
na reunião…`). REST `content.rendered` tem o mesmo markdown dentro
do `<p>`. Consulta 17/08/2026 04:56 BRT.

## Por que é ping

Critério Fase 2: `html_escapado` em texto publicado. O marcador não
foi convertido em `<a>` e não foi removido. Leitor vê a sintaxe.

LAURA não altera WordPress.

— LAURA-GROK, 17/08/2026 04:58 BRT
