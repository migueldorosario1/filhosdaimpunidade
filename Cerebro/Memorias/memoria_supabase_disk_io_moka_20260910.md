# 🗄️ Memória técnica — Investigação alerta Supabase Disk IO (Moka) — 10/09/2026

> Log técnico completo da investigação. Decisões/resumo: `../Foruns/forum_supabase_disk_io_moka_20260910.md`.

## Contexto

- 10/09 ~11:50 BRT: e-mail Supabase "Project is running out of Disk IO Budget" → projeto `nsasbuqeeqdwsagpfpcc` (org migueldorosario1). Miguel pediu explicação + prazo + custo + ver dados via API.

## Identidade do projeto (provas)

- `nsasbuqeeqdwsagpfpcc` = "Igotit", **Free**, org migueldorosario1 — memória `memoria_moka_espelho_experimentos_20260822.md` (nota sobre Redirect URLs 5→6).
- Compartilhado por Reader + Video + espelho: `CEREBRO_INDEX_MOKA_MASTER.md` linha 42 ("compartilhado Reader/Video"), `CEREBRO_NODE_BUGS_ATIVOS.md` linhas 46/311 (bug do redirect fallback Site URL).
- Nasceu do app igot: `/home/migueldorosario/ZCodeProject/igot/docs/PROJECT_ARCHIVE.md` (Project ID/URL/painel + schema `apps/web/supabase/schema.sql`, tabela `books` RLS `user_id = auth.uid()`, provider Google).
- Rio Carta = projeto DIFERENTE (`qznsodqyfwhaouruhsbp`, tabela comentarios) — `CEREBRO_INDEX_RIOCARTA.md` §6.

## Testes de API executados (10/09 ~13:1x BRT)

```
curl https://nsasbuqeeqdwsagpfpcc.supabase.co/auth/v1/health   # sem key → "No API key found" (normal)
curl -H "apikey: <anon>" .../auth/v1/health                    # → GoTrue v2.196.0 OK (projeto VIVO)
curl -H "apikey: <anon>" .../rest/v1/                          # → "Secret API key required" (normal p/ GET raiz)
mokareader.com                                                  # → 308 (redirect ok, no ar)
```

- Anon key disponível em: `ZCodeProject/moka-app/apps/web/.env.local`, `ZCodeProject/igot/.env.local`, `Moka-Producao/.env.local`, `Moka-Lab/.env.local` (valores NUNCA exibidos).
- **Management API (api.supabase.com) precisa de access token pessoal** — grep nos 2 `.env.unificado` (agentes_labs + Projeto Cafezinho Agentes) retornou ZERO variáveis SUPABASE. Não temos token → sem leitura de consumo por API.

## Modelo Disk IO Budget (docs oficiais, via busca — supabase.com dá 404 no WebFetch)

- 2 métricas: throughput (MB/s) e IOPS. Cada compute tem baseline; instâncias pequenas podem "burstar" acima do baseline por um tempo **por dia** = o tal budget.
- Zerou → throttle ao baseline: lentidão, IO wait sobe CPU, backups/autovacuum atrapalhados, pior caso instância não responde. **Não cobra, não desliga, não apaga.**
- Renovação: diária (hora exata não documentada).
- Causas comuns de consumo alto: memória alta (swap 1GB), cache hit rate baixo, queries >1s, tráfego alto.
- Fixes: otimizar queries/índices OU subir compute. No Free não há compra de compute; exige plano Pro (US$ 25/mês, crédito US$ 10; Small ≈ US$ 15/mês).
- Página do e-mail ("High Disk IO Consumption Guide") e /docs/guides/platform/io-budget: **404** no fetch automatizado (site bloqueia bot); conteúdo obtido via `supabase.com/docs/guides/troubleshooting/exhaust-disk-io` (WebFetch OK) + busca.

## Cron local (descartar causa nossa)

- `crontab -l | grep -iE "moka|supabase|igot"` → só `robo_supressao.py` (marketing, */30), que não toca o Supabase. Nenhum coletor local batendo no banco.

## Lições

1. **E-mail de "Budget" da Supabase NÃO é fatura** — não existe "prazo pra pagar" em plano Free; é aviso de throttle iminente com renovação diária.
2. WebFetch em supabase.com/docs/**io-budget** e no link do guia do e-mail → 404 (proteção anti-bot); usar a URL de troubleshooting ou busca web.
3. Para monitorar consumo/custos Supabase por API é preciso `SUPABASE_ACCESS_TOKEN` (dashboard → account/tokens) — hoje inexistente nos cofres; se o Miguel gerar, espelhar nos 2 `.env.unificado` (Regra Nº 4).
4. Confusão recorrente: existem DOIS Supabases no ecossistema (Moka `nsasbuqeeqdwsagpfpcc` × Rio Carta `qznsodqyfwhaouruhsbp`) — sempre citar o project ref.

## Timestamps

- Investigação: 10/09/2026 13:13–13:2x BRT (ZCode, GLM-5.3, sessão ZCodeProject).
