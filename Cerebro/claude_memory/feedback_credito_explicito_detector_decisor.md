---
name: Crédito explícito de detecção/opinião/decisão/ação em toda autocura
description: Miguel exige (11/05 17:59 BRT) que toda autocura, alerta ou achado credite explicitamente quem detectou, quem opinou, quem decidiu e quem executou.
type: feedback
originSessionId: 74d51083-651f-4cd2-8c94-a94a70f6fdcb
---
**Regra inegociável:** TODO append no canal_trindade, fórum, JSONL ou Cérebro sobre autocura/alerta/rebaixamento/escalada deve nomear explicitamente os 4 papéis:

1. **DETECÇÃO** (quem viu) — sentinela X / Claude no loop V2 / Codex auditoria / Miguel visual / DeepSeek-Kimi-Qwen em consulta. Não atribuir ao agente errado por preguiça (ex: dizer "sentinela detectou" se foi Claude que viu visualmente listagem WP).
2. **OPINIÃO/PARECER** (quem opinou sobre o que fazer) — registrar voto literal com timestamp, especialmente quando trio diverge.
3. **DECISÃO** (palavra final) — Miguel humano / §37 técnico / autocura automática autorizada.
4. **AÇÃO** (executou no servidor/WP/canal) — Claude / Codex / script automático.

**Why:** Miguel cobrou 11/05 17:59 BRT após caso fundador da duplicata João Feres (posts 245808/245816). Eu (Claude) tinha rebaixado 245808 sem creditar explicitamente quem detectou (eu, não o sentinela). Crédito errado polui o histórico e dificulta auditoria; Miguel precisa saber de quem foi cada decisão pra calibrar a Trindade.

**IMPORTANTE — correção 11/05 18:03 BRT:** o caso 245808/245816 NÃO foi "Miguel derrubando regra automática". Foi **exceção pontual** porque a duplicata teve **origem em ordens humanas do Miguel via Antigravity** (ele mandou corrigir o post; AG publicou versão nova; original ficou no ar). A regra automática `feedback_autocura_duplicata_mesmo_dia.md` ("rebaixar mais recente") **continua válida** — não foi derrubada, foi inaplicável a este caso específico de correção humana.

**How to apply:**
- Toda mensagem sobre autocura/alerta deve ter bloco "Cadeia de eventos: detecção→opinião→decisão→ação" com timestamps.
- Log JSONL do vigia autônomo (`agent_data/trindade_economica.jsonl`) já registra todos os 4 papéis — não simplificar.
- Quando trio diverge, NUNCA esconder a divergência. Listar voto literal de cada um.
- Quando Miguel derruba regra automática, registrar explicitamente "Miguel derrubou regra X em favor de decisão Y porque Z".
- Indexado no Cérebro como §46 do `CEREBRO_NODE_GOVERNANCA.md`.
