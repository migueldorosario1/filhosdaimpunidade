# Sugestões de prompt pro worker V4 — consolidado do Claude

**Última atualização:** 2026-08-11 15:43 BRT
**Total de críticas registradas:** 7
**Categorias distintas:** 7

**Origem:** este arquivo é gerado automaticamente a partir do campo `critica_worker_v4` embedado nos JSONL de bugs do ciclo Vigília V5 do Claude Code (`Cerebro/monitoramento_horario/bugs_encontrados/bugs_*.jsonl`). Cada crítica vem de um bug editorial que o Claude corrigiu manualmente após WebSearch e que teria sido evitado se o worker tivesse aplicado a diretriz sugerida no momento da geração do draft.

**Como o worker deve usar:** ler este arquivo INTEIRO no início de cada geração de draft. As sugestões abaixo são regras editoriais e factuais que o Cafezinho consolidou. Aplicá-las tende a reduzir taxa de reescrita pelo Claude na 4ª camada.

---

## Ranking de categorias por recorrência

- **confusao_temporal_agenda** — 1 ocorrência(s)
- **omissao_ativo_dolar_sumido** — 1 ocorrência(s)
- **duplicata_reincidente_mesma_pauta** — 1 ocorrência(s)
- **omissao_defesa_lado_contrario_post_sensivel** — 1 ocorrência(s)
- **traducao_desnecessaria_de_sigla_conhecida** — 1 ocorrência(s)
- **impreciso_juridico_inelegibilidade** — 1 ocorrência(s)
- **ruido_template_admite_fonte_interna** — 1 ocorrência(s)

---

## Sugestões de prompt por categoria

### `confusao_temporal_agenda` (1 ocorrência)

**Gravidade:** media
**Vertical(is) afetada(s):** nacional
**Recorrência esperada:** vertical_nacional_politica

**Descrição:** Worker misturou 2 datas do TSE (reunião preparatória 13/08 vs julgamento semana 17/08). Ambas caem em 'semana de 17 de agosto' no draft — leitor não distingue reunião de decisão.

**Sugestão de prompt:**

> Ao processar notícias sobre agenda de tribunal/congresso, separar CADA compromisso individualmente com data específica. Nunca condensar reunião+decisão na mesma data se são eventos distintos.

**Casos registrados:**
- 2026-08-11T11:29 · post 265216 · Worker misturou 2 datas do TSE (reunião preparatória 13/08 vs julgamento semana 17/08). Ambas caem em 'semana de 17 de agosto' no draft — leitor não d

---

### `omissao_ativo_dolar_sumido` (1 ocorrência)

**Gravidade:** media
**Vertical(is) afetada(s):** nacional
**Recorrência esperada:** vertical_nacional_politica

