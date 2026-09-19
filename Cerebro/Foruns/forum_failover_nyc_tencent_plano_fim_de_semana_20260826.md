# 🌉 Fórum — FAILOVER NYC × TENCENT: mapa vivo + plano de trabalho do fim de semana (29–30/08)

> **Par técnico (log completo):** [`Memorias/memoria_failover_nyc_tencent_inventario_20260826.md`](../Memorias/memoria_failover_nyc_tencent_inventario_20260826.md)
> **Autor:** ZCode/Kimi K3 · **Data:** 26/08/2026 ~11:50 BRT
> **Origem:** ordem do Miguel ~11:30 ("faz um plano de trabalho pra gente fazer o failover... o que a gente tá usando em Tencent, o que a gente tá usando em Nova York... qual a maneira mais segura... no final de semana, se cair algum servidor a gente usa o outro")
> **Status:** PLANO PRONTO PARA O FIM DE SEMANA — aguardando "vai" do Miguel
> **Antecessores:** `forum_dualidade_nyc_tencent_20260726.md` (mecanismo da era do enxarme) · `forum_plano_enxutice_nyc_espelho_tencent_20260807.md` (Fase E, disco NYC) · Plano Segurança & Contingência P5/S5 (02/09)

---

## 1. A mudança de paradigma (por que o failover antigo não serve mais como está)

O mecanismo de failover da era do enxarme (abril–julho) ainda existe na NYC (`failover_armar_completo.sh`, `failover_manual.py`, `orquestrador_failover.sh`, `ativar_nyc.sh`, `ativar_cingapura.sh`, `run_if_master.sh`, `agente_china_health.py`, flag `FAILOVER_ARMED` de 01/07). Ele foi feito para quando **as duas máquinas rodavam a mesma carga** (espelho par-a-par).

**Hoje a arquitetura DIVERGIU:** NYC e Tencent não são mais espelhos, são **complementares**. Um failover "flip de master" puro não cobre o estado atual — o plano abaixo reconstrói a redundância por função.

## 2. MAPA VIVO (verificado por SSH em 26/08/2026 ~11:40)

### 2.1 NYC — `198.199.121.136` (DigitalOcean) — "a fábrica"
Uptime 7 semanas · **disco 78% (37G/48G, 11G livres — atenção)**

| Função | Componente | Ritmo |
|---|---|---|
| **Produção oficial Cafezinho** | `v41_ciclo` (V4.1 único desde 24/08) | cron */2h por vertical |
| Coleta V4 (desligada por comentário, crons ainda rodam) | `coletor.py` + `v4_vertical_intake.py` | várias |
| Repetidor Estatal | `agente_repetidor_estatal.py` | 7 */2h |
| YouTube/Transkriptor GSN | `youtube_v2_pipeline.sh` + `transkriptor_detalhe.py` | 11/17 UTC · */30 |
| Bot News | `/opt/bot_news/run_bot_news.sh` | */10 |
| Sites temáticos (8) | `orquestrador.py --all --sem-youtube` | 12,18 UTC |
| SEO/indexação Google | `daemon_indexador.py`, auditor, seo_pruning, GSC/GA4/PageSpeed | */30 + diários |
| Auditoria de títulos | `agente_auditor_titulos_gpt.py` (poll/advisor/relatório) | */10, */30 |
| Ponte Telegram | Augusto (`augusto-cafezinho.service`) + Mayra (`mayra-cafezinho.service`) | serviço |
| Infra/autocura | `agente_autocura_v4.py`, validador de modelos, fiscal de tokens, manchete | diário / */2h |
| Custos/telemetria | `coletar_custos_internos.py` + `flusher_ao_vivo.py` (por minuto) + rsync → Tencent */15 | contínuo |
| Top 10 espelho | `top_tendencias_push.py`, `atualizar_top10_espelho.py` | horário/diário |
| Cícero coleta + Tribunal agêntico | `cicero_robo_coleta.py`, `tribunal_agentic_diario` | */2h · diário |
| Banco Ouro | **réplica read-only** (sync da Tencent */6h + faltas */30) | passivo |

### 2.2 Tencent — `43.156.151.165:38422` (porta 22 fechada!) — "a torre de controle"
Uptime 19 semanas · disco 57% (65G/118G)

