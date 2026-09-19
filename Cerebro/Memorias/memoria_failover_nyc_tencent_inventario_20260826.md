# 🧠 Memória — FAILOVER NYC × TENCENT: inventário técnico bruto (26/08/2026)

> Par do fórum: `Foruns/forum_failover_nyc_tencent_plano_fim_de_semana_20260826.md`
> Autor: ZCode/Kimi K3 · Coleta: 26/08/2026 ~11:38–11:45 BRT, via SSH direto do Dell do Miguel.

## 1. Comandos usados

```bash
# NYC (DigitalOcean)
ssh -o BatchMode=yes root@198.199.121.136 'uptime -p; df -h / | tail -1; \
  systemctl list-units --type=service --state=running --no-pager --no-legend; \
  crontab -l'
# Tencent — porta 22 RECUSADA (Connection refused); a porta certa é 38422
ssh -p 38422 ubuntu@43.156.151.165 'uptime -p; df -h / | tail -1; \
  sudo -n systemctl list-units --type=service --state=running --no-pager --no-legend --plain; \
  sudo -n crontab -l; crontab -l; sudo -n ss -tlnp'
```
Acesso root direto `root@43.156.151.165` (porta 22) citado em fóruns antigos **não funciona mais** — usar sempre `-p 38422 ubuntu@` com sudo.

## 2. NYC `198.199.121.136`

- Uptime: 7 semanas, 2 dias. Disco: `/dev/vda1 48G, 37G usados, 11G livres, 78%`.
- Nota: a listagem systemd saiu truncada no primeiro comando (`cut -d" " -f1` sem `--plain`); serviços Augusto/Mayra confirmados pelo nodo ecossistema (verificar de novo na Fase 1 com `--plain`).

### 2.1 crontab root (dump integral, 26/08 11:40)
```
SHELL=/bin/bash
INTERLINK_DRY_RUN=0
0 * * * * cd /root && source chaves.sh && /usr/bin/python3 /root/remover_no_home.py >> /root/agent_data/remover_no_home.log 2>&1
14 6 * * * cd /root && /root/venv/bin/python3 /root/auditor_indexacao_posts.py --auditar >> /root/agent_data/auditor_index_posts.log 2>&1
52 * * * * cd /root && /root/venv/bin/python3 agente_performance.py >> /root/agent_data/performance.log 2>&1
0 8 * * * cd /root && /root/venv/bin/python3 augusto_fiscal_tokens.py >> /root/agent_data/fiscal_tokens.log 2>&1
0 3 * * * cd /root && /root/venv/bin/python3 agente_validador_modelos.py >> /root/agent_data/validador_modelos.log 2>&1
17 15 * * * cd /root && AUTOCURA_DRY_RUN=false AUTOCURA_ALLOW_REBAIXAMENTO=false /usr/bin/python3 agente_autocura_v4.py --deterministico >> /root/agent_data/autocura_v4.log 2>&1
0 8 * * * cd /root && /usr/bin/python3 agente_autocura_v4.py --resumo-diario >> /root/agent_data/autocura_v4.log 2>&1
0 14 * * 5 cd /root && /usr/bin/python3 agente_autocura_v4.py --relatorio-semanal >> /root/agent_data/autocura_v4.log 2>&1
7 * * * * PYTHONPATH=... PROMETHEUS_INSTANCE=cafezinho_failover_nyc python3 /root/push_metricas_llm_completo.py >> /home/ubuntu/prometheus_agent/llm_completo.log 2>&1
7 * * * * cd /root && /root/venv/bin/python /root/custos/coletar_custos_inteiros.py --write && gerar_relatorio_financeiro.py --write
0 6 * * * /usr/bin/python3 /root/caetano_auto_limpeza.py >> /var/log/caetano_auto_limpeza.log 2>&1
0 */2 * * * cd /root && /root/venv/bin/python3 agente_manchete.py >> /root/agent_data/manchete.log 2>&1
*/10 * * * * flock -n /tmp/auditor_titulos_gpt.lock /root/venv/bin/python3 /root/agente_auditor_titulos_gpt.py --modo poll
58 * * * * flock auditor_titulos_relatorio ... --relatorio-diario
7 3 * * * seo_pruning/seo_progressive_noindex.py
*/30 * * * * daemon_indexador.py
23 * * * * verificador_indexing_retroativo.py --horas 6
0 9 * * * util_cron_pagespeed_diario.py
0 10 * * * util_cron_gsc_diario.py
0 11 * * 1 util_cron_ga4_semanal.py
7 */2 * * * agente_repetidor_estatal.py
# V4_DESLIGADO_20260824 (ordem Miguel: só V4.1) — linhas de coletor/intake por vertical AINDA EXECUTAM (crons vivos, só o rótulo diz desligado — ambiguidade já notada no mapa de arquitetura 25/08):
0 * * * * v4_geopolitica (coletor.py geo + v4_vertical_intake.py geopolitica)
20 */6 * * * v4_nacional (pol)
35 */4 * * * v4_economia (eco)
5 */4 * * * v4_cultura (cul)
15 13/14/15 * * * meio_ambiente / esporte / saude
10,40 * * * * v4_ciencia (coletor.py tec + intake tecnologia)
# fins de semana (V4_FDS_BOOST): linhas extras 6,0 com V4_QUOTA_MIN=30 para as mesmas verticais
17 */6 * * * v4_media_mechanical_promoter.py --execute
47 6 * * * v4_media_expander.py --execute --leaders 3 --per-leader 2
25 */2 * * * cicero_remote/root/cicero_robo_coleta.py --run
*/15 * * * * rsync -a -e "ssh -p 38422" /root/agent_data/governanca_financeira_api_usage.jsonl /root/agent_data/banco_custos_$(date +%Y-%m).jsonl ubuntu@43.156.151.165:/home/ubuntu/cafezinho/v6_data/custos/   # CORRIGIDO_20260824
10 5 * * * cd /root/V3 && varredura_unificar_nomes_ouro.py   # DUPLICADO: também roda na Tencent 12:05
0 9 * * * atualizar_top10_espelho.py
*/30 * * * * agente_auditor_titulos_gpt.py --modo advisor
0 11,17 * * * /root/youtube_v2_pipeline.sh   # REATIVADO_20260823_ZM
*/30 * * * * v4_tendencias_intake.py
5 13 * * * entrega_auditor_loops.sh
25 * * * * top_tendencias_push.py   # TOP_TENDENCIAS_PUSH_20260819
30 23 * * * v4_labs codigo.tribunal_agentic_diario
25 */2 * * * v4_labs codigo.v41_ciclo                # V41_UNICO_20260824
35 1-23/2 * * * v41_ciclo --vertical economia
45 */2 * * * v41_ciclo --vertical ciencia
55 */2 * * * v41_ciclo --vertical geopolitica
* * * * * python3 /root/flusher_ao_vivo.py   # TELEMETRIA_AO_VIVO_§118 filtro não-LLM
0 12,18 * * * tematicos/agentes_tematicos/v4 orquestrador.py --all --sem-youtube
10,40 * * * * /opt/bot_news/run_bot_news.sh   # BOT_NEWS_20260825
*/30 * * * * python3 /root/transkriptor_detalhe.py   # TRANSCRITOR_DETALHE_§118_20260826
```
(Comando completo com argumentos no dump da coleta; aqui condensado preservando ritmo+alvo.)

