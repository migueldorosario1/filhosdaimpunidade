# MEMÓRIA TÉCNICA — GSN: seção Colunistas + categoria Priscila Miranda (2026-07-29)

**Fórum (decisões):** `Foruns/forum_gsn_colunistas_priscila_20260729.md`
**Agente:** ZCode/Kimi K3 · **Commit:** `f2edc9c` em `globalsouth-v4` (push → Vercel)

## Contexto

Pedido do Miguel: submenu "Colunistas" dentro do menu Editorial do globalsouth.news, com as postagens da colunista **Priscila Miranda** marcadas com a categoria dela. Ela tem 3 posts (cinema Índia anti-colonial, Citizen Netflix/streaming BR, Resurrection/Bi Gan China). Outros autores com posts: Paulo Nogueira Batista Jr. (3), Miguel do Rosário (3), Global South News Desk (39).

## O que foi feito (5 arquivos, +255/-2)

1. `src/components/Header.astro`:
   - `isEditorialActive` passa a incluir `colunistas/*`.
   - Dropdown Editorial: item "Columnists ▸" com **flyout aninhado** (`.submenu-flyout`, CSS-only: hover/focus-within no desktop; `@media ≤950px` vira bloco estático indentado — o JS de toggle mobile já existente cobre o pai). Itens: Priscila Miranda, Paulo Nogueira Batista Jr., Miguel do Rosário + "Editorial Method" (`/editorial`).
2. `src/pages/colunistas/[author].astro` (novo): `getStaticPaths` mapeia cada `author` da coleção → slug (NFD strip + lowercase + hífens). Página = kicker "Columnists" + h1 nome + "N columns" + grid de posts (mesmo padrão visual de `tags/[tag].astro`).
3. `src/content/blog/{how-india-transformed-cinema-into-anticolonial-tool,citizen-netflix-streaming-regulation-brazil,the-chinese-dream-resurrection-bi-gan}.md`: `categoria_macro: "Priscila Miranda"` após `author:`.

## Armadilhas evitadas

- **Schema zod** (`content.config.ts`) só conhece `categoria_macro` — campo `category` seria silenciosamente descartado. É por isso que a categoria foi gravada como `categoria_macro`.
- Chips da home seguem vindo de `tags` (lógica em `index.astro:29`) — não alterado.
- Byline visível não existe no template (author só no JSON-LD, `BlogPost.astro:251`) — nada a linkar.

## Validação

Build 339 páginas ✅ · `dist/colunistas/priscila-miranda/index.html` com h1 "Priscila Miranda" + "3 columns" ✅ · flyout no HTML da home ✅ · 3/3 posts com `categoria_macro` ✅.

## Pendência conhecida

Menu de colunistas é hardcoded: ao entrar colunista novo, adicionar `<li>` no flyout do Header (a página dele é automática).
