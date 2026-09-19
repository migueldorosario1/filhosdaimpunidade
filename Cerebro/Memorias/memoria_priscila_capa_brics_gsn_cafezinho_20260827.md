# MEMÓRIA — Troca de capa do artigo BRICS da Priscila (GSN EN + Cafezinho PT)

**Data:** 27/08/2026 22:20→22:35 BRT · **Agente:** ZCode/GLM-5.3 (Dell) · **Ordem:** Miguel (chat, ~22:20)
**Fórum:** `Foruns/forum_gsn_colunistas_priscila_20260729.md` (Adendo 3)

## Missão

Trocar a capa do artigo "O discreto charme dos BRICS" (Priscila Miranda, 25/08) pela foto real do painel "Women Leading the Future of the BRICS Creative…" (BRICS India 2026) — arquivo local `Outros/Negocios Priscila/fotos/4N5A0613-compressed.jpg` (5760×3840) — com legenda "Priscila de Miranda, autora do artigo, em evento dos BRICS na Índia (BRICS Wave)" e crédito "Divulgação".

## Execução

### GSN (EN) — repo Astro, NÃO WordPress
- Repo canônico: `Projeto Cafezinho Agentes/sites-v4/globalsouth` (branch main) → GitHub `migueldorosario1/globalsouth-v4` → Vercel (`www.globalsouth.news`).
- Commit **`29e9b7f`**: novo hero `public/hero/the-discreet-charm-of-the-brics-photo.jpg` (1200×675 JPEG 200KB, crop 16:9 do original 3:2 com viés 30% do topo p/ manter rostos; QA visual: 5 rostos completos, banner BRICS legível).
- Frontmatter: `heroImage` novo; `alt` descritivo; **`hero_legenda`** (campo do schema `content.config.ts`, renderizado como `.hero-caption-text` no BlogPost.astro:284-287) = "Priscila de Miranda, author of the article, at a BRICS event in India (BRICS WAVES)"; `hero_credit: "Divulgação"`; `hero_license: "Editorial Use"`; `hero_source_url` removido (handout não linka o próprio site).
- Ilustração IA antiga (`the-discreet-charm-of-the-brics.png`) mantida no repo, apenas desreferenciada.

### Cafezinho (PT) — WP, post 267645
- scp da foto p/ `cafezinho-wp:/tmp/priscila-brics-india.jpg` → `wp media import` (--title/--caption/--alt/--desc, anexada ao post) = **attachment 268047** (arquivos gerados: `priscila-brisc-india-1*.jpg|webp`).
- 1ª tentativa de troca do `_thumbnail_id` BLOQUEADA pelo mu-plugin `cafezinho-protecao-editorial` (post_publicado_por_humano) — resolveu com `export CAFEZINHO_EDITORIAL_HUMAN_OVERRIDE=1` antes do wp-cli (bate com a lição da memória do 423).
- `_thumbnail_id=268047` + `_cafezinho_img_check=ok` (já estava) + `wp_update_post(['ID'=>267645])` (reindex Yoast do og:image) + `rocket_clean_domain()` + `wp_cache_flush()`.

## Provas (ao vivo, 22:32-22:33)

- Cafezinho `https://www.ocafezinho.com/2026/08/25/o-discreto-charme-dos-brics/?nocache=1`: og:image = `.../uploads/2026/08/priscila-brics-india-1-scaled.jpg` (HTTP 200, 801KB); `<figcaption>Priscila de Miranda, autora do artigo, em evento dos BRICS na Índia (BRICS Wave). Foto: Divulgação</figcaption>` presente; srcset responsivo completo (o tema `ocafezinho-portal` renderiza `post_excerpt` do attachment como figcaption — single.php:37-38).
- GSN `https://www.globalsouth.news/blog/the-discreet-charm-of-the-brics/`: HTTP 200 com hero novo + caption "…at a BRICS event in India (BRICS WAVES) — Photo: Divulgação (Editorial Use)"; hero jpg HTTP 200 (200KB).

## Aprendizados / pegadinhas

1. **`globalsouth.news` NÃO é WP** — `/wp-json/*` devolve 403 da borda Vercel (iad1). As vars `GSN_WP_*` em `/root/.env` (NYC) são LEGADAS (as `_DEPRECADA_20260817` do `.env.unificado` confirmam). Qualquer edição GSN = commit no repo Astro.
2. Posts de humano no Cafezinho: TODO wp-cli que mexe no post (até meta de thumbnail) precisa `CAFEZINHO_EDITORIAL_HUMAN_OVERRIDE=1`.
3. Legenda de capa no Cafezinho = `post_excerpt` do attachment (caption do media import), renderizada automaticamente pelo tema.
4. Crop 16:9 de foto de painel: viés ~30% do topo preserva os rostos; conferir visualmente antes de subir.

## Estado

**O que aconteceu:** tudo trocado e provado nos 2 sites. **O que falta:** nada. **Preciso do Miguel:** nada.
