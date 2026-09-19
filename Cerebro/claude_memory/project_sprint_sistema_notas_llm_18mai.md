---
name: project-sprint-sistema-notas-llm-18mai
description: "Sprint Trindade (18/05+) — substituir nomenclatura \"luxo/econômico\" por sistema de notas 2D (Qualidade 1-5⭐ + Economia 1-5⭐), gerar llm_ratings.json, refatorar roteador pra usar tarefa= em vez de provider_forcado=. Frente dividida 18/05 15:05 BRT."
metadata: 
  node_type: memory
  type: project
  originSessionId: 4c52d90e-06f8-4198-8f65-dc7d7dc0c759
---

# Sprint Sistema de Notas LLM (18/05/2026+) — estado vivo

**Fato:** sprint da Trindade pra (1) substituir a nomenclatura ambígua "luxo/econômico" da política §4.2 por **sistema de notas em 2 dimensões** (Qualidade editorial 1-5⭐ + Economia 1-5⭐, mais estrelas = mais desejável), (2) gerar arquivo `root/config/llm_ratings.json` consolidado, (3) refatorar o roteador (`agente_roteador_llm.py`) pra usar `gerar_texto(..., tarefa="redacao"|"perifericos_editoriais"|...)` em vez dos hardcodes `gerar_texto_provider_hard("zhipu", ...)`. Inclui agente curador semanal pra manter notas atualizadas + monitor matriz editorial pra detectar desvios.

**Why:**
- Nomenclatura legada misturava dimensões (preço × qualidade) e gerava decisões erradas (ex: "DeepSeek é econômico mas é luxo" — ambíguo)
- Hardcodes `provider_forcado="zhipu"` espalhados em 4 arquivos (`agente_analytics_v9.py`, `agente_master_trends_v9.py`, `agente_rail_post.py`, `mayra_tools.py`) — manutenção frágil
- Bug `BUG-20260518-GLM-4-PLUS-ALUCINA-COM-TRAVA-EXPLICITA` mostrou que confiar em política sem teste-trava empírico produz escolhas erradas (Claude recomendou `glm-4-plus` primário, DeepSeek-V4-Pro mostrou-se superior)
- Miguel decidiu inverter prioridades: notas ANTES da migração F0a (que ficou suspensa)

**How to apply:**

**Fonte de verdade (LER PRIMEIRO ao retomar):**
- Fórum principal: `Projeto Cafezinho Agentes/Foruns/forum_sistema_notas_llm_20260518.md` (~1200 linhas, 22 seções)
- Fórum monitor matriz: `Projeto Cafezinho Agentes/Foruns/forum_comparativo_monitoramento_llm_20260518.md` §4.3 + §4.5 (patch)
- Cérebro: `Projeto Cafezinho Agentes/CEREBRO_NODE_GOVERNANCA.md` §66.8 + §66.8.1
- Cérebro: `Projeto Cafezinho Agentes/CEREBRO_NODE_CHAVES_E_LLMS.md` linhas 178-231 (status)

**Estado em 18/05 15:18 BRT:**

| Quem | Frente | Status |
|---|---|---|
| Claude | §3 rascunho 26 modelos + §19 auto-crítica + §20 parecer sobre §18 + §22 handoff + §4.5 patch monitor | DONE |
| Codex | §14 custos reais logs PROD + §17 parecer AG + §18 consolidação técnica (schema mínimo, tabela 18 modelos, regras por tarefa, ordenação roteador) | DONE |
| Antigravity | §15 preços oficiais 1M tokens + benchmarks Arena 2026 | DONE (falta URLs §18.5 item 1) |
| DeepSeek | §16 testes ao vivo Zhipu/DS/Qwen + §21 status próprio | DONE pesquisa, PENDENTE testes-trava §22.2 |

**Frente dividida (Miguel 15:05 BRT):**
- DeepSeek (chaves PROD): testes-trava `qwen3-max`, `mistral-large-latest`, `kimi-k2.5`, `qwen-max-latest`, `glm-5.1[enable_thinking=false]`, `qwen-vl-max-latest` (imagem real), `glm-5.1` em temas sensíveis CN + validar custos reais chineses no `governanca_financeira_api_usage.jsonl` + custo real `deepseek-v4-pro` PROD
- Claude (sem chaves): supervisão arquitetural reativa + auditoria pré-deploy PR Codex + indexação Cérebro + memória persistente
- Codex (código): aguarda decisão Miguel A/B/C F0a + monta `llm_ratings.json` proposta em paralelo + depois implementa `escolher_modelos_por_tarefa()` + `gerar_texto(..., tarefa=)` com compat backward
- Antigravity: adicionar URLs/fontes/data nas tabelas oficiais §15

**Decisão Miguel PENDENTE (16/05 15:18 BRT):** F0a intermediário (deploy hoje hardcode zhipu nos 4 arquivos) vs reescalonar pra dentro do sprint completo. Claude errou no §20.6 ao propor F0a apoiado em "sangria Anthropic ativa" — auditoria 14:58 BRT mostrou `anthropic.enabled=false` desde 14/05 + zero custos Anthropic em maio. Sangria já tinha parado. Veja [[feedback_verificar_premissa_antes_decisao]]. Decisão revisada: A (reescalona) / B (deploy mesmo assim como defense-in-depth) / C (outro). Aguardando Miguel.

**Schema consolidado (§18.2 + adendo §20.2 Claude):** entrada por modelo guarda `qualidade`, `economia_oficial`, `economia_observada`, `preco_oficial_usd_1m_input/output`, `preco_fonte_url`, `custo_real_medio_chamada_usd`, `status` (ativo/bloqueado/legado/pendente_teste), `funcoes_permitidas`, `bugs_ativos`, `flags` (search/vision/reasoning/exige_temperature_01/tratar_4xx_como_erro_ferramenta/bloqueado_por_politica/motivo_bloqueio).

**10 decisões consensuais §18.1:** F0a suspenso até sistema avançar; hardcode sai; redação/revisão/auditoria/fact-check Q≥4; status=bloqueado precede Q/E; `deepseek-v4-pro` primário provisório; `glm-4-plus` bloqueado enquanto bug ativo; `glm-5.1` vira 2 entradas (reasoning + thinking_false); search/RAG é categoria separada; HTTP 4xx chinês = erro ferramenta; economia tem 2 leituras (oficial + observada).

**Cronograma realista §19.5:** 14-18 dias até sistema completo + monitor + curador rodando.

**Próximas ações esperadas (em ordem):**
1. Miguel decide A/B/C F0a → Codex executa rota escolhida
2. Codex cria `llm_ratings.json` em modo proposta (`status: "draft"`)
3. DeepSeek roda testes-trava + valida custos reais → atualiza tabela §3
4. Antigravity adiciona URLs §15
5. Trindade revisa JSON proposta consolidado
6. Codex implementa `gerar_texto(..., tarefa=)` + compat backward
7. Codex refatora 4 arquivos F0a usando `tarefa=`
8. Claude audita PRs → smoke test → deploy Tencent
9. Codex coda `agente_monitor_matriz_editorial.py` consumindo `llm_ratings.json` (com patches §4.5 do `forum_comparativo_monitoramento_llm_20260518.md`)
10. Codex coda `agente_curador_notas_llm.py` semanal (cron `0 8 * * 0`)

Relacionado: [[feedback_verificar_premissa_antes_decisao]] (lição da minha cagada §20.6), [[reference_cerebro_secao_66_modelos_llm]] (§66 do Cérebro Governança, tabela mestra LLM).
