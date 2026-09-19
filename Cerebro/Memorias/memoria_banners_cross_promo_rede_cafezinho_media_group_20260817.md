# MEMÓRIA TÉCNICA — Banners cross-promotion da rede CMG (17/08/2026)

**Fórum irmão:** `Foruns/forum_banners_cross_promo_rede_cafezinho_media_group_20260817.md`

## 1. Fontes das identidades (verificadas em código/arquivos)
- Cafezinho: `--red: #CD152B` em `wp-content/themes/ocafezinho-portal/style.css:43` (canônico); logo xícara em `Outros/logo cafezinho/logo-ocafezinho classico (1).png` (xícara preta desenhada à mão + wordmark condensado).
- GSN: `sites-v4/globalsouth/src/styles/global.css` (--bg-main #fff1e5, --accent #9e2f50, --accent-alt #0a5a66); `SITE_DESCRIPTION='The Voice of the Developing World'` em `src/consts.ts`; logo = globo wireframe de anéis orbitais coral (`src/assets/logo.png`, 52x52).
- Rio Carta: `sites-v4/riocarta/src/styles/global.css` (--accent #2337ff, --accent-dark #000d8a); consts: "Portal de Notícias do Rio de Janeiro, por Miguel do Rosário"; logo = monograma R c/ morros+ondas (`src/assets/logo-transparent.png`).
- Aiatolah: `sites-v4/aiatolah/src/styles/global.css` (--bg-dark #0a0a0c, --accent-primary #00ff88, --accent-secondary #7000ff); bilíngue: `aiatolah.com/en` e `/pt` (links no header); PostLayout: "Editorial analysis from a Global South perspective".
- Media Group: site `cafezinhomediagroup.vercel.app` ("Central de Portais de Mídia Independente"); selo "Um portal do/Part of the" no ar desde 05/08 nos 8 temáticos+espelho+Moka (`memoria_selo_cafezinho_media_group_20260805.md`); repo GitHub `migueldorosario1/cafezinhomediagroup` (sem clone local).
- Moka: gradiente #FF9E3D→#C25410, creme #FFF3E6, Archivo (banners estáticos em `Outros/mokareader/banners/_zip_extraido/AMP estatico/`).

## 2. Zonas vazias escolhidas no Cafezinho (mapa de ads de 17/08)
- `#banner-sidebar` (sticky, sidebar do single) → 300x250 desktop rotativo.
- `#banner-after-recents-mobile` (single mobile) → 300x250.
- `#banner-after-recents-desktop` (home, entre Recentes e Top10) → 728x90.
- Moka já ocupa home-pós-LinhaDoTempo e single-antesDoTexto → cross nunca cola no Moka.

## 3. Decisões
- Formatos: 300x250 + 728x90 (padrão Moka) + 320x100 só p/ Cafezinho-PT e GSN-EN (app Moka).
- Arte estática, sem foto de pessoa, texto exato no prompt (conferir e corrigir no editor).
- Componentes futuros: `CrossPromo.astro` (rodapé, acima do selo .group-tag) nos 8 temáticos; `PromoBanner.tsx` no Moka (leitor+biblioteca, por locale).
- Aiatolah troca set por rota (EN raiz / PT em /pt/); deploy Aiatolah = `vercel --prod` manual.

## 4. Pendências do Miguel
Artes aprovadas? Moka 10 outros idiomas = GSN-EN ou nada? Rio Carta-EN entra no GSN? "vai" da implementação.
