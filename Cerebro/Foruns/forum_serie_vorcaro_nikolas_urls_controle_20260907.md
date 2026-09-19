# Fórum — Série Vorcaro/Nikolas: correção urgente de URLs `controle.ocafezinho.com` nos posts 269245/269246/269247 (07/09/2026)

**Sessão:** ZCode Dell (Kimi K3) · 07/09/2026 ~16:14→16:31 BRT
**Pedido do Miguel (urgente):** os 3 posts da série publicados hoje tinham URLs de imagem apontando para o domínio de administração `controle.ocafezinho.com`, que não pode aparecer em nada público. Corrigir contornando a trava editorial (`HTTP 423 editorial_post_intocavel / post_publicado_por_humano`).

## Decisões / o que foi feito

1. **Caminho escolhido: WP-CLI com override (opção b do pedido).** A trava é o mu-plugin `cafezinho-protecao-editorial.php`, já documentado no Cérebro (OBS-035 do CEREBRO_NODE_BUGS_ATIVOS + lições do DSN-Chefe). O desbloqueio oficial, com ordem explícita do Miguel, é a env `CAFEZINHO_EDITORIAL_HUMAN_OVERRIDE=1` no wp-cli. REST estava fora de cogitação (423 por desenho).
2. **Search-replace global DESCARTADO na hora:** a string `controle.ocafezinho.com` existe no `post_content` de **centenas de posts antigos** (query trouxe de 94268 até 269304). Escopo restrito aos 3 IDs, edição via arquivo (`wp post get > /tmp`, `sed`, `wp post update <id> <arquivo>` com override).
3. **Conteúdo:** 4 ocorrências por post (mapa/cronologia/diagrama, em `<figure>`/`<img>`) → `www.ocafezinho.com`. Banco conferido: **0 ocorrências restantes** nos 3. Texto fora isso intocado (revisado à mão pelo Miguel).
4. **Categorias:** alvo [Política 22 + Nacional 21141]. 269245 já tinha as duas; 269246 e 269247 tinham só Política → Nacional adicionada. REST público confirma `[21141, 22]` nos 3.
5. **Thumbnail 269245:** `_thumbnail_id` 269290 → **269289** (foto Nikolas plenário jul/2024, attachment confirmado). REST confirma `featured_media: 269289`.
6. **Cache:** `rocket_clean_post` ×3 + `rocket_clean_domain()` + `wp_cache_flush()` + `redis-cli FLUSHALL`. Páginas públicas re-lidas com `?nocache=`: imagens servidas de `www` (HTTP 200 nas 12 URLs únicas).
7. **Backups antes de tocar:** `Cerebro/Backups/posts_editados/{269245,269246,269247}_pre_fix_20260907.md` + `269245_thumbnail_pre_fix_20260907.txt` (valor antigo 269290).

## Resposta ao pedido "registrem como se desbloqueia a trava"

Já estava parcialmente no Cérebro (memória wp-cli + lições DSN), mas a OBS-035 não tinha a receita. Ficou registrado como **ATUALIZAÇÃO na OBS-035** (CEREBRO_NODE_BUGS_ATIVOS): desbloqueio = `sudo -u www-data env CAFEZINHO_EDITORIAL_HUMAN_OVERRIDE=1 wp --path=/var/www/ocafezinho ...` (só com ordem do Miguel) + purge em camadas + readback do servidor como prova.

## 🆕 Armadilha nova descoberta nesta sessão

`wp post term add <id> category 21141` **resolve por SLUG, não por ID** — criou uma categoria nova chamada literalmente "21141" (term_id 21230) em vez de vincular a Nacional. Curado na mesma sessão (removida dos posts, deletada, readicionada pelo slug `nacional`). **Receita correta: sempre usar slug (`nacional`) ou `--by=term_id`... atenção: `post term add` não aceita id numérico como id.**

## 🔴 Achado estrutural (fora do escopo, NÃO mexido)

Mesmo após a correção, **toda página pública do site** expõe `https://controle.ocafezinho.com/wp-admin/admin-ajax.php` no JS do plugin **WP Statistics** (`WP_Statistics_Tracker_Object.ajaxUrl`). Causa: `admin_url()` resolve para o vhost `controle` mesmo com `siteurl`/`home` = `www` (filtro/mu-plugin da casa roteia o admin para o domínio de administração). É decisão de arquitetura + exposição que o Miguel disse que "não pode aparecer em nada público" — **precisa de deliberação dele** (mexer mexe no site inteiro, não em 3 posts).

## Estado da missão

- **O que aconteceu:** 3 posts 100% corrigidos e verificados (conteúdo, categorias, thumbnail), cache purgado, provas via wp-cli + REST público + curl nas imagens. Monitor atualizado (linha Kimi K3 ✅).
- **O que falta:** decisão do Miguel sobre a exposição site-wide do `controle` pelo WP Statistics (e, se quiser, varredura dos posts antigos que também têm a string no conteúdo — centenas, de migrações velhas).
- **O que preciso de você (Miguel):** "vai" ou não para o tema estrutural do WP Statistics/admin_url.

**Ref.:** memória irmã `Cerebro/Memorias/memoria_serie_vorcaro_nikolas_urls_controle_20260907.md` · OBS-035 (CEREBRO_NODE_BUGS_ATIVOS) · receita wp-cli `wp-correcao-pontual-post-receita-wpcli-20260907` (memória ZCode).

## Adendo 1 (07/09 ~16:4x, ZCode Kimi K3) — dupla checagem de categorias a pedido do Miguel ("nacional e politica")

Reconferido: os 3 posts estão com **Nacional (21141, slug nacional) + Política (22, slug politica-2)**. Primária Yoast do 269245 = 22 (Política), como estava; 269246/247 sem primária explícita. Página pública expõe `"articleSection":["Nacional","Política"]` no JSON-LD. Arquivos de seção ao vivo: os 3 posts listados tanto em https://www.ocafezinho.com/nacional/ quanto em https://www.ocafezinho.com/politica-2/ (verificado com `?nocache=`).
