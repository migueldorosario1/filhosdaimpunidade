# Lição — D8 formal: o que morre no ranking é o push GitHub (token), não o coletor

**Data:** 2026-09-02 · Ronda 13:00 (52º CHECK) · Ref: DS-N-20260902-019

## O quê
O mini-inventário D8 formal (missão do Miguel via CM-20260902-002) confirmou com prova:
- Painel `/v6/custos` VIVO com dados de hoje (R$ 25,09 · 263 chamadas 24h · série "02/09 hoje parcial | 158 | 969,4k | R$ 11,51").
- Ledger `banco_custos_2026-09.jsonl` com 184 linhas de hoje (última 12:59:53).
- Prometheus Alibaba (cofre `alibaba_prometheus.env`) VIVO: push_metrics.py "OK: 636 metricas" às 13:00.
- **ÚNICO morto:** o push GitHub do ranking de preços das LLMs (Mural das IAs) — o script `atualizador_precos_llm.py` RODA todo dia 09:00 e escreve o JSON local, mas o push para `cafezinhomediagroup.git` falha desde 22/08 09:00 com "Authentication failed: Invalid username or token" (credencial gh do root expirada). É isso que congela o rodapé "atualizado em 22/08/2026 09:00" no card de RANKING.

## Por quê
O rodapé da SEÇÃO (ranking) foi lido como rodapé da PÁGINA (telemetria) — mesma armadilha da lição "rodapé congelado, medição viva" das 00:32, agora com a causa raiz fechada: não é refactor, é credencial expirada. E o coletor que "parece morto" estava vivo — o morto era o elo de PUBLICAÇÃO do artefato (push git), não a produção do dado.

## Como aplicar
1. Rodapé de card ≠ rodapé de página: identificar QUAL seção o timestamp congela antes de decretar parada.
2. "Script roda e escreve local" ≠ "artefato publicado": checar o elo de push (git/cron) quando o público (CDN/painel) mostra data velha.
3. Credencial expirada em push git = dono ZM com cofre; reportar a cura SEM expor o valor (regra E4 HMAC-lite).
4. Prova viva = dados de HOJE no painel + ledger com timestamp + HTTP 200; veredito autodeclarado com essa trinca.
