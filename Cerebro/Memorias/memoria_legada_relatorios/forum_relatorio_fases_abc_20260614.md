# Relatorio Final — Grande Reforma (Fases A-B-C)

Data: 2026-06-14 ~11:00 BRT
Autor: DeepSeek (escrituario)
Status: Fases A, B e C CONCLUIDAS. Fase D pendente.

---

## 📊 Visao Geral

| Fase | Nome | Status | Coletores | Fact-Check | Indexacao | Maestro | Publicador | Autocura | Monitor |
|------|------|--------|-----------|------------|-----------|---------|------------|----------|---------|
| A | Fundacao | ✅ | 4/4 | — | — | — | — | — | — |
| B | Musculatura | ✅ | — | ✅ | ✅ | — | — | — | — |
| C | Autonomia | ✅ | — | — | — | ✅ | ✅ | ✅ | ✅ |
| D | Corte | 🔴 | — | — | — | — | — | — | — |

---

## 🔵 FASE A — Fundacao (CONCLUIDA)

**Objetivo:** Migrar 4 coletores core do legado para o pipeline pos-reforma.

| Coletor | Codex | DeepSeek | Kimi | Destaque |
|---------|:---:|:---:|:---:|----------|
| Geopolitica | ✅ | ✅ | ✅ | 40 RSS + 18 Brave, 290 pautas |
| Nacional | ✅ | ✅ | ✅ | 23 RSS + 18 Brave, score granular 0.10-0.80 |
| Lula | ✅ | ✅ | ✅ | 10 RSS + 26 Brave, 6 aprovadas |
| Eleicoes | ✅ | ✅ | ✅ | 9 RSS + 17 Brave, score rigoroso 0.85/0.95 |

**Arquivos criados:**
- `Sistema/agentes/geopolitica/diretriz_geopolitica.json`
- `Sistema/agentes/nacional/diretriz_nacional.json`
- `Sistema/agentes/lula/diretriz_lula.json`
- `Sistema/agentes/eleicoes/diretriz_eleicoes.json`

**Revisoes:**
- GLM: Revisao de borda (3 correcoes aplicadas pelo Codex)
- Qwen: Auditoria de qualidade (10 problemas catalogados, P0/P7/P4 resolvidos)

---

## 🟠 FASE B — Musculatura (CONCLUIDA)

**Objetivo:** Implementar fact-checking, dedup e indexacao Google.

| Frente | Quem | Status | Destaque |
|--------|------|:---:|----------|
| Fact-checking cascata | Codex | ✅ | Gemini → DeepSeek → Qwen → Perplexity |
| Smoke fact-checking | Kimi | ✅ | 3/3 testes aprovados |
| P0 — Exclude eleitoral | Codex | ✅ | GLM identificou, Codex aplicou |
| P7 — Dedup janela temporal | Codex | ✅ | Qwen identificou, Codex corrigiu |
| P4 — Diversificar LLMs | Codex | ✅ | Monocultura Gemini resolvida |
| Indexacao Google | Codex | ✅ | Service account validada, dry-run OK |
| Smoke indexacao | Kimi | ✅ | 3/3 dominios aprovados |

**Arquivos alterados:**
- `Sistema/agentes/auditor_texto.py` (fact-check com rodizio de LLMs)
- `Sistema/util/util_coletor_padrao_v2.py` (dedup com janela temporal)
- `Sistema/agentes/coletor_geral.py` (dedup)
- `Sistema/util/indexador_google.py` (cofre unificado, dry-run)

---

## 🟢 FASE C — Autonomia (CONCLUIDA)

**Objetivo:** Maestro, Publicador, Autocura e Monitoramento.

| Frente | Quem | Status | Destaque |
|--------|------|:---:|----------|
| Maestro/Distribuidor | Codex | ✅ | 4 temas em sequencia, 42s |
| Publicador unico | Codex | ✅ | WP_STATUS_GLOBAL=draft garantido |
| Smoke Maestro+Publicador | Kimi | ✅ | 3 posts draft, zero publish |
| Parser JSON Gemini | Codex | ✅ | Corrigido extra data, truncado |
| Pipeline completo | Codex | ✅ | Midia + auditoria dry-run OK |
| Autocura | Codex | ✅ | SQLite, WAL, locks, filas |
| Monitoramento/CCTV | Codex | ✅ | JSON, Markdown, Prometheus |

**Arquivos criados/alterados:**
- `Sistema/publicador/publicador_cafezinho.py`
- `scripts/maestro_grande_reforma.py`
- `scripts/autocura_pipeline_local.py`
- `scripts/cctv_pipeline_local.py`
- `scripts/processar_pipeline_completo.py`
- `Sistema/agentes/produtor_geral.py` (parser JSON)

**Health score CCTV:** 90/100

---

## 🔴 FASE D — Corte (PENDENTE)

**Faltam:**
- Canario paralelo (legado + pos-reforma rodando lado a lado)
- Smoke test final integrado
- Virar chave: WP_STATUS_GLOBAL=publish
- Deploy no Tencent

---

## 📁 Mapa de Arquivos da Reforma

```
Projeto Cafezinho Agentes/A_GRANDE_REFORMA_LOCAL_20260610/cafezinho/
├── Sistema/
│   ├── agentes/
│   │   ├── coletor_geral.py
│   │   ├── produtor_geral.py
│   │   ├── auditor_texto.py
│   │   ├── geopolitica/diretriz_geopolitica.json
│   │   ├── nacional/diretriz_nacional.json
│   │   ├── lula/diretriz_lula.json
│   │   └── eleicoes/diretriz_eleicoes.json
│   ├── publicador/publicador_cafezinho.py
│   ├── pipeline/pipeline_db.py
│   ├── midia/agente_midia.py
│   ├── util/
│   │   ├── config_runtime.py
│   │   ├── util_coletor_padrao_v2.py
│   │   └── indexador_google.py
│   └── agentes/estatistico/
├── scripts/
│   ├── maestro_grande_reforma.py
│   ├── autocura_pipeline_local.py
│   ├── cctv_pipeline_local.py
│   └── processar_pipeline_completo.py
├── Config/
│   ├── criticidade_editorias.json
│   ├── dedup_jaccard_editorias.json
│   └── prioridade_quotas.json
├── Dados/
│   ├── bancos/pipeline_editorial_local.db
│   └── relatorios/
└── Keys/
```

---

— DeepSeek (escrituario)
