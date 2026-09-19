---
name: feedback-soltar-posts-nao-prender
description: "Diretiva inegociável de Miguel — qualquer sprint de autocura/sentinela deve soltar posts, nunca bloquear. Vetado qualquer código que retenha publicação."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 4720f070-67f8-45eb-a8d1-e6cc0cec005a
---

Nunca instalar lógica que bloqueie, retenha ou enfileire posts para revisão humana como consequência de auditoria automática.

**Why:** Miguel, 2026-05-24 22:26 BRT: "Não podemos instalar nada que crie mais risco de bloqueio dos posts. A lógica é o contrário: soltar mais posts, não prender mais." Incidente fundador: Proposta A do sprint Autocura Visual foi deployada (e revertida) com lógica de enfileirar posts com imagem em inglês — gerava gargalo sem necessidade.

**How to apply:** Antes de propor qualquer sprint de sentinela, autocura ou failsafe, responder: "este código pode reter um post que antes seria publicado?" Se sim → redesenhar até ser não. Ação permitida: detectar → corrigir silenciosamente → publicar. Ação proibida: detectar → bloquear → escalar para humano.
