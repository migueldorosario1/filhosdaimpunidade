---
name: feedback-checagem-dupla-editorial-com-autonomia
description: "Claude tem AUTONOMIA total pra fazer checagem dupla + corrigir + publicar drafts V4 (Cafezinho) — não pedir OK do Miguel a cada caso, só reportar depois; regra fundadora 27/07 06:37 BRT no caso 263017 (Irã/EUA)"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 0c239f1e-08c3-4beb-a91e-5adf020d8159
---

**Regra:** Claude Code deve tomar autonomamente as decisões editoriais de última milha nos drafts V4 do Cafezinho — quando faz checagem dupla depois do DeepSeek, se identifica erro e sabe o remédio certo, aplica direto (patch + publish + registro 3 camadas) e reporta ao Miguel DEPOIS. Não pedir OK a cada caso. Escalar só se: (a) proposta implicar mudança editorial de fundo (ângulo político, escolha de fonte primária vs secundária), (b) dúvida real sobre o fato mesmo depois de WebSearch, (c) ação irreversível grande (deletar post publicado, mudar autor, mexer em URL indexada).

**Why:** Miguel 27/07 06:37 BRT, imediatamente após meu primeiro caso de checagem dupla (draft 263017 Irã/EUA): *"mas esse é o tipo de decisão que eu quero que voce tome autonomamente"*. Contexto: eu tinha detectado que a proposta do DeepSeek (junho→julho) manteria "domingo 25/07" quando 25/07 foi sábado, fiz WebSearch, achei o remédio certo (domingo 26/07), preparei o patch mas pedi OK antes de publicar. Miguel corrigiu — quer fluxo autônomo. O ponto do pedido de "checagem dupla" NÃO é criar gate humano, é ter minha camada de verificação factual antes de qualquer publicação, e depois decidir sozinho.

**How to apply:**
- Todo draft V4 que aparecer na esteira, se DeepSeek propõe correção semântica OU eu detecto erro por conta própria: WebSearch pra confirmar fato → aplicar remédio correto (não necessariamente o do DeepSeek) → publish → 3 camadas (JSONL bugs + manual se padrão novo + memória se regra nova) → ponteiro no canal_trindade.
- Backup SHA-256 antes do patch é obrigatório (regra AUTOCURA irmã [[autocura-protocolo-registro-com-solucao-e-rollback]]).
- Reportar ao Miguel DEPOIS em bloco curto: o que estava errado, o que corrigi, link do post publicado, quaisquer lições novas.
- Escalar ANTES de agir só nos 3 casos listados acima (mudança de fundo / dúvida real / ação irreversível grande).
- Se dúvida real: WebSearch primeiro, se ainda houver dúvida → aí sim escalar.
- Aplica a: correções de data, cargo (com [[nome-proprio-figura-publica-nunca-publish-com-proposta]]), grafia, ortografia, factos objetivos verificáveis, número/valor.
- NÃO aplica a: mudanças de enquadramento editorial (título com ângulo, escolha de qual figura destacar), decisão sobre incluir/excluir bloco inteiro do post, retirada de posts já publicados.

**Caso fundador (draft 263017, 27/07 06:37 BRT):**
DeepSeek propôs "25 de junho → 25 de julho" (só o mês). Meu WebSearch (CNN, CBS, NPR, Fox, referência The Hindu) mostrou: pausa mútua começou domingo 26/07 (EUA pausou sex+sáb à noite; Irã aderiu no domingo). Correção real: "domingo, 25 de junho de 2026" → "domingo, 26 de julho de 2026" + "sexta-feira, 24 de junho" → "sexta-feira, 24 de julho". Publiquei com essa correção após OK do Miguel. Próximo caso similar: aplico sem pedir OK.

**Regra irmã:** [[sempre-pesquisar-web-em-duvida]] — quando eu não tenho certeza, WebSearch sempre precede a ação. Combinadas: primeira faz o gate de verificação, esta dá autonomia pra executar depois do gate passar.
