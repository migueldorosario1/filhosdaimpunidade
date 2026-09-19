---
name: Foruns/legacy/ só pra fóruns com mtime ≥48h
description: Regra dura — nunca mover pra Foruns/legacy/ um fórum atualizado nas últimas 48h. Mtime <48h = vivo, fim. E mesmo ≥48h pede confirmação de Miguel.
type: feedback
originSessionId: 084851fc-dace-4658-b659-01c53123a273
---
**Regra:** nunca mover um fórum pra `Foruns/legacy/` se ele foi atualizado nas últimas **48 horas**. Legacy é pra fóruns velhos (mtime ≥48h) E parados.

**Why:** em 26/04 09:55 BRT propus mover 4 fóruns pra legacy (forum_eleicoes 25/04, forum_enxame_comentaristas 24/04 23:11, forumeleicoeshoje 25/04, forum_custos_IA 22/04). Miguel cortou: "esses foruns estão sendo usados. nao move nunca nenhum forum que foi atualizado há menos de 24 horas para o legacy. legacy é para foruns velhos, com mais de 48 horas". Aprendizado: contexto vivo > análise estática do conteúdo. Um fórum pode parecer "resolvido" pela leitura mas ainda estar sendo consultado/expandido por outras sessões.

**How to apply:**
- Antes de mover qualquer fórum pra `Foruns/legacy/`: rodar `stat -c '%y %n' arquivo` pra checar mtime.
- mtime <48h → **NUNCA MOVER**, nem propor.
- mtime ≥48h → ainda pede confirmação explícita de Miguel antes de mover. Não tomar decisão sozinho — outros slots podem estar usando.
- Para a triagem inicial dos 7 fóruns duvidosos do Slot 5: todos os 4 candidatos ficam como ESTÃO. Único que tecnicamente passaria os 48h é forum_custos_IA (22/04) e forum_novosagentes (21/04), e mesmo esses Miguel marcou como "em uso".
