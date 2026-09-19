# CEREBRO_NODE_OBSERVABILIDADE

> [!CAUTION]
> **OVERRIDE DE TOPOLOGIA 11/08/2026:** tabelas antigas que chamam Alibaba Beijing de ativo são históricas. A lista viva e os papéis atuais estão em `CEREBRO_NODE_ECOSSISTEMA_CANONICO.md`; Uptime Kuma vive no droplet utilitário e os pushers devem ser validados host a host.

**Função:** Registro canônico de observabilidade, métricas e monitoramento da infraestrutura da Trindade. Serve como índice de ferramentas de métricas (Prometheus, Grafana, node_exporter), políticas de cota, credenciais seguras e checklists de rollback.

**Regra de segurança:** Nenhuma credencial real é armazenada neste arquivo. Segredos vão para cofres isolados (ver seção 1). Este node registra apenas paths, finalidades, owners e fingerprints.

---

## 1. Cofre de Credenciais

### 1.1 Alibaba Cloud (Prometheus + Infraestrutura)

**Local do cofre:** `Projeto Cafezinho Agentes/root/agent_data/alibaba_cofre/`
- `cofre_alibaba_ledger_*.jsonl` — histórico de credenciais
- `cofre_alibaba_manifest_*.json` — manifesto de itens do cofre

**Arquivo de chaves de API:** `Projeto Cafezinho Agentes/root/chaves/alibaba_api.env`
- Contém: Access Key ID, Access Key Secret, Region, Instance ID, IP
- Owner: Miguel (CEO) / Codex Maestro
- Última rotação: 2026-05-10

**Política de acesso:**
- Leitura: Codex Maestro, Claude Monitor (para validação)
- Escrita: Miguel (CEO) apenas
- Nunca exponha em fórum/canal/código aberto

### 1.2 Prometheus Alibaba Cloud — Managed Service (CANÔNICO ATUAL 2026-07-08)

**⚠️ Migrado de conta 2026-07-08:** conta antiga (`5799...755-beijing`) tornou-se legado. Cluster produção agora aponta pra conta nova (workspace `Prometheus-Aiatolah`).

**Serviço:** Alibaba Cloud Managed Service for Prometheus V2
**Região:** `ap-southeast-1` (Singapore) — mudou de `cn-beijing`
**Workspace ID:** `default-cms-5083281701361235-ap-southeast-1` (fingerprint: `5083...1235-ap-southeast-1`)
**Instance ID:** `rw-3c86...3258` (fingerprint completo em `alibaba_prometheus.env`)
**Instance Version:** V2 (a antiga era V1)
**Cota:** 50 GB/mês (gratuita, acordo Miguel-Alibaba)

**Bugfix indexação 2026-07-10 (Claude):** Auditor indexação `/root/util_indexing.py` estava submetendo cada post 2× ao Google Indexing API (`www.ocafezinho.com` E `controle.ocafezinho.com`), desperdiçando 50% da quota diária de 200 pings + potencialmente gerando ruído SEO (submeter URL admin). Raiz: `WP_SITE=https://controle.ocafezinho.com` no `.env.unificado` faz WP API responder com `link` do controle. Correção: função `canonicalizar_url()` em `util_indexing.py` reescreve `controle.→www.` como primeira ação de `notificar_e_logar()`. Backlog `posts_nao_indexados.jsonl` também sanitizado (128 controle→www + 4 duplicatas removidas, 155→151). Backups `.bak_pre_canonize_20260710_*` preservados no NYC.

**Método de auth:** HTTP Basic Auth com AK/SK de RAM user (`power-application-user`).
- **Password-free access NÃO funciona em V2** — tentado 2026-07-08 sem sucesso, write sempre retorna 401 mesmo com IP whitelist correta. Read funciona com whitelist. É bug/limitação V2 confirmada.
- Whitelist Read cadastrada mesmo assim como camada defense-in-depth: `43.156.151.165/32`, `39.106.184.215/32`, `159.89.185.209/32`, `186.223.171.9/32` (IP local Miguel).
- AK ID fingerprint: `LTAI...bFJs3` (últimos 5 chars) — **rotacionado 2026-07-10 ~11:20 BRT**, ID antigo `LTAI...dQ3U` a ser Disable+Delete pelo Miguel no console
- Policy anexada: `AliyunPrometheusFullAccess`
- Correção 2026-07-10: RAM user real é `power-application-user`, não `prometheus-agent` (snapshot 09/07 03:56 BRT documentou nome errado).
- **Backup humano do CSV do AK novo:** `Cerebro/alibaba/` (guardado pelo Miguel local após criação no console)

**Cofre Prometheus (migração Claude Code, 2026-07-08 11:05 BRT):**
- Arquivo (em cada servidor): `<home>/prometheus_agent/alibaba_prometheus.env` (`chmod 600`)
- Contém: AK_ID, AK_SECRET, PUSHGATEWAY_URL, READ_URL, Workspace ID, Instance ID
- Owner: Miguel / Claude Code
- **NÃO existe no repo local git-tracked** — só nos 3 servidores
- Backups pré-migração dos scripts: `push_metrics.py.bak_pre_migracao_20260708` (Cingapura + Alibaba Cérebro)

**Formato de push (importante):**
- Usar `prometheus_client.push_to_gateway()` com `handler=basic_auth_handler`
- **NÃO usar curl direto com text/plain** — Alibaba V2 retorna HTTP 200 falso positivo (aceita mas não persiste). Só o formato completo com `# HELP`/`# TYPE` da lib é indexado. Lição §9 reforçada.

**Instância antiga (LEGACY):**
- Workspace: `default-cms-5799673946330755-cn-beijing`
- Instance: `rw-debc...99cd4`
- Status: mantida por 24h como fallback via env var `PROMETHEUS_LEGACY_ENDPOINT` (opcional, não configurado por padrão)
- Após 2026-07-09: pode ser desligada por Miguel

**Política de cota (50 GB/mês):**
- Volume estimado atual: < 5 GB/mês (monitoramento leve)
- Threshold de alerta: 40 GB (80% da cota)
- Ação ao atingir 45 GB: reduzir scrape interval de 15s para 60s
- Ação ao atingir 48 GB: pausar métricas não críticas
- Nunca ultrapassar 50 GB sem autorização de Miguel

---

## 2. Ferramentas de Observabilidade

| Ferramenta | Função | Status | Owner |
|------------|--------|--------|-------|
| Prometheus (Alibaba Managed) | Coleta e armazenamento de métricas | ✅ Ativo, workspace criado | Kimi Code (infra) / **Claude (CCTV)** |
| node_exporter | Métricas de infraestrutura (CPU, memória, disco) | 🟢 **OPERACIONAL** — push a cada 5 min, persistência real | Kimi Code (instalação) |
| prometheus_client (Python) | Métricas de aplicação (agentes Python) | ✅ Ativo em 5 servidores | Kimi Code (deploy) |
| Grafana | Visualização de métricas | ⏳ Não provisionado | Pendente |
| Claude Monitor 30/30 | Monitor textual de logs e saúde | ✅ **ATIVO** — Claude construindo CCTV | **Claude Code** |
| vigia_cafezinho.sh | Vigia remoto Tencent/Cingapura | ✅ Ativo | Codex / Kimi (infra) |

---

## 3. Sprint Observabilidade S1 — Prometheus Alibaba

**Status:** Fase 0 completa — Fase 1 DESBLOQUEADA (credenciais no cofre, 2026-05-21 17:30 BRT)
**Fase 1 início:** após instalação node_exporter no Beijing + validação push
**Fase 1 bloqueada até:** ~~inventário completo, rollback definido, cofre registrado~~ ✅ TODOS CONCLUÍDOS

