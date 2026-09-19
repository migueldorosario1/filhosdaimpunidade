---
name: Sistema de aprendizado V4 autocura — diagnóstico 2026-04-19
description: 4 camadas do aprendizado do V4. Funciona mas com baixa variedade — 1 princípio aprendido (entidades tipográficas) em 30 curas. RLHF Reverso nunca exercitado.
type: project
originSessionId: 47c65b42-a2a7-4314-a9db-56d574d902d2
---
**Diagnosticado 2026-04-19 ~11:20 BRT a pedido do Miguel.**

**Arquivos-chave (TODOS em `/root/agent_data/`, não em `/root/`):**
- `autocura_acoes.json` — ações executadas (cura_regex, cura_llm, rebaixar)
- `licoes_recentes_autocura.json` — FIFO de lições (separado por polaridade evitar/tolerar)
- `historico_absoluto_licoes.txt` — memória vitalícia append-only

**Estado em 2026-04-19:**

| Camada | Status | Números |
|---|---|---|
| Ações (`autocura_acoes.json`) | ✅ grava | 30 ações: 29 cura_regex + 1 cura_llm. Última 2026-04-18 17:17 |
| Lições FIFO (`licoes_recentes_autocura.json`) | ✅ deduplica bem | 1 evitar ativa, 0 tolerar |
| Histórico absoluto (`historico_absoluto_licoes.txt`) | ✅ append | 21 linhas, todas `[renovada]` do mesmo princípio |
| Regras Vivas (`Outros/regras_vivas_auditoria.md`) | ✅ editável | 11 bullets, R1 reescrita 2026-04-19 |

**O único princípio ativo na FIFO evitar:**
> "Nunca devolva texto com entidades HTML tipográficas (&#8217;, &#8220;, &#8211; etc.). Use os caracteres reais (' " – —) — o WordPress já entende e renderiza certo."

**Insights:**
- Deduplicação funciona: 29 curas idênticas viraram 1 lição, não polui FIFO.
- Hoje (19/04) não houve novas curas porque o fix `content.raw` de 18/04 eliminou a fonte dos `&#038;` (bug do ciclo fantasma). Sistema aprendeu que esse bug não existe mais.
- **RLHF Reverso zerado** — Miguel nunca reverteu uma cura (zero entradas `tolerar`).
- Variedade baixa: 1 princípio em 30 curas. Todas as curas foram variações do mesmo bug.
- Investimento maior do aprendizado hoje está no **humano** (Miguel+Claude editando `regras_vivas_auditoria.md`), não no autônomo. Isso é por design conservador do V4.

**Pra crescer variedade de sabedoria:**
1. Bugs reais novos que caiam na regex (não escalados pra V3) — raro hoje
2. Miguel reverter alguma cura (ativa RLHF Reverso → vira tolerar com peso alto)
3. Mais cura_llm aprovada em consenso (hoje só 1)
