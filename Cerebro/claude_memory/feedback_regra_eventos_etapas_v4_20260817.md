---
name: feedback-regra-eventos-etapas-v4-20260817
description: "REGRA CRÍTICA vigente 17/08/2026: gate obrigatório contra confusão entre evento principal e etapa paralela (mostras/inscrições/premiações/itinerâncias/reprises). Aplica-se a festivais, congressos, feiras, mostras, campeonatos, eleições, lançamentos. Ficha factual obrigatória antes de agendar/publicar: evento + edição + etapa + datas + local + universo contado + fonte oficial + fato novo. Divergência/dúvida = veredito HOLD_PENDING_EVENTO_AMBIGUO, nunca agendar/publicar. Hierarquia de fontes: (1) organizador oficial (regulamento/comunicado); (2) assessoria/instituição; (3) veículo jornalístico apenas como confirmação. Release/snippet/republicação NÃO substituem fonte oficial. Incidente fundador: post 266143 (Guarnicê) que agendei 21:32 e publicou 23:00 com número '150 obras' não confirmado (Mostras Paralelas têm 83-87). Vereditos: APROVA_EVENTO_IDENTIFICADO / REPROVA_ETAPA_CONFUNDIDA / HOLD_PENDING_EVENTO_AMBIGUO. Origem: CODEX-MIGUEL-REGRA-EVENTOS-ETAPAS-20260817-0132, ordem direta Miguel. Documento canônico: cerebro/Foruns/diretrizes/regra_evento_principal_etapas_paralelas_v4_20260817.md."
metadata:
  node_type: memory
  type: feedback
  originSessionId: d556bf3a-514a-43d5-a6d6-417905366fd5
---

## Regra vigente (17/08/2026 imediata, ordem direta Miguel via Codex)

**Documento canônico:** `cerebro/Foruns/diretrizes/regra_evento_principal_etapas_paralelas_v4_20260817.md`

**Aplica-se a todo agente** (V4, repetidor, agentes de Cultura, Loop Miguel, Loop Laura, qualquer redator/revisor/agendador/publicador) que trate:
- festivais
- congressos
- feiras
- mostras
- premiações
- eleições
- campeonatos
- lançamentos
- qualquer evento com múltiplas etapas

## Regra central textual (Codex)

> "O agente nunca pode tratar uma etapa paralela, mostra complementar, abertura de inscrições, anúncio de selecionados ou cerimônia como se fosse o evento principal. Nome parecido e data recente não tornam duas etapas equivalentes."

## Ficha factual obrigatória (checklist pré-publish)

Antes de liberar texto (agendar `future` ou publicar), preencher e conferir:

1. **Nome oficial** do evento + **número da edição**
2. **Natureza exata da etapa**: evento principal / mostra paralela / inscrição / seleção / premiação / itinerância / reprise / atividade complementar
3. **Data inicial e final** dessa etapa específica
4. **Cidade, local, formato** (presencial/híbrido/online)
5. **Quantidade e unidade correta**: obras inscritas ≠ selecionadas ≠ exibidas ≠ sessões ≠ convidados ≠ atividades (nunca misturar universos)
6. **Fonte oficial usada**: URL + data de publicação/atualização
7. **Fato novo** que justifica a matéria naquele dia

Sem ficha completa → **`HOLD_PENDING_EVENTO_AMBIGUO`** obrigatório.

## Hierarquia de fontes (v4)

1. **Programação/regulamento/comunicado do organizador** (site oficial, edital)
2. **Assessoria/instituição responsável** (UFMA, TSE, CBF, ministério, etc.)
3. **Veículo jornalístico independente** apenas como confirmação adicional

**Release + snippet de buscador + republicação + matéria de terceiro NÃO substituem** fonte oficial para datas, edição, número de selecionados, nome de etapa. Divergência entre páginas oficiais → registrar divergência + nova busca + manter `pending`. Nunca escolher silenciosamente uma.

## Teste de identidade do evento (obrigatório, antes de aprovar)

Responder literalmente:
- "Qual etapa começa nessa data?"
- "O evento principal já aconteceu?"
- "O número citado se refere a inscritos, selecionados ou exibidos?"
- "O título e o lide nomeiam a etapa correta?"

Qualquer resposta incerta → proibido agendar/publicar.

## Proibições objetivas

- Não fundir calendários de etapas diferentes
- Não chamar "Mostras Paralelas" de "49ª edição do festival"
- Não converter inscrições em obras exibidas
- Não usar presente/futuro só porque a página consultada é recente
- Não completar datas/números por inferência
- Não escrever título mais amplo do que a prova disponível

## Vereditos do gate final (revisor com WebSearch)

- **`APROVA_EVENTO_IDENTIFICADO`** — ficha completa, fonte oficial confere
- **`REPROVA_ETAPA_CONFUNDIDA`** — texto trata etapa como evento principal (ou vice-versa)
- **`HOLD_PENDING_EVENTO_AMBIGUO`** — dúvida factual, divergência entre fontes, fonte oficial inacessível

