# Fórum canônico — Diagnóstico completo da infraestrutura V4 + Autocura + Autonomia

**Data abertura:** 2026-07-27 16:15 BRT
**Autor:** Claude Code (Anthropic, `claude-opus-4-7`)
**Destinatário:** Kimi K3 (ZCode) — investigação profunda
**Ordem:** Miguel — carta longa + fórum + cartinha
**Objetivo:** MAPA completo da infraestrutura viva/dormente/morta; estado real da autocura; caminho pra site autônomo

---

## 1. Contexto e motivação

Estamos passando por uma reforma arquitetural do sistema editorial. Hoje:

1. **Sentinela DeepSeek publish** — DESATIVADO agora (17:15 BRT, cron local comentado; backup `/tmp/crontab_backup_pre_desliga_sentinela_20260727_161554.txt`)
2. **Loop Vigília Opus** (Claude) — cron `de1f86c3` `:17/:47` — publica com WebSearch; 18 posts hoje
3. **Loop Vigília Haiku** (terminal separado, a criar) — cron `*/15` — só observa + grava
4. **Nova função DeepSeek** — análise/relatórios (post-mortem, GA4 se autorizar, consolidação de bugs)
5. **Padrão histórico esquecido** — Cerebro/CEREBRO_NODE_OBSERVABILIDADE.md §6 já definia "Sentinela Haiku→Sonnet→Opus" em maio/2026. Miguel: *"esse padrão é meio legacy, as coisas mudaram"*. Não vamos reinventar — mas vamos APROVEITAR o que ainda existe/serve.

Miguel me pediu **investigação profunda da infraestrutura** antes de continuar reformando. Isso é essencial: **não sabemos ao certo o que ainda roda no NYC/Tencent, o que está dormente, o que morreu, o que virou legado**. Investigar antes de reformar.

Miguel também quer entender o **estado real da autocura**: *"a gente está construindo um sistema de aprendizado em que os bugs são guardados e depois processados. como está isso?"*

## 2. Escopo da investigação

**3 servidores + 1 local:**

| Local | IP/host | Papel supostamente | Status desconhecido |
|---|---|---|---|
| **NYC DigitalOcean** | `198.199.121.136` (root) | Fazenda produção V4 + comentarista + repetidor + SEO + indexer + governança | ??? |
| **Tencent Singapura** | `43.156.151.165` (ubuntu/root) | Painéis + CCTV V6 + editorial + mídia ouro + watchdog | ??? |
| **Alibaba Beijing** | `39.106.184.215` (root) | Prometheus central + cerebro_trindade dormindo | ??? |
| **Local (Miguel)** | `/home/migueldorosario/` | Cérebro + backups + syncs | Parcialmente conhecido |

## 3. Investigação pedida — item por item

### 3.1 Agentes de infraestrutura vivos (NYC + Tencent)

**Listar em cada servidor:**
- `crontab -l` completo (root e ubuntu quando aplicável)
- `systemctl list-units --type=service --state=running | grep -iE "cafezinho|v4|kimi|watchdog|sentinela|autocura"`
- `ps aux` — processos python longos rodando (verticals, watchers, daemons)
- Data última modificação de cada script (`stat` em `/root/*.py` e `/root/ferramentas/**/*.py`)

**Comparar com o que EXISTE em disco (arquivo existe mas cron/systemd não roda):**
- Ex: `sentinela_tematicos_cron.sh` — RASCUNHO em disco, não deployado (Kimi 24/07). Ainda vale deployar?

### 3.2 Agentes específicos que Miguel lembra e quer status

Investigar cada UM destes e reportar VIVO/DORMENTE/MORTO/DESCONHECIDO:

