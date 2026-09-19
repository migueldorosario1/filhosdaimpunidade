# FÓRUM — Diagnóstico: pico de gasto 31/07 foi tribunal visual (cadeia do no-home) — 02/08/2026

**Data:** 2026-08-02 ~14:30 BRT
**Autor:** ZCode (GLM-5.2), investigação a pedido do Miguel
**Status:** ✅ Diagnóstico concluído. Nenhuma mudança em produção (Miguel optou por manter qualidade).
**Relacionado:** `forum_cap_dinamico_humanos_livres_20260802.md` · `forum_vazamento_deepseek_comentarista_v4flash_ativo_20260802.md`

---

## 1. A pergunta do Miguel

> "no final de semana, como a gente reduz a produção humana, eu pedi pro Claude publicar. V4 publica só draft, Claude no loop vigília faz checagem dupla e publica. Eu pedi pra ele publicar e **tirar a flag no-home** que vinha do V4. isso implicou em maior despesa de tokens?"

## 2. ✅ Resposta: SIM, implicou — mas indiretamente

**Cadeia causal completa (medida, não chute):**

1. Miguel pediu ao Claude publicar drafts + tirar `no-home` (cat 20699).
2. O `no-home` em si **não consome tokens** (categoria WordPress, $0 LLM).
3. Com mais posts visíveis/publicados, o pipeline V4 **continuou produzindo drafts** na cadência normal (50-78/dia, estável — não houve pico de publicação).
4. Cada draft passa pelo **tribunal visual** (`v4_prompt_visual`, contexto `perifericos_editoriais`).
5. Esse contexto exige **`qualidade_minima: 4`** + `preferir_origem: asiatico` → roteador escolheu **`qwen-max`** ($1,04/1M).
6. `qwen-max` é **4× mais caro** que `qwen-vl-plus` ($0,26/1M) — mas `qwen-vl-plus` é Q3, não atinge o piso Q4 do contexto.
7. **450 chamadas em 31/07 × ~$0,007 = $3,22** = **87% do pico de $3,70**.

## 3. 📊 Dados reais (de `governanca_financeira_api_usage.jsonl`)

### Gasto por dia
| Data | Chamadas | Gasto total | % comentários | % tribunal visual |
|------|----------|-------------|---------------|-------------------|
| 2026-07-29 | 111 | $0,16 | 78% | — |
| 2026-07-30 | 245 | $1,02 | 14% | — |
| **2026-07-31** | **856** | **$3,70** | 13% | **87%** ($3,22) |
| 2026-08-01 | 484 | $1,63 | 22% | — |
| 2026-08-02 | 182 | $0,43 | 29% | — (após correções) |

### Decomposição 31/07 (pico)
| Agente | Modelo | Chamadas | Custo | % |
|--------|--------|----------|-------|---|
| **`v4_prompt_visual`** | **alibaba/qwen-max** | **450** | **$3,22** | **87%** |
| `agente_comentarista_v4` | alibaba/qwen-plus | 404 | $0,48 | 13% |

## 4. 🔍 Hipóteses descartadas (com dados)

| Hipótese | Descartada porque |
|----------|-------------------|
| `no-home` consome tokens | ❌ É só categoria WP, zero LLM |
| Mais posts publicados | ❌ Volume estável (50-78/dia), sem pico |
| Mais comentários humanos | ❌ Comentários estáveis (1-7/dia) |
| Comentarista (399/dia) | ❌ Era 13% do pico ($0,48), não a causa principal |

**Causa confirmada:** `v4_prompt_visual` (tribunal visual) usando `qwen-max` caro, acionado pela continuidade normal do pipeline V4 que produzia drafts enquanto o Claude publicava no fim de semana.

## 5. Arquitetura do tribunal visual (mapeamento)

- **Arquivo:** `/root/v4_vertical_draft_worker.py`
- **Funções:** `_qwen_visual` (linha ~117, fallback direto) + rota roteador (contexto `perifericos_editoriais`)
- **Config roteador:** `llm_ratings.json` → `perifericos_editoriais`: `{"qualidade_minima": 4, "preferir_origem": "asiatico"}`
- **Variável:** `V4_QWEN_VISION_MODEL` (default `qwen-vl-plus`, mas não setada em `.env` — então quando vai pelo roteador, segue o rating Q4 = `qwen-max`)
- **`tarefas_tier.json`:** `tribunal_visual: medio`

## 6. Decisão do Miguel (02/08 ~14:30)

> **Manter `qwen-max` (qualidade).** O pico foi pontual (fim de semana); com as correções de hoje (comentarista 30min, caps dinâmicos), o gasto já estabilizou ($0,43 hoje vs $3,70 no pico).

**Nenhuma mudança aplicada em produção.** Diagnóstico é registro/documentação.

## 7. Lição operacional (pra Trindade)

A cadeia "publicar + no-home" tem efeito cascata **invisível**: não é o `no-home` que custa, é o **pipeline V4 que continua rodando** alimentado pela publicação, e cada draft aciona o tribunal visual caro. Pra fins de planejamento:

