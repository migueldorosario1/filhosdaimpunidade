---
name: Termine o código e suba — não pare no meio
description: Miguel expressou que, quando Claude começa um fix, deve terminar e deployar imediatamente. Não deixar incompleto para "perguntar depois".
type: feedback
originSessionId: 82c307d7-bd07-4c7a-8ed2-9e86b6fa4e22
---
Regra de fluxo: **quando o fix já está autorizado e em andamento, terminar e subir antes de pausar.** Não deixar "meia-feito" por pudor de "perguntar se continua".

**Why:** em 2026-04-17 Claude começou um fallback Grok→gpt-4o no `gerador_meta_textos.py`, deixou meio-feito (3 call sites não trocados), e pausou para "esperar Miguel ouvir algo novo". Miguel respondeu: *"desculpa, o certo é sempre voce terminar o codigo e voce subir."* Ele prefere que o trabalho chegue no servidor, mesmo quando chega uma interrupção pra conversa.

**How to apply:**
- Quando iniciei um fix com autorização clara ("pode corrigir") e já tenho o diagnóstico, devo **acabar** antes de mudar de assunto — especialmente se faltam apenas trocas triviais (renomear função, call sites, etc).
- Se uma interrupção importante chegar (novo contexto/pedido), terminar o fix antes de processar o novo contexto. Pausar só se o novo input contradisser o fix em andamento.
- **Não perguntar "posso continuar?" se a autorização original cobre:** só rodar.
