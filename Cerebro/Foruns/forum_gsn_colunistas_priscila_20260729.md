# FÓRUM — GSN: seção Colunistas (submenu Editorial) + categoria Priscila Miranda

**Data:** 2026-07-29 ~13:25 BRT · **Agente:** ZCode/Kimi K3 · **Pedido:** Miguel (chat): "no global south news você cria um submenu lá no editorial [...] postagens da Priscila Miranda [...] confere se estão com categoria Priscila Miranda [...] volta a categoria de todas as postagens dela"

## Decisões / implementação (commit `f2edc9c`, repo globalsouth-v4)

1. **Menu:** `Editorial ▾` agora tem **Columnists ▸** (flyout aninhado) listando os 3 colunistas com posts no portal + item "Editorial Method" (página `/editorial` existente). CSS próprio de flyout (desktop hover; mobile vira bloco indentado, CSS-only). Arquivo: `src/components/Header.astro`.
2. **Páginas de colunista:** novo `src/pages/colunistas/[author].astro` (padrão copiado de `tags/[tag].astro`) — gera uma página por autor presente na coleção: `/colunistas/priscila-miranda/`, `/paulo-nogueira-batista-jr/`, `/miguel-do-rosario/` (+ `/global-south-news-desk/`, automático). Hero com nome + contagem de colunas + grid de posts.
3. **Categoria:** as 3 postagens da Priscila Miranda (`How India Turned Cinema...`, `Citizen Netflix`, `Resurrection: Bi Gan's...`) estavam **sem campo de categoria** → adicionado `categoria_macro: "Priscila Miranda"` (campo do schema `content.config.ts`; `category` seria descartado pelo zod). Autoria já estava correta (`author: "Priscila Miranda"`).

## Validação

`npm run build` ✅ 339 páginas; `/colunistas/priscila-miranda/` renderiza h1 "Priscila Miranda" + "3 columns"; menu com flyout presente no HTML da home; deploy Vercel via push.

## Observações

- Novos colunistas passam a ter página automaticamente quando um post com `author` novo entrar — mas o **item de menu é hardcoded** (padrão do Header, igual Geonews): adicionar `<li>` no flyout quando surgir colunista novo.
- A página `/editorial` (método editorial) segue existindo; o rótulo do menu que apontava para ela ("Columnists") foi corrigido para "Editorial Method".

**Memória técnica:** `Memorias/memoria_gsn_colunistas_priscila_20260729.md`

---

## ADENDO 2 — Coluna Paulo Nogueira Batista Jr.: "The Age of Endarkenment" PUBLICADA (24/08/2026 19:55 BRT)

**Ordem do Miguel (~19:42):** publicar o docx de `Outros/Global South News/posts/` na coluna dele, conferir assinatura, revisão leve.

1. **Repo de produção confirmado por prova:** `Projeto Cafezinho Agentes/sites-v4/globalsouth` → GitHub `migueldorosario1/globalsouth-v4` → Vercel (www.globalsouth.news). ⚠️ NÃO confundir com `Dados_Frios/Global South News/gsn` → repo `global-south-news` (arquitetura antiga, sem colunistas, sem os briefs novos — nunca publicar ali).
2. **Post:** `src/content/blog/the-age-of-endarkenment.md` (commit `105694c`, rebase sobre `c856942`). Nome correto **Paulo Nogueira Batista Jr.** (docx assina assim; o Miguel inverteu o sobrenome na ordem, usado o do documento).
3. **Assinatura em 3 níveis:** byline visível `**By Paulo Nogueira Batista Jr.**` (padrão dos 3 posts anteriores) + `author:` no frontmatter (alimenta a coluna) + **patch no `BlogPost.astro`**: JSON-LD agora usa `author` do frontmatter como `Person` (fallback Organization p/ quem não tem). Antes o JSON-LD hardcodeava "Global South News" para todos.
4. **Coluna:** `/colunistas/paulo-nogueira-batista-jr/` ao vivo mostra **"4 columns"** com o novo post (página é automática via `author`, sem `categoria_macro`).
5. **Revisão leve (typos/gramática, voz do autor intocada):** "degradation of its" → "of its elites"; "only o remember" → "only remember"; "form the rise" → "from"; Gandhi "what assessment he made...?" → pergunta indireta correta; "in that fact that" → "in the fact that"; "needs prepare" → "needs to prepare"; "Se vis pacem" → "*Si vis pacem, para bellum*"; "totally or almost" → "totally or almost totally"; "can – and does do –" → "can – and does –"; espaços duplos normalizados; títulos de livro em itálico (*The West and the Rest*, *Human, all too human*).
6. **Capa:** pintura de domínio público "A Philosopher Lecturing on the Orrery" (Joseph Wright of Derby, 1766, Wikimedia) — 1200×675 blur-fill (padrão dos heroes), crédito/licença/link no frontmatter.
7. **Provas ao vivo:** post 200 + byline + JSON-LD Person no HTML; hero 200; coluna "4 columns"; home linka o post.

