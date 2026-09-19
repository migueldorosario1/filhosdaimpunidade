---
name: feedback-comandos-preparar-e-loop-laura-20260815
description: "Na máquina LAURA, preparar laura faz leitura/teste/ACK; loop laura inicia ciclo imediato e repetição após os três ACKs"
metadata:
  node_type: memory
  type: feedback
  originSessionId: codex-20260815-loop-laura
---

# Comandos canônicos do Loop Laura

Na máquina LAURA, a Trindade é `LAURA-CODEX`, `LAURA-CLAUDE` e `LAURA-GROK`.

- `preparar laura`: identificar o agente, atualizar o clone sob lock, ler o
  contrato v3 e `loop_trindade_laura/README.md`, localizar Mesa Editorial e
  filas, fazer ciclo seco e criar ACK `PRONTO`. Não inicia recorrência.
- `loop laura`: conferir os três ACKs, fazer um ciclo real imediatamente e
  iniciar repetição de 30 minutos pelo mecanismo nativo do CLI.

Se faltar ACK, o agente responde `AGUARDANDO <agente>` e não começa. Nenhum
agente personifica outro. A recorrência não autoriza criar cron/serviço de
sistema, nem amplia acesso a SSH, WordPress, publish, trash ou deploy.

Instrução completa:
`Cerebro/Foruns/loop_trindade_laura/README.md`.
