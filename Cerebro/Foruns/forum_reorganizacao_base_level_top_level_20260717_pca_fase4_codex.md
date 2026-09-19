# Fórum — Reorganização do topo de `Projeto Cafezinho Agentes` (Fase 4)

**Data:** 2026-07-17 01:45 BRT  
**Status:** concluída (execução local)

## Contexto
Foi solicitada redução de arquivos soltos no diretório base de `Projeto Cafezinho Agentes` com rastreabilidade explícita e sem apagamento.

## O que foi feito
- Levantado o topo do diretório e movidos **94 itens** para:
  - `legacy_reformado_20260717/toplevel_legacy/limpeza_extra_20260717/top/top_level_residuo_v4_20260717/base_level_clean_20260717`
- Mantidos apenas no topo:
  - `.env.unificado`
  - `.gitignore`
  - diretórios já canônicos do projeto

## Rastreabilidade
- Manifesto: `Projeto Cafezinho Agentes/legacy_reformado_20260717/toplevel_legacy/limpeza_extra_20260717/top/top_level_residuo_v4_20260717/base_level_clean_20260717/MANIFESTO_REORGANIZACAO_BASE_FILES_20260717.md`
- Inventário bruto: `Projeto Cafezinho Agentes/legacy_reformado_20260717/toplevel_legacy/limpeza_extra_20260717/top/top_level_residuo_v4_20260717/base_level_clean_20260717/.reorg_base_cleanup_inventory.txt`
- Decisão de estrutura: arquivos por categoria em subpastas (`markdown`, `yaml`, `json`, `python`, etc.)

## Pontos de atenção
- Esta operação é de reorganização estrutural; não altera conteúdo.
- Links históricos que apontavam para os nomes originais podem precisar de atualização de rota se acessarem diretamente esses arquivos no topo.
- Nenhum arquivo foi apagado.

## Ação após esta fase
- Ajustar os processos que dependem de caminhos de raiz (se necessário) em nova etapa de hardening de execução.
