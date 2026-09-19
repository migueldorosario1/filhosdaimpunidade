---
name: feedback-ponte-robo-robo-git-gdrive-nyc-20260914
description: "A ponte de mensagens ENTRE ROBÔS tem 3 vias — Git canônica + GDrive rclone API + Mirror NYC (git remote). Telegram é canal humano Miguel, NÃO ponte robô. SSH cafezinho-wp é operação WordPress, NÃO ponte. Regra Miguel: sempre 2 vias ativas simultâneas."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 6424d2e0-280b-4dab-80c6-fffc0f353814
---

Em 14/09/2026 ~16:4x BRT, o Miguel corrigiu no chat CLI o conceito da ponte tripla robô-robô durante o teste PROVA-3PONTE-CM008: «o Telegram não é espelho. é git, gdrive e um outro que esqueci. o telegram é comunicação com humano, ou seja, eu. a ponte dos robôs não pode usar telegram — digo a ponte entre robôs». Em 16:5x completou: «o outro acho que é o próprio servidor NYC».

O ZM entregou a PROVA-3PONTE-ZM-20260914-001 (commit `6669089ec` no origin, 17:12 BRT) que confirmou tecnicamente os 3 canais reais + expôs o estado atual de cada.

**As 3 pontes robô-robô do ecossistema Cafezinho (2026-09-14):**

**(A) Git canônica** — `git@github.com:migueldorosario1/cerebro-miguel.git` branch `main`. Todos os agentes têm clone local, com crons de pull `0,15,30,45` + push `7,22,37,52` na Dell (padrão CONTRATO_PONTE_COMPLETA §Cadência). Escrita = `git commit + git push origin main`. É o canal principal.

**(B) GDrive via rclone API** — remote `drive:espelho-zcode/ponte_zcode/` acessado por comandos rclone (`rclone copy`, `rclone ls`) a cada 30min. Vive e atualiza normalmente (mtime 17:00 hoje na prova ZM). ATENÇÃO: o mount fuse `~/GDrive/ponte_laura_completa/` está com escrita parada desde 12/09 19:56 (rotina de escrita específica dessa pasta morreu) — **não usar o mount fuse pra Ponte B**; usar o remote API `drive:espelho-zcode/ponte_zcode/`.

**(C) Mirror NYC** — repo bare `nyc:/home/ubuntu/cerebro-miguel-mirror.git` acessado via git remote `nyc` (todo clone Dell tem `git remote -v` retornando este remote além do `origin`). Independente do GitHub — se GitHub cair, ainda tem git via SSH ao NYC. **HOJE ÓRFÃO desde 02/09** (13 dias): o cron `mirror_to_github.sh` no NYC (5min) falha contínua com `non-fast-forward`. Precisa reconciliar (proposta ZM: `git push nyc main` no sync 15min Dell + reconciliar mirror uma vez ~10min execução).

**NÃO SÃO PONTE ROBÔ-ROBÔ (usos legítimos, outros canais):**

- **Telegram** — canal HUMANO. `@pontelaura_bot` (Miguel↔CL exclusivo, 2 vias, scripts `~/.laura_tools/tg_alerta.sh` + `tg_ler.sh`); `@pontecafezinhobot` (alertas ZM/CM→Miguel, apenas envio). Comunicação com o dono, nunca robô-robô.
- **SSH ao cafezinho-wp / nyc** — canal de OPERAÇÃO do WordPress e da fábrica V4.1. É por onde robôs (CM, CL, AGY-M, claudionor) executam wp-cli, scripts `/tmp/clNNN.sh`, gates. Não é ponte de mensagens/blocs.
- **Path Antigravity espelho passivo** (`~/Downloads/Antigravity Google/Cerebro/Foruns/ponte_laura_completa/`) — reverse-sync 15min do canônico via cron. É espelho local do git canônico, útil como cópia read-only. Pode contar como redundância local mas depende do git canônico existir; se A cai, este também para (fica travado no último sync).

**Regra Miguel** (14/09): **sempre 2 vias ativas simultâneas**. Se A cai, B + C mantêm 2. Se B cai, A + C. Se C cai, A + B. Nunca 1 só. Hoje real: **2 sólidas (A git + B GDrive espelho-zcode) + 1 candidata órfã 13d (C mirror NYC)** — aguarda autorização Miguel pra ZM reconciliar.

**Como diagnosticar as pontes num setup novo:**

1. `git remote -v` no clone local — se aparecer `nyc → nyc:...cerebro-miguel-mirror.git` além do `origin`, você tem a ponte C configurada.
2. `mount | grep GDrive` — se tem fuse rclone mount, você tem acesso via filesystem; verifique tanto mount fuse quanto rclone API remote (`rclone lsd drive:` mostra os folders).
3. `cd ~/cerebro-miguel && git rev-parse HEAD` vs `git ls-remote origin main` — confirma que canônica GitHub está sincronizada com seu local.

**Cuidado ao declarar prova 3 pontes** (aprendizado do CM):

- Não confundir «acesso ao WordPress via SSH» com «ponte de mensagens»
- Não confundir «Telegram» com «canal robô»
- Verificar o remote `nyc` no clone local antes de declarar «não tenho terceira via» (provavelmente tem)
- Se o mount fuse GDrive parece congelado, teste rclone API direto (`rclone ls drive:espelho-zcode/ponte_zcode/`) — pode estar vivo por outra pasta

**Ligação com outras memórias:**

- [[feedback-ponte-canonica-cerebro-miguel-20260829]] — canônica sempre `~/cerebro-miguel`, escrever aqui + push origin
- [[feedback-verificar-markers-conflito-antes-git-push-20260914]] — antes de commit + push, checar markers
- [[feedback-check-cm-ponte-laura-a-cada-loop-20260822]] — CHECK CM em cada ronda mantém agente visível na ponte
- [[project-wp-agent-connector-instalado-20260908]] — App Password REST via WP Agent Connector (canal de escrita no WP, não ponte)
