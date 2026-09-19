# Regra editorial — evento principal, etapas paralelas e datas

**Vigência:** 17/08/2026, imediata  
**Status:** regra viva e bloqueante  
**Aplica-se a:** todos os V4, repetidores, agentes de Cultura, Loop Miguel,
Loop Laura e qualquer agente que selecione, redija, revise, agende ou publique
conteúdo sobre festivais, congressos, feiras, mostras, premiações, eleições,
campeonatos, lançamentos ou outros eventos com várias etapas.

## Regra central

> O agente nunca pode tratar uma etapa paralela, mostra complementar, abertura
> de inscrições, anúncio de selecionados ou cerimônia como se fosse o evento
> principal. Nome parecido e data recente não tornam duas etapas equivalentes.

## Ficha factual obrigatória

Antes de liberar o texto, o agente deve preencher e conferir:

1. nome oficial e número da edição;
2. natureza exata da etapa: evento principal, mostra paralela, inscrição,
   seleção, premiação, itinerância, reprise ou atividade complementar;
3. data inicial e data final dessa etapa;
4. cidade, local e formato;
5. quantidade e unidade corretas: obras inscritas, selecionadas, exibidas,
   sessões, convidados ou atividades — não misturar esses universos;
6. fonte oficial usada, URL e data de publicação ou atualização da página;
7. fato novo que justifica a matéria naquele dia.

Sem essa ficha, o resultado obrigatório é `HOLD_PENDING_EVENTO_AMBIGUO`.

## Hierarquia de fontes

1. programação, regulamento ou comunicado do organizador;
2. assessoria ou instituição responsável;
3. veículo jornalístico independente, como confirmação adicional.

Release, snippet de buscador, republicação e matéria de terceiro não substituem
a fonte oficial para datas, edição, número de selecionados e nome da etapa. Se
duas páginas oficiais divergirem, o agente não escolhe silenciosamente uma
delas: registra a divergência, faz nova busca e mantém o post em `pending`.

## Teste de identidade do evento

Antes da aprovação, responder literalmente:

- "Qual etapa começa nessa data?"
- "O evento principal já aconteceu?"
- "O número citado se refere a inscritos, selecionados ou exibidos?"
- "O título e o lide nomeiam a etapa correta?"

Se a resposta a qualquer pergunta for incerta, é proibido agendar ou publicar.

## Proibições objetivas

- Não fundir calendários de etapas diferentes.
- Não chamar "Mostras Paralelas" de "49ª edição do festival".
- Não converter quantidade de inscrições em quantidade de obras exibidas.
- Não usar o presente ou o futuro só porque a página consultada é recente.
- Não completar datas ou números por inferência.
- Não escrever título mais amplo do que a prova disponível.

## Gate final do revisor

O revisor com WebSearch deve abrir a fonte oficial, comparar título e lide com
a ficha factual e registrar um dos vereditos:

- `APROVA_EVENTO_IDENTIFICADO`;
- `REPROVA_ETAPA_CONFUNDIDA`;
- `HOLD_PENDING_EVENTO_AMBIGUO`.

Fact-check por conhecimento interno do modelo, sem busca real, não vale. O
agente que redigiu não pode considerar a própria interpretação como segunda
fonte. Em caso de dúvida, Loop Miguel decide; Loop Laura faz a redundância
read-only.

## Incidente fundador — post 266143

O texto tratou as Mostras Paralelas do Festival Guarnicê como se fossem a 49ª
edição principal. Também fundiu datas e quantidades: a edição principal ocorreu
de 9 a 16/07/2026; as Mostras Paralelas foram anunciadas para 20 a 24/08/2026,
com 87 obras selecionadas. A matéria dizia 20 a 26/08 e cerca de 150 obras.

**Lição:** uma fonte pode ser recente e verdadeira, mas o agente ainda pode
atribuir seus dados à fase errada do evento. A unidade factual é
`evento + edição + etapa + datas + universo contado`, nunca apenas o nome do
festival.