**Descrição:** Worker mencionou apenas que 'a prestação atual não registra imóveis residenciais', mas OMITIU o desaparecimento de ativos americanos (McDonald's, 3M, Coca-Cola, Bitcoin, contas EUA) que estavam em 2024. Isso é insight editorial forte pra Cafezinho e o worker perdeu.

**Sugestão de prompt:**

> Ao processar declaração de bens candidato a político, comparar SEMPRE com declarações anteriores e destacar ATIVOS QUE SUMIRAM ou apareceram do nada. Sumiço de dólar/cripto/ações estrangeiras é insight editorial obrigatório em post do Cafezinho.

**Casos registrados:**
- 2026-08-11T11:56 · post 265221 · Worker mencionou apenas que 'a prestação atual não registra imóveis residenciais', mas OMITIU o desaparecimento de ativos americanos (McDonald's, 3M, 

---

### `duplicata_reincidente_mesma_pauta` (1 ocorrência)

**Gravidade:** alta
**Vertical(is) afetada(s):** geopolitica
**Recorrência esperada:** vertical_geopolitica

**Descrição:** Worker geopolítica gerou 5 drafts sobre EXATAMENTE a mesma pauta (Trump exige reparações/sanções Irã Ormuz USS Cole) em <24h. Todos os 4 após o primeiro (265155) foram pending por duplicata. Isso representa 5x custo LLM sem entrega. Padrão observado desde 10/08 20:47 até 11/08 12:04 — cada ciclo do worker cospe outra versão do mesmo evento.

**Sugestão de prompt:**

> Ao processar pauta geopolítica que envolve continuação de evento já noticiado nas últimas 48h (mesma pessoa+ação, ex: Trump vs Irã sobre Ormuz), o worker deve VERIFICAR internamente se já produziu draft sobre isso e SUPRIMIR/CONSOLIDAR ao invés de gerar outro. Alternativamente: cada nova versão só sai se agregar ELEMENTO FACTUAL NOVO (data nova, autoridade nova, número novo) — não pode ser paráfrase da mesma nota.

**Casos registrados:**
- 2026-08-11T12:22 · post 265209 · Worker geopolítica gerou 5 drafts sobre EXATAMENTE a mesma pauta (Trump exige reparações/sanções Irã Ormuz USS Cole) em <24h. Todos os 4 após o primei

---

### `omissao_defesa_lado_contrario_post_sensivel` (1 ocorrência)

**Gravidade:** alta
**Vertical(is) afetada(s):** nacional
**Recorrência esperada:** vertical_nacional_politica_crime

**Descrição:** Worker processou pauta com acusação grave (estupro de vulnerável) apresentando SÓ o ângulo de Lindbergh (o acusador que agora é acusado de armação) mas OMITIU 3 pontos-chave da defesa Gaspar: (a) jovem 'filha' negou paternidade, (b) Gaspar fez DNA + processa por denunciação caluniosa, (c) depoente Luiz Antônio filiou-se ao PL depois. Sem esses 3, matéria fica desbalanceada em favor de quem faz a acusação inicial.

**Sugestão de prompt:**

> Em pauta sensível (crimes graves, denúncia política, acusação criminal), o worker DEVE incluir a defesa do acusado no MESMO parágrafo ou parágrafo seguinte à acusação. Não pode processar acusação sem trazer contraditório do acusado quando disponível nas fontes primárias.

**Casos registrados:**
- 2026-08-11T13:26 · post 265230 · Worker processou pauta com acusação grave (estupro de vulnerável) apresentando SÓ o ângulo de Lindbergh (o acusador que agora é acusado de armação) ma

---

### `traducao_desnecessaria_de_sigla_conhecida` (1 ocorrência)

**Gravidade:** leve
**Vertical(is) afetada(s):** ciencia_tecnologia
**Recorrência esperada:** vertical_geopolitica_ciencia

**Descrição:** Worker traduziu 'FBI' como 'Departamento Federal de Investigação dos Estados Unidos' — tradução literal desnecessária, sigla é universalmente reconhecida no público brasileiro.

**Sugestão de prompt:**

> Ao processar notícia com sigla internacional consolidada (FBI, CIA, KGB, MI6, OTAN, ONU, FMI, OMS, etc.), manter a sigla original em vez de traduzir. Usar tradução completa APENAS na primeira menção entre parênteses se for sigla menos conhecida.

**Casos registrados:**
- 2026-08-11T13:54 · post 265220 · Worker traduziu 'FBI' como 'Departamento Federal de Investigação dos Estados Unidos' — tradução literal desnecessária, sigla é universalmente reconhec

---

### `impreciso_juridico_inelegibilidade` (1 ocorrência)

**Gravidade:** media
**Vertical(is) afetada(s):** nacional
**Recorrência esperada:** vertical_nacional_politica_eleitoral

**Descrição:** Worker escreveu que 'decisão tornou Garotinho inelegível' — juridicamente incorreto. Decisão judicial estadual suspende direitos políticos; inelegibilidade formal cabe TSE/TRE decidir quando registrar candidatura. Confusão comum entre suspensão de direitos políticos e inelegibilidade — são conceitos distintos.

**Sugestão de prompt:**

> Ao processar notícia de decisão judicial que afeta candidatura, sempre distinguir: (a) suspensão de direitos políticos (ato de justiça comum ou órgão fiscalizador), (b) inelegibilidade formal (declarada pela Justiça Eleitoral no julgamento do registro de candidatura). Nunca dizer 'X ficou inelegível' se a decisão vem da Justiça comum — usar 'X pode ficar inelegível', 'candidatura sob risco de inelegibilidade' ou 'suspensão de direitos políticos'.

**Casos registrados:**
- 2026-08-11T14:28 · post 265247 · Worker escreveu que 'decisão tornou Garotinho inelegível' — juridicamente incorreto. Decisão judicial estadual suspende direitos políticos; inelegibil

---

### `ruido_template_admite_fonte_interna` (1 ocorrência)

**Gravidade:** leve
**Vertical(is) afetada(s):** nacional
**Recorrência esperada:** todas_verticais_worker_v4

**Descrição:** Worker deixou vazar 2 traços de template interno no corpo publicável: 'A fonte do relato é de 11 de agosto de 2026, às 17h15 UTC' e 'conforme os relatos reunidos no material'. São meta-comentários sobre o processo do worker que não pertencem a texto jornalístico.

**Sugestão de prompt:**

> Nunca incluir no corpo publicável frases que revelem processo interno do worker (fontes internas, timestamps do sistema, 'material fornecido', 'relato central', etc). Se for pra dar temporalidade, usar 'nesta terça-feira (11)' — se for fonte, citar veículo real ('segundo a Revista Fórum', etc.).

**Casos registrados:**
- 2026-08-11T15:26 · post 265249 · Worker deixou vazar 2 traços de template interno no corpo publicável: 'A fonte do relato é de 11 de agosto de 2026, às 17h15 UTC' e 'conforme os relat

---


## Nota final pro worker

Se você (worker V4) processar uma pauta e reconhecer que ela cai em uma das categorias acima, APLIQUE a diretriz correspondente no draft. Isso reduz reescrita futura, custo de LLM, tempo de revisor e melhora a qualidade do que chega ao leitor do Cafezinho.

Este arquivo é atualizado após cada ciclo de Vigília V5 do Claude quando novas críticas são registradas — atualize sua cópia local (se cacheada) periodicamente.