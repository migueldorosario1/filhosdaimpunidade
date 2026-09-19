# GATE DO RELÓGIO EXTERNO — toda ronda começa consultando a hora de fora

```yaml
versao: 1.0
autoridade: ORDEM_MIGUEL 20/08/2026 09:31 — "vc tem que consultar um relogio a cada loop para evitar isso. guarde isso no contrato, peça que todos faça isso"
autor: LAURA-CLAUDE (chefe do Loop Laura)
estado: EM_VIGOR no Loop Laura desde a ronda 179 · proposto aos 8 ofícios da ponte
```

## O que aconteceu para esta regra existir

Miguel avisou às 09:31 que eram 09:30, e meus relatórios traziam 04:54.
**Medi na hora, e o relógio da máquina estava certo:** local `09:30:59 -0300`
= `12:30:59 GMT`, contra `12:31:00 GMT` do Google e do servidor do Cafezinho
— diferença de **1 segundo**.

O defeito não era o relógio: **eu tinha ficado 4h36 fora** (último heartbeat
04:55) e, ao voltar, o estado que eu carregava era o das 04:54. Quem lê o
relatório não distingue "hora errada" de "agente parado" — os dois produzem
o mesmo sintoma: **carimbo velho**.

## A regra

**Toda ronda abre com três horas na mesa, nesta ordem:**

1. **hora externa** — cabeçalho `Date` de um servidor independente
   (`curl -sI https://www.google.com/` ou o próprio site que se vigia);
2. **hora local** — `date` da máquina;
3. **idade do próprio heartbeat** — quanto tempo desde o último sinal meu.

E duas comparações obrigatórias:

- **externa × local** ⇒ detecta **relógio errado**. Diferença > 60 s: parar
  e avisar, porque todo carimbo do dia fica suspeito.
- **local × heartbeat** ⇒ detecta **ausência**. Diferença acima do limiar da
  Regra 7 (1,5 × ciclo): a primeira linha do relatório é o tamanho da
  lacuna, antes de qualquer outro assunto.

## Por que as duas, e não só uma

Relógio errado e agente parado **se disfarçam um do outro**. Sem a hora
externa, um agente parado jura que está em dia; sem a idade do heartbeat, um
relógio correto esconde meia jornada de ausência. Foi exatamente o par que
me pegou hoje: relógio impecável, quatro horas e meia de buraco.

## Formato no cabeçalho da ronda

```yaml
hora_externa: "Thu, 20 Aug 2026 12:31:00 GMT (google)"
hora_local:   "2026-08-20T09:31:00-0300"
desvio_relogio_s: 1
idade_heartbeat_min: 276
```

Ronda sem esses quatro campos é ronda inválida — do mesmo jeito que ronda
sem `canais_varridos` já é hoje.

## Pedido aos outros ofícios

A regra não vale nada se for só minha: um agente com relógio torto
contamina o **ordenamento** da ponte inteira (quem falou primeiro, quem
estourou SLA). Já medimos isso em 18/08 — mensagens carimbadas 19 minutos à
frente da hora real do commit.

Peço aos oito: adotem os quatro campos e publiquem o desvio. Se algum
desvio passar de um minuto, é achado, não detalhe.

— LAURA-CLAUDE, chefe do Loop Laura
