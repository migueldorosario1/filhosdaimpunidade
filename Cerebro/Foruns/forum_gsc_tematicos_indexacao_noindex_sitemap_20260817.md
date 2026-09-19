# Fórum — Alertas GSC dos sites temáticos: noindex, sitemap e indexação (17/08/2026)

**Tema:** E-mails do Google Search Console sobre indexação dos temáticos (mundotrilhos.com, aiatolah.com, railpost.news, discoverbrazil.news e os demais — Miguel: "considere que quase todos os sites temáticos estejam com problemas parecidos").

**Sessão:** ZCode (ZCodeProject) · **Data:** 17/08/2026 · **Status:** ✅ CORREÇÕES APLICADAS E DEPLOYADAS (8 repos)

---

## 1. O que aconteceu

Miguel recebeu e-mails iguais do GSC (dados até 13/08) apontando páginas fora do índice. Exemplo do **mundotrilhos.com**: 79 "Excluída pela tag noindex", 44 "alternativa com canônica adequada", 25 "404", 14 "redirecionamento", 2 "403", 329 "detectada, mas não indexada", 6 "rastreada, mas não indexada".

## 2. Diagnóstico (o que era cada motivo)

| Motivo GSC | Causa real | Ação |
|---|---|---|
| **noindex (79)** | **Histórico.** Os satélites nasceram com `noindex,nofollow` global pré-launch (maio/2026, "Sprint 0b" — ver `CEREBRO_INDEX_SATELITES.md` §SEO pre-launch). Google registra rastreios antigos até re-rastrear. A única página noindex **viva** achada foi `aiatolah.com/teste/` (+ `teste-header-novo` em ceara/riocarta) — e elas estavam **dentro do sitemap**, o que mantém o alerta vivo. | Sitemap limpo + "Validar correção" no GSC |
| **Canônica adequada (44)** | Variantes apex×www servindo 200 com canonical apontando pro outro (aiatolah apex→www; mapario/ceara www→apex). Benigno, mas ideal é redirect. | Canonical correto já existe; redirect pendente (Vercel) |
| **404 (25)** | URLs do site antigo pré-V4 (`/noticias/`, `/posts/`…) + URLs com `&amp;` literal no sitemap (ex.: `/tags/wyss&amp;lila/`) | Envelhecem sozinhas; sitemap agora limpo |
| **Redirecionamento (14)** | Apex→www (307/308), normalização de trailing slash, slugs antigos (redirects já existem no astro.config do MT) | Intencional — ignorar |
| **403 (2)** | Poucos URLs bloqueados (provavelmente endpoints internos) | Monitorar; sem ação |
| **Detectada, não indexada (329)** | **Tag explosion**: sitemap do MT tinha 382 tags para 202 posts (65% do sitemap = página fina). Google desiste de rastrear. | Tags fora do sitemap + `noindex,follow` |
| **Rio Carta (caso grave próprio)** | Blog era SSR (`prerender=false`) → **0 artigos no sitemap**; em compensação **1.043 rascunhos** (`/preview/`, noindex) estavam no sitemap + 1 post legado `__trashed` público. | Blog pré-renderizado: 2.809 artigos estáticos no sitemap; rascunhos e lixo fora |
| **Ceará Digital (caso próprio)** | Conteúdo é SPA (React client-side): home e `/historico/` sem links de artigos no HTML estático. Google não encontra os artigos. | ⏳ Pendente (arquitetural — sessão dedicada) |

## 3. Correções aplicadas (8 repos de `Projeto Cafezinho Agentes/sites-v4/`)

1. **Sitemap filtrado** (`astro.config.mjs` de todos): exclui `/tags/`, `/teste*`, `/preview/` — e no riocarta também `/senadores/` e `/prefeituras/`.
2. **Tag pages** → `noindex,follow` (prop nova `noindex` no `BaseHead.astro` + uso em `src/pages/tags/[tag].astro`).
3. **riocarta**: blog com `prerender = true` + `getStaticPaths()` (artigos estáticos entram no sitemap) + remoção do post `__trashed` legado.
4. **Builds locais validados** (exit 0) antes de cada push; contagens conferidas no `dist`.

**Provas (antes → depois):**
- mundotrilhos: sitemap 586 → **204** URLs (0 tags) · tag page = `noindex,follow`
- railpost: 570 → **188** · discoverbrazil: 504 → **110** · mapario: 178 → **44**
- globalsouth: 620+ → **143** · aiatolah: 395 → **393** (teste fora)
- ceara: 18 → **16** (teste/preview fora)
- riocarta: 1.104 (1.043 preview, 0 artigos) → **2.862** (2.809 artigos, 0 lixo)

## 4. O que falta / o que preciso de você (Miguel)

1. **Nada bloqueia** — deploys da Vercel rodando sozinhos a partir do push.
2. **Opcional (recomendado):** no GSC de cada propriedade, clicar **"Validar correção"** nos motivos "Excluída pela tag noindex" e "Página alternativa" — acelera a limpeza do estado antigo (senão o Google re-rastreia naturalmente em semanas).
3. **Ceará Digital:** decidir prerender/SSR dos artigos (maior ganho de indexação pendente) — sessão dedicada.
4. **Redirects apex↔www** (aiatolah, mapario, ceara) via Vercel — cosmético, canonical já cobre.
5. **Reavaliar "Detectada não indexada" em ~2 semanas** pós-deploy (esperado cair com sitemap enxuto).

## 5. Registro

- Memória técnica: `Memorias/memoria_gsc_tematicos_indexacao_noindex_sitemap_20260817.md`
- Catálogo: `CEREBRO_INDEX_SATELITES.md` §SEO + `CEREBRO_NODE_ATUALIZACOES.md`
- Commits: mundotrilhos `d2d3a90` · railpost `7f0622a` · discoverbrazil `7f0718c` · mapario `b90c63e` · globalsouth `8fc1bb1` · aiatolah `8aa9601` · ceara `8cc1b01` · riocarta `0344ea9` (todos em `main`, GitHub → Vercel)
