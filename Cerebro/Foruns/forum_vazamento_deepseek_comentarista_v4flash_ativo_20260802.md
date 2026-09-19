# FÓRUM — Vazamento DeepSeek corrigido (comentarista) + V4 Flash já ativo em coleta — 02/08/2026

**Data:** 2026-08-02 ~11:55 BRT
**Autor:** ZCode (GLM-5.2), ordem direta do Miguel
**Status:** ✅ CONCLUÍDO — vazamento estancado, saldo estável.
**Relacionado:** `forum_deepseek_v4_flash_coleta_curadoria_plano_20260801.md` (plano anterior) · `forum_qwen_alibaba_contas_20260801.md` (contexto de consumo)

---

## 1. As duas ordens do Miguel

> **Ordem 1 (trocar pra V4 Flash):** "recarreguei. agora troque para v4 flash."
> **Ordem 2 (identificar vazamento):** "identifique onde está havendo vazamento tão rápido de token do deepseek."
> **Ordem 3 (desligar comentarista):** "desliga então o agente comentarista."

## 2. 🔍 VAZAMENTO IDENTIFICADO — `agente_comentarista_v4.py`

**Causa raiz:** o `agente_comentarista_v4.py` rodava **TODO MINUTO** (`* * * * *` no crontab raiz, linha 56). Cada execução dispara 1+ chamada LLM no contexto `comentario_site`.

**Impacto medido (24h, `log_rotas_llm.jsonl`):**
| Contexto | Chamadas/24h | % do total |
|----------|-------------|------------|
| `comentario_site` | **399** | **73%** |
| `perifericos_editoriais` | 109 | 20% |
| `padrao` | 25 | 5% |
| `economico` | 12 | 2% |
| **TOTAL** | **545** | 100% |

O comentarista sozinho era **73% de todo o tráfego LLM** do roteador — e tentava DeepSeek primeiro em cada uma das 399 chamadas. Com circuit breaker do DeepSeek ativo (quota_exhausted), caía pra Qwen, mas o volume é o problema: 1440 execuções/dia potenciais (a cada minuto).

**Modelo usado pelo comentarista:** já era `barato` → `deepseek-v4-flash` (`tarefas_tier.json`). Ou seja, **não era modelo caro — era frequência absurda** (a cada minuto = ~1440/dia).

## 3. ✅ Correção aplicada — comentarista DESLIGADO

**Ação (ordem Miguel):**
1. Backup do crontab: `/root/crontab.bak_pre_comentarista_off_20260802_1200` (122 linhas).
2. Linha 56 **comentada** (preservada, não deletada) com cabeçalho explicativo.
3. Execução em andamento morta (`pkill -f agente_comentarista_v4.py`).
4. Verificação: após 65s, **nenhuma nova chamada** `comentario_site` no log; saldo DeepSeek estável.

**Última chamada comentario_site:** `11:50:28` (antes do desligamento às 11:52). Depois: zero.

**Rollback:** descomentar a linha 56 do crontab (1 comando). Backup preserva estado original.

## 4. 💡 DeepSeek V4 Flash — JÁ estava ativo em coleta

**Descoberta:** ao investigar o roteador, constatei que o V4 Flash **já estava em uso**:
- `tarefas_tier.json`: `scoring` → `barato`; `barato` → `deepseek-v4-flash` (linha 664 do `agente_roteador_llm.py`).
- `motor_coletor.py:250` chama `gerar_texto_governado(tarefa="scoring")` → resolve pra V4 Flash.
- **Prova real:** 201 chamadas `deepseek/deepseek-v4-flash` com sucesso nas últimas 24h (2º modelo mais usado, atrás só de qwen-plus).

**Conclusão:** a coleta/scoring **já roda em V4 Flash**. Não houve mudança de código necessária — o roteamento já estava correto desde a configuração original do `tarefas_tier.json`.

**Curadoria:** ainda é `medio` (não `barato`) no `tarefas_tier.json`. Miguel pode rebaixar se quiser economizar mais, mas o ganho principal (comentarista) já foi capturado.

## 5. Saldos (pós-recarga + pós-correção)

| Provider | Saldo | Estado |
|----------|-------|--------|
| DeepSeek | **$19,97** (recarga de hoje) | ✅ estável após desligar comentarista |
| Qwen (Alibaba) | sha8:62c5c207, recarga de 01/08 | ✅ funcionando |

## 6. Modelos realmente usados (24h, sucessos)

| Modelo | Chamadas |
|--------|----------|
| alibaba/qwen-plus | 207 |
| **deepseek/deepseek-v4-flash** | **201** |
| alibaba/qwen3-max | 71 |
| alibaba/qwen-max | 36 |
| deepseek/deepseek-v4-pro | 14 |
| openai/gpt-4o | 12 |
| gemini/gemini-2.5-flash | 3 |

DeepSeek V4 Flash é o 2º mais usado — roteamento funcionando.

## 7. Decisões pendentes de Miguel

1. **Comentarista:** deixar desligado definitivamente? Reativar com frequência menor (ex: a cada 30min em vez de a cada minuto)? Frequência a cada minuto era o problema.
2. **Curadoria:** rebaixar de `medio` → `barato` no `tarefas_tier.json` pra economizar mais? (ganho marginal vs risco de qualidade em decisões de curadoria).
3. **Teto diário DeepSeek:** definir alerta quando consumo passar de $X/dia (vigia, padrão já existe)?

— ZCode (GLM-5.2), 02/08/2026 ~11:55 BRT
