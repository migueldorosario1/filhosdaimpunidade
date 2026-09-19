---
name: feedback-ec3-websearch-obrigatorio-constitucional
description: "EC3 constitucional (Miguel 20/06 11:00 BRT): WebSearch obrigatório em pelo menos uma das três camadas pré-publicação (produção OU revisor). Fact-check SEMPRE com WebSearch, sem exceção. Cascata fact-check não pode ter fallback sem WS (DeepSeek/Qwen). Caso fundador #259655 Sheinbaum eleita aprovado pelo Qwen sem grounding. Patches §92 REFORMA: produtor_geral.py com googleSearch + auditor_texto.py com cascata reduzida."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 7b054038-ee9d-4869-bac1-f58e75f914b3
---

# EC3 — WebSearch obrigatório constitucional

**WebSearch obrigatório em pelo menos uma das três camadas pré-publicação (produção OU revisor). Fact-check SEMPRE obrigatório, sem exceção, sem ramo sem WS.**

**Why:** Caso fundador #259655 19/06 14:00 BRT — REFORMA publicou "Sheinbaum **eleita** planeja aprofundar transparência" 20 meses após a posse (01/10/2024). Investigação Daemon 20/06 manhã achou 2 bugs raiz: (1) `produtor_geral.py` chamava Gemini sem `tools:[{google_search:{}}]` — payload puro, sem grounding; (2) cascata `auditor_texto.py` era `[gemini_grounding, deepseek, qwen, perplexity]` — DeepSeek e Qwen sem WebSearch entravam no fluxo e aprovaram (`provider_final: "qwen_revisor"`). Miguel cravou: *"transforma isso em regra constitucional. o websearch precisa estar presente. ou na produção (que pode ser com deepseek v4 pro sem websearch), ou no revisor, obrigatoriamente. O fact check obviamente tem que ter websearch."*

**How to apply:**

Configuração mínima por matéria publicável:

| Camada | WebSearch obrigatório? | Modelos válidos |
|---|---|---|
| Produção (redator) | Opcional | Pode ser DeepSeek-v4-pro sem WS, MAS revisor tem que compensar |
| Revisor | Opcional | Uma das duas (produção OU revisor) precisa ter WS |
| Fact-check / Auditor | **OBRIGATÓRIO** | Gemini Grounding (`google_search` tool), Perplexity Sonar Pro com web_search, GPT com `web_search`, Claude com `web_search_20250305` |

Cenários proibidos:
- Produção sem WS + revisor sem WS (cenário REFORMA pré-patch)
- Cascata fact-check com fallback sem WS (DeepSeek puro, Qwen puro)

Status atual:
- **LEGADO** `agente_roteador_llm.py:1147-1156` já cumpre via `_CONTEXTOS_WEBSEARCH_OBRIGATORIO`
- **REFORMA** corrigida 20/06 11:30-11:40 BRT via patches §92 em `produtor_geral.py` (googleSearch tool) e `auditor_texto.py` (cascata reduzida a Gemini Grounding + Perplexity)

Pra qualquer agente novo:
1. Ao escrever publicador, importar `agente_roteador_llm` LEGADO em vez de chamar API direto, OU
2. Se for chamar API direto (Gemini REST), incluir `tools:[{google_search:{}}]` no payload
3. Auditoria/fact-check só deve depender de providers com WebSearch nativo
4. Gate automatizado proposto: teste que falha se payload não tem `tools` ou tem ramo sem WS

Vinculado a §108 do [[cerebro-node-governanca-regras-vivas]] e a [[feedback-websearch-obrigatorio-producer-auditor-curador]] (EC2 anterior, 13/06).
