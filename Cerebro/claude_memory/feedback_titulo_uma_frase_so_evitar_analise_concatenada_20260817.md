---
name: feedback-titulo-uma-frase-so-evitar-analise-concatenada-20260817
description: "Título Cafezinho: UMA frase só, focada no fato principal. Se aparecer 'X e Y' onde Y é análise/consequência subjetiva ('colapsa mandato', 'sinaliza crise', 'expõe fraqueza'), CORTAR Y e ficar só com X. Sugestão/orientação (não bloqueia). Miguel 17/08/2026 18:15 BRT — incidente 266313 'Trump bate recorde de impopularidade E colapsa o próprio mandato'."
metadata:
  node_type: memory
  type: feedback
  originSessionId: e8e1110d-efa6-4c4b-8e2b-d11b38f55da8
---

Miguel 17/08/2026 ~18:15 BRT (referindo-se ao post 266313 recém-publicado):

> "auditor de titulo e os titulos continuam esquisitos! auditor de titulos, v4, claude, loop laura, e ainda assim os titulos são ruins. o certo aqui é 'Trump bate recorde de impopularidade'. vamos focar numa frase só. 'colapsa o proprio mandato' é uma frase estranha. corrige lá e faz uma nova diretriz, mas sem bloquear nada, sugestao, orientação."

**Título original:** "Trump bate recorde de impopularidade e colapsa o próprio mandato" (65 chars)
**Título corrigido por Claude 18:15 BRT:** "Trump bate recorde de impopularidade" (36 chars)

**Por que "colapsa o próprio mandato" é problema:**
- Segunda oração adiciona ANÁLISE/CONSEQUÊNCIA subjetiva, não fato
- "Colapsar mandato" é metáfora política forte — se acontecer no corpo com fonte, ok; mas título vira sentença editorial sem lastro
- Título forte é o que já traz o fato (impopularidade recorde) — anexar análise dilui, não fortalece
- Frase única = leitor pega a manchete em 1 segundo; frase dupla = leitor titubeia entre 2 ideias

**Diretriz (SUGESTÃO/ORIENTAÇÃO — não bloqueia publish):**

Ao editar/promover título V4 ou de qualquer origem no Cafezinho:

1. **Preferir 1 fato central por título.** Se o modelo/worker/auditor gerou "X e Y", perguntar: **Y é fato novo mensurável? Ou é análise/consequência/adjetivo?**
   - **Y fato novo** (número, decisão, ação verificada) → manter conjunto se couber ≤80 chars
   - **Y análise/consequência/metáfora** ("colapsa mandato", "expõe fraqueza", "sinaliza crise", "muda paradigma") → **CORTAR Y**, deixar só X
2. **Verbos-sinal de análise concatenada** a evitar como 2ª ideia: `colapsa`, `sinaliza`, `expõe`, `desafia`, `revela`, `redesenha`, `abala`, `sepulta`, `enterra`, `redimensiona`, `redefine`. Se aparecer como verbo principal (frase única), pode; se aparecer depois de `e/mas/enquanto`, cortar.
3. **Fórmula segura por vertical** (herdada dos contratos V4):
   - Nacional/Política: `sujeito + verbo factual + objeto/número`
   - Economia: `dado + o que muda`
   - Cultura: `cena + significado curto`
   - Meio-amb: `fato + escala + bioma`
   - Esporte: `sujeito + ação + placar`
   - Saúde: `fato + magnitude + local`
   - Geopolítica: `sujeito + ação HOJE + contexto se couber`
4. **Regra pré-existente que continua valendo:** ≤80 chars ([[feedback-encurtar-titulo-sem-quebrar-sintaxe-20260817]]), sem `:`/`—`/`...`, sentence case, verbo concreto.
5. **Auditor de títulos NYC** ([[feedback-auditor-titulos-entrega-diaria-inbox-20260817]]) já pega "duas ideias concatenadas" (regra 2). Esta diretriz é MAIS ESTRITA: mesmo quando as duas ideias são FACTUAIS, se a 2ª é análise/consequência não medida, cortar. Complementa o auditor, não substitui.
6. **Não bloqueia publish.** É sugestão editorial. Loop Miguel aplica a orientação ao revisar; Loop Laura pode sugerir edição via alerta §126. Auditor não vira bloqueador.

**How to apply (checklist ao ver título antes de wp_update_post):**
- Título tem "e" no meio? Ler as 2 metades separadas.
- 2ª metade tem verbo de análise (lista acima)? Cortar 2ª metade.
- 2ª metade é adjetivo forte ("crítico", "histórico", "sem precedentes")? Cortar.
- 2ª metade é número/decisão/nome próprio? Manter (é fato).
- Resultado final ainda ≤80 chars? Se cortou virou <40 chars, também OK — título curto e forte é preferível a longo e diluído.

**Comunicação:** ordem Miguel foi "sem bloquear nada, sugestão, orientação". Registrar na inbox_trindade/claude.md pra ZCode e Codex reforçarem no auditor NYC (nova regra 8 opcional?) e nos workers V4. Alertar Laura pra incluir no ACK dela quando pegar título ruim.

**Origem:** incidente 266313 "Trump bate recorde de impopularidade e colapsa o próprio mandato" (autor 5780, publish 17:48 BRT). Corrigido pelo Claude in-place 18:15 BRT para "Trump bate recorde de impopularidade" (36 chars). Miguel: "vamos focar numa frase só".

Relacionado: [[feedback-encurtar-titulo-sem-quebrar-sintaxe-20260817]] (não sacrificar sintaxe pra caber), [[feedback-auditor-titulos-entrega-diaria-inbox-20260817]] (auditor advisor), [[feedback-laura-alertas-entrada-obrigatoria-20260817]] (Laura como entrada obrigatória — pode sugerir simplificação).
