# Fórum — GA4 instalado no Moka Reader (ordem do Miguel, 18/08/2026)

> Data: 2026-08-18 ~18:45 · Autor: ZCode/DeepSeek · Status: ✅ **NO AR E VERIFICADO** (commit `87c76c6`)
> Pendência urgente criada ~18:30 atendida na íntegra. Snapshot que motivou: `Foruns/forum_moka_quadro_audiencia_emails_20260818.md` (site sem NENHUM analytics; tabelas do Supabase ausentes).

## O que foi feito

1. **Propriedade GA4 criada pelo Miguel no console** (fluxo assistido no chat, ~15 min): propriedade "Moka Reader" + fluxo Web "Moka Reader Web" (`https://www.mokareader.com`). **ID de medição: `G-43CSQVKW6N`** (público por design — vai embutido em toda página; não é segredo).
2. **Código (ZCode/DeepSeek):**
   - Novo componente `apps/web/src/components/GoogleAnalytics.tsx` — tag oficial `gtag.js` (async) + config inline, no mesmo padrão dos scripts inline do layout (theme/UI scale), sem libs novas.
   - `apps/web/src/app/layout.tsx` — `<GoogleAnalytics />` no `<head>` do root layout (vale para TODAS as páginas: home, /video, /sobre, /tutorial, /socios…).
3. **Qualidade:** `tsc --noEmit` exit 0 · `next build` verde (19/19 páginas) · backup pré-deploy `Moka/backups/moka_lab_pre_ga4_20260818.zip` (58 MB, regra de backup cumprida).
4. **Deploy:** commit `87c76c6` push main → Vercel implantou automaticamente.
5. **Prova no ar:** curl em `https://www.mokareader.com/` retorna `googletagmanager.com/gtag/js?id=G-43CSQVKW6N` ✅ (Enhanced Measurement ativo na propriedade: pageviews, scroll, cliques, busca).

## Estado da missão

- **O que aconteceu:** GA4 instalado, publicado e verificado no site. A audiência do Moka passa a ser medida a partir de agora (dados aparecem no relatório "Tempo real" em minutos; "Visão geral" consolida em ~24–48h).
- **O que falta:** (1) conferir no console se o Realtime registrou visitas (ação Miguel, 1 min — ou o ZCode na próxima sessão com acesso); (2) **ainda pendente:** rodar `socios-schema.sql` no Supabase (medição interna do painel /socios — item 1 do MASTER Moka); (3) opcional futuro: consent mode (LGPD) antes de habilitar recursos de anúncios.
- **O que preciso de você (Miguel):** nada — só abrir o GA4 → Relatórios → Tempo real pra ver as visitas chegando. O passo seguinte de medição completa é o SQL do Supabase (2 min no dashboard).

---
— ZCode/DeepSeek, 2026-08-18
