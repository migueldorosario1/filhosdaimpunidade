# 🧯 Fórum — Incidente GA4 backlog × página /v6/tendencias (03/09/2026)

**Ref:** DIAG-GA4-20260903 · **Sessão:** ZCode/GLM-5.3 · **Status:** DIAGNÓSTICO FECHADO, aguardando backfill do Google

## 1. O que aconteceu (queixa do Miguel, ~09:10 BRT)

O Miguel abriu `http://43.156.151.165/v6/tendencias` e estranhou: (a) "sinais quentes" citando **irã/ormuz** e **lula**; (b) **views do Top 10 muito baixos** (2 a 24 views/48h).

## 2. Método

1. HTML da página baixado e dissecado → seções e números exatos.
2. Código auditado: `painel_cctv_v6.py` (Tencent, rota `/tendencias` linha ~5795) + `top_tendencias_push.py` (NYC, alimenta o Top 10 via REST `wp-json/cafezinho/v1/top-tendencias`).
3. GA4 Data API consultada direto (property **374552425**, service account `/root/keys/ga4.json` no Tencent): por dia, por hora, realtime.
4. **FAROL** (`v6_data/farol_audiencia.db`, tabela `medicoes`: `online` = contador próprio; `views_ga4` = realtime GA4) comparado hora a hora.
5. Busca web de incidentes do Google.

## 3. Provas (a tríade que fecha o caso)

| Fonte | 27/08–01/09 | 02/09 (ontem) | 03/09 (hoje) |
|---|---|---|---|
| GA4 report (screenPageViews/dia) | 8.984–11.550 | **335 views / 93 users** | **zero linhas processadas** |
| GA4 report (views/hora) | 340–746/h | 1–50/h, **corte seco à 00h**, última hora 15h | nada |
| GA4 **realtime** | normal | **110–335 ativos o dia todo** (coluna FAROL) | **133 ativos agora** |
| **FAROL** (contador próprio) | 146–912 online | **257–790 online, dia normal** | 282–505 online, normal |
| GSC (Google Search Console) | — | **11.040 pessoas via busca** (mostrado na própria página) | — |

Conclusão: **tráfego real normal**; a tag `G-4E5DKNTYET` segue no HTML e disparando (realtime vivo). O **pipeline de REPORTING do GA4 está doente**: dia 02/09 quase congelado (329→335 views entre duas queries), hoje sem nenhuma linha, horas ausentes após 15h de ontem.

## 4. Causa raiz: incidente GLOBAL do Google (não é nosso)

Relatos públicos com o MESMO padrão (realtime OK, standard reports zerados/incompletos) começando 31/08–01/09:

- Reddit r/GoogleAnalytics: "GA4 Shows sharp drops on Aug 31 2026 data" — "We see realtime data, but no new data in standard reports" → https://www.reddit.com/r/GoogleAnalytics/comments/1w4chxu/
- Search Engine Roundtable: "Google Analytics Broken Again: September 1 Data Missing" → https://seroundtable.com/google-analytics-broken-42002.html

O backfill típico desses incidentes completa os dias em 24–48h (padrão documentado do GA4; ver também thread oficial support.google.com/analytics/thread/308344049 de incidente análogo).

## 5. Por que a página ficou "estranha" (irã/ormuz, lula, views baixos)

- **Top 10**: o algoritmo (`top_tendencias_push.py`) usa `screenPageViews` hoje+ontem por slug — metricamente correto; os valores são lixo porque a FONTE (GA4 report) está capada. Views 2–24 e scores ~0 são sintoma, não bug.
- **Sinais quentes**: o radar consolida 3 fontes (GA4 24h + GSC queries + ao vivo). Com o GA4 a 3% , micro-sinais viram "tendência": «lula» aparece porque o post Quaest tem 23 "leituras" GA4 (que hoje é o máximo); «irã/ormuz» sobrevive mais por GSC/Trends. Ruído por falta de base, não invenção da página.

## 6. Estado / o que falta / o que preciso do Miguel

- ✅ Diagnóstico fechado: nada no nosso código mudou; página fiel à fonte.
- ⏳ Falta: o Google fazer o backfill de 02/09+ (esperado em 24–48h, confirmar em 04–05/09).
- 🔀 Decisão do Miguel (não implementei nada): (a) deixar como está até o backfill; (b) eu adiciono banner "GA4 com atraso global" na página tendencias; (c) trocar/complementar a base do Top 10/radar com o FAROL enquanto o GA4 está doente (FAROL tem `online` por minuto, mas NÃO tem views POR POST — essa métrica por post só existe no GA4/GSC, então a opção realista é o banner + esperar).

## 7. Receita para checar o backfill (próxima sessão)

```bash
ssh tencent "cd /root && python3 - <<'EOF'
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import DateRange, Dimension, Metric, RunReportRequest
c = BetaAnalyticsDataClient.from_service_account_file('/root/keys/ga4.json')
r = c.run_report(RunReportRequest(property='properties/374552425', dimensions=[Dimension(name='date')], metrics=[Metric(name='screenPageViews')], date_ranges=[DateRange(start_date='2daysAgo', end_date='today')]))
[print(x.dimension_values[0].value, x.metric_values[0].value) for x in r.rows]
EOF"
```
02/09 saudável = ~10–11k views. Se em 48h não encher, reabrir o caso (aí seria problema na property, não backlog).

— ZCode/GLM-5.3, 03/09/2026
