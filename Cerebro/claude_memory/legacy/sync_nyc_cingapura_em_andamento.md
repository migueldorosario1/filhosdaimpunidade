---
name: Sync NYC ↔ Cingapura — Etapa 2 concluída, Etapa 3 bloqueada, ressync manual 2026-04-24
description: Failover manual LIVE via orquestrador_failover.sh (porta 38422). Ressync Cingapura→NYC em 2026-04-24 08:56 BRT deixou 225 .py gêmeos. Etapa 3 (sync automático) ainda bloqueada.
type: project
originSessionId: 84d9e2a3-8768-4dc3-940f-82446d06d8f7
---
**Documento fonte:** `Projeto Cafezinho Agentes/planodesicronia_nycecingapura.md`

## Etapas 1+2 — CONCLUÍDAS
- Sync Cingapura→NYC com opção X (Shared-Nothing: código gêmeo, estado runtime isolado)
- SSH Cingapura→NYC OK (chave `/root/.ssh/id_ed25519_nyc_sync` em Cingapura, pubkey no authorized_keys do NYC)
- `/root/failover_manual.py` em ambos + `bot_augusto.py` com `/mudar_servidor` (Cingapura PID 1163267)
- Script CLI `Projeto Cafezinho Agentes/failover_manual.sh` no laptop

## Gate real em produção: `/root/orquestrador_failover.sh` (NYC)
Não é o `run_if_master.sh` (este tem bug de porta — ver abaixo). Os crons do NYC usam `orquestrador_failover.sh`:
- Testa porta **38422** (correta) de Cingapura via `nc -z -w 5`
- Fase 2: conecta via SSH e lê `stat -c %Y` do log do agente em Cingapura; se idade > tolerância (45min), assume
- Tem `flock` pra evitar dupla execução

**Teste ao vivo 2026-04-24 08:57:** `[STANDBY PASSIVO] Cingapura atualizou maestro.log ha 5 mins. NYC dormindo.` ✓

## Ressync manual 2026-04-24 08:56 BRT
Rsync Cingapura→NYC (sem `-a`, com `--no-o --no-g --checksum`, sem `--delete`):
- 9 .py atualizados no NYC: flickr_live, gerar_token_youtube, postador_meta, postador_twitter, processador_imagem, robo_coleta_lula, scratch_test, test_wp, test_yt_auth
- Pós-sync: **225 arquivos gêmeos (MD5 match)**, 0 diffs, 44 legacy extras no NYC preservados
- Backup dos .py anteriores em `/root/backup_sync_20260424_0838/` no NYC
- Deploys críticos já estavam gêmeos antes (util_fonte, agente_mercado, motor_publicador, publicador_tematicos, agente_ferroviario_v2)

## Episódio 2026-04-21 19:40-19:55 BRT
Durante o caos do incidente .env, NYC assumiu: master_geopolitica rodou no NYC e timeou em 300s; analytics executou; fantastico rodou até 19:17. Comportamento esperado — Cingapura ficou 45min+ com maestro.log parado. Depois voltou STANDBY.

## ✅ `run_if_master.sh` corrigido 2026-04-24 09:00 BRT
Porta 22→38422. Backup em `/root/run_if_master.sh.bak_20260424`. Mesmo assim **não está em uso** pelos crons (que usam `orquestrador_failover.sh`), mas agora está correto caso seja invocado.

## ✅ Crontab parcialmente simétrico — 10 temáticos adicionados 2026-04-24 09:00 BRT
- NYC: 32→42 crons (de `orquestrador_failover.sh`)
- Adicionados: master_lula, agente_ia, latam, sheinbaum, agente_mercado, matriz(2x FOSSIL/TRANSICAO), agente_inflacao, militar, crime — todos com gate tolerância 45min
- Backup crontab NYC pré-mudança em `/root/crontab_backup_pre_sync_temáticos_20260424_0900.txt` (102 linhas)

