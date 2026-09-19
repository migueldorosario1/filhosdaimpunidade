# CEREBRO INDEX — Vigias

> **Status**: DRAFT Fase 1 — criado por GLM 17/06 ~14:05 BRT (Miguel autorizou frente via fórum Codex)
> **Node canônico associado**: `CEREBRO_NODE_VIGIAS.md` (a ser criado no nó Alibaba)
> **Fórum técnico**: `Projeto Cafezinho Agentes/Foruns/forum_reorganizacao_indexacao_backup_vigias_20260617.md`
> **Política**: indexação pura (read-only). Não há deploy associado a este arquivo.
> **Manutenção**: atualizar seções 4-9 a cada incidente significativo ou mudança de padrão operacional.

---

## 1. Visão Geral

Dois vigias monitoram o ecossistema Cafezinho:

| Vigia | Função | Localização | Modo |
|---|---|---|---|
| **Vigia Chinês / Tencent** | Observa production Cafézinho (Tencent 43.156.151.165): ticks consultivos, gates, offlines por provider, custo LLM, GA4 | nó Alibaba (espelho) | read-only |
| **Vigia NYC / externo** | Endereço externo do portal: HTTP status, latência, posts novos, WP API health | nó Alibaba (espelho) | read-only |

**Arquitetura**:
- Script produtor: `root/agente_relatorio_vigias.py` (no nó Alibaba)
- Output corrente: `root/agent_data/vigias/` (4 arquivos: 2 JSONs sobrescritos + 2 tails legíveis)
- Série histórica: `root/agent_data/vigias/relatorio_vigias_YYYYMMDD_HHMMSS.md` (já imutável)
- Resumo executivo: `CEREBRO_NODE_VIGIAS.md` (anexos horários)

**Problema estrutural diagnosticado** (forum Codex §4):
1. Node cresce sem particionamento
2. JSONs correntes sobrescritos → perda de granularidade histórica fina
3. Sem índice próprio (este arquivo corrige)
4. Sem backup dedicado (Fase 3)

---

## 2. Vigia Chinês / Tencent

### 2.1 KPIs monitorados

| Campo | Significado | Frequência |
|---|---|---|
| `TICK_CONSULTIVO` | Cada tick where consultas foram respondidas | horário |
| `GATE_OFFLINES_CONSECUTIVOS` | Gates caídos em sequência (sinal crítico) | horário |
| `WP_FAIL` | Falhas WP API detectadas | horário |
| `offline.deepseek` / `.kimi` / `.qwen` | Contagem offline por provider LLM | horário |
| `ga4_avg` | Média pageviews GA4 | horário |
| `custo_total_usd_est` | Custo LLM estimado US$ no tick | horário |

### 2.2 Snapshot JSON canônico

- **Corrente**: `vigia_chines_stats.json` (sobrescrito a cada run)
- **Proposto Fase 2**: `vigia_chines_stats_<run_id>.json` (timestamp imutável, em subpasta mensal)

### 2.3 Exemplo de saída (amostra histórica 10/06 07:25 BRT)

```json
{
  "eventos": {
    "TICK_CONSULTIVO": 1779,
    "GATE_OFFLINES_CONSECUTIVOS": 36,
    "WP_FAIL": 13
  },
  "offline": {
    "deepseek": 35,
    "kimi": 61,
    "qwen": 1
  },
  "ga4_avg": 422.7,
  "exemplos_tail": [
    {"ts": "2026-06-03 05:40:02 BRT", "tick": 1446, "evento": "WP_FAIL", "acao": "abort"}
  ]
}
```

### 2.4 Provider com maior incidência offline

- **Kimi**: 61 (vigilância especial — parece instável)
- **DeepSeek**: 35
- **Qwen**: 1 (estável)

---

## 3. Vigia NYC / externo read-only

### 3.1 KPIs monitorados

| Campo | Significado |
|---|---|
| `cron.runs` | Total de runs horários |
| `cron.ok` / `.fail` | Sucessos / falhas |
| `cron.crit` / `.warn` | Críticos / avisos |
| `tipos_top` | Top eventos: `post_novo_ok`, `wp_api_indisponivel`, `titulo_vazio`, `titulo_curto` |
| `latencia_avg` | Latência média HTTP |
| `crit_tail` | Últimos eventos críticos com detalhe (post_id, status) |

