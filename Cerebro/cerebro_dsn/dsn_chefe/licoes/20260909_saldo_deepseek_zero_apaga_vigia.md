# Lição 09/09/2026 — Saldo DeepSeek zero apaga a vigia (DS-N + DS-Dell caem juntos)

## O quê
Na madrugada de 09/09, as rondas DS-N 359a-366a (02:00→05:30) e as rondas do DS-Dell (pós-339a, 01:32) NÃO executaram. Causa provada no log /tmp/ronda_dsn/20260909.log: "dsh: QUOTA: Insufficient Balance" em todas as 7 tentativas. O saldo DeepSeek zerou ~01:45 (DSN-F ronda 625 anotou US$ -0,07) e a recarga só veio ~05:45 (DSN-F 641: US$ 19,79). Consequência: o relatório 4/4h das 04:00 NÃO foi enviado ao Telegram (1º 4/4h perdido da série DS-N) e a vigia ficou cega 4h30 — o watch do lag do mirror (269518) ficou sem cobertura e a família evoluiu de lag ≤60 min para interrupção total (~6h30, mirror parado no 269538 das 23:00).

## Por quê
A conta DeepSeek é compartilhada entre os robôs DS (DS-N na Tencent e DS-Dell). Quando o saldo chega a ≤ 0, o provider devolve QUOTA e o launcher (ronda_dsn.sh) morre no 1º segundo — sem ronda, sem ponte, sem relatório. O DSN-F (financeiro) anotou o saldo NEGATIVO na ronda 625 (01:45) mas nenhuma ronda DS-N leu isso a tempo (a 358a das 01:30 já não teria como agir; a 359a das 02:00 já caiu). CL e AL (Claude/Anthropic) não foram afetadas — dependência de UM provedor para a cadeia de vigia.

## Como aplicar
1. Watch do saldo DeepSeek como item fixo de ronda: quando o DSN-F anotar saldo ≤ US$ 1-2 (ou negativo), a ronda deve ESCALAR recarga imediatamente (aviso ao ZM/DSN-F/dono no bloco da ponte + menção no 4/4h) — recarga ANTES do zero, não depois.
2. Se a ronda cair por QUOTA: registrar no log (o launcher já grava) e, na volta, declarar o buraco com hora na ponte (que rondas caíram, o que ficou sem cobertura, o que o 4/4h seguinte precisa consolidar).
3. O relatório 4/4h perdido NÃO gera mensagem avulsa — consolida no 4/4h seguinte (régua da casa).
4. Watchs abertos (ex.: mirror) ganham cobertura dobrada na ronda de retorno — o buraco de vigia pode ter deixado um lag virar parada (foi o caso do mirror: 269518 ausente 5h30 quando voltei).
5. Conferir também o DS-Dell: mesma conta = mesmo buraco; registrar o retorno dele quando o saldo dele voltar.