**VALIDADO 2026-04-24 09:30-09:34 BRT — master_lula primeiro trigger pós-add:**
- Cingapura publicou normalmente: post 239175 às 09:32:32 ("Lula cobra qualidade e inovação no agronegócio")
- NYC gate: `[STANDBY PASSIVO] Cingapura atualizou master_lula.log ha 1 mins. NYC dormindo.` ✓
- Zero dupla publicação (WP API confirma — só 239175 Lula entre os 3 posts recentes)
- Teoria confirmada: 45min de tolerância é seguro mesmo para 1x/dia porque no horário do cron, o `>>` do bash em Cingapura toca o log em milissegundos antes do SSH stat do NYC.

**Pendente:** validar os outros 9 gates conforme seus horários (agente_ia 10:30, latam 11:30, sheinbaum 13:30, mercado 15:30, matriz 17:00, inflacao 18:30, militar 14:00/20:00, crime 14:15/20:15).

## Etapa 3 — ARQUIVADA 2026-04-24
Miguel rejeitou sync automático (*/30min ou */2h): **NYC é backup temporal, não espelho**. Ver `arquitetura_nyc_backup_temporal.md`.

## Rodada 12 do forum_failover.md — ações executadas 2026-04-24 10:00-10:20 BRT
**Auditoria crítica primeiro:** Antigravity alegou "Backblaze B2 já integrado" — mentira. `/root/mayra_sync_cron.py` marca B2 como TODO, sem rclone instalado, sem chaves B2 em `chaves_novas.env`. Expansão B2 bloqueada até Miguel confirmar conta. Ver `feedback_antigravity_alega_desfazer_mas_nao_desfaz.md`.

**5 ações validadas e executadas (todas com backup):**
1. **44 legacy .py arquivados** em `/root/_legacy_archive/` no NYC. `/root/` agora tem só 225 .py (espelho Cingapura). README explica critério e rollback.
2. **`sync_nyc_leve.sh` espaçado** para `0 4 * * 0` (domingo). Próxima execução: 2026-04-26 04:00. Backup: `/root/crontab_backup_pre_spacing_sync_nyc_20260424_1015.txt` em Cingapura.
3. **Alerta Telegram em `orquestrador_failover.sh`** — função `alertar_telegram()` dispara via TELEGRAM_TOKEN_AUGUSTO pra chat_id 1894890759 em 3 pontos (QUEDA_TOTAL/SSH_STAT_FAIL/AGENTE_X). Flag diária evita spam. Fail-silent se curl falhar. Teste de entrega: Telegram retornou `OK`. Backup: `/root/orquestrador_failover.sh.bak_20260424_1020` no NYC.
4. **Tolerância dinâmica** nos 10 temáticos novos do crontab NYC — já era crítico: master_lula idade 46min (>45 tol antigo) e crime idade 123min (>45) iam disparar failover indevido AGORA. Novas tolerâncias:
   - 1500 min (1×/dia): master_lula, ia, latam, sheinbaum, mercado, matriz (FOSSIL+TRANSICAO), inflacao
   - 480 min (3×/dia): militar
   - 600 min (a cada 6h): crime
   - Backup: `/root/crontab_backup_pre_tolerancia_current_20260424_1020.txt` no NYC
5. **`run_if_master.sh` porta 22→38422** — corrigido de manhã, continua válido. Não é usado pelos crons (que usam orquestrador), mas agora está correto se invocado.

## Bloqueado
- Q6 (Augusto despertar sob demanda no NYC) — design OK mas complexo. Systemd unit + flag de estado compartilhada entre jobs. Aguarda ok Miguel.

## Rodada 14 (2026-04-24 11:15-11:25 BRT) — sync B2 LIVE
Miguel criou bucket `failover-cafezinho1` do zero (Antigravity havia alucinado integração prévia):
- Encryption SSE-B2 Enabled, Lifecycle 30 dias, endpoint `s3.us-east-005.backblazeb2.com`
- Application Key escopada ao bucket (read+write)
- `rclone v1.60.1` + `sqlite3` instalados via apt em Cingapura
- Profile `[b2]` em `/root/.config/rclone/rclone.conf` (perms 600)

