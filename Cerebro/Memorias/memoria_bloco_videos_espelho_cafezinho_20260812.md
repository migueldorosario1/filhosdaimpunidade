# Memória — Bloco VÍDEOS no espelho cafezinho.news (12/08/2026)

**Data:** 2026-08-12 · **Autor:** ZCode/GLM-5.2 (Kimi/Qwen 🔴🔴, fallback final) · **Fórum pareado:** `Foruns/forum_bloco_videos_espelho_cafezinho_20260812.md`

---

## Resumo executivo

Criado bloco **"Vídeos"** na home do espelho `cafezinho.news`, alimentado pela categoria **Vídeos (ID 28, term_taxonomy_id 29)**. A categoria foi populada com **107 posts do agente YouTube** (posts `publish` com embed de YouTube no conteúdo, dos últimos 2 meses). Menu **Economia** do canônico confirmado já presente (não mexido). Validação no ar: HTTP 200, PHP lint verde, HTML renderizado mostra o bloco e os vídeos.

## Ambiente

| Item | Valor |
|---|---|
| Espelho | `root@159.65.177.60`, WP `/var/www/cafezinho-news`, tema `ocafezinho-portal` |
| Canônico | `cafezinho-wp` (190.89.239.65:51439), WP `/var/www/ocafezinho` |
| wp-cli (espelho) | `sudo -u www-data wp --path=/var/www/cafezinho-news` |
| wp-cli (canônico) | `sudo -u www-data wp --path=/var/www/ocafezinho` |
| Ruído conhecido | wp-cli cospe PHP Notice + dump de `wp_bs_pagination` no ServerDo; filtrar com `grep -vE` ou `grep -E "^(ID,|[0-9])"` |

## Investigação (antes de agir)

- **Categorias relevantes (espelho = canônico, sincronizadas):**
  - `28` Vídeos (slug `videos`) — count declarado **655**, count **real 4** (fantasma).
  - `20751` Youtube (slug `youtube`) — 17 posts, só de 16–23/06/2026.
  - `43` Economia, `5003` Geopolítica, `79` Cultura, `30` Tecnologia, `22` Política, etc.
- **term_taxonomy_id da cat 28 = 29** (confirmado via post 68999, que tem relação tt_id 29).
- **Posts com "youtube" no conteúdo por mês (2026):** mai=4, jun=59, jul=25, ago=30. Agente ativo.
- **Autores dos posts de vídeo em jul+ago:** 5786 (32), 5470 (19), 5780 (2), 2018 (2).
- **Autor 5470 tem 4.147 posts** — usuário genérico de vários agentes/verticais; **não usar autor como critério**.
- **Cruzamento autor 5470 × cat 28 = 0**; posts de vídeo × cat 28 = 0 (antes da ação).
- **Menu canônico 21062 atual:** Quem somos? + Editorias(Regional▸Ceará/RJ, Política 22, **Economia 43**, Geopolítica 5003, Tecnologia 30). Economia já presente.

## Passos executados

### Passo 1 — Backup (espelho)
```bash
BK=/root/bloco_videos_espelho_20260812
mkdir -p $BK
cp /var/www/cafezinho-news/wp-content/themes/ocafezinho-portal/front-page.php $BK/front-page.php.pre
# SHA 4b781a5979e56ce1e179eb3dc8a9004575283bbcadd0628d5d5f2ee506f2b7a6, 708 linhas
wp db query "SELECT object_id, term_taxonomy_id FROM wp_term_relationships WHERE term_taxonomy_id=29;" > $BK/cat28_relacoes_pre.txt
# 4 relações originais (posts antigos 2015-2017)
```

### Passo 2 — Associar 107 posts à cat 28 (term_taxonomy_id 29)
```sql
INSERT IGNORE INTO wp_term_relationships (object_id, term_taxonomy_id, term_order)
SELECT p.ID, 29, 0 FROM wp_posts p
WHERE p.post_content LIKE '%youtube%'
  AND p.post_status='publish' AND p.post_type='post'
  AND p.post_date >= '2026-06-12';
-- Rows affected: 107
```
Recálculo do count (só publish):
```sql
UPDATE wp_term_taxonomy SET count=(
  SELECT COUNT(*) FROM wp_term_relationships tr
  JOIN wp_posts p ON tr.object_id=p.ID
  WHERE tr.term_taxonomy_id=29 AND p.post_status='publish' AND p.post_type='post'
) WHERE term_taxonomy_id=29;
-- count: 4 → 111
```
`wp cache flush`.

### Passo 3 — Bloco VÍDEOS no front-page.php
Snippet PHP (28 linhas) replicando o bloco Cultura, com `category__in => array(28)` (2×: hero + lista), inserido **antes do separador Cultura** via `awk`:
```awk
{ if ($0 ~ /Cultura \(V4_ESPELHO\)/) { while ((getline line < "/tmp/bloco_videos.php") > 0) print line; close("/tmp/bloco_videos.php") } print }
```
- `front-page.php`: 708 → **736 linhas**.
- `php -l`: **No syntax errors detected**.
- Estrutura do bloco (igual Cultura/Economia/Meio Ambiente/etc.):
  - Separador: `<div class="container-xxl my-4">` com `<img icon-start.svg alt="Vídeos">` + `<h4 class="m-0 text-red">Vídeos</h4>` + linha.
  - `<section class="pb-5">`: hero 1 post (thumbnail large, h2, data) + `<div class="row row-cols-1 row-cols-md-5 g-3 pt-3 border-top">` com 5 posts (h5, data).
  - Usa `$excludes` (array_push) — não repete posts entre blocos.

