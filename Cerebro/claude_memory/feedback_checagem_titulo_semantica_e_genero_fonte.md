---
name: feedback-checagem-titulo-semantica-e-genero-fonte
description: "Além dos checks óbvios (siglas/caps/fatos/HTML), sempre revisar: (1) gênero da fonte no artigo (Segundo A Folha/Al Jazeera/CNN/Revista Fórum vs Segundo O UOL/SCMP/The Hindu/Poder360); (2) semântica/regência do título (verbos + objetos + tempo verbal x data do evento)."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 9ff9d002-2c71-4670-87db-7c5f55616550
---

**Regra:** Toda checagem dupla de draft V4 deve ir ALÉM dos checks estruturais (siglas, caps, ponto-e-vírgula, HTML, ruído template, fatos verificáveis) e cobrir também:

## 1. Gênero da fonte (artigo)

Toda menção "Segundo [artigo] <a>NomeFonte</a>" tem que casar gênero. Padrões catalogados:

**Femininas (Segundo A):**
- A Folha, A Revista Fórum, A Al Jazeera, A Prensa Latina, A Agência Brasil, A Agência Senado, A BBC, A CNN, A CNN Brasil, A Gazeta do Povo, A Reuters, A Actualidad RT, A Carta Capital (CartaCapital), A Time, A Bloomberg (ambíguo, mas comum como fem)

**Masculinos (Segundo O):**
- O The Hindu, O SCMP, O UOL, O Poder360, O Brasil de Fato, O Opera Mundi, O Metrópoles, O Diário do Grande ABC, O Diário do Rio, O Resumen Latinoamericano, O Brasil 247, O Terra, O G1, O The Times of London (ambíguo, mas comum como masc quando "o jornal The Times"), O Portal (qualquer coisa nomeada "portal")

## 2. Semântica e regência do título

- **Verbo + objeto sem artigo/preposição errada**: "Irã ataca Patriot em Erbil" → confuso; correto: "Irã destrói base de lançamento de mísseis Patriot no Iraque" (verbo específico + objeto claro com artigo).
- **Regência inexistente**: "atacar de X" (não existe), "chamar por X" (deveria "chamar de X").
- **Verbo genérico para fato específico**: "ataca" quando foi "destrói/inutiliza/bombardeia" — usar o verbo real do fato.
- **Fragmentação com aspas soltas**: "de 'ladrão' de novo" → reformular natural ("novamente").
- **Ponto-e-vírgula proibido no título** (regra já existente `feedback_titulos_sem_ponto_virgula`) — reforço aqui.
- **Título sem conector entre orações**: "STJ ganha X aguarda Y" → adicionar "e" ou reformular.

## 3. Tempo verbal x data do evento

- Se o fato aconteceu ONTEM ou dia anterior, verbo tem que estar no PASSADO.
- "Chegam à convenção" só se convenção é HOJE/em curso.
- "Chegaram à convenção" quando convenção foi ontem ou antes.
- Regra prática: comparar data do evento no corpo com data de publicação (hoje). Se diferentes, verbo do título tem que refletir.

## 4. Peso editorial x cat 20699

- Se V4 curou matéria de traje/coreografia/detalhes menores de evento (importante ou não), avaliar se é home-worthy. Se não é, adicionar cat 20699 mesmo se o worker não fez.
- Exemplos de tema tipicamente no-home mesmo em Nacional: visual de militantes, curiosidades de bastidor, hobbies de figuras públicas.

## Casos fundadores (03/08/2026)

- **264062**: "Militantes chegam à convenção" (convenção foi ontem 02/08) → passado + cat 20699 adicionada por peso editorial fraco. Miguel: "traje dos petistas não me parece importante".
- **264068**: "Irã ataca Patriot em Erbil" → "Irã destrói base de lançamento de mísseis Patriot no Iraque". Miguel: "ataca Patriot? o certo é destrói base de lançamento".
- **264054**: "Milei ataca Lula de 'ladrão' de novo" → "Milei ataca Lula novamente". Miguel: "o certo seria Milei ataca Lula novamente".
- **33 posts 02-03/08** corrigidos in-place por "Segundo o [Fonte feminina]" → "Segundo a".

## Como aplicar

Em toda checagem dupla, ANTES de publish:
1. Ler título em voz alta mental — soa natural? Fluente? Verbo específico?
2. Verificar data do evento no corpo — se ontem/anterior, título deve estar no passado.
3. Grep no corpo por "Segundo o " e "Segundo a " — casar com o gênero da fonte.
4. Peso editorial — se tema é frivolidade/curiosidade, adicionar cat 20699.

Regras irmãs: [[feedback-titulos-sem-ponto-virgula-com-autonomia]], [[feedback-checagem-dupla-editorial-com-autonomia]], [[feedback-nacional-tem-no-home-por-score]].
