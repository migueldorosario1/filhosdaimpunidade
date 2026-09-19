# Pull bloqueado por arquivos sujos de robô vizinho — como destravar sem pisar no trabalho alheio

Data: 03/09/2026 (2ª ocorrência do dia no meu slot; a 1ª foi na ronda 00:00 com o cron do DSN-F)

## O quê
Na abertura da ronda, `git pull --rebase` falhou com "unstaged changes" em arquivos de OUTRO robô
(canal + relatório do DSN-F, com mtime de segundos antes). O vizinho não estava rodando (lock livre,
sem processo), mas o trabalho dele estava solto na árvore — e o origin tinha 6 commits novos que eu
precisava ler (CL-106, ZM, ds laura).

## Por quê
Este repositório é MULTI-ESCRITOR: robôs locais (DSN-F, YouTube, revisores, eu) committam no mesmo
working tree em horários que se cruzam. Regras da casa proíbem commitar/descartar arquivo alheio
(restauro é do dono). Travado entre as duas regras, o erro seria: (a) `git checkout --` nos arquivos
do vizinho = destruir trabalho; (b) `git add` seletivo dos arquivos dele = commitar em nome alheio;
(c) ficar sem pull = ronda cega.

## Como aplicar
1. Antes de qualquer coisa, checar se o dono está VIVO: lock (`flock -n` no /tmp/<robo>.lock →
   "LIVRE/OCUPADO"), processo (`ps aux | grep`), mtime (segundos atrás = escrevendo AGORA).
2. Dono vivo → NÃO stashar (ele pode commitar por cima; pop conflitaria). Esperar o ciclo dele ou
   ler o origin via `git show origin/main:<arquivo>` (leitura não toca a árvore).
3. Dono morto/sem processo → stash SELETIVO só dos arquivos dele, numa linha só com pull+pop:
   `git stash push -m "r30-bkp" -- <arquivos> && git pull --rebase origin main && git stash pop`.
   Pop imediato restaura o conteúdo exato; verificar `git status` depois (os arquivos voltam "M").
4. `git pull --no-rebase` NÃO resolve quando o merge precisa atualizar árvore suja; o stash seletivo
   sim. Nunca `reset --hard` (a mensagem do git sugere — ignorar).
5. Registrar o procedimento no CHECK (transparência de que o trabalho do vizinho ficou intacto).

## Verificação
Ronda 87º: stash+rebase+pop em ~2s; `git status` pós-pop = exatamente os 2 arquivos do DSN-F de
volta como "M"; o rebase trouxe os 6 commits do origin; nenhuma linha alheia alterada por mim.
