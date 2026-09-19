---
name: circuito-monitoramento-diretrizes
description: "Visão Miguel 27/05: 5 fontes de monitoramento (cloud/humano/performance/qualidade/diretrizes) alimentam circuito fechado. Resumo 24h → agente qualidade → agente diretrizes AMPLIADO que muda tudo. Fórum para discutir."
metadata: 
  node_type: memory
  type: project
  originSessionId: 23db8fb8-ae8e-4d0f-a1e7-3645e7d8bbc6
---

# Circuito Monitoramento → Diretrizes (visão Miguel 27/05 ~17:20 BRT)

**Fato:** Miguel quer que os relatórios de monitoramento alimentem um circuito fechado de melhoria contínua. O agente de diretrizes será AMPLIADO para mudar tudo (prompts, cascatas, configs, regras), não só diretrizes editoriais.

**Why:** Monitoramento sem ação é desperdício. Os dados do loop 30/30 + monitoramento humano + performance devem gerar mudanças concretas no sistema.

**How to apply:**

5 fontes → resumo diário 24h → agente qualidade → agente diretrizes ampliado:
1. **Monitoramento Cloud** (Loop Maestro 30/30min) — JÁ ATIVO
2. **Monitoramento Humano** (Cláudia/Miguel via Google Doc) — VERIFICAR estado
3. **Monitoramento Performance** (agente_analytics_v9) — ATIVO no cron
4. **Agente Qualidade** (agente_qualidade_redacao) — EM CONFIGURAÇÃO, Miguel quer mais sofisticado
5. **Agente Diretrizes** (agente_diretrizes_editoriais) — AMPLIAR para mudar tudo

Fórum de discussão: `Foruns/forum_circuito_monitoramento_diretrizes_20260527.md`

Pendências:
- Verificar se Cláudia está atualizando o Doc
- Configurar agente qualidade mais sofisticado
- Desenhar ampliação do agente diretrizes
- Definir horário de fechamento diário (00:00? 05:00?)
- Sprint após aprovação Trindade
