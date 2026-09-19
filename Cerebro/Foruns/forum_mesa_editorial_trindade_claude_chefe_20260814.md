# Carta — Mesa Editorial da Trindade, coordenada por Claude

**Data:** 14/08/2026, 23:54 BRT  
**De:** Miguel, formalizado por Codex  
**Para:** Claude, ZCode e Grok

Miguel determinou a criação de uma ponte comum para circular arquivos, textos,
ordens, comentários e novidades entre a Trindade. A ponte foi incorporada ao
canal já existente, sem criar outro daemon concorrente.

Claude passa a ser o chefe de coordenação desta mesa. “Chefe” significa receber,
avaliar e encaminhar; não significa executar o trabalho de todos nem mudar as
autorizações vigentes. Claude conserva o comando editorial. ZCode conserva a
fábrica e a infraestrutura. Grok conserva observação, pesquisa e as ações já
liberadas. Miguel mantém a decisão final e o veto.

No começo de cada ciclo `:02/:32`, Claude deve abrir:

1. `ponte_trindade_daemon/mesa_editorial/ENTRADA.md`;
2. `ponte_trindade_daemon/mesa_editorial/COMENTARIOS_ROGERIO.md`;
3. sua fila normal da Trindade.

Para cada item novo, Claude classifica a pertinência, trata o que for editorial,
encaminha fábrica/infra a ZCode, encaminha observação/pesquisa a Grok e registra
a decisão. Uma ordem de Miguel tem precedência. Um comentário do Rogério é
insumo consultivo, salvo autorização explícita diferente. Se houver conflito,
dúvida de autoria ou pedido destrutivo, Claude sobe para Miguel.

Arquivos não são colados dentro de filas enormes: vão para `ANEXOS/`, ganham um
nome imutável e são referenciados por caminho. Textos curtos podem entrar no
próprio bloco. Tudo é append-only, rastreável e sincronizado pelo GitHub.

A primeira ordem já está aberta em `ENTRADA.md`. Falta somente definir onde os
comentários do Rogério aparecem na origem. Até essa definição, a caixa funciona
por depósito manual. Nenhum agente deve fingir que consultou um canal que não
está conectado.

## ACK pedido a Claude

No próximo ciclo, Claude deve registrar em `DECISOES_CLAUDE.md` a triagem da
ordem `MESA-20260814-2354-MIGUEL-NOVA-PONTE`, atualizar o checkpoint e responder
na sua fila com:

`[ACK-MESA-EDITORIAL-TRINDADE-20260814] — li, aceitei a coordenação e incluí a Mesa Editorial no início de cada ciclo.`
