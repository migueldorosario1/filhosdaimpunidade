---
name: feedback-auditor-titulos-entrega-diaria-inbox-20260817
description: "Auditor de Títulos (agente_auditor_titulos_gpt.py) entrega 9 sugestões/dia via cron 10:05 BRT na inbox_trindade/claude.md. Considerar SEMPRE ao revisar/promover post citado; aplicar se concordar (antes de publish/agendar); ignorar se sugestão for pior semanticamente. Auditor é advisor, não bloqueador."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: d556bf3a-514a-43d5-a6d6-417905366fd5
---

**📮 REGRA (ZCode/DeepSeek + Miguel, 17/08/2026 09:42 BRT):** Auditor de Títulos automático (`agente_auditor_titulos_gpt.py` no NYC, cron */10 poll + relatório diário :58) julga títulos V4 (author 5786) contra 7 regras editoriais (comprimento ≤80c, siglas, ideias concatenadas, fórmula c/ verbo, clareza, sentence case, etc.) e sugere reescritas quando falha. Custo ~US$ 0,005/dia. Não edita nem bloqueia — advisor.

**Canal de entrega (ligado 17/08 09:42 BRT por ordem Miguel):**
- Auditor exporta `SUGESTOES_ATUAL.md` no relatório diário (patch NYC c/ backup `.bak_pre_entrega_loops_20260817`)
- Entregador local `~/ZCodeProject/scripts/entrega_auditor_loops.py` puxa via scp, anexa em duas inboxes
- Cron local `5 10 * * *` (10:05 BRT, backup crontab)
- Duas inboxes:
  - `Cerebro/Foruns/inbox_trindade/claude.md` (Loop Miguel = eu)
  - `Cerebro/Foruns/loop_trindade_laura/mensagens/para_laura` (Loop Laura)
- Idempotente por dia, não spam em dia vazio

**Como usar (pedido Miguel):**
1. Ao revisar/promover qualquer post citado na entrega do dia → **considerar a sugestão**
2. Se concordar: aplicar título novo ANTES do `wp_update_post future/publish`
3. Se sugestão piora semanticamente: **ignorar** (auditor não pesa factualidade, só forma)
4. Se sugestão só não cabe pra pauta específica: ignorar

**Why:** Auditor treina uniformidade dos títulos V4 (evita 108c, "e"+"para" na mesma frase, ideias concatenadas). Automação da revisão sem burocracia — nenhuma edição forçada.

**How to apply:** Antes do meu `wp post update` em qualquer post V4, `grep -A 3 "Post $POST_ID" Cerebro/Foruns/inbox_trindade/claude.md | head -5` pra ver se tem sugestão do dia. Se tem, comparar com título atual, escolher.

**Casos de exemplo (17/08 primeiro dia):**
- ✅ **Aceitar quando encurta sem perder factual**: 266195 Rubio 112c→79c
- ❌ **Ignorar quando muda semântica**: 266229 Palmeiras "busca...para encerrar" (finalidade) → "busca...e encerra" (afirma resultado) — auditor não percebe diferença modal
- ❌ **Ignorar quando antecipa fato**: 266225 Equador "chega a Pequim" (fato) → "se encontra com Xi" (encontro ainda não ocorreu)
- ⚠️ **Caso a caso quando ângulo muda**: 266217 Irã "recompõe rápido" ≠ "desafia previsões" (ambos válidos, editorial escolhe)

Taxa aceite primeiro dia: ~50% (4 aceitas, 2 ignoradas, 2 espera, 1 self-dup). Saudável — auditor está aprendendo bem.

**Reporte de feedback pro auditor:** se o next model puder pesar factualidade além de forma (regra 2 falha em "e" vs "para"), ganharia aceite. Não urgente.

Ver também: [[feedback-processo-autoaprendizado-ler-memoria-todo-ciclo-20260815]] (ler inbox faz parte do ritual de reancoragem).
