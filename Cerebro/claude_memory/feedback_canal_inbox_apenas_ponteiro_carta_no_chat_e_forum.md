---
name: canal-inbox-apenas-ponteiro-carta-no-chat-e-forum
description: "canal_trindade.md e inbox_trindade/*.md são APENAS ponteiros curtos (1-2 linhas); conteúdo longo (\"carta\"/\"cartinha\") vai no chat com Miguel + cópia no fórum canônico"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: f333da72-7610-439d-ab22-49569ae85b4a
---

**REGRA:** `canal_trindade.md` e `inbox_trindade/*.md` armazenam APENAS **ponteiros curtos** (1 linha no canal, 1-3 linhas no inbox) apontando pro fórum canônico onde está o conteúdo. Nunca colar conteúdo longo nesses arquivos.

Quando Miguel disser "**carta**" ou "**cartinha**" — ele quer o conteúdo:
1. **Escrito AQUI no chat** (pra ele visualizar em tempo real)
2. **Copiado no fórum canônico** (pra persistência e outros agentes lerem)

Não no inbox. Não no canal.

**Why:** Miguel 26/07 13:00 BRT: *"não, a carta é aqui no chat e no forum. o inbox é apenas ponteiro, assim como o canal !!!"*. E depois 13:02 BRT: *"quando eu falar carta, ou cartinha, é aqui no chat, mas sempre copiando também no forum"*. Contexto: escrevi uma carta longa de 9 seções detalhando escalação Kimi K3 (bug duplo fact-check + Brave) direto no `inbox_trindade/kimi.md` — errado. Miguel corrigiu duas vezes seguidas. Ele quer o fluxo assíncrono limpo: canal = tag+link, inbox = mensagem curta "leia isto no fórum", fórum = single source of truth pra outros agentes. E chat = comunicação viva com ele, onde ele vê o que estou dizendo em tempo real.

**How to apply:**
- **Ponteiro no canal_trindade.md:** `[TAG] YYYY-MM-DD HH:MM BRT — autor → destinatário — 1-2 frases + link fórum`
- **Ponteiro no inbox_trindade/<agente>.md:** cabeçalho "## [YYYY-MM-DD HH:MM BRT] Autor → Destinatário", 1-3 parágrafos curtos ("Fórum: xxx.md — contexto de 1 linha — leia §6 e responda §10")
- **Carta/cartinha:** escrevo no chat como resposta ao Miguel (formatada, seções, detalhes técnicos), e cria/atualiza fórum canônico com o mesmo conteúdo pra persistência
- **Se em dúvida:** default = ponteiro curto no canal/inbox, conteúdo detalhado no fórum + chat

Regras irmãs: [[autocura-protocolo-registro-com-solucao-e-rollback]], [[protocolo-memoria-bugs-ler-antes-agir]].
