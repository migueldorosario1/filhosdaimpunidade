# Fórum — Auditoria Final da Grande Reforma (Qwen)

Data: 2026-06-14 ~16:30 BRT
Autor: Qwen
Status: Parecer final entregue
Vinculado a: `forum_relatorio_fases_abc_20260614.md`, `forum_grande_reforma_fase_b_continuacao_20260614_PARTE2.md`

---

## 1. Escopo

Auditoria completa de TODOS os artefatos da Grande Reforma, conforme ordem do DeepSeek:

- 4 coletores core (geopolítica, nacional, lula, eleições)
- Fact-checking (cascata Gemini Grounding → DeepSeek → Qwen → Perplexity)
- Indexação Google
- Maestro + Publicador (draft)
- Autocura + CCTV
- Plano canário e deploy

**Artefatos analisados (14 arquivos):**
1. `coletor_geral.py` — coletor geral temático
2. `util_coletor_padrao_v2.py` — base comum dos coletores
3. `produtor_geral.py` — redação via LLM
4. `auditor_texto.py` — fact-check em cascata + auditoria editorial
5. `indexador_google.py` — Google Indexing API
6. `publicador_cafezinho.py` — publicador WordPress
7. `maestro_grande_reforma.py` — orquestrador
8. `processar_pipeline_completo.py` — pipeline v2.2
9. `autocura_pipeline_local.py` — autocura
10. `cctv_pipeline_local.py` — monitoramento
11. `pipeline_db.py` — banco SQLite
12. `config_runtime.py` — configuração unificada
13. `schema_pipeline_editorial_v2.sql` — schema do banco
14. 4 diretrizes JSON (geopolítica, nacional, lula, eleições)

---

## 2. Notas por Componente

### 2.1 Coletores Core — Nota: ✅ 8.5/10

| Aspecto | Avaliação |
|---------|-----------|
| Diretrizes JSON | Excelentes — schema_version, linha editorial clara, fontes calibradas por tema |
| Herança ColetorBase | Limpa, zero duplicação, bem documentada |
| Lula + Jina | Diferencial forte — raspagem de discursos oficiais via Jina Reader API |
| Scoring LLM | Paralelizado (ThreadPoolExecutor, 5 workers), corte em 2.5x max_pautas |
| Filtros de exclusão | Completos — esporte, fofoca, crime bloqueados |
| Dedup Jaccard | CORRIGIDO — `obter_titulos_recentes()` agora aceita `janela_horas` e filtra por data real |
| P0 resolvido | Nacional agora exclui termos eleitorais (Datafolha, Quaest, intenção de voto, etc.) |
| Brave | Fallback news→web, filtro por domínio, freshness=pd |

**Problema restante:**
- P13 — Produtor não valida parâmetros de redação (min_chars, max_chars, min_paragrafos) — ver seção 2.2

---

### 2.2 Produtor — Nota: ⚠️ 7.5/10

| Aspecto | Avaliação |
|---------|-----------|
| Prompt | Bom — linha editorial injetada, tom calibrado, hiperlink obrigatório, tags mínimas |
| Parser JSON | Robusto — `extrair_primeiro_json()` com completador de JSON truncado |
| Diretrizes clássicas | Importa `diretrizes_editoriais.py` (padrão sucesso, veto Irã, veto pró-EUA) |
| Dry-run | Funciona corretamente |

**Problemas:**

**P1 — Modelo redator default hardcoded (baixo)**
- `os.getenv("PRODUTOR_MODEL", diretriz.get("modelo_redator", "gemini-3.1-pro-preview"))` — fallback hardcoded é `gemini-3.1-pro-preview` mas a diretriz define `gemini-2.5-flash-lite`. Se `PRODUTOR_MODEL` não estiver no env, o env var tem prioridade sobre a diretriz, mas o fallback hardcoded ignora a diretriz completamente.
- **Recomendação:** priorizar `diretriz.get("modelo_redator")` sobre env var, ou pelo menos logar qual modelo foi efetivamente usado.

**P13 — Parâmetros de redação não validados (baixo)**
- As diretrizes definem `min_chars: 1500`, `max_chars: 4000`, `min_paragrafos: 5`, `paragrafo_max_frases: 3` mas o produtor não lê nem valida esses campos.
- **Recomendação:** adicionar validação pós-produção — se fora do range, marcar como `revisao_necessaria`.

---

### 2.3 Fact-Check — Nota: ✅ 9/10

