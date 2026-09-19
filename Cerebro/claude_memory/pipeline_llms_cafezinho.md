---
name: Pipeline de LLMs do Cafezinho (6 modelos por matéria, 5 provedores)
description: Cada matéria passa por 6 LLMs em cascata (produção, revisão, auditoria, fact-check primário Perplexity, fact-check fallback Claude, Tribunal Visual Gemini). Modelos são descobertos dinamicamente por atualizador_llm.py.
type: reference
originSessionId: 82c307d7-bd07-4c7a-8ed2-9e86b6fa4e22
---
Toda matéria que passa pelo `motor_publicador.py` (Trindade Editorial, reciclador, soberania, militar) é processada por **6 LLMs em cascata**, distribuídos em **5 provedores**. Agentes standalone (feminino, eleições, fantástico, analytics, temáticos) usam subconjunto semelhante via `agente_roteador_llm.py`.

## Pipeline completo por matéria (ordem de execução)

| # | Etapa | Modelo atual | Provedor | Fallback | Arquivo |
|---|---|---|---|---|---|
| 1 | Produção (texto base) | `gpt-5-search-api-2025-10-14` / `gpt-4o` | OpenAI | gemini-2.5-pro | `agente_roteador_llm.py` |
| 2 | Revisão Swarm (afia tom) | `grok-4.20-0309-reasoning` | xAI | claude-sonnet-4-6, pixtral-large | idem |
| 3 | Auditoria Final | `claude-sonnet-4-6` | Anthropic | voxtral-small-latest | idem |
| 4 | **Fact-check PRIMÁRIO** (Juiz) | **`sonar-reasoning-pro`** | **Perplexity** | — | `fact_check_perplexity.py` |
| 5 | Fact-check fallback (se Perplexity timeout/crash) | `claude-sonnet-4-6` | Anthropic | — | motor_publicador → `fact_check` |
| 6 | Tribunal Visual (imagem) | `gemini-2.5-flash` | Google | — | `agente_roteador_llm.analisar_imagem_gemini_vision` |

## Categorias de modelos do Roteador

Definidas em `agente_roteador_llm.py`:

- **Luxo:** gpt-4o / claude-sonnet-4-6 (produção premium)
- **Econômico:** gpt-4o-mini / gemini-2.5-flash (buscas rápidas, auditorias leves)
- **Padrão:** gpt-4o / gemini-2.5-pro
- **Revisor:** grok-3/grok-4.20 / claude-sonnet-4-6
- **Auditor:** claude-sonnet-4-6

## Discovery dinâmico

`atualizador_llm.py` roda 1x/dia às 08:00 (crontab) e atualiza `agent_data/modelos_vivos.json`. Por isso às vezes aparece versão nova de modelo (ex: `gpt-5-search-api-2025-10-14`) sem hardcode — o sistema descobriu sozinho.

## Uso do Perplexity (importante, não esquecer)

**Perplexity é Juiz Primário, não backup.** Arquitetura (definida pelo Miguel em 14/04/2026):

```
[Perplexity sonar-reasoning-pro — liberal, tolerante ao viés progressista]
  ├─ aprovado=True  → PUBLICA direto (pula o Claude)
  └─ timeout/crash/False → Claude Sonnet 4.6 como segurança
```

13 arquivos de produção usam diretamente: `motor_publicador`, `agente_feminino`, `agente_eleicoes`, `agente_fantastico`, `agente_analytics_v9`, `agente_rail_post` (ferroviário), `agente_riocarta`, `agente_petroleo`, `agente_mercado`, `agente_ia`, `agente_inflacao`, `agente_energias`, `publicador_tematicos`.

## Redes sociais (pipeline separado)

- **Twitter:** `gerador_fios_x.py` usa `grok-3` direto (com fallback `grok-3-mini`).
- **Facebook/Instagram:** `gerador_meta_textos.py` usa `chamar_llm()` — tenta Grok primário, fallback `gpt-4o` (fix adicionado em 2026-04-17 08:30).

## How to apply

- **Adicionar um novo modelo:** adicionar no discovery do `atualizador_llm.py` + criar/editar função de chamada em `agente_roteador_llm.py`.
- **Trocar ordem de prioridade:** editar as listas em `agente_roteador_llm.py` (luxo/eco/padrão/revisor/auditor).
- **Desabilitar um provedor temporariamente:** tirar a chave do `.env.unificado` — o sistema detecta chave vazia e pula o modelo.
- **Monitorar custo:** `banco_custos.json` registra cada chamada; `agente_contador.py` envia resumo diário às 08:30 ao Telegram do Augusto.
