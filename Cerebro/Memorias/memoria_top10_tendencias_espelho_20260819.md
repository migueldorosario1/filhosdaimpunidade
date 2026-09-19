# 🧠 Memória técnica — Box Top 10 Tendências no espelho + fix proxy V4 (19/08/2026)

> Sessão: ZCode (Kimi K3 → failover DeepSeek) · 10:55→11:30 BRT
> Fórum irmão: `Foruns/forum_top10_tendencias_espelho_arquiteturas_v4_20260819.md` (com os desenhos Radar/RAR/PES/Constituição)

---

## 1. Box Top 10 Tendências (em produção no espelho)

**Fluxo:** NYC calcula (GA4) → empurra REST → espelho guarda option → front-page renderiza.

- **NYC `/root/top_tendencias_push.py`** (cron `25 * * * *`, marcador `TOP_TENDENCIAS_PUSH_20260819`; backup crontab `/root/crontab_backup_pre_top10_20260819.txt`):
  - GA4 `BetaAnalyticsDataClient` (propriedade 374552425), dimensão pagePath, métrica screenPageViews, limit 300; junta path normal + `/amp`; extrai slug por segmento (path `/aaaa/mm/dd/slug/`).
  - Posts: REST público do canônico `/wp-json/wp/v2/posts` (48h, per_page 100) — **precisa User-Agent de navegador** (Cloudflare 1010 sem ele).
  - Score = views_hoje + views_ontem×0,3 (padrão do agente_manchete); descarta cat 20699; Top 10 → `safe_post` p/ `https://cafezinho.news/wp-json/cafezinho/v1/top-tendencias` com auth `ESPELHO_WP_USER/PASS` (já existiam no `/root/chaves.sh`, bloco V4_ESPELHO_20260812).
  - Log: `/root/agent_data/top_tendencias_push.log`.
- **Espelho mu-plugin `cafezinho-top-tendencias.php`:**
  - POST guarda option `cafezinho_top10` {ts, items[]} — só post que JÁ existe no espelho e publish (o canônico pode ter coisa não espelhada; o filtro cai fora sem erro) e fora da 20699; limita 10; `wp_cache_flush()`.
  - Renderer `cafezinho_render_top_tendencias()`: card amarelo (bg #fff8e6, borda #f0c36d), título "🔥 Top 10 Tendências", subtítulo "Os mais vistos nas últimas 24 horas · atualizado às HH:MM", `<ol>` de links (get_permalink local). **Exclui a manchete atual** (lê wp_highlights) para não repetir o hero logo abaixo dele.
  - **front-page.php:** chamada inserida após `endwhile; wp_reset_query();` da manchete e antes do `banner-after-manchete-mobile` (backup `front-page.php.bak_pre_top_tendencias_20260819`).
- **Provas:** 1ª rodada 11:21 BRT — GA4 261 slugs hoje/213 ontem; top10 montado (1º Ciro/Mossad); espelho aceitou 8 (2 não espelhados ainda); home: ordem manchete→box→banners ✓, títulos sem views/tags ✓.

## 2. Fix proxy V4 Tendências (NYC)

- **Sintoma:** `worker_exception ProxyError ... host='cafezinho.news'` + `v4_production_stall_alert` (desde 17/08 04:58 UTC).
- **Causa raiz:** `/root/chaves.sh` exporta `HTTP_PROXY/HTTPS_PROXY` (iProyal) globalmente; `NO_PROXY` tinha controle.ocafezinho.com etc. mas **faltava cafezinho.news** → chamadas do worker ao espelho iam pelo proxy e falhavam. Direto NYC→cafezinho.news responde 200 em 0,35s.
- **Fix:** `cafezinho.news,www.cafezinho.news` adicionados a `NO_PROXY` e `no_proxy` (backup `chaves.sh.bak_pre_noproxy_espelho_20260819`). Prova com env carregado: 200. Rodada manual do worker: **publicou 400129** (força-da-onu…). Nota: saiu `publicado_sem_imagem` (flickr falhou na rodada — fluxo de imagem é outra esteira, dos loops).
- **Lição permanente:** qualquer domínio NOSSO novo precisa entrar no NO_PROXY do chaves.sh do NYC (proxy é para tráfego de coleta externa, não para nossos sites).

## 3. Pendências aguardando Miguel (do fórum §7)

Aprovação dos desenhos: Radar de Tendências v1 (agente único consultivo), RAR+portão no publicador, PES conservador, minuta da Constituição de Estilo (10 mandamentos + 8 ritmos; escopo blindado: espelho + Filhos da Impunidade, nada canônico por ora). Sessão separada do Miguel vai calibrar os ritmos do FdI.
