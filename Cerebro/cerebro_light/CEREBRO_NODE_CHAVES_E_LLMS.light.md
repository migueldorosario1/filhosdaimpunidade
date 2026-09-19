# CEREBRO_NODE_CHAVES_E_LLMS — VERSÃO LIGHT
> Gerado automaticamente por `cerebro_light.py` em 2026-07-09 03:32 BRT
> Original: `CEREBRO_NODE_CHAVES_E_LLMS.md` (36KB) — 38 entradas totais
> Este arquivo é READ-ONLY. Edite sempre o original.

---

## CABEÇALHO ORIGINAL (primeiras linhas)

# 🔑 CÉREBRO CAMADA 2: Nodo de Chaves, Inteligência e LLMs

---

## 🐋 MAPA ESTRATÉGICO DE LLMs — Pipeline V2 — 2026-06-18

**Fórum canônico:** [`Projeto Cafezinho Agentes/Foruns/forum_mapa_estrategico_llms_pipeline_v2_20260618.md`](../Projeto%20Cafezinho%20Agentes/Foruns/forum_mapa_estrategico_llms_pipeline_v2_20260618.md)

Mapa completo de qual LLM usar em cada uma das 7 etapas do pipeline V2 (Coleta+Filtro → Scoring → Redação → Mídia → Fact-check → Auditoria → Publicação+Validador). Custo total: ~$0.12/dia (6.7x mais barato que o legado). Inclui gap analysis do que já está codeado vs o que falta implementar.

📰 **Boletim Baleia Azul:** [`Projeto Cafezinho Agentes/Foruns/boletim_baleia_azul_20260618.md`](../Projeto%20Cafezinho%20Agentes/Foruns/boletim_baleia_azul_20260618.md) — Edição #1 do jornal interno diário. Manchete: Pipeline V2 definido. Cobre decisões, sprints, AUTHs, Trindade e custos. (Coleta+Filtro → Scoring → Redação → Mídia → Fact-check → Auditoria → Publicação+Validador). Custo total: ~$0.12/dia (6.7x mais barato que o legado). Inclui gap analysis do que já está codeado vs o que falta implementar. Decisões de Miguel em 18/06: fact-check com Gemini Grounding, auditoria com websearch de luxo, filtro antilixo na coleta, validador final com poder de bloqueio.

---

## ✅ Regra Operacional — Cascata LLM com Websearch Obrigatório — 2026-06-11

**Fórum canônico:** [`Foruns/forum_cascata_llm_websearch_20260611.md`](../Foruns/forum_cascata_llm_websearch_20260611.md)

Decisão Miguel/Codex:

- Produção pode usar LLM sem busca: `deepseek-v4-pro → openai_luxo → claude-sonnet-4-6`.
- Revisão, auditoria e fact-checking exigem websearch real.
- Perplexity/Sonar está sob investigação por falso positivo; fica apenas como fallback final investigado.

Estado deployado no Tencent:

| Etapa | Cascata |
|---|---|
| Produção | `deepseek_luxo → openai_luxo → anthropic_luxo` |
| Revisão | Gemini + `google_search` → OpenAI `web_search` → Claude `web_search` |
| Auditoria | Gemini + `google_search` → OpenAI `web_search` → Claude `web_search` |
| Fact-check | Gemini + `google_search` → OpenAI `web_search` → Claude `web_search` → Perplexity fallback investigado |

Arquivos canônicos no Tencent:

- `/root/agente_roteador_llm.py`
- `/root/config/llm_context_routes.json`
- `/root/fact_check_perplexity.py`

Backups principais:

- `/root/agente_roteador_llm.py.bak_pre_openai_claude_search_20260611_codex`
- `/root/config/llm_context_routes.json.bak_pre_openai_claude_search_20260611_codex`
- `/root/fact_check_perplexity.py.bak_pre_openai_claude_search_20260611_codex`

Correção pós-auditoria real dos posts — 2026-06-11 22:27 BRT:

- A primeira subida existiu, mas a checagem dos posts `257676` e `257674` mostrou que não bastava.
- Causa 1: diversidade dinâmica podia excluir Gemini/OpenAI em `auditor` e deixar Qwen/Moonshot/Mistral entrar.
- Causa 2: `motor_publicador.py` ainda tinha fact-check/auditoria auxiliar por `gerar_texto_provider_hard("anthropic")`, sem contexto `fact_check`/`auditor`.
- Correção: `/root/agente_roteador_llm.py` agora força apenas Gemini/OpenAI/Claude com websearch em contextos obrigatórios e pula provider sem suporte; `/root/motor_publicador.py` agora chama `gerar_texto(..., contexto="fact_check")` e `gerar_texto(..., contexto="auditor")` nos portões finais.
- Backups novos: `/root/agente_roteador_llm.py.bak_fix_websearch_diversidade_20260611_codex`, `/root/motor_publicador.py.bak_fix_factcheck_websearch_20260611_codex`, `/root/motor_publicador.py.bak_fix_auditoria_extra_websearch_20260611_codex`.
- Validação remota: `compile(...)` OK nos 3 arquivos; simulação de `auditor`, `revisor` e `fact_check` com exclusões artificiais ainda retorna Gemini/Search → OpenAI/Search → Claude/Search.

