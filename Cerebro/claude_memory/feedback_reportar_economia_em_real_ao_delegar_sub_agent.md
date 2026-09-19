---
name: reportar-economia-em-real-ao-delegar-sub-agent
description: "Toda vez que Claude delegar tarefa pra sub-agent Sonnet/Haiku via Agent tool, deve reportar no chat com Miguel o custo de tokens da delegação e a economia estimada em REAIS (BRL) em relação ao que teria custado se rodasse tudo em Opus"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: f333da72-7610-439d-ab22-49569ae85b4a
---

**REGRA:** Toda delegação pra sub-agent Sonnet ou Haiku via Agent tool deve terminar com um bloco de transparência de custo:

```
💰 Delegação → <Modelo>: <total_tokens_subagent> tokens (~R$ X.XX)
   Se fosse Opus: ~R$ Y.YY
   Economia: R$ Z.ZZ (NN% mais barato)
```

**Tabela de preços (Anthropic pública, ~julho 2026):**

| Modelo | Input $/M tok | Output $/M tok | Razão input | Razão output |
|---|---:|---:|---:|---:|
| **Opus 4.7** | $15.00 | $75.00 | 1.00× | 1.00× |
| **Sonnet 4.6** | $3.00 | $15.00 | 0.20× | 0.20× |
| **Haiku 4.5** | $0.80 | $4.00 | 0.053× | 0.053× |

Câmbio USD → BRL: usar 5.00 como default (Miguel pode atualizar em memória se cotação mudar significativamente).

**Fórmula:**

```
# assumir mix 30% input / 70% output (padrão de respostas concisas)
# ou usar breakdown real se Agent tool retornar

custo_sub_agent_usd = (input_tokens * price_input + output_tokens * price_output) / 1_000_000
custo_opus_hipotetico_usd = (input_tokens * 15 + output_tokens * 75) / 1_000_000
economia_usd = custo_opus_hipotetico_usd - custo_sub_agent_usd

custo_brl = custo_sub_agent_usd * 5.00
custo_opus_brl = custo_opus_hipotetico_usd * 5.00
economia_brl = economia_usd * 5.00
percentual = (1 - custo_sub_agent_usd / custo_opus_hipotetico_usd) * 100
```

**Break-even:** delegação vale a pena se `custo_sub_agent + custo_overhead_opus < custo_opus_direto`. Pra tarefas < 500 tokens totais, overhead da delegação (meu prompt Opus pra anunciar + processar retorno, ~250-500 tokens) pode superar economia. **Regra prática:** delegar apenas tarefas com output esperado >1000 tokens OU tarefas repetitivas de padrão simples.

**Overhead de delegação a subtrair:**
- Meu prompt Opus pra anunciar delegação: ~50-100 tokens output → ~R$ 0.02-0.04
- Meu processamento do retorno + reporte pro Miguel: ~100-300 tokens output → ~R$ 0.04-0.11
- Overhead total típico: ~R$ 0.06-0.15 por delegação

**Report final:** subtrair overhead da economia bruta pra dar número honesto.

**Why:** Miguel 26/07 16:00 BRT (aprox): *"cada vez que você usar o SONNET ou usar o modelo inferior, o SONNET ou o HAIKU, você faz a estimativa de quanto você economizou. O custo da transição foi tantos tokens, mas a economia de tokens foi de tanto. calcula em real. A economia foi de tantos reais nessa operação em relação ao Opus."*

Contexto: teste 15:50 BRT tentou delegar Sonnet mas env vars da sessão (contaminadas pelo wrapper GLM `~/bin/glm`: `ANTHROPIC_DEFAULT_SONNET_MODEL=glm-5-turbo`) fizeram alias resolver pra modelo GLM inexistente → 404. Assim que essas env vars forem corrigidas pra `claude-sonnet-4-6` e `claude-haiku-4-5-20251001`, o teste anda e a economia começa a aparecer.

**How to apply:**
- Ao terminar QUALQUER Agent call com `model: sonnet|haiku`, ler `usage.total_tokens` retornado (ou estimar por breakdown)
- Rodar cálculo com fórmula acima
- Anexar bloco 💰 no final da minha resposta ao Miguel
- Se overhead > economia (tarefa curta): reportar honestamente ("Delegar aqui custou mais caro que Opus direto — regra: só delegar tarefas >1000 tokens")
- Manter contador acumulado por sessão? Opcional — se Miguel pedir, posso somar economia total do dia em uma mensagem de checkup

Regras irmãs: [[padrao-sentinela-escalada-haiku-sonnet-opus]] se existir (§6 do CEREBRO_NODE_ARQUITETURA), [[governanca-financeira-transparente]] (§16 Miguel 05/05).