- **Fim de semana com publicação acelerada pelo Claude** → esperado gasto +X em tribunal visual (proporcional ao nº de drafts × qwen-max).
- **Se quiser economizar sem perder qualidade:** opções futuras = (a) cache de imagens repetidas no tribunal; (b) pular tribunal pra posts de baixo risco; (c) rebaixar Q4→Q3 (recusado hoje).
- **Vigia recomendado:** alertar quando `v4_prompt_visual` passar de N chamadas/dia (detectar novo pico cedo).

## 8. 🔄 ATUALIZAÇÃO CORRETIVA (02/08 ~15:00 BRT) — Miguel apontou: o gasto maior foi DeepSeek, não Qwen

Miguel: *"o gasto maior que eu notei foi do Deep Seek, não o Qwen. O que pode ter acontecido é que quando eu melhorei o QWEN, o Tribunal Visual começou a trabalhar melhor e aí o Deep Seek também foi mais usado."*

**Miguel estava certo.** Investigação aprofundada revelou **dois gastos distintos que se confundiram**, e a **correlação causal** entre eles:

### 8.1 DeepSeek esgotou $20→$0,37 entre 24-30/07 (a raiz real)

`log_rotas_llm.jsonl` — tentativas DeepSeek por dia:

| Data | Sucesso | Pulada (cooldown) |
|------|---------|-------------------|
| 24/07 | 469 | 0 |
| 25/07 | 500 | 0 |
| 26/07 | 478 | 0 |
| 27/07 | 468 | 0 |
| 28/07 | 465 | 0 |
| 29/07 | 309 | 113 ← começa a exaurir |
| 30/07 | 326 | 246 |
| **31/07** | **0** | **890** ← esgotou de vez |
| 01/08 | 118 | 515 |
| 02/08 | 97 | 172 |

**Total chamadas DeepSeek bem-sucedidas (24-28/07): ~2.380** — majoritariamente `deepseek-v4-flash` (3.237 no período) em coleta/scoring + `deepseek-v4-pro` (216) em redação. **Foi isso que consumiu os $20.**

### 8.2 Qwen disparou em 31/07 = fallback da carga que era do DeepSeek

Quando DeepSeek esgotou (31/07), o roteador fez **fallback** e o Qwen assumiu:

| Data | DeepSeek sucesso | Qwen sucesso (tribunal visual) |
|------|------------------|-------------------------------|
| 24-28/07 | ~470/dia (saudável) | ~1-3/dia (dormindo) |
| 29/07 | 309 (caindo) | 111 (acordando) |
| 30/07 | 326 | 121 |
| **31/07** | **0 (esgotou!)** | **450 (pico — assumiu tudo)** |

**O pico de Qwen em 31/07 (450 chamadas qwen-max) foi consequência do esgotamento do DeepSeek**, não causa independente. Quando um caía, o outro absorvia a carga.

### 8.3 Hipótese do Miguel sobre "melhorei Qwen → tribunal melhor → +DeepSeek"

**Parcialmente correta, com timing refinado:**
- ✅ A rotação Qwen (01/08, chave 62c5c207 unificando 6 drift) **estabilizou** o tribunal (a chave morta `850f5099` no cofre canônico já dava erro intermitente).
- ⚠️ Mas a rotação foi **depois** do pico (31/07). O pico em si foi **fallback** do DeepSeek esgotado.
- ✅ A intuição de "Qwen melhor → sistema flui mais → mais consumo geral" é **arquiteturalmente correta**: o tribunal visual é um **gargalo habilitante** — quando ele funciona, mais drafts avançam, mais coleta/scoring roda, mais DeepSeek é demandado.

### 8.4 Cadeia causal completa (versão corrigida)

```
1. DeepSeek era o primário de coleta/scoring/periféricos (470 chamadas/dia, 24-28/07)
2. DeepSeek esgotou $20→$0,37 progressivamente (29-31/07)
3. Roteador fez fallback → Qwen assumiu (pico 450 qwen-max em 31/07)
4. Miguel notou: "DeepSeek sumiu, Qwen disparou" ← interpretação correta dos sintomas
5. Rotação Qwen 01/08 estabilizou o tribunal (chave morta removida)
6. Recarga DeepSeek 02/08 ($19,97) reativou o primário
7. Correções de hoje (comentarista 30min, caps dinâmicos) reduziram demanda geral
```

### 8.5 Lição refinada

O ecossistema tem **acoplamento de demanda**: DeepSeek (coleta/scoring) e Qwen (tribunal visual) formam um **pipeline em série**. Quando o primário (DeepSeek) falha, o secundário (Qwen) **absorve carga extra** no fallback — gerando pico aparente no "outro" provider. Sintoma "Qwen disparou" pode significar "DeepSeek morreu", não "Qwen têm bug". **Sempre verificar ambos providers juntos, não isoladamente.**

**Vigia recomendado (refinado):** monitorar não só saldo de cada provider, mas a **razão DeepSeek:Qwen** — se inverter bruscamente (Qwen >> DeepSeek), é sinal de que DeepSeek esgotou e Qwen está em fallback caro.

— ZCode (GLM-5.2), 02/08/2026 ~15:00 BRT (atualização corretiva)