| Função | Componente | Porta/ritmo |
|---|---|---|
| **CCTV V6 (painel canônico)** | `cctv-v6.service` + páginas `/v6/*` | 8084 |
| CCTV V5 (camada anterior, viva) | `cctv-v5.service` | 8082 |
| Painel editorial | `painel-editorial.service` | 8083 |
| Painel Mídia Ouro | `midia-ouro-panel.service` | 8091 (local) |
| nginx público (painéis + email) | `nginx.service` | 80/443/8080 |
| **Banco Ouro MASTER** | `/root/agent_data/banco_midia_ouro_v3/` + `robo_banco_ouro_midia_v3.py` | empurra p/ NYC */6h |
| **Proxy de visão (túnel)** | `visao_proxy_gemini.py` (usado pela cascata dos temáticos NYC) | 127.0.0.1:8778 |
| Moka pontos_api | `pontos_api` (vigia_saldos, descadastro, uvicorn) | 8420 |
| Hub de telemetria §118 | recebe custos NYC */15 · puxa temáticos (rio-ag) por minuto · reconciliador · CEO diária | contínuo |
| FAROL | coletor */30 + healthcheck */5 + backup R2+B2 */30 | contínuo |
| LUMINA | coleta */30 + backup R2+B2 */6h | contínuo |
| Radar/preços/performance | `agente_radar_tendencias.py`, `atualizador_precos_llm.py`, `agente_performance.py` (duplicado da NYC!) | vários |
| Monitor de chaves API | `monitor_chaves_api.py --test-api` | */15 |
| Prometheus push | `push_metrics.py` (`cingapura_tencent`) | */5 |

### 2.3 Pontes entre os dois (dependências cruzadas)
- NYC → Tencent: rsync de custos a cada 15 min; cascata de visão usa o túnel 8778 da Tencent.
- Tencent → NYC: Banco Ouro master empurra réplica a cada 6h.
- Tencent → rio-ag (159.89.185.209): puxa custos dos temáticos por minuto.

### 2.4 O que JÁ tem redundância (não entra no plano)
- **Sites no ar NÃO dependem de NYC nem Tencent:** ocafezinho.com vive no ServerDo (`190.89.239.65:51439`) com espelho horário Cafezinho News (`159.65.177.60`); temáticos publicam nos próprios WP (rio-ag/GSN WP). Queda de NYC/Tencent **não tira nenhum site do ar** — para a produção de material novo e some a observabilidade.
- Dados do FAROL/LUMINA/telemetria já no tripé R2+B2+Cérebro (diretriz 24/08).
- Cérebro: GitHub + B2 + Drive.

### 2.5 O que NÃO tem redundância (os alvos do plano)
| Se cair... | morre... | impacto |
|---|---|---|
| **NYC** | produção V4.1, Augusto/Mayra, SEO/indexação, YouTube, bot news, temáticos | nenhum post novo; ponte Telegram muda; indexação para |
| **Tencent** | CCTV V6/painéis, FAROL, LUMINA, Banco Ouro master, pontos_api Moka, proxy visão 8778 | ficamos cegos dos painéis; mídia nova trava; temáticos perdem 1 perna da cascata de visão (gemini→qwen-vl R2 seguem) |

## 3. A MANEIRA MAIS SEGURA (princípios aprovados neste fórum)

1. **Detecção automática, troca MANUAL.** Watchdog (Uptime Kuma) avisa no Telegram; o flip é executado por runbook, nunca 100% automático — positivo-falso criaria **dois escritores ativos** (post duplicado, bot de Telegram duplicado, dois masters de banco). O modo automático antigo (`agente_china_health.py`) fica arquivado como referência.
2. **Regra do escritor único:** WP (publicadores), bot Telegram e Banco Ouro master têm UM dono ativo por vez. Todo standby fica **instalado e desligado** — ligar = 1 comando documentado.
3. **Backup antes de qualquer toque:** crontabs, código e configs → B2 `failover-cafezinho1` + Cérebro, com sha256; snapshots de droplet nos consoles dos provedores.
4. **Uma mudança por vez, com prova e rollback** (smoke test + `.bak` datado).
5. **DNS não se toca** nos simulados (painéis são acessados por IP:porta; sites não dependem desses hosts).

## 4. PLANO DE TRABALHO DO FIM DE SEMANA (29–30/08)

