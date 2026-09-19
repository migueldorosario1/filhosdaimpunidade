---
name: reference-cerebro-secao-66-modelos-llm
description: §66 do Cérebro tem tabela MESTRA de modelos LLM testados (Qwen/Kimi/DeepSeek/Claude) + cadeia auditoria editorial. SEMPRE consultar antes de escolher modelo.
metadata: 
  node_type: memory
  type: reference
  originSessionId: 2b9623d1-ac11-4398-963e-f595ae871d7f
---

# §66 Cérebro — Tabela mestra modelos LLM + cadeia auditoria editorial

**Localização:** `Projeto Cafezinho Agentes/CEREBRO_NODE_GOVERNANCA.md` §66 (criada 2026-05-14 22:55 BRT por Claude).

## Quando consultar
- Antes de codar/deployar QUALQUER agente que chame LLM novo
- Quando Miguel perguntar "qual modelo X funciona melhor pra Y"
- Quando aparecer modelo novo de provedor chinês (Alibaba, Moonshot, DeepSeek, Zhipu)
- Quando algum modelo regredir em produção (auditor não respondeu, content vazio, latência alta)

## Resumo das 6 sub-seções

- **§66.1 Tabela mestra** — 14 modelos testados com prompt Mearsheimer-like: latência, tokens, reasoning?, acertou?, custo, status
- **§66.2 Cadeia AUDITORES_DIVERSOS** — qwen3-max → qwen-max-latest → qwen-plus-latest → deepseek-chat
- **§66.3 Preços (Mai/2026)** — Qwen Plus $0.003/audit (12× barato Sonnet), Qwen3-Max $0.010, Opus $0.195
- **§66.4 Endpoints + chaves** — Alibaba/Moonshot/DeepSeek são 3 provedores INDEPENDENTES, chaves separadas
- **§66.5 Regra Miguel:** Cérebro = tabela viva. Modelo novo → testar prompt-padrão → indexar → DEPOIS deployar
- **§66.6 Prompt-teste canônico** Mearsheimer-like (detectar atribuição cruzada Diesen×Kagan PT-BR) + critérios aprovação

## Achados críticos (NÃO usar em produção)

| Modelo | Problema |
|---|---|
| `kimi-k2.6` | Reasoning model — content VAZIO mesmo com max_tokens=800 |
| `deepseek-v4-pro` | Reasoning model — precisa max_tokens≥2000, lento |
| `qwen3.5-*`, `qwen3.6-*` (plus/flash/max-preview) | Todos reasoning, ≥7s latência |

## Bug fundador relacionado

`BUG-20260514-DEEPSEEK-V4-REASONING-TOKENS-CONSUMIDOS` em `CEREBRO_NODE_BUGS.md` — incidente fundador que motivou todo o bake-off. Codex identificou que `motor_publicador.py` chamava `deepseek-v4-pro` com `max_tokens=500` e auditoria geopolítica falhava 80% dos ciclos.

## Atualizar quando

Toda vez que provedor lançar SKU novo, mudar preço, deprecar modelo, ou regredir comportamento. Disciplina: testar com prompt §66.6 antes de tocar produção.
