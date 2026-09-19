---
name: Histórico do canal Trindade — INDEX e procedimento de poda
description: Onde encontrar mensagens antigas do canal_trindade.md após podas + procedimento padrão de poda (mantenedor designado: Codex)
type: reference
originSessionId: 7c7867b0-668d-4c9f-9f68-fd2bf7f1ba99
---
O `Foruns/canal_trindade.md` é podado periodicamente para manter ~24h vivas. Cada poda gera arquivo arquivado em `Foruns/historico_canal_trindade/`. Listagem canônica:

**Índice formal:** [`Foruns/historico_canal_trindade/INDEX.md`](Foruns/historico_canal_trindade/INDEX.md) — criado em 2026-05-09 11:50 BRT por Claude a pedido de Miguel. Lista cada arquivo arquivado com faixa de datas, tamanho (linhas/bytes), distribuição diária de mensagens, sumário de eventos críticos por dia, e procedimento de manutenção.

**Arquivos atualmente arquivados:**
1. `BACKUPS/backup_canal/canal_claude_antigravity_20260504_a_20260506.md` (~400 KB, 2026-05-04 a 2026-05-06 ~12:50 BRT) — preservado no path original
2. `Foruns/historico_canal_trindade/canal_trindade_20260506_a_20260509_1146.md` (~980 KB, 13.074 linhas, 2026-05-06 ~12:55 a 2026-05-08 ~11:46 BRT)

**Cérebro:** `CEREBRO_NODE_COMUNICACAO.md` §6 linha 46 aponta para esse INDEX.

**Mantenedor designado pela §22:** Codex. Procedimento padrão (no INDEX): a cada vez que o canal vivo passar ~900 KB ou ~10.000 linhas, fazer backup → identificar linha de corte 24h → arquivar em `historico_canal_trindade/canal_trindade_<INI>_a_<FIM>.md` → reescrever canal vivo atomicamente (temp + `mv`) → atualizar INDEX com nova entrada → anunciar §22 no canal → validar com `scripts/validar_cerebro.py`.

**Como buscar decisão histórica sem abrir arquivos de 1 MB:**
```bash
grep -n -A5 '<termo>' Foruns/historico_canal_trindade/canal_trindade_*.md
grep -n -A5 '<termo>' BACKUPS/backup_canal/canal_*.md
```

**Padrão de nome para futuros arquivos:** `canal_trindade_YYYYMMDD_HHMM_a_YYYYMMDD_HHMM.md` (timestamps de início e fim no nome, sem ambiguidade).
