---
name: feedback-gatilho-tick-ler-inbox
description: "Quando Miguel escrever apenas \"tick\" (sem prompt §53 completo), o gatilho é LER o inbox de Claude (`Projeto Cafezinho Agentes/Foruns/inbox_trindade/claude.md`), não rodar o tick §53 inteiro."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 83feb640-dee1-483b-9372-162a5be7876e
---

# Gatilho "tick" = ler inbox

Quando Miguel digitar apenas `tick` (palavra solta, sem o template longo do TICK §53 LOOP MAESTRO CAFEZINHO), o comportamento esperado é:

1. Ler `Projeto Cafezinho Agentes/Foruns/inbox_trindade/claude.md`
2. Responder/agir conforme as mensagens novas lá

**NÃO** rodar o tick §53 completo (auditoria 30 posts, §93, §53C, etc) — esse rito só acontece quando Miguel cola o prompt longo "TICK §53 LOOP MAESTRO CAFEZINHO — CADÊNCIA 30min ...".

**Why:** Miguel deixou explícito em 2026-06-14 ~07:50 BRT: "quando eu escrever tick, é para o ler o inbox. não precisa ler agora. só para voce saber." Diferenciar gatilho curto (inbox) do gatilho longo (loop completo).

**How to apply:** Mensagem do Miguel = apenas a palavra `tick` (ou variantes curtas tipo "tick aí", "tick por favor") → abrir inbox e ler. Se ele colar o template completo do §53 (começando com "TICK §53 LOOP MAESTRO CAFEZINHO"), aí sim rodar o ritual completo.

Relacionado: [[feedback_gatilho_retomar_ritual_despertar]] (gatilho "retomar" = ler boletins news + instruções gerais de despertar).