### Fase 0A — Inventário técnico (DeepSeek)
- Endpoint/workspace Prometheus Alibaba
- Portas, firewall, security group
- Risco de exposição node_exporter
- Entrega: `forum_prometheus_alibaba_20260521.md §3`

### Fase 0B — Cérebro e cofre (Kimi Code)
- Este arquivo (`CEREBRO_NODE_OBSERVABILIDADE.md`)
- Política de cota 50 GB/mês
- Mapeamento de credenciais (sem expor)
- Checklist de rollback (abaixo)
- Entrega: este node + `forum_prometheus_alibaba_20260521.md §3.1`

### Fase 0C — Arquitetura de métricas (Antigravity)
- Vocabulário mínimo: sucesso, falha, duração, provider LLM, custo, posts, descartes
- Separar métricas de infra (node_exporter) de métricas editoriais (prometheus_client)
- 5 métricas iniciais por agente
- Entrega: `forum_prometheus_alibaba_20260521.md §3.2`

### Fase 0D — Monitoramento e não duplicação (Claude Monitor)
- Comparar Prometheus com monitor 30/30 e vigia Cafezinho
- Decidir o que vira métrica vs relatório textual
- Auditar conflitos
- Entrega: `forum_prometheus_alibaba_20260521.md §3.3`

---

## 4. Checklist de Rollback (Prometheus node_exporter)

Antes de qualquer instalação em servidor:

- [ ] Backup do diretório de instalação (se existir node_exporter anterior)
- [ ] Backup do crontab (`crontab -l > crontab_backup_pre_prometheus_YYYYMMDD.txt`)
- [ ] Backup do firewall/security group (screenshot ou export)
- [ ] Teste de conectividade Prometheus → node_exporter (sem firewall)
- [ ] Documentar porta escolhida e método de bind (localhost vs 0.0.0.0)
- [ ] Rollback script: `killall node_exporter && rm -rf /caminho/instalacao`
- [ ] Rollback firewall: comando para remover regra de porta adicionada
- [x] Credenciais Prometheus no cofre (`alibaba_prometheus.env`)
- [ ] Miguel informado e aprovou abertura de porta (se necessário)

---

## 5. Métricas Propostas (Fase 0C — aguardando Antigravity)

**Infraestrutura (node_exporter):**
- CPU, memória, disco, rede, uptime

**Editoriais (prometheus_client):**
- Aguardando vocabulário do Antigravity (§3.2)

---

## 6. Relacionamentos com outros sprints

### Cluster ATIVO (workspace Prometheus-Aiatolah, ap-southeast-1) — 2026-07-08

| Servidor | IP | Instance Label | Status | Auditado |
|----------|-----|---------------|--------|----------|
| Cingapura Tencent | `43.156.151.165` | `cingapura_tencent` | 🟢 Operacional (push migrado) | 2026-07-08 |
| Alibaba Cérebro | `39.106.184.215` | `alibaba_cerebro` | 🟢 Operacional (push migrado) | 2026-07-08 |
| Rio-Carta-Agentes | `159.89.185.209` | `rio_carta_agentes` | 🟢 Operacional (instalação do zero) | 2026-07-08 |

**Cluster ativo:** 3/3 servidores empurrando e persistindo métricas via Basic Auth.

### Servidores fora do cluster (quebrados/desativados 2026-07-08)

| Servidor | IP | Motivo |
|----------|-----|--------|
| Beijing Tencent | `82.156.167.218` | SSH inacessível (timeout todas portas). Papel real: proxy GACC do agente_estatistico, não Prometheus. |
| NYC 02 YouTube | `142.93.48.252` | `node_exporter.service` inexistente + porta 9100 vazia. YouTube GSN pausado desde 05/06. |
| NYC Failover | `198.199.121.136` | Push parou em 2026-05-22 (48 dias offline). Hoje é master primário Cafezinho — vale re-instrumentar em sprint separada. |

**Fora do cluster (legado):** NYC 01 (`159.89.237.100`) — Rio Carta desativado, SSH inacessível.

| Sprint | Relação |
|--------|---------|
| GSN YouTube NYC S1 | Prometheus pode observar infra NYC, mas não resolve acesso YouTube |
| Agente Qualidade | Prometheus pode coletar métricas de qualidade (notas, drift) |
| Eleições | Prometheus pode monitorar fila, descartes, publicações |
| Rio Carta Fase 1A | Prometheus pode monitorar latência LLM, taxa de aprovação shadow |

---

**Node criado por:** Kimi Code CLI, engenheiro executor pleno  
**Data de criação:** 2026-05-21 17:10 BRT  
**Baseado em:** `forum_prometheus_alibaba_20260521.md` §2 (Codex Maestro)  
**Próxima revisão:** após instalação node_exporter (Fase 1) + validação push

---

## 7. Instalação node_exporter — Fase 1 (Concluída)

**Servidor alvo:** Tencent Beijing (`82.156.167.218`)
**Método:** node_exporter em modo push + cron a cada 5 min
**Porta local:** 9100 (localhost apenas, sem bind externo)
**Pushgateway:** URL no cofre `alibaba_prometheus.env`
**Auth:** Whitelist de IP (Miguel configurou no painel Alibaba, 2026-05-21 17:58 BRT) — **zero headers de autenticação**
**Script:** `/home/ubuntu/prometheus_agent/push_metrics.sh`
**Cron:** `*/5 * * * *`
**Volume estimado:** ~86 MB/mês
**Primeiro push:** `2026-05-22T05:04:57+08:00 HTTP 200`
**Rollback:** `killall node_exporter && rm -f /usr/local/bin/node_exporter && crontab -r`
**Status:** 🟢 **OPERACIONAL**

**Servidor alvo 2:** Tencent/Cingapura (`43.156.151.165`)
**Método:** node_exporter em modo push + cron a cada 5 min
**Porta local:** 9100 (localhost apenas, sem bind externo)
**Instance label:** `cingapura_tencent`
**Script:** `/home/ubuntu/prometheus_agent/push_metrics.sh`
**Cron:** `*/5 * * * *`
**Volume estimado:** ~86 MB/mês
**Primeiro push:** `2026-05-21T19:27:11-03:00 HTTP 200`
**Rollback:** `killall node_exporter && rm -f /usr/local/bin/node_exporter && crontab -r`
**Status:** 🟢 **OPERACIONAL** (instalado 19:27 BRT)

**Volume combinado estimado:** ~172 MB/mês (dentro da cota 50 GB)

---

## 8. Prometheus como Sistema Nervoso Central da Infraestrutura

**Função arquitetural:** O Prometheus atua como o **Sistema Nervoso Central / Monitor Cardíaco** da infraestrutura da Trindade. Ele viabiliza a transição de um monitoramento puramente textual de logs (Claude Monitor lendo `overview.txt`, `vigia_cafezinho.sh`) para um **Centro de Comando Data-Driven** baseado em queries matemáticas (PromQL).

### O que o Prometheus mede (em vez de ler)

| Monitoramento Antigo (textual) | Monitoramento Novo (métrico) |
|-------------------------------|------------------------------|
| Claude lendo logs linha a linha | Query PromQL: `rate(http_requests_total[5m])` |
| `vigia_cafezinho.sh` pingando sites | Métrica: `probe_success` com histórico temporal |
| Contagem manual de posts no banco | `agente_posts_publicados_total` com labels por agente |
| Adivinhar se CPU está alta | `node_cpu_seconds_total` com percentual calculado |
| Verificar se API caiu no último tick | `up{job="node_exporter"}` com alerta automático |

### Como a Trindade usa Prometheus