**Script deployado:** `/root/sync_b2.sh` em Cingapura. 3 fases:
1. `sqlite3 .backup` do DB de mídia pra `/tmp/staging/` (snapshot consistente sem bloquear writers)
2. `rclone sync /root → b2` com filter ancorado `+ /*.py` + configs + `mayra_brain/`, exclui `banco_midia/`
3. `rclone copy` do snapshot DB separado
Flag falhas consec + alerta Telegram após 2 falhas via Augusto.

**Cron Cingapura** (crontab 145→148): `0 5 * * * bash /root/sync_b2.sh`. Próxima execução cron: 2026-04-25 05:00 BRT. Backup `/root/crontab_backup_pre_sync_b2_20260424_1123.txt`.

**Run real validado 11:22:04-11:22:41:** 37s total, 233 arquivos ≈ 98 MB no bucket. Fases OK.

**2 bugs corrigidos durante deploy:**
- Filter `+ *.py` globals pegou subpastas indesejadas (`cingapura_workspace/`) — fix: ancorar com `/` (`+ /*.py`)
- `rclone sync` abortava com `source file is being updated` no DB 94MB — fix: snapshot `sqlite3 .backup` primeiro

**Custo estimado:** ~$0.36/mês (com DB mídia, 30 versões × 2GB). Upload grátis ilimitado, download 3× armazenado/mês grátis.

## Arquitetura final de backup (3 camadas)
| Camada | Quando | RPO | Retenção |
|---|---|---|---|
| Cingapura master | contínuo | 0 | atual |
| NYC warm standby + time-machine | domingo 04h | 3-7 dias | 1 versão |
| Backblaze B2 cold | diário 05h | 24h | 30 versões |

## Pendências
- Q11 Augusto despertar sob demanda no NYC — fórum próprio
- Revogar Application Key B2 colada em chat → gerar nova (Miguel faz, eu substituo rclone.conf)
- Validar primeiro run cron das 05h amanhã (25/04)

## Auditoria `failover_manual.py` 2026-04-24 12:30 BRT
Script em `/root/failover_manual.py` em ambos servidores (idênticos). Funções: `migrar_cingapura_para_nyc()`, `migrar_nyc_para_cingapura()`, `status_atual()`. CLI: `python3 failover_manual.py [status|para_nyc|para_cingapura]`.

**Fluxo `para_nyc`:** precheck canônico × 2 → backup crontab Cingapura → `crontab -r` em Cingapura → `crontab crontab_server.txt` no NYC via SSH → cria flag `/root/nyc_operou_sozinho.flag` no NYC. **Tempo: 5-7s.** Depois: 0-10min pra maestro NYC rodar, 1h pra 90%, 24h pra 100%.

**3 problemas identificados:**
1. **Canônico DESATUALIZADO (22/04)** — `crontab_server.txt` em ambos estava de 22/04, não tinha `sync_b2`, tinha ferroviário ativo (na verdade pausado no live), `sync_nyc_leve` diário (não domingo). **RESOLVIDO 12:37:** atualizei o canônico nos 2 servidores pro estado live de hoje (MD5 match `1b5fcfd9ef1b10d64a1ee2af6634a50f`, 149 linhas). Backups: `/root/crontab_server.txt.bak_20260424_1130` em ambos.
2. **Ordem de falha perigosa** — script desliga Cingapura ANTES de testar NYC. Se NYC inacessível no momento, **ambos ficam sem crons**. Deveria inverter: ligar NYC primeiro, validar, depois desligar Cingapura. **PENDENTE** — não patched.
3. **NYC perde gates ao voltar de failover** — `migrar_nyc_para_cingapura` faz `crontab -r` no NYC, que fica vazio. Precisa restaurar os 42 gates. **RESOLVIDO 12:37:** salvei os 40 gates + 2 coletores stats em `/root/crontab_nyc_gates_canonico.txt` no NYC (114 linhas, 10863 bytes). Restauração pós-failover: `crontab /root/crontab_nyc_gates_canonico.txt`.

Nenhum failover foi executado — só ajustes preparatórios técnicos. Sistema continua publicando em Cingapura.
