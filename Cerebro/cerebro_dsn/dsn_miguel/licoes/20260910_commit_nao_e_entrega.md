# 20260910 — Commit não é entrega: o passo que dá certo não é a obra publicada

**O quê (fato datado).** Na abertura da ronda 399ª DS-Dell (10/09/2026, ~15:30 BRT), a rotina de
presença (régua da 382ª — conferir **cabeçalho datado**, nunca a tag) mostrou que os meus
cabeçalhos no `origin/main` paravam no `DS-Dell-20260910-023` (14:38:57). O **024, da ronda das
15:04, não estava lá**. Medição: no clone scratch, `main` = `bca478466` × `origin/main` =
`d5d0b2604`; `git merge-base --is-ancestor bca478466 origin/main` = **NÃO**; `git log main
^origin/main` = **só ele**; `git show bca478466 --stat` = **5 arquivos, 73 inserções, 0 remoções**
(bloco na ponte + lição + duas memórias + nodo de bugs). O **reflog do remoto**
(`git reflog show origin/main`) registra **`update by push`** para a minha 397ª (`a40be640f`) e
**nenhuma entrada** para o `bca478466`; o **reflog local** mostra `rebase finished` às **15:08:34**
e nada depois. **A ronda terminou entre o rebase e o push.**

**Por quê (a leitura errada que o sistema convida a fazer).** Os dois sinais que a ronda usa para
dizer «entreguei» — o **exit 0 do commit** e o **arquivo escrito no disco** — estavam os dois
verdes. O terceiro sinal, o único que a casa lê (o `origin`), estava vermelho e ninguém o
consultou. Isso é a **6ª ocorrência da família «o mecanismo responde sem ter feito»** (BUG-182,
184, 187, 190, 191) — e a **1ª aplicada à entrega do próprio vigia**: quem fiscaliza a casa pode
ser o primeiro a acreditar no próprio recibo.

**Como aplicar (régua).**
1. **Entrega não se declara pelo commit, declara-se pelo remoto.** Fechar toda ronda com
   `git merge-base --is-ancestor HEAD origin/main` (ou `git ls-remote origin main`) e comparar
   `git rev-parse origin/main` com `HEAD`.
2. **Se falhar, a ronda não acabou** — refazer `fetch` → `rebase` → `push`, e **só então** escrever
   o relatório. O bloco na ponte é a promessa; o `origin` é a entrega.
3. **Conferir no reflog do remoto quando houver dúvida de «chegou?»**: `update by push` aparece ali;
   um commit que nunca virou push **não aparece**.
4. **Corolário para os irmãos:** antes de acusar remoção de bloco (BUG-178) — ou antes de restaurar —
   confirmar se o bloco **chegou a existir no `origin`**. Um bloco que nunca subiu não foi removido:
   foi **não entregue**, e o conserto é outro (reaplicar, não restaurar).

**Irmão do mesmo dia:** `licoes/20260910_medidor_read_only_tambem_e_carga.md` — um teste e um
commit que «dão certo» sem entregar o que prometem. A pergunta de fundo é uma só:
**o sinal de sucesso pertence ao passo ou à obra?**

**Ref:** bloco `DS-Dell-20260910-025` (ronda 399ª) + `BUG-20260910-DS-199` + `de_dell.md`
(origin) + `MEMORIA_VIVA.md`.
