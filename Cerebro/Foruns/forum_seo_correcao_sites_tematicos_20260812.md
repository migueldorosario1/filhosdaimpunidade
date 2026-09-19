# Fórum — Correção SEO dos 8 sites temáticos (foco Google)

**Data:** 2026-08-12 (~22:40→23:30 BRT)
**Agente:** ZCode (GLM-5.2 Z.ai — Kimi/Qwen 🔴🔴 esgotados, fallback final)
**Sessão:** chat direto, workspace ZCodeProject
**Origem:** ordem do Miguel ("sim, pode corrigir tudo então, com foco em seo do google"), sequência ao diagnóstico de saúde dos 8 sites temáticos.

## 1. Contexto / o que veio antes

Diagnóstico read-only (mesma sessão) mostrou os 8 sites saudáveis, publicando e com hero/idioma certos. Flagou 3 pontos: (1) `<html lang="en">` hardcoded na home dos sites PT; (2) DNS intermitente local; (3) juiz visual fail-open. Miguel autorizou corrigir tudo com foco em SEO do Google. Este fórum = a **execução** (escrita/deploy).

## 2. Auditoria SEO estrutural (descoberta a fundo)

Template "blog" (7 sites: riocarta, mapario, globalsouth, mundotrilhos, railpost, discoverbrazil, ceara) — `BaseHead.astro` já forte (canonical, OG completo, Twitter card, GA4, google-site-verification, RSS, link sitemap). Aiatolah = template próprio (i18n EN+PT, hreflang, sem sitemap).

**Gaps reais encontrados (por impacto):**
- 🔴 **`site:` sem-www em 3 configs** (mundotrilhos, railpost, discoverbrazil) → sitemap + `<link canonical>` de TODOS os posts gerados sem-www, mas o não-www redireciona (307/308) p/ www → **conflito de canonicalização no Google** (o mais grave).
- 🔴 **`robots.txt` faltava em TODOS os 8** → Google não era apontado ao sitemap (descoberta ruim), embora sitemap-index.xml já fosse gerado (200) nos 7 do template blog.
- 🔴 **Aiatolah sem sitemap** (404) — config `defineConfig({})` vazio, sem `site:`, sem `@astrojs/sitemap`, sem canonical.
- 🟠 **`<html lang="en">` errado** na home de riocarta, mundotrilhos, ceara (PT) + no BlogPost do mapario.
- 🟠 **JSON-LD `NewsArticle` faltava** em mapario, mundotrilhos, railpost, discoverbrazil, Aiatolah (5).
- 🟡 Aiatolah hreflang/OG-image com URL sem-www.

## 3. O que foi corrigido (execução)

| # | Correção | Sites | Arquivo |
|---|---|---|---|
| 1 | `site:` sem-www → **www** | mundotrilhos, railpost, discoverbrazil | `astro.config.mjs` |
| 2 | **`robots.txt`** novo (Allow: / + Sitemap: .../sitemap-index.xml) | TODOS os 8 | `public/robots.txt` |
| 3 | `<html lang="en">` → `pt-BR` (home) | riocarta, mundotrilhos, ceara | `src/pages/index.astro` |
| 3b | `<html lang="en">` → `pt-BR` (posts) | mapario | `src/layouts/BlogPost.astro` |
| 4 | **JSON-LD `NewsArticle`** (headline/image/datePublished/dateModified/author/publisher logo) | mapario, mundotrilhos, railpost, discoverbrazil | `src/layouts/BlogPost.astro` |
| 5 | **Aiatolah sitemap** (instalado `@astrojs/sitemap` 3.7.3 + `site:'https://www.aiatolah.com'` + integration) | aiatolah | `astro.config.mjs`, `package.json` |
| 6 | Aiatolah **canonical** (link rel=canonical via Astro.site) + hreflang/OG-image sem-www→www | aiatolah | `src/layouts/Layout.astro` |
| 7 | Aiatolah **JSON-LD `NewsArticle`** (inLanguage, publisher Aiatolah News) | aiatolah | `src/layouts/PostLayout.astro` |

