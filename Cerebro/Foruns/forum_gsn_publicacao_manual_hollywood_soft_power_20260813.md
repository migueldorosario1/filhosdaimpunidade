# Fórum — Publicação manual GSN (EN): "The American Neoimperialism Behind Hollywood's Soft Power"

**Data:** 2026-08-13 (início ~22:40 BRT, no ar 23:09 BRT)
**Executor:** ZCode (GLM-5.2)
**Origem:** ordem direta do Miguel — publicar tradução EN no GSN do post O Cafezinho 265537.
**Post original (PT):** https://www.ocafezinho.com/2026/08/13/o-soft-power-de-hollywood-e-a-desumanizacao-do-sul-global-por-que-precisamos-de-uma-nova-mitologia-audiovisual-multipolar/

## Estado da missão
- ✅ **PUBLICADO E NO AR.** URL: https://www.globalsouth.news/blog/hollywood-soft-power-dehumanization-global-south
- ✅ Byline solicitada pelo Miguel: **Miguel do Rosário** (sua coluna).
- ✅ Imagem de capa no R2 (`pub-f814950afdbb40b7801fc9ec9dc9e04c.r2.dev/hero/hollywood-soft-power-global-south.jpg`).
- ✅ `draft:false`, `lang:en`, `categoria_macro:"Geopolitics"`, `interlink_*` apontando p/ o original PT.
- Commits: `270b8cd` (post+hero) → `316cc19` (byline Miguel do Rosário) em `migueldorosario1/global-south-news` (origin/main).

## O que aconteceu / o que falta / o que preciso de você (Miguel)
- **Aconteceu:** tradução fiel EN criada; hero baixada do O Cafezinho e subida ao R2; commit+push; **deploy manual Vercel** ao projeto correto.
- **Falta:** nada operacional — revisar/aprovar a tradução e a capa se quiser.
- **Preciso de você:** confirmar se a assinatura "Miguel do Rosário" + crédito `source_name:"O Cafezinho"` está como deseja; e se quer republicar também no Aiatolah/outra frente.

## ⚠️ APRENDIZADO OPERACIONAL CRÍTICO (não estava claro no INDEX_GSN)
1. **Push sozinho NÃO publica o GSN.** A integração GitHub→Vercel **não posta status checks** (combined status fica `pending` com `total_count:0` para todo commit). Publicar exige rodar `vercel deploy --prod --yes` no repo (é o que o `gsn_publish_hourly_batch.mjs` faz na linha 1074-1075 com flag `--vercel-deploy`).
2. **EXISTEM 2 PROJETOS VERCEL confundíveis:**
   - `global-south-news` → **CANÔNICO**, alias `gsnews.vercel.app`, serve `globalsouth.news`. ← USE ESTE.
   - `gsn` → alias `gsn-sage.vercel.app`, **NÃO serve o domínio** (projeto paralelo/legado). (Primeira tentativa de deploy caiu aqui por o repo não estar linkado — link automático pegou o errado.)
3. **Sempre `vercel link --yes --project global-south-news` antes de deployar** a partir de um checkout novo (o link é local em `.vercel/project.json`, gitignored).
4. **Hero images:** bucket R2 `riocarta-hero-images/hero/` (compartilhado c/ temáticos) → URL pública `https://pub-f814950afdbb40b7801fc9ec9dc9e04c.r2.dev/hero/<slug>.jpg`. `public/hero/` é gitignored (é só mirror local). Upload via `rclone copyto <jpg> r2:riocarta-hero-images/hero/<slug>.jpg`.
5. **Repo de trabalho local:** `/home/migueldorosario/Dados_Frios/Global South News/gsn` (remote `global-south-news.git`). O `Antigravity Google/Global South News/gsn` (repo Astro) **não existe** ali; há `Antigravity Google/Global South News/root/` (silo de agentes).
6. **Slug de post** = nome do arquivo `.md` (sem extensão); rota `/blog/[slug]`. Drafts (`draft:true`) são filtrados em `[...slug].astro`.

## Detalhes técnicos
- Post ID O Cafezinho: 265537. Texto verbatim obtido via `wp-json/wp/v2/posts/265537` (REST core **funciona** em read no ocafezinho.com — contradiz nota antiga de que "www não tem REST core"; aquele limite era p/ auth/escrita).
- Tags: soft-power, global-south, hollywood, brics, multipolar-world, media, cultural-decolonization, united-states.
- Deploy correto: 88 páginas build em ~3s, pronto em 18s.