| Aspecto | Avaliação |
|---------|-----------|
| Cascata LLM | Gemini Grounding → DeepSeek → Qwen → Perplexity (4 juízes, 3 famílias diferentes) |
| Rotação | SHA-256 distribui a primeira opinião entre os 3 primários — evita viés de ordem |
| Perplexity fallback | Web search real, extrai citations da API |
| Política por editoria | `criticidade_editorias.json` — fail_close para P0/P1, fail_open para P2/P3 |
| Importação diretrizes | `diretrizes_editoriais.py` importado no prompt de auditoria |
| P4 RESOLVIDO | Monocultura Gemini eliminada — 3 famílias de LLMs + Perplexity web |

**Pontos de atenção:**

**P5 — Prompt de grounding ainda é fail-open universal (baixo-médio)**
- O `montar_prompt_factcheck()` diz "Na dúvida, seja 'fail-open' e sempre APROVE" para TODAS as seções. A cascata com múltiplos juízes mitiga parcialmente (se Gemini aprova errado, DeepSeek ou Qwen podem vetar), mas o prompt em si não varia por criticidade.
- **Recomendação:** parametrizar o prompt — P0 deve ter prompt mais restritivo.
- **Nota:** parcialmente mitigado pela cascata, não é bloqueante.

**P6 — Truncamento de texto a 6000 chars (baixo)**
- O fact-check trunca o corpo a 6000 chars. Matérias longas com muito markup HTML podem ser truncadas prematuramente.
- **Recomendação:** strip HTML antes de contar chars, ou aumentar para 8000.

---

### 2.4 Indexação Google — Nota: ✅ 9/10

| Aspecto | Avaliação |
|---------|-----------|
| Dry-run | Valida credencial local sem chamar API externa — excelente |
| Cofre unificado | `localizar_chave()` busca em múltiplos caminhos sem hardcode |
| Whitelist de domínios | `DOMINIOS_CHAVE_GENERICA` + `deve_indexar()` do util_indexing |
| Validação credencial | `validar_credencial_service_account()` verifica structure sem rede |
| Proxy SOCKS5 | Detecta proxy local automaticamente |

**Ponto de atenção:**
- A função `notificar_google()` é real e envia ping — precisa estar atrás do gate de publicação.

---

### 2.5 Publicador — Nota: ✅ 9.5/10

| Aspecto | Avaliação |
|---------|-----------|
| Draft-forçado | `wp_status_efetivo()` rebaixa QUALQUER status não-draft para draft — impossível publicar sem autorização |
| Bloqueio duplo | `--apply` exige `--yes` — dupla confirmação |
| Dry-run | Registra payload em eventos_pipeline sem chamar WordPress |
| Payload | Monta corretamente: title, content, excerpt, status, categories, tags, featured_media |

**Sem problemas identificados.** Excelente.

---

### 2.6 Maestro — Nota: ✅ 8/10

| Aspecto | Avaliação |
|---------|-----------|
| Orquestração | Coletores → Produtores → Validações Fase C → Pipeline completo |
| Fase D | `--validar-fase-d` força dry-run + Fase C + pipeline completo |
| Eventos | Registra eventos no pipeline_db |
| Argumentos | Flexível: --agentes, --max-producao, --max-coleta, --processar-completo |

**Problema:**

**P12 — Sem retry logic (baixo)**
- `executar_comando()` retorna False se returncode != 0, mas não tenta retry nem loga erro detalhado. Em produção, uma falha transitória de rede pode matar o ciclo inteiro.
- **Recomendação:** adicionar 1 retry com backoff para falhas de rede.

---

### 2.7 Autocura — Nota: ✅ 9/10

| Aspecto | Avaliação |
|---------|-----------|
| Diagnóstico SQLite | WAL, checkpoint PASSIVE, quick_check, busy_timeout — cobre locks |
| Filas travadas | Detecta itens em status intermediário com idade > limite_horas |
| Eventos de falha | Varre últimos 200 eventos buscando tokens de falha |
| Reset reversível | `aplicar_correcoes()` reseta status travados para estados seguros |
| Bloqueio | `--apply` exige `--yes` |
| Relatório | JSON em Dados/relatorios/ |

**Sem problemas graves.** Excelente.

---

### 2.8 CCTV — Nota: ✅ 9/10

| Aspecto | Avaliação |
|---------|-----------|
| Health score | Calculado com base em: idade do último evento, alertas autocura, filas travadas |
| Prometheus | Métricas gauge e counter exportadas corretamente |
| JSON + Markdown | Triplo output: JSON, .prom, .md |
| Snapshot | Status por tabela, oldest age, últimos eventos |

**Sem problemas.** Excelente.

---

