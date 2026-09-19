# Lição 2026-09-06 — `git pull | tail` engole o exit code e o `&&` seguinte roda no meio do rebase

## O quê
Na ronda 247ª (16:30 de 06/09), o `git pull --rebase origin main` estava bloqueado por um arquivo append-only de outro agente (canal DSN-F) com mudança não commitada. Usei a cadeia:
`git stash push -- <arquivo> && git pull --rebase 2>&1 | tail -3 && git stash pop`
O pipeline `git pull ... | tail` devolve o exit code do `tail` (0) mesmo quando o rebase falha com conflito — então o `git stash pop` rodou NO MEIO do rebase em andamento, reaplicou o stash sobre a árvore com conflito e recriou um estado `UU` (unmerged) em arquivo que eu já tinha resolvido e adicionado (canal dos revisores), com marcadores de conflito fantasmas. O `git rebase --continue` passou a recusar com "You must edit all merge conflicts" mesmo com `git ls-files -u` vazio (estado do sequencer inconsistente pelo pop no meio). Removi o lixo com `git checkout HEAD -- <arquivo>` (o conteúdo correto já estava commitado no HEAD do rebase) + drop dos stashes redundantes; o rebase terminou com os 2 picks e o push saiu limpo.

## Por quê
1. `cmd | tail` mascara o exit code real do `cmd` — a cadeia `&&` não sabe que o pull falhou.
2. `git stash pop` durante um rebase em conflito não é seguro: ele tenta aplicar sobre a árvore de merge e pode reintroduzir estágios unmerged em arquivos já resolvidos (conflito fantasma).
3. O padrão da casa para destravar pull com append de outro agente NÃO é stash: é commit seletivo do append do dono com a mensagem padrão "canal X (appends do dono ... — commit seletivo p/ destravar pull, padrao da casa)" — já praticado por DS-N 236ª e outros.

## Como aplicar
- NUNCA pipear git (nem outros comandos cujo exit code decide a cadeia) dentro de `&&`: verificar o exit code (`echo "EXIT:$?"` ou `if ! git pull ...; then ...`) antes de seguir.
- Append não commitado de outro agente que bloqueia o pull → commit seletivo do arquivo dele com a mensagem padrão da casa (git add <arquivo> + commit), nunca stash/pop.
- Se um pop acidental rodar no meio de rebase e criar `UU` fantasma: o HEAD do rebase já contém a resolução correta → `git checkout HEAD -- <arquivo>` + `git add`, depois `git rebase --continue`; drops de stashes só depois de conferir que o conteúdo do dono está no worktree/commit.
- Integridade = conteúdo no arquivo final (grep do marcador do dono), não o caminho bonito.
