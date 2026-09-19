# FÓRUM — Plano: DeepSeek V4 Flash em coleta + curadoria (temáticos + V4 Cafezinho) — 01/08/2026

**Data:** 2026-08-01 ~17:30 BRT
**Autor:** ZCode (GLM-5.2), ordem direta do Miguel
**Status:** ⏸️ **PLANO PRONTO, deploy BLOQUEADO pelo saldo DeepSeek ($0,37)** — ativa quando Miguel recarregar.
**Memória irmã (diagnóstico técnico completo + pontos exatos de mudança):** `Memorias/memoria_deepseek_v4_flash_coleta_curadoria_plano_20260801.md`
**Doutrina aplicada:** "produção só muda com autorização explícita do Miguel por item + plano de rollback" (HISTORICO.md Kimi 29/07). Miguel autorizou por contexto: **coleta SIM, curadoria SIM, redação NÃO, auditoria NÃO**.

---

## 1. A ordem do Miguel (transcrição)

> "vamos usar geral o deep seek v4 flash nos temáticos, que é mais barato. e usar no v4 do cafezinho também onde for possível para economizar. mas não redação, não auditoria, coleta sim, curadoria sim."

**Matriz de permissão (autorização por contexto):**

| Contexto/Tarefa | DeepSeek V4 Flash? |
|-----------------|-------------------|
| **Coleta** (coleta/filtering bruto) | ✅ SIM |
| **Curadoria** (scoring/curadoria rápida) | ✅ SIM |
| Redação (luxo/editorial) | ❌ NÃO |
| Auditoria | ❌ NÃO |
| Revisão | ❌ NÃO (não mencionado → manter) |

## 2. Por que DeepSeek V4 Flash é a escolha certa

Do `CEREBRO_NODE_CATALOGO_MODELOS_LLM.md`:
- **Preço:** $0,14/1M input · $0,28/1M output (vs `deepseek-v4-pro` $0,44/$0,87; vs `qwen-plus` $0,26/$0,78)
- **Contexto:** 1M tokens
- **Reasoning:** Não (rápido, sem inflar tokens)
- **Notas:** Q2 P5 V5 — "Ativo — periféricos simples apenas" (coleta/curadoria = periférico simples, encaixa perfeito)
- **Prova de viabilidade:** `agente_produtor_bella_ciao.py` **já usa `deepseek-v4-flash` direto** em produção.

## 3. 🚫 BLOQUEADOR — Saldo DeepSeek $0,37

Medido ao vivo no cofre de produção NYC (~17:25 BRT):
```
DeepSeek total_balance: $0.37
```
- `deepseek-chat` responde HTTP 200 (ainda funciona), mas $0,37 é **insuficiente** para coleta+curadoria de 8 temáticos + V4 (alto volume: centenas de chamadas/dia).
- Estimativa: $0,37 dura **poucas horas** sob carga de coleta → **production down**.
- Histórico: fórum de hoje já registrava $1,20 às 15:05 + circuit breaker `deepseek-v4-pro quota_exhausted` às 13:52 → consumo real em andamento.

**Decisão técnica (melhor julgamento, Miguel não respondeu às perguntas):** NÃO deployar agora. Preparar tudo pronto pra ativar em 1 comando quando o saldo entrar.

## 4. Pontos exatos de mudança (pré-mapeados, sem tocar ainda)

### A. `motor_coletor.py` (curadoria rápida da coleta) — PRINCIPAL
- **Linha 250:** `gerar_texto_governado(tarefa="scoring", ...)` → é a curadoria/filtro da coleta.
- **Mudança:** forçar `deepseek-v4-flash` como modelo primário no contexto/tarefa `scoring` do roteador.
- **Impacto:** todos os temáticos que usam `motor_coletor` (herdam).

### B. `agente_roteador_llm.py` + `llm_context_routes.json` — onde `scoring` resolve modelo
- `llm_context_routes.json` **não tem** contexto `scoring` explícito (contextos atuais: luxo, padrao, economico, revisor, auditor, comentario_site...). O `gerar_texto_governado(tarefa="scoring")` provavelmente cai num tier default.
- **Mudança:** adicionar/ajustar o mapeamento `scoring` → `deepseek_economico` (que aponta pra v4-flash) no roteador, OU criar contexto `scoring` no JSON.

### C. Curadores diretos (revisar caso a caso)
- `agente_curadoria.py`, `agente_curadoria_gsn.py`, `agente_curador_fontes.py`, `agente_curador_midia.py`, `refresh_curadoria.py` — alguns chamam `gerar_texto` sem contexto explícito (caem no default). Avaliar 1 a 1 no deploy.

### D. V4 Cafezinho (orquestrador temático)
- Confirmar qual tarefa/contexto a curadoria V4 passa ao roteador. Herda de motor_coletor se for o caso.

## 5. Matriz de escopo (decidir no deploy)

| Portal | Coleta | Curadoria | Redação | Auditoria |
|--------|--------|-----------|---------|-----------|
| 8 Temáticos (Rio Carta, GSN, Mundo Trilhos...) | ✅ DS-v4-flash | ✅ DS-v4-flash | mantém | mantém |
| V4 Cafezinho | ✅ DS-v4-flash | ✅ DS-v4-flash | mantém (gpt-5.5 etc) | mantém |

## 6. Plano de execução (QUANDO recarregar)

**Pré-condição:** saldo DeepSeek ≥ $5 (confirmar ao vivo antes).

1. **Backup:** `agente_roteador_llm.py`, `llm_context_routes.json`, `motor_coletor.py` → `.bak_pre_dsflash_<ts>` no NYC.
2. **Mudança A (roteador):** mapear `scoring`/curadoria → `deepseek_economico` (v4-flash) em `llm_context_routes.json`.
3. **Mudança B (motor_coletor):** confirmar tarefa `scoring` no `gerar_texto_governado` resolve pra v4-flash.
4. **Smoke isolado:** 1 chamada `curadoria_llm_rapida()` com payload de teste → confirmar responde via v4-flash.
5. **Observação:** 1 ciclo V4 + 1 ciclo de 1 temático → confirmar custo caiu, zero erros.
6. **Rollback (1 comando):** restaurar `.bak_pre_dsflash_<ts>` dos 3 arquivos.

## 7. Decisões pendentes de Miguel

1. **Recarregar DeepSeek** (platform.deepseek.com → Add Funds). Quanto? Sugestão: $10-20 pra validar.
2. **Confirmar saldo ≥ $5** comigo antes de eu ativar.
3. **Escopo:** temáticos + V4 (todos) ou piloto em 1 portal primeiro?
4. (Opcional) Definir teto de gasto diário DeepSeek pra evitar nova exaustão.

— ZCode (GLM-5.2), 01/08/2026 ~17:30 BRT