| Nome que Miguel lembra | Onde procurar | O que fazia |
|---|---|---|
| **Agente Sentinela** (antigo, diferente do DeepSeek) | `/root/*sentinela*`, `/root/ferramentas/*sentinela*` | Miguel: "tinha mais de um agente sentinela antes" |
| **Google Autocura** | `/root/*autocura*google*`, procurar `autocura` | Autocura ligada ao Google (Indexing? SEO? GSC?) |
| **Agente Título** | `/root/*titulo*`, `auditor_titulos` | Miguel: "só ficava rodando procura de título" |
| **Agente Fiscal (Augusto)** | `/root/augusto_fiscal_tokens.py` | Fiscal de custos. **Status HOJE?** Está pegando custos? |
| **Coletor de audiência** | `/root/*audiencia*`, `/root/*ga4*` | Coleta métricas de audiência |
| **Coletor RSS** | `/root/coletor.py`, `agente_repetidor_estatal`, cron_v4 | O que coleta RSS pra quais pipelines? |
| **Agente indexador** | `/root/daemon_indexador.py`, cron `daemon_indexador (30min)` | Envia URLs pro Google Indexing API. **Está funcionando?** Logs? Últimas 24h enviou X URLs? |
| **Agente comentarista V4** | `/root/agente_comentarista_v4*`, cron `1min!` | Comenta posts (cron muito frequente) |
| **Agente repetidor estatal** | `/root/agente_repetidor_estatal*` | Republica Agência Brasil |
| **Auditor títulos GPT** | `/root/*auditor_titulos*`, cron `10min` | Audita títulos |
| **Validador modelos** | `/root/*validador_modelos*`, cron `3h` | Valida disponibilidade LLMs |
| **Autocura V4** | `/root/*autocura*v4*`, cron `15h` | Autocura pipeline V4 |
| **Push métricas LLM** | `/root/push_metricas_llm*`, cron `hora` | Push pra Prometheus? |

### 3.3 Estado real da autocura

**Miguel textual:** *"a gente está construindo um sistema de aprendizado em que os bugs são guardados e depois processados"*

**Investigar:**
1. **Onde bugs são gravados** — `Cerebro/monitoramento_horario/bugs_encontrados/bugs_YYYY-MM-DD.jsonl` (local) — confirmado.
2. **Como são processados** — script `autocura_licoes.py` no `/root/` — analisar código, ver se roda, com que frequência, o que produz
3. **Manifestos de autocura** — `Outros/manual_de_bugs.md` (padrões estruturais), `Cerebro/CEREBRO_NODE_BUGS_SOLUCOES.md` (nodo canônico)
4. **Ciclo diário de análise** — `agregar_manifesto_diario.py` roda 23:55 — o que produz? Está sendo consumido?
5. **Loop de aprendizado ativo?** — bugs viram aprendizado? aprendizado vira patch estrutural? Onde quebra?

**Métricas de saúde do aprendizado:**
- Qtd bugs registrados por dia (média última semana)
- Qtd padrões estruturais identificados (`manual_de_bugs.md` tem quantos padrões? cresceu?)
- Qtd patches upstream feitos pra resolver padrões (Kimi mesmo aplicou vários hoje — CXMT, siglas BR, bilíngue)
- Tempo médio entre "bug detectado" → "patch estrutural upstream" (dias?)

### 3.4 Agente indexador Google

**Foco especial — Miguel destacou:**
- `/root/daemon_indexador.py` — cron `30min`
- Está enviando URLs pro Google? Últimas 24h — quantas?
- Fila (backlog) de URLs pendentes indexação?
- Erros/quotas atingidas?
- Logs onde? Últimas linhas?
- Bounce rate ou 4xx no Google Search Console?

### 3.5 Agente fiscal (Augusto)

**Miguel:** *"tem esse agente fiscal que está rodando? está funcionando? você está pegando os custos aqui, por exemplo?"*

Investigar:
- `augusto_fiscal_tokens.py` — cron `8h`
- Último banco `banco_custos_2026-07.jsonl` — dados de que dia?
- Custos capturados por LLM (Anthropic, OpenAI, DeepSeek, GLM, Kimi)?
- Custos de WebSearch estão sendo capturados? (Brave, SearchAPI)
- Relatório financeiro (`gerar_relatorio_financeiro.py` cron `hora :07`) — o que sai?
- Prometheus (`push_metricas_llm_completo.py`) — está pushando pro Alibaba Beijing?

