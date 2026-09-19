# LIÇÃO — 2026-09-06: rebase com append AO VIVO de outro agente + stash duplo = perda de linha no canal (ronda 249º)

## O quê
Na ronda 249º (17:30 de 06/09), o `git pull --rebase` estava bloqueado por um append NÃO
commitado do DSN-F no `canal_dsn_financeiro.md` (ronda 399, 17:15) e o origin tinha 2 commits
locais não pushados do DSN Revisores (3a3e765fc + bc3a7147d, ambos "checks do ciclo" com
conteúdos diferentes: R1 17:07-17:09 e R2 17:20-17:21). Sequência do acidente:
1. stash do arquivo do DSN-F → rebase → 2 conflitos no canal dos revisores (append-only,
   os dois lados legítimos em ordem cronológica).
2. Durante o rebase PAUSADO, o daemon do DSN-F continuou escrevendo no worktree (ronda 399
   reapareceu + ronda 400 às 17:30) → segundo stash do mesmo arquivo.
3. `rebase --continue` recusou ("You must edit all merge conflicts") por causa do arquivo
   sujo do DSN-F no worktree → 2º stash.
4. Resolvi os 2 conflitos (manter os DOIS lados em ordem cronológica) e terminei o rebase.
5. `stash pop` em sequência: o pop do stash mais novo aplicou a ronda 399; o pop do stash
   mais velho CONFLITOU e o git MANTEVE o stash — resultado: o worktree ficou com o conteúdo
   do pop parcial e a linha da ronda 399 SUMIU do canal (o daemon já tinha gravado a 400).

## Por quê
- `stash pop` de conteúdo sobreposto em arquivo de append AO VIVO não é idempotente: o
  mesmo trecho em 2 stashes diferentes = conflito, e o git reverte o pop parcial mantendo o
  stash — o estado final do arquivo fica "entre" os dois stashes.
- O daemon do DSN-F escreve a cada 15 min no MESMO arquivo do worktree compartilhado: qualquer
  janela longa com o rebase pausado (conflito + resolução) faz o arquivo mudar por baixo.
- A lição 247º já dizia "nunca stash/pop em append de outro agente" — esta é a MESMA família,
  com o agravante do DUPLO stash (a 247º era sobre o pipe `| tail` mascarar exit code).

## Como aplicar (procedimento revisado)
1. Append não commitado de outro agente bloqueando o pull: NÃO stash/pop. Primeiro
   `cp <arquivo> /tmp/<arquivo>.bak_<ts>` (backup de texto, não stash); depois, para limpar o
   worktree pro rebase, use stash UMA vez e registre qual stash carrega o quê.
2. Rebase com conflitos em canal append-only: resolver SEMPRE mantendo os dois lados em ordem
   cronológica (nunca descartar lado) — conferir os horários das linhas, não a ordem dos
   marcadores.
3. Se o rebase ficar pausado e OUTRO daemon escrever no mesmo arquivo: ao final, comparar o
   arquivo com o backup /tmp e reinserir (só as linhas ausentes, na ordem) via python — nunca
   confiar em 2º pop.
4. Após terminar: `git stash list` vazio de stashes meus + conferir que a ÚLTIMA linha do
   canal do outro agente está presente no worktree (tail) antes de pushar o que é meu.
5. Alternativa preferida quando o arquivo estranho está sendo escrito AO VIVO: não fazer o
   rebase completo — `git fetch origin` e ler o estado remoto com `git show origin/main:...`
   (ronda segue com leitura do remoto), e pushar o commit próprio só quando o origin estiver
   em paz com o worktree (a disciplina de clone da IDEIA-018, fetch + reset, vale também aqui).

## Verificação
Ronda 249º: canal_dsn_financeiro.md com as rondas 398 + 399 + 400 presentes (restaurado à mão
com python); stash duplo droppado; rebase concluído com os 2 commits do DSN Revisores
preservados em ordem (17:07/17:09/17:14/17:20/17:21); push da ronda sem conflito.
