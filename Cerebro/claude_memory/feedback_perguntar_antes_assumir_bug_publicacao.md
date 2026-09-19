---
name: perguntar-antes-assumir-bug-publicacao
description: "Antes de assumir bug/ação automática quando um post mudou de status ou aparece published inesperado, perguntar ao Miguel se foi ele quem publicou"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 1bb17b73-7603-4ca4-8fbc-e3a059066760
---

**Regra:** Sempre que encontrar um post em status diferente do esperado (ex: `publish` quando script declarou `draft`, ou `draft` quando esperava `publish`), perguntar ao Miguel se foi ação manual dele antes de assumir bug no código, reverter status, ou abrir incidente.

**Why:** Caso 15/07/2026 — repetidor estatal rodou smoke test. Log mostrou "PUBLICADA AO VIVO! ID=261744" + Indexing API OK. Achei que era bug do script (script tinha `status: draft` hardcoded na linha 504 mas post saiu publish). Reverti pra draft imediatamente sem perguntar. Miguel corrigiu: "eu que publiquei aqui, voce tem que perguntar sempre se fui eu que publiquei." Ou seja, ele tinha ido no wp-admin e clicado publish manualmente.

**How to apply:**
- Antes de qualquer ação de reversão/correção de status de post, enviar mensagem curta ao Miguel: "Post X está publish — foi você que publicou manualmente ou é pra ser draft?"
- Só assumir bug se Miguel confirmar que não foi ação manual
- Aplica a qualquer status (`publish`, `draft`, `pending`, `private`, `future`)
- Aplica também a mudanças suspeitas: categoria alterada, autor trocado, slug modificado, featured media trocada — sempre confirmar antes de reverter
- Esta regra é IRMÃ da [[feedback-trigger-retomar]] e do princípio "pause perante ambiguidade" (REGRA #2 Tencent) — assumir bug sem confirmar é o oposto de pausar
