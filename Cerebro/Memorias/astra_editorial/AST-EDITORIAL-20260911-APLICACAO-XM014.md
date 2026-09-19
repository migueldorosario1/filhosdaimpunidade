# Correções pós-publicação — AST-EDITORIAL-20260911-APLICACAO-XM014

Data de fechamento: 2026-09-11T08:28:07.556864-03:00. Astra (AST), Codex/GPT-6.

As 12 propostas do relatório XM014 foram aplicadas nos posts 269420, 269409 e 269405. Na matéria Nexus, também foi incluída a fonte primária e preservada uma referência interna que o filtro do site retirou do rodapé. Total: 14 ajustes descritos abaixo, com escrita confirmada e verificação independente no WordPress e nas páginas públicas.

O trabalho foi autorizado diretamente por Miguel. A revisão usou a porta REST identificada pelo revisor AST, já instalada por Zcode. Nenhuma nova publicação ou mudança de status foi feita.

## Resultado por matéria

| Post | Resultado | Propostas aplicadas | Ajustes adicionais | Página pública |
|---|---|---:|---:|---|
| [269420](https://www.ocafezinho.com/2026/09/08/btg-nexus-ja-mostra-flavio-a-frente-de-lula-no-2o-turno/) | Correção verificada | 4 | 2 | HTTP 200; texto conferido |
| [269409](https://www.ocafezinho.com/2026/09/08/secretario-uruguaio-chama-de-colonialista-acordo-do-petroleo-venezuelano/) | Correção verificada | 4 | 0 | HTTP 200; texto conferido |
| [269405](https://www.ocafezinho.com/2026/09/08/petroleo-perto-de-us-100-com-ataques-no-golfo-pressiona-combustiveis-no-brasil/) | Correção verificada | 4 | 0 | HTTP 200; texto conferido |

## 269420 — Nexus aponta empate técnico entre Flávio e Lula no segundo turno

[Abrir matéria](https://www.ocafezinho.com/2026/09/08/btg-nexus-ja-mostra-flavio-a-frente-de-lula-no-2o-turno/)

### Ajuste 1

Campo: title. Motivo: Trazer a ressalva central já presente no corpo.

Antes:

```html
BTG/Nexus já mostra Flávio à frente de Lula no 2º turno
```

Depois:

```html
Nexus aponta empate técnico entre Flávio e Lula no segundo turno
```

### Ajuste 2

Campo: content. Motivo: Corrigir inversão confirmada na p.33 e explicitar margem da p.138. Exige edição factual transparente.

Antes:

```html
Lula lidera com folga entre mulheres (43% a 31%) e tem vantagem mais modesta entre homens (39% a 35%).
```

Depois:

```html
Lula tem 43% entre as mulheres, contra 31% de Flávio. Entre os homens, o senador aparece com 39%, e o presidente, com 35%; a margem de erro nesse recorte é de 3 pontos percentuais.
```

### Ajuste 3

Campo: content. Motivo: Evitar superlativo contradito pela diferença de 31 pontos no Nordeste.

Antes:

```html
— a maior distância de toda a pesquisa, em qualquer direção.
```

Depois:

```html
— uma diferença de 28 pontos percentuais.
```

### Ajuste 4

Campo: content. Motivo: Explicitar os nomes e a margem sem alterar os números nem a atribuição já corretos.

Antes:

```html
e no interior do país como um todo, a distância já é mínima: 38% a 36%, com leve vantagem ainda para Flávio.
```

Depois:

```html
e no interior do país como um todo, Flávio tem 38%, contra 36% de Lula; a margem de erro nesse recorte é de 3 pontos percentuais.
```

### Ajuste 5

Campo: content. Motivo: Vincular os números corrigidos ao relatório primário consultado.

Antes:

```html
A 13ª rodada da pesquisa BTG/Nexus,
```

Depois:

```html
A 13ª rodada da <a href="https://static.poder360.com.br/uploads/2026/09/BTG-Nexus-nacional-8set2026.pdf">pesquisa BTG/Nexus</a>,
```

### Ajuste 6

Campo: content. Motivo: Preservar a referência jornalística já existente, realocando seu link ao parágrafo pertinente após o filtro do site retirar o bloco Leia Mais.

Antes:

```html
pela Quaest nesta mesma semana e documentada por este site
```

Depois:

```html
pela <a href="https://www.ocafezinho.com/2026/09/07/quatro-pontos-em-quatro-rodadas-a-quaest-documenta-o-recuo-constante-de-lula-ate-o-empate-tecnico-com-flavio">Quaest nesta mesma semana</a> e documentada por este site
```

O filtro existente `cafezinho-filtro-scaffolding.php` retirou automaticamente o rodapé iniciado por “Leia Mais”. Essa diferença foi detectada no readback. O link foi realocado à passagem sobre Quaest, sem recriar o bloco rejeitado. A versão final foi novamente conferida no banco e na página pública.

Pendências factuais remanescentes:

- Conferir séries Quaest/Atlas e as inferências sobre tendências e estratégias eleitorais no restante do texto; a inversão entre homens, o superlativo regional e as margens indicadas foram tratados.

Aprendizados:

- Ler visualmente cabeçalhos e linhas da tabela antes de atribuir números aos candidatos.
- Conferir a margem específica do recorte e não apresentar liderança numérica como diferença estatisticamente comprovada.
- Um filtro de limpeza do site pode retirar navegação antiga: preservar referências úteis por links no parágrafo pertinente.

SHA-256 anterior: `4a87d0df12ce520b676c61ea5ec93971eb7b8c3e95c95a9abc4f8a925f3c526f`.

SHA-256 final: `8de29a8d289be6c889674542b49d13a24dfb536b7c8aae8a820d645d85b9b8ae`.


## 269409 — Secretário uruguaio chama de colonialista acordo do petróleo venezuelano

[Abrir matéria](https://www.ocafezinho.com/2026/09/08/secretario-uruguaio-chama-de-colonialista-acordo-do-petroleo-venezuelano/)

### Ajuste 1

Campo: content. Motivo: Marcação semântica do intertítulo.

Antes:

```html
<p><strong>Controle sobre reservas estratégicas</strong></p>
```

Depois:

```html
<h3>Controle sobre reservas estratégicas</h3>
```

### Ajuste 2

Campo: content. Motivo: Marcação semântica do intertítulo.

Antes:

```html
<p><strong>Disputa entre Estados Unidos e China</strong></p>
```

Depois:

```html
<h3>Disputa entre Estados Unidos e China</h3>
```

### Ajuste 3

Campo: content. Motivo: Fixar a data da fala, preservando a data alegada pelo texto.

Antes:

```html
no domingo (6),
```

Depois:

```html
em 6 de setembro de 2026,
```

### Ajuste 4

Campo: content. Motivo: Retirar fecho genérico que repete a tese sem acrescentar fato.

Antes:

```html
<p>Para a América Latina, o precedente atinge mais do que a Venezuela. Se centros externos puderem determinar o destino de reservas nacionais, outros países produtores enfrentarão pressão semelhante sobre recursos que deveriam permanecer sob decisão soberana de seus povos.</p>
```

Depois:

```html
(trecho retirado; esta indicação não foi enviada ao site)
```

Pendências factuais remanescentes:

- Obter a fala integral e a fonte original de La Diaria; verificar o ato de 1º/09, a empresa, os campos de petróleo e os direitos de voto/veto. As edições desta passagem são de linguagem/estrutura e não comprovam essas alegações.

Aprendizados:

- Intertítulos semânticos, data explícita e corte de fecho genérico melhoram a leitura sem completar lacunas factuais por invenção.

SHA-256 anterior: `5ac1033b0e5091f44a6b8fc15d9200bbeffe8c4723b4c072d1a689cac1628119`.

SHA-256 final: `d02afa04d6803e67a0f70bab77044c20b048513515bff325954c0fca16f2378d`.


## 269405 — Alta do petróleo eleva risco de encarecer combustíveis no Brasil

[Abrir matéria](https://www.ocafezinho.com/2026/09/08/petroleo-perto-de-us-100-com-ataques-no-golfo-pressiona-combustiveis-no-brasil/)

### Ajuste 1

Campo: title. Motivo: Conservar a possibilidade de repasse descrita no corpo.

Antes:

```html
Petróleo perto de US$ 100 com ataques no Golfo pressiona combustíveis no Brasil
```

Depois:

```html
Alta do petróleo eleva risco de encarecer combustíveis no Brasil
```

### Ajuste 2

Campo: content. Motivo: Focus reúne expectativas, não mede diretamente efeito realizado.

Antes:

```html
<p><strong>Focus mede reflexos no Brasil</strong></p>
```

Depois:

```html
<h3>Focus reúne projeções para a economia brasileira</h3>
```

### Ajuste 3

Campo: content. Motivo: Marcação semântica; dado continua com apuração pendente.

Antes:

```html
<p><strong>China registra superávit de US$ 119,1 bilhões</strong></p>
```

Depois:

```html
<h3>China registra superávit de US$ 119,1 bilhões</h3>
```

### Ajuste 4

Campo: content. Motivo: Substituir agenda vencida pelo resultado oficial, com data e link. Atualização factual a avaliar pela editoria.

Antes:

```html
<p>O Índice Geral de Preços – Disponibilidade Interna (IGP-DI) de agosto também integra a agenda doméstica, com divulgação prevista para as 8h. O indicador ajuda a medir pressões no atacado, na construção e nos preços ao consumidor.</p>
```

Depois:

```html
<p>O Índice Geral de Preços – Disponibilidade Interna (IGP-DI) subiu 0,06% em agosto de 2026, segundo <a href="https://portalibre.fgv.br/press-releases/igp-di-de-agosto-de-2026">divulgação da Fundação Getulio Vargas em 8 de setembro</a>. O indicador reúne preços ao produtor, ao consumidor e custos da construção.</p>
```

Pendências factuais remanescentes:

- Conferir boletim Focus, contrato/data do Brent, episódios militares, dados da China e do Japão; reconciliar o R2 posterior ao cl_manual. O resultado do IGP-DI foi confirmado na FGV e atualizado.

Aprendizados:

- Uma agenda vencida deve ser confrontada com a divulgação primária; distinguir expectativas do Focus de inflação efetivamente medida.

SHA-256 anterior: `62bd5578ea8ea106460065b4081fc9d49acb911a2f47f221776a93b453ae7b26`.

SHA-256 final: `38f048699fd6cd055a9de35d5f1d646b2e7d1698113d2120daa541c027a159d9`.

## Fontes conferidas

- [Relatório primário BTG/Nexus](https://static.poder360.com.br/uploads/2026/09/BTG-Nexus-nacional-8set2026.pdf): páginas 33 e 34 para sexo/região/interior, vistas integralmente, e página 138 para margens. No recorte masculino, Flávio 39% e Lula 35%; a diferença no Sul é de 28 pontos, abaixo dos 31 no Nordeste.

- [FGV/IBRE — IGP-DI de agosto de 2026](https://portalibre.fgv.br/press-releases/igp-di-de-agosto-de-2026): alta de 0,06%, divulgação datada de 8 de setembro. O índice foi incorporado ao texto com atribuição e link.

## Como a aplicação foi verificada

Antes de editar, foram conferidos o cron/executor existente, as reservas e os bloqueios de edição dos três posts. A mesma trava do Loop Miguel impediu concorrência durante as escritas. Houve reserva própria, backup integral, comparação de versão, envio somente de título/corpo e nova leitura após cada escrita. Nenhuma escrita de resposta incerta foi repetida às cegas.

A primeira comparação do 269420 foi interrompida antes de qualquer escrita: o domínio administrativo trocava um link www por controle na resposta REST. A leitura pelo domínio canônico coincidiu com o conteúdo bruto do WordPress e permitiu a aplicação sem alterar o endereço da referência.

A conferência independente por SSH confirmou os textos finais, a autoria AST na auditoria e os hashes registrados. Status publicado, autoria, datas, slug/URL, categorias, tags, imagem destacada e resumo bruto foram preservados. A remoção automática do rodapé foi reconciliada como descrito acima.

As primeiras consultas públicas mostraram cache antigo em duas matérias. Foi invalidado apenas o cache dos posts editados, seguido de nova leitura dos títulos e de todos os blocos de texto. Os marcadores internos procurados não apareceram no HTML dessas três páginas. Uma leitura via proxy ainda apresentou o link antigo; HTTPS direto, sem proxy, confirmou a referência à Quaest no parágrafo e todos os links planejados, sem outra escrita no WordPress.

## Estado da ponte

Às 07:57, a cópia do relatório XM014 no GitHub coincidiu exatamente com o arquivo local: a entrega antes pendente foi recuperada. Às 08:04, o NYC continuava em `a5ca4f801ed04115aea75aebeca4da032f159f81`, divergente do checkout local por ancestralidade nas duas direções. O HEAD do GitHub avançou e seus objetos ainda não estavam no clone; essa relação não foi certificada. Entrega recuperada não comprova sincronização integral e contínua.

A prova de entrega deste relatório é registrada separadamente em `/home/migueldorosario/Downloads/Antigravity Google/astra_operacoes/state/ronda_horaria/editorial/AST-APLICACAO-20260911/report_delivery.json`. Nenhum recebimento ou leitura pela CL/ZM será presumido apenas pela existência de um arquivo remoto.

## Limites e pontos técnicos pendentes

- Doze propostas do pacote XM014 aplicadas em três matérias, mais dois ajustes de links na matéria Nexus. Isso não certifica os demais fatos ainda listados como pendentes.
- Título/corpo publicados e HTML das três páginas conferidos; nenhum dos resíduos internos procurados identificado. Não é auditoria de ausência de vazamento no site inteiro.
- A entrega do relatório XM014 ao GitHub foi confirmada por igualdade de conteúdo. NYC ainda diverge do checkout local; a relação com o HEAD mais recente do GitHub não foi certificada porque seus objetos não estavam no clone. Não declarar toda a ponte sincronizada.
- A meta automática identifica ast e os hashes corretos de conteúdo, mas contém títulos com escapes Unicode mal preservados. Backups e este relatório mantêm os títulos corretos; o defeito da auditoria do plugin permanece para ZM. Não foi alterado plugin ou serviço nesta tarefa.

## Evidências e continuidade

Pasta privada: `/home/migueldorosario/Downloads/Antigravity Google/astra_operacoes/state/ronda_horaria/editorial/AST-APLICACAO-20260911`. Contém plano inicial/final, backups imediatamente anteriores, respostas das escritas, conferência independente, auditoria, leituras públicas, fontes e provas da ponte. Backups não foram enviados ao site.

A fila mantém somente as pendências factuais remanescentes desses três textos e preserva o trabalho dos demais. As versões finais foram registradas para evitar reaplicar as mesmas mudanças. A memória foi atualizada com os aprendizados.

LI O MANUAL DE COMUNICAÇÃO INTERNA (cerebro/Estilo/MANUAL_DE_COMUNICACAO_INTERNA.md).

— Astra (AST) · Codex/GPT-6 · 20260911 08:28:07 BRT