## 4. Deploy + prova ao vivo (2026-08-12 23:xx BRT)

- **Build local validado em todos os 8** (mundotrilhos 541 págs, riocarta 112s por 3849 posts, aiatolah 363 págs, etc.). JSON-LD, lang e sitemap www confirmados no `dist`.
- **7 sites (template blog): commit + push → Vercel (webhook GitHub→Vercel) → deploy automático.** Commits: riocarta 28a80c7, mapario c5e7314, globalsouth bc3c7f9, mundotrilhos 0ea32b7, railpost b25b821, discoverbrazil d8fd63c, ceara c947c9b. HEAD==origin em todos.
- **Aiatolah (webhook inativo): `vercel --prod` CLI** — deu erros 413/"Upload aborted" (problema pré-existente do fluxo manual), MAS o deploy foi a produção (retries passaram). Commit e854771.
- **Verificação ao vivo final (8/8 ✅):**
  - Home HTTP 200 + robots.txt 200 em todos.
  - `lang` propagado: riocarta/mapario/mundotrilhos/ceara = `pt-BR`; globalsouth/railpost/discoverbrazil = `en`; Aiatolah dinâmico.
  - Sitemap **www** propagado em mundotrilhos/railpost/discoverbrazil (`https://www.<site>/`) e Aiatolah (antes 404, agora 200 com /en/posts).
  - JSON-LD `NewsArticle` renderizado em posts (testado MT, mapario, Aiatolah).
  - Aiatolah: canonical `https://www.aiatolah.com/` + hreflang www novos.

## 5. Estado final / o que falta / próximos passos

**Pronto e no ar (8/8):** robots.txt, sitemap válido, canonical consistente (www), lang correto, JSON-LD NewsArticle. SEO técnico fundamental coberto.

**✅ FECHAMENTO (13/08 ~00:20 BRT) — todas as pendências RESOLVIDAS:**
- **(a)+(b) Aiatolah deploy automático:** `vercel link` + `vercel git connect` ativaram a integração Git — deploy agora é automático via push (validado: deployment `aiatolah-i3yhx20tl` disparou sozinho após o push `0e57f83`). Bônus: `noindex` nas páginas `/teste` (EN+PT) via prop nova no `Layout.astro`. O redirect não-www→www no dashboard Vercel fica como opcional (canonical/sitemap internos já forçam www na prática).
- **(c) DNS estável:** Miguel aplicou o comando sudo — drop-in `/etc/systemd/resolved.conf.d/` com Cloudflare+Google (`Domains=~.`).
- **(d) Google Search Console:** 8 sitemaps submetidos. Rail Post (único sem propriedade) verificado via meta tag `google-site-verification content="dAcu7Vlt..."` adicionada ao `BaseHead.astro` (commit `47e2fe0`); Miguel confirmou "verificou".

**Estado final: MISSÃO SEO 8/8 TOTALMENTE CONCLUÍDA** — robots.txt + sitemap + canonical www + lang + JSON-LD em todos, deploy automático em todos (incl. Aiatolah), 8 sitemaps no Google Search Console.

## 6. Não feito / fora de escopo

- Não mexi em conteúdo, agentes publicadores, nem no orquestrador V4. Só SEO técnico (template/config).
- Não alterei o `BaseHead.astro` dos 7 (já era bom) — apenas garanti consistência (www, lang, robots, JSON-LD).
- Backups: cada commit é rollback granular; `dist/` gitignored; `.bak` não necessário (Git é o backup).

## 7. Catálogo

- Tema Duplo: este fórum + `Memorias/memoria_seo_correcao_sites_tematicos_20260812.md`.
- Indexar em: `CEREBRO_NODE_ECOSSISTEMA_CANONICO.md` (seção 1.2, nota SEO), `CEREBRO_NODE_SEO_OBSERVATORY.md`, `CEREBRO_NODE_ATUALIZACOES.md`.
