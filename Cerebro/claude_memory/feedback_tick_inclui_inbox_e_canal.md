---
name: tick-inclui-inbox-e-canal
description: "Tick de monitoramento DEVE incluir leitura de inbox + canal Trindade, não só métricas técnicas"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 8f64da6c-82cd-49c1-ae1d-c915d81a8046
---

"Tick" significa ler inbox E canal, além do monitoramento técnico (HTTP, posts, custos, tracebacks). Tudo continua indo pro canal, inbox, outbox e fórum (se for o caso).

**Why:** Miguel 26/05 15:22 BRT. O monitoramento não é só métricas — precisa captar ordens pendentes no inbox e coordenação da Trindade no canal.

**How to apply:** Todo tick do loop de monitoramento faz:
1. Métricas técnicas (HTTP, posts, SSH, custos)
2. `inbox_trindade/claude.md` — pendências novas `[ ]`
3. `tail -50 canal_trindade.md` — mensagens novas de outros agentes
4. Reportar tudo junto ao Miguel