### Fase 0 — sexta 28/08 à noite (~1h): PREPARAÇÃO
1. Backup dos 2 crontabs (root NYC + root/ubuntu Tencent) → Cérebro + B2.
2. tar do código vital: NYC `/root/v4_labs`, `/root/*.py`, `/root/tematicos`; Tencent `/home/ubuntu/cafezinho/v6`, `/root/V3`, `/etc/nginx` → B2 `failover-cafezinho1/failover_202608/`.
3. **Snapshot das duas droplets nos consoles** (DigitalOcean + Tencent Cloud) — já serve como teste de acesso a console (exigência P5/S5 de 02/09).
4. Conferir saúde do tripé R2/B2 (farol, telemetria, lumina já sobem).

### Fase 1 — sábado 29/08 manhã (~2h): AUDITORIA
1. Diff de drift dos scripts que existem nos DOIS (`agente_performance.py`, `varredura_unificar_nomes_ouro.py`) — regra do fórum de 26/07: drift = bug fantasma no flip.
2. Auditoria do mecanismo antigo: crons atuais NÃO usam `run_if_master.sh` e a flag `FAILOVER_ARMED` é de 01/07 → mecanismo está **desarmado e desatualizado**. Registrar estado e arquivar (não apagar — §115).
3. Verificar defasagem da réplica do Banco Ouro na NYC.
4. **Disco NYC 78%:** recomendado aplicar a Fase A da Enxutice (~14G, dry-run pronto desde 07/08) ANTES do failover — folga de disco é margem de segurança. Depende do "pode aplicar" do Miguel.

### Fase 2 — sábado 29/08 tarde (~3h): INSTALAR REDUNDÂNCIA MÚTUA
1. **Produção NYC→Tencent:** rsync de `/root/v4_labs` + venv mínimo → Tencent; cron do `v41_ciclo` instalado COMENTADO. Ativação = descomentar (com NYC comprovadamente caído).
2. **Painéis Tencent→NYC:** standby do CCTV V6 na NYC (verificar porta 8084 livre; senão droplet utilitário `142.93.48.252`); FAROL/LUMINA o standby puxa do R2.
3. **Banco Ouro:** runbook de promoção da réplica NYC a master provisório (congelar o robô escritor, inverter sync, reabrir escrita) — 1 script + prova.
4. **Augusto/Mayra:** serviço copiado à Tencent **desligado** (bot Telegram não aceita 2 pollers — só ligar com NYC caída).
5. **Watchdog:** Uptime Kuma (já vive na droplet utilitário) monitorando NYC (porta 22) e Tencent (38422/8084) com **alerta Telegram** — a detecção automática da regra 1.

### Fase 3 — domingo 30/08 06:00–10:00: SIMULADO CONTROLADO
1. **Simulado A (Tencent assume produção):** desliga 1 ciclo do `v41_ciclo` NYC → liga o espelho Tencent por 1 ciclo → prova do rascunho no WP → reverte.
2. **Simulado B (NYC assume painéis):** parar `cctv-v6` Tencent → subir standby → Miguel confere o painel no navegador → reverte.
3. Escrever os **runbooks definitivos** ("NYC caiu" / "Tencent caiu") com a sequência exata de comandos, e gravar no Cérebro.
4. Registro final: adendo neste fórum + memória + `CEREBRO_NODE_ATUALIZACOES.md` + monitoramento.

### Fase 4 — decisão do Miguel: DROPLET VIRGEM (a ideia dele)
- **Recomendação desta sessão:** primeiro o **snapshot da DigitalOcean** (custo baixo, restauração em 1 clique) — já cobre "NYC morreu de vez".
- A **droplet virgem** (mesma região NYC3, provisionada só com python/nginx/rclone/chaves, pronta pra assumir qualquer papel) vale como reserva fria genérica. Custo ~US$6–12/mês. Se aprovada, entra na Fase 2 de sábado.

## 5. Estado da missão
- **O que aconteceu:** inventário ao vivo dos dois servidores (26/08 ~11:40), mecanismo antigo localizado e avaliado, plano completo escrito e registrado no Cérebro.
- **O que falta:** execução das Fases 0–3 no fim de semana (29–30/08).
- **O que preciso do Miguel:** (1) "vai" do plano + horário de sábado; (2) "pode aplicar" da Enxutice Fase A (disco NYC 78%); (3) decisão droplet virgem × só snapshot; (4) disponibilidade domingo de manhã pra conferir o Simulado B (é só abrir um link).