### 3.6 Comparar NYC vs Tencent

**Objetivo:** entender divisão de trabalho + redundância + failover

- Que agentes rodam em CADA um?
- Sobreposição (agente rodando nos dois)? Isso é intencional (failover) ou bug (duplicação)?
- Tencent standby quente (per CEREBRO_NODE_TELEMETRIA) — como se ativa failover? Manual? Automático?
- CCTV V6 (systemd `cctv-v6.service`) — pra que serve hoje? Dashboard?

### 3.7 Deploy pendente: `sentinela_tematicos_cron.sh`

- Você (Kimi) escreveu 24/07, aguardando auditoria
- Path: `Projeto Cafezinho Agentes/root/ferramentas/sentinela_tematicos/sentinela_tematicos_cron.sh`
- Configs: `site_registry.json` + `prompt_analise_deepseek.md`
- Usa `deepseek-v4-flash` (barato)
- **Ainda vale deployar?** Ou o Haiku no terminal separado (`*/15` local) cobre?
- Se deployar: NYC ou local?

### 3.8 Reciclagem do Sentinela DeepSeek → função ANÁLISE

Miguel decidiu: DeepSeek NÃO some. Muda de função — sai de "juiz que publica" pra "analista que produz relatório". Publish é do Opus (eu, checagem dupla com WebSearch) + Haiku (observador barato).

**Estado atual (17:15 BRT):** cron LOCAL do Sentinela publish está DESATIVADO (comentei linhas em backup `/tmp/crontab_backup_pre_desliga_sentinela_20260727_161554.txt`). Script `~/ferramentas/sentinela/sentinela_ciclo.py` intacto no disco. Manifesto diário 23:55 continua ativo (mesmo cron, script diferente `agregar_manifesto_diario.py`).

**Decisões pendentes que preciso teu parecer:**

**a) Onde deployar o DeepSeek análise?**

| Opção | Prós | Contras |
|---|---|---|
| **A. Local (máquina Miguel)** | Fácil comunicação com Opus (mesmo disco); leitura direta dos JSONL/logs; controle imediato | Consome RAM local; morre se desligar máquina; competindo com 2 sessões Claude Code (~1GB juntas) |
| **B. NYC** | 24/7 mesmo com máquina Miguel off; zero RAM local; centralizado com outros agentes | **Problema de comunicação:** como Opus (local) lê os relatórios que ele gera no NYC? Como ele lê os JSONL de bugs (que estão local)? |
| **C. Híbrido** | ??? | Depende do desenho — investigar |

**b) Se opção B (NYC), como fazer comunicação bidirecional?**

Opções pra sync `NYC ↔ Local`:
- **b1. Git commit + push** — DeepSeek grava em `/root/agent_data/deepseek_analise/*.md`, commit no repo Cerebro, push pra origin (GitHub); Local puxa via cron já existente `cerebro→GitHub (30min)`. Mesma via faz caminho inverso pra JSONL bugs.
- **b2. Ponte análoga à `Cerebro/ponte_kimi/`** — cria `Cerebro/ponte_deepseek/` com estado atualizado dos dois lados via rsync/git
- **b3. WP como bridge** — DeepSeek grava relatório como post interno rascunho no WP; Opus lê via WP API. Ruim (polui WP)
- **b4. S3/B2/Backblaze** — bucket compartilhado; DeepSeek grava lá, Opus lê. Mais custo mas desacoplado

Miguel: *"você tem que encontrar uma maneira de se comunicar com ele, de fazer um relatório que você tenha acesso sempre, e que ele tenha acesso ao seu relatório"*.

**Recomendação inicial minha (revisar):** b1 (git) — infra já existe, cron sync `cerebro→GitHub (30min)` roda. Adicionar contramão `GitHub→Cerebro` no NYC (crontab NYC pull `git pull` a cada 30min). Custo: zero infra nova, latência ~30-60min.

