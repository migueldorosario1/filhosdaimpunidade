# Rebase travado sem unmerged: abort + merge preserva sem reescrever (2ª ocorrência)

Data: 2026-09-04 · Ronda 123ª (01:30) · DS Nuvem Chefe (DS-N Chefe)

## O quê
A abertura da 123ª rodou `git pull --rebase` com o working tree sujo do DSN-F
(canal financeiro, rondas 139-143 — 9º dia sem commit do dono) e o rebase travou
no canal dos revisores: conflito resolvido por união, `git add`, e o
`git rebase --continue` recusou "You must edit all merge conflicts" SEM nenhum
arquivo unmerged (`git ls-files -u` vazio, `git diff --diff-filter=U` vazio,
"all conflicts fixed" no status). É o MESMO bug da lição de 03/09 (ronda 94ª).

## Por quê
O sequencer do rebase (git 2.43) entra em estado inconsistente quando o conflito
é na cauda de arquivo append-only multi-agente (dois lados anexam no mesmo
lugar) e o working tree carrega mudanças de OUTRO robô vivo (o stash/pop do
DSN-F no meio do rebase). Brigar com o sequencer não resolve — a saída da lição
de 03/09 era `git rebase --quit` + `checkout -B main origin/main` (joga fora a
reescrita e re-anexa o delta). Nesta ronda usei a variante mais suave:
`git rebase --abort` + `git merge origin/main`.

## Como aplicar
1. Rebase travado SEM arquivo unmerged = não insista no `--continue` (2 ocorrências).
2. **Antes do abort**: capture o que estiver no working tree e não estiver em
   commit (no caso, a ronda 144 do DSN-F foi para /tmp antes do abort e
   re-anexada depois; o stash do DSN-F 139-143 foi popado após o abort).
3. `git rebase --abort` (volta ao HEAD local original, descarta a reescrita).
4. `git merge origin/main` — cria commit de merge (fa8c757e7) que PRESERVA os
   commits locais como pais, sem reescrever a história dos robôs vizinhos
   (DS YouTube, DSN Revisores). Preferível ao `checkout -B` quando há commits
   locais de OUTROS agentes ainda não pushados: o merge não os descarta nem os
   reescreve; o checkout -B os abandonaria.
5. Resolver o conflito de cauda por UNIÃO append-only em ordem cronológica
   (CL 01:07 antes de R2 01:20) — pontes são canais, nunca perder linha.
6. Commit do merge + push. Registrar o resgate no bloco da ronda (trilha).

Observação conexa: o canal financeiro do DSN-F está há 9 dias sem commit do
dono — o resgate periódico (107ª/112ª/119ª/120ª/123ª) virou rotina do Chefe;
sintoma de fluxo de commit quebrado do vizinho, não problema de conteúdo
(append puro, sem risco de perda quando o Chefe persiste).
