---
name: manchete-lock-purge-fix-20260715
description: "Sistema manchete Cafezinho — plugin hello-highlight + lock file no NYC + purge cache WP Rocket automatico. Fixes aplicados 15/07/2026 pra resolver \"manchete manual nao funciona\"."
metadata: 
  node_type: memory
  type: project
  originSessionId: 1c40a258-af33-4486-998a-a90995cc6a02
---

**Manchete-hero do Cafezinho é definida pelo plugin `hello-highlight` (Leandro Guedes, v0.1) via tabela `wp_highlights` — NÃO é categoria.** Miguel marcava manual mas agente_manchete sobrescrevia em 2h + cache WP Rocket segurava versão antiga.

**Why:** Miguel reportou "manchete manual não funciona" em 15/07/2026. Investigação revelou dois problemas em série: (1) `agente_manchete.py` no NYC roda a cada 2h via cron e sobrescreve manchete manual sem checar override, (2) plugin hello-highlight só faz UPDATE no banco mas não purga WP Rocket que segurava HTML antigo.

**How to apply:** Se surgir conversa sobre manchete Cafezinho, referenciar node `Cerebro/CEREBRO_NODE_MANCHETE.md` (documentação completa). Comandos rápidos:
- Travar manchete manual: `ssh root@198.199.121.136 'touch /root/agent_data/manchete_lock'`
- Destravar: `rm /root/agent_data/manchete_lock`
- Ver manchete atual: `curl https://controle.ocafezinho.com/wp-json/cafezinho/v1/manchete-status`
- Purgar cache manualmente: `curl -X POST -u "Redator:APP_PASSWORD" https://controle.ocafezinho.com/wp-json/cafezinho/v1/purge-cache`

Arquivos deployados 15/07:
- Novo mu-plugin: `/var/www/ocafezinho/wp-content/mu-plugins/cafezinho-purge-on-manchete.php` (hook AJAX + 2 endpoints REST)
- Patch: `/root/agente_manchete.py` no NYC (backup `.bak_pre_lock_purge_20260715_171057`)

**NÃO CONFUNDIR:** categoria "Destaques" (cat_id=5087) alimenta widgets secundários, NÃO define a manchete-hero. Cat "Redação" (cat_id=2403) é adicionada automaticamente pelo agente ao post-manchete pra compat de tema, mas também não é o mecanismo de manchete.

Ver também: [[forum-analise-gsc-completa-20260714]] (contexto SEO geral do Cafezinho).
