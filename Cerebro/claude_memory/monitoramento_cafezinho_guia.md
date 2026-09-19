---
name: Guia de Monitoramento Contínuo do Cafezinho (Slot 6)
description: Memória hub que centraliza tudo que uma sessão de monitoramento precisa — quais memórias ler, qual SSH usar, quais logs varrer, como reportar e onde gravar. Ler ANTES de cada tick.
type: reference
originSessionId: 359cf71d-e9c2-425b-9033-99a3ae54bfa5
---
> **Quando ler:** despertou pra rodar Slot 6 (monitoramento contínuo) ou foi acordado por um tick do `/loop` de monitoramento. Ler INTEIRA antes do primeiro check de cada sessão; releitura rápida nos ticks seguintes.

---

## 🎯 Escopo do Slot 6 — APENAS PORTAL CAFEZINHO

> **DELIMITAÇÃO 2026-04-26 11:18 BRT (Miguel):** Slot 6 cuida **apenas do portal Cafezinho**. Não invade outros slots. NÃO ler canal Antigravity. NÃO entrar em propostas de reorganização de memória, projeto Bella Ciao, ou Slot 3 Comentaristas (este último tem sessão Claude dedicada e cuida da própria telemetria).

Monitoramento autônomo do **portal Cafezinho** em três eixos a cada checkpoint (default 30 min):

1. **Técnico** — sistema firme: Trindade publicando, Sentinela V4 viva, Autocura V4 viva, crontab íntegro, sem traceback novo, sync NYC saudável, carga/uptime razoáveis.
2. **Jornalístico** — qualidade editorial dos posts publicados: títulos com peso, parágrafos 2-3 frases, foto casa com tema, sem alucinação temporal, fecho natural, citação IA crua removida.
3. **Audiência (GA4)** — pulso de tráfego: realtime users, sessions/views/users hoje, engagement rate, top 10 páginas, delta vs tick anterior, posts publicados hoje que já estão pegando tração.

Autoridade: **detectar → corrigir → registrar** sem pedir ok caso-a-caso (`feedback_autonomia_monitoramento_20260417.md`). Exceções (pedir ok antes): ações irreversíveis — deletar crontab, reset de credencial compartilhada, sobrescrever banco SQLite, mensagem externa em massa.

**Fora de escopo neste slot** (cuidado por outras sessões/slots):
- Slot 1 — Custos e reforma do sistema
- Slot 2 — Análise V2 (pausado)
- Slot 3 — Comentaristas (incluindo "pares simultâneos <60s", Telegram 400 do comentarista, etc.)
- Slot 4 — Eleições
- Canal Antigravity (`Foruns/canal_claude_antigravity.md`)
- Reorganização de memórias do Antigravity
- Projeto Bella Ciao

---

## 📚 Memórias obrigatórias por categoria

### 🔌 Acesso (SSH, infra, chaves)
- `ssh_servidores_cafezinho.md` — porta **38422** (NÃO 22)
- `ssh_usuario_ubuntu.md` — login `ubuntu@`, sudo NOPASSWD
- `infra_servidores_cafezinho.md` — Tencent (Cingapura) `43.156.151.165` + NYC `45.55.50.249` + GSN `159.89.237.100`
- `reference_chaves_guia.md` — onde achar credenciais (`chaves/` na raiz + `.env.unificado` no Tencent)
- `protocolo_seguranca_cafezinho.md` — protocolo geral de mudanças
- `regra_critica_rsync_nao_usar_a.md` — NUNCA `-a/-o/-g` em rsync pra `/root/` (lock-out SSH)

### 🛠️ Operação (crontab, sync, sentinela)
- `crontab_espelho_oficial.md` — espelho canônico em `crontab_server.txt`
- `coordenacao_crontab_deploy.md` — multi-autor, checar mtime + sentinelas
- `sentinela_v4_arquivos_canonicos.md` — quais arquivos a sentinela toca
- `sync_cingapura_nyc_correto.md` — sync correto Tencent → NYC
- `arquitetura_nyc_backup_temporal.md` — NYC é backup temporal, não espelho
- `playbook_paralisacao_ponteiro.md` — como parar tudo sem quebrar
- `manual_de_bugs_ler_primeiro.md` — LER antes de propor fix de bug recorrente

### 📰 Padrão editorial (eixo jornalístico)
- `feedback_publicar_os_melhores.md` — política "publicar os melhores"
- `feedback_data_chumbada_link_tangencial.md` — proibido "Nesta segunda-feira, 26/04/2026"
- `feedback_fecho_natural_sem_e_dai.md` — sem fórmula rígida de fecho
- `feedback_freshness_datas_inflacao.md` — freshness Inflação + remover citação IA crua
- `feedback_agente_mercado_regras_editoriais_20260424.md` — regras agente mercado
- `feedback_priorizar_categorias_audiencia.md` — priorizar editorias de alta audiência

