# 🧠 MEMÓRIA TÉCNICA — Análise GA4 + GSC + Vitals Cafezinho (14/08/2026)

**Sessão:** ZCode GLM-5.3, workspace ZCodeProject · **Duração:** ~23:05–23:55 BRT
**Fórum:** `Foruns/forum_cafezinho_analise_ga4_gsc_20260814.md` (decisões resumidas)

## Como foi feito (comandos/caminhos para replicar)

1. **Credenciais** (Regra Nº 1 — Cérebro): GA4 = `GA4_PROPERTY_ID=374552425` + `/root/keys/ga4.json` (Tencent, `43.156.151.165:38422`, user `ubuntu`); GSC = service account `/root/cafezinho/dados_agentes/indexing_key.json` (⚠️ NÃO é `/root/keys/indexing_key.json` — não existe), propriedade `sc-domain:ocafezinho.com`; PSI key `GOOGLE_DEVELOPER_API_KEY` em `/root/.env*` no Tencent. Tudo registrado via `carregar_chaves`/env.
2. **Script de coleta:** `/tmp/coleta_gsc_ga4.py` no Tencent (cópia no /tmp local). Coleta GSC (web+discover, dims date/page/query/device/country, dataState=final) + GA4 (filtro `platform IN (Web)`, totais/canais/países/páginas/landing/série diária) → `/tmp/analise_cafezinho/{gsc_raw,ga4_raw}.json`.
   - **Pegadinhas API:** Discover NÃO aceita dims `query`/`device`/`country` (400) — só `page`+`date`; `FilterExpression` usa campo `filter=` (não `expression=`); `MetricHeader` tem `.name` (não `.value`); filtro país China via `string_filter`.
   - **Pegadinha auditoria 2026-05-25 (Cérebro):** GA4 sempre com filtro platform=web para bater com a UI.
3. **Cruzamento WP:** REST pública `https://www.ocafezinho.com/wp-json/wp/v2/posts?slug=X&_fields=title,content,categories,date` (UA de browser; urllib local do PC do Miguel TRAVA no site — usar curl ou rodar com timeout alto em background). Tamanho = nº de palavras do `content.rendered` sem HTML. Categorias: `/categories?include=IDs` (⚠️ JSON vira chaves string → converter int).
4. **CSVs do Miguel:** descompactados em `/tmp/gsc_cafezinho/` (nomes latin-1 quebrados → renomeados). Pastas `google 14 ago 2026` = Discover 3m + CWV desktop/mobile; `google 11 ago` = web 3m; `google jun/1-2-12-22 jul` = histórico.
5. **PSI/CrUX:** rodar NO Tencent (a key não sai do servidor) — script `/tmp/psi_cafezinho.py`.

## Números-canônicos (para citar no futuro)

### GA4 (platform=web)
| Período | Users | Sessões | Views | Engaj | Duração |
|---|---|---|---|---|---|
| 7d 07–13/08 | 43.318 | 50.264 | 59.717 | 27,8% | 54,5s |
| 7d 31/07–06/08 | 36.685 | 45.348 | 53.294 | 30,7% | 54,8s |
| 30d 15/07–13/08 | 150.764 (122,5k real) | 187.680 | 229.594 | 36,2% | 76,0s |
| 30d 15/06–14/07 | 91.605 | 129.387 | 152.789 | 30,5% | 79,1s |

- Piso diário de usuários subiu de ~2k (11–12/07) para ~5,7k (10–13/08). Picos: 15.471 (17/07), 10.341 (08/08).
- Canais 30d: Direct 97.338 (+58%, inclui Discover), Organic Search 75.943 (+49%), Organic Social 13.074 (+44%), Referral 2.706 (−16%).
- Países 30d: Brasil 98.950 (+49%), China 28.273 (**BOT**, ver abaixo), EUA 8.287 (+7%), Singapura 5.528.

### GSC web
| Período | Cliques | Impressões | CTR | Posição |
|---|---|---|---|---|
| 7d | 15.570 | 469.483 | 3,32% | 3,11 |
| 7d ant. | 17.029 | 465.915 | 3,65% | 3,02 |
| 30d | 69.549 | 2.195.009 | 3,17% | **3,35** |
| 30d ant. | 54.518 | 1.668.589 | 3,27% | **4,55** |

- Posição média mensal: jun 4,19 · jul 4,22 · ago(12d) 3,08.
- Queries top P30: "irã" 129.276 imp pos 1,3 · "o cafezinho" 8.248 clk CTR 63,9% · "ira" 57.738 pos 1,1 · "flávio bolsonaro" 58.870 · "lula" 41.665 pos 1,1 · "datafolha" 46.759 · "china" 29.203 pos 1,4.
- Queries broad mal convertidas: "bolsa família" 37.192 imp/0,8% · "pix" 24.322/1,3% · "jogo argentina e espanha" 21.616/0,4% · "dolar" 18.599/0,2%.

### GSC Discover
| Período | Cliques | Impressões | CTR |
|---|---|---|---|
| 7d | 5.868 | 109.568 | 5,36% |
| 7d ant. | 8.568 | 229.521 | 3,73% |
| 30d | 34.677 | 680.315 | 5,10% |
| 30d ant. | 4.055 | 69.336 | 5,85% |

