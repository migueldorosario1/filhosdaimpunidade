---
name: seo-pruning-automatizado-20260701
description: Sistema SEO pruning progressivo (1.317 URLs P0/P1) deployado 01/07/2026 end-to-end — aguardando baseline Miguel + sanção cron
metadata: 
  node_type: memory
  type: project
  originSessionId: 8dd532b4-0e93-4f61-b9a6-6a9c558362c2
---

Sistema de saneamento SEO em lotes (`/root/seo_pruning/seo_progressive_noindex.py` no Tencent + mu-plugin `/var/www/ocafezinho/wp-content/mu-plugins/cafezinho-seo-pruning.php` no ServerDo.in) deployado e validado end-to-end em 01/07/2026 04:10 BRT. Smoke PASS: 3 URLs P0 (243733, 233024, 234885) retornando HTTP 410 real, homepage 200 intacto, endpoint REST auth token funcionando (401 inválido, 200 válido).

**Why:** June 2026 Spam Update começou 24/junho (em curso). 1.317 posts adicionais (1317 P0 spam IA clickbait + 284 P1 borderline + 2594 P1 categorias deny) precisam ser saneados progressivamente (100/dia às 03:07 BRT, ~13 dias para P0). Estratégia híbrida AD-1: P0 → 410 Gone (3-5x mais rápido p/ desindexar), P1 → noindex,follow (preserva option value). Parecer técnico GLM registrado em `Foruns/inbox_trindade/glm.md` (01/07 02:40 BRT) com 4 adendos: AD-1 híbrido 410/noindex, AD-2 transient cache TTL 5min, AD-3 baseline GSC/GA4, AD-4 kill-switch tráfego automático.

**How to apply:**
- Token `CAFEZINHO_SEO_PRUNING_TOKEN` sincronizado entre `/root/.env.unificado` (NYC + Tencent) e `wp-config.php` (ServerDo.in) — NÃO commitar em git.
- Cron `7 3 * * *` com sentinela `SENTINELA_SEO_PRUNING_GLM_20260701_NYC` **deployado no NYC** (master desde 01/07) em 01/07/2026 19:28 BRT. Primeiro lote 100 URLs P0 roda 02/07 03:07 BRT.
- Baseline GA4 setado no estado NYC: `organic_28d_avg = 2029` (média diária 28d, janela 03-30/jun). Kill-switch automático ratio<60% (=1217/dia).
- Estado em `/root/agent_data/seo_pruning_state.json` (NYC) — independente do estado Tencent (que tem smoke test das 3 URLs P0 243733/233024/234885 aplicado manualmente, sem sync).
- Após P0 completo (~13 dias): rodar `--decision P1_NOINDEX_ADICIONAL` (284 URLs) → depois `--decision P1_NOINDEX_CATEGORIA_DENY` (2594 URLs).
- Kill-switch manual: `ssh root@198.199.121.136 '/root/venv/bin/python3 /root/seo_pruning/seo_progressive_noindex.py --set-status paused'`.
- Plugin estático 358-URLs (`cafezinho-noindex-pruning.php` sprint 27/06) coexiste sem conflito no ServerDo.in.
- Backups cron NYC duplos: servidor `/root/crontab_backup_pre_seo_pruning_20260701_162851.txt` + local `Projeto Cafezinho Agentes/root/crontab_nyc_backup_pre_seo_pruning_20260701_162851.txt`.
- Snapshot da sessão: `Ponto de Retomada/GLM Coding/20260701_041301_sessao.md` (estado inicial Tencent) + atualização pós-failover neste arquivo.

Relaciona-se com [[feedback-wpmudev-updates-trava-php-fpm]] (mesma família bugs produção ServerDo.in) e [[project-seo-meta-bulk-cron-20260628]] (cron paralelo também no `/root/`).
