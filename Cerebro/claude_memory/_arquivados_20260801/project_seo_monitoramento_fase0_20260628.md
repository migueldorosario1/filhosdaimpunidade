---
name: project-seo-monitoramento-fase0-20260628
description: FASE 0 do fórum de investigação autoridade Google concluída 28/06 20:30 BRT — 3 crons monitoramento ativos no Tencent root + baseline Ahrefs/GSC/GA4/PageSpeed capturado
metadata: 
  node_type: memory
  type: project
  originSessionId: 595de6c5-a613-4f51-b42d-e3bc009de9ef
---

FASE 0 (baseline + infraestrutura monitoramento SEO Cafezinho) concluída 28/06/2026 20:30 BRT. 3 crons ativos no Tencent root: `util_cron_pagespeed_diario.py` (06:00 BRT, saída `/root/agent_data/pagespeed/diario_YYYYMMDD.json`), `util_cron_gsc_diario.py` (07:00 BRT, `/root/agent_data/gsc/`), `util_cron_ga4_semanal.py` (segundas 08:00 BRT, `/root/agent_data/ga4/semanal_YYYYMMDD.json`). Sentinelas crontab `GLM_20260628`. Backup crontab em `/tmp/crontab_bak_20260628_201710.txt`. PAGESPEED_API_KEY=`AIzaSyDGeKBX5gt2JdIUXozao-VFoL5uGVPOyL4` adicionada ao `.env.unificado` (backup `.env.unificado.bak_pre_pagespeed_20260628_201453`).

**Why:** Sprint noindex 358 URLs (27/jun 17:25) foi execução; faltava medir se funciona. Sem baseline estruturado + coleta automatizada, recovery SEO seria achismo. FASE 0 estabelece: (1) métricas-base em snapshot canônico, (2) coleta diária/semanal automatizada, (3) ponto de comparação para +90/+180/+365 dias.

**How to apply:** Próxima sessão que mexer com SEO/recuperação Google deve (1) checar últimos JSONs em `/root/agent_data/{pagespeed,gsc,ga4}/` antes de inferir estado; (2) consultar fórum `forum_investigacao_autoridade_google_20260628.md` v1.1 (seção FASE 0); (3) baseline Ahrefs em `Outros/google search/backlinks/baseline_ahrefs_20260628.md` é referência para comparação longitudinal. Próximo snapshot Ahrefs: 28/09/2026 (+90d).

**Achados críticos do baseline:**
- DR 50 / 47K traffic mensal (Ahrefs) — site NÃO está queimado
- 99,99% dos 220K backlinks são UR<10, ZERO backlinks DR 30+ (calcanhar de Aquiles)
- "Banco Master" é entidade #1 (56,9%) — anomalia a investigar (P0)
- 3.816 páginas 4XX (8,6%) — investigar P0
- TTFB 2023ms mobile / 2212ms desktop (SLOW) — vilão Core Web Vitals
- Concorrentes diretos (brasil247/poder360/pt.org.br) overlap baixo (0,3-0,4%) — Google não nos vê como site político BR

**APIs estado final:** PageSpeed ✅, GSC ✅, GA4 ✅, Indexing ✅ (pré-existente), Ahrefs Free ✅ baseline. Custom Search API ⏸️ pulada (billing exigido mesmo free tier).

Relaciona com [[project-sprint-recuperacao-seo-27jun-pausa]] (execução noindex) e [[reference-gsc-property-sc-domain-cafezinho]] (decisão técnica).
