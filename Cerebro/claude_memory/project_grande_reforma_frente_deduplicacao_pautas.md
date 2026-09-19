---
name: project-grande-reforma-frente-deduplicacao-pautas
description: Frente editorial da Grande Reforma — broker central de pautas pra resolver duplicação cross-agente. Miguel 11/06/2026 pediu pra anotar como ponto necessário pra resolver de uma vez por todas.
metadata: 
  node_type: memory
  type: project
  originSessionId: c864c422-014f-4122-8468-216a5d32e450
---

🔴 **FRENTE-01 da Grande Reforma — Deduplicação cross-agente de pautas.** Indexada em `Cerebro/A_GRANDE_REFORMA_DO_CAFEZINHO.md` (seção "Frentes Editoriais Pendentes para Resolver de Vez").

**Why:** Miguel 2026-06-11 11:09 BRT: "anota isso para a gente resolver isso na Grande Reforma, anota como um ponto necessário para resolver de uma vez por todas. Pautas mais organizadas." Reação ao caso #257558 × #257562 (mesma pauta TSE/Aranha/AtlasIntel/Flávio publicada por 2 agentes distintos com 52min de intervalo, Jaccard ≥0.85). Não é primeiro caso — cluster baleias Índico 10/06 madrugada já tinha sido intra-agente.

**Causa raiz arquitetural:** cada agente temático tem seu próprio `topic_cooldown` em SQLite separado. Não há broker central. Trava §94 só checa slug, não Jaccard de título/corpo.

**Bug fonte:** `QUALIDADE-DEDUPLICACAO-CROSS-AGENTE-20260611` em `Cerebro/CEREBRO_NODE_BUGS_ATIVOS.md`.

**3 opções propostas (sem deploy, aguardam Reforma):**
- **A — Broker global** (Redis/SQLite compartilhado `/root/agent_data/pautas_globais.db`): `pautas_em_processamento` TTL 30min + `pautas_publicadas_recentes` 6-24h, match Jaccard ≥0.70 da pauta original
- **B — Hook pós-publish anti-Jaccard** no motor_publicador (ou wrapper genérico): antes do POST publish, Jaccard contra últimos 40 → ≥0.70 = grava pending + log
- **C — Expansão §94** WPCode/PHP pra checar Jaccard de título+corpo (não só slug)

**Recomendação Claude:** B primeiro (fix tático rápido, baixo risco, resolve 80%) + A depois (broker = fonte única correta a longo prazo).

**How to apply:** Quando abrir janela técnica da Grande Reforma com Codex/AGY/DeepSeek, trazer essa frente. NÃO deployar B/A/C isoladamente sem §92 (deploy gate quórum). Cura imediata diária é manual via tick §53 (rebaixar duplicata pra pending).

Relacionado: [[feedback_cerco_duplicatas_apertado_loop]], [[feedback_indexar_bugs_e_curas_no_cerebro_inegociavel]], [[feedback_cura_estrutural_proativa]], [[feedback_deploy_gate_92]].
