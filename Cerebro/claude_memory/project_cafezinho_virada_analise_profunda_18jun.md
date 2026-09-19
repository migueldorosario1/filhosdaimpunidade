---
name: project-cafezinho-virada-analise-profunda-18jun
description: Cafezinho viralizando hard news → análise profunda — 7× mais barato (81¢→12¢/dia). Política V2 + YouTube V2 pipeline 7 etapas com banco. Decisão Miguel 18/06.
metadata: 
  node_type: memory
  type: project
  originSessionId: 8151465d-76ab-4d1d-bfe5-285d266e7ca7
---

Em 2026-06-18 Miguel decidiu virar o Cafezinho: **menos hard news (muitas notícias curtas) e mais análise profunda (poucas peças por dia, altíssima qualidade)**. Política V2 e YouTube V2 são os pipelines novos — 7 etapas com banco entre elas. Custo cai de 81¢/dia (atual hard news) para 12¢/dia (V2 análise profunda) — 7× mais barato.

**Why:** Miguel quer jornal de melhor qualidade editorial (poucas peças bem-feitas vs muitas peças medianas) E sustentabilidade financeira do enxame (custo LLM caindo 86%). Decisão tomada após meses de iteração com Trindade.

**How to apply:** Daemon (tick §53) deve esperar vazão MENOR de publishes/hora quando Política V2 entrar em produção (não 4-6/hora, talvez 2-3/hora). NÃO interpretar queda de vazão como bug ou falha sistêmica. Métricas qualitativas (§53C auditor, Tribunal Visual, profundidade fact-check) ganham mais peso que volume bruto. Política V2 ainda NÃO substitui legado — corre em paralelo com cap gradual.

**Estado em 18/06 noite:**
- Política V2 (Kilo/Qwen) — Fases A/B/C ✅ concluídas localmente, 4 gaps em construção
- YouTube V2 (Codex) — funcional local mas depende PYTHONPATH legado
- 4 gaps: (1) Filtro antilixo aguarda Codex; (2) Validador saída ✅ AGY-CLI entregou 20:05; (3) Fact-check Gemini Grounding pode começar; (4) Auditoria Final Gemini 2.5 Pro pode começar
- Regras: zero deploy remoto sem AUTH; sem crontab; sem `--live`; sem desligar legado; Antigravity Desktop não coda

Documentos canônicos: `Projeto Cafezinho Agentes/Foruns/carta_trindade_3_noite_20260618.md` (carta final noite 18/06), `Projeto Cafezinho Agentes/Foruns/rodada_concisao_final_20260618.md` (rodada concisão DeepSeek).

Vinculado a [[project-cafezinho-media-group-diretriz-18jun]] (4 nichos: IA, Política/Geopolítica, Comércio Exterior, Ciência).
