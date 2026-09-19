# Fórum — Bloco VÍDEOS no espelho cafezinho.news (12/08/2026)

**Data:** 2026-08-12 · **Autor:** ZCode/GLM-5.2 (Kimi/Qwen 🔴🔴, fallback final) · **Tema:** criar bloco "Vídeos" na home do espelho, com posts do agente YouTube categorizados.  
**Memória técnica pareada:** `Memorias/memoria_bloco_videos_espelho_cafezinho_20260812.md`

---

## 1. Contexto (ordem do Miguel, 12/08)

> "Agora que eu me toquei, tem que fazer um bloco vídeo. Tem que botar categoria economia no menu, no menu lá do canônico. E vamos fazer um bloco vídeo. Faz primeiramente no cafezinho espelho, bloco vídeo. Só com aqueles vídeos do agente YouTube. E ver se a gente tem a categoria vídeos. E se esses posts que são do agente YouTube estão entrando na categoria vídeos. Se não tiver, você vai ter que rastrear todos que a gente publicou nos últimos, sei lá, um mês, dois meses, colocar na categoria vídeo. E aí a gente bota um bloco, que nem tem geopolítica, economia, bota categoria vídeos, só com os vídeos."

## 2. Decisões (fechadas com o Miguel via AskUserQuestion, 12/08)

| Ponto | Decisão |
|---|---|
| **Menu Economia (canônico)** | **MANTER** — já está no menu 21062 (submenu "Editorias", db_id 263597, entre Política e Geopolítica). Header reformado também traz no dropdown. Não mexer. |
| **Categoria de vídeos** | Reaproveitar **Vídeos (ID 28, term_taxonomy_id 29)**. |
| **Rastreamento** | Posts com **embed de YouTube** no conteúdo, últimos **2 meses** (≥ 2026-06-12). |

## 3. Investigação (antes de agir) — achados que mudaram o plano

- **Categoria Vídeos (28) JÁ EXISTIA**, mas o count declarado (655) era **fantasma** (desatualizado de migração antiga): count **real = 4** posts (de 2015–2017). Existe também "Youtube" (ID 20751, 17 posts só de 16–23/06).
- **Agente YouTube = posts com embed de YouTube no conteúdo.** Autores principais em jul+ago: **5786 (32)** e **5470 (19)**. Volume por mês: mai=4, jun=59, jul=25, ago=30. Ou seja, o agente **não parou em junho** — segue ativo.
- **Nenhum** desses posts estava na cat 28 (cruzamento = 0).
- ⚠️ **Autor 5470 tem 4.147 posts** — é usuário WP genérico de vários agentes/verticais (não só YouTube). Por isso o critério correto é **embed de YouTube**, não autor.

## 4. Estado (o que aconteceu — tudo no ESPELHO)

1. **Backup:** `front-page.php` (SHA `4b781a59…`, 708 linhas) + snapshot das 4 relações originais da cat 28 → `/root/bloco_videos_espelho_20260812/`.
2. **Associação:** 107 posts embed-YouTube (publish, ≥2026-06-12) associados à cat 28 via `INSERT IGNORE` em `wp_term_relationships` (term_taxonomy_id 29). count recalculado: **4 → 111**.
3. **Bloco VÍDEOS:** criado no `front-page.php` do tema `ocafezinho-portal` (espelho), replicando o modelo do bloco Cultura (`category__in => array(28)`, 1 hero + 5 na lista). Inserido **antes do separador Cultura** (após Tecnologia). 708 → 736 linhas. **PHP lint verde.**
4. **Validação no ar:** HTTP **200** na home (240 KB, TTFB 1,5s); HTML renderizado mostra `text-red">Vídeos<` (h4) + `alt="Vídeos"` + 4 títulos do agente ("Trump manda cubano…", "Lula reconquista as capitais", "Debate na Band…", "Bolsonarista que ameaçou…"). Total **11** blocos `section.pb-5` (antes 10).

## 5. O que falta / próximos passos

