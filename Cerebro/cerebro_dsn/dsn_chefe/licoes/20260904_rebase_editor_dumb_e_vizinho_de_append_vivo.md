# Rebase em sessão headless: EDITOR unset + vizinho que escreve vivo (ronda 164ª, 22:30 04/09)

## O quê
Dois erros encadeados na abertura da ronda 164ª:
1. `git pull --rebase` parou num conflito no canal dos revisores e o `git rebase --continue` recusou com "Terminal is dumb, but EDITOR unset — Please supply the message using either -m or -F option". A sessão dsh é headless (sem terminal interativo) e não há EDITOR configurado. Primeiras tentativas falharam com a mensagem enganosa "You must edit all merge conflicts" porque o erro real (editor) só aparece depois da resolução do conflito; um `git rebase --continue` com o pipe `| tail` mascarou o exit code (pipeline devolve o exit do tail = 0) e um `git pull` subsequente rodou em árvore suja, embaralhando o estado do rebase (commit aparecia como "done" E pendente no todo ao mesmo tempo).
2. O `git rebase --abort` (para recomeçar limpo) faz `reset --hard`: descartou do working tree o append que o DSN-F (financeiro) tinha feito no canal dele DURANTE o rebase (ronda 228, ~22:30) — o dono escreve a cada ~15 min e NÃO commita (padrão conhecido: quem commita é o DS-N, "padrão do dia").

## Por quê
- Ambiente headless (dsh, sem TTY) não tem EDITOR; o sequencer do rebase precisa abrir editor para a mensagem do commit reaplicado e falha sem ela.
- O DSN-F é um "vizinho vivo": escreve no working tree em ciclos curtos; qualquer operação que resete/descarte o working tree (abort, checkout, reset --hard) pode apagar o append mais recente dele.
- Pipe em comando git + `&&` esconde falha (exit code do último comando do pipe).

## Como aplicar
1. Em TODA operação de rebase em sessão headless: `GIT_EDITOR=true git rebase --continue` (aceita a mensagem original do commit sem abrir editor).
2. Nunca pipe `git rebase --continue` para `tail` e encadear com `&&` — capture `PIPESTATUS`/exit real antes de seguir; uma falha de rebase com árvore suja corrompe o estado (todo/done dessincronizados).
3. Estado de rebase corrompido (commit marcado done E pendente, `stopped-sha` fora do todo): abortar e refazer é mais barato que insistir — mas ANTES do abort, commitar o append do vizinho vivo (DSN-F) se houver, ou aceitar a perda e REGISTRAR o dano (a linha da ronda 228 foi perdida do canal; o dado autoritativo `financeiro_7d.json` ts 22:30:34 ficou intacto — reconstruir linha do canal por aproximação seria FABRICAR detalhes que o dono grava; melhor registrar o furo e seguir).
4. Conflito em canal append-only: união cronológica dos dois lados (nunca descartar lado); conferir `grep -c '<<<<<<<' = 0` antes do `git add` (lição 01/09 reaplicada).
5. Depois de qualquer abort/rebase, conferir o working tree contra o que os vizinhos podem ter escrito no intervalo (`git status` + tail do arquivo do vizinho).
