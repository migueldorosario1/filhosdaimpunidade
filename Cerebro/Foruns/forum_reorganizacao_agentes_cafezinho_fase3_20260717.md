# Fórum — Reorganização Fase 3 do `Projeto Cafezinho Agentes` (17/07/2026)

Status: **concluído parcial e seguro (sem deleção)**

Resumo da passada:
- Mantive o núcleo operacional e movi para `legacy` todo material de fórum histórico que não está no trilho ativo.
- Também isolei resíduos top-level (cadastros de assistente/caches/arquivos `.bak` e cron antigo) em `legacy_reformado_20260717`.

## Resultado imediato

- `Foruns/` (ativo) agora: **29 arquivos + 1 pasta (`inbox_trindade`)**
- `Foruns/` legadas: **1059 itens** em
  `legacy_reformado_20260717/toplevel_legacy/limpeza_extra_20260717/foruns/foruns_ativos_pruning_20260717`
- Resíduos top-level isolados: **11 itens** em
  `legacy_reformado_20260717/toplevel_legacy/limpeza_extra_20260717/top/top_level_residuo_v4_20260717`

## Arquivos de controle desta passada

- Manifesto: `Projeto Cafezinho Agentes/legacy_reformado_20260717/MANIFESTO_REORGANIZACAO_AGENTES_CAFEZINHO_FASE3_20260717.md`
- Inventário `Foruns` legado: `.../foruns_ativos_pruning_20260717/INVENTARIO_FASE3.md`
- Inventário top-level legado: `.../top_level_residuo_v4_20260717/INVENTARIO_FASE3_TOP.md`

## Riscos e cautelas

- `0` deleção. Tudo moveu por `mv` e pode ser restaurado.
- Mantive no ativo `foruns` os itens de operação e continuidade (jul/2026+), principalmente:
  - `canal_trindade.md`
  - `inbox_trindade/`
  - fóruns/v4 e fóruns de continuidade recentes.

## Próximo passo sugerido

- Prosseguir com a mesma regra para `Ponto de Retomada` e subpastas de `sites-tematicos` apenas após validação de última rodada de uso.

