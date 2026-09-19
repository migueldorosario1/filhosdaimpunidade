# 🧠 MEMÓRIA TÉCNICA — Análise 1.125 posts 3 semanas (25/07–15/08)

**Sessão:** ZCode GLM-5.3, 15/08 00:45→01:15 BRT · **Fórum:** `Foruns/forum_cafezinho_analise_posts_3semanas_20260815.md`

## Reprodução (como refazer)

1. **Posts:** WP REST `?after=2026-07-25T00:00:00&per_page=100&page=N&orderby=date&order=asc&_fields=id,date,slug,title,categories,author` — paginação ASC com `after=` (varredura DESC por page falha ~page 7, rate-limit); 12 páginas → 1.125 posts. `content` só para o top 150 por score (economia). REST `/users` é bloqueado → mapa de autores fixo {2018 Miguel, 5780 Gabriel, 5786 V4, 5470 Redação}.
2. **GA4:** script `/tmp/coleta_3sem.py` no Tencent — pagePath × [screenPageViews, userEngagementDuration, totalUsers, sessions, engagementRate], 25/07–14/08, platform=web, limit 5000 (retorna ~5k paths). Tempo de leitura por post = userEngagementDuration÷views (preferir canonical ≥30 views; AMP subestima).
3. **GSC:** mesmo script — page (web+discover) 25/07–13/08, dataState=final.
4. **Agregação:** por slug (regex `/(\d{4}/\d{2}/\d{2}/)?slug/?(amp/)?`), canonical+AMP somados; hora BRT = UTC-3; score = views + 3×cliques; ritmo = score/idade.

## Números-canônicos

- Universo: **1.125 posts** (25/07–15/08; ~54/dia; últimos 200 = só 10–15/08).
- Funil: mediana 25 views; >500 views: 2,0%; >200: 6,1%; >50: 30,4%; >1.000: 3 posts.
- Top audiência: China-míssil 6.044vw/38s · China-Rússia-Japão 5.501/45s · Deputada argentina-Lula 1.209/69s · Lula>2×Flávio 981/85s · Guia debates Band 812/22s.
- Top cliques: China-míssil 6.349 (6.260 Discover!) · China-Rússia 5.680 · China-fábricas 770 · Guia Band 742 · EUA-Irã 620 (pos 1,2).
- Top leitura: Trump afunda Flávio 167s · Ceará espelho 2022 134s · Milei palanque 130s · Lula tarifaço 128s (1.198 pal) · PL circo 125s.
- Ritmo: China-Rússia 2.818 pts/dia · China-míssil 1.930 · **Atlas/Focus Ciro×Elmano 865 (2 dias!)** · Bolsonarista-Moraes 696 · Guia Band 608.
- Categorias: Geopolítica 302 posts/29.543 clk (58% do total, 98/post) · Política 431/16.725 (39) · Eleições+Eleições 2026 44/4.572 (104–119/post) · Ceará 17/845 (50/post, 134s) · Tecnologia 90/1.703 (19) · Ciência+IA 164/2.176 (13) · Economia 71/874 (12).
- Autores: V4 709 posts/56.034 vw/47s · Redação 301/9.918/68s · Gabriel 82/7.587/61s · **Miguel 20/4.261/81s (213 v/post = 2,7× V4)**.
- Dia: Sáb 112 v/post > Dom 86 > Seg 77 > Qui 70 > Ter 61 > Sex 48 > Qua 45. Clk/post: Sáb 97 vs Qua 19.
- Hora BRT (v/post): 06h 137 · 10h 137 · 09h 123 · 11h 99 · 15h 97 || piores: 22h 23 · 18h 33 · 01h 36.
- AMP: 64% das views (50.981 vs 28.970).
- Título: verbo+nome 4,7% chance >500 views (n=233) · só verbo 2,2% · só nome 1,6% · nenhum 0,5% (n=407!). Views médios 92-105 vs 39. Comprimento 55–90: diferença pequena.
- Tamanho (138 top): ≤250 pal = 427 vw/410 clk/29s · 250–450 = 327/287/43s · 450–800 = 269/171/58s · 800–1.300 = 385/179/85s · >1.300 = 750/319/85s. r(words×views)=0,06; r(words×leitura)=0,49.

## Lições para aplicar (pendências com Miguel)

(a) briefing títulos V4/redatores: verbo+nome próprio; (b) agendar 06h/09h/10h/15h + reforço sexta→sábado; (c) escalar Regional (Ceará provou); (d) reformular Ciência/IA/Tecnologia p/ formato Discover ou reduzir cadência; (e) 2–3 posts-curto China-militar/semana (gatilho Discover: "arma"+China); (f) serviços de busca (guias) como base constante.