## 3. Tencent `43.156.151.165` (SSH `-p 38422`, usuário ubuntu)

- Uptime: 19 semanas, 4 dias. Disco: `/dev/vda2 118G, 65G usados, 49G livres, 57%`.
- Serviços em execução: `cctv-v5.service`, `cctv-v6.service`, `midia-ouro-panel.service`, `painel-editorial.service`, `nginx.service`, `ssh.service` (38422), `fail2ban`, `cron`, `snapd`, `tat_agent` (agente Tencent Cloud), `unattended-upgrades`, systemd padrão.
- Portas: 8084 (cctv-v6 python3), 8083 (painel-editorial), 8091 local (midia-ouro), 8082 (cctv-v5), 80/443/8080 (nginx), 8778 local (`visao_proxy_gemini.py`), 8420 local (uvicorn pontos_api), 9100 local (node_exporter), 18789/18791/18792 local (`openclaw-gateway`), 38422 sshd.

### 3.1 crontab root
```
0 9 * * * flock precos_llm /root/venv/bin/python3 /root/agentes_cafezinho/atualizador_precos_llm.py
12 5 * * * cd /root/V3 && varredura_unificar_nomes_ouro.py   # duplicado NYC (10 5)
17 */6 * * * /root/V3/sync_banco_ouro_para_nyc.sh
27,57 * * * * /root/V3/puxar_faltas_ouro.sh
*/15 * * * * /root/scripts/monitor_chaves_api.py --test-api   # MONITOR_CHAVES_API_20260815
*/30 * * * * /root/agente_radar_tendencias.py   # RADAR_TENDENCIAS_P0_20260816
50 5 * * * /root/agente_performance.py   # DUPLICADO da NYC (52 * * * *)
5 6 * * * /root/regenera_diretriz_tendencias.py
```

