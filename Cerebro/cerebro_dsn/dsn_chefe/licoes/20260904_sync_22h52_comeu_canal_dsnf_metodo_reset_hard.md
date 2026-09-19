# Lição 2026-09-04 — sync 22:52 comeu o canal do DSN-F (rondas 212-227) + método do reset --hard quando o origin já tem o estado

**Data:** 2026-09-04 ~23:00 BRT (165º CHECK) · **Autor:** DS-N Chefe

## O quê
A abertura da 165ª encontrou o working tree sujo (append do DSN-F ronda 229/230 no canal financeiro, sem commit) e o `git pull --rebase` conflitou 4 commits locais do DS YouTube (`porta-download: X -> BAIXADO`) em `queue_youtube.md` — o MESMO status BAIXADO já existia no origin com sufixo de anotação diferente (52 vs 59 partes "sem_legenda_e_sem_transcricao" na mesma linha). Em vez de resolver rebase 1 a 1 (4 conflitos do mesmo tipo), conferi que o origin já tinha o estado SEMÂNTICO (5× BAIXADO nos 4 vídeos) e fiz `git reset --hard origin/main` + `git stash pop` — os 4 commits locais eram redundantes.

No `stash pop`, o canal financeiro do DSN-F conflitou: o sync `e167775a1` (22:52, "10398 arquivos") tinha REVERTIDO o canal apagando rondas 212-227 (que estavam COMMITADAS às 22:15, commit e07544920). Prova: `git show e167775a1` mostra a deleção das linhas 212-227; o arquivo caiu de 194 linhas-ronda (última 227) para 178 (última 211). Restaurei 212-230 via stash local + commit seletivo ("padrão da casa").

## Por quê
O sync-bug da família DSC-049 (kill-switch SEM o ✓ do Miguel) NÃO está contido: pela primeira vez vi ele reverter um canal de DADOS (financeiro do DSN-F) para um snapshot mais velho, apagando conteúdo já commitado por TERCEIRO (o dono DSN-F) — antes os alvos eram os meus arquivos (VIVA/memória/grade) e o canal dos revisores. Isso reforça a urgência do kill-switch e mostra que a verificação "git log origin mostra sync tocando meus arquivos?" precisa incluir os canais dos OUTROS donos quando eu os tocar.

## Como aplicar
1. Rebase com N conflitos do MESMO tipo em arquivo do vizinho: ANTES de resolver 1 a 1, conferir se o origin já carrega o estado semântico (`git show origin/main:<arquivo> | grep` do status/ID). Se sim, `git reset --hard origin/main` é mais rápido e seguro que rebase (desde que os commits locais sejam redundantes — confirmar 1 a 1 no diff).
2. Stash antes do reset: guardar o working tree do vizinho (DSN-F escreve sem commitar — padrão conhecido) e restaurar com `git stash pop` DEPOIS; conflito no pop = o origin mudou o mesmo arquivo → resolver por UNIÃO cronológica (append-only), nunca descartando lado.
3. Sync que "encolhe" arquivo alheio: provar com `git show <sync> -- <arquivo>` (diff mostra a deleção) e contar linhas-ronda antes/depois (`git show <commit>:$F | grep -c`); restaurar é papel do co-dono do canal quando o dono está offline.
4. Registrar a recorrência como EVIDÊNCIA para o caso DSC-049 (kill-switch) — cada canal novo afetado (agora o financeiro) é um argumento a mais no lembrete ao Miguel.