### 3.2 Snapshot JSON canônico

- **Corrente**: `vigia_nyc_stats.json` (sobrescrito)
- **Proposto Fase 2**: `vigia_nyc_stats_<run_id>.json`

### 3.3 Exemplo de saída (amostra histórica)

```json
{
  "cron": {"runs": 762, "ok": 748, "crit": 17, "warn": 12, "fail": 14},
  "tipos_top": [
    ["post_novo_ok", 3145],
    ["wp_api_indisponivel", 14],
    ["titulo_curto", 4]
  ],
  "crit_tail": [
    {"tipo": "wp_api_indisponivel", "status": 500},
    {"tipo": "titulo_vazio", "post_id": 256637}
  ]
}
```

### 3.4 Tail legível

- `vigia_nyc_relatorio_tail.md` — para leitura humana rápida (HTTP OK, status, latência, posts recentes)

---

## 3.5 Diagnóstico read-only do NODE (`CEREBRO_NODE_VIGIAS.md`) — Fase 1.3

> Verificado 17/06 14:46 BRT via SSH Alibaba (`root@39.106.184.215`). Apenas `stat` + `grep` + `head` — **NODE de produção não foi tocado** (per direção Codex "não mexe ainda").

**Estado real:**

| Métrica | Valor |
|---|---|
| Tamanho | **1.005.105 bytes** (~1 MB) |
| Linhas | **24.611** |
| Anexos "Relatorio dos Vigias" | **665** (mesma contagem dos arquivos `.md` soltos → **zero curtailment**) |
| Primeiro anexo | 2026-05-20 15:48:10 BRT (bootstrap — todos campos `None`) |
| Último anexo | 2026-06-17 14:25:20 BRT (hoje, vivo) |
| Kadência | ~1 anexo/hora (`:25` min fixo) → ~24/dia |
| Estrutura | Apenas 1 cabeçalho simples + 665 blocos anexados. **Sem** seção de KPIs agregados, **sem** incidentes destacados, **sem** links pra INDEX/snapshots mensais |

**Projeção de crescimento sem curtailment:**
- 30 dias: ~720 anexos × ~37 linhas = ~26.640 linhas (~1.1 MB)
- 90 dias: ~80.000 linhas (~3.3 MB)
- 180 dias (6 meses): ~160.000 linhas (~6.5 MB)
- 365 dias (1 ano): ~320.000 linhas (~13 MB)

**Conclusões (valida diagnóstico Codex §4 item 1 "Node cresce sem particionamento"):**

1. **NODE é literalmente um append-vivo de todos os 665 relatórios horários sem curtailment nenhum**. Não há agregação, não há destaque de incidentes, não há separação entre "resumo executivo" e "histórico fino".
2. **Conteúdo é 100% duplicado dos arquivos `.md` soltos** — cada bloco no NODE é idêntico a `relatorio_vigias_<run_id>.md` na pasta `vigias/`. Sem valor adicional no NODE hoje.
3. **Cabeçalho mínimo**: 3 linhas declarando função + regra de governança. Sem KPIs, sem atalhos.
4. **Primeiros blocos (20/05 15:48 e 15:49 BRT)** têm todos campos `None`/`False` — bootstrap do sistema. Podem ser removidos com segurança num curtailment futuro.

**Proposta de curtailment quando Codex liberar Fase 1.3 (NÃO aplicar ainda — apenas registrar proposta):**

- Manter no NODE: cabeçalho enriquecido (com KPIs agregados 24h/7d/30d + links pra INDEX + incidentes destacados + últimos 14 dias de anexos)
- Mover pra arquivo histórico mensal: `CEREBRO_NODE_VIGIAS_archive_2026-05.md` (~270 anexos antigos) + `CEREBRO_NODE_VIGIAS_archive_2026-06.md` (restante)
- Adicionar ao cabeçalho do NODE: link canônico pra este INDEX + política de retenção ("mantém 14d no NODE, resto em arquivos mensais")
- Remover primeiros blocos de bootstrap (20/05 15:48 e 15:49 — campos `None` puro)

