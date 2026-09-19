# Memória — Log técnico: publicação manual GSN (EN) do post O Cafezinho 265537

**Data:** 2026-08-13 (~22:40→23:09 BRT) · **Executor:** ZCode (GLM-5.2) · **Status:** ✅ NO AR
**Fórum gêmeo:** `Foruns/forum_gsn_publicacao_manual_hollywood_soft_power_20260813.md`

## Missão
Miguel pediu: publicar tradução EN do post O Cafezinho no GSN. Post original PT:
https://www.ocafezinho.com/2026/08/13/o-soft-power-de-hollywood-e-a-desumanizacao-do-sul-global-por-que-precisamos-de-uma-nova-mitologia-audiovisual-multipolar/ (ID 265537, "O neoimperialismo americano por trás do soft power de Hollywood"). Miguel pediu depois: assinar **"na minha coluna Miguel do Rosário"**.

## Passos executados
1. **Texto verbatim** via `curl wp-json/wp/v2/posts/265537?_fields=...` (REST read FUNCIONA em ocafezinho.com).
2. **Repo correto:** `/home/migueldorosario/Dados_Frios/Global South News/gsn` (remote `git@github.com:migueldorosario1/global-south-news.git`, branch main, limpo). Achei comparando 2 candidatos; o `cerebro-miguel/global_south_news/gsn` aponta p/ outro remote (sync do cérebro, NÃO publicar).
3. **Schema:** `src/content.config.ts` (zod). Frontmatter modelo: último post `exclusive-documents-conviction-...md` (author "Miguel do Rosário", heroImage URL R2).
4. **Arquivo criado:** `src/content/blog/hollywood-soft-power-dehumanization-global-south.md` (title EN, description EN, pubDate `2026-08-13T13:02:42Z`, author "Miguel do Rosário", draft:false, lang:en, categoria_macro:"Geopolitics", interlink_url+interlink_lang:"pt" p/ o original, source_name:"O Cafezinho", wp_id:265537). Tradução fiel e fluente (6 seções H2 preservadas).
5. **Hero image:** baixada do O Cafezinho (`wp-content/uploads/2026/08/soft-power-global-demografia-arte.jpg`, 1024×1024, 215KB). Descoberto que `public/hero/` é **gitignored** e 50/51 posts usam URL R2. Bucket = `r2:riocarta-hero-images/hero/`. Upload: `rclone copyto <jpg> r2:riocarta-hero-images/hero/hollywood-soft-power-global-south.jpg`. URL pública: `https://pub-f814950afdbb40b7801fc9ec9dc9e04c.r2.dev/hero/hollywood-soft-power-global-south.jpg` (HTTP 200).
6. **Commit + push:** `270b8cd` → `316cc19` (byline). `git pull --rebase` (remote adianta por cron hourly).

## 🔑 PROBLEMA + SOLUÇÃO (o coração desta memória)
- **Push NÃO publicou.** Polling de ~6min: combined status GitHub = `pending` com `total_count:0` (zero checks da Vercel). Ou seja, a integração GitHub→Vercel **não dispara build** neste repo. Post ficava 404.
- **Deploy manual necessário:** `vercel deploy --prod --yes` (idêntico ao `gsn_publish_hourly_batch.mjs:1074-1075` que usa flag `--vercel-deploy`).
- **ARMADILHA — 2 projetos Vercel:**
  - `global-south-news` → `gsnews.vercel.app` → **serve globalsouth.news** (CANÔNICO).
  - `gsn` → `gsn-sage.vercel.app` (paralelo; NÃO serve o domínio).
  - Repo **não estava linkado** → primeiro `vercel deploy --prod --yes` caiu no projeto `gsn` (errado): build OK, 200 no `gsn-sage.vercel.app`, mas **404 em globalsouth.news**.
  - **Correção:** `vercel link --yes --project global-south-news` (reescreve `.vercel/project.json` p/ `prj_KCbxgDzYRlJ4v3WWo87oD9aKAxVi`) → `vercel deploy --prod --yes` → 88 págs em ~3s, pronto em 18s → **200 em globalsouth.news**.
- **Verificação final:** 200 no domínio; título "The American Neoimperialism Behind Hollywood's Soft Power"; byline "Miguel do Rosário" no render; hero carregando; conteúdo íntegro (85%, multipolar audiovisual).

## Comandos canônicos (para reaproveitar)
```bash
cd "/home/migueldorosario/Dados_Frios/Global South News/gsn"
# garantir link ao projeto CERTO (uma vez por checkout novo):
vercel link --yes --project global-south-news
# publicar:
git add ... && git commit -m "..." && git pull --rebase origin main && git push origin main
vercel deploy --prod --yes
# hero image:
rclone copyto "local.jpg" "r2:riocarta-hero-images/hero/<slug>.jpg"
```

## O que falta / lições
- **Falta:** nada (Miguel pode revisar tradução/capa).
- **Lição 1:** nunca assumir que `git push` publica o GSN — sempre `vercel deploy --prod` ao projeto `global-south-news`.
- **Lição 2:** cuidado com o projeto-fantasma `gsn` (gsn-sage) ao deployar de checkout deslinkado.
- **Lição 3:** REST read funciona no ocafezinho.com (útil p/ extrair texto verbatim de posts).