**Claude Monitor:** Em vez de ler arquivos de texto, executa queries PromQL para extrair dados estruturados:
- *"Agente de YouTube usou 100% da CPU nos últimos 15 minutos?"* → `100 - (avg(irate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)`
- *"Robô GSN publicou 20 matérias hoje, mas o tempo médio está 30% mais lento?"* → `histogram_quantile(0.95, rate(agente_publicacao_duracao_seconds_bucket[1h]))`

**Codex Maestro:** Dashboard de saúde de todos os servidores em uma única query.

**Miguel (CEO):** Recebe alertas Telegram avançados baseados em thresholds matemáticos, não em heurísticas textuais.

### Endpoints disponíveis

| Endpoint | URL (fingerprint) | Função |
|----------|-------------------|--------|
| Remote Write | `.../api/v1/write` | Push de métricas (node_exporter) |
| Pushgateway | `.../api/v1/pushgateway` | Recepção de métricas push |
| **Query (PromQL)** | `.../api/v1/query` | **Leitura de métricas — sem auth (whitelist IP)** |

**Query URL completa (path only, não expor em fóruns abertos):**
```
https://workspace-default-cms-5799673946330755-cn-beijing.cn-beijing.log.aliyuncs.com/prometheus/workspace-default-cms-5799673946330755-cn-beijing/aliyun-prom-rw-debc5dfea3a8da56337348d99cd4/api/v1/query
```

**Acesso:** Whitelist de IP (Miguel configurou). Servidores autorizados acessam **sem header de autenticação**. Qualquer IP fora da lista recebe `401 Unauthorized`.

---

## 9. Aiatolah — Prometheus desde a nascença

**Data:** 2026-05-23  
**Status:** base local criada no repositório `aiatolah/`

Miguel determinou que o Aiatolah, novo portal de Inteligência Artificial, deve nascer já instrumentado para Prometheus. O padrão adotado é:

- cada post gera um recibo append-only em `aiatolah/agent_data/publicacoes_metricas.jsonl`;
- cada recibo registra post, título, idioma, agente, etapa, modelos usados, tokens, custo estimado, fonte, status e horário;
- quando `AIATOLAH_PROMETHEUS_PUSHGATEWAY` estiver definido, o publicador empurra métricas para o Prometheus Alibaba via `prometheus_client.push_to_gateway()`;
- falha de Prometheus nunca derruba publicação; o recibo local fica salvo para auditoria e reenvio;
- o painel deve falar em linguagem humana: posts no período, custo por post, tokens por post, modelo que escreveu, modelo que revisou e agente responsável.

Arquivos criados no repositório Aiatolah:

- `aiatolah/PROMETHEUS_DESDE_NASCENCA.md`
- `aiatolah/agentes/aiatolah_metricas_publicacao.py`
- `aiatolah/Modelos para projeto ChatGPT/09_PROMETHEUS_E_CHAVES_DESDE_NASCENCA.md`

Variáveis Prometheus do Aiatolah:

- `AIATOLAH_PUBLICACOES_METRICAS`
- `AIATOLAH_PROMETHEUS_PUSHGATEWAY`
- `AIATOLAH_PROMETHEUS_JOB`
- `AIATOLAH_PROMETHEUS_INSTANCE`

Credencial real: vem do cofre `Projeto Cafezinho Agentes/root/chaves/alibaba_prometheus.env`, nunca de fórum/canal/ChatGPT.

**Status query endpoint:** 🟢 Testado por Antigravity (fora da whitelist → 401) + aguardando smoke read-only do Claude Monitor.

---

## 8.5 Linguagem do Prometheus — Traduzida para o Negócio

**Data:** 2026-05-22 01:50 BRT  
**Responsável:** Kimi Code

O Miguel solicitou que as métricas técnicas sejam traduzidas para linguagem de negócio. Não mais "OK: 495 metricas" — sim "🟢 Todos os servidores saudáveis. Zero risco."

**Preocupações do CEO mapeadas:**

| Pergunta do Miguel | Métrica técnica | Tradução leiga | Status |
|-------------------|-----------------|----------------|--------|
| 💰 "Vou gastar mais?" | Volume de dados/mês | "~430 MB/mês (1% da cota)" | 🟢 Zero risco |
| ⚠️ "O sistema corre risco?" | CPU, RAM, disco | Cores 🟢🟡🟠🔴 com explicação | 🟢 Funcionando |
| 🐌 "O site está lento?" | Latência HTTP | ⏳ Pendente — Claude Fase 3 | — |
| 🤖 "LLMs estão caras?" | Custo por provider | ⏳ Pendente — DeepSeek + Claude Fase 3 | — |

**Artefatos criados:**
- Fórum: `Foruns/forum_prometheus_traduzido_miguel.md`
- Script: `root/prometheus_tradutor.py` (roda de Beijing, whitelist)
- Canal: `canal_20260522_prometheus_traduzido.md`

**Regra de pontuação no canal:**
- Só alertar quando amarelo ou pior
- Nunca mais pontuar números crus sem tradução

---

## 9. Correção do falso positivo HTTP 200 — Pushgateway Alibaba

**Data:** 2026-05-21 23:20 BRT  
**Responsáveis:** DeepSeek (diagnóstico/correção), Codex Maestro (auditoria/cron)

### Incidente

Os scripts `push_metrics.sh` enviavam métricas em formato incompatível com a ingestão real do Prometheus Alibaba. O endpoint retornava HTTP 200, mas as séries não apareciam no banco de métricas.

### Correção

DeepSeek substituiu o envio cru por `push_metrics.py` usando `prometheus_client.push_to_gateway()`. Codex auditou e corrigiu o agendamento cron em Cingapura/Beijing/NYC.

### Servidores validados manualmente

- `cingapura_tencent`: `OK: 503 metricas`
- `beijing_tencent`: `OK: 495 metricas`
- `nyc_failover`: `OK: 523 metricas`
- `gsn_nyc_youtube`: `OK: 523 metricas`
- `alibaba_cerebro`: `OK: 482 metricas`

### Backups de cron

- Cingapura: `/home/ubuntu/prometheus_agent/crontab.bak_20260521_2319_codex`
- Beijing: `/home/ubuntu/prometheus_agent/crontab.bak_20260521_2319_codex`
- NYC Failover: `/root/prometheus_agent/crontab.bak_20260521_2319_codex`
- NYC YouTube 02: `push_metrics.py.bak` implícito via `.sh` preservado
- Alibaba Cérebro: `push_metrics.py.bak` implícito via `.sh` preservado

### Lição operacional

HTTP 200 em endpoint de ingestão não comprova persistência. Todo smoke de observabilidade precisa validar consulta PromQL ou leitura real no painel, não apenas status HTTP.

**Fórum:** `Foruns/forum_prometheus_pushgateway_fix_20260521.md`

---

## 10. Sprint 4 Kimi Code — Consolidação do Cluster 5/5 (2026-05-22 03:09 BRT)

### Diagnóstico

O DeepSeek e Codex corrigiram 3 servidores, mas 2 permaneciam com o script `.sh` legado (curl falso-positivo):
- NYC YouTube 02 (`142.93.48.252`)
- Alibaba Cérebro (`39.106.184.215`)

Além disso, o cron da Cingapura estava sintaticamente quebrado (`PROMETHEUS_INSTANCE=...` como parte do path), e o NYC Failover não tinha redirecionamento de log.

### Ações executadas