### Passo 4 — Validação no ar
```bash
wp cache flush; rm -rf wp-content/cache/wp-rocket/* (limpo)
curl home: status=200 size=240597 ttfb=1.51s
grep HTML: "text-red\">Vídeos<" ✅, "alt=\"Vídeos\"" ✅
Títulos presentes: "Trump manda cubano", "Lula reconquista as capitais",
                    "Debate na Band", "Bolsonarista que ameaçou" ✅
section.pb-5: 11 (era 10) ✅
```

## Sync do espelho — análise de durabilidade

- `/root/sync_from_cafezinho.sh`, cron `17 * * * *` (às :17 de cada hora), **delta por `post_modified`** (só posts modificados desde `last_sync`), copia **wp_posts + uploads** do canônico; **NÃO copia tema**.
- **Bloco no front-page.php: persiste** (tema fora do escopo do sync). ✅
- **107 associações: persistem no curto prazo** (posts de jun–ago não entram no delta, pois não são modificados no canônico). Risco: se um dos 107 for editado no canônico, o sync sobrescreve a relação (remove cat 28). Solução definitiva = **portar ao canônico**.

## Parte 2 — Garantia doravante: cat 28 automática (12/08 ~17:48–17:50)

**Ordem Miguel:** *"doravante, certifique-se de que o agente youtube use a categoria Vídeos."*

### Investigação multi-servidor (NYC + Tencent + rio-ag + droplet utilitário)
- `agente_youtube.py` (NYC) = **coletor**; linha 49: `canais_pt = ("opera mundi", "brasil", "revista forum", "tv 247", "icl noticias", "dcm")` — confirma Miguel (publica sobre Revista Fórum, UOL, Opera Mundi).
- Publicador `agente_youtube_publicador.py` (NYC `/root/`), linha 782: `CAT_YOUTUBE_ID = 20751` (AUTH-048, "obrigatória SEMPRE"); categorias `[cat_id, 20751]` — **nunca** cat 28.
- Outras fontes ativas de posts com vídeo: `agente_repetidor_estatal.py` (cron `7 */2`, ativo — log mostra "PUBLICADA AO VIVO ID=265402, Total hoje: 11") + V4 verticals. Posts de vídeo = autor 5786 (`Redator`/`Redação`) e 5470 (4.147 posts, genérico); cat Redação (2403) costuma acompanhar.
- Conclusão: solução robusta cobre **todas as fontes**.

### Solução 1 — mu-plugin no canônico (`/var/www/ocafezinho/wp-content/mu-plugins/cafezinho-auto-cat-videos.php`)
Hook `save_post` (prioridade 20, 3 args): se `post_type=post`, status em {draft,publish,pending,future,private}, não revisão/autosave, e conteúdo bate regex YouTube → adiciona cat 28 preservando existentes. Anti-recursão: `static $rodando`.
```php
preg_match('#(youtube\.com/embed/|youtube-nocookie\.com/embed/|youtu\.be/|youtube\.com/watch\?v=|wp-block-embed-youtube)#i', $content)
```
**Teste (validado):** `wp post create` draft com `<figure wp-block-embed-youtube>...embed/mKYn4jCR3D0...` → categorias resultantes `2403 (Redação) + 28 (Vídeos)`. Post de teste 265405 criado e deletado (`--force`). PHP lint verde.

### Solução 2 — patch publicador (NYC `/root/agente_youtube_publicador.py`)
Backup `.bak_pre_cat_videos_20260812_204937`. Patch (sed, 3 pontos):
```python
CAT_YOUTUBE_ID = 20751
CAT_VIDEOS_ID = 28  # cat Vídeos — ordem Miguel 12/08/26
...
if cat_id:
    post_data["categories"] = [cat_id, CAT_YOUTUBE_ID, CAT_VIDEOS_ID]
else:
    post_data["categories"] = [CAT_YOUTUBE_ID, CAT_VIDEOS_ID]
```
`py_compile` OK. Obs.: o publicador tem cópia no Tencent (`/root/agente_youtube_publicador.py`) — não patcheada (o cafezinho é publicado pelo NYC, canônico do V4).

### Rollback da Parte 2
- mu-plugin: `rm /var/www/ocafezinho/wp-content/mu-plugins/cafezinho-auto-cat-videos.php` (efeito cessa imediatamente; cat 28 já adicionada a posts antigos permanece até remoção manual).
- publicador: `cp /root/agente_youtube_publicador.py.bak_pre_cat_videos_20260812_204937 /root/agente_youtube_publicador.py`.

## Parte 3 — Menu canônico: cat Youtube (20751) como submenu (12/08 ~17:53)

