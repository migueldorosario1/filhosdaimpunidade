# CONTROLES — espelho git das flags de pause (P2, obra Reforma V3 — ZM-20260910-010)

Flags `<CHAVE>.pause` = botão de pause do painel /v6/agentes valendo entre máquinas (P2 instalada em 10/09/2026):

- FONTE da verdade: `/home/ubuntu/cafezinho/v6_data/controles/` no **tencent** (o painel escreve lá; `auditoria.jsonl` não vem ao espelho).
- **tencent**: 20 guards (13 crontab ubuntu + 7 root) lendo a pasta local.
- **nyc**: 31 guards lendo `/root/controles_pause/`, puxada do tencent por rsync `*/2` com --delete (`P2_CONTROLES_SYNC_20260910`).
- **dell**: 11 guards lendo ESTA pasta do repo (mantida pelo espelhador `*/2` `~/bin/espelha_controles_p2.sh`, que commita e pusha as mudanças; README nunca é apagado — exclude).
- Pause é GRACIOSO (bloqueia a próxima execução, não mata a em curso). `.pause` órfão = agente parado: checar AQUI e no tencent antes de debugar.
- Rollback da P2: restaurar `crontab.bak_pre_p2_20260910` de cada usuário tocado (ubuntu/root tencent; root nyc; usuário dell) + remover os crons `P2_CONTROLES_SYNC`/`P2_ESPELHA_CONTROLES`. Flags aqui ficam (inofensivas sem guards).
- Design, mapa de chaves e provas: `Foruns/forum_atualizacao_reforma_v3_20260908.md` §14-ZM e §14.1.
