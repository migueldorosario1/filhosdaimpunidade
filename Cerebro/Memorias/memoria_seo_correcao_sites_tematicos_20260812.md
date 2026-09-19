# Memória técnica — Correção SEO dos 8 sites temáticos

**Data:** 2026-08-12 (~22:40→23:30 BRT)
**Agente:** ZCode (GLM-5.2 Z.ai)
**Par de Tema Duplo:** `Foruns/forum_seo_correcao_sites_tematicos_20260812.md` (decisões resumidas — ler primeiro).

## Ambiente

- Repos canônicos: `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/sites-v4/{riocarta,mapario,aiatolah,globalsouth,mundotrilhos,railpost,discoverbrazil,ceara}`.
- Stack: Astro + `@astrojs/sitemap` + `@astrojs/mdx` (+ `@astrojs/vercel` adapter nos que têm SSR/server). Deploy Vercel.
- Node v22.22.2, npm 10.9.7. `dist/` e `.vercel` gitignored.

## Comandos / artefatos exatos

### Canonical www (3 configs)
```
mundotrilhos/astro.config.mjs:  site: 'https://mundotrilhos.com'   → 'https://www.mundotrilhos.com'
railpost/astro.config.mjs:      site: 'https://railpost.news'      → 'https://www.railpost.news'
discoverbrazil/astro.config.mjs: site: 'https://discoverbrazil.news' → 'https://www.discoverbrazil.news'
```
Prova: redirecionamento não-www→www (mundotrilhos 307, railpost 308, globalsouth/riocarta/discoverbrazil 307) confirmou www como canônico.

### robots.txt (8× novo, `public/robots.txt`)
```
User-agent: *
Allow: /

Sitemap: https://<www-site>/sitemap-index.xml
```
URLs: www.riocarta.com · mapario.com.br · www.globalsouth.news · www.mundotrilhos.com · www.railpost.news · www.discoverbrazil.news · ceara.digital · www.aiatolah.com.

### lang (4 arquivos)
- `riocarta/src/pages/index.astro`: `<html lang="en">` → `<html lang="pt-BR">`
- `mundotrilhos/src/pages/index.astro`: idem
- `ceara/src/pages/index.astro`: idem
- `mapario/src/layouts/BlogPost.astro`: `<html lang="en">` → `<html lang="pt-BR">` (posts PT estavam com lang en)
- (mundotrilhos BlogPost já era dinâmico `Astro.props.lang ?? 'pt-br'`; riocarta/ceara BlogPost já `pt-BR`)

### JSON-LD NewsArticle (5×, bloco antes de `</head>` no BlogPost / `<main>` no PostLayout)
Schema: `@context schema.org`, `@type NewsArticle`, headline=title, image=heroImage (absoluta www), datePublished=pubDate.toISOString(), dateModified=updatedDate??pubDate, author/publisher Organization (name+url do site), logo `/favicon.png` (ou `/favicon.svg` Aiatolah). Publisher por site: Mapa Rio, Mundo Trilhos, Rail Post, Discover Brazil, Aiatolah News. Fonte do bloco: cópia fiel do `ceara/src/layouts/BlogPost.astro` (já tinha).

### Aiatolah (caso especial — template próprio i18n)
- `npm install @astrojs/sitemap` → `@astrojs/sitemap@^3.7.3` em package.json.
- `astro.config.mjs`: `defineConfig({})` → `defineConfig({ site:'https://www.aiatolah.com', integrations:[sitemap()] })`.
- `src/layouts/Layout.astro`: adicionado `canonicalURL` (via `Astro.site`) + `<link rel="canonical">`; hreflang e imageURL `aiatolah.com`→`www.aiatolah.com`.
- `src/layouts/PostLayout.astro`: JSON-LD NewsArticle em `<main>` (Google aceita no body), com `inLanguage: lang`.
- Nota: o `Layout.astro` já era bom (lang dinâmico pt-br/en, hreflang, OG); faltava canonical + sitemap + JSON-LD.

## Validação (build local antes do deploy)
- `npm run build` em todos os 8: ✓. Páginas: mundotrilhos 541, globalsouth 565, railpost 565/525, discoverbrazil 440, mapario 169, ceara OK, riocarta 112s (3849 posts), aiatolah 363.
- No `dist` confirmado: sitemap-0.xml com `<loc>https://www.<site>/...</loc>`, robots.txt copiado, JSON-LD `NewsArticle` renderizado em `dist/blog/<slug>/index.html` (teste: `python3 -c "import re; ..."`).

## Deploy
- 7 sites: `git add` (arq. específicos) → commit "SEO Google: ..." → `git pull --rebase origin main` → `git push origin main`. HEAD==origin. Vercel webhook disparou build.
- Aiatolah: commit e854771 + `vercel --prod --yes`. CLI deu 413/"Upload aborted" (problema pré-existente do fluxo manual — nenhum arquivo >5M; 632 arquivos; 21M em public/), mas **deploy foi a produção** (retries passaram).

## Commits (rollback granular via Git)
riocarta `28a80c7` · mapario `c5e7314` · globalsouth `bc3c7f9` · mundotrilhos `0ea32b7` · railpost `b25b821` · discoverbrazil `d8fd63c` · ceara `c947c9b` · aiatolah `e854771`.

## Prova ao vivo final (2026-08-12 23:2x BRT)
- Home + robots.txt HTTP 200 nos 8.
- lang ao vivo: riocarta/mapario/mundotrilhos/ceara `pt-BR`; globalsouth/railpost/discoverbrazil `en`.
- sitemap www: mundotrilhos/railpost/discoverbrazil servem `<loc>https://www.<site>/</loc>`.
- Aiatolah: sitemap-index.xml 200 (era 404) com /en/posts; canonical `https://www.aiatolah.com/`; hreflang www; JSON-LD em post.

## Pendências (decisão Miguel)
1. Aiatolah redirect não-www→www (dashboard Vercel).
2. Aiatolah webhook GitHub→Vercel (reativar integração Git; evita CLI/413).
3. DNS estável local (1.1.1.1/8.8.8.8) p/ reduzir rodadas vazias do orquestrador.
4. Submeter os 8 sitemaps no Google Search Console.

## Lições
- `site:` do `astro.config` é a **fonte do canonical + sitemap** — mismatch www ali contamina todos os posts de uma vez (silencioso, alto impacto SEO).
- `robots.txt` faltante é gap comum em Astro: o `@astrojs/sitemap` gera o sitemap mas NADA aponta pra ele sem o robots.
- Aiatolah = template separado (não o "blog"); trata-se caso a caso. Já era o mais avançado em i18n (hreflang) mas o mais atrasado em sitemap/canonical.
- `vercel --prod` CLI pode dar 413/aborted e ainda assim deployar (retries); não confiar só na mensagem de erro — validar ao vivo.