### 3.2 crontab ubuntu
```
*/5 * * * * PROMETHEUS_INSTANCE=cingapura_tencent push_metrics.py
*/10 * * * * gerar_pulse_cafezinho.py
45 9 * * * CAFEZINHO_BATCH_SIZE=2 cafezinho_hourly_cron.sh
0 9 * * * moka/pontos_api vigia_saldos.py
*/15 * * * * moka/pontos_api descadastro.py
*/25 * * * * curl warm-cache CCTV 8084 (/audiencia, /, /baleia)   # WARM_CACHE_V6_20260816
*/5 * * * * cafezinho/v6/telemetria_export_pontos.py   # §118_TENCENT_20260824
* * * * * rsync root@159.89.185.209:/root/agent_data/banco_custos_$(date +%Y-%m).jsonl → ao_vivo_tematicos.jsonl   # temáticos (rio-ag)
0 12 * * 0 telemetria_reconciliador.py   # RECONCILIADOR_§118_SEMANAL
10 8 * * * telemetria_ceo_diaria.py
*/10 * * * * ss -tln | grep -q 8778 || setsid python3 visao_proxy_gemini.py   # watchdog do proxy de visão
*/30 * * * * curl 127.0.0.1:8084/api/farol-coletar   # FAROL_COLETOR_DB_20260825
3,33 * * * * rclone copy farol_audiencia.db → r2:cafezinho/farol/ + b2:failover-cafezinho1/farol/
10 4 * * * rclone copy custos + reconciliacao → r2:cafezinho/telemetria/
*/5 * * * * healthcheck_farol.py   # HEALTHCHECK_FAROL_§118_20260826
*/30 * * * * lumina_coleta.py   # LUMINA_COLETOR_§118_20260826
23 */6 * * * rclone copy lumina_audiencia.jsonl → r2 + b2   # LUMINA_TRIPE_R2B2_§118_20260826
```

## 4. Mecanismo de failover da era do enxarme (ainda em disco na NYC)

`ls -la /root/failover* /root/ativar_* /root/run_if_master.sh /root/agente_china_health.py /root/FAILOVER_ARMED` em 26/08:
```
-rw-r--r-- 1 root root    0 Jul  1 16:52 FAILOVER_ARMED
-rwxr-xr-x 1 root root 7362 May  9 22:22 agente_china_health.py
-rwxrwxr-x 1 root root 3574 Jun  8 12:53 ativar_cingapura.sh
-rwxrwxr-x 1 root root 2598 Jun  8 12:53 ativar_nyc.sh
-rwxrwxr-x 1 root root 1138 May  1 17:32 failover_armar_completo.sh
-rwxrwxr-x 1 root root 1070 May  1 17:32 failover_desarmar_silencioso.sh
-rw-rw-r-- 1 root root 6458 Apr 18 21:37 failover_manual.py
-rw-rw-r-- 1 root root 2234 May  1 16:31 orquestrador_failover.sh
-rw-r--r-- 1 root root  666 Apr 10 22:22 run_if_master.sh
```
Diagnóstico: os crons atuais de nenhuma das duas máquinas passam por `run_if_master.sh`; o mecanismo está desarmado na prática (modelo par-a-par não existe mais). Auditoria completa na Fase 1 do plano.

## 5. Duplicatas/drift já identificados ( Fase 1 )
- `agente_performance.py`: NYC `52 * * * *` × Tencent `50 5 * * *` — frequências DIFERENTES (horária × diária).
- `varredura_unificar_nomes_ouro.py`: NYC `10 5` × Tencent `12 5`.
- `agente_radar_tendencias.py` e `atualizador_precos_llm.py` só na Tencent; `agente_manchete.py` só na NYC.

## 6. Pontos de atenção herdados
- **Disco NYC 78%** — Enxutice Fase A (~14G) com dry-run pronto desde 07/08, aguardando "pode aplicar" (`forum_plano_enxutice_nyc_espelho_tencent_20260807.md`).
- crons V4 "desligados" por comentário ainda executam (mapa arquitetura 25/08) — considerar limpar ANTES do espelho de produção pra não duplicar coleta.
- Tencent porta 22 fechada; só 38422. Backups de crontab pré-failover antigos existem na NYC (`crontab_backup_pre_failover_armar_completo_20260701_165216.txt` etc.).
- Uptime Kuma vive na droplet utilitário `142.93.48.252` — casa natural do watchdog do plano (Fase 2.5).

## 7. Referências
- `CEREBRO_NODE_ECOSSISTEMA_CANONICO.md` §3.1–3.6 (papéis por servidor, 11/08)
- `Foruns/forum_dualidade_nyc_tencent_20260726.md` (histórico do mecanismo + regra anti-drift)
- `Foruns/forum_plano_enxutice_nyc_espelho_tencent_20260807.md` (disco NYC, Fase E)
- `Foruns/forum_plano_seguranca_contingencia_20260823.md` (P5 Servidores, bloco S5 02/09)
- `Memorias/memoria_mapa_servidores_ecossistema_20260806.md` (fotografia histórica)