**Estado:** concluído. Coluna do Nogueira: 4 posts (china-does-not-improvise, the-greatest-country, brics-dedollarization, the-age-of-endarkenment).

---

## ADENDO 3 — Troca de capa "The Discreet Charm of the BRICS": ilustração IA → foto real do painel BRICS WAVES (27/08/2026 22:33 BRT)

**Ordem do Miguel (~22:20):** trocar a capa do artigo da Priscila nos DOIS sites (GSN EN + Cafezinho PT) pela foto real do evento na Índia (`Outros/Negocios Priscila/fotos/4N5A0613-compressed.jpg`, painel "Women Leading the Future of the BRICS Creative…" do BRICS India 2026), com legenda + crédito "Divulgação".

1. **GSN (EN):** commit `29e9b7f` no repo canônico `sites-v4/globalsouth` (main → `migueldorosario1/globalsouth-v4` → Vercel). Hero novo `/hero/the-discreet-charm-of-the-brics-photo.jpg` (1200×675, crop 16:9 viés 30% topo; provas: página 200 com hero novo + caption "Priscila de Miranda, author of the article, at a BRICS event in India (BRICS WAVES) — Photo: Divulgação (Editorial Use)"). Frontmatter: `hero_legenda` (campo novo usado pela 1ª vez neste post) + `hero_credit: "Divulgação"`; `hero_source_url` REMOVIDO (não faz sentido linkar o próprio site num handout). Ilustração IA antiga mantida no repo (histórico), só desreferenciada.
2. **Cafezinho (PT):** post **267645** ("O discreto charme dos BRICS", 25/08). Mídia nova **268047** (`priscila-brics-india-1.jpg`, wp media import com caption/alt/desc) → `_thumbnail_id=268047` via WP-CLI **com `CAFEZINHO_EDITORIAL_HUMAN_OVERRIDE=1`** (guard `cafezinho-protecao-editorial` bloqueou a 1ª tentativa — post de humano) + `wp_update_post` (reindex Yoast do og:image) + purge Rocket (`rocket_clean_domain`) + flush object cache. Provas ao vivo `?nocache`: og:image = `priscila-brics-india-1-scaled.jpg` (200), `<figcaption>` com a legenda completa (o tema `ocafezinho-portal` renderiza o `post_excerpt` do attachment como figcaption em single.php:37), srcset responsivo completo.
3. **⚠️ Aprendizado GSN:** `globalsouth.news` NÃO é WordPress (REST `/wp-json` dá 403 da borda Vercel) — as vars `GSN_WP_*` do `.env` do NYC são legadas. Publicação GSN = commit no repo Astro.

**Estado:** concluído e provado nos 2 sites. **O que falta:** nada. **Preciso do Miguel:** nada.

**Memória técnica:** `Memorias/memoria_priscila_capa_brics_gsn_cafezinho_20260827.md`
