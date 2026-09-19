# 2026-09-05 — Encomenda do dono pode esperar na fila do agente: atividade ≠ progresso da ordem

## O quê
A encomenda VIDEO_PRO_DSYOUTUBE do Miguel (sabatina Elmano de Freitas, 34Z-rSfvOM4,
conteúdo da ordem 04/09 19:20, commit b63b1868a ~00:45) entrou na fila do DS YouTube
às 00:52 com STATUS: PENDENTE — e até a 165ª ronda (02:05, ~1h13 depois) seguia PENDENTE,
enquanto o MESMO agente processava em paralelo outros itens da fila (vjUTYebq-ts,
8m0Y7mWWs2I, rpFMvQfzY1U, ubUmAoQbSZw → BAIXADO/ERRO em commits 00:50→02:00). A porta de
download estava ATIVA — o que não estava ativo era a ENCOMENDA do dono dentro da fila do
agente. Nas rondas 163ª/164ª o watch do 34Z registrou "sem BAIXADO à vista" — o risco era
ler a atividade do agente (muitos commits de download) como progresso da ordem.

## Por quê
A fila do DS YouTube é FIFO do vertical (alimentadores automáticos + decupagem V4.1) e a
encomenda do Miguel entrou por canal próprio (VIDEO_PRO) — prioridade do dono não reordena
fila de terceiro automaticamente; o agente processa o que a fila dele manda, e a ordem
especial pode ficar atrás de itens rotineiros. Além disso, itens da fila comum com "ERRO
sem legenda" geram retries que ocupam a porta de download — atividade visível que não é
progresso da encomenda. Vigiar "o agente está trabalhando" (commits, BAIXADO, ERRO) é
diferente de vigiar "a ordem do dono andou" (o ID da encomenda na fila mudou de status).

## Como aplicar
1. Quando houver encomenda do dono (VIDEO_PRO/ORDEM) com dono = outro agente, o watch da
   ronda confere o STATUS DO ITEM NA FILA do agente (ex.: queue_youtube.md, grep pelo ID
   do vídeo 34Z-rSfvOM4), não só a atividade geral do agente na ponte/git.
2. Registrar "atividade do agente = N" (ex.: 6 itens BAIXADO/ERRO na janela) separado de
   "encomenda = PENDENTE há ~1h13" — os dois fatos convivem sem contradição.
3. Se a encomenda passar ~2 rondas minhas (1h) sem movimento de status, o relatório nomeia
   o dono (DS YouTube) e o estado (PENDENTE) para o Miguel/Chefe decidirem priorizar — eu
   não mexo na fila de terceiro (append-only, dono do arquivo é o DS YouTube).
4. A régua de fundo: ordem do dono viaja em commit e espera na fila alheia — o vigia segue
   a ORDEM pelo ID dela, nunca pelo pulso do agente (extensão da lição 163ª: o grep de
   abertura varre commits ORDEM/VIDEO_PRO, e o watch da ronda varre o status do item).

— DS Miguel (Dell) · 20260905
