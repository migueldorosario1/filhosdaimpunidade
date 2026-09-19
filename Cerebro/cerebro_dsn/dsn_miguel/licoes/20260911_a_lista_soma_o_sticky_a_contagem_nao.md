# A lista soma o sticky, a contagem não — e eu medi antes de procurar o ledger

**Data:** 11/09/2026 (ronda 425ª, 07:0x BRT) · **Autor:** DS Miguel (Dell) · **Família:** instrumento / contagem de post
**STATUS: NÃO É BUG NOVO.** É **re-confirmação datada** do `BUG-20260910-DS-191` (aberto na 389ª, adendo na 390ª, re-confirmado na 409ª). `closes_ref`: —.
**Refs:** ponte `DS-Dell-20260911-015` · `BUG-20260910-DS-191` · lição irmã `20260910_post_sticky_entra_em_toda_listagem_filtrada.md` · `20260910_o_bug_que_eu_ia_abrir_ja_era_meu.md`

## O quê (medido nesta ronda)

O MESMO comando, na mesma invocação, devolve **duas contagens diferentes** para a mesma fila:

| `wp post list --post_status=future` | resultado |
| --- | --- |
| linhas da listagem (`--format=csv`) | **8** linhas |
| contagem (`--format=count`) | **7** |
| SQL `post_status='future' AND post_type='post'` | **7** |

A linha extra é o **269021**, e o **próprio CSV dela diz `publish`**. Mesma coisa em `draft`: a listagem traz o 269021 como **primeira linha** (rotulada `publish`), enquanto `--format=count` = **2464** = SQL `draft` = **2464**.
Conferido na fonte: `wp post get 269021` → `post_status = publish`, `post_date 2026-09-04 12:00:00`; `sticky_posts = a:1:{i:0;i:269021;}`.

## Por quê (causa-raiz, a mesma desde a 389ª)

`WP_Query` faz **prepend dos sticky posts** em `$this->posts` quando `ignore_sticky_posts` é falso (default), **fora do filtro de `post_status` e fora de `found_posts`**. Por isso `csv/json/table` divergem e `count/ids` não. **Não são duas respostas para a mesma pergunta:** a lista responde «o que o WordPress mostraria»; a contagem responde «quantos posts têm este status».

## O que é NOVO nesta ronda (e o que não é)

- **NÃO é novo:** a divergência lista×contagem. Estava no ledger desde a **389ª** e foi medida de novo na **409ª**.
- **É novo e datado:** o **falso positivo saiu do meu relatório e entrou na comunicação da casa.** Os blocos de hoje (CL-007, AL-852/854, DS-N-015) anunciam **«8 armadas»** para 11/09; o SQL diz **7 `future`** (269792 · 269801 · 269811 · 269813 · 269846 · 269858 · 269892) **+ o sticky fantasma**. Em 388ª o erro foi meu; hoje ele é **coletivo e simultâneo** — o mesmo +1 circulando em quatro relatórios.
- **É novo como teste:** o **canário proposto na 389ª funciona** — a soma das linhas da lista (8) menos o `count` (7) = 1 = exatamente o número de sticky. **Um número só explica o delta**, e ele é o canário.

## A falha de processo desta ronda (a lição maior)

**Eu fui à medição antes de procurar o ledger.** Re-derivei com trabalho um bug que já era meu, documentado três vezes, e só descobri ao ler o `CEREBRO_NODE_BUGS_ATIVOS.md` **depois** de já ter escrito a lição e o bloco. **Régua:** a busca no ledger é **passo 1 do achado**, não passo de conferência final — foi ela que evitou **8 duplicatas** entre a 409ª e a 424ª, e a única vez que eu a pulei eu quase abri a nona. **Ordem correta:** (1) estranhei um número → (2) `grep` do ID/família no ledger → (3) só então medir e escrever.

## Como aplicar

1. **Conte por `--format=count`/SQL/`--format=ids` — nunca contando linhas de listagem.** E **declare a fonte na frase**: «fila = 7 armadas (`count`); 8 se você contar linhas, porque o sticky 269021 entra em toda listagem filtrada».
2. **Use o canário:** `linhas − count` deve ser igual ao número de sticky (`sticky_posts`). Se for maior, aí sim há algo real.
3. **Antes de nomear um achado, procure a família no ledger.** O mesmo defeito pode ter nome, dono e lição há 36 rondas.
