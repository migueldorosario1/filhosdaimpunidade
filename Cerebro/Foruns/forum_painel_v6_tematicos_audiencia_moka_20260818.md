# Fórum — Painel CCTV V6: audiência dos temáticos + página própria do Moka (18/08/2026)

> Data: 2026-08-18 ~22:50 · Autor: ZCode/DeepSeek · Status: ✅ **NO AR E VALIDADO** (temáticos + /v6/moka)
> Ordem do Miguel (18/08 ~21:55): "na página sites temáticos do painel cctv, bota a audiência de cada um deles. cria também uma outra página, só para o moka reader, onde você vai listar os emails recebidos e detalhar audiência e uso do site, por país, tempo de uso, etc."

## O que foi entregue

**1. Audiência na página Temáticos (/v6/tematicos):**
- Linha "📈 30d: X usuários · Y páginas · Z sessões" em CADA card (janela fechada até ontem, GA4 Data API).
- Nova seção **"📈 Audiência dos temáticos — últimos 30 dias fechados"** com tabela por site + linha TOTAL.
- **Dados reais da primeira leitura (30d fechados):** Mundo Trilhos 12 · RioCarta 261 · Aiatolah 60 · GSN 164 · RailPost 43 · Discover Brazil 14 · Ceará Digital 50 → **TOTAL 604 usuários** (Mapa Rio sem GA4 instalado — card mostra isso).
- Fonte: os IDs numéricos GA4 dos 7 sites JÁ estavam no dict TEMATICOS do painel (sessões anteriores instalaram); a service account do painel (`BASE_DIR/root/ga4.json`, o canônico de julho) tem acesso a todos. ⚠️ Aviso: a tag vista no RailPost difere (site não apareceu no grep) — números dele podem estar submedidos; conferir depois.

**2. Página nova /v6/moka (nav "☕ Moka"):**
- **📧 E-mails recebidos (info@mokareader.com):** contadores (caixa, não lidas, enviadas) + tabela dos últimos 30 (data/remetente/assunto, remetente decodificado). IMAP GoDaddy direto do servidor do painel, senha lida do `.env` do pontos_api (nunca exposta), cache 10min.
- **📈 Audiência do site (GA4):** usuários ativos, páginas, sessões (30d fechados), tempo médio por sessão, tempo total engajado, **tabela por país (top 12)** e **por dispositivo**. ⚠️ **BLOQUEADO até o Miguel colar o ID NUMÉRICO da propriedade** (env `GA4_PROPERTY_MOKA` do cctv-v6) — a página mostra a instrução exata. Sem ele, exibe aviso.
- **💾 Uso do app (pontos_api):** usuários cadastrados, logins 7d, transcrições, consumos/pontos (SQLite local, cache 10min).

## Técnica

- Funções novas: `ga4_site_30d()`, `moka_inbox()`, `moka_pontos()`, `moka_ga4()`, `_fmt_seg()`, `pagina_moka()`; NAV + ROUTES `/moka`; CSS `.tabela`/`.num`.
- Backup: `painel_cctv_v6.py.bak_pre_tematicos_audiencia_moka_20260818` (servidor). py_compile ✅ (servidor 3.12; o 3.10 local não entende f-strings PEP 701 pré-existentes). Restart cctv-v6 ✅. Provas: /tematicos 200 c/ total 604; /moka 200 c/ e-mails decodificados e aviso GA4 correto. Primeira carga lenta (13s / 10s — 7 relatórios GA4 + IMAP); depois cache 30min/10min (2ms).
- Detalhe do cache: moka_inbox.json persiste em arquivo entre restarts (limpar manualmente após mudar decodificação — feito).

## O que falta / preciso de você (Miguel)

1. **Destravar o GA4 da página Moka (30 segundos):** abrir o GA4 da propriedade Moka Reader e me mandar o **ID numérico** — o número que vem depois de `p=` na URL do navegador (ex.: `analytics.google.com/analytics/web/#/p<b>123456789</b>/...`). Com ele eu configuro o env e testo.
2. Se, depois disso, a API negar acesso (403), aí será preciso dar permissão de **Visualizador** à service account `augusto-arquivista@gen-lang-client-0200069757.iam.gserviceaccount.com` (Admin → Gerenciamento de acesso à propriedade → Adicionar usuários) — eu te guio na hora.
3. Opcional: instalar GA4 no Mapa Rio (único temático sem medição).

---
— ZCode/DeepSeek, 2026-08-18


## ✅ ADENDO 19/08 ~01:35 — GA4 do Moka ACESO na página /v6/moka

- **ID numérico:** `550658820` (colado pelo Miguel; propriedade numa conta GA separada `a405267492` — não é a `a47408235` do Cafezinho).
- **Acesso:** o Miguel adicionou a SA `augusto-arquivista@…` como **Editor** em "Gerenciamento de acesso à conta" do Moka → Data API já lê (teste OK antes mesmo do env).
- **Config:** `Environment=GA4_PROPERTY_MOKA=550658820` na unit `cctv-v6.service` (backup `.bak_pre_moka_ga4_20260819`) + daemon-reload + restart.
- **Fix de métrica:** `averageEngagementTimePerSession` NÃO existe na Data API (erro 400) → trocada por `averageSessionDuration` (as duas edições: query e render).
- **1ª leitura (janela fechada até ontem):** 1 usuário · 1 página · 1 sessão · 0s engajamento (a tag só entrou no ar 18/08 ~18:45; números de hoje aparecem na janela fechada amanhã). Seções por país e por dispositivo renderizadas (vazias até acumular dados).
- **Pendências Miguel:** NENHUMA restante nesta missão. Restam as opcionais: GA4 no Mapa Rio + `socios-schema.sql` do Supabase.
