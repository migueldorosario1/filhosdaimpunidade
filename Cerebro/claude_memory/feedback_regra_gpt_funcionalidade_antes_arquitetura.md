---
name: feedback-regra-gpt-funcionalidade-antes-arquitetura
description: "Regra GPT 25/06/2026 — toda decisão deve responder \"isso aproxima Miguel de publicar matéria conversando com ChatGPT?\". Se não, adia."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: ab544d32-d470-42b2-8246-7c83f1137bc1
---

## Regra GPT 25/06/2026 — funcionalidade entregável antes de arquitetura elegante

**Regra**: antes de postar qualquer parecer técnico, sugestão de PR, ou bloqueio no projeto Publicador Cafezinho / Acervo Editorial de Mídia, perguntar:

> "Isso aproxima Miguel de publicar uma matéria conversando com o ChatGPT?"

Se a resposta for "não", **adia ou cala**.

**Why**: trigger foi 25/06/2026 noite. A Trindade (GPT/Codex/GLM/Claude) tinha caído em loop de discussão arquitetural sobre bump v1.1.0, enums ortogonais, schema JSON com 10 campos extras, embeddings, ranking avançado, busca semântica — enquanto o **objetivo simples** ("Miguel fala com ChatGPT → sistema publica matéria com imagem certa") ainda não estava entregue end-to-end. GPT cortou a discussão com carta de reorientação. Miguel endossou: "essa é a mensagem mais importante da conversa inteira".

**Minha contribuição própria pro problema** (auto-crítica registrada): meu parecer de 3 enums ortogonais pro bump v1.1.0 era tecnicamente correto MAS exatamente o tipo de discussão que GPT acabou de adiar — não impedia publicar matéria com imagem do Moraes. Igualmente: minhas sugestões de PR #3/#4/#5/#6 antes do PR #2 funcionar end-to-end.

**How to apply**:

1. **Critério único de bloqueio**: só bloqueio PR/decisão se IMPEDIR o objetivo simples. Issues elegantes mas não-bloqueantes vão pra "PR de débito declarado", não pra discussão antes do merge.

2. **Filtro de sobrevivência aplicado nos meus 7 pareceres de 25/06**: só sobreviveu o pré-merge da `license` Flickr (P3) — porque é jurídico (Cafezinho infringe regra própria). Os outros 6 (bump v1.1.0, enums ortogonais, dedupe doc, CI, schema completo, usage_history) ficaram adiados.

3. **Sprint válida = Sprint que entrega função utilizável por Miguel**. Se Miguel não consegue fazer algo novo ao fim da Sprint, a Sprint falhou. Decoração arquitetural não conta como entrega.

4. **Ordem GPT pra Sprint atual** (não inverter):
   - Passo 1: PR #2 funcionando end-to-end (image_query → imagem → WordPress)
   - Passo 2: Flickr Harvester (sem Vision)
   - Passo 3: Wikimedia Harvester (mesmo contrato)
   - Passo 4: R2 Uploader (hash + envia R2 + atualiza índice)
   - Passo 5: SÓ DEPOIS Vision (enriquece acervo, não é requisito pra primeiro post)

5. **Adiados explicitamente** (não trazer de volta sem AUTH Miguel): embeddings, ranking avançado, histórico completo de uso, busca semântica, curator automático, migração em massa do legado.

**Não se aplica a**: bloqueio jurídico (licença/crédito ausentes), bloqueio de segurança (credencial vazada, AUTH Miguel ausente em deploy main), bloqueio de carta dura (REGRA #1/#2/#3 violadas no Tencent). Esses seguem bloqueio imediato independente do filtro.

**Relacionado**: [[project-sprint-acervo-midia-publicador-microsservicos-20260625]] — sprint cuja Sprint A está sob essa regra de cadência funcional.
