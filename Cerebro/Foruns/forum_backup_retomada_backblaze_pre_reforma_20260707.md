# Forum - Backup Backblaze e Retomada Pre-Reforma de Diretrizes

Aberto em: 2026-07-07 19:03:22 -03  
Responsavel operacional: Codex  
Status: backup pausado, retomada pendente

## 1. Motivo

Este forum existe para nao perdermos o estado do backup feito antes da nova grande reforma de diretrizes.

A regra central permanece:

> Nao iniciar a reforma grande de diretrizes antes de retomar, concluir e validar o backup.

## 2. Onde Esta o Backup

Origem local:

```text
/home/migueldorosario/Downloads/Antigravity Google
```

Destino Backblaze B2 do espelho do workspace:

```text
b2:failover-cafezinho1/Antigravity_Google/backups/pre_reforma_diretrizes_20260707_171801/workspace/
```

Area de controle no Backblaze:

```text
b2:failover-cafezinho1/Antigravity_Google/backups/pre_reforma_diretrizes_20260707_171801/controle/
```

Pasta local de controle:

```text
Backups/pre_reforma_diretrizes_20260707_171801/
```

## 3. Estado Atual

O backup foi pausado manualmente em 2026-07-07 19:00:32 -03, a pedido do usuario.

Ultimo progresso visto no terminal antes da pausa definitiva:

- `13.194 GiB / 36.032 GiB`
- `37%` por volume
- `31436` arquivos listados
- `2380 / 12402` no contador do rclone

Estado confirmado no Backblaze apos a pausa:

- `2381` objetos
- `1.902 GiB`

Observacao importante:

- O volume confirmado no B2 e menor que os `13.194 GiB` tentados porque arquivos grandes estavam em upload multipart e foram cancelados antes do commit final.
- As linhas `ERROR ... context canceled` no log sao consequencia da pausa manual.
- Isso nao e, por si so, diagnostico de corrupcao.

## 4. Arquivos de Controle Ja Criados

Locais:

```text
Backups/pre_reforma_diretrizes_20260707_171801/MANIFESTO_BACKUP.md
Backups/pre_reforma_diretrizes_20260707_171801/ROLLBACK.md
Backups/pre_reforma_diretrizes_20260707_171801/CHECKPOINT_EM_ANDAMENTO.md
Backups/pre_reforma_diretrizes_20260707_171801/CHECKPOINT_PAUSA_20260707_190032.md
Backups/pre_reforma_diretrizes_20260707_171801/git_status_short.txt
Backups/pre_reforma_diretrizes_20260707_171801/git_diff_stat.txt
Backups/pre_reforma_diretrizes_20260707_171801/arquivos_cerebro_diretrizes_foruns.txt
Backups/pre_reforma_diretrizes_20260707_171801/sha256_criticos.txt
```

Forum tecnico relacionado:

```text
Cerebro/Foruns/forum_backup_pre_reforma_diretrizes_20260707.md
```

Este forum de retomada:

```text
Cerebro/Foruns/forum_backup_retomada_backblaze_pre_reforma_20260707.md
```

## 5. Como Retomar

Retomar com `rclone copy` no mesmo destino. Nao usar `rclone sync`.

```bash
cd "/home/migueldorosario/Downloads/Antigravity Google"

rclone copy . \
  b2:failover-cafezinho1/Antigravity_Google/backups/pre_reforma_diretrizes_20260707_171801/workspace/ \
  --fast-list \
  --transfers 6 \
  --checkers 16 \
  --progress \
  --stats 30s \
  --log-file /tmp/rclone_full_pre_reforma_diretrizes_20260707_171801_resume.log \
  --log-level INFO
```

Motivo:

- `copy` pula objetos que ja existem e reenvia ausentes/diferentes.
- `sync` pode apagar destino e nao deve ser usado nesta etapa.

## 6. Arquivos Grandes Interrompidos

O log indicou interrupcao manual durante uploads multipart destes objetos grandes:

- `.git_gordo_20260620/rebased-patches`
- `scratch/root_full_backup_20260616_0101.tar.gz`
- `.git_gordo_20260620/objects/pack/pack-408609e378d57b04da9088d83ae7161789fb9d7a.pack`
- `Outros/Bella Cia Project/Poster/Poster.zip`
- `Rio Carta Agentes/server doin/2018.tar`

Na retomada, esses arquivos devem ser reenviados ou completados conforme o rclone comparar origem/destino.

## 7. Validacao Obrigatoria Depois do Fim

Antes de declarar o backup fechado:

1. Rodar `rclone size` no destino.
2. Comparar inventario local e remoto.
3. Rodar `rclone check` ou validacao equivalente.
4. Tratar explicitamente os avisos de symlink `Can't follow symlink without -L/--copy-links`.
5. Atualizar este forum.
6. Atualizar `Cerebro/Foruns/forum_backup_pre_reforma_diretrizes_20260707.md`.
7. Atualizar `Cerebro/CEREBRO_NODE_BACKUPS_BACKBLAZE.md`.

## 8. Observacao Sobre Symlinks

O log do rclone registrou varios avisos:

```text
Can't follow symlink without -L/--copy-links
```

Eles aparecem em indices antigos dentro de:

```text
Projeto Cafezinho Agentes/A_GRANDE_REFORMA_LOCAL_20260610/cafezinho/Cerebro/Foruns/por_tag/...
```

Pendencia:

- decidir se esses symlinks devem ser preservados como symlink, seguidos com `--copy-links`, ou apenas documentados como indices derivados.

## 9. Proximo Passo

Quando o usuario mandar retomar:

1. executar o comando de retomada acima;
2. acompanhar ate concluir;
3. salvar novo checkpoint;
4. validar;
5. so entao liberar a reforma grande de diretrizes.
