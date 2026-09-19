---
name: feedback-creditos-apis-primeiro-item-diagnostico-lentidao
description: "Miguel 16/06 ~04:55 BRT — quando há sintoma sistêmico de lentidão/timeout no Cafezinho LEGADO, SEMPRE verificar PRIMEIRO se há esgotamento de créditos em APIs LLM (Gemini, xAI, OpenAI, Anthropic, Brave, etc) antes de investigar hipóteses arquiteturais profundas. Caso fundador: 16/06 AGY perdeu 1h mapeando JSON gigante/I-O/disco/locks até descobrir que era Gemini-2.5 com créditos esgotados (HTTP 429 desde 15/06) + bug DeepSeek nomes inválidos. Lição: cota financeira é o item #1 do diagnóstico de lentidão sistêmica, não o item #10."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 83feb640-dee1-483b-9372-162a5be7876e
---

# Créditos de APIs LLM = item #1 do diagnóstico de lentidão sistêmica

Miguel 16/06 ~04:55 BRT:

> "seria muito mais fácil e rápido se a Trindade me informasse mais rapidamente que era problema de crédito no Gemini."

## A regra

**Quando há sintoma sistêmico de lentidão/timeout no Cafezinho LEGADO (timeouts repetidos no `maestro.log`, agentes morrendo silenciosamente, "publicou=não cota preservada" em série), a Trindade DEVE verificar PRIMEIRO os créditos/status das APIs LLM antes de investigar hipóteses arquiteturais profundas.**

Ordem recomendada de diagnóstico (do mais barato pro mais caro):

1. 🔴 **Créditos APIs LLM** (Gemini, xAI/Grok, OpenAI, Anthropic, DeepSeek, Moonshot, Qwen, Groq, Mistral, Perplexity)
   - Logs do circuit breaker: `/root/agent_data/llm_circuit_breaker_events.jsonl`
   - HTTP 429 = créditos esgotados
   - Painel de billing de cada provider
2. 🔴 **APIs externas saudáveis** (Brave Search, Ideogram, Aliyun, Flickr)
   - Mesmo princípio: créditos + status
3. 🟡 **Bug de configuração** (`llm_providers.json` com nomes inválidos)
4. 🟡 **Cascata sequencial mal-ordenada** (canais funcionais no final da fila)
5. 🟢 **Hipóteses arquiteturais profundas** (JSON gigante, I/O, locks, OOM, bugs de import) — só DEPOIS de descartar 1-4

## Por quê

Cota financeira é diagnóstico que custa segundos (ler 1 JSONL + acessar painel) vs hipóteses arquiteturais que custam horas (benchmarks, strace, py-spy, leitura de código).

No caso fundador 16/06:
- AGY entregou diagnóstico bom mas **gastou ~1h benchmarking JSON/I-O/disco/locks** primeiro
- Causa raiz era simples: **Gemini-2.5 com HTTP 429 desde 15/06** + bug DeepSeek `deepseek-v4-pro/flash` (nomes inexistentes na API)
- Se AGY (ou eu) tivesse aberto o `llm_circuit_breaker_events.jsonl` PRIMEIRO, teria visto o 429 e identificado a raiz em ~5min

## Como aplicar

### Em diagnóstico de lentidão sistêmica (LEGADO ou REFORMA)

Roteiro mínimo antes de qualquer hipótese arquitetural:

```bash
# 1. Verificar circuit breaker recente (últimos 24h)
ssh -i ~/.ssh/id_rsa -p 38422 ubuntu@43.156.151.165 \
  "sudo tail -100 /root/agent_data/llm_circuit_breaker_events.jsonl | grep -E '429|credits|depleted|exhausted'"

# 2. Listar providers com erros recentes (frequência)
ssh ... "sudo grep -oE 'HTTP [0-9]+' /root/agent_data/llm_circuit_breaker_events.jsonl | sort | uniq -c"

# 3. Verificar status_modelos.json se existir
ssh ... "sudo cat /root/agent_data/modelos_vivos.json 2>/dev/null | head -30"
```

### Em ticks §53 quando observar padrão de timeouts

Se notar 3+ timeouts seguidos no `maestro.log`, abrir circuit breaker IMEDIATAMENTE antes de seguir investigando código.

### Em proposta de AUTH

Quando propor AUTH pra "consertar lentidão", incluir SEMPRE um check de créditos APIs como Step 0 — explicitar que verificou.

### Em cartinha pros engenheiros (AGY/Codex/Kimi/GLM/DeepSeek)

Quando despachar investigação de lentidão, incluir como **primeira pergunta**:
> "Antes de qualquer outra hipótese, abra `/root/agent_data/llm_circuit_breaker_events.jsonl` e veja se há HTTP 429 / credits depleted nas últimas 24h."

Economiza horas de trabalho do engenheiro + da Trindade inteira.

## Caso fundador

**16/06 04:20 BRT** — Daemon (eu) escalou pro AGY mistério do `agente_ia.py` timeout silencioso com 10 hipóteses estruturadas (H1-H10). NENHUMA delas era "créditos esgotados".

**16/06 04:30 BRT** — AGY descartou 7 hipóteses empiricamente (JSON 33MB parse 0.5s, I/O 0.025s, locks limpos, disco 28GB livre, etc) e identificou H7 (APIs externas) com 3 sub-causas:
- Gemini-2.5 com HTTP 429 desde 15/06
- xAI Grok desligado por créditos
- Bug DeepSeek `deepseek-v4-pro/flash` (nomes inexistentes)

**16/06 04:50 BRT** — Miguel confirma que JÁ comprou crédito Gemini.

**16/06 04:55 BRT** — Miguel deixa lição:
> "seria muito mais fácil e rápido se a Trindade me informasse mais rapidamente que era problema de crédito no Gemini"

## Why

1. **Trindade é cara**: cada hora de engenheiro mapeando hipótese custa dólares e tempo do humano
2. **Créditos têm sinal explícito**: HTTP 429 é unambiguous, fácil de detectar
3. **Miguel é o único que pode resolver**: cota financeira é decisão de billing, não código — escalar pra ele rápido
4. **Sintoma 1 ≠ Causa 1**: lentidão sistêmica parece arquitetural mas frequentemente é financeira
5. **Padrão sistêmico**: 781 timeouts no `maestro.log` de hoje — todos provavelmente conectados a esse mesmo crédito esgotado

## Implicação pra Daemon (eu)

- Em qualquer escalação futura pra AGY/Codex/Kimi/GLM/DeepSeek sobre lentidão: **incluir Step 0 (verificar créditos APIs) explicitamente no roteiro**
- Em ticks §53: se observar padrão de 3+ timeouts, **abrir circuit breaker antes do tick seguinte**
- Em propostas de AUTH: **incluir status de créditos como pré-requisito de diagnóstico**
- Cartinha modelo: sempre começar "Antes de qualquer hipótese, abra `/root/agent_data/llm_circuit_breaker_events.jsonl`..."

Relacionados:
- [[feedback_grep_historico_log_sem_data]] (cruzar com logs datados)
- [[feedback_websearch_obrigatorio_producer_auditor_curador]] (EC2)
- [[feedback_hierarquia_trindade_claude_daemon_vivo]] (Daemon coordena diagnósticos)
- [[reference_reforma_arquitetura_produtor_unico_diretrizes_json]] (arquitetura REFORMA)
