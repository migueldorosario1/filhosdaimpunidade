---
name: NYC não é só failover — é também backup TEMPORAL (cold-ish)
description: NYC deliberadamente mantém versão com atraso pra proteger contra erros humanos em Cingapura. Sync automático frequente destrói essa função. Sync raro/manual sob demanda.
type: feedback
originSessionId: 84d9e2a3-8768-4dc3-940f-82446d06d8f7
---
Decisão arquitetural: NYC cumpre DUAS funções simultâneas:
1. **Failover reativo** — via `orquestrador_failover.sh` (gate de 45min de tolerância por log)
2. **Backup temporal** — snapshot do código com atraso proposital

A segunda função é a MAIS importante. Permite Miguel+Claude+Antigravity ser ousado com deploys em Cingapura sabendo que se algo quebrar, NYC tem a versão sã de N dias atrás pra restaurar.

## Por que sync automático frequente quebra essa lógica
- `*/30min` ou `*/2h` propaga bug em minutos
- Se Miguel/Antigravity/Claude deployar código quebrado às 09:32, o bug chega no NYC às 09:35 e perde-se a rede de segurança
- Sync "desejável pra drift" destrói a proteção contra erro humano

## **Why:** filosofia "asynchronous replication with intentional lag" como proteção
Analogia: replicação PostgreSQL async com delay, ou snapshots de backup diários. NYC = time machine, não espelho.

## **How to apply:**
- **NÃO propor** sync automático frequente (*/5, */30min, */2h, horário) para NYC
- Sync manual sob demanda após deploys validados (como o que fizemos 2026-04-24 após dias sem sincronizar)
- Se drift for grande o bastante pra doer no failover, chamar `rsync` na hora — não virar cron
- `sync_nyc_leve.sh` 04h que já existe em Cingapura → questionar se ainda faz sentido; se toca muita coisa, pode estar violando essa filosofia
- Etapa 3 do plano original (`/root/sync_nyc.sh` + cron */5) é **ARQUIVADA** — não implementar

## Cadência recomendada
- Deploy crítico em Cingapura → validar 24-72h → sync manual pro NYC se quiser reduzir RPO
- Sem deploy → não sincronizar

## Estado atual (confirmado 2026-05-04 por Miguel)
- `sync_nyc_leve.sh`: **semanal** (`0 4 * * 0`, domingos 04h) — intencional, alinhado com filosofia de lag
- CLAUDE.md que documentava como "diário" estava desatualizado — a regra correta é semanal
- Backup primário real: **Backblaze B2 diário às 05h** (`sync_b2.sh` + `backup_sistema_v9.sh`), bucket `failover-cafezinho1`, lifecycle 30 dias
- NYC = failover rápido (ambiente já montado) | B2 = cold backup diário com retenção
