---
name: feedback-encurtar-titulo-sem-quebrar-sintaxe-20260817
description: "Ao encurtar título pra caber ≤80 chars, NUNCA sacrificar sintaxe. Trocar verbo/reformular frase é melhor que tirar preposição obrigatória. Origem: incidente 266195 17/08 15:20 — cortei 'sobre' de 'alerta sobre pressão' pra caber em 80, ficou 'alerta pressão' (erro gramatical grave). Miguel: 'quem escreveu essa porcaria?'."
metadata:
  node_type: memory
  type: feedback
  originSessionId: e8e1110d-efa6-4c4b-8e2b-d11b38f55da8
---

Ao encurtar título pra caber ≤80 chars (regra auditor), **NUNCA remover preposição obrigatória do regime verbal**. Sacrifica sintaxe = título fica errado, Miguel corrige na hora.

**Why:** incidente 266195 17/08 15:14 — auditor sugeriu "Marco Rubio defende capitalismo e alerta sobre pressão dos EUA na eleição brasileira" (84 chars, viola ≤80 por 4). Eu apliquei, wp calculou 84, encurtei tirando "sobre" → "Marco Rubio defende capitalismo e alerta pressão dos EUA na eleição brasileira" (78 chars). Miguel chegou 15:22: *"esse titulo alerta pressão dos EUA está errado. quem escreveu essa porcaria?"*. "Alertar" é intransitivo/pronominal — regime pede "sobre/para/contra": "alerta sobre X", "alerta para X", "alerta-se sobre X". Sem preposição é agramatical, parece que o objeto direto é "pressão" (quem alerta pressão? ninguém alerta uma pressão diretamente).

**How to apply:**
1. **Se sugestão auditor tem >80 chars**, NÃO tirar preposição/artigo obrigatório. Preferir:
   - trocar verbo por sinônimo mais curto ("alerta sobre" → "revela", "expõe", "denuncia", "aponta")
   - remover palavra decorativa ("Marco" antes de nome próprio já conhecido; "muito", "realmente", "novamente")
   - remover complemento circunstancial ("na eleição brasileira" → "no Brasil"; "sobre a eleição" → nada, contexto do post basta)
   - reformular sujeito ("Marco Rubio defende X e alerta sobre Y" → "Discurso de Rubio expõe X e Y")
2. **Fazer checagem mental de 3 passos ANTES de gravar:** (a) o título é uma oração completa? (b) o verbo principal tem seu objeto/complemento pedido pelo regime? (c) leitor entende sujeito x objeto sem ambiguidade?
3. **Casos de verbos que EXIGEM preposição** (grep antes de encurtar):
   - alertar → sobre/para/contra
   - avisar → sobre/de
   - aspirar → a
   - preferir → a
   - assistir → a (quando "presenciar")
   - visar → a (quando "objetivar")
   - obedecer/desobedecer → a
   - responder → a
   - insistir → em
   - depender → de
   - discordar/concordar → com/de
4. **Fórmula de emergência quando nada cabe**: reescrever com "Discurso/Fala/Vídeo/Análise de X revela Y" — sempre curto e sintaxe travada.

**Lição maior:** título que atende auditor (≤80) mas está agramatical FALHA no editorial. Miguel exige AMBOS: chars OK **e** gramática OK. Melhor pagar 82 chars com sintaxe correta do que 78 quebrado — se for esse o dilema, escrever bloco pro ZCode revisar regra auditor pra aceitar overflow de 2-4 chars quando sintaxe protege sentido. Mas antes disso, tentar reformular.

Relacionado: [[feedback-auditor-titulos-entrega-diaria-inbox-20260817]] (auditor é advisor não bloqueador — posso adaptar sugestão), [[project-cadencias-trindade-20260817]] (Grok OFF, ZCode `*/30`).
