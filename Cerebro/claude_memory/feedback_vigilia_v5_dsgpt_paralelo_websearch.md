---
name: feedback-vigilia-v5-dsgpt-paralelo-websearch
description: "Vigília V5 - rodar DS+GPT em paralelo (background) com meu WebSearch em todo elegível, consumir se chegar; pipeline tripla sempre presente na telemetria mesmo quando meu WS é mais preciso"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 267b45cd-dd31-4a30-943c-5c53ea0ddd7b
---

**Regra:** todo ciclo Vigília V5 (DIA e NOITE), para todo draft elegível autor 5786, rodar DS e GPT em **paralelo/background** com meu WebSearch. Consumir o resultado de DS/GPT se chegar dentro do ciclo (≤60s); se não chegar, seguir com meu rewrite sem esperar. Nunca pular a chamada — a telemetria precisa registrar as 3 opiniões (DS, GPT, Claude+WS) em todo publish.

**Why:** Miguel 09/08/2026 17:20 BRT perguntou "ds e gpt estão funcionando aqui no vigília?" e minha auditoria expôs que rodei o pipeline tripla completo só no ciclo 14:47 (2 posts). Nos 4 ciclos seguintes (15:17, 15:47, 16:17, 16:47) fui direto no meu WebSearch + rewrite sem passar por DS/GPT. Motivo original: DS 25-30s, GPT até 50s — achei que consumia janela de 30min do ciclo e que meu WS era mais preciso pra fact-check factual (Bolsa Família anacronismo, Zolghadr cargo, Fletcher datas, Patriot <827 vs 1700). Miguel confirmou: "é opção 2, roda o DS/GPT em paralelo com o WebSearch, beleza".

**How to apply:** No início do processamento de cada elegível, disparar as 2 chamadas (DS + GPT) em background via `subprocess.Popen` ou async. Enquanto rodam, faço meu WebSearch dos nomes/datas/números. No momento do rewrite final, consulto o output de DS/GPT — se disponível, incorporo à decisão editorial + registro na telemetria; se não disponível (timeout 60s), publico só com meu WS e marco `dsgpt_timeout=true` no JSONL. A tripla continua a ser DS→GPT→Claude+WS na regra escrita, mas fisicamente executa em paralelo pra não gastar 60-80s adicionais em série. Regra irmã de [[feedback-relatorio-diario-revisores]] (relatório diário conta todas as calls, não pula nenhuma).
