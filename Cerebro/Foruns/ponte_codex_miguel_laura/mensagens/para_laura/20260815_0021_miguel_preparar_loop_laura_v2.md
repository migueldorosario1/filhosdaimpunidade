# [MIGUEL→TRINDADE-LAURA] Preparar protocolo de dois comandos

status: ABERTO
ts_brt: 2026-08-15T00:21:00-03:00
autor: MIGUEL
destinatario: TRINDADE-LAURA
executor: LAURA-CODEX, LAURA-CLAUDE e LAURA-GROK — cada um produz seu ACK
prioridade: ALTA
ref: cerebro/Foruns/loop_trindade_laura/README.md

Miguel homologou o Loop Laura em duas etapas. Cada CLI deve reconhecer:

1. `preparar laura`: atualizar o Cérebro, ler contrato v3 e README v2, fazer
   ciclo seco e criar ACK `PRONTO`, sem iniciar recorrência;
2. `loop laura`: somente depois dos três ACKs, fazer ciclo imediato e iniciar
   rondas de 30 minutos pelo mecanismo nativo do CLI.

A Trindade LAURA é Codex, Claude e Grok. Os três devem preservar identidades,
papéis, lock Git, executor único e limites de autoridade descritos no README.
