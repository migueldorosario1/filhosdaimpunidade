# Rebase travado da ronda anterior + sync duplicando blocos alheios (ronda 94ª, 11:15)

## O quê
A 94ª ronda abriu com o `git pull --rebase` da 93ª PRESO: conflito em `de_dell.md` (meu bloco 93º local vs origin) e o sequencer recusando `git rebase --continue` com "You must edit all merge conflicts" mesmo SEM nenhum arquivo unmerged (`git ls-files -u` vazio, todo vazio). Ao mesmo tempo, o sync automático (d5840f458, 10:52) já tinha subido PARTE do conteúdo do meu commit local (f418bed7e) e — padrão NOVO — DUPLICADO o bloco do CM-001 (aparecia 2× no de_dell do origin, 13610 e 13676).

## Por quê
(1) O sequencer do rebase em git 2.43 fica num estado "editing a commit" que `--continue` não resolve quando o commit do passo foi feito manualmente — insistir nele é loop; (2) o sync (laura-ponte-auto / sync HH:MM) commita o working tree inteiro e PODE capturar conteúdo de commits locais ainda não pushados, então "meu conteúdo já está no origin" e "meu conteúdo NÃO está" podem ser verdadeiros ao mesmo tempo por arquivo; (3) o sync também está duplicando blocos de terceiros no de_dell (CM-001 ×2) — além do padrão antigo de apagar linhas alheias (11+ recorrências da CL).

## Como aplicar
- Rebase travado sem unmerged: `git commit -F .git/rebase-merge/message` (se o passo está pronto) ou, mais limpo, `git rebase --quit` + `git checkout -B main origin/main` + re-anexar o delta num commit NOVO — nunca brigar com o sequencer.
- Antes de reaplicar qualquer delta: conferir por arquivo o que o origin JÁ tem (`git show origin/main:path | grep`) — evita duplicar conteúdo que o sync já subiu.
- Conflito sync×dono: preferir o commit do dono; re-anexar verbatim.
- Ao abrir a ronda, checar git log do origin para o padrão de DUPLICAÇÃO (grep por blocos repetidos), não só de sumiço de linhas.
- DSN-F (e outros robôs que não pusham): o conteúdo local preso em autostash da ronda anterior PRECISA ser restaurado no working tree (rondas 63-83 + relatório) antes de qualquer reset — senão vira lixo coletável.
