# Lição 2026-09-04 — O append no nodo foi comido pelo sync MESMO depois do push confirmado

## O quê
Na ronda 139ª (05:30), a conferência de abertura no origin mostrou que o sync
`25d564c0` (05:22, "10364 arquivos") COMEU do `CEREBRO_NODE_BUGS_ATIVOS.md` os
appends 24ª (DS-137, commit `1d10c09d`, 04:30) e 25ª (DS-138, commit `422e657a`,
05:00) que eu havia feito e PUSHADO — o diff do sync mostra as linhas removidas
(e ele comeu também a 25ª do DS-N 130º). Os commits existem no histórico do git;
o CONTEÚDO no origin voltou a terminar na 23ª (DS-136). As rondas 137ª/138ª
haviam conferido "sync-bug sem recorrência nos MEUS arquivos" — mas só olharam
VIVA/memoria, não o NODO.

## Por quê
O produtor do snapshot defasado (o processo de sync do mirror) sobrescreve
arquivos com uma cópia antiga; append que eu confirmei no meu commit é revertido
por um commit de sync POSTERIOR. O método da 138ª — "diff vs último commit que
tocou o arquivo" — pegou o caso: o último commit que tocou o nodo era o PRÓPRIO
sync. A lição da 133ª (conferir pelo origin, não pelo clone local RO) valia para
ler; faltava estender a conferência pós-append a TODOS os arquivos que eu
appendi — o nodo de bugs era o ponto cego. E o commit do sync é assinado como o
dono ("Miguel do Rosario") — carimbo textual não é autoria, é o processo.

## Como aplicar
1. Na abertura da ronda, conferir no ORIGIN o conteúdo dos arquivos que appendei
   na ronda anterior: `git show origin/main:cerebro/CEREBRO_NODE_BUGS_ATIVOS.md |
   grep "CONFIRMAÇÃO" | tail -2` (e o mesmo para VIVA, memoria e de_dell).
2. Se o sync comeu: re-append com NOTA do gap (append-only, nunca reescrever;
   a série completa fica nos blocos da ponte + histórico do git) e registrar a
   recorrência com o hash do sync no nodo.
3. Isto é o argumento mais concreto para o kill-switch DSC-049 (prazo era 03/09,
   aguarda ✓ do Miguel): o append que EU conferi no commit foi revertido por um
   snapshot defasado horas depois — restaurar é respiro (02/09), a cura é o
   kill-switch.
4. Carimbo textual (autor "Miguel do Rosario" no commit do sync) não é cursor de
   autoria — o diff é a prova.
