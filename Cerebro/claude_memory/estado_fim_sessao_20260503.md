---
name: Estado fim sessão 2026-05-03
description: Snapshot da sessão 03/05 — Sprint A + Sprint B Slot 7 deployados; gap arquitetural roteador→autocura fechado
type: project
originSessionId: 27fa3d94-687d-4e76-883e-a27400677272
---
Sessão em andamento 2026-05-03 BRT. Slot 7 completamente concluído (Sprint A + Sprint B).

**Why:** Incidente 03/05 — `claude-opus-4-7` temperatura deprecated causou degradação silenciosa. Sprint A corrigiu proativamente; Sprint B fecha o loop de retroalimentação em runtime.

**How to apply:** Slot 7 concluído. Próxima sessão pode reciclar ou abrir nova tarefa.

---

## Sprint A — DEPLOYADO (2026-05-03 ~14:00)

1. `agente_validador_modelos.py` — smoke test inclui `temperature=0.4`; 400 deprecated → flag `sem_temperature: true` em `modelos_vivos.json`
2. `agente_roteador_llm.py` `_anthropic_payload()` — lê flag `sem_temperature`, omite temperature se True
3. `atualizador_llm.py` — filtro blocklist antes de eleger modelos
4. `fact_check_perplexity.py` — data em caixa proeminente no SYSTEM_PROMPT + USER_PROMPT
5. `agente_china.py` — URLs RSS corrigidas + parser auditoria robusto

Backups: `*.bkp_pre_sem_temperature_20260503`, `atualizador_llm.py.bkp_pre_blocklist_filter_20260503`, `agente_china.py.bkp_pre_rss_fix_20260503`, `fact_check_perplexity.py.bkp_pre_data_inject_20260503`

---

## Sprint B — DEPLOYADO (2026-05-03 ~17:55)

1. `agente_roteador_llm.py`:
   - `from datetime import datetime, timedelta` (adicionado `timedelta`)
   - `_registrar_falha_parametro(modelo, tipo_erro)` — grava em `agent_data/falhas_modelos_runtime.json` atomicamente; prune >4h
   - Chamada nos 2 blocos Anthropic (linha ~531 e ~906) quando `_anthropic_temperature_deprecated()` retorna True

2. `agente_autocura_v4.py`:
   - `FALHAS_RUNTIME_PATH` e `MODELOS_VIVOS_PATH` adicionados como constantes
   - `_falhas_ja_notificadas: set` — evita notificação dupla por execução
   - `verificar_falhas_modelos_runtime()` — filtra janela 2h, ≥3 falhas tipo "sem_temperature" → aplica flag em `modelos_vivos.json` + `enviar_telegram()`
   - Chamada no início de `run_ciclo()` após `pausa_ativa()` check

Backups: `*.bkp_pre_sprintb_20260503` (local + servidor)

---

## Pendências ainda ativas

- **Onda 3 `detectar_recusa_llm`**: escritor_scifi, historiador, singularidade, riocarta (baixa prioridade)
- **`google.generativeai` → `google.genai`**: pacote deprecated afeta agente_curador_midia, agente_crime, agente_news_trend, publicador_tematicos, agente_diario_direita
- **master_lula anacronismo**: paralisado
- **Temáticos sem retry**: sem mecanismo de retry em falhas isoladas
- **Sprint B futuro**: tratar outros tipos de erro em runtime (max_tokens, model_not_found) — estrutura já pronta, só adicionar branches em `verificar_falhas_modelos_runtime()`
