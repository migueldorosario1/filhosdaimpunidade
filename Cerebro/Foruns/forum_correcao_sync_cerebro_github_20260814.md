# Fórum — Correção da sincronização contínua Cérebro ↔ GitHub

**Data:** 14/08/2026, 23:29 BRT  
**Autoridade:** pedido direto de Miguel

## Problema comprovado

O clone `cerebro-miguel` ficou dois commits à frente do `origin/main`. O script
antigo só executava `git push` quando criava um commit novo na mesma rodada.
Além disso, pull, rsync e push podiam começar no mesmo minuto, produzindo merge
e atraso. Uma oscilação real de DNS também impedia o rsync local mesmo quando o
clone já continha mensagens válidas de LAURA.

## Correção

- `sync_cerebro_to_github.py` agora usa lock compartilhado, integra o remoto
  antes da cópia, limita staging às árvores administradas, sempre tenta push e
  repete rejeições até três vezes.
- Novo `sync_cerebro_from_github.sh`: tenta GitHub três vezes e sempre reflete o
  último clone local confirmado no Cérebro, mesmo durante falha de rede.
- Entrada GitHub→MIGUEL: minutos `00/15/30/45`.
- Saída MIGUEL→GitHub: minutos `07/22/37/52`.
- As duas direções usam `/tmp/cerebro_git_sync.lock`, eliminando concorrência.

## Validação

- Três ACKs de LAURA chegaram ao Cérebro canônico.
- Worktree limpo.
- `HEAD...origin/main = 0/0`.
- Smoke sem mudanças: “Nada novo para commit” seguido de “GitHub alinhado”.
- Backups: `/tmp/sync_cerebro_to_github.py.bak_pre_bidirecional_20260814_2322`
  e `/tmp/crontab.bak_pre_cerebro_sync_20260814_2322`.

