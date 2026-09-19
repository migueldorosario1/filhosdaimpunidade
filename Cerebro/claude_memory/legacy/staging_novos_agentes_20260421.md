---
name: Novos agentes em produção — staging 1/dia publish 2026-04-21
description: Lula, IA, Latam, Sheinbaum, Mercado, Matriz Energética, Inflação — todos LIVE no crontab Tencent com 1 publicação/dia em status=publish.
type: project
originSessionId: 50202c88-5137-43d9-ac6f-5fb1c3ffc1d6
---
**Ativado 2026-04-21 ~15:45 BRT.** Miguel autorizou publicar (não draft).

## Disparos/dia (BRT)
- 09:30 `agente_master_lula.py` (editorial "Olhar do Stuckert", skip se plano A/B1/B2 vazio)
- 10:30 `agente_ia.py` (cat 5008 inteligência artificial)
- 11:30 `agente_latam.py` (15 feeds Latam Pátria Grande — ainda sem categoria dedicada)
- 13:30 `agente_sheinbaum.py` (5 feeds México)
- 15:30 `agente_mercado.py` (cat 5064, fail-fast yfinance)
- 17:00 `agente_matriz_energetica.py` — FOSSIL (dias ímpares) / TRANSICAO (dias pares)
- 18:30 `agente_inflacao.py` (cat 43, aborta se dia>15 pela regra freshness)

## Coletores
- `robo_coleta_latam.py` a cada 3h
- `robo_coleta_sheinbaum.py` 10h e 14h
- `robo_coleta_lula.py` 07h, 11h, 15h, 19h

## Mudanças de código pra habilitar publish
- `agente_ia.py:79`, `agente_mercado.py:123`, `agente_matriz_energetica.py:139` → `status="publish"`
- `agente_inflacao.py:240` → `status="publish"` (comentário "inflação SEMPRE draft" removido; Miguel autorizou 21/04)
- `agente_master_lula.py:191` → `como_rascunho=False`
- Latam/Sheinbaum no cron sem `--rascunho` (default do motor é publish)

## Backup + rollback
- Crontab anterior: `/root/agent_data/crontab_backup_pre_staging_20260421.txt` (123 linhas)
- Novo canônico: `/root/crontab_server.txt` (141 linhas)
- Reverter: `cat /root/agent_data/crontab_backup_pre_staging_20260421.txt | sudo crontab -`

## Categoria "Pátria Grande" (Latam+Sheinbaum)
Ainda não decidida. LLM categoriza automático → Latam cai em "argentina" (5012) ou "internacional" (15). Decisão A/B/C do `forum_novosagentes.md §2` segue pendente.

## Monitorar
```bash
ssh -i ~/.ssh/id_rsa -p 38422 ubuntu@43.156.151.165 "sudo tail -f /root/agent_data/master_lula.log /root/agent_data/agente_ia.log /root/agent_data/latam.log /root/agent_data/sheinbaum.log /root/agent_data/agente_mercado.log /root/agent_data/matriz.log /root/agent_data/agente_inflacao.log"
```