---

## 🟢 SNAPSHOT CHAVES VIVAS — 2026-05-22 14:00 BRT (Claude Maestro · ordem direta Miguel)

**Contexto:** este snapshot foi criado por ordem direta do Miguel após o incidente Perplexity HTTP 401 detectado em 22/05/2026 que deixou o fact-check em fail-open. Inscrito em lugar visível pra qualquer agente da Trindade poder conferir rapidamente o estado vivo das chaves sem precisar SSH.


---

## ⏩ 33 entradas antigas omitidas
> Para ver o histórico completo, leia `CEREBRO_NODE_CHAVES_E_LLMS.md` diretamente.
> Busca rápida: `python3 cerebro.py --buscar <termo>`

---

## ÚLTIMAS 5 ENTRADAS

### Substituição de hardcodes

Hardcodes tipo `gerar_texto_provider_hard("zhipu", ...)` viram dinâmicos:
```
gerar_texto(..., tarefa="redacao") → roteador lê llm_ratings.json e escolhe
```

---

### Cronograma

2 semanas estimadas até sistema completo + monitor + curador rodando. Detalhe em §12 do fórum.

---

### Status atual (atualizado 18/05 15:10 BRT)

- ✅ Critérios definidos
- ✅ Tabela inicial rascunho Claude (26 modelos com notas Q/E) — §3 do fórum
- ✅ Pesquisa independente Codex — concluída 18/05 13:15 BRT (§14 do fórum: agregação local `banco_custos.json` + `governanca_financeira_api_usage.jsonl` + `log_rotas_llm.jsonl`)
- ✅ Pesquisa independente DeepSeek — concluída 18/05 (§16 do fórum: testes ao vivo Zhipu/DeepSeek/Qwen)
- ✅ Pesquisa independente Antigravity — concluída 18/05 (§15 do fórum: preços oficiais 1M tokens + Arena 2026)
- ✅ Parecer cruzado Codex sobre §15 — §17 do fórum (13:25 BRT: pediu URLs/data + propôs duas economias separadas)
- ✅ Consolidação técnica provisória Codex — §18 do fórum (14:55 BRT: schema mínimo, tabela 18 modelos, regras por tarefa, ordenação roteador)
- ✅ 

> *(... 1575 chars omitidos — ler original)*

---

### [2026-05-21 19:25 BRT] — Política Perplexity por silo

**Decisão Miguel:** Perplexity continua permitido no Cafezinho, mas fica pausado no Rio Carta e no Global South News durante a reforma editorial/infraestrutural.

**Motivo:** diagnóstico de custo mostrou uso relevante no Cafezinho/Tencent (`sonar-pro` em fact-check), e Miguel decidiu evitar expansão desse custo para os satélites.

**Regra operacional:**
- Cafezinho: Perplexity permitido para fact-check, sob monitoramento financeiro.
- Rio Carta: Perplexity bloqueado/pausado.
- Global South News: Perplexity bloqueado/pausado.
- Roteadores, cascatas e `llm_ratings` não devem escolher Perplexity para Rio Carta/GSN sem autorização explícita de Miguel.

**Arquivos locais ajustados por Codex:**
- `Rio Carta Agentes/root/riocarta_publicad

> *(... 148 chars omitidos — ler original)*

---

### [2026-05-22 00:38 BRT] — Política LLM Mundo Trilhos

**Decisão Miguel/Trindade:** Mundo Trilhos deve operar durante a reforma com pipeline editorial 100% asiático e sem Perplexity.

**Arquitetura proposta no fórum:**

- Triagem: DeepSeek V4 Flash
- Redação: DeepSeek V4 Pro
- Higienização: Qwen Max
- Fact-checking de coerência lógica: Kimi/Moonshot
- Auditoria final: Zhipu/GLM

**Regra operacional:** Mundo Trilhos não deve usar Perplexity, OpenAI, Anthropic ou Gemini no pipeline de publicação sem autorização explícita posterior de Miguel. Antes de deploy, a Trindade deve confirmar nomes reais dos modelos configurados no roteador/cascata e testar chaves sem expor segredos.

**Registro:** `Foruns/forum_mundo_trilhos.md`

---

## PONTEIROS
- Original completo: [`CEREBRO_NODE_CHAVES_E_LLMS.md`](./CEREBRO_NODE_CHAVES_E_LLMS.md)
- Índice geral: [`indice_cerebro.json`](./indice_cerebro.json)
- Busca: `python3 cerebro.py --buscar <termo>`
- Validador: `python3 validar_cerebro.py`