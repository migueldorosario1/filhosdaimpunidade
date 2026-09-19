# FÓRUM — Seletor de LLM Inteligente + Assinatura + Telemetria Prometheus (princípio arquitetural do ecossistema) — 12/08/2026

**Data:** 2026-08-12 ~19:55 BRT
**Autor:** ZCode (GLM-5.2, Z.ai coding plan — fallback final; Kimi/Qwen 🔴🔴)
**Status:** 🟡 DESIGN/princípio (para codar no momento certo). Sem código nesta fase.
**Origem:** ordem Miguel — *"qq que seja a llm que a gente use, não pode ser hardcode, precisa assinar o que faz, ter telemetria rigorosa, prometheus. inclusive podiamos ter um seletor de llms inteligente, que olhasse o preço, visse o ranking de qualidade, e escolhesse de acordo com uma nota média de qualidade e preço. anota isso num forum."*
**Relacionado:** `forum_arquitetura_curadoria_manchete_estavel_20260812.md` · `forum_moka_agente_precos_llm_20260809.md` · `CEREBRO_NODE_TELEMETRIA.md` · `CEREBRO_NODE_CATALOGO_MODELOS_LLM.md` · `CEREBRO_NODE_CHAVES_E_LLMS.md`

---

## 0. Por que existe (o problema de fundo)

Hoje a escolha de LLM no ecossistema é **hardcoded por papel** (`luxo`/`economico`/`padrao`/`revisor`/`comentarista` no `agente_roteador_llm.py`) e os ratings (`llm_ratings.json`) são **mantidos à mão**. O `atualizador_precos_llm.py` gera preços frescos, **mas nenhum roteador os consome**. Resultado: não há seleção dinâmica por custo-benefício, não há assinatura/auditabilidade da decisão, e a telemetria de LLM é parcial. O Miguel quer **elevar isso a princípio**: nenhuma chamada LLM é "mágica" — toda decisão é **assinada, justificada e telemetrada**.

## 1. Princípios (não-negociáveis, do Miguel)

1. **Zero hardcode de modelo em tarefa.** Nenhum agente escreve `modelo = "deepseek-v4-flash"` no código. Todo agente pede uma **função/capacidade** (ex.: "avaliar manchete política", "gerar comentário curto"), e o **seletor** decide o modelo.
2. **Assinatura obrigatória.** Toda chamada LLM registra **quem chamou, qual modelo, qual versão, qual tarefa, qual motivo da escolha, tokens, custo, latência, resultado**. Registro **imutável e auditável** (log/append).
3. **Telemetria rigorosa (Prometheus).** Métricas de cada chamada expostas no Prometheus existente (Alibaba) — custo, latência, taxa de erro, taxa de uso por modelo, qualidade reportada.
4. **Decisão = função(qualidade, preço).** O seletor escolhe por uma **nota média de custo-benefício**, olhando preço (do agente de preços) + ranking de qualidade.

## 2. O Seletor de LLM Inteligente (núcleo)

**Função:** `escolher_modelo(capacidade, contexto) → {modelo, motivo, score}`

### 2.1 Nota de custo-benefício (score composto)
Para cada modelo elegível à capacidade, num instante:
```
score = w_q * normaliza(qualidade)  +  w_p * normaliza_inversa(preco)  +  w_s * saldo_disponivel
```
- **qualidade** (0-100): ranking de qualidade (ver §3).
- **preço** (inverso): preço real do `ranking_llm.json` (ajustado ao tamanho esperado da tarefa).
- **saldo_disponível**: se o modelo está com crédito/saldo agora (vigília de crédito já existe: Kimi/Qwen esgotam em janelas 5h). **Modelo sem saldo = score 0.**
- Pesos `w_q`, `w_p`, `w_s` configuráveis por capacidade (ex.: curadoria → qualidade pesa mais; comentário filler → preço pesa mais).

### 2.2 Capacidades (não modelos)
O agente pede a **capacidade**, não o modelo. Ex.: `curadoria_manchete`, `comentario_seed`, `comentario_resposta_humano`, `redacao_rascunho`, `revisao`, `titulos`, `classificacao_binaria`. Cada capacidade tem pesos próprios (qualidade vs preço) e um conjunto de modelos elegíveis.

## 3. Fontes de dados (as 3 vigas)

| Fonte | O que dá | Estado | Lacuna |
|---|---|---|---|
| **`atualizador_precos_llm.py`** → `ranking_llm.json` | **preço** (input/output USD+BRL), atualização diária | 🟡 escrito, **deploy pendente** (cron Tencent) | ligar ao seletor |
| **ranking de qualidade** | **qualidade** (0-100) por modelo/capacidade | 🔴 não existe unificada | **criar** (benchmarks + ratings internos + LLM-as-judge) |
| **vigília de crédito/saldo** (`credito_vigilia.py`) | **saldo disponível** agora (janela 5h Kimi/Qwen, etc.) | 🟢 existe (hook + estado) | expor pro seletor |

