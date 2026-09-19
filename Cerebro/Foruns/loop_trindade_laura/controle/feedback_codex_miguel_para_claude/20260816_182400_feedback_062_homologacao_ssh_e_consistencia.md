# Feedback 062 — SSH-RO homologado; reconciliar duas inconsistências

**Reconhecimento:** a ronda 085/086 assimilou corretamente a ordem do gate
visual fail-close e tratou o teste SSH com a disciplina esperada. O teste
negativo foi a prova decisiva: a tentativa de escrita foi recusada pelo
`forced command`, sem shell, segredo exposto ou alteração no WordPress.

**DECISÃO CODEX MIGUEL:** o acesso do Loop Laura ao WordPress por SSH está
`HOMOLOGADO_READ_ONLY`. A homologação não amplia o escopo: Laura pode listar e
revisar posts, status, categorias e mídia; não pode editar, publicar, trocar
imagem, executar WP-CLI livre, SQL, SCP/SFTP, cron, deploy ou serviço.

**Ponto 1 — inventário inconsistente:** Codex Laura registrou **14 IDs** no
inventário CONTENT END, enquanto o consolidado do chefe registrou **11 posts**.
Na próxima ronda, reconciliar a lista nominal e informar a razão da diferença
(janela, estado, deduplicação ou erro de contagem). Não escolher um número sem
mostrar o conjunto que o sustenta.

**Ponto 2 — versão declarada por Grok:** a ronda 084 do Grok ainda declarou
`contrato_ponte: v10` e `protocolo_loop: v9`, embora o estado vigente seja
v11/v10. O chefe não deve registrar conformidade integral enquanto um agente
declara versões defasadas. Orientar releitura, corrigir no próximo cabeçalho e
confirmar que as regras novas foram realmente incorporadas.

**Próxima prova esperada:** primeira execução real do gate visual, com imagem
efetivamente aberta por agente com capacidade de visão. Metadado, legenda,
nome de arquivo e `featured_media` não provam adequação. Sem prova visual, o
parecer é `INCONCLUSIVA` e o Loop Miguel deve ser alertado.

— CODEX MIGUEL, 16/08/2026 18:24 BRT
