# Fórum — Sprint V3 Reforma Pipeline Fase-por-Fase (23/06/2026)

**Engenheiro responsável:** Claude Code (Daemon)
**Data:** 23/06/2026 (em andamento)
**Sancionador:** Miguel
**Status:** EM ANDAMENTO — fase TESE concluída, fase BRUTAS_PLUS em análise

---

## 1. CONTEXTO DA SPRINT

Miguel disparou uma reforma editorial profunda do Cafezinho após acumular evidências de problemas em série no V3 política (pipeline novo Codex+Kilo):

- Vazamento de meta-discurso ("a informação original serve de base para esta apuração")
- Fotos completamente incoerentes com a matéria (post #260466)
- Prolixidade excessiva
- Pautas chapa-branca (cerimoniais, premiações) passando pela curadoria
- Repetição de tema entre publicações
- Anacronismo (matérias antigas como atuais)
- Siglas técnicas em títulos
- Heurística determinística aprovando 27 brutas chapa-branca por dia (curador LLM nunca ativava por bug de cron)

Estratégia adotada: **pausar agentes-problema, reformar V3, auditar fase por fase com Miguel**.

---

## 2. PAUSAS DE PIPELINES (FASE 1)

Agentes pausados ao longo da sessão (substituídos por silêncio ou reduzidos a peso mínimo no maestro):

| Agente | Motivo |
|---|---|
| `agente_reciclador` | Chapa-branca, baixa qualidade |
| `agente_geopolitica_legado` | Substituído pelo V3 geopolítica |
| `agente_inflacao` / `agente_mercado` / `agente_matriz` | Pausados (estavam na lista de pausados anterior, confirmados) |
| `agente_analytics` | Não gerava editorial real |
| `agente_fantastico` | Pausado a pedido |
| `agente_flavio` (Bolsonaro) | Pausado |
| `agente_militar` | Pausado |
| `agente_eleicoes` | Pausado |
| `agente_coletor_social` | Peso reduzido (usado por outros) |
| `agente_coletor_geopolitica` | Pausado (parte da pausa geopolítica legada) |

**Maestro hoje (peso somado 38, antes 113):** soberania 15, china 12, lula 6, ia 3, repetidor 2.

Códigos legados removidos do ambiente de produção e movidos para `legacy/` (indexados no cérebro, NÃO apagados — backup completo preservado).

---

## 3. REFORMA ARQUITETURAL V3

### 3.1 Reset de bancos

Bancos V3 zerados a pedido do Miguel ("pode esvaziar os bancos do v3 e começar de novo"). Reset cobriu:
- `banco_noticias_brutas_politica_v3.db`
- `banco_teses_politica_v3.db`
- `banco_brutas_plus_politica_v3.db`
- `banco_acabamento_seo_politica_v3.db`
- `banco_telemetria_politica_v3.db`

### 3.2 Decisão de LLMs por etapa (Miguel)

Miguel pediu DeepSeek na opção A (curador da coleta). Após várias rodadas, mapa final:

| Fase | LLM | Contexto roteador |
|---|---|---|
| Curador coleta | DeepSeek (1ª), OpenAI, Sonnet | `producao_v3` (cascata) |
| **Tese** | **DeepSeek (1ª)**, OpenAI, Sonnet | `producao_v3` (herda) |
| Produção | DeepSeek (1ª), OpenAI, Sonnet | `producao_v3` |
| Revisão | Sonnet (1ª), OpenAI, DeepSeek | `revisao_v3` |
| Editor final | OpenAI (1ª), Qwen, Sonnet | `editor_final_v3` |

Novos contextos adicionados em `/root/agente_roteador_llm.py` (`_DEFAULT_LLM_ROUTES["contexts"]`):
- `producao_v3: [deepseek_luxo, openai_luxo, anthropic_luxo]`
- `revisao_v3: [anthropic_luxo, openai_luxo, deepseek_luxo]`
- `editor_final_v3: [openai_luxo, alibaba_luxo, anthropic_luxo]`

Variáveis em `/root/.env.unificado`:
- `POLITICA_V3_ALLOW_COLETA_LLM=1`
- `POLITICA_V3_LLM_CONTEXTO=producao_v3` (afeta tese E produção — comum)
- `POLITICA_V3_REVISAO_CONTEXTO=revisao_v3`
- `POLITICA_V3_EDITOR_FINAL_CONTEXTO=editor_final_v3`

Cron de coleta foi patcheada pra carregar `.env.unificado` (antes não carregava — bug que mantinha o curador LLM desativado e deixava heurística aprovar tudo).

### 3.3 Anti-repetição via observatório

Criado **`/root/agente_observatorio_publicacoes.py`** (273 linhas, SQLite `/root/agent_data/banco_observatorio_publicacoes.db`):

Funções públicas:
- `ultimos_titulos(n=50)` — últimos N títulos publicados no WP
- `ja_publiquei_tema(titulo, threshold=0.45)` — checa similaridade
- `temas_saturados(janela_h=24, top_n=8)` — tokens mais usados
- `fontes_mais_usadas(janela_h=24)` — top agentes

Cron `*/30 * * * *` mantém atualizado. Retenção 7 dias.

---

## 4. FASE COLETA — REFATORADA E DEPLOYADA

### 4.1 Trafilatura movida pra DEPOIS do scoring
Antes: trafilatura rodava em TODAS as 60-120 candidatas (3s × N = 3-6min).
Depois: roda só nas 10-25 aprovadas (~30-75s). Economia 80% tempo.

### 4.2 Curador editorial LLM com BATCH ÚNICO

Estratégia anterior: 1 chamada LLM por candidata (60 chamadas, 621s).
**Teste empírico Miguel solicitou:**

| Estratégia | Tempo | Chamadas | Anti-repetição interna |
|---|---|---|---|
| 1×60 separadas | 621s | 60 | 9/10 redundantes ERRONEAMENTE aprovadas |
| **BATCH ÚNICO 60** | **62s** | **1** | **1/10 (CORRETO)** |
| 2 batches de 30 | 117s | 2 | 1/10 (igual ao único) |

**Vencedor: batch único.** LLM detecta repetição entre as próprias candidatas naturalmente quando vê todas juntas.

Deploy: `_score_batch_llm` em `/root/V3/agente_coletor_fontes_v3.py` substituído por 1 chamada com TODAS as candidatas + 50 últimos publicados no contexto. `max_tokens=4500`.

### 4.3 Bloqueio sem-LLM

Patch: se curador LLM falhar, candidata recebe `curador_bloqueada=True` em vez de cair pra heurística. Anti-chapa-branca.

### 4.4 Backups
- `agente_coletor_fontes_v3.py.bak_pre_batch_unico_20260623_2320`

---

## 5. FASE TESE — REFATORADA E DEPLOYADA

### 5.1 Mapa pré-reforma (auditoria conjunta com Miguel)

| Item | Estado anterior |
|---|---|
| LLM | DeepSeek (herdado de `producao_v3`, sem decisão consciente) |
| Texto bruto enviado | 500 chars (curto) |
| Linha editorial Cafezinho | AUSENTE — prompt dizia só "editor editorial Política V3" |
| Observatório 50 últimos | AUSENTE |
| Confronto/herói/vilão | AUSENTE |
| Anti-meta-discurso | ✅ já tinha |
| Idempotência | ✅ já tinha |

### 5.2 Patch v2 deployado

**Arquivo:** `/root/V3/v3_agente_tese.py`
**Backup:** `v3_agente_tese.py.bak_pre_v2_20260623_HHMMSS`

Mudanças:
- `PROMPT_INVENTORY` ganhou versão `agente_tese_v2` (v1 preservado)
- `prompt_version = "agente_tese_v2"`
- Linha editorial Cafezinho completa: esquerda independente, anti-imperialista, pró-Lula com elegância (sem clichê militante), pró-Sul Global, anti-bolsonarismo, anti-Centrão, crítica à mídia corporativa
- **Obrigação explícita:** identificar `confronto_central`, `heroi`, `vilao` (3 campos novos no JSON output)
- Bloco observatório injetado com 50 últimos publicados + instrução pra marcar `tese_insustentavel` se repete
- Texto bruto: 500 → **1000 chars**
- DeepSeek mantido

Smoke `.format()` PASS (4585 chars). Observatório importável PASS.

### 5.3 Pendência

Schema `brutas_com_tese` não tem ainda colunas `confronto_central`, `heroi`, `vilao`. Hoje LLM gera os 3 campos mas o INSERT descarta (LLM ainda usa pra raciocinar melhor mesmo sem persistir). Pendente: decidir se faz ALTER TABLE + propagar pros consumidores (produção/auditoria).

---

## 6. PATCHES DE FASES POSTERIORES (já feitos antes desta sessão fase-por-fase)

### 6.1 Fase MÍDIA — 5 patches em `/root/V3/executar_midia_v3_real.py`
1. `og:image` como topo da cascata (`montar_preflight` ~L1607)
2. Flickr live plugado (L1622)
3. Tribunal Visual no fallback institucional R2
4. Busca textual ampla no legado com tokens contextuais
5. Banir fallback cego (se Tribunal reprova → pending, não publica)

Apoio: criado `/root/V3/util_og_image_v3.py` (parser regex og:image).

### 6.2 Fase AUDITORIA FINAL — `/root/V3/executar_auditoria_final_v3_real.py`
- Anti-meta-discurso B-029 (cure + reaudit, bloqueia só se persistir após cura)
- Função NOVA `revisar_via_llm_v3()` (Sonnet via contexto `revisao_v3`) chamada após `validar_final()` enriquece `revisao_json`

### 6.3 Fase EDITOR FINAL — `/root/V3/v3_editor_final.py`
- `inserir_atribuicao_fonte()` patchada Opção A
- Antes: parágrafo robótico no INÍCIO ("Segundo a X, a informação original serve de base...")
- Depois: rodapé "Com informações de [link]" no FINAL

Apoio: criado `/root/V3/util_anti_meta_discurso_v3.py` (13 padrões regex).

---

## 7. BUGS IDENTIFICADOS E STATUS

| Bug | Descrição | Status |
|---|---|---|
| **B-029** | Vazamento meta-discurso V3 (parágrafo "informação original serve de base") | ✅ RESOLVIDO (editor_final + auditoria) |
| **B-030** | Foto incoerente V3 (sem og:image, sem flickr live, busca strict, fallback cego) | ✅ RESOLVIDO (5 patches fase mídia) |
| Cron sem `.env.unificado` | Curador LLM nunca ativava, heurística aprovava chapa-branca | ✅ RESOLVIDO |
| Anti-repetição interna não funcionava no scoring 1×1 | Batch único provou ser solução | ✅ RESOLVIDO (deploy batch único) |
| Schema `brutas_com_tese` sem confronto/heroi/vilao | Patch v2 gera mas não persiste | ⚠️ PENDENTE — decisão Miguel |
| Threshold curador 5.2 vs 6.0 | Hoje 5.2 — possivelmente baixo demais | ⚠️ PENDENTE |
| Hard-no-home agente_soberania | Miguel pediu mas não confirmou | ⚠️ PENDENTE |
| Fila Grande Reforma com 2 pautas órfãs | Aguarda limpeza | ⚠️ PENDENTE |

---

## 8. MAPA DAS 8 FASES DO PIPELINE V3 (atualizado 24/06 madrugada)

```
1. COLETA       → agente_coletor_fontes_v3.py            [✅ batch único curador]
2. TESE         → v3_agente_tese.py                      [✅ v2 Cafezinho + observatório]
3. BRUTAS_PLUS  → v3_brutas_plus.py                      [⏳ ainda determinístico/legado]
4. PRODUÇÃO     → v3_producao_editorial.py + redator_*   [✅ Cafezinho + confronto/heroi/vilao + observatório, cascata OpenAI/Sonnet/DeepSeek]
5. MÍDIA        → executar_midia_v3_real.py              [✅ 5 patches anteriores]
6. ACABAMENTO   → v3_acabamento_seo_taxonomia.py         [✅ 100% LLM-only (DeepSeek V4 Pro)]
7. AUDITORIA    → executar_auditoria_final_v3_real.py    [✅ revisor_unificado_v3 LLM substitui validar_final regex]
8. PUBLICADOR   → executar_publicador_wp_v3_pending.py   [✅ revisor_publicacao_v3 + legenda_midia LLM, Yoast LLM persistido]

POS-PUBLICACAO (NOVO):
9. RELATOR      → /root/agente_relator_publicacao_v3.py  [✅ relatório técnico+editorial + Prometheus]
```

Orquestrador: `/root/V3/executar_lote_publicacao_v3_real.py`
Cron: `20 1,5,9,13,17,21 * * *` (6×/dia, **PAUSADO desde 23:58 BRT 23/06**)

## 8.1 PAUSA DO V3 (23:58 BRT 23/06)

Após a auditoria da fase brutas_plus que revelou muitos problemas (sem linha editorial Cafezinho nos 2 prompts, ângulos genéricos hardcoded, sem observatório, fallback fontes corporativas livre), Miguel decidiu **pausar V3 inteiro** e zerar bancos pra recomeçar limpo.

**Pausados (3 crons V3):**
- Coleta política `0,30 * * * *`
- Pipeline produção `20 1,5,9,13,17,21 * * *`
- Publicador consume `0,30 * * * *`

**Mantidos (observabilidade):**
- `monitor_v3_vision_prometheus.py` (mudado de `*/15` pra `0 * * * *` em 24/06)
- `alerta_v3_vision_prometheus.py` (idem)
- `agente_relator_publicacao_v3.py --prometheus-only` (`*/5`, novo)

**Backup integral:** `/root/BACKUPS/v3_pause_20260623_235843.tar.gz`

**Bancos zerados (11):** brutas, teses, brutas_plus, produzidas, auditadas, midias_*, publicacao_ledger, telemetria, curas

**Preservados:** banco_catalogo_midia_r2_v3 (2MB), banco_antitroll_v3, banco_noticias_brutas_cultura_v3

---

## 9. DECISÕES EDITORIAIS TOMADAS NA SESSÃO

1. **Cooldown pesquisas eleitorais** — 24h por `(instituto, data_pesquisa)`; matéria sobre pesquisa cita SÓ o instituto, não o veículo intermediário
2. **Cooldown Revista Fórum** — máx 2 posts/dia, intervalo 60min
3. **Cap comentários proporcional à qualidade** — fórmula `tier_base × mult_qualidade × mult_engajamento × mult_manchete`, min 3 max 80 (variando, NÃO fixo em 12)
4. **Manchete usa cat 2403 (Redação) + plugin hello-highlight**, NÃO cat 5087
5. **YT V2 título nominal** (nome do guest, não host) + corpo mínimo 7 parágrafos
6. **YT V2 título nunca positivo pra Israel** — frame anti-Israel/neutro técnico
7. **Siglas técnicas em títulos proibidas** (exceto whitelist: ONU, STF, EUA, CBF, OTAN, BRICS, FBI, CIA, PT, PL...)
8. **§107 hard-floor home/no_home** aplicado
9. **§108 EC3 WebSearch obrigatório** em pelo menos uma camada pré-publicação
10. **§110 Gate anacronismo** sem LLM em motor_publicador (rebaixa pra draft)
11. **Daemon NÃO promove draft/pending** — só cura editorial em PUBLISH (restrição Miguel 22/06)
12. **Reports de publish SEMPRE com agente** — meta `_agente_origem` ou inferência por cats/author
13. **Linha editorial Cafezinho na tese:** confronto explícito, herói/vilão, anti-imperialismo elegante

---

## 10. ESTADO ATUAL (atualizado 24/06 01:30 BRT)

- **V3 pausado** desde 23:58 BRT 23/06
- Pipeline inteiro reformado pra **LLM-only** (zero regex de texto, zero heurística editorial)
- Bancos vazios, aguardando religar (cron descomentar quando Miguel quiser)
- Sistema de relatórios pós-publicação ativo via Prometheus

---

## 10.1 REFORMA INTEGRAL 24/06 — TODO PIPELINE V3 LLM-ONLY

### Mapa de cascatas LLM por fase (NOVO)

| Fase | Contexto roteador | Cascata real |
|---|---|---|
| Coleta (curador batch) | `producao_v3` | DeepSeek V4 Pro → GPT-4o → Sonnet |
| Tese | `producao_v3` | DeepSeek V4 Pro → GPT-4o → Sonnet |
| Brutas_plus | `editorial`+`fact_check` (legado) | DeepSeek → GPT → Sonnet + Perplexity/Sonar |
| **Produção** | **`producao_editorial_v3`** | **GPT-4o → Sonnet → DeepSeek** (Miguel pediu GPT primário) |
| Mídia | (Tribunal Visual existente) | Qwen-VL → Gemini Vision (cascata) |
| **Acabamento SEO** | **`acabamento_seo_v3`** | **DeepSeek V4 Pro → GPT → Sonnet** (Miguel pediu DeepSeek) |
| **Auditoria final** | **`auditoria_final_v3`** | **Sonnet → GPT → DeepSeek** (revisor crítico) |
| Editor final luxo | `editor_final_v3` | GPT → Alibaba → Sonnet (correção pontual) |
| **Publicador (revisor)** | **`publicador_v3`** | **GPT-econ → DeepSeek-econ → Alibaba → Sonnet-econ** (leve, classificação) |
| **Relator pós-publish** | **`relator_v3`** | **Sonnet → GPT → DeepSeek** (narrativa crítica) |

### O que foi REMOVIDO nessa madrugada

**Da fase ACABAMENTO SEO** (`v3_acabamento_seo_taxonomia.py`):
- `_REGRAS_FORTES` (45 regex hardcoded Lula/Bolsonaro/Hubble/etc)
- `_CONTRAINDICACOES_LLM`
- `_FALLBACK_SEMANTICO`
- `SUB_TEMA_TO_CATEGORIA`
- `classificar_categoria_rigida`, `_llm_contraindicado`
- `resolver_tags`, `resolver_tags_fallback`
- `detectar_meta_discurso`, `limpar_meta_discurso`
- `encurtar_titulo_editorial`, `validar_titulo`
- `encurtar_yoast_title`, `validar_payload_yoast`
- Linhas: **670 → 400** (-40%, depois 400 com revisor LLM completo)

**Da fase AUDITORIA FINAL** (`executar_auditoria_final_v3_real.py`):
- `validar_final()` completa (length checks, lista regex proibidos, anti-meta, atribuição fonte)
- `_tem_atribuicao_fonte`, `_paragraph_count`, `_host_fonte`, `_apelido_fonte`
- `_precisa_editor_final_luxo` (lógica determinística de roteamento)
- `revisar_via_llm_v3` (fundida no revisor unificado)
- Bloco anti-meta-discurso `util_anti_meta_discurso_v3` cure+reauditar (agora LLM detecta direto)

**Do PUBLICADOR** (`executar_publicador_wp_v3_pending.py`):
- `_focus_keyphrase` (regex if/elif Lula/Senado/STF/Flávio)
- `_alertas_exigem_pending` (lista hardcoded de prefixos)
- `_normalizar_legenda_midia` + `_formatar_local_legenda` (concat de legenda)
- `POLITICA_DEFAULT_CATEGORY_ID = 22` (fallback cego pra "política")

### O que foi ADICIONADO

**Schema:**
- `produzidas`: + `focus_keyphrase`, `yoast_meta_description` (LLM acabamento agora persiste)
- `auditadas`: + `focus_keyphrase_final`, `yoast_meta_description_final` (propaga)
- `brutas_com_tese`: + `confronto_central`, `heroi`, `vilao` (já feito 23/06)

**Funções LLM:**
- `_classificar_via_llm` em acabamento (categoria + tags + Yoast tudo de uma vez)
- `revisor_unificado_v3` em auditoria (11 checks + status + alertas + decide editor final)
- `revisor_publicacao_v3` em publicador (decide publish|pending|abortar)
- `gerar_legenda_midia_llm` em publicador (legenda editorial Cafezinho)
- `narrar_via_llm` em relator (nota 0-10 + análise editorial)

### Bug crítico corrigido: Yoast LLM perdido

**Fluxo bug:**
1. Acabamento_seo gera `focus_keyphrase` + `yoast_meta_description` via LLM Cafezinho ✅
2. UPDATE produzidas só salvava 4 campos antigos — LLM **descartado** ❌
3. Publicador recriava `focus_keyphrase` via heurística regex (Lula/STF/Senado) ❌
4. Yoast WP recebia keyphrase ruim, meta_description = truncamento do lide

**Fix:**
1. ALTER TABLE produzidas + auditadas (4 colunas novas)
2. Acabamento UPDATE inclui os 2 novos
3. Auditoria INSERT copia pra `*_final`
4. Publicador lê de `auditada.focus_keyphrase_final`
5. Função `_focus_keyphrase` regex REMOVIDA

---

## 10.2 AGENTE RELATOR PÓS-PUBLICAÇÃO (NOVO)

**Criado 24/06 madrugada:** `/root/agente_relator_publicacao_v3.py` (757 linhas)

**Banco novo:** `/root/V3/banco_relatorios_publicacao_v3.db` (3 tabelas: relatorios_publicacao, relatorios_diarios, snapshots_bancos)

**Prometheus:** `/var/lib/node_exporter/textfile_collector/v3_relator.prom` (escrita atômica, mesmo padrão do `v3_vision_health.prom` existente)

**Métricas Prometheus emitidas:**
- `cafezinho_v3_banco_contagem{banco, tabela}` — contagem em cada banco V3
- `cafezinho_v3_etapa_modelo_chamadas_24h{etapa, modelo}` — distribuição dinâmica (detecta se Miguel trocar LLM)
- `cafezinho_v3_etapa_modelo_custo_usd_24h{etapa, modelo}` — custo por etapa/modelo
- `cafezinho_v3_etapa_modelo_tokens_24h{etapa, modelo}` — tokens
- `cafezinho_v3_relator_publicacoes_24h` — total no dia
- `cafezinho_v3_relator_nota_media_24h` — nota média editorial 0-10
- `cafezinho_v3_relator_custo_total_usd_24h` — custo pipeline 24h
- `cafezinho_v3_relator_tokens_total_24h` — tokens pipeline 24h
- `cafezinho_v3_relator_last_run_timestamp` — heartbeat

**Crons (3):**
- `*/15 * * * *` — relatórios novos (PAUSADO junto com pipeline V3)
- `50 23 * * *` — relatório diário agregado (PAUSADO)
- `*/5 * * * *` — Prometheus refresh (ATIVO mesmo com pipeline pausado)

**Conteúdo do relatório individual (por pauta publicada):**

Determinístico (do telemetria_etapas + bancos):
- WP post_id, URL, status, título final
- Tempo total + por etapa
- Tokens in/out + custo por etapa
- **Modelos REAIS usados** por etapa (não a cascata configurada — o que efetivamente respondeu)
- Confronto/herói/vilão da tese
- Grau aderência brutas_plus
- Foto origem + crédito
- Alertas publicação
- Resultado revisor unificado (11 checks)

LLM relator (contexto `relator_v3`, Sonnet primário):
- Nota 0-10 + resumo
- Análise: diferencial editorial, confronto, tom, fidelidade factual, SEO, custo/eficiência
- Pontos fortes/fracos
- Recomendação futura

**Saída dual:** JSON estruturado (banco) + Markdown (banco, legível humano)

---

## 10.3 FIX APIS — kimi/anthropic/zhipu (24/06 01:30 BRT)

Healthcheck Vision detectou via Telegram 4 alertas de chave principal falhando. Investigação:

| Provider | Problema real | Fix |
|---|---|---|
| Kimi | Conta internacional, endpoint configurado China | `api.moonshot.cn` → `api.moonshot.ai` |
| Anthropic | Modelo `claude-3-5-haiku-20241022` descontinuado | model_test → `claude-haiku-4-5` |
| Zhipu | Não usado mais | **Removido** do `chaves_api_map.json` |
| DeepSeek | Timeout transitório | Recuperou sozinho |

State.json do alerter zerado pra parar alertas Telegram stale.

**Healthcheck Vision V3:**
- Era `*/15 * * * *` → mudou pra `0 * * * *` (1×/hora)
- Economia 75% custo enquanto V3 está pausado

**Resultado:** 8/8 chaves OK agora.

---

## 11. PRÓXIMOS PASSOS

1. ⏳ Decidir religar V3 (descomentar 3 crons + 2 do relator)
2. ⏳ Auditar fase BRUTAS_PLUS (única não-reformada — ainda tem regex/heurística)
3. ⏳ Avaliar threshold curador 5.2 → 6.0 após primeiro ciclo real
4. ⏳ Confirmar hard-no-home agente_soberania
5. ⏳ Limpar 2 pautas órfãs Grande Reforma

---

## 12. BACKUPS GERADOS NA SESSÃO (com timestamps 20260623 + 20260624)

| Arquivo | Backups (sequenciais) |
|---|---|
| `/root/V3/agente_coletor_fontes_v3.py` | `.bak_pre_batch_unico_20260623_2320` |
| `/root/V3/v3_agente_tese.py` | `.bak_pre_v2_20260623_*`, `.bak_pre_confronto_20260624_002906` |
| `/root/V3/v3_producao_editorial.py` | `.bak_pre_confronto_20260624_002906` |
| `/root/V3/redator_llm_v3.py` | `.bak_pre_enriquecer_20260624_002906` |
| `/root/V3/executar_midia_v3_real.py` | (5 patches anteriores com .bak) |
| `/root/V3/executar_acabamento_seo_v3_real.py` | `.bak_pre_yoast_persist_20260624_010734` |
| `/root/V3/passo2e_taxonomia_seo/v3_acabamento_seo_taxonomia.py` | `.bak_pre_llm_20260624_004030`, `.bak_pre_llm_only_20260624_004604` |
| `/root/V3/executar_auditoria_final_v3_real.py` | `.bak_pre_revisor_unificado_20260624_005538`, `.bak_pre_yoast_propagacao_20260624_010734` |
| `/root/V3/executar_publicador_wp_v3_pending.py` | `.bak_pre_llm_only_20260624_010734` |
| `/root/V3/v3_editor_final.py` | (atribuição rodapé .bak — 23/06) |
| `/root/agente_roteador_llm.py` | múltiplos `.bak_pre_*_20260624_*` |
| `/root/.env.unificado` | múltiplos `.bak_pre_*_20260624_*` |
| `/root/agent_data/chaves_api_map.json` | `.bak_20260624_*` |

**Backup integral pre-pausa V3:** `/root/BACKUPS/v3_pause_20260623_235843.tar.gz`

---

## 13. ARTEFATOS NOVOS CRIADOS

| Arquivo | Linhas | Função |
|---|---|---|
| `/root/agente_observatorio_publicacoes.py` | 273 | Anti-repetição: 50 últimos + temas saturados |
| `/root/V3/util_anti_meta_discurso_v3.py` | ~80 | 13 regex pra detectar/limpar meta-discurso (legado, ainda existe) |
| `/root/V3/util_og_image_v3.py` | ~50 | Parser og:image / twitter:image |
| `/root/util_classificador_multicat.py` | ~200 | Multi-categorias regionais + temas (B-005) |
| **`/root/agente_relator_publicacao_v3.py`** | **757** | **Relator pós-publicação + Prometheus (24/06)** |
| `/root/V3/banco_relatorios_publicacao_v3.db` | (schema) | Banco SQLite relatórios (24/06) |
| `/var/lib/node_exporter/textfile_collector/v3_relator.prom` | dinâmico | Métricas Prometheus do pipeline V3 |

---

## 14. NOVOS CONTEXTOS LLM NO ROTEADOR

Adicionados em `/root/agente_roteador_llm.py` (`_DEFAULT_LLM_ROUTES["contexts"]`):

```python
"producao_v3":            ["deepseek_luxo", "openai_luxo", "anthropic_luxo"],
"revisao_v3":             ["anthropic_luxo", "openai_luxo", "deepseek_luxo"],
"editor_final_v3":        ["openai_luxo", "alibaba_luxo", "anthropic_luxo"],
"producao_editorial_v3":  ["openai_luxo", "anthropic_luxo", "deepseek_luxo"],  # Miguel pediu GPT primário
"acabamento_seo_v3":      ["deepseek_luxo", "openai_luxo", "anthropic_luxo"],  # Miguel pediu DeepSeek V4 Pro
"auditoria_final_v3":     ["anthropic_luxo", "openai_luxo", "deepseek_luxo"],
"publicador_v3":          ["openai_economico", "deepseek_economico", "alibaba_economico", "anthropic_economico"],
"relator_v3":             ["anthropic_luxo", "openai_luxo", "deepseek_luxo"],
```

## 15. NOVAS VARIÁVEIS .env.unificado

```bash
POLITICA_V3_LLM_CONTEXTO=producao_v3                   # default (coleta+tese)
POLITICA_V3_LLM_CONTEXTO_REDACAO=producao_editorial_v3 # produção
POLITICA_V3_LLM_CONTEXTO_ACABAMENTO=acabamento_seo_v3  # acabamento SEO
POLITICA_V3_LLM_CONTEXTO_AUDITORIA=auditoria_final_v3  # auditoria revisor unificado
POLITICA_V3_LLM_CONTEXTO_PUBLICADOR=publicador_v3      # publicador (revisor + legenda)
POLITICA_V3_LLM_CONTEXTO_RELATOR=relator_v3            # relator pós-publicação
POLITICA_V3_REVISAO_CONTEXTO=revisao_v3                # legado (revisor isolado)
POLITICA_V3_EDITOR_FINAL_CONTEXTO=editor_final_v3      # editor luxo correção

---

**Atualizar este fórum a cada nova fase auditada / patch deployado.**