### 3.1 Ranking de qualidade — como medir (decidir)
- **(a) Benchmarks públicos** (MMLU, GPQA, etc.) — estáticos, genéricos.
- **(b) Ratings internos** (`llm_ratings.json` já tem `qualidade` S/A/B + `economia`) — base histórica do Cafezinho.
- **(c) LLM-as-judge contínuo** — o `agente_validador_modelos.py` (já no cron) pode alimentar notas de qualidade por tarefa ao longo do tempo.
- **(d) Feedback humano** (Miguel curando) — sinal de ouro, esporádico.
- Proposta: **combinar b+c+d**, com (c) atualizando continuamente e (d) recalibrando.

## 4. Assinatura (schema do registro de cada chamada LLM)

Append-only (JSONL), uma linha por chamada:
```json
{
  "ts": "2026-08-12T19:55:00-03:00",
  "agente": "scorer_manchete_llm",
  "capacidade": "curadoria_manchete",
  "modelo": "deepseek-v4", "versao": "...", "provider": "deepseek",
  "motivo_escolha": "score=0.87 (q=0.9,p=0.8,saldo=ok); top1 entre 5",
  "tokens_in": 312, "tokens_out": 88,
  "custo_usd": 0.00012, "latencia_ms": 1840,
  "ok": true, "erro": null,
  "resultado_hash": "sha8:...",   // hash do output (p/ auditoria sem vazar conteúdo)
  "meta": {"post_id": 265426, "nota": 720}  // específico da tarefa
}
```
> **Regra do Cofre:** o registro guarda **hash** do conteúdo (não o texto), salvo necessidade de debug (com TTL de expurgo). Tokens/custo são sempre registrados.

## 5. Telemetria Prometheus (métricas a expor)

| Métrica | Tipo | Labels |
|---|---|---|
| `llm_chamadas_total` | counter | `agente`, `capacidade`, `modelo`, `ok` |
| `llm_tokens_total` | counter | `modelo`, `direcao`(in/out) |
| `llm_custo_usd_total` | counter | `modelo`, `capacidade` |
| `llm_latencia_ms` | histogram | `modelo`, `capacidade` |
| `llm_modelo_score` | gauge | `modelo`, `capacidade` (score de custo-benefício atual) |
| `llm_modelo_saldo_ok` | gauge | `modelo` (1/0 da vigília) |
| `llm_qualidade_reportada` | histogram | `modelo`, `capacidade` |

Infra: já há Prometheus no Alibaba (`CEREBRO_NODE_TELEMETRIA.md`) e `push_metricas_llm_completo.py` (no cron). **Estender** com essas métricas. Painel: custo/dia por modelo/capacidade, ranking de custo-benefício ao vivo, alertas (modelo sem saldo, custo alto).

## 6. Arquitetura integrada (alvo)

```
┌─ atualizador_precos_llm.py (cron diário Tencent) ── preço ─┐
├─ ranking_qualidade (ratings + validador + juiz + humano) ── qualidade ─┤
├─ credito_vigilia.py ── saldo ─┤
│                                                              ▼
│   ╔═════════════════════════════════════════╗
│   ║  SELETOR DE LLM INTELIGENTE (novo)      ║   escolhe modelo por
│   ║  escolher_modelo(capacidade, contexto)  ║   nota média qualidade+preço
│   ╚═════════════════════════════════════════╝
│              │  + ASSINATURA (registro imutável)  +  TELEMETRIA Prometheus
│              ▼
│   todos os agentes (curadoria manchete, comentarista, redação, revisão, títulos...)
```

## 7. Como a curadoria da manchete se encaixa

O `scorer_manchete_llm.py` (o juiz da manchete) **não escolhe modelo** — ele pede a capacidade `curadoria_manchete` ao seletor, que retorna o modelo de melhor custo-benefício **naquele instante** (considerando saldo). Toda chamada é assinada + telemetrada. Se DeepSeek cair, o seletor pula pro próximo (Gemini/Qwen) automaticamente. **Zero hardcode.**

## 8. Lacunas / pendências (pra codar no momento certo)

1. **Criar o `ranking_qualidade` unificado** (hoje não existe) — combinar ratings + validador + juiz + humano.
2. **Deploy do `atualizador_precos_llm.py`** na Tencent (cron diário) — ainda pendente.
3. **Ligar as 3 fontes** (preço + qualidade + saldo) ao seletor novo.
4. **Implementar o seletor** (`escolher_modelo`) + **assinatura** (JSONL append) + **métricas Prometheus**.
5. **Refatorar agentes** pra pedirem capacidade (não modelo) — migração incremental (começar pelo scorer da manchete + comentarista).
6. **Decidir pesos** (`w_q/w_p/w_s`) por capacidade — calibrar com dados reais.

## 9. Próximos passos (quando for o "momento certo")

1. Aprovar este design + decidir a fórmula da nota de custo-benefício.
2. Sprint 1: deploy agente de preços + ranking de qualidade v1 (ratings+validador) + seletor mínimo + assinatura.
3. Sprint 2: telemetria Prometheus completa + painel + alertas.
4. Sprint 3: migrar agentes pra "pedir capacidade" (curadoria e comentarista primeiro).
5. Catalogar Tema Duplo (fórum + memória) quando implementado.

---

— **ZCode (GLM-5.2, Z.ai coding plan)**, 12/08/2026 ~19:55 BRT
