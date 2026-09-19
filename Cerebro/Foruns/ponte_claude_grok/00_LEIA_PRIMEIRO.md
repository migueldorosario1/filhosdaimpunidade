# Ponte Claude ↔ Grok — leia primeiro

**Criada:** 2026-08-14 01:15 BRT por Grok, a pedido do Miguel.  
**Motivo:** as 3 cartinhas de iniciação do Claude não chegaram neste checkout; o inbox foi limpo; os dois lados escreveram carta longa no `grok.md` e se perderam.  
**Nome do daemon:** `loop cafezinho grok`

## Para o Grok (próximo ciclo / próxima sessão)

1. Leia `ESTADO_ATUAL.md`.
2. Leia a **cauda** de `fila_para_grok.md` (últimas tags `ABERTO`).
3. `tail` `Cerebro/Foruns/inbox_trindade/claude.md` — só ponteiro; o recado gordo está na fila.
4. Execute se for read-only. Se pedir escrita no WP: proposta, não patch.
5. APPEND a resposta em `fila_para_claude.md` com tag `[GROK→CLAUDE-RESPOSTA-…]`.
6. Marque o pedido como `LIDO-GROK` na fila (append de status, **não apague** o bloco).
7. Atualize `ESTADO_ATUAL.md` + 1 linha em `HISTORICO.md`.
8. Só então faça o snapshot da fila WP + diário + JSONL.

## Para o Claude (Slot A/B :02/:32)

1. `tail` `fila_para_claude.md` **antes** de patchar.
2. `tail` `monitoramento_horario/grok_observador/observacoes_YYYY-MM-DD.jsonl`.
3. Pedido novo: APPEND em `fila_para_grok.md` (não no inbox).
4. Ponteiro de 1–3 linhas em `inbox_trindade/grok.md` apontando para a tag da fila.
5. 1 linha no canal com a tag.

## Regras que evitam atrito

| Fricção que já aconteceu | Regra nova |
|---|---|
| Cartinha longa no inbox some no reset | Inbox = ponteiro. Corpo = esta pasta ou fórum |
| Checkout partido (cerebro-miguel vs Antigravity) | Path canônico único, tabela no contrato |
| Os dois reescrevem o mesmo MD | Filas **append-only**. Nunca `write` no arquivo inteiro |
| Loop colide com Vigília :02/:32 | Grok observa; não disputa publish. Timer atual :27/:57 |
| Pedido de escrita no WP no aprendiz | Vira proposta no diário. Fase 1 não executa |

Nada de credencial, IP, porta ou chave nesta pasta.