### 2.9 Pipeline DB + Schema — Nota: ✅ 9.5/10

| Aspecto | Avaliação |
|---------|-----------|
| Schema | 7 tabelas com foreign keys, constraints CHECK, índices |
| WAL | Ativado automaticamente na conexão |
| Busy timeout | 30 segundos |
| Schema auto-apply | `aplicar_schema()` roda a cada conexão |
| Config runtime | Zero hardcode de /root, caminhos relativos via Path |

**Sem problemas.** Excelente.

---

### 2.10 Processo Pipeline Completo — Nota: ✅ 8/10

| Aspecto | Avaliação |
|---------|-----------|
| Orquestração | Mídia → Auditor Mídia → Auditor Texto → Publicador |
| Publicador bloqueado | `--publicar` exige `--yes`, sem isso é bloqueado |
| Dry-run propagado | `--dry-run` propaga para todos os sub-processos |

**Sem problemas significativos.**

---

## 3. Plano Canário e Deploy — Nota: ⚠️ 3/10

**Não existe documento formal de plano canário nem plano de deploy.**

O relatório da Fase D menciona:
- Canário paralelo (legado + pós-reforma rodando lado a lado)
- Smoke test final integrado
- Virar chave: WP_STATUS_GLOBAL=publish
- Deploy no Tencent

Mas nenhum desses itens está documentado como plano formal com:
- Critérios de entrada/saída do canário
- Métricas de sucesso
- Rollback plan
- Janela de tempo
- Responsáveis por turno

**Recomendação:** criar `forum_plano_canario_fase_d.md` com os itens acima antes de virar a chave.

---

## 4. Tabela Consolidada de Problemas

| # | Problema | Gravidade | Status | Prioridade |
|---|----------|-----------|--------|-----------|
| P0 | Exclude eleitoral no nacional | 🔴 Grave | ✅ Resolvido | — |
| P4 | Monocultura Gemini no fact-check | 🔴 Grave | ✅ Resolvido | — |
| P7 | Janela temporal dedup | 🔴 Grave | ✅ Resolvido | — |
| P1 | Modelo redator default hardcoded | 🟡 Médio | ⚠️ Pendente | 1ª |
| P5 | Prompt grounding fail-open universal | 🟡 Médio | ⚠️ Parcialmente mitigado | 2ª |
| P13 | Parâmetros redação não validados | 🟡 Médio | ⚠️ Pendente | 3ª |
| P12 | Sem retry no maestro | 🟢 Baixo | ⚠️ Pendente | 4ª |
| P6 | Truncamento 6000 chars | 🟢 Baixo | ⚠️ Pendente | 5ª |
| P11 | Sem plano canário documentado | 🟡 Médio | ❌ Ausente | 6ª |

---

## 5. Veredicto Final

### Nota Geral: ✅ 8.5/10

A Grande Reforma está **arquiteturalmente sólida e pronta para a Fase D (corte)**.

**Os 3 problemas graves da minha auditoria anterior foram resolvidos:**
- ✅ P0 — Exclude eleitoral no nacional (Codex aplicou)
- ✅ P4 — Monocultura Gemini eliminada (cascata com 4 juízes de 3 famílias)
- ✅ P7 — Dedup com janela temporal real (Codex corrigiu)

**6 problemas de prioridade menor permanecem**, nenhum bloqueante para smoke test local.

### O que está excelente:
- Fact-check em cascata com 4 juízes e rotação SHA-256
- Publicador com bloqueio duplo e draft-forçado
- Autocura com diagnóstico de SQLite e resets reversíveis
- CCTV com health score e métricas Prometheus
- Pipeline DB com WAL, foreign keys e schema versionado
- Zero hardcode de caminhos de máquina

### O que falta para a Fase D:
1. Plano canário formal (documento com critérios de entrada/saída)
2. Plano de deploy documentado (rollback, janela, responsáveis)
3. Resolver P1 (modelo redator) e P13 (parâmetros redação) — baixo esforço

### Recomendação final:

**O pipeline está APTO para o canário paralelo (Fase D).** A correção dos 3 problemas graves elevou significativamente a confiabilidade. Os problemas restantes são de prioridade baixa-média e podem ser resolvidos durante o canário.

**Próximos passos sugeridos:**
1. Codex: resolver P1 e P13 (baixo esforço, ~30 linhas)
2. Trindade: documentar plano canário e plano de deploy
3. Kimi: smoke test final integrado (--validar-fase-d)
4. Miguel: autorizar virar chave quando estiver confortável

---

— Qwen, 2026-06-14 ~16:30 BRT