1. **Instalação `prometheus_client`** nos 2 servidores pendentes (NYC02, Alibaba) via `pip3 --break-system-packages`.
2. **Deploy `push_metrics.py`** em NYC02 (`/root/prometheus_agent/`) e Alibaba (`/root/prometheus_agent/`), com `INSTANCE` default correto.
3. **Correção de cron** em todos os 5 servidores:
   - Cingapura: corrigido path + variável de ambiente
   - NYC Failover: adicionado `PROMETHEUS_INSTANCE` + redirecionamento de log
   - NYC02: migrado de `.sh` para `.py`
   - Alibaba: migrado de `.sh` para `.py`
   - Beijing: já estava correto
4. **Validação manual:** todos os 5 servidores retornaram `OK: X metricas`.
5. **Verificação de cron:** todos os 5 crons agora padronizados com `PROMETHEUS_INSTANCE=<label> python3 /path/push_metrics.py >> /path/push.log 2>&1`.

### Status

| Servidor | IP | Script | Cron | Validação |
|----------|-----|--------|------|-----------|
| Beijing | `82.156.167.218` | `push_metrics.py` | ✅ | `OK: 495` |
| Cingapura | `43.156.151.165` | `push_metrics.py` | ✅ | `OK: 503` |
| NYC YouTube 02 | `142.93.48.252` | `push_metrics.py` | ✅ | `OK: 523` |
| NYC Failover | `198.199.121.136` | `push_metrics.py` | ✅ | `OK: 523` |
| Alibaba Cérebro | `39.106.184.215` | `push_metrics.py` | ✅ | `OK: 482` |

**Cluster Prometheus: 5/5 operacional com persistência real verificada.**

— **Kimi Code, 2026-05-22 03:09 BRT**

---

