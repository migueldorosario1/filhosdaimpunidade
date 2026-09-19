# Fórum — Saúde dos servidores + PLANO AUTOLIMPEZA (16/08/2026)

## 1. Saúde medida hoje

| Servidor | Disco | RAM | Load | Alertas |
|---|---|---|---|---|
| **Canônico** cafezinho-wp (190.89.239.65) | 48% (151G/335G) | 7,8Gi (2,6 livre) | **6,6 (alto)** | `/var/www` = **125G** (uploads+backups); reboot diário 03:30 (uptime 5h47) |
| **NYC** (198.199.121.136) | 68% (33G/48G) | 1,9Gi (1,1 livre — apertado) | 0,39 | agent_data 2,6G; logs 365M |
| **Tencent** (43.156.151.165) | 57% (64G/118G) | 7,5Gi (5,2 cache) | 0,15 | ok |
| **Espelho** (159.65.177.60) | 22% (17G/77G) | 3,8Gi | 0,06 | ok |
| **Alibaba** (39.106.184.215) | ⚠️ **HOST KEY MUDOU** | — | — | possível reinstalação ou ataque MITM — verificar no painel do provedor ANTES de qualquer ssh; nunca aceitar a chave automaticamente |

## 2. PLANO AUTOLIMPEZA (Cafezinho + temáticos)

### Princípios (regras do ecossistema)
- **Nada se apaga sem quarentena + manifesto** ("nenhum arquivo pode se perder"); quarentena desce p/ frio (B2) após N dias.
- **Dry-run primeiro**: toda regra roda 1 ciclo em modo relatório (só lista o que faria) antes de ativar.
- **Health-check pós-limpeza**: curl 200 home + post + WP_Query antes de dar por concluído; rollback = restaurar quarentena.

### Componentes
1. **Coletor diário** (`scripts/saude_servidores.sh`, cron 06:10 em todos os 4 servidores OK): df/free/uptime + top-10 dirs + contagens WP (transients, revisões, lixo, spam) → linha em `/var/log/saude_servidores.log` + sinc p/ Cérebro (`Cerebro/estado_servidores/AAAA-MM-DD.md`). Alerta se disco > 85% ou RAM livre < 300Mi.
2. **Regras de limpeza (cron semanal, seg 04:45, só age se disco > 70%):**
   - **Backups `.bak*` > 30 dias** (raízes, mu-plugins, temas, /root) → compactar p/ `/quarentena/bak_AAAA-MM/` + manifesto SHA; > 90 dias → B2 e remove local.
   - **Logs** (agent_data/*.log, /var/log): rotacionar > 14 dias (gzip), apagar comprimidos > 60 dias.
   - **WP uploads** (canônico 125G): mapear anexos órfãos (mídia não referenciada em nenhum post/meta) → quarentena (NUNCA apagar direto); revisar `smush-webp` antigo, `backup/`, `uploads/cache*`.
   - **WP banco**: transients expirados, revisões de post (limitar a 10/post via `wp post-revision` ou WP_ALLOW), lixeira > 30 dias, spam, oembed caches; `wp db optimize` mensal.
   - **Transcript/cache YouTube** (NYC): dirs de cache > 30 dias sem lock → quarentena.
   - **Revisão `<?` curto** (lição do incidente 16/08): varredura `grep -rln "^<?$"` em todos os temas/mu-plugins dos 2 WP → corrigir para `<?php` (já incluído como tarefa 0 da autolimpeza).
3. **Governança**: cada execução escreve linha no `MONITORAMENTO_DE_TRABALHO.md` e no log do Cérebro; rollback documentado por regra (onde está a quarentena e como restaurar).

### Implementação sugerida (fases)
- **Fase 0 (rápido):** varredura `<?` curto nos 2 WP + coletor de saúde diário no ar.
- **Fase 1:** regras de logs + backups `.bak*` (dry-run 1 semana, depois ativa).
- **Fase 2:** uploads órfãos do canônico (maior ganho: 125G) com quarentena + manifesto.
- **Fase 3:** banco WP (transients/revisões/lixo) + NYC agent_data/transcripts.
- Pendências Miguel: "vai" para as fases; decisão sobre a chave do Alibaba.
