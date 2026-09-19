---
name: feedback-indexar-relatorios-tick-no-cerebro
description: "Miguel 16/06 23:15 BRT — relatórios de tick do Loop §53 (`Projeto Cafezinho Agentes/Foruns/relatorio_monitoramento_<YYYYMMDD>_loop53_30min.md`) DEVEM ser indexados em `Cerebro/CEREBRO_NODE_RELATORIOS_MONITORAMENTO.md` no fim de cada dia (ou no fim de tick noite ~23:43 BRT). Eu estava esquecendo — índice ficou parado em 04/06 enquanto relatórios diários acumulavam até 16/06. Lacuna catastrófica de 12 dias. Padrão de manutenção: cada novo relatório do dia ganha 1 linha na tabela cronológica do CEREBRO_NODE_RELATORIOS_MONITORAMENTO com: data, link relativo, escopo curto, lista de Críticos (AUTHs PASS + curas + descobertas)."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 83feb640-dee1-483b-9372-162a5be7876e
---

# Indexar relatórios de tick no Cérebro — fim de cada dia

## A regra

Miguel 16/06 ~23:15 BRT perguntou: "voce está indexando todos os relatórios de tick no cérebro?"

Resposta honesta: NÃO. Eu estava escrevendo o relatório diário em `Projeto Cafezinho Agentes/Foruns/relatorio_monitoramento_<YYYYMMDD>_loop53_30min.md` mas NUNCA atualizava `Cerebro/CEREBRO_NODE_RELATORIOS_MONITORAMENTO.md`, que é o índice canônico no Cérebro. Índice estava parado em **04/06** enquanto relatórios diários haviam acumulado até **16/06**. Lacuna de 12 dias.

Curei retroativamente 23:18 BRT adicionando entradas dos 12 dias (06-16/06).

## Como aplicar daqui pra frente

**Pra todo dia (no fim de tick noite ~23:43 BRT OU no primeiro tick do dia seguinte)**: adicionar 1 linha na tabela cronológica do `CEREBRO_NODE_RELATORIOS_MONITORAMENTO.md` com:

```markdown
| 2026-MM-DD | [relatorio_monitoramento_YYYYMMDD_loop53_30min.md](../Projeto%20Cafezinho%20Agentes/Foruns/relatorio_monitoramento_YYYYMMDD_loop53_30min.md) | Loop §53 30min — DD/MM | <síntese dos críticos: AUTHs PASS, curas §51 importantes, descobertas, incidentes, fóruns abertos> |
```

**Coluna "Críticos"** deve ter:
- Número de AUTHs PASS (e quais)
- Resumo de curas estruturais ou massivas
- Descobertas importantes (bugs novos, padrões, etc)
- Fóruns abertos
- Incidentes
- Timeouts/comportamentos anômalos

**Período**: link relativo `../Projeto%20Cafezinho%20Agentes/Foruns/relatorio_monitoramento_YYYYMMDD_loop53_30min.md` (com %20 pra espaço no path).

## Quando NÃO esquecer

- Última linha do dia ANTES do primeiro tick do dia seguinte (~00:13 BRT)
- OU no tick 23:43 BRT do próprio dia, se já dá pra fechar
- Não esperar acumular vários dias — Miguel pediu indexação CORRENTE

## Caso fundador

16/06 23:15 BRT: Miguel detectou índice parado em 04/06. Eu confessei e indexei retroativamente 12 dias.

## Relacionados

- [[reference_doc_claudia_beatriz_monitoramento]] — outro doc que também precisa ser cruzado em ticks §53
- [[feedback_tick_53_qualidade_20_posts_e_claudia]] — formato canônico do tick