**Ordem Miguel:** *"acrescente a categoria Youtube como submenu".*

### Comando executado (menu 21062, canônico)
```bash
WP='sudo -u www-data wp --path=/var/www/ocafezinho'
$WP menu item add-term 21062 category 20751 --parent-id=263602 --title="Youtube"
# → Success: Menu item added. db_id=265406, position 10 (submenu de Editorias 263602)
```
- Backup PRÉ: `/root/backup_menu_youtube_20260812_175232/menu_21062_items_pre.txt` + `nav_menu_options_pre.json`.
- auto_add conferido vazio antes e depois: `{"0":false,"auto_add":[]}` (regra de ouro mantida).
- Cache: `rocket_clean_domain()` + `wp_cache_flush()` via `wp eval-file` → `CACHE_OK`.
- Validação no ar: `curl https://www.ocafezinho.com/` contém `>Youtube<`; `curl -L /categoria/youtube/` → HTTP 200.

### Estrutura final do menu 21062 (11 itens)
Quem somos?(page 158707) · Editorias(custom) ▸ Regional(4986)▸Ceará(4968)/RJ(1656) · Política(22) · Economia(43) · Geopolítica(5003) · Tecnologia(30) · **Youtube(20751)**.

### Rollback
`$WP menu item delete 265406` (remove o item Youtube; auto_add já está vazio).

## Parte 4 — Menu: cat Vídeos (28) ANTES de Economia (canônico, 12/08 ~18:01)

**Ordem Miguel:** *"botar videos antes de economia".*

### Passos
1. Backup: `/root/backup_menu_videos_20260812_175651/menu_21062_items_pre.txt`.
2. `wp menu item add-term 21062 category 28 --parent-id=263602 --title="Vídeos"` → db_id 265408 (Success).
3. Pegar db_id via meta (query por `_menu_item_object_id=28` no menu 21062) — o `--porcelain` e a query por `post_title="Vídeos"` falharam (acento); meta é confiável.
4. **Reordenação via `menu_order` direto** (SQL UPDATE em wp_posts):
```sql
UPDATE wp_posts SET menu_order=60  WHERE ID=263596; -- Política
UPDATE wp_posts SET menu_order=70  WHERE ID=265408; -- Vídeos (antes de Economia)
UPDATE wp_posts SET menu_order=80  WHERE ID=263597; -- Economia
UPDATE wp_posts SET menu_order=90  WHERE ID=263598; -- Geopolítica
UPDATE wp_posts SET menu_order=100 WHERE ID=263600; -- Tecnologia
UPDATE wp_posts SET menu_order=110 WHERE ID=265406; -- Youtube
```
5. Validação: `curl -sL "https://www.ocafezinho.com/?cb=$(date +%s)"` → dropdown-item mostra `Política → Vídeos → Economia` (hrefs `politica-2/` → `videos/` → `economia/`).

### Lição técnica
Neste servidor (ServerDo), **reordenar menu via `wp menu item update --position=N` é não-determinístico** (renumera os irmãos de forma confusa, agravado pelo notice wp_bs_pagination). **Setar `menu_order` direto via SQL** é determinístico e recomendado. Documentado no `CARTAO_BOLSO_MENU_WP_CAFEZINHO.md`.

### Rollback
Restaurar `menu_order` do backup pré, ou `wp menu item delete 265408` (remove Vídeos) + reordenar.

## Comandos de rollback

```bash
# 1. Restaurar front-page.php
cp /root/bloco_videos_espelho_20260812/front-page.php.pre \
   /var/www/cafezinho-news/wp-content/themes/ocafezinho-portal/front-page.php
# 2. Desassociar os 107 da cat 28
wp db query "DELETE FROM wp_term_relationships WHERE term_taxonomy_id=29 AND object_id IN (SELECT ID FROM wp_posts WHERE post_content LIKE '%youtube%' AND post_status='publish' AND post_type='post' AND post_date>='2026-06-12');"
# 3. Recalcular count + flush
```

## Aprendizados

1. **Count de categoria pode ser fantasma** — sempre cruzar `wp_term_taxonomy.count` com `COUNT(*)` real em `wp_term_relationships` antes de confiar.
2. **Autor WP genérico** (5470 com 4.147 posts) não identifica pipeline; preferir critério de conteúdo (embed) ou categoria específica.
3. **Blocos da home do tema `ocafezinho-portal`** = `<section class="pb-5">` com `WP_Query(category__in, post__not_in=$excludes)`; padrão replicável (já usado por Cultura/Economia/Meio Ambiente/Saúde/Esporte).
4. **Heredoc aninhado via SSH** (`ssh host 'bash -s' << 'REMOTE'` contendo `cat > f << 'SNIPPET'`) funciona para injetar PHP sem expansão de `$` — útil para editar tema remoto.

## Pendências Miguel

- Validar visualmente o bloco no espelho (`cafezinho.news`, hard refresh).
- Autorizar **port ao canônico** + definir posição final (hoje: após Tecnologia, antes de Cultura).
- Decidir se quer manutenção automática: associar novos posts de vídeo à cat 28 (hoje é manual/pontual).
