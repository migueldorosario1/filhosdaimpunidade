# Lição 2026-09-10 — O sticky não só infla a contagem: ele inverte o topo da listagem

**O quê.** No mesmo bug (BUG-20260910-DS-191), a 1ª leitura my registrou apenas «a listagem filtrada ganha +1 linha». A leitura de hoje, na torneira WP-CLI read-only, mostrou o dano maior: o post sticky **269021** (publicado em **04/09 12:00**) é **prependado como PRIMEIRA linha** de `wp post list --post_status=publish --posts_per_page=3`, à frente do **269725 (10:18:11)** — e o `count` **não muda** com `--ignore_sticky_posts=1` (79087 nos dois modos).

**Por quê (causa).** `WP_Query` busca os sticky **fora do filtro de status** e os coloca em `$this->posts` **fora de `found_posts`**. Por isso: (a) `count` e `ids` não sofrem; (b) `csv/json/table` sofrem; (c) **a ORDEM também sofre** — o sticky não respeita `post_date` da listagem.

**Como aplicar.**
1. Toda leitura de **topo** («último post publicado», «post mais recente») usa `--ignore_sticky_posts=1` (ou `WP_Query` com `'ignore_sticky_posts' => true`).
2. Contagem/inventário só por `--format=count` ou `--format=ids`; `csv/json/table` **nunca** para contar nem para ordenar.
3. Teste de controle embutido: a soma das linhas do `csv` tem de bater com o `count`; o **269021 fora do filtro é o canário** de que a listagem está distorcida.
4. Não remover o sticky (é editorial): o defeito é do **medidor**, não do post.

**A pergunta de método que faltou na 389ª:** não é «quantas linhas vieram?», é **«qual é a leitura que a casa mais usa?»** — contar é raro, **ler o topo é diário**. Verificar o instrumento exige olhar para o uso mais frequente dele, não para o mais evidente.

**Família:** «o mecanismo responde sem ter feito» — BUG-182 (lock que não barra) · 184 (pré-condição que não pré-condiciona) · 187 (alerta que morre com a causa) · 190 (filtro aceito e ignorado) · **191 (linha injetada fora do filtro e fora da ordem)**.

**Prova:** `sticky_posts=[269021]`; publish listing sem flag = 269021/269725/269722; com `--ignore_sticky_posts=1` = 269725/269722/269678; count = 79087 nos dois. Ronda 390ª DS-Dell, 10/09/2026 10:33 BRT.
