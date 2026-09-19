# FÓRUM — Telemetria completa de APIs: FASE 0+1 concluídas (mistério DeepSeek resolvido) — 02/08/2026

**Data:** 2026-08-02 ~18:00 BRT
**Autor:** ZCode (GLM-5.2), ordem direta do Miguel
**Status:** ✅ FASE 0+1 CONCLUÍDAS E VALIDADAS. FASES 2-5 pendentes.
**Plano aprovado:** ver §1 (componentes A-D, 6 fases).
**Relacionado:** `forum_diagnostico_pico_gasto_31jul_tribunal_visual_20260802.md` (origem do mistério)

---

## 1. Contexto — por que telemetria nova

O Miguel notou gasto DeepSeek alto (~$20 em poucos dias) que a telemetria **não explicava** (DeepSeek constava $0 no `api_usage.jsonl`). Investigação com 3 agents revelou **4 gaps**:

1. **~85 scripts chamam API direto sem telemetria** (`coletor.py`, `bot_*`, `agente_escritor_scifi`, `v4_media_expander`, etc.)
2. **DeepSeek não caía no `api_usage`** (ramo dedicado do roteador só chamava `registrar_gasto` → `banco_custos`; watchlist cega)
3. **Risco de double-counting** (Alibaba/Moonshot/Zhipu em ambos arquivos)
4. **Moka (Tencent) + Temáticos V4 locais** têm roteador próprio → fora do painel

**Plano aprovado (6 fases):** F0 fundação → F1 gap DeepSeek roteador → F2 top-15 scripts diretos → F4 preços/double-count → F3 Moka/temáticos → F5 dashboards.

## 2. ✅ FASE 0 — `telemetria_api.py` (helper universal)

**Arquivo:** `/root/telemetria_api.py` (novo, deployado no NYC; cópia local em `agentes_tematicos/telemetria_api.py`).

**Componentes:**
- `registrar_chamada_api(provider, modelo, tokens, agente, contexto, ...)` — ponto ÚNICO. Calcula custo via `gerenciador_tokens.calcular_custo()` (mesma `precos_modelos.json` canônica), escreve em `banco_custos` + `api_usage` com `corr_id` (uuid) e flag `contabilizado_em="telemetria_api"` (anti-double-count).
- `instrumentar(agente="...", contexto="...")` — **wrapper automático** de `requests.post` (e futuro openai). 1 linha no topo de scripts legados captura todas chamadas diretas sem refactor.
- Fail-open total (telemetria nunca derruba produção). Idempotente. Thread-safe (fcntl flock).

**Validação (self-test NYC):** deepseek-v4-flash 2000+500 tokens → custo `$0.00109` (bate tabela `$0.14/$0.28` por 1M). ✅

## 3. ✅ FASE 1 — Gap DeepSeek no roteador (VALIDADO)

**Problema:** `agente_roteador_llm.py` ramo DeepSeek (linha ~2003) chamava só `gerenciador_tokens.registrar_gasto()` (→ `banco_custos`), **nunca** `registrar_llm_openai_compatible()` (→ `api_usage`). Resultado: DeepSeek invisível no painel/watchlist.

**Correção aplicada:** após `registrar_gasto`, adicionar chamada `telemetria_api.registrar_chamada_api(provider="deepseek", ...)` com `extra={"origem": "roteador_ramo_deepseek"}`. Anti-double-count via flag `contabilizado_em`.

**Backup:** `/root/agente_roteador_llm.py.bak_pre_telemetria_fase1_20260802_1800`. `py_compile` OK.

**VALIDAÇÃO REAL (disparo via roteador, contexto economico):**
- ANTES: **0** registros DeepSeek no `api_usage`
- DEPOIS: **1** registro:
```json
{"provider": "deepseek", "modelo": "deepseek-v4-flash", "prompt_tokens": 2387,
 "completion_tokens": 12, "custo_usd": 0.000658, "contabilizado_em": "telemetria_api",
 "corr_id": "342dbd7e8cd9", "extra": {"origem": "roteador_ramo_deepseek"}}
```
**O mistério do "DeepSeek $0" está resolvido na origem.** Daqui pra frente, toda chamada DeepSeek (via roteador) aparece no painel com custo real e `corr_id` pra cruzar com `log_rotas_llm`.

## 4. Arquitetura resultante (após F0+F1)

```
Chamada API (roteador central)
   ↓
agente_roteador_llm.py
   ├─ registrar_gasto()      → banco_custos.jsonl   (fonte canônica custo)
   └─ telemetria_api         → api_usage.jsonl      (NOVO — gap fechado p/ deepseek)
        ↓
        └─ corr_id (uuid) liga custo ↔ rota ↔ latência
   ↓
coletar_custos_internos.py (cron 07h) consolida → custo_consolidados/{data}.json
   ↓
push_metricas_llm_completo.py (cron 07h) → Prometheus/ARMS Pequim
```

## 5. Fases pendentes

### FASE 2 — Top-15 scripts chamada direta (próxima)
Instrumentar (1 linha cada, com backup): `coletor.py`, `agente_comentarista.py` (legado), `agente_flavio_bolsonaro.py` (29 chamadas), `v4_media_expander.py`, `agente_escritor_scifi.py`+`_en.py`, `agente_novo_trends.py`, `agente_auditor_titulos_gpt.py`, `publish_caiado.py`, `revisor_titulo_luxo.py`, bots (`bot_augusto`, `bot_gabriel`, `miller_bot`, `bot_zizi_linda`, `bot_mayrag_v3`, `bot_secretaria`).

### FASE 4 — Preços + double-count + watchlist
- Preencher `precos_modelos.json`: ElevenLabs, Transkriptor, Kimi k2.6/k2.7/k3 nativos, GLM 5.2/4.7, qwen-vl-*
- Corrigir bug substring no `_precos_modelo` (chaves com `:` não casam)
- Anti-double-count no `coletar_custos_internos.py` (respeitar flag `contabilizado_em`)
- Expandir watchlist MVP1 p/ todos providers (hoje só zhipu/alibaba/brave)

### FASE 3 — Moka (Tencent) + Temáticos V4 locais
- Moka backend `/ia/completar`: adicionar `telemetria_api.registrar_chamada_api()` no FastAPI
- Temáticos V4 locais `nucleo_llm.py`: parar de descartar `usage`

### FASE 5 — Vigia + dashboard
- Vigia diário: alerta se gasto > $X/dia ou razão DeepSeek:Qwen inverter (sinal fallback caro)
- Alimentar painel `/v6/custos` com dados completos

## 6. Rollback

| Item | Comando |
|------|---------|
| FASE 1 (roteador) | `ssh nyc "cp /root/agente_roteador_llm.py.bak_pre_telemetria_fase1_20260802_1800 /root/agente_roteador_llm.py"` |
| FASE 0 (helper) | `ssh nyc "rm /root/telemetria_api.py"` (novo arquivo; remover desativa telemetria) |

## 7. Decisão pendente do Miguel

- **Continuar direto pras FASES 2-5**, ou **pausar e observar 24-48h** a FASE 1 funcionando em produção antes de avançar? (Recomendo observar um pouco — F1 já resolve o mistério principal; F2-5 são cobertura extra.)

— ZCode (GLM-5.2), 02/08/2026 ~18:00 BRT
