---
name: Deploy de crontab precisa de coordenação humana
description: Miguel + Antigravity + Claude Code podem editar o crontab do Tencent em paralelo. Rollback acidental já aconteceu 2026-04-21 18:43.
type: feedback
originSessionId: aa80db10-86be-445e-a416-a07e41c62677
---
Deploy de crontab é multi-autor: Miguel edita via seu cliente, Antigravity edita durante ajustes (ex: redundância), Claude Code edita via SSH. **Nenhum canal único.** Em 2026-04-21 às 18:43 Miguel+Antigravity fizeram REPLACE que sobrescreveu silenciosamente o deploy do Claude Code das 17:08 (SHELL=bash, 7 temáticos novos, sync leve, Autocura V4). Claude Code só descobriu por acaso ao investigar por que Fantástico 19:05 não rodou. Restauração custou ~30min + forensics.

**Why:** syslog registra `REPLACE (root)` sem identificar sessão, então não há como detectar divergência em tempo real. E um carregamento inocente de "snapshot conhecido" como base apaga tudo feito em paralelo.

**How to apply:**
1. Antes de qualquer deploy novo de crontab no Tencent, Claude Code deve:
   - Fazer `stat /var/spool/cron/crontabs/root` e comparar com o mtime do último deploy registrado
   - Se mtime > último deploy conhecido, alertar Miguel e só deployar após confirmar
2. Sempre criar backup timestamped **antes** do REPLACE: `sudo crontab -l > /root/crontab_backup_pre_<motivo>_<ts>.txt`
3. Após o deploy, atualizar `Projeto Cafezinho Agentes/root/crontab_server.txt` (espelho canônico) imediatamente — permite diff rápido em próximo incidente
4. Em cada ciclo do monitoramento 24h, checar mtime do crontab e linhas principais (SHELL=bash, temáticos, autocura, sync leve) como sanity check
5. Se perceber regressão (ex: Fantástico deveria ter rodado e não rodou), investigar mtime do crontab PRIMEIRO antes de qualquer hipótese de bug de código
