# Fórum — Reforma de Estrutura no Diretório `Projeto Cafezinho Agentes`

Data: 17/07/2026

## Status resumido
Reorganização executada sem exclusão:
- Tudo que estava claramente legado, histórico ou backup de sprint foi movido para:
  - `legacy_reformado_20260717/toplevel_legacy`
  - `legacy_reformado_20260717/agents_labs_legacy`
  - `legacy_reformado_20260717/foruns_legacy`
- O fluxo v4 atual foi preservado em `/root`, `/agents_labs/youtube_v2`, `/agents_labs/ceo_cerebro`, `Foruns/inbox_trindade` e `Foruns/canal_trindade.md` (sem exclusão/regravação).
- Foram movidos 28 blocos principais.

## Principais decisões
1. **Tornar explícito o que é canônico**: manter só o que é usado no loop ativo.
2. **Isolar legado sem risco**: nada apagado; tudo foi movido para um diretório único e rastreável.
3. **Evitar ruído operacional**: remover da raiz diretórios de sprint/bkp antigo e versões obsoletas de agentes.

## Arquivo fonte da migração
- `legacy_reformado_20260717/MANIFESTO_REORGANIZACAO_AGENTES_CAFEZINHO_20260717.md`

## Itens mais relevantes movidos
- `A_GRANDE_REFORMA_LOCAL_20260610`, `Agente Tiktok`, `Agente Youtube`, `Backups`, `backups_operacionais`.
- `Foruns/backups_*`, `Foruns/historico_*`, `Foruns/parqueados`, `Foruns/snapshots_estado`, `Foruns/monitoramento`, `Foruns/summaries`.
- `agents_labs/calhau_v3`, `agents_labs/copa_v2`, `agents_labs/grande_reforma_v2`, `agents_labs/politica_v2`, `agents_labs/politica_v3`, `agents_labs/youtube_nacional_v3`.

## O que permanece no lugar (e deve ser tratado como ativo)
- `root`
- `root/v4_labs`
- `agents_labs/youtube_v2`
- `agents_labs/ceo_cerebro`
- `sites-tematicos`
- `Foruns/inbox_trindade`
- `Foruns/canal_trindade.md`
- `Foruns/sub_cerebro_antigravity_desktop.md`
- `Foruns/sub_cerebro_antigravity_miguel.md`

## Ação de continuidade recomendada
- Próximo agente deve ler o manifesto acima antes de tocar em `agents_labs` ou `Foruns`.
- Qualquer restauração de legado deve ser decisão explícita; padrão é manter no diretório `legacy_reformado_20260717/...`.