1. **Miguel valida visualmente** no espelho: `https://cafezinho.news/` (hard refresh). Ajustes de posição/estilo sob demanda.
2. **Portar ao canônico** (`ocafezinho.com`) após homologação — é lá que associações + bloco ficam **duráveis** (o espelho é sincronizado DO canônico).
3. **Atenção sync do espelho** (`/root/sync_from_cafezinho.sh`, cron `:17`/hora, delta por `post_modified`, só copia posts + uploads — **não copia tema**):
   - Bloco no `front-page.php`: **persiste** (tema não é sincronizado). ✅
   - 107 associações: **persistem** enquanto esses posts não forem modificados no canônico (posts antigos de jun–ago não entram no delta). ✅ curto prazo.
   - Solução definitiva de durabilidade = portar ao canônico (e o sync passa a propagar a cat 28 de volta ao espelho).

## 5b. Garantia doravante: vídeos sempre na cat 28 (12/08 ~17:48–17:50)

**Ordem Miguel:** *"doravante, certifique-se de que o agente youtube use a categoria Vídeos."* (corrigiu minha leitura inicial: o agente **não** está pausado — publica sobre Revista Fórum, UOL, Opera Mundi).

**Realidade encontrada (investigação multi-servidor NYC + Tencent + rio-ag + droplet utilitário):**
- `agente_youtube.py` (NYC) = **coletor**; patrulha canais YouTube de **Opera Mundi, Revista Fórum, TV 247, ICL Noticias, DCM** (linha 49 — confirma o Miguel). Publicador = `agente_youtube_publicador.py` (camada 4), usava `[cat_id, CAT_YOUTUBE_ID=20751]` — **nunca** cat 28.
- Múltiplas fontes publicam posts com vídeo hoje: `agente_repetidor_estatal.py` (ativo, cron `7 */2`, 11 posts no dia) + V4 verticals + agente YouTube. Ou seja, a solução robusta precisa cobrir **todas as fontes**, não só o agente.

**Solução dupla (defesa em profundidade), no CANÔNICO (`ocafezinho.com`):**
1. **mu-plugin `cafezinho-auto-cat-videos.php`** (`/var/www/ocafezinho/wp-content/mu-plugins/`): hook `save_post` detecta embed YouTube (`youtube.com/embed`, `youtu.be`, `watch?v=`, `wp-block-embed-youtube`, `youtube-nocookie`) e adiciona cat 28 preservando as existentes; anti-recursão via flag `static`. **Testado**: draft c/ embed → ganhou cat 28 automaticamente (post 265405, criado e deletado). Cobre TODA fonte (repetidor, V4, agente YouTube, futuro).
2. **Patch `agente_youtube_publicador.py` (NYC `/root/`)**: adicionado `CAT_VIDEOS_ID = 28` (linha 783); categorias agora `[cat_id, 20751, 28]` ou `[20751, 28]`. py_compile OK. Backup `.bak_pre_cat_videos_20260812_204937`.

**Resultado:** daqui pra frente, **todo post com vídeo do YouTube entra automaticamente na cat Vídeos (28)** — seja qual for o agente que o publicar.

## 6. Rollback

- `front-page.php`: restaurar de `/root/bloco_videos_espelho_20260812/front-page.php.pre`.
- cat 28 (desassociar os 107): `DELETE FROM wp_term_relationships WHERE term_taxonomy_id=29 AND object_id IN (SELECT ID FROM wp_posts WHERE post_content LIKE '%youtube%' AND post_status='publish' AND post_type='post' AND post_date>='2026-06-12');` + recalcular count. Snapshot das 4 relações originais em `/root/bloco_videos_espelho_20260812/cat28_relacoes_pre.txt`.

## 5c. Menu canônico: cat Youtube (20751) como submenu de Editorias (12/08 ~17:53)

**Ordem Miguel:** *"acrescente a categoria Youtube como submenu".*

- **Ação (menu 21062, canônico):** `wp menu item add-term 21062 category 20751 --parent-id=263602 --title="Youtube"` → item db_id 265406, submenu de Editorias (263602), position 10 (após Tecnologia).
- **auto_add** segue vazio `{"0":false,"auto_add":[]}` (regra de ouro do menu, §BUG-20260806-MENU-SPAM-CASSINO-AUTOADD, mantida).
- **Validação:** cache WP Rocket purgado; home renderiza `>Youtube<`; `/categoria/youtube/` HTTP 200.
- **Estrutura atual do menu 21062 (11 itens):** Quem somos? + Editorias ▸ Regional(4986)▸Ceará(4968)/RJ(1656), Política(22), Economia(43), Geopolítica(5003), Tecnologia(30), **Youtube(20751)**.
- **Backup:** `/root/backup_menu_youtube_20260812_175232/`.

