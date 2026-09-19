# Incidente editorial — 266360 publicado chamando Kushner de “embaixador”

```yaml
identidade: LAURA-CODEX
tipo: INCIDENTE_EDITORIAL_POS_PUBLICACAO
post_id: 266360
ts_primeiro_publish_observado_brt: 2026-08-18T06:50:37-03:00
horario_nominal_brt: 2026-08-18T06:45:00-03:00
status: publish
modified_brt: 2026-08-18T02:11:34-03:00
featured_media_id: 266365
classificacao: CORRIGIR_CARGO_E_ATRIBUICAO
wordpress_mutations_laura_codex: 0
```

## Achado confirmado

O post 266360 passou de `future` às 06:47:36 para `publish` às 06:50:37 sem
edição desde 02:11:34. O segundo parágrafo publicado diz “o **embaixador Jared
Kushner**”. Essa função está errada:

- a AP o identifica como negociador americano;
- o Axios o identifica como assessor do presidente Trump.

As duas fontes sustentam o núcleo da pauta — Israel e o Board of Peace
concordaram em criar dois grupos de trabalho —, mas delimitam o segundo grupo
como saúde pública/situação humanitária, com atenção a água e saneamento. A AP
também ressalva que a reunião não produziu compromisso concreto de Israel com
o plano americano mais amplo.

O alerta pré-publicação com texto pronto foi enviado às 06:23, cerca de 22
minutos antes do horário nominal, no commit `a5ecf8a9`. A publicação ocorreu
sem incorporar o alerta.

## Recibo público às 06:51

- REST `publish`, mídia 266365, `modified=02:11:34`.
- `<article>` encontrado; CONTENT END 0 no REST e no artigo; Markdown cru 0;
  unicode literal 0; `<br>` escapado 0.
- “embaixador Jared Kushner”: 1 ocorrência no artigo.
- ressalva sobre ausência de compromisso amplo/concreto: 0 ocorrências.
- Alt: “Fachada sul da Casa Branca e o gramado”. Legenda: “Casa Branca vista
  do gramado sul, em Washington. Foto: Rob Young.”
- Estrutura e capa estão limpas; o defeito é factual/editorial.

## Correção recomendada

Substituir a abertura pelos termos já medidos:

> Segundo o gabinete de Benjamin Netanyahu, Israel e o Conselho de Paz criado
> pelos Estados Unidos concordaram em formar dois grupos de trabalho: um sobre
> desarmamento e desmilitarização de Gaza e outro sobre saúde pública e a
> situação humanitária, com foco em água e saneamento. A reunião envolveu o
> negociador americano e assessor de Trump Jared Kushner. A AP ressalvou que o
> encontro não produziu um compromisso concreto de Israel com o plano
> americano mais amplo.

Fontes:

- AP:
  https://apnews.com/article/kushner-trump-netanyahu-board-of-peace-mladenov-18252d84c29658ca13ac3380743953be
- Axios:
  https://www.axios.com/2026/08/17/kushner-netanyahu-hamas-gaza

LAURA-CODEX permaneceu somente leitura e não alterou produção.

— LAURA-CODEX, 18/08/2026 06:51 BRT
