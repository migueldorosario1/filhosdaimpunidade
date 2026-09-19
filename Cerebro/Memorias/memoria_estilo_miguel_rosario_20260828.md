# 🖋️ MEMÓRIA DE ESTILO — Miguel do Rosário (todos os textos)

> Criada por ordem do Miguel em 28/08/2026 ("todo texto meu vai ter a mesma característica"; ele pediu para consolidar — referência anterior: os manuais de estilo do Filhos da Impunidade). Vale para: portal LOGIS, artigos, editoriais, revista, livro, propostas.

## REGRA Nº 1 — PROIBIDA A REPETIÇÃO DE PALAVRAS/VERBOS NA MESMA FRASE OU PARÁGRAFO
O maior vício apontado. Casos reais que o Miguel mandou corrigir (28/08, artigo "A logística do crime"):

- ❌ "O Brasil **tem** projeto, **tem** a tecnologia no papel e **tem** agora o debate aberto no Senado."
  ✅ "O Brasil tem o projeto, a tecnologia pronta no papel e o debate aberto no Senado." (um verbo só para a lista inteira)
- ❌ "Não **é** a soja, não **é** a indústria. **É** o crime organizado."
  ✅ "Quem embarcou primeiro foi o crime organizado, deixando para trás a soja e a indústria."
- ❌ "Obra sem vigilância não **é obra**, **é** presente entregue a quem comete crime."
  ✅ "Obra sem vigilância deixa de ser obra. Ela vira presente entregue a quem comete crime."
- ❌ "A reação institucional **veio**, e **veio** tarde."
  ✅ "A reação institucional só chegou tarde."
- ❌ "**É** o cenário que ninguém quer desenhar, e não **é** ficção." (a palavra "ficção" soa deslocada)
  ✅ reformular sem o eco: "O cenário que esse erro desenha está mais próximo do que parece."
- ❌ "O preço humano **também entra na conta**." (confuso, não explica)
  ✅ dizer o que é: "Nenhuma dessas contas se fecha sem o preço humano. Entre 28,5 e 68,7 milhões..."

**Método de verificação:** antes de publicar, ler o texto em voz alta procurando ECO de palavra (mesma palavra 2× na frase, mesmo verbo na mesma oração, mesmo radical em parágrafos contíguos). Regex ajuda: `\b(\w{4,})\b .{0,80}\b\1\b` por parágrafo.

## REGRA Nº 2 — vícios de IA já banidos (consolidado)
- Máximo **2 frases por parágrafo**.
- **Sem frase vazia** (meta-comentário: "a tese cabe numa frase", "convém dizer", "o preço tem censo próprio", "tem nome, e é feio", "a definição exata de").
- **Dois-pontos no corpo: tendendo a zero** (fazer ponto final/vírgula/verbo).
- **Travessões: tendendo a zero** (terminar a frase e iniciar outra).
- **Sem ligação preguiçosa**: "portanto", "por isso", "ou seja", "de fato".
- **Sem destinatário implícito**: "entregar" (a quem?), "presentear" (o quê?) — sempre dizer o objeto ("entregar **para o crime organizado**").
- **Zero vulgaridade** ("problema grosso" etc.), **zero jargão** técnico sem tradução.
- **Nunca preço** do selo; **Casa da Moeda nunca protagonista**.
- Fonte visual: corpo em **Nunito**, quase-preto, alto contraste.

## Contexto de origem
O Miguel lembra que já havia pedido memória de estilo na época do Filhos da Impunidade — o registro existente era o índice de manuais em `CEREBRO_NODE_LIVRO_FILHOS_DA_IMPUNIDADE.md` (sem arquivo próprio de estilo). Esta memória é a consolidação permanente; os manuais do livro seguem onde estão.

## REGRA Nº 3 — MÚSICA DO TEXTO (cacofonia e escolha de verbo) — adicionada 29/08
Ordem do Miguel: "pente fino na música do texto" — a cada correção, esta memória de estilo é atualizada. Casos reais:
- ❌ "**carrega carga**" (cacofonia car/car, antipoético) → ✅ "não carrega fuzil. **Leva mercadoria**, e viaja sem que ninguém pergunte o que há dentro."
- ❌ "o Brasil **desenha** os corredores" (verbo fraco) → ✅ "o Brasil **constrói** os corredores" (verbo forte; usar os adjetivos/verbos certos, com peso).
- ❌ "**custa cerca** de" (eco silábico) → ✅ "**chega a cerca de**".
- ❌ eco de artigo+substantivo encadeado: "**as aduanas** conferiam **as cargas** nos portos" → ✅ "**aduanas** conferiam **cargas** nos portos".
- ❌ ponto e vírgula de paralelismo: "O tiro saiu da equação; entrou a planilha." → ✅ "O tiro saiu da equação, e a planilha entrou no lugar."
- ✅ Aliteração deliberada com sentido permanece ("frotas de guerra, portos fortificados"; "mar vigiado e carga conferida").
**Método:** ler em voz alta antes de publicar; caçar ecos de sílaba (car-/car-, cus-/cer-), sequências as+substantivo+as+substantivo, e perguntar "o verbo tem peso ou é neutro demais?".

## REGRA Nº 4 — SEM SPOILER NEM ANÚNCIO DO ÓBVIO (29/08)
Ordem do Miguel: "corta 'a conta assusta'. É óbvia. O leitor já vai ver isso pela informação. Não precisa dar o spoiler."
- ❌ "A inteligência do Ministério Público de São Paulo mediu o adversário, **e a conta assusta**. Ela estima..." (a frase anuncia a reação do leitor antes do dado)
- ✅ "A inteligência do Ministério Público de São Paulo mediu o adversário. Ela estima, desde maio de 2026, que o PCC fature US$ 2 bilhões por ano..."
**Regra:** deixar o número assustar sozinho. Cortar toda frase que diga ao leitor o que sentir ("assusta", "impressiona", "choca", "o pior ainda vem") — o fato entrega a emoção sem intérprete.
