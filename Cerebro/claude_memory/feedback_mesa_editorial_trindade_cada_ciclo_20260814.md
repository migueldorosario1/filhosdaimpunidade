---
name: feedback-mesa-editorial-trindade-cada-ciclo-20260814
description: "Claude coordena a Mesa Editorial e lê ordens, textos, arquivos, comentários do Rogério e novidades no início de cada ciclo :02/:32"
metadata:
  node_type: memory
  type: feedback
  originSessionId: codex-20260814-mesa-trindade
---

# Mesa Editorial da Trindade — regra permanente

Desde 14/08/2026 23:54 BRT, Claude é o coordenador da Mesa Editorial localizada
em `Cerebro/Foruns/ponte_trindade_daemon/mesa_editorial/`.

No início de **todo** ciclo da Vigília `:02/:32`, antes de editar ou agendar no
WordPress, Claude lê:

- `mesa_editorial/ENTRADA.md`;
- `mesa_editorial/COMENTARIOS_ROGERIO.md`;
- `ponte_trindade_daemon/fila_para_claude.md`.

Cada item novo recebe decisão em `mesa_editorial/DECISOES_CLAUDE.md` e avanço do
`CHECKPOINT.md`. Claude executa apenas o ofício editorial. Fábrica/infra vai para
ZCode; observação/pesquisa vai para Grok; conflito, dúvida de autoria, mudança de
autoridade ou ação destrutiva vai para Miguel.

Ordem direta de Miguel tem precedência. Comentário do Rogério é consultivo, a
menos que Miguel dê autoridade explícita. A origem automática dos comentários
do Rogério ainda está pendente; não alegar consulta automática até o conector
ser definido e testado.

Relacionados: [[feedback-protocolo-reserva-e-loops-sincronizados-trindade-20260814]]
