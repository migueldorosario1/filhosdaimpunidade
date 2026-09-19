# Protocolo permanente — Loop Laura informa o Loop Miguel

**Decisão de Miguel:** 15/08/2026  
**Nome oficial do fluxo operacional:** Loop Miguel  
**Chefia do Loop Laura:** Claude Laura

## Objetivo

O Loop Laura funciona como um segundo par de olhos. Ele observa, pesquisa,
audita e aprende. Quando encontra algo relevante, o achado entra no fluxo
operacional do Loop Miguel, que decide e executa a correção com os protocolos
oficiais do Cafezinho.

## Caminho único

1. Laura registra o achado em
   `ponte_codex_miguel_laura/mensagens/para_miguel/`, com post, evidência,
   risco e sugestão.
2. Codex Miguel verifica de forma independente. Achado não confirmado não
   vira ordem de correção.
3. Se confirmado e relevante, Codex Miguel abre item append-only em
   `ponte_trindade_daemon/fila_para_claude.md`, identificado como
   `ACHADO-LOOP-LAURA`.
4. Claude Miguel coordena o tratamento dentro do Loop Miguel. Um único
   executor recebe a tarefa para evitar duas correções concorrentes.
5. Quando Miguel já tiver autorizado o tipo de correção, Codex Miguel também
   pode executá-la diretamente. Para post publicado: funções oficiais do
   WordPress via SSH + WP-CLI, revisão/backup, precondições, rollback e
   validação pública.
6. O resultado entra na memória oficial diária em
   `monitoramento_horario/ciclos_vigilia/` e, quando couber, em
   `bugs_encontrados/`.
7. A conclusão volta a Claude Laura como feedback, para que a equipe aprenda
   o que foi confirmado, corrigido ou descartado.

## Fronteiras

- Loop Laura continua somente leitura no WordPress e na infraestrutura.
- A ponte transporta observações; não concede SSH, publicação, lixeira ou
  deploy.
- Claude Miguel continua coordenador editorial do Loop Miguel.
- Codex Miguel é o verificador e pode ser executor seguro quando autorizado.
- Miguel conserva decisão final, veto e poder de ampliar ou reduzir escopo.
- Toda tarefa tem um só dono operacional e um estado: `ABERTO`, `EM_CURSO`,
  `FECHADO` ou `DESCARTADO_COM_EVIDENCIA`.

## O que sobe da Laura para o Miguel

Sobem achados capazes de mudar qualidade, segurança ou funcionamento:

- erro factual, cronológico ou eleitoral;
- metalinguagem, prompt, bastidor ou parâmetro de IA vazado;
- duplicata, imagem incorreta, ausência de imagem ou crédito inadequado;
- título enganoso, conteúdo sem atualidade ou fonte contraditória;
- falha de worker, idempotência, lock, fila, cadência ou estado WordPress;
- oportunidade editorial realmente atual, acompanhada de fontes verificáveis.

Relatórios rotineiros sem ação permanecem na memória do Loop Laura e chegam ao
relatório de 30 minutos de Codex Miguel, sem congestionar a fila editorial.

## Primeiro caso integrado

Grok Laura encontrou seis links com `utm_source=openai` no post 265876. Codex
Miguel confirmou, removeu somente os parâmetros `utm_*` com revisão WordPress,
validou que título, status, categoria e imagem permaneceram intactos e
registrou a correção. Esse é o modelo: Laura vê, Miguel confirma, o Loop Miguel
corrige e a memória oficial aprende.

