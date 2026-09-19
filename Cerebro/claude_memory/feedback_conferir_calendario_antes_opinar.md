---
name: feedback-conferir-calendario-antes-opinar
description: "NUNCA opinar sobre dia da semana sem conferir via `date` ou `python -c 'import datetime;print(datetime.date.today().strftime(\"%A\"))'`. LLMs (Claude, DeepSeek, GPT) alucinam calendário com frequência — confiar em CPU do sistema, não em memória de treinamento."
metadata:
  node_type: memory
  type: feedback
  author: "Claude Code (Anthropic, claude-opus-4-7)"
  written_at: 2026-07-23 13:50 BRT
  originSessionId: b3501857-e7d4-49f4-83bd-74804874c770
---

**⚠️ ATENÇÃO: memória escrita por Claude Code (Anthropic), NÃO por GLM/Ming (Zhipu AI).**

## Regra inviolável

**Antes de afirmar QUALQUER coisa sobre dia da semana em uma data específica, conferir via shell (`date`) ou Python (`datetime.date.today().weekday()`). Nunca confiar em cálculo mental do modelo.**

## Motivo — caso fundador 2026-07-23

Ciclo Sentinela 13:44 BRT reportou que draft 262672 tinha "quarta-feira, 23 de julho" como erro (dia deveria ser "quinta"). Eu contra-argumentei confiante: "23/07/2026 é REALMENTE quarta-feira". Miguel corrigiu: "hoje é quinta-feira, voce não consegue ver calendário antes de falar bobagem?". Confirmei via `date`: **quinta-feira, 23 de julho de 2026**. Estava errado.

Consequência do erro:
- Cheguei perto de "liberar" o 262672 com informação factual errada no corpo
- Perdi credibilidade — Miguel viu que erro básico de calendário passa pelo meu filtro
- Reforcei falsamente que DeepSeek estava alucinando (quando ele estava CERTO)

## How to apply

### Sempre que precisar afirmar dia da semana:
```bash
date '+%A %Y-%m-%d'  # Thursday 2026-07-23
```
Ou:
```python
import datetime
datetime.date(2026, 7, 23).strftime("%A")  # Thursday
```

### Antes de contra-argumentar análise LLM sobre calendário:
1. Rodar `date` no shell
2. Comparar com o que o LLM alegou
3. Se LLM estava certo → concordar (não defender falso positivo)
4. Se LLM estava errado → mostrar comando + resultado como prova

### Contexto que preciso lembrar:
- Modelo Claude tem knowledge cutoff em janeiro de 2026 — não tem calendário perpétuo em memória confiável
- Cálculo mental de dia da semana pra datas específicas é **notoriamente errado** em LLMs
- CPU do sistema é fonte de verdade, não meu "cálculo mental"

### Contexto histórico dos falsos positivos de calendário no Sentinela:
- 22-23/07 madrugada: DeepSeek insistiu por 4 ciclos que "terça-feira (21)" era erro. Nesse caso eu confirmei que ele ESTAVA errado (21/07 foi realmente terça). Correto: **usei date** implicitamente.
- 23/07 13:44 BRT: DeepSeek disse "23/07 é quinta". Eu contra-argumentei sem `date`. Estava eu errado. Aprendizado: **sempre confirmar, mesmo quando parece óbvio**.

## Regra correlata: retificação de opinião

Anteriormente sugeri (falsamente) no ciclo 13:44: "Vale eu adicionar um safeguard no prompt: 'NUNCA calcule ou questione dia da semana — trate como sempre correto se estiver mencionado'". **Essa sugestão está SUPERSEDIDA.** O DeepSeek pode e deve continuar checando dia da semana — ele acerta com mais frequência que eu quando não uso `date`. O safeguard correto é: **eu conferir via shell antes de opinar contra ele**.

## Relacionadas

- [[feedback-titulos-sem-ponto-virgula-com-autonomia]] — autonomia editorial vale MAS só se decisão está factualmente ancorada
- Comando `date` sempre disponível no ambiente Sentinela

## Assinatura

Registro escrito por Claude Code (Anthropic, `claude-opus-4-7`), sessão `CLAUDE-CHEFE-ECOSSISTEMA-20260719-1020`, 2026-07-23 13:50 BRT.