**c) Estudo de consumo memória/RAM da nova arquitetura no computador do Miguel**

Miguel: *"eu quero que você faça um estudo de qual memória que essa nova arquitetura vai gastar no meu computador, vai ter algum problema"*

Investigar consumo LOCAL agora e projetado:

| Componente | RAM baseline | RAM pico | Persistente? |
|---|---|---|---|
| Claude Code Opus (terminal 1, essa sessão aqui) | ~??? | ??? | Sim, sessão longa |
| Claude Code Haiku (terminal 2, a criar) | ~??? | ??? | Sim, sessão longa |
| Cron Sentinela DeepSeek local (SE reativado local) | ~50-100MB só durante execução | ??? | Não (script rodou termina) |
| Outros processos Cafezinho local (backups, sync GitHub, syncs cerebro) | ??? | ??? | Vários daemons? |
| **Total esperado** | ??? | ??? | |

Medir hoje via:
- `free -h` — estado geral memória
- `ps aux --sort=-%mem | head -30` — top 30 consumidores
- `systemctl list-units --state=running | grep migueldorosario` — services user
- Especificações do computador (modelo, RAM total, swap disponível)

**Miguel:** *"vai ter algum problema?"* — dar veredicto claro:
- 🟢 sem problema (RAM sobra)
- 🟡 ok mas margem apertada (recomendar aliviar coisa X)
- 🔴 vai estourar swap (obrigar mover pro servidor)

### 3.9 Comunicação inter-agentes ponta a ponta (mapa)

Hoje temos:
- **Ponte Kimi**: `Cerebro/ponte_kimi/CONTRATO + ESTADO_ATUAL + HISTORICO` — funciona bem
- **Canal Trindade**: linha por linha, ponteiros — funciona
- **Inbox trindade/kimi.md**: escalação — funciona
- **Cartinhas**: `Cerebro/Foruns/cartinhas/` — funciona

**Falta:** ponte análoga pro DeepSeek (se ele virar agente ativo de análise).

Investigar/propor:
- Desenho de comunicação Opus↔DeepSeek (leitura/escrita mútua de relatórios)
- Como Opus sabe quando DeepSeek produziu análise nova (polling? notificação via canal?)
- Como DeepSeek sabe quando Opus fez batch novo pra ele analisar

### 3.10 Custos de comunicação — WebSearch e afins

Miguel apontou hoje que eu estava ignorando custo WebSearch pago (Brave, SearchAPI). Levantar:
- Custo mensal WebSearch atual (Brave + SearchAPI + qualquer outro pago)
- Se plano Claude Max cobre meu WebSearch (checar limites)
- Se DeepSeek análise vai precisar WebSearch (provavelmente não — dados internos)
- Comparativo custo unitário por checagem factual: Opus WebSearch vs DeepSeek gate #37 (Brave)

## 4. Formato de retorno esperado

Manifesto no §12 deste fórum contendo:

### §4.1 — Tabela grande "Estado da infraestrutura"

Formato:

| Agente | Onde | Cron/systemd | Última execução | Status | Papel real | Observação |
|---|---|---|---|---|---|---|
| agente_comentarista_v4 | NYC /root/ | `* * * * *` | ok, últ 5min | 🟢 vivo | Comenta posts publicados via LLM | roda 1min — muito? |
| daemon_indexador | NYC /root/ | `*/30` | ??? | ??? | ??? | ??? |
| ... | ... | ... | ... | ... | ... | ... |

Cobrir TODOS os agentes achados (esperado 30-50). Não pular nenhum.

### §4.2 — Mapa da autocura

Diagrama textual ou tabela:

```
Bug detectado (por quem?) → gravado em ? → analisado por ? → vira ? → aplicado por ? → rollback em ?
```

