# ☕ Fórum Moka Reader — 2026-07-21 — V 1.3.6 "Capa cabe na tela"

> Nodo de índice (Camada 2): `CEREBRO_INDEX_MOKA_LOG.md`.
> Continuação da sprint de 2026-07-20 (`forum_moka_reader_20260720.md`).

## Caso
Miguel reportou que o livro **"The New China Playbook" (Keyu Jin, Viking/PRH)**
abriu com a **capa gigante** no mokareader.com, sem como diminuir
(https://www.mokareader.com/book/bmru1rbqbuhx1).

## Diagnóstico (causa raiz no Moka, não no EPUB)
- O EPUB é saudável (reflowable, fontes em `em`, sem DRM). Capa de 1522×2298px.
- O parser (`packages/parser/src/epub.ts`) emite blocos `type: "image"` e o
  `Reader.tsx` renderiza `<img>` puro — **não existia nenhuma regra CSS para
  `.reader-text img`** em `globals.css`. A imagem renderizava no tamanho natural.
- O zoom A−/A+ (V 1.3.5) só escala `font-size` — por isso "não dava pra diminuir".

## Correção (commit `2e08b7b`, branch main)
`apps/web/src/app/globals.css` — nova regra:
```css
.reader-text img {
  display: block;
  max-width: 100%;
  max-height: 62vh; /* deixa espaço pro header e pra barra de navegação */
  width: auto; height: auto;
  object-fit: contain;
  margin: 0.5em auto 1.1em;
}
```
Vale pra **qualquer EPUB** (capa, folha de rosto, figuras) — não é patch por livro.

## Deploy (política cumprida)
1. Backup pré-deploy: `backups/moka_V1.3.5_producao_DEPLOYADO_2026-07-21_0811.zip`
   (git archive do main `a65049f`).
2. `npm run build` ✓ → commit → push → auto-deploy Vercel projeto `moka`.
3. Deployment `moka-cbdshlohb-…vercel.app` **Ready** → www.mokareader.com.
4. Health: 3× HTTP 200 + /ajuda 200. CSS de produção contém a regra nova
   (`object-fit:contain`, `62vh`) — verificado no bundle `c2c30b564e5749f7.css`.
5. `MANIFESTO_ROLLBACK.md` atualizado (V 1.3.6 ATUAL; rollback V 1.3.5).

## Nota
Também foi gerado (a pedido, antes de achar a causa no Moka) um EPUB patcheado
em `~/Downloads/.../livros baixados novos/moka/The New China Playbook (FIX capa).epub`
— virou desnecessário com a correção no reader, mas não atrapalha.

---

## Update 2026-07-21 — V 1.3.7 "seleção não escorrega no começo do parágrafo"

**Caso:** Miguel (iPhone/iPad): ao selecionar desde o começo de um parágrafo
EPUB, a seleção "escorrega" e **começa na linha de baixo**. Sempre no começo
de parágrafo.

**Causa raiz (2 camadas):**
1. **CSS/hit-testing iOS:** o espaço entre parágrafos era `margin-bottom`
   (vão "sem dono"). Um toque nesse vão ancora a seleção no fim do parágrafo
   anterior; ao arrastar, a seleção efetivamente começa na 2ª linha do
   parágrafo-alvo. Agravado por `line-height: 1.85` (meia-leading generosa).
   O PDF já tinha um "anti-pulo" (`endOfContent`); o EPUB não tinha nada.
2. **UX:** não havia como corrigir a âncora sem brigar com a alça do iOS.

**Correção (commit `d7c6acc`, 3 arquivos):**
- `globals.css`: `.reader-text p { margin: 0 }` + `.reader-text p + p {
  padding-top: 1.1em }` — o vão passa a pertencer ao parágrafo SEGUINTE, e o
  toque nele ancora no INÍCIO da 1ª linha. Espaçamento visual idêntico.
- `Reader.tsx`: novo botão **¶** no menu de seleção
  (`expandSelectionToParagraph`) — expande a seleção pro(s) parágrafo(s)
  inteiro(s) tocados; correção determinística.
- `ui-strings.ts`: chave `reader_sel_paragraph` × 12 idiomas.

**Deploy:** backup `moka_V1.3.6_producao_DEPLOYADO_2026-07-21_0915.zip` →
build ✓ → push → deployment `moka-jju314pnt` Ready → www 3× HTTP 200 →
CSS de produção com `p+p{padding-top:1.1em}` (e `62vh` da V 1.3.6) ✓.
Manifesto de rollback atualizado (V 1.3.7 ATUAL; rollback V 1.3.6).

**Pendência:** validação do Miguel no aparelho (o hit-testing do iOS só se
confirma com o dedo). Se ainda escorregar, próximo passo é reduzir a
`line-height` de 1.85 ou estudar `::first-line` com padding negativa.

---

## Update 2026-07-21 — V 1.3.8 "assistente anti-escorregão"

**Feedback do Miguel (iPad):** mesmo após a V 1.3.7, ainda escorrega —
mas agora com sintoma mais preciso: **a 1ª palavra ancora bem; ao
ESTENDER a seleção, a alça escorrega pro começo da palavra 2 ou pra
linha seguinte.**

**Diagnóstico refinado:** o padding-top da V 1.3.7 corrigiu o toque no
vão entre parágrafos, mas NÃO muda a física da alça do iOS: com
`line-height: 1.85`, a faixa ambígua entre linhas é grande e, ao
arrastar a alça de início, o WebKit re-ancora no começo da palavra 2
(ou da linha 2). Mexer na seleção DURANTE o arraste não é opção —
quebra a alça do iOS (comentário já existente no código).

**Correção (commit `7f79019`):** assistente pós-gesto — listener de
`touchend`/`mouseup` (com 60ms de atraso pra seleção assentar): se só
a 1ª palavra do parágrafo ficou de fora da seleção (`/^\S+\s+$/`),
estica o início de volta pro começo do parágrafo e reabre o menu.
Trade-off documentado: quem quiser começar deliberadamente na 2ª
palavra ainda pode re-arrastar (raro) ou usar o botão ¶.

**Deploy:** backup `moka_V1.3.7_producao_DEPLOYADO_2026-07-21_1039.zip`
→ build ✓ → push → deployment `moka-serjmdytd` Ready → www 3× 200.
Manifesto atualizado (V 1.3.8 ATUAL; rollback V 1.3.7).

**Pendência:** validação do Miguel no iPad. Se persistir: considerar
`line-height` configurável (1.85 → opção 1.6) pra diminuir a faixa
ambígua, ou seleção por toque-longa-arraste estilo Apple Books
(custom, sem alças nativas).

---

## Update 2026-07-21 — V 1.3.9 "duas assinaturas de deslize + botão ⇤"

**Feedback do Miguel:** "ainda escorrega na primeira palavra". Verificado
que o assistente da V 1.3.8 ESTAVA no ar (regex achada no bundle de
produção) — ou seja, havia assinatura de deslize não coberta.

**Refinamento:** o iOS tem (pelo menos) DUAS formas de errar a âncora no
começo do parágrafo: (1) começo da palavra 2 — coberta na 1.3.8;
(2) FIM do parágrafo anterior (arraste pro vão) — não coberta. A (2) é
segura de corrigir: do bloco anterior nada foi selecionado, então mover
o início pro começo do próximo bloco não perde texto.

**Entregue (commit `a08b752`):**
- Assistente cobre o caso 2 (âncora no fim do parágrafo anterior com a
  seleção seguindo pro bloco seguinte → move o início).
- Novo botão **⇤** no menu de seleção (`snapSelectionStartToParagraph`):
  move o INÍCIO da seleção pro começo do parágrafo mantendo o fim —
  correção 100% determinística, sem heurística. Trio de recuperação no
  menu: ⇤ (começo) + ¶ (parágrafo inteiro) + toque duplo.
- i18n `reader_sel_from_start` × 12 idiomas.

**Deploy:** backup `moka_V1.3.8_…zip` → build ✓ → push → deployment
`moka-5msv97sbw` Ready → www 3× 200 → bundle com `from_start` ✓.
Manifesto atualizado. **Pendente:** validação do Miguel (fechar e
reabrir o app pro SW atualizar).