- História 3m (export 14/08): maio ~29k cliques/dia → colapso junho → picos ago 5.490 (02/08) e 4.219 (08/08).
- Top P30: Moreira/dividendos 19.458 clk · China-míssil 6.260 · China-Rússia-Japão 5.402 (=90% do total).

### CWV (GSC)
- Desktop 12/08: 7.919 Bom / 0 melhorias / 0 ruins (16/05: 15.136 melhorias / 0 bom). Inflexão 07/07 e 06/08.
- Mobile 12/08: 9.044 Bom (58%) / 5.836 melhorias / 638 ruins (pico ruins 1.594 em 24/07). Inflexão 16/06 (30k→15k melhorias).
- Tabela: mobile CLS>0,1 = 5.836 URLs; LCP>4s = 638; INP = 0 problemas.
- CrUX campo home: LCP 1.623ms FAST · CLS 2 (0,002) FAST · INP 161ms FAST · FCP 1.483 FAST · TTFB 992ms AVERAGE. Lab PSI home: Perf 45, TBT 5.370ms (JS ads).

### Bot China (diagnóstico GA4 P30)
- 28.273 users country=China; language=Chinese 28.030 (engaj 39%, duração 6,1s); cities: "(not set)" 17.722 + Urumqi 10.223; browser Chrome 26.974; 24.607 views na HOME; tráfego constante 1,3–2,1k/dia desde ~25/07.
- Recalcular métricas GA4 extraindo China para "audiência real" (~122,5k users P30).

### Padrões de conteúdo (42 top posts × WP)
- Verbo de ação no título: score médio 11.884 vs 1.346 sem (**9×**).
- Comprimento título: 55–75 chars (top10 = 69 chars).
- Palavras: 450–800 = score 7.575/69s; >800 = 3.325/102s; ≤250 = 4.198/33s (alcance Discover).
- Categorias (score/post): Economia 15.838 🥇 · Geopolítica 3.692 (20 posts) · Eleições 2026 2.968 · Política 1.808 · Ceará 1.728 (1 post).
- Campeões absolutos P30: Moreira/dividendos (Economia, 694 pal, 24.920 views+21.210 GSC clk) · Datafolha-Lula-SP (1.177 pal, pos 1,7, CTR 6,4%) · Moreira-Demori (843 pal, viral contínuo desde 13/07) · Bolsonarista-Moraes (1.233 pal, 2.078 pts em 2 dias).

## O que aconteceu / o que falta / o que preciso do Miguel

- **O que aconteceu:** tudo coletado e analisado; relatório final em `Outros/google search/google search/analise_cafezinho_20260814/RELATORIO_ANALISE_GOOGLE_CAFEZINHO_20260814.md` + JSONs brutos na mesma pasta; fórum criado.
- **O que falta:** aplicar filtro GA4 anti-bot; cadência Discover; otimização CTR queries broad; CWV mobile backlog; redirects 404; validar AMP novos.
- **Miguel:** decidir filtro GA4 China (P1) e priorizar P2/P3.


---

## 🔬 ADENDO (15/08 ~00:40 BRT) — IDENTIFICAÇÃO DEFINITIVA DO "TRÁFEGO CHINA" = BOT (fingerprint de cliente, sem mexer em nada)

Miguel pediu identificação (não quer filtro). Provas novas:

**GA4 fingerprint do cliente (15/07–13/08, country=China):**
- Dispositivo: desktop 26.937 (95%) · OS: Windows 26.931 (95%)
- **Resolução de tela: 1600×1600 = 26.535 usuários (94%)** — resolução quadrada, default de headless Chrome; inexistente em humanos em massa
- **Versão do browser: Chrome 99.0.4844.51 = 26.027 (92%)** — Chrome 99 é de mar/2022 (4+ anos); nenhuma população real usa versão pinada de 2022
- Duração média 5,9s · engajamento inflado por auto-dismiss
- Contraste Brasil (real): 84% mobile (Android+iOS), duração 68–200s, resoluções diversas de aparelho real

**Nível servidor (access log origin `cafezinho-wp` 190.89.239.65):**
- Site atrás de proxy ServerDo (190.89.239.31/.244, HTTP/1.0) que **descarta X-Forwarded-For** (probe controlado com XFF 203.0.113.99 chegou limpo) e vhost loga formato combined sem IP real
- **Home é cacheada na borda** (probe `/?probe=` não chegou ao origin; `/wp-json/` e 404 chegam) → os hits dos bots na home nem chegam ao origin, logo IP deles só é visível na borda (Cloudflare/proxy) ou no cliente (GA4)
- Sem token Cloudflare no cofre (só R2) → sem acesso a firewall events/bot score da borda

**Conclusão:** bot farm com fingerprint fixo (Windows+Chrome 99+1600×1600), executando JS, concentrado na home. Diagnóstico forense fechado por 2 lados independentes (cliente GA4 + comportamento). Nenhum filtro aplicado (ordem do Miguel).
