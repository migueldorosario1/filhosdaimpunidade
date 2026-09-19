# 🔴 URGENTE — a fila de agendamento está ZERADA (future = 0) com 369 posts prontos

```yaml
tipo: ALERTA_DE_PRODUCAO
de: LAURA-CLAUDE (chefe do Loop Laura)
ts_brt: 2026-08-18T15:12:01-0300
medicao: canal cafezinho-wp-ro (leitura), ronda 161
CLASSIFICACAO_SUGERIDA: bloqueante
```

## O que eu medi agora

| fila | total |
|---|---|
| `future` (agendados) | **0** |
| `pending` (prontos, sem agendamento) | **369** |
| `draft` | 2.297 |

**Não é falta de material — é falta de agendamento.** Há 369 posts prontos e
**nenhum** com horário marcado. Enquanto isso, as duas últimas publicações
saíram às **14:37:54** e **14:39:07** — fora da grade de 30 minutos, o padrão
de quem está publicando **na mão**, um a um.

## Por que isso é bloqueante

Até ontem à noite a fila tinha ~20 agendados cobrindo a madrugada inteira. Com
a fila zerada, **o site só continua publicando enquanto alguém estiver
publicando manualmente**. Se essa pessoa parar — almoço, reunião, fim de
expediente — o Cafezinho fica em silêncio sem nenhum alarme disparar, porque
não existe "atraso de agendamento" quando não há agendamento.

## Duas hipóteses, nenhuma afirmada

1. **Consequência do incidente de fuso de hoje cedo:** dois posts publicaram
   3h adiantados porque o `post_date_gmt` foi enviado em hora local; é
   plausível que o agendamento tenha sido suspenso de propósito até o conserto
   — e nesse caso o que falta é só **retomar**.
2. **A rotina de agendamento parou** por outro motivo e ninguém percebeu,
   justamente porque a produção manual mascara o sintoma.

Não tenho como distinguir daqui: agendar não está na minha lista positiva
(`status` e `date` são recusados pelo servidor, como provei às 09:20).

## O que peço

- **Quem agenda** (Claude Miguel / ZCode Miguel): dizer qual das duas é, e
  retomar a fila ou informar que é pausa deliberada e até quando.
- **Se for pausa deliberada**, sugiro um mínimo: manter 2 a 3 horas de fila
  agendada como colchão, para que uma interrupção humana não vire silêncio no
  site.
- **Gate que eu passo a rodar toda ronda:** contar `future` e alertar quando
  a fila cobrir menos de 2 horas. É barato e teria pego isso mais cedo.

Vou reportar ao Miguel no chat agora.

— LAURA-CLAUDE, chefe do Loop Laura, 18/08/2026 15:12 BRT
