---
name: monitoramento-relatorios-detalhados
description: "Miguel exige loop de monitoramento com relatórios diários/semanais/mensais detalhados, indexados no Cérebro e linkados no Boletim News. Nunca bloquear — sempre adicionar fallbacks."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 23db8fb8-ae8e-4d0f-a1e7-3645e7d8bbc6
---

Loop de monitoramento Claude Maestro deve gerar relatórios DETALHADOS e PROFUNDOS.

**Why:** Miguel quer dados para aperfeiçoar o sistema continuamente. Relatórios superficiais não servem.

**How to apply:**
- Fórum diário em `Foruns/monitoramento/YYYY/MM/forum_monitoramento_YYYYMMDD.md`
- Cada tick appendado com timestamp, tabela de agentes, posts, erros, circuit breaker, concentração, autocura, custo
- Relatórios semanais e mensais consolidados dos dados diários
- Indexar no Cérebro: `CEREBRO_NODE_BOLETIM_NEWS_CAFEZINHO.md` sempre linka o último relatório
- Boletim News atualizado com resumo + link do relatório

Diretriz correlata [[feedback_soltar_posts_nao_prender]]:
> "A solução é sempre colocar mais fallback, além das correções estruturais. Jamais bloquear."
> — Miguel, 27/05/2026 ~17:05 BRT
