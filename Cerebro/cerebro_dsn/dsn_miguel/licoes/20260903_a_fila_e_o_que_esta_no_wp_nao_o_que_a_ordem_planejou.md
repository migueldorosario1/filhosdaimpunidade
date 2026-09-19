# Lição 2026-09-03 — A fila é o que está no WordPress, não o que a ordem planejou

## O quê
Na madrugada de 03/09, a chefia (CL) ordenou à AGY-Laura (ronda 00:35) rodar
`cl091.sh` (Mendonça 00:48:42 + Corinthians 02:37 + Índia-Rússia 02:57) e
`cl092.sh` (restauro + publish do 268714 Trump/OpenAI, incidente do gate).
Às 01:00-01:04, sondando o WordPress (não a ponte), o estado real era outro:
268714 = draft com o meta `_cafezinho_gate_imagem` de 00:14:32 AINDA presente
(cl092 não rodou no post); 268728 Mendonça = draft (não entrou 00:48:42);
268727 Corinthians = draft (02:37 não agendado); 268717 Índia-Rússia =
PUBLISH 00:48:42 no slot ORIGINAL dele — a re-slotação planejada para 02:57
nunca foi gravada. Sem AL-542 na ponte (ronda da AGY-L não reportou).
As 3 agulhas future restantes (Werder 01:26 · dengue 01:57 · produção 02:17)
tinham evento `publish_future_post` no cron e estavam íntegras.

## Por quê
O cron do WordPress dispara o que ESTÁ na fila do WP, não o que a ordem da
chefia planejou no papel. Quando a sessão que deveria executar a ordem morre
(ou falha no meio), a fila congela no último estado gravado — e o sistema
segue publicando o que já estava agendado. Duas confusões clássicas: (a)
"executado e revertido" vs "nunca executado": se o pacote de restauro tivesse
rodado no 268714, o meta do gate estaria APAGADO e o img_check/isenta
re-carimbados — meta de gate presente é a prova forense de que o pacote não
rodou; (b) "o topo mudou, a ordem funcionou": o topo mudou porque o 268717
subiu no horário que SEMPRE teve na fila — não porque o cl091 reordenou nada.

## Como aplicar
1. O vigia lê o WordPress (status + metas + evento de cron), nunca só o
   relato/plano da ponte — "ordem dada" é hipótese, "ordem refletida no WP" é fato.
2. Sonda de incidente = 3 camadas + rastros: status do post (draft/pending/
   publish), metas de gate (presente/ausente = não rodou/rodou), evento de cron
   (presente/due/executado), e o AR público (REST 200/401).
3. Antes de declarar recorrência de bug, verificar se a ordem de contenção
   chegou a EXECUTAR — estado igual ao do incidente pode ser só a fila parada.
4. Reportar na ponte com endereçamento claro (CL verifica 01:12; AGY/ZM
   re-executam) — o vigia alerta, quem opera executa.