**Volume estimado pós-curtailment (quando aplicado):**
- NODE vivo: ~336 anexos × 37 linhas = ~12.432 linhas (~510 KB) — **49% do tamanho atual**
- Arquivos mensais: ~270 (maio) + ~335 (junho passado) = ~605 anexos arquivados (~2.5 MB combinados)
- Total combinado: ~3.0 MB (igual ao total atual da pasta `vigias/` — sem perda de dados)

---

## 4. Incidentes destacados

> Seção a ser populada quando incidentes aparecerem. Critério de entrada:
> - 3+ `wp_api_indisponivel` em 1h, OU
> - `GATE_OFFLINES_CONSECUTIVOS > 50`, OU
> - custo estimado > US$ 5 em 1 tick, OU
> - GA4 cair > 30% vs média 24h, OU
> - arquivo corrente vigia vazio/zero bytes (novo critério adicionado 17/06)

| Data BRT | Vigia | Evento | Detalhe | Resolução |
|---|---|---|---|---|
| **2026-06-17 14:25** | NYC | `vigia_nyc_relatorio_tail.md` = **0 bytes** (estava 4960B no chinês). Relatório horário confirma: `período: None a None` + `tipos principais: []` + `custo total: US$0.0`. Suspeita: cron NYC caiu OU perdeu acesso SSH ao alvo externo. Latência média `1.086s` ainda aparece (parses de stat ainda rodam), mas coleta de eventos cron está vazia. | **Aberto** — flagrado pra Codex/Daemon na cartinha 14:35 BRT 17/06. Próximo passo sugerido: diagnosticar `cron.log` no Alibaba + verificar conectividade SSH outbound → alvo NYC. |
| **2026-06-08 ~11:25** (detectado 17/06 16:25) | Tencent (custo) | **Custo LLM em plateau há 9 dias** — `custo_total_usd_est` congelado em **US$ 0.8109** desde 08/06 11:25 BRT. Antes: subida contínua de US$ 0.25 (20/05) → US$ 0.81 (08/06). 254 ticks (38% do total) acima de US$ 0.78, **todos pós-07/06**. Possível bug no estimador OU teto artificial OU mudança manual no cálculo. Detalhe e hipóteses na seção 8. | **Aberto** — flagrado pra Codex/Daemon 16:30 BRT 17/06. Próximo passo: cruzar vs `/root/agent_data/llm_circuit_breaker_events.jsonl` real no Tencent; verificar `git log agente_relatorio_vigias.py` perto de 08/06. |
| _(a preencher conforme próximos incidentes)_ | | | | |

---

## 5. Offlines por provider — tendência

> Amostragem Fase 1.4 — 17/06 16:25 BRT. Soma cumulativa em todos os 666 ticks (não-média).

| Provider | Offlines acumulados (666 ticks) | Média/tick | Status |
|---|---|---|---|
| **Kimi** | **38.153** | 57 | 🔴 **instável** — 2.2× mais que DeepSeek |
| DeepSeek | 17.155 | 26 | 🟡 razoável |
| Qwen | 666 | 1 | ✅ estável |

> Kimi é consistentemente o provider com mais offlines em todos os ticks observados. Antes já tínhamos visto 61 em um único tick (10/06 07:25 BRT); agora confirmado como padrão sistêmico.

---

## 6. WP / API failures

Tipos canônicos observados (amostra manual de relatórios):

- `wp_api_indisponivel` (HTTP 500, timeouts WP) — **2-14 por tick** (baixo, dentro do esperado)
- `post_novo_ok` — **1.264-1.279 por tick** (cumulativo crescente, normal)
- `modified_antes_date` — 3 por tick (estável, sinal de edge case recorrente)
- `titulo_curto` — 3 por tick (estável)
- `titulo_vazio` — intermitente (ex: post 256637 em 10/06)

**Críticos/warnings NYC agregados**:

| crit/warn | Ticks | % |
|---|---|---|
| 17 / 12 | 201 | 30% |
| 4 / 8 | 105 | 16% |
| 2 / 6 | 80 | 12% |
| 4 / 7 | 62 | 9% |
| 17 / 11 | 52 | 8% |
| demais | 166 | 25% |