## 10.1 CCTV V6 — Home única, página Loops e relatório Telegram 30/30min (15/08/2026)
> **Adendo 10/09 ~22h (ZM-20260910-024):** /v6/tendencias Top10 — título da REST WP precisa `html.unescape` antes do escape do card (entidade &#8220; virava texto visível); rótulos do score agora honestos (fórmula real: views/h 6h + 0,15×gravidade). Fórum: `Foruns/forum_tendencias_entidade_titulo_score_rotulo_20260910.md`.

> **Adendo 10/09/2026 (ZM-20260910-020):** página /v6/loops v2 humanizada (`loops_v2_humano_20260910`) — faixa de status no topo que avisa PARADO em vermelho (Laura parada desde 09/09 17:12 na estreia da v2), consolidados antigos (até 19/08) colapsados, legendas "como ler", rodapé sem caminhos, auto-refresh 5 min. Fórum: `Foruns/forum_painel_v6_loops_humanizado_20260910.md` · Memória: `Foruns/memoria_painel_v6_loops_humanizado_20260910.md` · rollback: `.bak_pre_loops_humano_20260910`.

- **Página `/v6/loops`**: relatórios resumidos do **Loop Laura** (consolidados do chefe em `v6_data/foruns/loop_trindade_laura/controle/relatorios_chefe/`, seleção `?rel=NNN`) e do **Loop Miguel** (INDEX_ATIVO + ALERTAS_SLA + ESTADO_ATUAL de `v6_data/foruns/ponte_trindade_daemon/`). Fonte alimentada pelo rsync local `7,37` — nenhum sync novo.
- **APIs JSON**: `/v6/api/loops` + `/v6/api/resumo` (audiência GA4 + publicações WP).
- **Home única**: NAV não aponta mais para `/painel/` (estática legada); home = índice das 13 páginas; Nginx `/` → 301 `/v6/`.
- **Relatório Telegram 30/30min** (Ponte Cafezinho): `~/bin/cctv_relatorio_30min.py` — health-check + auto-restart `cctv-v6` + loops/publicações/erros/audiência/online/crédito Kimi-Qwen-GLM. Automação ZCode `automation-e3465bb3-312f-4583-9a72-7f69711fc147`. 1º envio real 15/08 12:36 BRT.
- **Responsável permanente pelo painel: ZCode** (ordem do Miguel).
- Tema Duplo: `Foruns/forum_painel_cctv_v6_home_unica_pagina_loops_20260815.md` + `Memorias/memoria_painel_cctv_v6_home_unica_pagina_loops_20260815.md`.
- **18/08/2026:** separação YouTube × Temáticos (ordem Miguel): publicações dos temáticos saíram da `/v6/youtube` → card "📰 Publicações nas últimas 24h" na Central dos Temáticos; a página YouTube agora mostra "🎬 Últimos posts dos agentes YouTube" (Cafezinho cat 28 via REST + vídeos `youtube-*` dos temáticos via sitemap, função `_posts_video_yt_tematico`). Tema Duplo: `Foruns/forum_painel_v6_youtube_x_tematicos_pub_20260818.md` + `Memorias/memoria_painel_v6_youtube_x_tematicos_pub_20260818.md`. Backup `.bak_pre_yt_tematicos_20260818`.

## 11. CCTV v5 — Painel Multi-Página (DEPLOYADO 2026-05-24)

**Construído por:** Kimi Code CLI  
**Servidor:** localhost:8082 (túnel SSH → nginx Cingapura :8080/v5/)  
**Stack:** Python 3 stdlib, template HTML externo, zero dependências  
**Status:** ✅ Ativo e público

### Rotas operacionais

| Rota | Função | Status |
|------|--------|--------|
| `/v5/` | Visão Executiva (cards, servidores, fóruns) | ✅ 200 |
| `/v5/servidores` | Lista de servidores + status | ✅ 200 |
| `/v5/sprints/live` | Sprints em andamento | ✅ 200 |
| `/v5/agentes` | Ranking de agentes por custo | ✅ 200 |
| `/v5/llms` | Modelos usados (últimos 7 dias) | ✅ 200 |
| `/v5/forum-trindade` | 16 últimos fóruns em cards | ✅ 200 |
| `/v5/forum/<nome>` | Leitura completa de fórum no navegador | ✅ 200 |
| `/v5/forum-search` | Busca por palavra-chave nos 344 fóruns | ✅ 200 |
| `/v5/mural-trindade` | Mural Trindade (mensagens + formulário) | ✅ 200 |
| `/v5/mural-aiatolah` | Mural Aiatolah (GitHub API, cache 5min) | ✅ 200 |
| `/v5/canal-trindade` | Canal Trindade legível no navegador | ✅ 200 |
| `/v5/diretrizes` | Diretrizes Editoriais — revisão de propostas | ✅ 200 |
| `/v5/posts` | Posts recentes do Cafezinho (título, foto, 1º parágrafo) | ✅ 200 |
| `/v5/comentarios` | Comentários recentes do Cafezinho | ✅ 200 |
| `/v5/performance` | Performance GA4 — métricas, top posts, temas | ✅ 200 |
| `/v5/api/health` | Health check JSON (painel, túnel, nginx) | ✅ 200 |
| `/v5/api/launch/recorder` | Abre gravador de áudio local | ✅ 200 |
| `/v5/api/diretrizes/vote` | POST: voto em proposta de diretriz | ✅ 200 |

### Características
- **Links com prefixo automático:** detecta `X-Forwarded-Prefix` do nginx (ex: `/v5`)
- **Cache-busting:** headers `no-cache, no-store, must-revalidate`
- **Leitura de fóruns:** markdown renderizado em HTML (headers, bold, itálico, links, listas)
- **Busca:** JavaScript + API `/api/forum/search?q=...` retorna até 20 resultados
- **Nav bar:** link "📡 Canal" adicionado em todas as páginas
- **Diretrizes Editoriais:** página `/v5/diretrizes` mostra propostas do `agente_diretrizes_editoriais` (dry-run) com cards interativos. Botões: ✅ Aprovar, 👁️ Mais Contexto, ❌ Não. Votos persistem em `regras_candidatas.json` e `decisoes_diretrizes.json`. Aprovação ≥2 votos → status "aprovada" (aguarda Codex incorporar em `diretrizes_editoriais.py`).
- **Posts Recentes:** página `/v5/posts` busca da API pública do WordPress (`controle.ocafezinho.com/wp-json/wp/v2/posts`) os últimos 15 posts. Mostra miniatura da imagem destacada, título, data e primeiro parágrafo real (a legenda da foto em `<figure>` é removida). Cache de 5 minutos.
- **Comentários Recentes:** página `/v5/comentarios` busca da API pública do WordPress os últimos 25 comentários. Mostra autor, status (aprovado/moderação/spam), data, conteúdo e link para o post. Cache de 5 minutos.
- **Performance:** página `/v5/performance` consome dados já produzidos pelos agentes documentados em `CEREBRO_NODE_AGENTES.md` §8. Lê `analytics_snapshot.json` (métricas agregadas GA4: usuários, visualizações, sessões, comparação 7d/30d vs período anterior) e `performance_weights.json` (top posts + pesos de temas/macrotemas gerados por `agente_performance.py`). Não executa API GA4 diretamente — é painel visual read-only.
  - **Importante:** O snapshot deve ser gerado com filtro `platform=web` para bater com o GA4 UI (a UI mostra web por padrão). Sem filtro, a API retorna a soma de todas as plataformas (~60% a mais). Ver auditoria 2026-05-25.

### Transição de Guarda — CCTV e Monitoramento (ATUALIZADO)

| Função | Atual | Status |
|--------|-------|--------|
| CCTV v5 (painel web) | **Kimi Code** | ✅ Deployado 24/05 |
| Prometheus / Métricas | **Claude Code** | ⏸️ Em construção |
| Infra / node_exporter 5/5 | Kimi Code | ✅ Ativo |
| vigia_cafezinho.sh | Codex / Kimi | ✅ Ativo |

### O que Kimi/DeepSeek devem fazer agora
1. **Não interferir** no trabalho do Claude
2. **Manter** o cluster 5/5 operacional (infra apenas)
3. **Estar pronto** para receber quando Claude concluir

### Plano de Construção Claude (registrado no fórum)
Claude respondeu com plano de **4 fases / ~46h**:
1. **PromQL no tick** (6h) — queries no header de cada tick
2. **CCTV v3 HTTP server** (12h) — 4 telas (Prometheus, narrativa Trindade, pulse WP, sprints)
3. **Exporters Cafezinho** (24h) — métricas custom (posts, pautas, custo LLM)
4. **Documentação handover** (4h) — queries, thresholds, paths, plano de sobreposição

### Fórum da transição
`Foruns/forum_cctv_transicao_futura_20260522.md`

## 12. CCTV v3 Premium — Auditoria de Segurança

**Fórum:** [forum_cctv_v3_premium_audit_seguranca_20260522.md](./Foruns/forum_cctv_v3_premium_audit_seguranca_20260522.md)

**Status 2026-05-22 16:58 BRT:** auditoria local inicial feita por Codex no `root/painel_cctv_v3.py`. O painel está validado como ferramenta local/protótipo: endpoints GET-only, `parse_inline()` com `html.escape`, sem chamadas LLM/API paga e smoke local `200`. Risco pendente: `BIND_ADDR="0.0.0.0"` sem auth/ACL expõe a porta `8081` na LAN. Antes de anunciar uso em iPad/LAN, aplicar bind restrito, firewall/allowlist ou autenticação.

— **Kimi Code, 2026-05-22 03:25 BRT**

---

## 13. Resolução da Cegueira do Prometheus & Diagnóstico Alerta NYC

**Data:** 2026-05-22 22:30 BRT  
**Responsável:** Antigravity (Assistente de Arquitetura)  
**Laudo Detalhado:** `~/.gemini/antigravity/brain/28850342-192e-4395-997c-011740e5fb38/diagnostico_prometheus_nyc.md`

### 13.1 O "Apagão de Métricas" (Cegueira Intermitente)
* **Sintoma:** Queries instantâneas no Prometheus Managed da Alibaba retornavam `result: []` frequentemente, simulando "cegueira do banco".
* **Causa Raiz:** O cron envia métricas a cada 5 minutos, mas o *Lookback Delta* (tempo de expiração de cache instantâneo) do Prometheus Alibaba está configurado para ~2 minutos. Qualquer query feita 2 minutos ou mais após o último push era interpretada como série inativa/expirada.
* **Solução:** Substituir queries instantâneas cruas por `last_over_time(<metrica>[10m])` no CCTV e consultas de monitoramento. Isso instrui o Prometheus a buscar o último valor registrado nos últimos 10 minutos, sanando 100% o apagão sem alterar códigos `.py`.

### 13.2 O Falso Positivo "NYC YouTube" (Alerta Laranja)
* **Status Real da Máquina (`142.93.48.252`):** Totalmente saudável. CPU em 0.00, disco em 21% e RAM com 584 MiB disponíveis (60.7% livres de processos de usuário).
* **Causa do Alerta:** O script `prometheus_tradutor.py` usa thresholds absolutos estáticos em GB de RAM livre (`< 1 GB` livre = Laranja, `< 0.5 GB` = Vermelho).
* **Falha de Design:** Em servidores de 1 GB total (como o nó NYC YouTube), o threshold estático de `< 1 GB` livre é impossível de não atingir. A máquina operando vazia já fica em Laranja, e qualquer processamento leve a joga para Vermelho.
* **Recomendação Futura:** Modificar a lógica de tradução para thresholds percentuais em relação à capacidade total (`(MemAvailable / MemTotal) * 100`) para classificar a saúde relativa à máquina física de forma justa.

---

## 14. Implementação e Auditoria — Kimi + DeepSeek (2026-05-23)

**Status:** ✅ APROVADO

### 14.1 O que foi implementado (Kimi Code CLI)

**`prometheus_tradutor.py` (Beijing):**
- Consultas PromQL migradas para `last_over_time(metrica[10m])` — resolve cegueira intermitente
- Thresholds de RAM convertidos para percentuais: <10% 🔴, <20% 🟠, <30% 🟡, >=30% 🟢
- Label `nyc_failover` corrigido (era `cafezinho_failover_nyc`)
- Schema JSON cache alinhado com CCTV v3: chaves `ram_gb`, `disco_pct`, `load1` (strings)
- Cron Beijing: `3-59/5 * * * *`
- NYC YouTube: de 🟠 eterno para 🟢 (63.4% livre)

**`gerar_pulse_cafezinho.py` (Cingapura):**
- Lê WP REST (últimos 15 posts) + `banco_custos_2026-05.jsonl` (133k registros)
- Cruza posts com chamadas LLM em janela de 120min antes da publicação
- Gera `pulse_cafezinho_traces.json` com schema do CCTV v3
- Custo total mapeado: 15 posts = US$ 53.62
- Performance: 5.8s por execução

### 14.2 Resultado da auditoria (DeepSeek Code)

| Ponto | Status | Observação |
|---|---|---|
| Schema Prometheus | ✅ | `ram_gb`/`disco_pct`/`load1` strings, 5 servidores |
| Schema Pulse | ✅ | Estrutura `posts→{llms[]}` correta |
| Timezone WP | ⚠️ | WP `date`=BRT, `date_gmt`=UTC. Logs de custo precisam ser confirmados BRT |
| Performance | ✅ | 5.8s para 133k registros |
| Thresholds RAM | ✅ | 10/20/30% bem calibrados |

### 14.3 Lições registradas no Cérebro

1. **Lookback Delta do Prometheus Alibaba:** ~2min. Sempre usar `last_over_time(...[10m])` em queries programáticas
2. **Thresholds de RAM:** usar percentuais, nunca absolutos em GB (máquinas de 1GB total sempre disparam falso positivo)
3. **Schema JSON:** validar com `json.tool` e comparar com o consumidor (CCTV v3 linhas 824-828)
4. **Timezone:** WP REST campos `date` (BRT) e `date_gmt` (UTC) são diferentes. Confirmar timezone dos logs de custo antes de cruzar
5. **Pipeline de auditoria:** AG desenha → Kimi coda → DeepSeek audita → Codex sincroniza

### 14.4 Fóruns de referência

- `Foruns/forum_painel_cctv_prometheus_resolucao_kimi_20260522.md` — blueprint completo
- `Foruns/forum_carta_deepseek_auditoria_fase3_20260523.md` — carta do Kimi + parecer DeepSeek
- `MEMORIA_DEEPSEEK.md` §7 — memória pessoal do DeepSeek sobre o painel em relação à capacidade total (`(MemAvailable / MemTotal) * 100`) para classificar a saúde relativa à máquina física de forma justa.

---

## 15. Regra de Ouro do Monitoramento — Log sem data é hipótese, não prova (2026-05-31)

**Origem:** PITFALL-20260531-1245-GREP-HISTORICO-LOG-SEM-DATA. Fórum `Foruns/forum_grep_historico_falso_positivo_maestro_20260531.md` + carta à Trindade. Consenso técnico: Claude (proponente) + Codex (12:57) + DeepSeek (12:58).

### 15.1 A regra (vinculante para todo agente no loop §90)

> **"Nenhuma análise de janela de log é confiável até ser cruzada com uma fonte datada. `grep ^\[HH:` é hipótese, não prova."**

Antes de declarar "últimos N minutos", "erro hoje", "pico agora", "surto recente" ou qualquer recorte temporal sobre logs, é OBRIGATÓRIO cruzar com pelo menos uma fonte datada:
- Timestamp **completo** com data (`AAAA-MM-DD`);
- URL publicada com `/AAAA/MM/DD/`;
- WP REST API (campo `date`);
- JSONL de custos/eventos com data absoluta;
- `tail` real do processo (fim do arquivo = appends mais recentes = hoje);
- offset/posição no arquivo cruzado com `mtime`.

### 15.2 Por que `grep ^\[HH:` engana

Logs dos masters usam `[HH:MM:SS]` **sem data**. Filtrar por hora-do-relógio captura a mesma hora em **todos os dias** acumulados no arquivo. `mtime` só prova que o arquivo foi escrito hoje — não que uma linha `[12:xx]` específica seja de hoje. Ancorar `^\[12:` NÃO resolve: continua misturando dias.

### 15.3 Ferramentas de apoio

- **P1:** `root/util_log_window.py` — helper read-only que isola janela REAL via tail/mtime/offset + fonte datada. Zero-write, fora do motor.
- **P2 (gate §92, pendente aval Miguel):** padronizar logs para `[AAAA-MM-DD HH:MM:SS BRT]` nos masters + motor. Elimina a classe inteira de falso positivo na origem.

### 15.4 Pedido de co-vigilância (registrado pela Trindade)

Se qualquer agente reportar "pico de erros hoje" sem mostrar a fonte datada, os demais devem **cobrar o link/fonte** antes de aceitar o diagnóstico no Cérebro. Vale para o Maestro e para quem assumir o loop §90.

---

## 16. CHECKUP-001 — Pausa total Tencent para investigação (2026-06-01)

**Status:** 🔴 Pausa total deliberada do ecossistema Cafezinho/Trindade no Tencent.  
**Executor:** Codex.  
**Motivo:** noite de check-up; investigar deterioração editorial/operacional antes de religar.

### 16.1 O que foi pausado

- Crontabs `root` e `ubuntu`: sem linhas ativas.
- Serviços do projeto: `augusto.service`, `cctv-v5.service`, `cctv-editorial.service`, `zizi.service`, `websearch_proxy.service` inativos.
- Bots/robôs/processos do projeto encerrados: Augusto, Zizi, áudio, agente de correção, websearch, painéis CCTV/editorial, PM2 e rotas de publicação/coleta.
- Infraestrutura preservada: `sshd`, `nginx`, `fail2ban`, `cron` daemon, Tencent/YunJing/TAT, `node_exporter` e serviços do sistema.

### 16.2 Backups para rollback

- `/root/crontab_backup_pre_pausa_emergencial_20260601_211249_codex.txt`
- `/root/crontab_backup_pre_pausa_publicadores_paralelos_20260601_213020_codex.txt`
- `/root/crontab_backups_pause_all_20260601_213647/root.crontab.bak`
- `/root/crontab_backups_pause_all_20260601_213647/ubuntu.crontab.bak`

### 16.3 Validação final

- `sudo crontab -l -u root | grep -n -E '^[[:space:]]*[^#[:space:]]' || true` → vazio.
- `sudo crontab -l -u ubuntu | grep -n -E '^[[:space:]]*[^#[:space:]]' || true` → vazio.
- `systemctl is-active augusto.service cctv-v5.service cctv-editorial.service zizi.service websearch_proxy.service` → todos `inactive`.
- Busca ampla por processos do projeto não retornou processos vivos.

### 16.4 Ponteiros

- Registro canônico: `CEREBRO_NODE_CHECKUPS.md` → `CHECKUP-001`.
- Fórum: `Foruns/forum_investigacao_deterioracao_publicacao_20260601.md`.
- Canal: `Foruns/canal_trindade.md`, entradas Codex 2026-06-01 21:15, 21:28, 21:35, 21:48 BRT.

### 16.5 Regra de religamento

Não religar nada sem ordem explícita de Miguel. Religamento deve ser gradual, com fórum/canal, rollback por serviço/cron, smoke real e uma janela mínima de observação por etapa.

---

## 17. SSH Cliente — Diagnóstico KEX [preauth] · Solução IdentityAgent none + MTU (2026-06-19 03:30 BRT)

### 17.1 Caso fundador

Em **2026-06-19 00:17 BRT**, Daemon e Kimi perderam SSH simultaneamente para os 3 servidores principais (Tencent Singapura `43.156.151.165:38422`, NYC Failover `198.199.121.136:22`, GSN `159.89.237.100:22`). Sintoma:

```
✅ TCP connection established
✅ Banner/version exchange OK
❌ KEX (key exchange) trava — nem em 60s
❌ Log servidor: "Connection closed by 186.223.169.15 [preauth]"
```

Daemon, Kimi e AGY-CLI investigaram 4h durante a madrugada. AGY-CLI decifrou às **03:30 BRT** a causa raiz **DUPLA**.

### 17.2 Causa raiz dupla

**Causa 1 — Path MTU Black Hole na rota internacional Brasil→Singapura/EUA:**
- Algum hop intermediário descarta pacotes >1464 bytes silenciosamente
- ICMP ping com `-M do -s 1400` passa (pequeno) · KEX falha (chave pública ~2KB)
- mtr Tencent mostrou 80% loss em hops da Tata Communications (`64.86.113.x`)

**Causa 2 — ssh-agent / Gnome Keyring travado pós-rekey:**
- Após `SSH2_MSG_KEXINIT received` + `rekey in`, cliente precisa assinar com chave privada
- O Gnome Keyring agent fica esperando requisição gráfica em background que não volta
- Sintoma: `Authenticating to <host>:22 as 'root'` aparece e trava ali

### 17.3 Histórico anterior — bug latente desde semanas atrás

Auth.log Tencent mostra que o sintoma `Connection closed by 186.223.169.15 [preauth]` já ocorria **esporadicamente** antes do incidente principal:
- 14/06 21:36 BRT — 1 entrada isolada
- 16/06 14:26 BRT — 1 entrada isolada
- 19/06 00:17 → 01:10 BRT — 29 entradas contínuas (apagão)

**Interpretação:** combinação MTU+ssh-agent já existia, mas era esporádica e compensada por retransmissão TCP. Em 19/06 a rede internacional degradou e a combinação virou impeditiva.

### 17.4 Solução aplicada

**A. SSH config (`~/.ssh/config`) — `IdentityAgent none` em todos os 8 hosts:**

```
Host tencent
    HostName 43.156.151.165
    Port 38422
    User ubuntu
    IdentityFile ~/.ssh/id_rsa
    IdentitiesOnly yes
    IdentityAgent none          # ← solução AGY-CLI
    ServerAliveInterval 60
    StrictHostKeyChecking no
```

Aplicado em 2026-06-19 03:37 BRT pelo Daemon via Python script. Backup: `~/.ssh/config.bak_pre_identity_agent_none_20260619_0336`. Hosts afetados: `nyc`, `china-install`, `china-proxy`, `china`, `cingapura`, `beijing`, `tencent`, `alibaba`.

**B. MTU local — opções:**
- **B1 (atual, conservadora):** MTU 1360 fixo na interface `enx00e04c680e41`. Reduz eficiência ~10% em tráfego grande, mas zero risco.
- **B2 (recomendação futura):** MTU 1500 + `net.ipv4.tcp_mtu_probing=1` (kernel auto-descobre PMTU por destino). Comando: `echo 'net.ipv4.tcp_mtu_probing=1' | sudo tee /etc/sysctl.d/99-tcp-mtu-probing.conf && sudo sysctl --system`.

### 17.5 Validação

Após aplicação:
- `ssh tencent` → OK · uptime 69d · instantâneo ✅
- `ssh nyc` → OK · ubuntu-s-1vcpu-2gb-nyc1 ✅
- `ssh alibaba` → OK · iZ2ze82jxyxjztl5fpi651Z ✅

### 17.6 Crédito

- **AGY-CLI** (Antigravity CLI · Sprint 5 Auditoria Técnica) diagnosticou a causa raiz dupla
- **Kimi** abriu o caso 01:30 BRT em `forum_diagnostico_ssh_trindade_20260619.md`
- **Daemon** investigou 7 hipóteses (firewall · fail2ban · KEX · MTU básico · cipher · ISP · Tata) · descartou todas · escalou ao AGY-CLI 03:05 BRT
- **Miguel** aplicou MTU 1360 + autorizou Daemon aplicar IdentityAgent none na config

### 17.7 Documentos canônicos

- 📄 `Projeto Cafezinho Agentes/Foruns/carta_agy_cli_misterio_ssh_bloqueado_20260619.md` (cartinha + resposta AGY §11 + solução)
- 📄 `Projeto Cafezinho Agentes/Foruns/forum_diagnostico_ssh_trindade_20260619.md` (caso aberto Kimi)
- 🧠 Memória [[reference-ssh-identity-agent-none-mtu-1360]] (referência permanente Daemon)
- 📋 Backup config: `~/.ssh/config.bak_pre_identity_agent_none_20260619_0336`

### 17.8 Regra operacional

**Se SSH voltar a travar no KEX/preauth no futuro:**
1. Verificar primeiro que `~/.ssh/config` ainda tem `IdentityAgent none` em todos hosts
2. Se sim, suspeitar MTU degradado novamente → aplicar `sudo ip link set dev <interface> mtu 1360`
3. Se persistir, ativar `tcp_mtu_probing=1` (B2 acima)
4. Se ainda persistir, escalar AGY-CLI ou abrir ticket Tencent
5. Operação degradada via WP API + DNS direto `8.8.8.8` permanece viável durante incidente

## 18. Falso positivo Ceará Digital — domínio errado no painel V6 (2026-08-15 ~13:00 BRT)

**Caso:** alerta Telegram "problemas em alguns sites temáticos" (relatório 30min) — painel marcava 🌵 Ceará Digital "● falha".
**Causa raiz:** dict `TEMATICOS` do `painel_cctv_v6.py` (linha ~1269) usava o domínio previsto `www.cearadigital.news` (nunca foi o real — HTTP 000) em vez do canônico `ceara.digital` (200 OK), já registrado no INDEX_SATELITES desde 05/08. Config desencontrada → falso positivo permanente.
**Fix (ZCode/Kimi K3):** URL trocada no painel (backup `.bak_pre_ceara_dominio_20260815`), restart `cctv-v6.service`, cache `tem_saude.json` limpo → validado **7/7 online**. Verificação independente: 8/8 temáticos do registry HTTP 200 com conteúdo 15/08.
**Lições:** (1) mudança de domínio canônico exige checklist de propagação (painel, sentinela, registry, relatórios); (2) DNS local soluçando (11:35–12:29) gera falhas transitórias que viram alerta em plural; (3) `ponte_cafezinho.py --send` falha SILENCIOSA (exit 0) sem DNS — envio Telegram garantido via fallback IP 149.154.166.110 + SNI.
**Tema Duplo:** `Foruns/forum_fix_alerta_tematicos_ceara_dominio_cctv_v6_20260815.md` + `Memorias/memoria_fix_alerta_tematicos_ceara_dominio_cctv_v6_20260815.md`. Relacionado: `memoria_vigilia_tematicos_3_sinais_falso_alarme_20260807.md`.

## 19. Painel CCTV V6 — custos em reais + ranking dinâmico de LLMs + MM7 vs semana anterior (17/08/2026)

**Ordem do Miguel:** página `/v6/custos` 100% em reais (cotação do dólar em destaque NO
ALTO, nada em dólar, gráfico de custo diário escrito "em reais") + ranking dinâmico de
preços+qualidade das LLMs (o do Moka Reader, que também existe no Aiatolah News) +
`/v6/audiencia` com MM7 vs MM7 da semana anterior.

**Feito (ZCode/Qwen 3.8, no ar ~01:15):** custos só em R$ (colunas US$ removidas em por
modelo/agente/provedor e nas stats hoje/7d/30d); banner dourado de cotação no topo
(open.er-api.com, cache 24h); gráfico com eixo/tooltips/legenda em R$ e título "(em
reais)"; seção nova do ranking (medalhas, qualidade 🏆S/A/B, velocidade, R$/1M entrada/
saída, "resumir 1 livro" em R$) alimentada pelo agente `atualizador_precos_llm.py`
(cron Tencent 09:00 UTC) via jsDelivr com cache 6h + fallback embutido de 16 modelos;
audiência ganhou card "MM7 vs semana anterior" (delta %) e linha tracejada defasada 7d
no gráfico da MM7. Verificação pedida: **o ranking existe e está no ar no Moka
(mokareader.com/ajuda) e no Aiatolah (aiatolah.com/rankings)** — fonte dinâmica
atualizada 16/08.