### 🤖 Pipeline e agentes
- `pipeline_llms_cafezinho.md` — 6 LLMs em cascata (gpt-5 → grok → claude → perplexity → claude-fb → gemini)
- `banco_midia_cafezinho.md` — banco SQLite de fotos
- `flickr_live_modulo_compartilhado_20260420.md` — `flickr_live.py`
- `agente_youtube_arquitetura.md` + `youtube_agent_desligado_20260418.md` — YouTube DESLIGADO
- `fb_token_longlived_20260417.md` — FB token expira **2026-06-16**
- `agente_analise_v2_deploy_20260425.md` — Análise V2 deployado 25/04
- `reducao_crontab_20260424_2343.md` — A/B test crontab reduzido
- `forum_custos_qualidade_aprovado_20260425.md` — plano emergencial §19 LIVE

### 🤝 Disciplina, comunicação e autoridade
- `feedback_autonomia_monitoramento_20260417.md` — **CRÍTICA** — autoridade pra corrigir sem pedir ok
- `feedback_terminar_e_subir.md` — terminar código e subir, sem pausar
- `feedback_bots_telegram_nunca_param.md` — bots Telegram não podem cair
- `feedback_timestamp_em_toda_comunicacao.md` — toda mensagem abre com `[YYYY-MM-DD HH:MM:SS BRT]`
- `feedback_timestamp_completo_em_logs.md` — timestamp em logs "sem novidade"
- `feedback_atualizar_canal_proativo.md` — avisar Miguel sem esperar
- `feedback_responder_direto_pelas_novidades.md` — direto ao ponto
- `feedback_explicar_jargao_na_hora.md` — explicar termo técnico ao usar
- `project_desencaixe_timestamp_canal_25abr.md` — canal Antigravity ~1h7min adiantado
- `feedback_nunca_heredoc_em_memoria_compartilhada.md` — NUNCA HEREDOC/`open(w)` em .md compartilhado; usar Edit
- `feedback_fix_canonico_primeiro.md` — fix sempre no canônico LOCAL primeiro

### 📋 Estado vivo (slots paralelos relevantes)
- `Tarefasdeagora.md` — slots ativos (Slot 3 Comentaristas tem checkpoint 14:40 BRT 26/04)
- `sessao_pausa_eleicoes_pilar1_20260424.md` — Pilar 1 Eleições draft 239311 aguarda Miguel
- `sessao_pausada_20260424_1915.md` — sessão pausada 24/04 19:15
- `blindagem_ancoras_universal_20260424.md` — blindagem anti-alucinação âncoras
- `investigacao_truncamento_textos_20260425.md` — investigação truncamento 25/04
- `fix_deepseek_branch_roteador_20260425.md` — fix branch deepseek
- `fix_observador_truncamento_20260424.md` — fix observador truncamento

---

## 📂 Onde escrever os relatórios

**Diretório dedicado:** `/home/migueldorosario/Downloads/Antigravity Google/monitoramento cafezinho/`

**Convenção de arquivo:** um arquivo por dia, nome `monitoramento_YYYYMMDD.md`.

**Estrutura do arquivo:**

```markdown
# Monitoramento Cafezinho — YYYY-MM-DD

📂 **ABRIU:** YYYY-MM-DD HH:MM:SS BRT  (timestamp do primeiro tick do dia)

---

## Tick HH:MM BRT
- Técnico: ✅/⚠️/🔴 ...
- Jornalístico: ✅/⚠️/🔴 ...
- Slot 3: ✅/⚠️/🔴 ...
- Fixes aplicados: ...
- Pendências pra Miguel: ...

---

## Tick HH:MM BRT
...

---

🔒 **FECHOU:** YYYY-MM-DD HH:MM:SS BRT  (timestamp do último tick antes de meia-noite OU quando Miguel mandar parar)
```

**Regras de escrita:**
- Primeira escrita do dia: criar arquivo com cabeçalho + `📂 ABRIU`. Sempre via `Write` (criação) ou `Edit` (append) — NUNCA HEREDOC nem `cat >`.
- Tick subsequente: append via `Edit` no final do arquivo, ANTES da linha de fecho (ou simplesmente acrescentando ao fim se ainda não fechado).
- Cruzou meia-noite? Fechar arquivo do dia anterior com `🔒 FECHOU` no penúltimo tick do dia (ou quando o primeiro tick do dia novo perceber a virada). Abrir novo arquivo do dia atual.
- `/loop` parou (TaskStop ou Miguel mandou parar)? Fechar arquivo do dia com `🔒 FECHOU` no último tick.

---

## 🔍 Comandos canônicos por tick

### Eixo técnico