> 30% dos ticks rodam com 17 críticos + 12 warnings — patamar operacional normal do NYC.

---

## 7. GA4 — trend audiência

> Amostragem Fase 1.4 — 666 ticks analisados.

| Métrica | Valor |
|---|---|
| Média geral | **500.3 pageviews/hora** |
| Top 5 (mais altos) | **701.1** (20/05 — início do monitoramento, provável tráfego inicial elevado) |
| Bottom 5 (mais baixos) | **422.7** (08/06 — manhã de domingo, padrão esperado) |
| Faixa observada | 422.7 — 701.1 |

> A faixa é saudável e reflete padrão dia/semana esperado. Não há outliers de queda abrupta neste recorte.

---

## 8. Custo histórico LLM (estimado)

> Amostragem Fase 1.4 — 17/06 16:25 BRT. **Dado agregado direto dos 666 relatórios no Alibaba.**

| Período | Ticks | Total US$ | Média/tick |
|---|---|---|---|
| Total histórico (20/05 — 17/06) | 666 | **US$ 412.66** | US$ 0.6196 |
| Maio 2026 (parcial desde 20/05) | 270 | US$ 109.38 | **US$ 0.4051** |
| Junho 2026 (até 17/06) | 397 | US$ 303.29 | **US$ 0.7639** |

**Aumento maio→junho no custo médio/tick: +88.5%**

### Evolução cronológica do custo médio por dia

| Data | Ticks | Média US$/tick |
|---|---|---|
| 2026-05-20 | 9 | **0.2481** |
| 2026-05-21 | 23 | 0.2623 |
| 2026-05-25 | 24 | 0.3762 |
| 2026-05-28 | 24 | 0.4761 |
| 2026-06-01 | 22 | 0.6089 |
| 2026-06-05 | 24 | 0.7283 |
| 2026-06-08 | 24 | **0.8098** |
| 2026-06-11 | 24 | 0.8109 |
| 2026-06-14 | 24 | 0.8109 |
| 2026-06-17 (até 16:25) | 17 | 0.8109 |

### 🔴 INCIDENTE: Custo em plateau desde 08/06

**Sintoma**: O custo médio por tick está **congelado em US$ 0.8109 desde 08/06/2026** — há **9 dias sem variação**, após subir de US$ 0.25 (20/05) a US$ 0.81 (08/06) em 19 dias.

**Estatísticas**:
- 254 ticks (38% do total) estão acima de US$ 0.78 — **todos** agrupados cronologicamente entre 07/06 e hoje
- Após 08/06 11:25 BRT, nenhum tick registrou outro valor que não 0.8109 ou 0.81087
- Antes de 08/06, a subida era contínua e visível dia a dia

**Hipóteses (a investigar por Codex/Daemon)**:

1. **Bug no estimador de custo** — campo `custo_total_usd_est` em `agente_relatorio_vigias.py` pode estar calculando errado ou ter atingido teto artificial
2. **Custo é cumulativo desde bootstrap** — pode ter parado de incrementar
3. **Mudança manual** — alguém alterou fonte do cálculo em ~08/06 (verificar git log / alterações no script)
4. **Custo é média móvel** — paralisa quando denominador (tempo) cresce mais rápido que numerador

**Recomendação**: cruzar `custo_total_usd_est` reportado vs `/root/agent_data/llm_circuit_breaker_events.jsonl` real no Tencent. Se divergence > 10%, confirmar bug. Memória vinculante: `feedback_creditos_apis_primeiro_item_diagnostico_lentidao`.

**Registrado como incidente na seção 4 desta INDEX** (entrada 2026-06-08 ~11:25 BRT).

> Memória `feedback_creditos_apis_primeiro_item_diagnostico_lentidao` aplica: cruzar custo reportado vs circuit breaker real antes de concluir.

---

## 9. Links para snapshots por mês

> **Catálogo real Fase 1.2 — 2026-06-17 14:32 BRT (GLM via SSH Alibaba `39.106.184.215`)**
> Path canônico: `/root/cerebro_trindade/root/agent_data/vigias/` (no nó Alibaba — **não** Tencent)
> Total real catalogado: **665 relatórios em 2 meses** (estimativa inicial 50-200 → realidade 3-13× maior)
> Tamanho total do diretório: **2.8 MB**

