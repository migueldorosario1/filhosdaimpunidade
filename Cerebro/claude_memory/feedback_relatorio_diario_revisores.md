---
name: feedback-relatorio-diario-revisores
description: Gerar todo dia (24h) relatório MD dos gastos com DeepSeek + GPT revisores. Auto no primeiro ciclo BRT do dia novo. Miguel 2026-08-03 14:15 BRT.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 9ff9d002-2c71-4670-87db-7c5f55616550
---

**Regra:** No PRIMEIRO ciclo Vigília V5 de cada dia BRT (00:17 ou o primeiro que rodar), gerar automaticamente o relatório do dia anterior via:

```bash
python3 /home/migueldorosario/ferramentas/sentinela/relatorio_diario_revisores.py YYYY-MM-DD
```

**Saída:** `Cerebro/monitoramento_horario/relatorios_revisores/YYYY-MM-DD.md`

**Comandos:**
- `python3 relatorio_diario_revisores.py` — hoje
- `python3 relatorio_diario_revisores.py 2026-08-03` — dia específico
- `python3 relatorio_diario_revisores.py --stdout` — imprime sem salvar

**Conteúdo do relatório:**
- **DeepSeek:** chamadas, tokens in/out, custo USD+BRL, latência média, contagem de recomendações
- **GPT:** chamadas, tokens, custo, latência, tabela por modelo (calls/custo BRL/latência)
- **Concordância GPT↔DeepSeek:** % (extraído do `concordo_deepseek`)
- **Total combinado:** USD+BRL do dia + projeção mensal (30d)
- **Por vertical:** contagem de drafts revisados por vertical (v4d_geopolitica/nacional/ciencia)

**Fontes de dados:**
- `logs/deepseek_revisor_telemetria.jsonl`
- `logs/gpt_revisor_telemetria.jsonl`
- `state/deepseek_counter_YYYY-MM-DD.json`
- `state/gpt_counter_YYYY-MM-DD.json`

**Como aplicar:**
1. No primeiro ciclo BRT do dia (00:xx normalmente), ANTES de puxar drafts:
   - `data_ontem = (hoje - 1 dia).strftime("%Y-%m-%d")`
   - Verificar se `Cerebro/monitoramento_horario/relatorios_revisores/{data_ontem}.md` existe
   - Se não, rodar `python3 relatorio_diario_revisores.py {data_ontem}`
   - Mencionar no report do ciclo que o relatório foi gerado + link.
2. Miguel também pode pedir "relatorio revisores" a qualquer momento — gerar sob demanda.
3. Se algum dia o custo saltar (>3x média 7d), alertar no relatório.

**Caso fundador (03/08 17:07 BRT):** 3 chamadas (2 DS + 1 GPT), R$ 0.033 total, R$ 1.00 projeção mensal com esse volume mínimo. Volume real esperado ~30 posts/dia = ~R$ 30/mês combinado.

Regras irmãs: [[feedback-deepseek-revisor-camada-extra]], [[feedback-gpt-revisor-camada-tripla]].