```bash
# Timestamp BRT (sempre primeiro)
TZ='America/Sao_Paulo' date '+%Y-%m-%d %H:%M:%S BRT'

# (a) Tracebacks novos últimos 30min
ssh -i ~/.ssh/id_rsa -p 38422 ubuntu@43.156.151.165 \
  "sudo find /var/log -name '*.log' -mmin -30 -exec grep -l Traceback {} \;"

# (b) Tail do log unificado pra contexto
ssh -i ~/.ssh/id_rsa -p 38422 ubuntu@43.156.151.165 \
  "sudo tail -n 50 /root/agente_cafezinho_unificado_log.txt"

# (c) Posts publicados últimos 5 (Cafezinho)
curl -s -u "Redator:Ziod RKRI SESl vGwF UfGW KJWG" \
  "https://controle.ocafezinho.com/wp-json/wp/v2/posts?per_page=5&status=publish" \
  | jq '.[] | {id, title: .title.rendered, date, link}'

# (d) Crontab linhas (esperado ~41)
ssh -i ~/.ssh/id_rsa -p 38422 ubuntu@43.156.151.165 'sudo crontab -l | wc -l'

# (e) Sentinelas do crontab (SHELL, temáticos, autocura, sync)
ssh -i ~/.ssh/id_rsa -p 38422 ubuntu@43.156.151.165 \
  'sudo crontab -l | grep -E "^(SHELL|agente_matriz|autocura|sync_nyc)" | head'

# (f) Heartbeat sentinela V4 (último log)
ssh -i ~/.ssh/id_rsa -p 38422 ubuntu@43.156.151.165 \
  "sudo ls -lt /var/log | grep -i observ | head -5"

# (g) Carga / processos zumbis
ssh -i ~/.ssh/id_rsa -p 38422 ubuntu@43.156.151.165 \
  "uptime && ps aux | grep -E 'python|ffmpeg' | grep -v grep | wc -l"
```

### Eixo jornalístico

Pegar os 3 posts mais recentes via WP API e avaliar:
- **Título:** sujeito + verbo forte + consequência? (não Title Case americano, não verbo fraco)
- **Lide:** sem data chumbada ("Nesta segunda-feira, 26 de abril de 2026")?
- **Parágrafos:** 2-3 frases cada? Nenhum de 1 frase só?
- **Foto:** casa com tema? Tem crédito real visível?
- **Fecho:** natural? (sem "E daí?", "Em resumo")
- **Citação IA crua:** ausente? (não pode ter `([fonte.com](url))`)
- **Cross-link:** "Leia também" no final?

Se algum post tiver problema sério (alucinação, foto errada grosseira), aplicar fix conforme autoridade — rebaixar pra draft via `curl -X POST .../posts/<ID> -d '{"status":"draft"}'` ou corrigir título.

### Slot 3 Comentaristas — FORA DE ESCOPO

Não checar aqui. Há sessão Claude dedicada ao Slot 3.

### Audiência (GA4) — snippet canônico

Service account: `/root/keys/ga4.json` no Tencent. Property: `374552425`. Lib: `google-analytics-data` (já no `/root/venv`).

