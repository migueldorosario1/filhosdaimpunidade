# Carta humanizada para Codex e Trindade — Fase 3 da reforma do `Projeto Cafezinho Agentes`

Pessoal, finalizei uma rodada forte de reorganização no `Projeto Cafezinho Agentes`.

Objetivo: deixar o ativo limpo e com trilha útil para a operação, sem perder nada.

O que foi feito:

- Em `Foruns/`, mantive somente o núcleo vivo e movi o restante histórico para:
  `legacy_reformado_20260717/toplevel_legacy/limpeza_extra_20260717/foruns/foruns_ativos_pruning_20260717`.
  Foram **1059 itens** isolados lá.
- Removi do topo do projeto ruído de cache/backup antigo (sem apagar):
  `.agents`, `.claude`, `.codex`, `.pytest_cache`, `.bak` antigos, cron de backup legado e arquivos de ambiente legado.
  Isso foi para:
  `legacy_reformado_20260717/toplevel_legacy/limpeza_extra_20260717/top/top_level_residuo_v4_20260717`.
  Foram **11 itens**.

Arquivos de controle dessa passada:

- `MANIFESTO_REORGANIZACAO_AGENTES_CAFEZINHO_FASE3_20260717.md`
- `foruns/foruns_ativos_pruning_20260717/INVENTARIO_FASE3.md`
- `top/top_level_residuo_v4_20260717/INVENTARIO_FASE3_TOP.md`

Pontos importantes:

- Nada foi apagado.
- Se precisarmos recuperar qualquer item antigo, retorno por movimento inverso a partir do `legacy`.
- O ativo ficou reduzido para 29 arquivos de fórum + `inbox_trindade`, o que facilita achar o que realmente está em uso.

Se quiserem continuidade, o próximo corte pode seguir o mesmo padrão em:
`Ponto de Retomada/` e módulos de `sites-tematicos`.

