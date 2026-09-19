---
name: feedback-draft-humano-wip-nao-lixo-automatico
description: Drafts com pouco conteúdo / fm=0 podem ser rascunho humano em construção (especialmente do Miguel autor do site) — não classificar como captura do hard filter ou lixo automático sem checar autor/contexto.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 4b9c33c3-012b-4da8-a7ae-7da8ea3fc063
---

**Regra:** Em qualquer auditoria de posts WordPress do Cafezinho, posts em `status=draft` com pouco conteúdo (corpo curto, fm=0, cat genérica) **não devem ser interpretados automaticamente como falha do sistema nem lixo interceptado por guard-rail.** Eles podem ser **rascunho humano em construção** — especialmente do próprio Miguel, que escreve matérias editoriais no portal.

**Why:** Tick 6 do loop §53 (04/06/2026 18:20 BRT) — reportei #256444 "Colapso catastrófico... Ipec/Ipsos sobre Ciro Gomes" como "captura do hard filter Fase B" (porque tinha fm=0 + corpo 10 palavras). Miguel corrigiu 2 min depois: era ele próprio escrevendo. Frustração visível no chat ("meu deus"). Erro de interpretação publicado no canal_trindade e no relatório oficial.

**How to apply:**
1. Antes de classificar draft com pouco conteúdo como "captura do sistema", verificar:
   - `author` do post via WP API (`_fields=...,author`). Author 5470 = `Redator` automático; outros IDs = humanos.
   - Padrão do conteúdo: rascunhos humanos tendem a ter pergunta no título ("X ou Y?"), placeholders ("baixe aqui a íntegra"), referências a fontes externas a serem incorporadas.
2. Se houver dúvida, **mencionar como "possível WIP humano"** em vez de "captura do hard filter".
3. Hard filter Fase B (`guarded_wp_post` rebaixando publish→draft quando cat=[]||fm=0) é real e funciona, mas só conta como evidência se o post estava sendo *enviado* como publish e foi rebaixado pelo sistema — não se foi criado direto como draft (que é fluxo humano normal).
4. Vale para qualquer auditoria editorial do Cafezinho, não só o loop §53. Relacionado a [[feedback_soltar_posts_nao_prender]] — drafts humanos são intocáveis.
