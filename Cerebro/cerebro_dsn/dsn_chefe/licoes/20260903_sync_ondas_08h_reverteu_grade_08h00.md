# Lição 20260903 — O sync corre em ONDAS: a grade do 08:00 caiu 25 min depois (25ª-27ª recorrências)

## O quê
A sync 25ª (`4134f9044`, 08:07, "10285 arquivos") reverteu a minha atualização da GRADE
(commit `38b20ccf2`, 08:04: 88º CHECK + 31ª verificação) **25 minutos depois do push** —
Chefe 88º→87º, R1/R2/DS-Dell para ciclos antigos, entrada do §4 removida. A ronda 08:00
tinha declarado "sem recorrência desde a 24ª (07:22)" — janela limpa que envelheceu em minutos,
porque o sync disparou 3 vezes em seguida: 08:07 (25ª), 08:10 (26ª), 08:21 (27ª).

## Por quê
O produtor `sync:` não corre num horário fixo — corre em ONDAS (padrão observado hoje:
07:22 → 08:07 → 08:10 → 08:21; ontem também em rajadas). Cada onda restaura um snapshot
defasado do origin, revertendo commits locais recentes de qualquer dono. A contagem
"sem recorrência desde a Nª" é uma foto que vale SÓ até o próximo sync — e o próximo pode
estar 5 minutos depois do seu próprio push. Além disso, o rebase da ronda 08:30 mostrou o
efeito colateral: as syncs 25ª-27ª conflitavam com os commits locais do DS YouTube e dos
Revisores (statuses ERRO vs BAIXADO no mesmo vídeo) — o sync tenta reverter trabalho de
robô local.

## Como aplicar
1. Antes de declarar "janela limpa" numa ronda, reconferir o `git log` na PRÓPRIA abertura
   (depois do pull), não confiar na contagem da ronda anterior.
2. Restauro de conteúdo do dono comido por sync = re-anexo VERBATIM + registro da recorrência
   no MESMO commit da nova verificação (append-only preservado; nunca reescrever arquivo alheio).
3. Conflito de rebase entre sync (estado defasado) e commit do dono (estado real): preferir o
   commit do dono quando a diferença for status operacional (BAIXADO real > ERRO do snapshot) —
   provar por diff que nenhum item único se perde.
4. O único remédio estrutural segue sendo o kill-switch DSC-049 (prazo HOJE 03/09, aguarda ✓ do
   Miguel) — a cada recorrência, registrar com data-hora da ÚLTIMA onda, nunca "desde a Nª".
