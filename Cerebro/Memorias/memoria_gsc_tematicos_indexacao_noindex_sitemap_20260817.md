# Memória — GSC temáticos: diagnóstico de indexação + correções nos 8 repos sites-v4 (17/08/2026)

**Sessão:** ZCode (ZCodeProject) · **Início:** 17/08/2026 07:52 BRT
**Tema Duplo:** fórum `Foruns/forum_gsc_tematicos_indexacao_noindex_sitemap_20260817.md`

---

## 1. Arquivos tocados (8 repos em `Projeto Cafezinho Agentes/sites-v4/`)

| Repo | Arquivo | Mudança | Commit |
|---|---|---|---|
| mundotrilhos | `astro.config.mjs` | filtro sitemap (tags/teste/preview) | `d2d3a90` |
| | `src/components/BaseHead.astro` | prop `noindex` + meta condicional (removeu comentário "SEO defense pre-launch Sprint 0b" — era a prova do noindex histórico) | |
| | `src/pages/tags/[tag].astro` | `<BaseHead … noindex />` | |
| railpost | idem | idem | `7f0622a` |
| discoverbrazil | idem | idem | `7f0718c` |
| mapario | idem | idem | `b90c63e` |
| globalsouth | `astro.config.mjs` + `[tag].astro` | filtro + noindex (BaseHead já tinha prop noindex; removida meta redundante inserida por script) | `8fc1bb1` |
| aiatolah | `astro.config.mjs` | filtro (teste/preview) — sem tags no repo | `8aa9601` |
| ceara | `astro.config.mjs` + BaseHead + `[tag].astro` | filtro + noindex | `8cc1b01` |
| riocarta | `astro.config.mjs` | filtro + senadores/prefeituras | `0344ea9` |
| | `src/pages/blog/[...slug].astro` | `prerender=false`→`true` + `getStaticPaths()` (props por página) | |
| | `src/components/BaseHead.astro`, `[tag].astro` | noindex | |
| | `src/content/blog/__trashed.md` | **removido** (git rm — post legado WP 2023 com slug `__trashed`, draft:false, público) | |

## 2. Comandos-chave e provas

- Varredura de 2.055 URLs dos 4 sitemaps (xargs -P 20): único NOINDEX vivo = `aiatolah.com/teste/`; STATUS_000 da varredura paralela = falso positivo (re-teste serial 200 OK — não usar >15 concorrências).
- Builds locais de validação: `npm run build` nos 8 (todos exit 0).
- Contagens antes→depois: MT sitemap 586→204 (0 tags; tag page `noindex,follow` no dist) · railpost 570→188 · discoverbrazil 504→110 · mapario 178→44 · globalsouth →143 · aiatolah 395→393 · ceara 18→16 · riocarta 1.104 (1.043 preview/0 blog) → 2.862 (2.809 blog/0 preview).
- Push: `git push origin HEAD` nos 8 — GitHub→Vercel auto-deploy.

## 3. Lições

1. **Filtro do @astrojs/sitemap** recebe URL completo (string); usar `new URL(page).pathname` + regex por segmento. Segmento `teste` não pega `teste-header-novo` — precisa `(teste)(\/|-)`. Cuidado com falso positivo (`testes` ≠ `teste` — regex com `(\/|$)` não casa).
2. **Adapters mudam o caminho do dist**: com `@astrojs/vercel`, o sitemap vai para `.vercel/output/static/` (não `dist/`). `dist/client` existe mas o canônico é o `.vercel/output`.
3. **`grep -c` conta LINHAS**: sitemap minificado (1 linha com milhares de `<loc>`) exige `grep -o | wc -l`.
4. **`__trashed` no content collection**: pipeline WP importa posts arquivados como `__trashed.md` com `draft:false` → vão pro site/sitemap. Filtrar `!draft` NÃO pega (não tem o campo). Conferir `id`/slug ao auditar collections.
5. **SSR silencioso**: blog com `prerender=false` (adapter Vercel) não aparece no sitemap — enquanto rascunhos com `getStaticPaths()` (estáticos) sim. Exatamente o oposto do desejado no riocarta.
6. **noindex histórico do GSC**: o estado "Excluída pela tag noindex" persiste no relatório até o Google RE-rastrear as URLs antigas — as páginas vivas estavam todas `index,follow` desde a abertura pós-launch (comentário "SEO defense pre-launch (Sprint 0b 2026-05-16)" no BaseHead confirma). "Validar correção" no GSC acelera.

## 4. Pendências (ver fórum §4)

- GSC "Validar correção" (Miguel) · ceara.digital SPA (prerender dos artigos) · redirects apex↔www (aiatolah/mapario/ceara) · reavaliar "Detectada não indexada" em ~2 semanas.
