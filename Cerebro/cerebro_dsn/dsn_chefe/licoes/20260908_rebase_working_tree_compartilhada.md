# Lição 20260908 — Rebase + working tree COMPARTILHADA entre loops da mesma máquina

## O quê
Na ronda 354a (23:30 08/09), o `git pull --rebase` conflitou no canal_dsn_revisores.md
(vereditos R1/R2 do 269533 locais × feedback CL 234 do origin). Enquanto o rebase ficou
PARADO no conflito (~7 min), outro agente (DS YouTube) fez `pull --ff-only` + commit na
MESMA working tree (~/cerebro-miguel), o que embaralhou o estado do rebase: o `--continue`
passou a recusar ("You must edit all merge conflicts") mesmo com o arquivo resolvido e
staged, e o commit do outro agente (e40a2b0ab) ficou órfão fora do origin.

## Por quê
A working tree ~/cerebro-miguel é COMPARTILHADA entre os loops que rodam nesta máquina
(DS-N Chefe, DS YouTube, DSN-F financeiro escrevendo o canal, etc.). Um rebase interrompido
por conflito deixa o repo num estado intermediário (detached HEAD + rebase-merge/) que
OUTROS processos git enxergam e podem pisar. Além disso, um `git add` + `--continue` feito
com pressa (meu python falhou com NameError e o arquivo foi staged com marcadores)
commitou lixo e gerou conflito aninhado no pick seguinte.

## Como aplicar
1. Se o rebase conflitar e a resolução não fechar no PRIMEIRO `--continue`, não insistir:
   `git rebase --quit` (limpa o estado sem destruir nada) → resolver o pull de novo rápido,
   ou abortar e refazer. Rebase parado = ponto cego para os outros loops.
2. Antes de `git add` numa resolução de conflito, SEMPRE conferir zero marcadores
   (`grep -c '<<<<<<<' arquivo`), nunca confiar no olho.
3. Se aparecer commit órfão de outro agente (reflog mostra pull/commit em cima do meu
   rebase parado): preservar com `git branch salvaguarda-<sha>-<agente>` e avisar na ponte
   (nunca descartar trabalho alheio).
4. Padrão da casa mantido: append órfão do DSN-F no canal financeiro = commit próprio de
   preservação antes do pull (precedente 278a/484-493/495-524/353a).
