---
name: Agente Análise — skeleton + fina flor pinada 2026-04-24
description: Estado do Agente Análise ao fim de 24/04/2026 18h — Camadas 1-4 escritas em dry_run, fina flor pinada (Opus 4.7/GPT-5.5 Pro/Grok-4/Sonnet) via novo atualizador de modelos, sistema dinâmico contra obsolescência.
type: project
originSessionId: 7b364031-59bc-4cee-8526-b9521b506352
---
**Estado final 2026-04-24 ~17:58 BRT** — Agente Análise em `Projeto Cafezinho Agentes/root/analise/`, smoke test E2E rodando em dry_run.

## Skeleton escrito e testado (dry_run)
- `schemas.py` — dataclasses 5 camadas + `MatrizEditorial.validar()`
- `historico_analises.py` — SQLite TF-IDF anti-repetição (limiar 0.78, 14d) + `bootstrap_do_corpus()`
- `banco_teses.py` — leitor 15 teses + `selecionar_few_shots(tema, lentes, top_n)`
- `augusto_notifier.py` — 4 notificações Telegram (rascunho/expiração/abortado/fact-check)
- `llm_router.py` — resolver papel→modelo via `modelos_vivos.json`
- `camada1_escuta.py` — motor_coletor + GA4 + curadoria manual
- `camada2_agrupamento.py` — LLM agrupa sinais em blocos de sentido
- `camada3_tese.py` — gera 3-4 teses + anti-repetição + escolhe melhor
- `camada4_redacao.py` — TWO-PASS (matriz JSON → prosa) + fact-check Perplexity hook + pós-processamento regex (clichês, data chumbada, períodos/parágrafo, palavras)

**Falta:** camada5_distribuicao.py, wp_publisher.py (integração WP), agente_analise.py (orquestrador raiz).

## Fina flor pinada por camada (§8.3 do forum_agenteanalise.md)
| Papel | Modelo | Uso |
|---|---|---|
| luxo_raciocinio | **claude-opus-4-7** | Camada 3 gerar teses |
| luxo_redacao | **claude-opus-4-7** | Pass B da redação |
| luxo_estrutura | **gpt-5.5-pro** | Pass A da Matriz JSON |
| auditor | **grok-4.20-0309-reasoning** | 2ª opinião (laudo) |
| padrao | claude-sonnet-4-6 | Camada 2, escolha de tese |
| economico | claude-haiku-4-5-20251001 | pré-processamento |

## Sistema anti-obsolescência (cron-ready)
**Novo arquivo:** `root/atualizador_modelos_llm.py` — bate em `/v1/models` de 7 providers (Anthropic, OpenAI, xAI, Gemini, Mistral, DeepSeek, Groq), filtra o top de cada família e atualiza `agent_data/modelos_vivos.json`. Heurística evita snapshots datados (`-YYYYMMDD`), exclui variantes `search-api` / `non-reasoning` / `mini` onde não fazem sentido, prefere aliases `-latest`.

**Dia 1 rodou e descobriu upgrades:**
- novo: `anthropic_opus: claude-opus-4-7` (antes inexistente)
- `openai_luxo: gpt-5-search-api → gpt-5.5-pro`
- `openai_economico: gpt-4o-mini → gpt-5-mini`
- `mistral_luxo: pixtral-large → mistral-large-latest`
- `deepseek_luxo: deepseek-reasoner → deepseek-v4-pro`

**Agendar cron semanal:** `0 4 * * 1 cd /root && python3 atualizador_modelos_llm.py` (quando deploy no Tencent).

## Corpus e banco de teses
- `agent_data_analise/banco_analises_amplo.json` — 7.290 análises do Miguel (james2017, 2011-2026), 49 MB, 26 rótulos temáticos, 6.6M palavras.
- `agent_data_analise/banco_teses.json` — 15 teses-âncora (Antigravity) × 5 exemplos históricos TF-IDF (cada).
- `agent_data_analise/historico.db` — SQLite criado mas vazio; `bootstrap_do_corpus()` popula no 1º run.

## Decisões editorial-arquiteturais sacramentadas (§11 do fórum)
- Matriz vai pro WP em bloco Gutenberg colapsável `<!-- wp:details -->` (opção A).
- Autor: "Redação" (ID 5470). Sem persona ficcional.
- `NEWS_STATUS=draft` forçado no código na 1ª semana.
- Two-Pass (Matriz JSON → Redação) com pós-processamento regex como defesa em profundidade.
- Notificação Augusto dupla: rascunho pronto (~16h) + expiração (20h).
- **Regra de Ouro (§11.3):** "inteligência pela escolha da tese, não pela quantidade de informação".

## Pontos de atenção
- Smoke test só rodou em `dry_run=True`. Primeira execução real vai gastar Opus/GPT-5.5 — monitorar custo.
- `agente_roteador_llm.gerar_texto_modelo_especifico` foi mapeado como ponto de entrada do `llm_router.call` — confirmar que a assinatura bate no primeiro run real (ou ajustar wrapper).
- Fact-check Perplexity está como hook: se `fact_check_perplexity.py` não estiver com `checar_fatos()` pública, cai em "pulo" silencioso — precisa validar quando for deploy.
