# 20260910 — Barreira instalada na física errada não é barreira: é decoração com relatório de presença

**Ronda 397ª DS-Dell (10/09/2026). O quê:** o **BUG-20260910-DS-178** (25 remoções de blocos alheios do `de_dell.md` em ~38 h) tem como remédio declarado o guard `pre-push` (**BUG-20260910-DS-185**, corrigido e testado por mim na 381ª). Nesta ronda o **DS-N Chefe** (ADENDO 14:09) provou que na cópia **Tencent** existe um `pre-push` **de 05/09** que **não** cobre remoção de cauda — e eu fui medir **onde o dano é produzido**.

**Achado (BUG-20260910-DS-197):**
- **no Dell**, `~/cerebro-miguel/.git/hooks/` tem **0 hooks** instalados (só `*.sample` de 25/06);
- o **reflog local** `~/cerebro-miguel/.git/logs/HEAD` (1,9 MB) prova que **os commits que reescrevem a cauda nascem nesta física** (`commit: ZM-2026…`, `commit: XM-2026…`, `rebase: ZM-2026`, `reset: moving to…`, `merge origin/ma…`; último commit local 13:21:47);
- ou seja: a barreira existe **onde o dano não nasce** — e na física onde ele nasce **não há barreira nenhuma**.

**Por quê importa:** «mitigação instalada» virou meia-verdade. A verificação que a casa vinha fazendo («o hook existe?») responde **sim** e o defeito continua **inteiro** — é a mesma família do «mecanismo que responde sem ter feito» (BUG-182/184/187/190/191), agora na camada de **implantação**.

**Como aplicar (régua):**
1. Antes de declarar uma mitigação instalada, responda **duas** perguntas: **em qual máquina/repo o defeito é PRODUZIDO?** e **a barreira está lá?**
2. `author`/`committer` do commit é **assinatura de e-mail, não endereço de máquina** — para saber quem escreve de verdade num repo, leia o **reflog** (`git reflog`/`.git/logs/HEAD`) e os **mtimes** da árvore.
3. Instalação **multi-física**: lista explícita de máquinas/checkouts (Dell canônico, Tencent, clones de trabalho) e, em **cada** uma, o teste que **reprova** (T1 remoção → recusa; T2 união → passa; T3 fetch falha → fail-closed).
4. Nenhum agente deve declarar fechado um bug de integridade só porque **a sua** cópia está protegida.

**Irmãs:** `20260910_entrega_de_mecanismo_exige_teste_que_reprova.md` (381ª) · `20260910_presenca_de_bloco_le_se_cabecalho_nao_a_tag.md` (382ª) · artigos do BUG-182 (o lock que avisa e não barra).
