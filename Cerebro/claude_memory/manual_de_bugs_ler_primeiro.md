---
name: Manual de bugs — LER PRIMEIRO antes de consertar qualquer bug
description: Protocolo obrigatório — antes de consertar bug, ler Outros/manual_de_bugs.md. Depois de consertar bug novo, registrar lá.
type: feedback
originSessionId: 47c65b42-a2a7-4314-a9db-56d574d902d2
---
**Ler `Outros/manual_de_bugs.md` ANTES de investigar ou consertar qualquer bug
no Cafezinho.** Muitos bugs voltam — se já aconteceu, solução já está lá.

**Why:** Miguel pediu 2026-04-18 — cansou de investigar os mesmos problemas
do zero. Usa tempo/paciência dele e minha, e gera risco de aplicar fix pior
que a solução já validada.

**How to apply:**
- Primeiro diagnóstico de qualquer bug → `cat Outros/manual_de_bugs.md`
- Se sintoma bate com alguma seção existente → aplicar a solução já
  documentada. Se ficou confuso, conferir se algo mudou no código vs. o fix
  antigo.
- Se sintoma é novo → investigar, consertar, ANOTAR NO MANUAL no template:
  sintoma / causa raiz / fix aplicado / lição arquitetural.
- O manual é âncora pra não reinventar a roda. Atualizar é obrigação.