### 2026-05
- **270 relatórios** confirmados (maio parcial — coleta começou dia 20/05 15:48 BRT)
- Primeiro: `relatorio_vigias_20260520_154807.md` (1.3KB, 21/05 02:48 CST)
- Último: `relatorio_vigias_20260531_232501.md` (a confirmar — limiar de mês)
- A organizar sob subpasta mensal quando Fase 2 (Codex) aplicar patch

### 2026-06
- **395 relatórios** confirmados (junho até 17/06 14:25 BRT — mês em curso)
- Mais recente: `relatorio_vigias_20260617_142501.md` (1.4KB, 18/06 01:25 CST = 17/06 14:25 BRT)
- Cadência observada: ~1 relatório/hora (`:25` min fixo) → ~24/dia
- Frequência atualizada última vez: 14:25 BRT hoje (saudável)

### 2026-07
- _(a partir de Fase 2 ativa — subpasta `2026-07/`)_

### Arquivos correntes (estado vivo) — verificado 14:32 BRT 17/06

| Arquivo | Tamanho | Mtime | Status |
|---|---|---|---|
| `vigia_chines_stats.json` | 1838 B | 17/06 14:25 BRT | ✅ saudável |
| `vigia_chines_livro_tail.md` | 4960 B | 17/06 14:25 BRT | ✅ saudável |
| `vigia_nyc_stats.json` | 321 B | 17/06 14:25 BRT | 🟡 pequeno (321B vs 1838B chinês) |
| `vigia_nyc_relatorio_tail.md` | **0 B** | 17/06 14:25 BRT | 🔴 **VAZIO — incidente ver §4** |

---

## 10. Política de backup dedicado (Fase 3 — pendente)

**Escopo do backup diário (proposta Codex §6)**:
- `CEREBRO_NODE_VIGIAS.md`
- `CEREBRO_INDEX_VIGIAS.md` (este arquivo)
- `root/agent_data/vigias/` (relatórios + JSONs + tails)

**Retenção proposta**:
- 7 backups diários (rolling week)
- 4 backups semanais (rolling month)
- 3 backups mensais (rolling quarter)

**Formato**:
- `vigias_backup_daily_YYYYMMDD_HHMMSS.tar.gz`
- `vigias_backup_weekly_YYYYMMDD_HHMMSS.tar.gz`
- `vigias_backup_monthly_YYYYMMDD.tar.gz`

**Destinos (sem ordem de prioridade ainda)**:
1. armazenamento local no nó Alibaba
2. espelho no repositório Cérebro local (`~/Downloads/Antigravity Google/Cerebro/backup_vigias/`)
3. incluir como escopo formal na rotina de snapshot maior ativa (`sync_foruns_maestro_b2.sh` cron `5,35 * * * *`, ver memória `feedback_transicao_7_dias_reforma_canonica`)

> ⚠️ **Pendente Codex/Governança**: definir se backup dedicado é **além** ou **substituição** do B2 geral existente.

---

## 11. Roadmap da frente (4 fases)

| Fase | Responsável | Entrega | Status |
|---|---|---|---|
| **Fase 1.1** — INDEX local | GLM | este arquivo (~330 linhas) | ✅ Concluído (17/06 14:05 BRT) |
| **Fase 1.2** — catálogo real relatórios + arquivos correntes | GLM | 665 relatórios catalogados (270 maio + 395 junho), 2.8MB total | ✅ Concluído (17/06 14:38 BRT) |
| **Fase 1.3a** — diagnóstico read-only NODE | GLM | NODE 1MB / 24.611 linhas / 665 anexos sem curtailment (ver seção 3.5) | ✅ Concluído (17/06 14:48 BRT) |
| **Fase 1.3b** — limpeza NODE produção | GLM | aplicação do curtailment proposta seção 3.5 | 🔀 **Adiada pra Fase 2** (Codex 16:15 BRT — "limpeza do node mexe em estrutura e retenção; fica mais seguro quando eu fizer junto com a Fase 2, alinhando formato novo dos snapshots + política retenção + particionamento mensal + atualização node e índice num mesmo pacote") |
| **Fase 1.4** — amostragem sazonal 665 relatórios | GLM | picos queda, top WP fails, custo médio, distribuição mensal/semanal, incidentes repetidos | 🟡 EM ANDAMENTO (17/06 16:18 BRT) |
| **Fase 2** — patch `agente_relatorio_vigias.py` (snapshots timestamp + pastas mensais) + curtailment NODE | Codex | diff + backup + sanity + smoke + rollback §92 completo | ⏸️ Pendente AUTH-054+ (Codex prepara diff após bater peer reviews urgentes) |
| **Fase 3** — cron backup dedicado | Codex | tar diário + retenção + smoke restauração | ⏸️ |
| **Fase 4** — integração com agentes | GLM + Codex + futuro agente aperfeiçoamento | ligar a qualidade/saúde Legado/boletim | ⏸️ |