```bash
ssh -i ~/.ssh/id_rsa -p 38422 ubuntu@43.156.151.165 'sudo /root/venv/bin/python3 -c "
import os, json
from datetime import datetime, timedelta, timezone
os.environ[\"GOOGLE_APPLICATION_CREDENTIALS\"]=\"/root/keys/ga4.json\"
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import RunRealtimeReportRequest, RunReportRequest, Metric, Dimension, DateRange
PROP=\"properties/374552425\"
c=BetaAnalyticsDataClient()
out={}
rt=c.run_realtime_report(RunRealtimeReportRequest(property=PROP, metrics=[Metric(name=\"activeUsers\")]))
out[\"realtime_users\"]=int(rt.rows[0].metric_values[0].value) if rt.rows else 0
td=c.run_report(RunReportRequest(property=PROP, date_ranges=[DateRange(start_date=\"today\", end_date=\"today\")], metrics=[Metric(name=\"sessions\"), Metric(name=\"screenPageViews\"), Metric(name=\"totalUsers\"), Metric(name=\"engagedSessions\")]))
v=[m.value for m in td.rows[0].metric_values] if td.rows else [\"0\",\"0\",\"0\",\"0\"]
out[\"sessions\"], out[\"pageviews\"], out[\"users\"], out[\"engaged\"]=int(v[0]),int(v[1]),int(v[2]),int(v[3])
out[\"engagement_rate\"]=round(out[\"engaged\"]/max(out[\"sessions\"],1)*100,1)
top=c.run_report(RunReportRequest(property=PROP, date_ranges=[DateRange(start_date=\"today\", end_date=\"today\")], dimensions=[Dimension(name=\"pageTitle\"), Dimension(name=\"pagePath\")], metrics=[Metric(name=\"screenPageViews\")], order_bys=[{\"metric\":{\"metric_name\":\"screenPageViews\"},\"desc\":True}], limit=10))
out[\"top10_geral\"]=[{\"title\":r.dimension_values[0].value, \"path\":r.dimension_values[1].value, \"views\":int(r.metric_values[0].value)} for r in top.rows]
# Top 10 dos publicados nas últimas 24h (filtra paths /YYYY/MM/DD/ de hoje ou ontem em BRT)
brt=timezone(timedelta(hours=-3))
hoje=datetime.now(brt).strftime(\"/%Y/%m/%d/\")
ontem=(datetime.now(brt)-timedelta(days=1)).strftime(\"/%Y/%m/%d/\")
amplo=c.run_report(RunReportRequest(property=PROP, date_ranges=[DateRange(start_date=\"today\", end_date=\"today\")], dimensions=[Dimension(name=\"pageTitle\"), Dimension(name=\"pagePath\")], metrics=[Metric(name=\"screenPageViews\")], order_bys=[{\"metric\":{\"metric_name\":\"screenPageViews\"},\"desc\":True}], limit=200))
recentes=[]; vistos=set()
for r in amplo.rows:
    p=r.dimension_values[1].value
    if p.startswith(hoje) or p.startswith(ontem):
        slug_base=p.replace(\"/amp/\",\"/\").rstrip(\"/\")
        if slug_base in vistos: continue
        vistos.add(slug_base)
        recentes.append({\"title\":r.dimension_values[0].value, \"path\":p, \"views\":int(r.metric_values[0].value)})
        if len(recentes)>=10: break
out[\"top10_publicados_24h\"]=recentes
print(json.dumps(out, ensure_ascii=False))
"' 2>/dev/null
```

**Cache de delta:** salvar saída do tick em `/home/migueldorosario/Downloads/Antigravity Google/monitoramento cafezinho/.audiencia_ultimo.json`. No próximo tick, ler antes de gravar e calcular `Δ pageviews`, `Δ users`, `Δ realtime`, `Δ views por post no top10_publicados_24h` (pra ver quem está acelerando).

**Identificar "posts publicados hoje no top":** comparar `pagePath` do `top10_geral` com paths dentro de `top10_publicados_24h`. Marcar com `🆕 publicado hoje` (se path comeca com hoje) ou `📅 ontem` (se ontem).

**Output no relatório:**
```
### 🌐 Audiência (GA4)
- Realtime: N usuários online (Δ vs tick anterior: ±X)
- Hoje: S sessions / V pageviews / U users / E engaged (engagement N%)
- Δ vs tick anterior: +Δviews views / +Δusers users

#### 🏆 Top 10 GERAL hoje (todas as datas)
1. NNN views — Título (🆕 hoje | 📅 ontem | ⏪ N dias)
...

#### 🆕 Top 10 dos publicados nas últimas 24h
1. NNN views — Título (🆕 hoje HH:MM | 📅 ontem HH:MM)
...
```

---

## 🚦 Status flags pro relatório

- ✅ **OK** — comportamento esperado, sem desvio
- ⚠️ **ATENÇÃO** — desvio menor, vale registrar mas não bloqueia (ex: 1 traceback transitório, 1 título médio)
- 🔴 **CRÍTICO** — sistema parado/quebrado ou alucinação grave (ex: Maestro caído, post com data chumbada errada, crontab corrompido)

🔴 dispara fix imediato + nota explícita pra Miguel no resumo do tick.

---

## 🔄 Ritmo & comunicação

- **Toda mensagem ao Miguel:** abre com `[YYYY-MM-DD HH:MM:SS BRT]` (rodar `date` antes — não confiar em relógio do canal Antigravity, que está ~1h7min adiantado conforme `project_desencaixe_timestamp_canal_25abr.md`).
- **Resumo no chat por tick:** curto (5-10 linhas). Status por item, fixes aplicados, pendências.
- **Sem novidade:** ainda assim reportar `[ts] Tick HH:MM ✅ tudo verde, próximo às HH:MM` — silêncio NÃO é resposta válida.
- **Achou 🔴:** reportar JÁ no chat (não esperar próximo tick) + tentar fix automático conforme autoridade.

---

## 🛑 Quando parar o loop

- Miguel disse pra parar (TaskStop + fechar arquivo do dia com 🔒 FECHOU).
- Erro irrecuperável no próprio loop (ex: SSH morto > 3 ticks seguidos): reportar e pausar tick-by-tick até confirmação.
- Slot 6 marcado como ✅ CONCLUÍDO no `Tarefasdeagora.md`.

Ao parar: SEMPRE fechar o arquivo do dia com `🔒 FECHOU: <ts BRT>` na última linha.
