# Relatório de qualidade — AST-QUALIDADE-20260911-SEO-IMAGENS

Fechamento: 2026-09-11T08:58:20.912558-03:00. Astra (AST), Codex/GPT-6.

Miguel pediu ampliar a revisão para imagens, texto alternativo, resumos e SEO e manter um fórum que ensine os verticais. Nesta passagem, três capas foram abertas, os campos e o HTML de três matérias foram conferidos e cinco correções pontuais foram aplicadas e relidas.

O pacote editorial anterior já havia aplicado 12 propostas e dois ajustes de links. Este relatório acrescenta dois resumos, dois alts e a identificação do cenário de primeiro turno e de Lula como sujeito no parágrafo, acolhendo o apontamento independente da XM017. São etapas separadas; o total desta sessão é de 19 ajustes, sem tratar propostas pendentes como aplicação.

## Alterações verificadas

### 269420 — Nexus aponta empate técnico entre Flávio e Lula no segundo turno

[Abrir matéria](https://www.ocafezinho.com/2026/09/08/btg-nexus-ja-mostra-flavio-a-frente-de-lula-no-2o-turno/)

Campo: `excerpt`. Preencher resumo autônomo e evitar descrição automática cortada.

Antes:

> (vazio; indicação somente deste relatório)

Depois:

> Pesquisa BTG/Nexus de setembro registra empate técnico entre Flávio e Lula no segundo turno, com diferenças entre os recortes de sexo e região.

Campo: `alt_text`. Descrever os pixels da composição vista, sem inferir identidades ou acontecimento.

Antes:

> (vazio; indicação somente deste relatório)

Depois:

> Montagem com dois homens de terno sentados diante de fundo azul; o homem à esquerda usa chapéu claro.

Campo: `content`. Explicitar que a tabela é do cenário estimulado de primeiro turno e identificar Lula no recorte de 60 anos ou mais; clareza do sujeito apontada pela XM017, percentuais conferidos na página 33 do relatório Nexus.

Antes:

> Lula tem 43% entre as mulheres, contra 31% de Flávio. Entre os homens, o senador aparece com 39%, e o presidente, com 35%; a margem de erro nesse recorte é de 3 pontos percentuais. Entre eleitores com 60 anos ou mais, chega a 44%;

Depois:

> No cenário estimulado de primeiro turno, Lula tem 43% entre as mulheres, contra 31% de Flávio. Entre os homens, o senador aparece com 39%, e o presidente, com 35%; a margem de erro nesse recorte é de 3 pontos percentuais. Entre eleitores com 60 anos ou mais, Lula chega a 44%;

Verificação: campo salvo coincide; página pública HTTP 200; valores esperados de descrição/alt presentes conforme o campo editado; nenhum dos marcadores internos procurados encontrado. Autoria, status, data de publicação, URL, categorias, tags e imagem preservados.

Pendências:

- Apurar origem/crédito da montagem; não preencher com suposição.
- Investigar ausência de og:image, title duplicado e dimensão da capa (888 px); não houve alteração de template/arquivo.
- Conferir séries Quaest/Atlas e inferências eleitorais restantes, como no relatório anterior.

Imagem efetivamente vista: SHA-256 `c86a842bcd88aa546c5bf46201a26eb0a1fd841a1b935a6178d18f41d8a5d834`.

Hash título/corpo final: `e26405b038da8d5f69e1216c68694e15dd37380e524339b94101c492b915590d`. Hash metadados final: `7553b2add779a93a1cbcd60ca34fd3de5d3f1d72eef4f4c5866f04181a43ceda`.

### 269409 — Secretário uruguaio chama de colonialista acordo do petróleo venezuelano

[Abrir matéria](https://www.ocafezinho.com/2026/09/08/secretario-uruguaio-chama-de-colonialista-acordo-do-petroleo-venezuelano/)

Campo: `alt_text`. Corrigir a cor da camisa após abrir a imagem e descrever elementos visíveis.

Antes:

> Homem de barba e camisa clara sentado, falando em um estúdio de televisão

Depois:

> Homem de óculos, barba e camisa preta, com microfone junto ao rosto, sentado à mesa em um estúdio.

Verificação: campo salvo coincide; página pública HTTP 200; valores esperados de descrição/alt presentes conforme o campo editado; nenhum dos marcadores internos procurados encontrado. Autoria, status, data de publicação, URL, categorias, tags e imagem preservados.

Pendências:

- Conferir fonte integral de La Diaria/discurso e documentos do acordo, empresa, campos e voto/veto.
- Investigar title duplicado e avaliar original maior da capa (576 px), com licença comprovada.

Imagem efetivamente vista: SHA-256 `9c9a70e8e3ef952585b07ce1fb1b9af051b9326821166a98c987c1e1ae2c2b3a`.

Hash título/corpo final: `d02afa04d6803e67a0f70bab77044c20b048513515bff325954c0fca16f2378d`. Hash metadados final: `3b453668536937d8a12c336baf793930cae20c0396da0bb3aea6d996a9611ec0`.

### 269405 — Alta do petróleo eleva risco de encarecer combustíveis no Brasil

[Abrir matéria](https://www.ocafezinho.com/2026/09/08/petroleo-perto-de-us-100-com-ataques-no-golfo-pressiona-combustiveis-no-brasil/)

Campo: `excerpt`. Retirar agenda vencida do Focus e refletir o indicador já conferido na fonte primária.

Antes:

> Petróleo perto de US$ 100 e menor tráfego no Estreito de Ormuz ampliam o risco de inflação global. Boletim Focus mostrará possíveis efeitos nas expectativas brasileiras.

Depois:

> A alta do petróleo amplia o risco de pressão sobre os combustíveis no Brasil. Em agosto, o IGP-DI subiu 0,06%, segundo a FGV.

Verificação: campo salvo coincide; página pública HTTP 200; valores esperados de descrição/alt presentes conforme o campo editado; nenhum dos marcadores internos procurados encontrado. Autoria, status, data de publicação, URL, categorias, tags e imagem preservados.

Pendências:

- Conferir Focus, Brent, episódios militares e dados externos ainda pendentes; IGP-DI já verificado na FGV.
- Investigar title duplicado no HTML.

Imagem efetivamente vista: SHA-256 `40740980d08e2fbe8c96cda91e93c64d4ffd612001ac7a9467d2d355087eb8df`.

Hash título/corpo final: `38f048699fd6cd055a9de35d5f1d646b2e7d1698113d2120daa541c027a159d9`. Hash metadados final: `ce62ed79f8b3929f266a10840155ff9f91fa79902733267ebd2e044c8a2dca41`.

## Conferência visual

Nexus, mídia 269421: composição com dois retratos, fundo azul e chapéu claro à esquerda. Alt descreve os elementos visíveis sem identificar pessoas pela aparência nem apresentar a montagem como registro de um encontro. Não há legenda/crédito preenchidos; origem permanece em apuração. AVIF foi convertido localmente para PNG apenas para visualização; arquivo publicado não foi modificado.

Uruguai, mídia 269414: homem de óculos, barba, camisa preta e microfone junto ao rosto, à mesa. A descrição anterior dizia camisa clara; os pixels contradizem isso. Legenda/crédito anteriores foram preservados, sem nova certificação de identidade/licença nesta passagem.

Petróleo, mídia 269408: torres e tanques industriais, casas em primeiro plano e morros ao fundo. O alt existente corresponde à cena e foi mantido. Conferir licença/localidade é procedimento distinto da observação de pixels.

A verificação independente confirmou também o SHA-256 dos arquivos originais no servidor, iguais aos pixels abertos. A consulta de usos encontrou a mídia 269421 somente na capa do 269420 e a 269414 somente no 269409; não foi encontrada outra referência nos corpos pesquisados. Os alts foram editados na mídia existente por REST, sem trocar o arquivo.

## SEO e apresentação pública

| Verificação | Resultado na amostra |
|---|---|
| Resumo/descrição | Nexus preenchido; petróleo atualizado; os valores aparecem em description e og:description. Uruguai já tinha resumo, preservado. |
| Título e H1 | Títulos coerentes com os textos revisados; um H1 por página; dois title no head de cada página, pendência técnica. |
| Canonical | Correspondente ao URL publicado das três matérias; URLs preservadas. |
| Robots | max-image-preview:large presente; não foi encontrado noindex nessa meta. Isso não certifica indexação. |
| Compartilhamento | og:title e og:description presentes; og:image nas duas capas JPG, ausente na Nexus. |
| Imagens | Alt Nexus preenchido, Uruguai corrigido, petróleo mantido após visão. Dimensões originais 888×530, 576×554 e 1600×1200. |
| Dados estruturados | JSON-LD das três páginas pôde ser lido e inclui NewsArticle. Validação completa de todas as propriedades não executada. |
| Links | Fonte Nexus, referência Quaest e divulgação FGV preservadas e confirmadas na etapa anterior. |

A ausência de título/descrição customizados no Yoast não foi tratada automaticamente como defeito: o HTML já produzia esses campos. Corrigir excerpt resolveu as duas descrições sem gravar metadados protegidos nem alterar configuração global.

Para imagens grandes no Discover, o Google recomenda largura mínima de 1200 px; as capas Nexus e Uruguai ficam abaixo dessa referência. Isso não impede genericamente a indexação, e nenhum redimensionamento artificial foi feito. [Orientação Google Discover](https://developers.google.com/search/docs/appearance/google-discover).

As páginas normais ainda serviam versões antigas na primeira leitura das 08:40. A consulta das 08:58 confirmou os novos resumos, alts e esclarecimento, sem repetir as escritas. Os dois conjuntos de evidência foram preservados. A causa exata do atraso de propagação não foi estabelecida. O helper existente rocket_clean_post também limpa home e URLs relacionadas ao post; não houve limpeza global do Redis nem mudança de serviço.

## Fórum e aprendizado para a próxima matéria

`cerebro/Foruns/FORUM_QUALIDADE_POS_PUBLICACAO_ASTRA.md` foi criado e entregue ao GitHub. Reúne casos verificáveis, orientações atuais e pendências. O bloco de lições foi instalado no cabeçalho permanente da diretriz existente do V4.1 no NYC, preservando regras de Miguel e registros do Tribunal. O cabeçalho sobrevive à compactação diária de cinco dias.

O novo comando operacional `python3 -m astra_operacoes.ronda_horaria.quality_forum` atualiza esses dois destinos com recibos separados, backup no NYC e comparação de versão. Teste isolado executou somente o trecho real do V4.1 que lê a diretriz; nenhum modelo ou ciclo de publicação foi acionado. O briefing de produção consultado ainda era de 06:37: consumo das novas lições em ciclo real permanece pendente.

A rotina do Loop Miguel foi atualizada para revisar resumo/mídia mesmo quando o hash do corpo não muda, guardar prova visual e atualizar o fórum no fechamento. A análise Astra recebe agora o fórum e os metadados coletados. O modelo limitado a texto não simula visão; o executor operacional faz a inspeção visual antes de escrever alt.

Vícios registrados: conclusão genérica, superlativo sem comparação, agenda vencida, resumo esquecido após correção do corpo, alt deduzido sem olhar os pixels e sujeito implícito após alternar pessoas. A amostra não permite atribuir taxa ao site inteiro ou responsabilizar um vertical pela categoria do post. A origem de produção precisa de recibo próprio.

## Verificação da implantação e da concorrência

239 testes offline passaram. A consulta nova foi executada em modo somente leitura no WordPress e trouxe metadados de oito publicados (269882, 269770, 269719, 269758, 269716, 269852, 269735, 269727). Isso comprova a coleta dos campos, não revisão humana integral desses oito textos/imagens.

A ronda XM017 das 08:17 foi preservada e terminou às 08:26:39, rc=0, com recibo próprio de 08:25:07. Foram três leituras editoriais, duas propostas e zero escritas pelo XM. Ele confirmou as edições anteriores do AST e deixou 269882 adiado até reavaliação do lock às 09:02:30. O presente trabalho só retomou as escritas após a trava ficar livre. Não foi criado cron ou executor adicional.

A ponte entregou o pacote editorial anterior e o fórum por API com leitura de confirmação. A XM017 encontrou mensagens reconciliadas, porém controles/reservas e checkout NYC ainda divergentes; não se certifica sincronização geral. Ver provas específicas em vez de interpretar entrega como leitura/resposta de outro agente.

## Evidências e limites

- Amostra de três matérias, três capas vistas e cinco ajustes: dois resumos, dois alts e uma clarificação de cenário/sujeito. Não é auditoria do site inteiro.
- O relatório anterior registra separadamente as 12 propostas XM014 aplicadas e dois ajustes de links; não contar novamente como correções desta etapa.
- Campos protegidos, URLs, autoria, datas de publicação, arquivos/capas e créditos preservados. Origem/crédito ausentes da montagem não foram inventados.
- HTML tem canonical coerente, H1 e JSON-LD NewsArticle legível; isso não equivale a validação completa de dados estruturados ou garantia de indexação/posição.
- Três páginas com dois title no head e Nexus sem og:image: pendências técnicas documentadas, sem modificação de plugins, tema ou serviços.
- Diretriz entregue ao NYC e leitura V4.1 testada com o bloco real. Último briefing de produção consultado ainda era anterior à entrega; consumo em ciclo real não comprovado.
- A ponte entregou relatórios e fórum ao GitHub; o Git geral/controles ainda apresentam divergências, conforme XM017. Entrega de arquivo não é ACK/leitura de CL ou ZM.

Pasta privada de evidências: `/home/migueldorosario/Downloads/Antigravity Google/astra_operacoes/state/ronda_horaria/editorial/AST-APLICACAO-20260911`. Inclui planos, imagens vistas, backups, respostas REST, hashes, inspeções públicas, consulta SQL somente leitura, testes e recibos de entrega.

Referências: [alt e imagens — Google](https://developers.google.com/search/docs/appearance/google-images), [descrições — Google](https://developers.google.com/search/docs/appearance/snippet), [imagens informativas — W3C](https://www.w3.org/WAI/tutorials/images/informative/). O dado 0,06% do resumo vem da [FGV/IBRE](https://portalibre.fgv.br/press-releases/igp-di-de-agosto-de-2026), conferida na etapa editorial; empate técnico e percentuais vêm do [relatório Nexus](https://static.poder360.com.br/uploads/2026/09/BTG-Nexus-nacional-8set2026.pdf).

LI O MANUAL DE COMUNICAÇÃO INTERNA (cerebro/Estilo/MANUAL_DE_COMUNICACAO_INTERNA.md).

— Astra (AST) · Codex/GPT-6 · 2026-09-11T08:58:20.912558-03:00
