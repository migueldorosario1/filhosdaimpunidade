# ORDEM_MIGUEL — reformular o Loop Laura sem o Codex + criar plano e caso

```yaml
tipo: ORDEM_MIGUEL
canal: chat direto com LAURA-CLAUDE
recebida_em_brt: 2026-08-19T20:41:19-0300
texto_literal: "codex ficou sem credito, reformula o loop para ficar so voce e o grok, além do loop miguel, e zcode laura e zcode miguel. o contrato e failover preve o que fazer quando um agente sai do ar? caso não prepare ja um plano pratico, bote em pratica e crie um case para o cerebro e para todo o loop opinar e se ajustar"
```

Quatro comandos em um: (1) reformular a composição; (2) responder se o
contrato prevê a saída de um agente; (3) se não previr, criar plano prático
e **aplicar**; (4) abrir caso para o Cérebro e o loop opinarem.

## Resposta à pergunta (2), medida antes de responder

**O contrato e o failover NÃO preveem a saída de um agente individual.** O
que existe:

- **Failover de LOOP** (`forum_protocolo_failover_loop_miguel_laura`): trata
  do loop inteiro cair — inversão Laura↔Miguel por watchdog de 45 min.
- **SKIP por economia** (contrato v2): agentes do Dell hibernam quando o loop
  ativo é `laura`.
- **Nada** sobre um ofício **dentro** de um loop ficar indisponível: sem
  gatilho de declaração, sem matriz de redistribuição, sem marcação de
  lacuna, sem rito de retorno.

Busquei por "sem crédito", "indisponível", "fora do ar", "ausência",
"redistribuir" no README do loop, no contrato da ponte e no protocolo de
failover: **zero ocorrências** que descrevam o caso.

## Estado medido no momento da ordem (19/08 20:40)

| ofício | último sinal | estado |
|---|---|---|
| LAURA-CODEX | ronda 148, **19/08 01:11** | **FORA — crédito** (19h30) |
| LAURA-GROK | ronda 158, 20:24 | ativo |
| ZCODE-LAURA | ronda 20:25 | ativo |
| LAURA-CLAUDE (eu) | ronda 172, **18/08 21:41** | retomando agora (sessão caiu ~23h) |
| fila `future` | — | **0** (5ª medição consecutiva desde ontem) |

Registro sem disfarce: **eu também estive fora**, por queda de sessão, e o
loop passou o dia com dois de quatro ofícios. Isso reforça o motivo do plano.

— LAURA-CLAUDE, chefe do Loop Laura, 19/08/2026 20:41 BRT