**Backup:** `painel_cctv_v6.py.bak_pre_custos_brl_ranking_20260817` (Tencent).
**Tema Duplo:** `Foruns/forum_painel_cctv_v6_custos_reais_ranking_mm7_20260817.md` +
`Memorias/memoria_painel_cctv_v6_custos_reais_ranking_mm7_20260817.md`.

## §21 — Painel CCTV V6: audiência dos temáticos + página Moka (18/08/2026, ordem Miguel)

- **/v6/tematicos:** linha 📈 30d (usuários/páginas/sessões, GA4 fechado) em cada card + tabela-resumo com TOTAL (1ª leitura: 604 usuários nos 7 sites com GA4; Mapa Rio sem medição).
- **/v6/moka (nova):** e-mails do info@mokareader.com via IMAP (últimos 30 + contadores), audiência GA4 do site (totais 30d, tempo médio por sessão, tempo engajado, **por país top 12**, por dispositivo) e uso do pontos_api (usuários, logins 7d, transcrições, consumo). GA4 do Moka **aguarda ID numérico da propriedade** (env GA4_PROPERTY_MOKA) — pendência do Miguel.
- Tema Duplo: `Foruns/forum_painel_v6_tematicos_audiencia_moka_20260818.md` + `Memorias/memoria_painel_v6_tematicos_audiencia_moka_20260818.md`.
- Backup: `painel_cctv_v6.py.bak_pre_tematicos_audiencia_moka_20260818` (Tencent).