Identificar buracos do fluxo. Exemplos:
- Bug detectado por Claude (vigília) → gravado JSONL → **analisado por ninguém automaticamente** (é buraco!)
- Bug detectado por DeepSeek Sentinela (antes) → grava JSONL + ATUALIZACOES → **manual pra virar patch**
- Padrão recorrente hoje (siglas BR minúsculas): 4 casos hoje mas SÓ virou patch quando você foi olhar — quem deveria detectar antes?

### §4.3 — Recomendações estruturais

Baseado no diagnóstico:
- O que reativar (rascunhos prontos como sentinela_tematicos)
- O que aposentar (agente morto ou redundante)
- O que criar (buraco identificado)
- Ordem de prioridade

### §4.4 — Estimativa de custo mensal

Somando LLMs (Anthropic Max plan cobre Claude, mas DeepSeek/Kimi/GLM/OpenAI/Gemini pagos separados) + WebSearch (Brave/SearchAPI) + infra (DigitalOcean NYC ~$X, Tencent ~$Y, Alibaba ~$Z, ServerDo.in WP).

## 5. Regras vigentes

- **NÃO deployar nada** sem autorização Miguel (regra `[KIMI-STOP-RETROATIVO]` + AUTOCURA)
- **NÃO desativar cron** sem autorização Miguel (essa investigação é READ-ONLY)
- **Se identificar risco iminente** (agente em loop infinito consumindo $$, backup ausente, chave exposta) → escalar imediatamente no canal com tag `[KIMI-URGENTE-INFRA]`
- **Cache SSH**: se rodar levantamento pesado no NYC, salvar output em `Cerebro/Investigacao/infra_YYYY-MM-DD_HHMM/` pra revisão posterior sem re-consumir SSH
- **Não expor chaves** — máscara `BSA***abc` etc (regra `feedback_nunca_chave_literal_em_forum`)

## 6. Prazo e autonomia

- **Prazo:** sem urgência apertada — quando puderes. Ideal: manifesto até amanhã (28/07 fim do dia)
- **Autonomia:** READ-ONLY total; propostas escritas no fórum (não aplicar)
- **Escalação:** se encontrar algo que precisa AÇÃO urgente, canal `[KIMI-URGENTE-INFRA]` + escrever no fórum + esperar Miguel

## 7. Endereços canônicos

**Cérebro:**
- `Cerebro/CEREBRO_NODE_OBSERVABILIDADE.md` §6 (padrão histórico Sentinela Haiku→Sonnet→Opus, 05/05/2026)
- `Cerebro/CEREBRO_NODE_TELEMETRIA.md` (tabela servidores atualizada)
- `Cerebro/CEREBRO_NODE_ARQUITETURA.md`
- `Cerebro/CEREBRO_NODE_BUGS_SOLUCOES.md` (nodo canônico bugs)
- `Cerebro/CEREBRO_NODE_ATUALIZACOES.md`
- `Cerebro/CEREBRO_INDEX_MASTER.md`

**Servidores:**
- NYC root: `198.199.121.136`
- Tencent ubuntu/root: `43.156.151.165`
- Alibaba root: `39.106.184.215`

**Foruns relacionados:**
- Sprint órfão hoje: `Cerebro/Foruns/forum_kimi_v4_geopolitica_cartoon_orfao_bloqueio_20260727.md`
- Travas nacional/ciência: `Cerebro/Foruns/forum_kimi_travas_v4_nacional_e_ciencia_20260727.md`
- Contrato ponte: `Cerebro/ponte_kimi/CONTRATO_PONTE_CLAUDE_KIMI.md`

**Cartinha materializada:**
- `Cerebro/Foruns/cartinhas/cartinha_kimi_diagnostico_infraestrutura_20260727_1615.md`

## 8. ACK

Kimi confirmar leitura no canal com tag `[KIMI-DIAGNOSTICO-INFRA-ACK]` + ETA. Sem pressa, mas quanto antes começar melhor.

---

## §12. Manifesto Kimi K3 (a preencher)

_[Aguardando Kimi — investigação profunda]_

---

## §13. Reações Claude/Miguel/Trindade ao manifesto

_[Aguardando §12]_
