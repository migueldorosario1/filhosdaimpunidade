---
name: feedback-protocolo-resposta-inbox-mesmo-arquivo
description: "Quando alguém da Trindade escreve ordem no MEU inbox (`Cerebro/Foruns/inbox_trindade/claude.md`), eu respondo no MESMO arquivo embaixo. Nunca no canal, nunca em arquivo novo, nunca no inbox da outra pessoa."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 83feb640-dee1-483b-9372-162a5be7876e
---

# Protocolo de resposta — inbox é conversa, não passagem

Quando alguém da Trindade (DeepSeek, Codex, Kimi, GLM, Qwen, Grok, AGY, Antigravity) escreve uma ordem ou mensagem no MEU inbox (`Cerebro/Foruns/inbox_trindade/claude.md`), respondo **no mesmo arquivo, escrevendo embaixo**. Padrão:

```markdown
**DeepSeek → Claude:** Migrar coletor X. Cartinha quando terminar.

**Claude → DeepSeek:** Pronto. 193 pautas, 57 passaram. Cartinha em Foruns/cartinha_X_20260614.md.
```

**Regras inegociáveis:**

1. **Nunca** responder no `canal_trindade.md` (canal = só anúncios gerais "entregue", "aprovado", "pausando").
2. **Nunca** criar arquivo novo só pra responder (vira ruído + perde rastro da conversa).
3. **Nunca** responder no inbox da outra pessoa (cada inbox pertence a quem RECEBE).
4. **Sempre** dry-run antes de executar ordem que tenha efeito em produção.
5. **Sempre** cartinha humanizada como entrega final pro Miguel colar em outros chats.

**Fluxo completo:**
```
DeepSeek/outro → escreve ordem no MEU inbox
Eu → leio NO MEU inbox
Eu → executo local em dry-run
Eu → respondo NO MEU inbox (resultado + link da cartinha/fórum)
Eu → aviso no canal_trindade.md (só resumo curto: "entregue, fórum X")
```

**Why:** DeepSeek (escrituário da Reforma) consolidou regra 14/06 ~09:35 BRT via Miguel após confusão entre Trindade sobre onde responder. Sintoma: ordens iam pro inbox mas respostas iam pro canal, perdendo rastro de conversa por pessoa. Tem que ser inbox = histórico bidirecional 1:1.

**How to apply:**
- Mensagem no MEU inbox → resposta no MEU inbox (na mesma seção, abaixo do `**X → Claude:**`).
- Decisão coletiva/anúncio geral → canal.
- Análise/documentação longa → fórum em `Projeto Cafezinho Agentes/Foruns/forum_<tema>_<data>.md` e ponteiro no inbox/canal.
- Resumo pro Miguel → cartinha com emojis, linguagem simples, pronta pra colar.

Relacionado: [[feedback_constituicao_artigo2_comunicacao_trindade]] (Artigo 2 base: canal=ponteiro / fórum=memória / inbox=pessoal / cartinha=resumo).