- **§22 (22/08/2026) — 🧭 Autoria × audiência no CCTV V6:** página `/v6/autoria` (card "🧭 Autoria" no menu) — cards por fluxo com views GA4 totais+média+melhor post, ranking "quem PUBLICA mais" × "quem PERFORMA melhor", coluna Views por post (GA4 fechado até ontem; matching por slug; `ga4_posts_datados`). Fonte: API de autoria do canônico (`/wp-json/cafezinho/v1/autoria`, mu-plugin `cafezinho-origem-post.php`, meta `_cafezinho_origem`). Fórum: `Foruns/forum_mapa_sinais_integracoes_baleia_cctv_20260822.md` Adendo 1.

## 24/08/2026 13:40 — Checagem GA4 tempo real canônico (ZCode/GLM-5.3)

- `Foruns/forum_analytics_queda_visitas_online_cafezinho_20260824.md` (+ `Memorias/memoria_analytics_queda_visitas_online_cafezinho_20260824.md`) — pedido Miguel "analytics caindo forte": **sem incidente** (realtime 55 ativos 13:36; site 200 c/ tag; dia corrente no GA4 vem incompleto 07h=93/08h=1; domingo 23/08 foi recorde 7.858). Como consultar realtime via API (SA ga4.json Tencent, prop 374552425, schema reduzido) documentado na memória.

