---
name: Sistema voltou a usar "Slot" em Tarefasdeagora.md (terminologia anterior reativada)
description: Entre fim/abr e maio 2026 o Tarefasdeagora.md voltou ao modelo de Slots numerados (1..N) com estados 🟢🟡🔵⏸️✅. Vocabulário oficial é Slot, não Tarefa.
type: feedback
originSessionId: 7c7867b0-668d-4c9f-9f68-fd2bf7f1ba99
---
`Tarefasdeagora.md` usa **Slots numerados** (Slot 1, Slot 2, ..., Slot 26) com estados:
- 🟢 LIVRE — vago
- 🟡 ATRIBUÍDO — tarefa na fila, sem sessão tocando
- 🔵 EM ANDAMENTO — sessão Claude tocando agora
- ⏸️ PAUSADO — parado por dependência ou decisão
- ✅ CONCLUÍDO — fechado, slot reciclável

Cada slot tem memória própria em `Memorias/slots/slot_<NN>_<assunto>.md`, indexada em `Memorias/slots/INDEX_SLOTS.md` (regra §33 do `CEREBRO_NODE_GOVERNANCA.md`).

**Why:** Em 2026-04-26 esta memória registrava "abolido — usar tarefa, não slot". Mas o sistema operacional vivo (Tarefasdeagora.md + índice próprio em `Memorias/slots/` + `CEREBRO_NODE_GOVERNANCA.md` §33) reverteu pra Slot. Manter "Slot" como vocabulário oficial impede dissonância entre Claude e os arquivos canônicos.

**How to apply:**
- Ao ler `Tarefasdeagora.md`, falar em "Slot N", não "Tarefa N".
- Ao auto-alocar, marcar Slot como 🔵 EM ANDAMENTO e carimbar timestamp.
- Para abrir slot novo, criar memória em `Memorias/slots/slot_<NN>_<assunto>.md`.
- Slots ativos em 2026-05-09: Slot 1 CEO Cérebro 🔵; Slots 2–10 🟡 ATRIBUÍDO; Slots 20–26 ⏸️ ou ✅ (legados).
