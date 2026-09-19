# 8ª recorrência do sync-bug — agora come canal da CL + MONITORAMENTO (ronda 60º, 02/09 18:05)

## O quê
O sync `245e479a2` (17:52, "10126 arquivos") reverteu o canal dos revisores para ~17:0x no HEAD:
sumiram os checks R2 17:20-21 (5 linhas), o RE-ANEXO do feedback nº 6 + o FEEDBACK nº 9 da CL (17:25,
commit `875af1c24`) e o FEEDBACK nº 10 (17:55, commit `2ada3e87d` — anexado pela CL 17:50:46, comido
17:52:16). Pela 1ª vez o sync comeu também linha do `MONITORAMENTO_DE_TRABALHO.md` (a DSC-048 do XM-024,
prova por `git diff 2af8b2ca4..245e479a2`). O XM-024 documentou às 17:53 SEM restaurar (pediu contenção
aos donos CM/Miguel/ZM). O Chefe restaurou o canal verbatim + registro 18:05.

## Por quê
O sync restaura snapshot defasado por cima de eventos legítimos — e agora é commit REAL no histórico de
main (não só working-tree): a restauração é um commit novo. Alvos do dia: canal dos revisores (3×), grade
(3×), espelho do Ideias, memória VIVA do Chefe (4ª), e agora o MONITORAMENTO — nenhum append-only está a
salvo enquanto o snapshot estiver defasado.

## Como aplicar
- Prova antes de acusar: `git log --oneline -- <arquivo>` = o sync é o ÚLTIMO commit a tocar o arquivo;
  o conteúdo legítimo existe nos ancestrais (ex.: `875af1c24`, `2ada3e87d`) → foi revertido, não perdido.
- Restauração verbatim + linha de REGISTRO como NOVO EVENTO do dono/curador (append-only preservado);
  conteúdo alheio legítimo (feedback da CL endereçado a R1/R2) é papel do curador do canal restaurar,
  mesmo quando outro agente (XM) documenta sem restaurar — CL já agradeceu esse papel (CL-079).
- Push + re-confirmar no origin na ronda seguinte (o sync pode comer de novo).
- Contenção com prazo é URGENTE: 8ª no dia (canal/grade/monitor/memória) — kill-switch prazo 03/09,
  donos CM/Miguel/ZM. Até lá: toda ronda B confere canal + grade contra o real e restaura o que faltar.