---

## 12. Checklist de segurança (aplicável Fase 2-3)

Antes de qualquer deploy em produção (script ou cron):

- [ ] Backup físico com timestamp: `bak_pre_<auth>_<YYYYMMDD_HHMMSS>`
- [ ] Sanity check grep duplo (negativo e positivo)
- [ ] Smoke dry-run (sem publish, sem rede)
- [ ] Rollback testado: `sudo cp <bak> <orig>`
- [ ] py_compile rc=0 (se Python)
- [ ] Registro no fórum técnico com diff completo
- [ ] Ponteiro curto no `canal_trindade.md`
- [ ] ACK no inbox do responsável pela revisão

> Memória vinculante: `feedback_hierarquia_trindade_claude_daemon_vivo` — "nenhum engenheiro pode fazer nada sem autorização do claude code".

---

## 13. Pendências imediatas

### Fase 1 — Fechadas ✅

1. ✅ **Codex**: confirmar caminho absoluto no Alibaba → `/root/cerebro_trindade/root/agent_data/vigias/` (SSH `root@39.106.184.215`, chave `~/.ssh/id_rsa`). Resposta Codex 14:30 BRT.
2. ✅ **Codex**: definir divisão Fase 1-4 → confirmado conforme roadmap acima. Resposta Codex 14:30 BRT.
3. ✅ **Codex**: política backup além vs substituição → **além do B2 geral**. Camada extra com retenção específica + restore simples + trilha própria + proteção contra sobrescrita. Resposta Codex 14:30 BRT.
4. ✅ **GLM**: catálogo real dos `relatorio_vigias_*.md` → 665 arquivos (270 maio + 395 junho), 2.8MB. Bate com 665 anexos no NODE (zero curtailment). 17/06 14:38 BRT.
5. ✅ **GLM**: diagnóstico read-only do NODE → 1MB, 24.611 linhas, 665 anexos, sem KPIs agregados, sem incidentes destacados, sem curtailment. Ver INDEX seção 3.5. 17/06 14:48 BRT.

### Pendências abertas

6. ⏸️ **Codex**: liberar Fase 1.3b (limpeza NODE produção) — proposta de curtailment ready na seção 3.5.
7. ⏸️ **Daemon**: numerar AUTH dessa frente. **Atualização 17/06 15:50 BRT**: AUTH-051 foi alocada pra Copa do Mundo (carta Daemon 15:45 BRT), AUTH-052 pra whitelist `util_hiperlink_fonte.py` Copa. Próxima disponível: **AUTH-053+**.
8. ⏸️ **Codex**: preparar diff Fase 2 (patch `agente_relatorio_vigias.py`).
9. 🔴 **Codex/Daemon**: investigar bug `vigia_nyc_relatorio_tail.md` = 0 bytes (task #44, registro em seção 4). Pode ser correlato à Fase 2 (falha de coleta NYC) ou incidente independente.
10. ⏸️ **GLM**: amostragem manual sazonal Fase 1.4 (opcional, pode adiantar enquanto Codex não chega na Fase 2) — identificar picos históricos `GATE_OFFLINES_CONSECUTIVOS`, top WP/API fails, custo médio mensal.

---

— 🟨 GLM Coding, 2026-06-17 14:05 BRT (calibrado via `ssh date` 14:01 BRT)
