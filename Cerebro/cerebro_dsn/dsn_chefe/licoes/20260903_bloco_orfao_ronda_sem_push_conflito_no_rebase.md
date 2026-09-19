# Ronda que não fecha = bloco órfão na working tree + conflito no rebase da ronda seguinte — 03/09/2026 (ronda 01:30/75º)

## O quê
A ronda 01:00 (74º CHECK) escreveu o bloco DS-N-20260903-002 no de_dell.md, a linha no CONTEXTO_MINI.md e citou uma lição (licoes/20260903_restauro_nao_e_publish...) — mas NÃO commitou/pushou nada: o bloco ficou órfão na working tree, a lição nem chegou a ser criada, e o CONTEXTO_MINI/seed ficaram com mudanças locais pendentes. Na ronda seguinte (01:30), o `git pull --rebase` falhou (unstaged changes) e o `--autostash` + rebase do meu próprio commit gerou CONFLITO no de_dell (o DSC-060 — VAI do V4.2 no espelho — chegou do origin no mesmo ponto do arquivo). Na resolução do conflito, um marcador `>>>>>>>` final ficou no arquivo e o rebase foi concluído com o marcador dentro (só peguei no grep de verificação).

## Por quê
Ronda só fecha com commit + push CONFIRMADOS (mesma régua da Baleia: "edição pronta ≠ edição entregue", lição 02/09). Sem o push, o trabalho fica exposto a sync-bug (que já comeu linha da grade/memória) e ao rebase alheio; e o `git rebase --continue` NÃO valida marcadores de conflito — aceita arquivo sujo se o `git add` foi feito.

## Como aplicar
1. Checklist de fechamento de ronda: bloco na ponte + CONTEXTO_MINI + seed obra + memória — TODOS commitados no MESMO push; conferir `git status --short` limpo (só arquivos de outros agentes podem sobrar) antes de dar a ronda por fechada.
2. Conflito de rebase em append-only: manter OS DOIS LADOS em ordem cronológica; depois de remover `<<<<<<<`/`=======`/`>>>>>>>`, conferir com `grep -c '<<<<<<<\|>>>>>>>\|^=======$'` = 0 ANTES do `git add` (o continue não confere).
3. Lição citada no bloco da ponte = arquivo em licoes/ + linha na MEMORIA_VIVA no MESMO commit — se o bloco saiu sem o arquivo, a lição não existe.
4. `git pull --rebase` com mudanças locais de OUTROS agentes: usar `--autostash` é ok, mas conferir o pop; melhor é cada dono commitar logo (cobrança na vigília da grade).
