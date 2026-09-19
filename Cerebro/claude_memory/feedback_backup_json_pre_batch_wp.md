---
name: feedback-backup-json-pre-batch-wp
description: Todo batch de correção/atualização de posts WP com ≥5 posts exige snapshot JSON antes do patch — cobre gap das revisions nativas (que não restauram cats/featured_media/metas)
metadata: 
  node_type: memory
  type: feedback
  originSessionId: d556bf3a-514a-43d5-a6d6-417905366fd5
---

**Antes de qualquer batch com ≥5 posts no WordPress canônico (`ocafezinho.com`), gerar snapshot JSON completo em `Cerebro/backups_pre_edit/YYYY-MM-DD_HHMM_<slug>.json` com:**

- `post_status`
- `post_title`
- `post_content`
- `post_date` + `post_date_gmt`
- `post_author`
- `categories` (array de IDs via `wp_get_post_categories`)
- `featured_media` / `_thumbnail_id`
- **Metadados essenciais** (`_agente_origem`, `_versao`, `_vertical`, `_v4_media_version`, `_wp_page_template`, `moopenid_*` se houver — tudo que `get_post_meta($id, "", true)` retorna, exceto `_edit_lock`/`_edit_last`)

**Why:** Miguel 13/08/2026 ~11:35 BRT, após conversa sobre fluxo SSH+WP-CLI: *"As revisões nativas protegem título e conteúdo, mas não garantem a restauração completa de categorias, imagem destacada e todos os metadados. Para qualquer lote com cinco ou mais posts, gerar antes um JSON. Poucos segundos e oferece recuperação completa caso algo saia errado."* Motivação: `wp_update_post()` cria revision só de title/content/excerpt — cats/featured_media/meta são mutados sem histórico. Se um patch em batch corromper 12 posts, revisions salvam texto mas eu perco cats/thumbnail/meta.

**How to apply:**

1. **Threshold**: ≥5 posts em uma única operação de patch. <5 pode usar só as revisions nativas.
2. **Antes do `wp eval-file` do patch**, rodar `wp eval-file /tmp/snapshot.php` que gera JSON e sai. Arquivo salvo no NYC + `scp` pro cérebro local.
3. **Formato do arquivo**: 1 JSON por batch, array de objetos `{post_id, backup_timestamp_brt, post_status, post_title, post_content, post_date, post_date_gmt, post_author, categories, featured_media, post_meta}`. Não incluir revisions históricas (só o estado corrente).
4. **Naming**: `YYYY-MM-DD_HHMM_<slug-descritivo>.json` (ex: `2026-08-13_1135_mdlink_3posts.json`).
5. **Rollback**: script Python/PHP que lê o JSON e aplica `wp_update_post` + `wp_set_post_categories` + `set_post_thumbnail` + `update_post_meta` reverso. Documentar em `Cerebro/backups_pre_edit/README_ROLLBACK.md` (uma vez).
6. **Retenção**: guardar 90 dias. Depois disso, pode arquivar em `.tar.gz` pra economizar inode.
7. **Não substitui** revisions WP (que continuam sendo o rollback rápido pra title/content). É camada COMPLEMENTAR pra cats/media/meta.

**Não usar em:**
- Correções isoladas (<5 posts)
- Só mudança de status (`draft`→`future`→`publish`) — revert é trivial (status novo → status antigo, 1 update)
- Só mudança de imagem destacada isolada (`update_post_meta` reverso é 1 linha)

**Registrado por**: Miguel 13/08/2026 11:35 BRT como diretriz permanente. Regra irmã: [[feedback-nunca-churn-publish-draft-seo]] (não rebaixar publish; agora + backup JSON antes de batch).