## 5d. Menu: cat Vídeos (28) ANTES de Economia (canônico, 12/08 ~18:01)

**Ordem Miguel:** *"botar videos antes de economia".*

- **Ação (menu 21062):** adicionado item "Vídeos" (cat 28, db_id 265408) como submenu de Editorias e posicionado **antes de Economia**.
- **Reordenação via `menu_order` direto** (SQL UPDATE) — lição: o `wp menu item update --position=N` renumera de forma confusa neste servidor (wp-cli cospe notice wp_bs_pagination); setar `menu_order` é determinístico. Ordem final dos filhos de Editorias: Regional(30) · Política(60) · **Vídeos(70)** · Economia(80) · Geopolítica(90) · Tecnologia(100) · Youtube(110).
- **Validação frontend:** dropdown Editorias renderiza `Política → Vídeos → Economia` (hrefs confirmam). auto_add vazio. Cache purgado.
- **Backup:** `/root/backup_menu_videos_20260812_175651/`.

## 5e. PORT ao canônico (ocafezinho.com) — 12/08 ~18:25

**Ordem Miguel:** *"pode levar pro canonico"* + *"não estou vendo no menu, nem no visível (desktop) nem no hamburguer"*.

- **Diagnóstico do "não vejo":** hambúrguer (offcanvas `wp_nav_menu`) **já servia** tudo (cache-buster provou) — era **cache do navegador**. Header desktop dropdown era **HTML estático** sem Vídeos/Youtube.
- **Ação (canônico `/var/www/ocafezinho`):**
  1. `header.php`: dropdown "Editorias" estático atualizado — **Vídeos** (após Política) + **Youtube** (após Tecnologia).
  2. `front-page.php`: bloco **VÍDEOS** inserido antes de `banner-after-recents-desktop` (modelo canônico `col-md-7`+`col-md-5`, `category__in=array(28)`). PHP lint verde.
  3. cat 28 (tt_id 29): **+106 posts** embed-YouTube (≥2026-06-12) → count real **659→765**.
- **Validação:** HTTP 200; cache WP Rocket purgado; HTML mostra bloco + dropdown + hambúrguer.
- **Backup:** `/root/backup_bloco_videos_canonico_20260812_182409/` (header.php + front-page.php pré).
- **Pendência:** Miguel validar no desktop + mobile (hard refresh).

## 5f. UNIFICAÇÃO: cat Youtube (20751) → Vídeos (28) — canônico + NYC, 12/08 ~19:27

**Ordem Miguel:** *"vídeos youtube é a mesma coisa, unifica as categorias... tudo que tem categoria youtube entra na categoria vídeos... remove categoria youtube, remove do menu, deixe categoria vídeos"*.

- **Posts:** 19 da cat 20751 (17 já tinham 28; +2 migrados via INSERT IGNORE); `DELETE` relações tt_id 20751. **cat 20751=0, cat 28=767.**
- **Menu 21062:** item Youtube (db_id 265406) deletado.
- **header.php:** linha `<li>.../youtube/` removida do dropdown (preg_replace). Lint verde.
- **`agente_youtube_publicador.py` (NYC):** `CAT_YOUTUBE_ID=20751` aposentada; categorias `[cat_id, CAT_VIDEOS_ID]` / `[CAT_VIDEOS_ID]` (só 28). py_compile OK. Backup `.bak_pre_unifica_videos_20260812_222635`.
- **Validação:** HTTP 200; HTML Youtube=0 (offcanvas+dropdown); Vídeos permanece.
- **Backups:** canônico `/root/backup_unifica_videos_20260812_192503/`.
- **Cat 20751 (term):** mantida vazia no WP (não excluída — Miguel decide). mu-plugin já só usa 28.
- **Pendência:** replicar no espelho (ainda tem cat 20751 com 17 posts + item menu) se Miguel quiser; ou excluir term 20751.

## 7. Pendência Miguel

- Validar visualmente o bloco no espelho.
- Autorizar o **port ao canônico** (e se quer a mesma posição — após Tecnologia, antes de Cultura — ou outra).
