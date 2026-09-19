---
name: feedback-relatorios-53-deploy-alibaba-b2-cada-tick
description: Relatórios §53 Loop Maestro Cafezinho devem ter triplo deploy (Local PC + Alibaba + B2). Daemon sobe a cada tick §53 (sem cron — eu mesmo via scp + rclone). Caso fundador 17/06 18:10 BRT Miguel cobrou.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 8151465d-76ab-4d1d-bfe5-285d266e7ca7
---

# 📦 Relatórios §53 — triplo deploy obrigatório (Local + Alibaba + B2)

**Regra:** todo relatório `Projeto Cafezinho Agentes/Foruns/relatorio_monitoramento_*_loop53_30min.md` (ou variantes REFORMA / 24h / followup) DEVE estar deployado em 3 lugares:

| Camada | Path | Função |
|---|---|---|
| 💻 Local PC | `Projeto Cafezinho Agentes/Foruns/` | Origem viva (Daemon edita aqui) |
| 🟧 Alibaba | `root@39.106.184.215:/root/cerebro_trindade/root/agent_data/relatorios_maestro_cafezinho/{by_date,backups_diarios}/` | Espelho canônico no nó externo (vive com os Vigias `/root/cerebro_trindade/root/agent_data/vigias/`) |
| 🟪 B2 (Backblaze) | `b2:failover-cafezinho1/cingapura/relatorios_maestro_cafezinho/{by_date,backups_diarios}/` | Cold backup lifecycle 30d versões anteriores |

**Mecânica de sync (Miguel 17/06 18:10 BRT):** Daemon sobe a cada tick §53 (NÃO cron). Sequência:

1. Editar relatório local (append linha do tick).
2. SCP `.md` direto pro Alibaba: `scp <arquivo> root@39.106.184.215:/root/cerebro_trindade/root/agent_data/relatorios_maestro_cafezinho/by_date/`.
3. SCP `.md` pro Tencent `/root/agent_data/relatorios_maestro_cafezinho/by_date/` (staging).
4. `ssh ... sudo rclone copy /root/agent_data/relatorios_maestro_cafezinho/ b2:failover-cafezinho1/cingapura/relatorios_maestro_cafezinho/` (no Tencent).
5. Backup tar (fim do dia ou fim de pausa): tar+sha256 + scp pra `backups_diarios/` nos 3 lugares.

**Why:** Miguel cobrou 17/06 18:10 BRT que esses relatórios estavam só local (PC dele). "Todos esses relatórios eles tem que estar deployados no upload junto com o cérebro no Alibaba com backup indexados." Caso fundador 17 relatórios subidos em lote (17 `.md` + 1 tar = 188KB + 706KiB no B2). Sem deploy externo = perda total se PC quebra (ele reiniciou PC hoje 17:25 BRT — risco real).

**How to apply:** todo tick §53 que faz append no relatório do dia → também faz scp Alibaba + scp Tencent + rclone B2 antes de fechar o tick. Custom rotineiro, baixa latência (3 .md = ~60KB transfer, <5s total). Se SSH cair, registrar pendência no canal e tentar próximo tick. Tar diário 23:50 BRT (fim de tick noite) consolida.

**Não automatizar via cron Alibaba/Tencent puxando do PC** — Miguel descartou (PC pode estar desligado). Daemon sob demanda é o modelo.

**Vinculado a:** [[reference_cerebro_canonico_local_raiz_workspace]] (Alibaba `/root/cerebro_trindade/` é nó canônico externo) · [[feedback_indexar_relatorios_tick_no_cerebro]] (mesma família — índice + deploy = dupla rede).

**Estado 17/06 18:10 BRT:** primeira leva 17 relatórios subiu em todos os 3 destinos (sha256 do tar bate: `769ed05ad47458d8bfc67736f5019068d6df93bd2e2054d1320135408728a101`). Daqui pra frente é hábito.
