---
name: feedback-testes-agy-indistinguiveis-de-pauta-real
description: Testes do AGY são editorialmente reais — não dá pra distinguir teste de pauta legítima só por conteúdo. Único sinal seguro é vazamento (draft → publish)
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 83feb640-dee1-483b-9372-162a5be7876e
---

Miguel 2026-06-13 ~01:14 BRT corrigiu minha avaliação durante AGY-watch.

**Regra:** Durante período de testes do AGY, **todo draft pode ser teste — INCLUSIVE com qualidade editorial completa** (1500+ chars, tom Cafezinho, categoria definida, fm preenchida). Conteúdo real não é evidência de que NÃO é teste.

**Why:** AGY testa publicando textos com aparência de pauta verdadeira pra simular o fluxo real. Se eu classifico draft como "pauta legítima" só por ter conteúdo elaborado, posso liberar um teste que deveria ficar isolado (ou pior, dar OK pro Miguel quando ele me pergunta).

**How to apply (critério Miguel 13/06 ~01:15 BRT — "basta manter no rascunho"):**
- Drafts são intocáveis — não rebaixar, não classificar por conteúdo, não opinar sobre qualidade
- Único sinal de problema = **draft virou publish** sem aval Miguel
- A cada tick: comparar IDs em draft com baseline. Se algum ID do baseline saiu de draft pra publish → rebaixar imediato pra `pending` + alerta no chat
- Não preciso filtrar publish novos por "cara de teste" — basta seguir o set de IDs em draft

**Caso fundador:** 13/06 01:14 BRT, draft #257878 "A tuneladora poética: bisneta de Cora Coralina vai ver o tatuzão do metrô de SP". Conteúdo de 1804 chars, tom irônico jornalístico legítimo do Cafezinho, cat=22 (Política), fm=257877. Reportei como "pauta editorial legítima" e Miguel corrigiu: "esse é teste do agy. é que os testes são reais."

**Limite:** quando Miguel sinalizar fim do período de testes do AGY, voltar ao protocolo normal de drafts (rascunho humano WIP [[feedback_draft_humano_wip_nao_lixo_automatico]]).

Vinculante. Inclui [[feedback_soltar_posts_nao_prender]] como contexto — não prender legitima publicação, mas teste do AGY virando publish é justamente o que NÃO devemos soltar.
