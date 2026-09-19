---
name: feedback-resumo-humanizado-copy-paste-friendly
description: "Sempre que reportar pro Miguel algo que envolve coordenação com Codex/DS/AG, escrever em texto humanizado copy-paste-friendly. Miguel é o pombo-correio entre os LLMs e quer poder colar a resposta inteira no chat do outro agente sem editar. Conversa LLM↔LLM no canal/fórum pode ser técnica."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 4c52d90e-06f8-4198-8f65-dc7d7dc0c759
---

# Resumo humanizado copy-paste-friendly pro Miguel quando envolve outro LLM

**Regra:** quando reportar pro Miguel no chat e a mensagem envolver coordenação com Codex / DeepSeek / Antigravity (pedido pra eles, dúvida sobre o que eles fizeram, resumo do que está acontecendo entre os agentes), escrever em **texto humanizado, conversacional, sem jargão interno**, pensando que Miguel vai **copiar e colar inteiro no chat do outro LLM** sem editar.

**Why:** Miguel é o pombo-correio entre os LLMs do projeto (Claude no terminal, Codex/DS/AG em outros chats). Ele formalizou esse hábito 2026-05-19 ~12:45 BRT depois de eu ter postado 3 versões técnicas com prefixos `[SPRINT X]`, tabelas e checklists num pedido que deveria ter sido texto corrido. Justificativa dele: (a) acelera contato entre agentes — ele não precisa traduzir/resumir; (b) ele mesmo fica atualizado lendo um texto natural em vez de decifrar tabela técnica.

A conversa entre Trindade **dentro** do canal/fórum (`canal_trindade.md`, `forum_*.md`) pode continuar técnica e objetiva — esses arquivos são consumidos por LLMs, ok ter prefixos, tabelas, jargões §X.Y.

A regra vale só pro **chat com Miguel**, especialmente quando o conteúdo será re-transmitido.

**How to apply:**

- Se a mensagem é só pra Miguel (status próprio, achado, "vou fazer X") → resposta normal curta, não precisa humanizar
- Se a mensagem envolve outro LLM (pedido pra eles, contexto sobre o que eles fizeram, dúvida que ele vai consultar com outro) → **texto humanizado copy-paste-friendly**:
  - Tom conversacional, primeira/segunda pessoa
  - Português natural — sem siglas internas (§X.Y, ME-N) sem explicar, sem `[SPRINT X]` prefixos
  - Contexto suficiente: quem é alvo, qual problema, por que importa, o que precisa
  - Sem tabelas técnicas a menos que sejam essenciais e o destinatário consiga ler
  - Pedido/pergunta concreta no fim
  - Sem footer de custo `🤖💵💰` (poluição visual pro destinatário)

**Antipadrões (NÃO fazer pro chat humanizado):**

```
[SPRINT MONITORAMENTO EDITORIAL]
### TASK Codex + DeepSeek (endorsement explícito ME-5)
| ME | Patch | Risco |
|---|---|---|
| ME-5 | ... | 🟢 |
```

**Padrão certo:**

> Codex e DeepSeek, preciso de uma ajuda rápida...
> A história é a seguinte: na revisão editorial do Miguel apareceram problemas de capitalização...
> O que preciso de cada um de vocês é só uma frase curta dizendo se concordam...
> Obrigado. Quando puderem.

**Quando dúvida:** se você imagina Miguel selecionando-tudo-Ctrl+C-Ctrl+V no chat do Codex, está no formato certo. Se imagina ele tendo que editar/reformatar, está errado.

**Caso fundador:** 2026-05-19 sprint Monitoramento Editorial, pedido endorsement ME-5. Postei 3 versões (técnica com prefixos, depois fórum, depois "humanizado mas no fórum") até Miguel reclamar "eu estou falando para postar aqui no chat!!!!". Aprendi que "chat" = janela Claude Code com Miguel, não fórum/canal compartilhado.

Relacionado: [[feedback_re_sincronizar_antes_de_postar_coordenacao]] (re-sync canal/fórum antes de coordenar), [[feedback_canal_e_forum_papeis]] (canal é índice, fórum é detalhe — agora adiciona: chat é pombo-correio humanizado).

— Padrão Miguel 2026-05-19 12:45 BRT.
