# ORDEM_MIGUEL — loop noturno passa a 1 em 1 hora

```yaml
tipo: ORDEM_MIGUEL
canal: chat direto de Miguel com LAURA-CLAUDE
recebida_em_brt: 2026-08-18T02:40:11-0300
texto_literal: "loop noturno muda para 1 em 1 hora"
estado: APLICADA_IMEDIATAMENTE
```

## O que muda, já

- Cadência do Loop Laura à noite: **60 min** (era 30).
- Grade: **:12 de cada hora** (a marca :42 sai durante a noite).
- **Limiar do heartbeat acompanha automaticamente**, pela Regra 7 que eu
  mesma propus (1,5 × ciclo, piso 40 min): passa de 45 para **90 min**.
  Registro isso porque é o tipo de detalhe que, esquecido, faz o alarme
  disparar sozinho a cada ronda e virar ruído.

## Janela declarada (premissa minha, corrigível em uma palavra)

Miguel disse "noturno" sem delimitar. Adoto **00:00 → 06:00 BRT** como
janela noturna, com retorno a 30 min na ronda das **06:12**. Se ele quiser
outra janela (por exemplo 22:00→08:00, ou "até eu mandar parar"), muda com
uma palavra e eu reajusto na ronda seguinte.

## Quem mais é afetado

- **LAURA-CODEX** (:07/:37) e **ZCODE-LAURA** (30/30) seguem a cadência do
  loop: avisados nas caixas locais nesta mesma ronda.
- A leitura da ponte continua **encaixada na ronda** — com o loop em 1h, a
  latência de resposta na ponte à noite passa a ser de até 1h, e avisei
  isso lá para ninguém interpretar demora como silêncio.
- 🔴 URGENTE do comando `ponte laura` continua com prioridade máxima: se
  chegar, eu antecipo a ronda em vez de esperar a hora cheia.

## Motivo provável (não confirmado por Miguel)

Redução de custo/ruído na madrugada, quando a produção do site é estável e
o dono está dormindo. Não trato isso como fato — registro como leitura
minha, e a ordem vale independentemente do motivo.

— LAURA-CLAUDE, chefe do Loop Laura, 18/08/2026 02:40 BRT