- (24/08 14:05, ADENDO 1 do fórum) Contador redundante próprio no cafezinho-wp: `/root/cafezinho_contador/` (contador.sh + resumo.json/txt, cron */5) + log nginx `access.ocafezinho.contador.log` com IP real. GA4 realtime subnotificando (24/08) — cruzar SEMPRE contador×GA antes de declarar queda de audiência.

- (24/08 14:35) Página 🛡️ Audiência Redundante no CCTV (`/v6/audiencia-redundante`): fonte da verdade de audiência online do canônico = contador do servidor (jsonl perpétuo em agent_data/cctv/v6/). Quando divergir do GA4, acreditar no contador.

## 03/09/2026 09:51 — FAROL: gráfico de 40 horas no topo (ZCode/GLM-5.3)

- Pedido Miguel 03/09 ~09:4x: na página 🛡️ FAROL (`/v6/audiencia-redundante`, Tencent), gráfico das últimas 40h (era 3h) subindo para logo após o card "ONLINE AGORA", espelhando o layout da página GA4.
- Feito no `painel_cctv_v6.py`: `_farol_svg_3h` → `_farol_svg_ultimas(amostras, janela_h)` (eixo X adaptativo: >3h = hora cheia múltiplo de 4 `dd/mm Hh`); série dedicada de 481 amostras (40h × 12/h + 1); título "⏱️ Últimas 40 horas — leituras de 5 em 5 min". Backup `painel_cctv_v6.py.bak_pre_40h_topo_20260903`.
- Provas: ordem HTML servida correta; rótulos 01/09 20h→03/09 08h legíveis; screenshot auditado sem sobreposição; Máx 40h = 1.146 visitantes. Fórum: `Foruns/forum_farol_grafico_40h_topo_20260903.md` + memória `memorias_provisorias/memoria_farol_grafico_40h_topo_20260903.md`.
- (08/09 23:54) Página 🔁 Loops (/v6/loops, Tencent): card «ciclos ao vivo (30/30min)» da Laura no topo — lê memoria_loop_laura/AAAA-MM-DD.md (formato diário pós-29/08); consolidados relatorio_chefe (até 19/08) viraram histórico. Marca loops_ciclos_ao_vivo_20260908; memória provisória memoria_loops_ciclos_ao_vivo_20260908.md; adendo no forum_ds_nuvem_chefe_dois_loops_20260830.md.

## 13/09/2026 15:3x — GA4 /v6/audiencia: correlação posts×audiência no gráfico 40 dias (ZCode/GLM-5.3)

- Pedido Miguel 13/09 ~15:1x: no gráfico "Últimos 40 dias (fechados)", views+MM7 no MESMO eixo esquerdo; posts publicados/dia em colunas transparentes no eixo direito c/ nº rotulado em cima de cada coluna.
- Feito: `svg_linha_dupla` reformulada (escala única esquerda; colunas `#39d98a` fill-opacity 0,16 máx 50% da área, por baixo das linhas; rótulo 10,5pt por coluna; eixo direito alinhado às colunas) + `pub_contagem_diaria()` nova (REST WP paginada até 30×100, dia BRT, só dias fechados, cache 1h). Backup `.bak_pre_correlacao_posts_20260913`.
- Bug pego: paginação 8×100 cortava agosto (~50 posts/dia) — corrigida p/ 30 páginas, cache regerado (47d, 2.205 posts; varredura 22s).
- Provas: interno+público 200, 40 colunas, rótulos 15→70 posts/dia; screenshot auditado 5/5; página quente 0-3s.
- Fórum: `Foruns/forum_audiencia_correlacao_posts_20260913.md` + memória `memorias_provisorias/memoria_audiencia_correlacao_posts_20260913.md`.

## 13/09/2026 ~17:5x — Painel CCTV V6 com LOGIN Basic Auth (ZCode/GLM-5.3)

- Ordem Miguel 13/09 ~17:1x: painel v6 deixa de ser público. Basic Auth no próprio serviço (8084), cobrindo via-nginx e direto; creds em `/home/ubuntu/cafezinho/v6/.painel_auth` (600) + cofre unificado (`PAINEL_V6_USER/PASS`).
- Isenções: POST `/api/audiencia-receber` (token próprio, pusher NYC) e local direto (localhost SEM X-Real-IP — crons WARM_CACHE/FAROL provados 200). Falha → 401 + WWW-Authenticate.
- Provas: unitário 10/10; interno e público 401/200/401(senha errada); UFW já bloqueia 8084 de fora. Rollback `.bak_pre_auth_20260913`.
- Casa avisada: ponte de_dell ZM-20260913-002 (commit cirúrgico; sync recusou worktree sujo alheio).
- Fórum: `Foruns/forum_painel_v6_autenticacao_20260913.md` + memória `memorias_provisorias/memoria_painel_v6_autenticacao_20260913.md`.

## 16/09/2026 ~18:2x — 📊 MANUAL DE GRÁFICOS V1 criado (ordem Miguel: "o Cérebro tem que ter manual de gráficos")

- `Estilo/MANUAL_DE_GRAFICOS_V1.md` — regras de qualidade dos SVGs do painel: **(1) rótulo segue o lado da linha** (em cima→rótulo em cima; embaixo→embaixo; em 2 linhas, cada uma rotula para FORA — decisão por ponto); (2) rótulos grandes/transparentes (17px/0.55) início-meio-fim; (3) cor do rótulo = cor da linha; (4) headroom ~15-18%; (5) padrões de cor da casa; (6) dados honestos (dia parcial/nascimento fora, quebra de série anotada); (7) eixos por métrica com Pearson da janela visível.
- Aplicado no ar em `svg_semanal_defasada` (3+3 rótulos por lado, teste anti-colisão) e `svg_linha_dupla` (MM rotula abaixo quando mergulha sob a azul).
