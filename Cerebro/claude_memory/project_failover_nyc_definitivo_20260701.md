---
name: failover-nyc-definitivo-20260701
description: NYC (198.199.121.136) é master primário desde 01/07/2026 — Tencent (43.156.151.165) silenciado por ordem Miguel há dias
metadata: 
  node_type: memory
  type: project
  originSessionId: 8dd532b4-0e93-4f61-b9a6-6a9c558362c2
---

**01/07/2026**: NYC (`198.199.121.136`) é o master primário ativo do pipeline Cafezinho. Tencent (`43.156.151.165:38422`) foi silenciado por ordem Miguel há dias — não é master há mais. Antigravity apenas formalizou/registrou o failover no fórum `sub_cerebro_antigravity_desktop.md` em 01/07/2026 14:04 BRT (commit `83c8053 docs: finalize NYC failover log entry`).

**Why:** Agentes automáticos tavam "meio descontrolados" e publicaram conteúdo questionável (1.317 posts spam IA clickbait que motivaram o SEO pruning). Miguel decidiu silenciar agentes automáticos editorial-publicadores para retomar controle manual. NYC agora roda só serviços systemd de bots Telegram (`augusto-cafezinho.service`, `mayra-cafezinho.service`, `zizilinda-cafezinho.service`) + cron jobs de agentes de monitoramento/análise (`agente_performance.py`, `agente_autocura_v4.py`, `agente_auditor.py`, `agente_monitoramento_humano.py`, `agente_contador.py`, `agente_memoria_v9.py`, `agente_validador_modelos.py`). Tencent silenciado (cron root com 1 linha só, load 0.03, ocioso).

**How to apply:**
- **NÃO** assumir que Tencent é master ao acordar em sessões novas. Verificar status: `ssh root@198.199.121.136 'crontab -l | wc -l'` (≥40 linhas = master) vs `ssh -p 38422 ubuntu@43.156.151.165 'sudo crontab -l | wc -l'` (1 = silenciado).
- **Crons novos** devem ir no NYC, não no Tencent. Espelho canônico `Projeto Cafezinho Agentes/root/crontab_server.txt` ainda reflete Tencent (LEGADO) — precisa ser migrado/atualizado ou criar `crontab_nyc.txt`.
- **Backup cron NYC duplo** (servidor + local) antes de qualquer deploy: server `/root/crontab_backup_pre_*.txt` + local `Projeto Cafezinho Agentes/root/crontab_nyc_backup_pre_*.txt`.
- **Failover NÃO foi unilateral** do Antigravity (corrigi essa interpretação errada inicial). Foi decisão Miguel há dias, Antigravity só registrou formalmente.
- **Estado dos agentes** (LTM, banco de mídia 62MB, scheduler, lições autocura) ficou no Tencent — se precisar acessar pra auditoria/migração, está disponível lá apesar de silenciado.
- ServerDo.in (`us65.serverdo.in` / `cafezinho-wp`) intacto — WordPress + mu-plugins continuam funcionando normalmente (não depende de master ser Tencent ou NYC).
- GA4 service account `/root/keys/ga4.json` confirmado presente e funcional em ambos os servidores.

Relaciona-se com [[seo-pruning-automatizado-20260701]] (cron migrado pro NYC), [[reference-servidor-wp-cafezinho-ssh]] (ServerDo.in intacto), [[project-seo-monitoramento-fase0-20260628]] (3 crons SEO monitoramento podem precisar migração também).