**Fact-check por conhecimento interno do modelo, sem busca real, NÃO vale.** Agente que redigiu não pode considerar própria interpretação como segunda fonte. Loop Miguel decide em dúvida; Loop Laura é redundância read-only.

## Incidente fundador — 266143 Festival Guarnicê

**Meu ciclo Slot B 21:32 do 16/08**: agendei o post 266143 (Guarnicê) para 23:00, aprovado por gate visual §5 (Teatro Arthur Azevedo APROVA_CONTEXTUAL) e checklist V4 (fonte invisível/densidade/veículos). **NÃO validei factualmente**:

- Título dizia "reúne 150 obras" — número **não confirmado** pela UFMA. Fontes divergem:
  - UFMA/PROEC: 87 obras nas Mostras Paralelas + números não declarados de Competitivas + Universitária + Jogos Digitais
  - Cubo/Imirante: 83 obras nas Mostras Paralelas (só a etapa não competitiva)
  - **150 é interpretação errada** — provavelmente soma que ninguém oficialmente publicou

- Datas: UFMA confirma **20-26/08 para 49ª edição** (agosto). Codex inicialmente reportou "9-16/07 evento principal + 20-24/08 Mostras Paralelas" mas a WebSearch (01:45 do 17/08) mostrou que UFMA diz 20-26/08 para a edição inteira. Divergência de datas persiste entre Cubo (20-24) e UFMA (20-26) — cabe HOLD, não afirmação categórica.

**Correção in-place aplicada 01:48 do 17/08:**
- Título antigo: "Festival Guarnicê de Cinema reúne 150 obras em São Luís" (55c) — número não sustentado
- Título novo: "Festival Guarnicê abre 49ª edição em São Luís com programação híbrida" (69c) — sem número, com fatos sustentáveis
- Corpo antigo: "cerca de 150 produções selecionadas entre mais de 1,4 mil inscritas"
- Corpo novo: "As Mostras Paralelas, subprograma não competitivo, reúnem entre 83 e 87 obras selecionadas de 22 estados brasileiros; os números das mostras competitivas (Nacional e Maranhense), Universitária, de Jogos Digitais e infantojuvenil compõem a grade completa da edição." — declara faixa 83-87 explicitando etapa e usa "grade completa da edição" para o total sem inventar número
- Backup: `/root/snapshots_pre_edit/266143_regra_eventos_20260817_014800.json`

**Lição:** uma fonte pode ser recente e verdadeira, mas o agente pode atribuir dados à fase errada do evento. **A unidade factual é `evento + edição + etapa + datas + universo contado`, nunca apenas o nome do festival.**

## Meu procedimento revisado (Loop Miguel Vigília V6, a partir de 17/08 01:48)

Ao encontrar draft V4 sobre **festival/congresso/feira/mostra/premiação/eleição/campeonato/lançamento**:

1. Extrair do corpo os 7 campos da ficha factual
2. WebSearch dirigida à fonte oficial (site institucional, edital, comunicado)
3. Comparar título + lide + números com fonte oficial
4. Se qualquer campo incerto ou divergente → **`HOLD_PENDING_EVENTO_AMBIGUO`** + escalar (Grok pesquisa suplementar, Laura segunda vista, Miguel decisão)
5. Se ficha completa e sustenta o texto → `APROVA_EVENTO_IDENTIFICADO` + agendar normalmente com gate §5
6. Se texto trata etapa como evento principal (ou vice-versa) → `REPROVA_ETAPA_CONFUNDIDA` + corrigir com escopo real da etapa OU escalar para reescrita editorial

Custo adicional: 1-3 min por post de evento. Compensa: evita post publicado com dado errado (que Laura teria que pegar depois, como no 266143 e 266158).

## Relacionados

- [[feedback-worker-v4-perde-credito-foto-original-20260816]] — bug 2 do worker V4 (crédito foto)
- [[feedback-contrato-integridade-imagens-v1-homologado-20260816]] — §5 gate visual (não substitui gate factual)
- [[feedback-ritual-ler-memoria-toda-acao-editorial-20260815]] — reancorar memória antes de agir
- Documento canônico: `cerebro/Foruns/diretrizes/regra_evento_principal_etapas_paralelas_v4_20260817.md`

## Regra âncora

**"Uma fonte pode ser recente e verdadeira, mas o agente pode atribuir dados à fase errada do evento. Ficha factual: evento + edição + etapa + datas + local + universo contado + fonte oficial + fato novo. Sem ficha completa: HOLD_PENDING_EVENTO_AMBIGUO. Divergência entre fontes: registrar divergência, buscar mais, nunca escolher silenciosamente. Fact-check por conhecimento interno sem busca real NÃO vale."** — Codex Miguel por ordem direta Miguel, 17/08/2026 01:32 BRT (incidente fundador 266143).
