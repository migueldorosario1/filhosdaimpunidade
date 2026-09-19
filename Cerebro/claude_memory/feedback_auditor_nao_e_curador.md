---
name: auditor-nao-e-curador
description: "Papel do auditor em pipeline de agentes — veto-only binário, nunca curadoria editorial"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: ff302e2b-ddd7-460c-9ae1-9c5facf683e9
---

Em pipeline de agentes (repetidor estatal e similares), o **auditor LLM não é curador**. Ele só responde a uma pergunta binária: a matéria é **publicável**? Threshold baixo (40), "na dúvida aprove". Curadoria editorial (qualidade, relevância, tom) fica em outras camadas: ranker escolhe top 3, curadoria_e_reescrita refina texto, observador V3 faz higienização pós-publish.

**Why:** Miguel 16/07/2026 corrigiu meu desenho depois de eu propor Opção B (remover auditoria completamente) e Opção D original (threshold 40 + prompt ainda exigente "manchete do dia"). Ele disse: "a gente vai melhorar a qualidade pela coleta e curadoria. o auditor não pode ser curador. ele tem que ver se a matéria é publicável, ponto". 

Precedente: matéria "Senado aprova educação financeira nas escolas" (PLC 2.979/2023) foi descartada pelo auditor original (threshold 65) com Nota 15 "impacto difuso" — mas era matéria factual institucional legítima com fato jornalístico identificável (aprovação em Plenário). Auditor estava fazendo curadoria ("não é manchete do dia") em vez de veto-only.

**How to apply:**
- Desenhando pipeline novo: auditor = pergunta binária "publicável?", com threshold 40 ou similar
- Auditor só deve barrar lixo evidente: agenda/cerimônia/posse/pêsames/portaria seca/comunicado de serviço/matéria sem fato jornalístico
- Prompt NÃO deve ter: "Seja EXIGENTE", "manchete do dia", "calibragem média 40-45", "consequência mensurável R$"
- Prompt DEVE ter: "NA DÚVIDA, APROVE", "você não é editor-chefe", "só rede de segurança contra lixo evidente"
- Pra subir qualidade: ajustar ranker (prompt/top_n) e curadoria_e_reescrita, NÃO apertar auditor
- Aplica a: repetidor estatal, futuro repetidor turismo, qualquer robô resiliente que precise publicar sempre

Irirmã: [[feedback-pending-so-miguel-promove]] (escopo PENDING/rebaixamento), [[project-repetidor-estatal-reforma-data-driven]] (estado da reforma).
