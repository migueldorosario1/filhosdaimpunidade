# V4 — canário de ciência e geopolítica

**Data:** 2026-07-13 14:14 BRT  
**Responsável:** Codex  
**Estado:** pronto para testes shadow controlados; recibo emitido; sem publicação

## Decisão

O sprint foi limitado a ciência e geopolítica. Política nacional, cultura e tese 007 ficaram fora do escopo.

Foi adotado um runner incremental comum. Ele pode curar e persistir a linhagem automaticamente, mas para obrigatoriamente em uma seleção shadow humana e não simula autorização de Miguel.

O lançamento autorizado aqui é somente do canário local. WordPress, publicação, promoção, coleta externa, infraestrutura geral, bancos de dados e autocura não foram relançados neste sprint.

## Implementação

- runner e CLI: `root/v4_labs/codigo/canario_ciencia_geopolitica*.py`;
- contrato do runner: `v4_canario_ciencia_geopolitica_v1.json`;
- router novo: `v4_curadoria_router_v5.json`;
- geopolítica nova: contrato `v4_curadoria_internacional_v2.json`, plugin `curadoria_internacional_v2` e gate que distingue explicitamente a geração V2;
- ciência: preservado `v4_curadoria_ciencia_ia_v4.json`;
- downstream fixado em shadow pipeline V4, revisão V4 e fact-check V4;
- binder endurecido para copiar citação e tradução da canônica;
- fontes, declarações, prova temporal e extratos restritos a `dados/auditado`, com bloqueio de symlinks;
- `freshness_status=current` limitado a um dia da execução UTC; material antigo deve declarar `historical_context`;
- claims factuais novos precisam constar literalmente no trecho localizado da fonte e trazer metadados de fact-check;
- primeiro canário aceita somente citações diretas; tradução permanece bloqueada até revisão humana por hash;
- intake bruto e SHA entram na identidade, na canônica e no ledger;
- execução integral de cada item é serializada por lock e caminhos de saída com symlink ancestral são recusados.

O caso 005 e o contrato internacional V1 não foram alterados.

## Regra operacional

Agentes automáticos devem entrar exclusivamente por `V4ScienceGeopoliticsCanary` ou por `codigo.canario_ciencia_geopolitica_cli`. Chamadas diretas ao router, pipeline ou avaliador não carregam, em conjunto, as garantias de frescor UTC, alinhamento de intake novo e serialização integral.

## Verificação

- `OK 280 contract tests`;
- 11/11 agentes técnicos válidos em modo estrito;
- dois fluxos E2E registrados, um de ciência e um de geopolítica, da seleção ao fact-check V4, com replay idempotente;
- auditoria independente reexecutou os testes dirigidos, o histórico do caso 005 e os ataques de frescor, linhagem, citação, concorrência e symlink;
- recibo: `dados/testes/suite_receipt_796051a77b90fbf2144579d697ad9cb587d15baf641e77db68190036a829319a.json`;
- tree SHA: `796051a77b90fbf2144579d697ad9cb587d15baf641e77db68190036a829319a`.

## Próximo ato

Rodar um intake auditado novo de ciência como primeiro canário. Depois da seleção humana e do draft V5 estruturado, repetir com geopolítica. Ambos continuam locais, sem WordPress e sem qualquer promoção automática.
