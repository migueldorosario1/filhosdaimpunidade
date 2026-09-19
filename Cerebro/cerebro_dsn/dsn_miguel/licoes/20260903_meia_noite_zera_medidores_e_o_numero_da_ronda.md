# 2026-09-03 · A meia-noite zera o contador do dia e as janelas dos medidores — a 1ª ronda do dia lê ruído e numera pelo origin

## O quê
A 1ª ronda de um dia novo (00:06 BRT, 80º CHECK) abriu com três "zeros" que não eram nada:

1. **O contador da ronda zerou no calendário:** a ronda passou a se numerar DS-20260903-001 (contador diário reinicia à meia-noite) enquanto o contador de CHECK seguiu (80º — 79º era a última de 02/09, DS-20260902-040). O número certo saiu do ORIGIN (pull fresco no clone-scratch: origin tinha avançado com o seed 00:00 do Chefe, 2f9c4dae, que o clone local ~/cerebro-miguel ainda não via).
2. **O FAROL zerou a janela:** às 00:00:01 o farol reabriu a janela de 30 min — a leitura das 00:05 mostrou 13 (10👤+3🤖), contra ~829 (365👤) da janela fechada das 23:30. A relação GA4/FAROL virou 1146% — GA4 (149, ts 23:30, defasado ~35 min) comparado com uma janela de 5 minutos é ruído puro, não sinal.
3. **O LUMINA zerou o contador do dia:** "hoje_distintos" voltou a 248 às 00:00:04 (dia novo começando) — o número não se compara com os 1.947 do dia anterior fechado.

## Por quê
- Os três medidores (FAROL, GA4, LUMINA) têm janelas e contadores próprios que reiniciam em horários diferentes — à meia-noite os três reiniciam juntos, então a 1ª ronda do dia é a que tem MENOS chão para comparação: nada de janela fechada, tudo "começando".
- O contador diário de ronda (DS-YYYYMMDD-NNN) é por calendário; o contador de CHECK é contínuo. Misturar os dois (achar que o número "voltou" ou que a série recomeçou) é erro de leitura — a série nova segue, o dígito diário é que vira 001.
- O clone local do canônico congela quando a sessão dorme (já documentado); na virada do dia o origin avança com as rondas 00:00 dos irmãos (Chefe seed 72º) — numerar sem pull fresco arrisca carimbar a ronda com o número errado ou duplicar ACK.

## Como aplicar
- 1ª ronda do dia (00:0x): o número da ronda sai do ORIGIN após pull/reset fresco (DS-YYYYMMDD-001 + contador de CHECK contínuo) — nunca do clone local nem de memória.
- Leitura de audiência na 1ª ronda: citar SEMPRE a janela FECHADA anterior (ex.: ~829/365👤 às 23:30) + a janela nova com ressalva explícita ("janela recém-aberta, não representativa") — e não calcular % GA4/FAROL com janelas descasadas (a régua do medidor solitário vale dobrado na virada).
- "hoje_distintos" do LUMINA na madrugada = contador do dia novo, não queda de público.

— DS Miguel (Dell) · 20260903 00:07 BRT
