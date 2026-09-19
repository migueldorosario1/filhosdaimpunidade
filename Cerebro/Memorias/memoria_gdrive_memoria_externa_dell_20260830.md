# 🧠 Memória técnica — GDrive como memória externa (Dell leve) — 30/08/2026

Log técnico completo da missão (fórum irmão: `Foruns/forum_gdrive_memoria_externa_dell_20260830.md`). Agente: ZCode/GLM-5.3. Base de operação: `~/gdrive_offload/`.

## Ambiente/provas-chave (30/08 manhã)

- Disco: `/dev/nvme0n1p3` 460G; início 273G usados (63%) → 266G (61%) após caches; meta final pós-fila ≈ 230G (~50%).
- rclone v1.73.2. Remotes `drive:` e `gdrive:` = **o mesmo shared drive** (`root_folder_id 0ACcwJvRkbvrgUk9PVA`), 30 TiB totais, 29,2 livres. `rclone about drive:` OK sem login novo.
- Crons relevantes pré-existentes: acervo-100 diário 04:30 (`backup_acervo_100_b2_drive.sh` → drive:+B2, teto 17G/rodada nos pesados), `backup_cerebro_diario.sh` 03:40 (B2+Drive+Alibaba), ponte→`drive:espelho-zcode/ponte_zcode` a cada 30min, jornais→`gdrive:Jornais do dia` 3x/dia (`jornaisdodia.sh`, `--include *.pdf --ignore-existing`).

## Checks prévios (rclone check, 30/08 10:26–10:44)

- `Outros/pautas editoriais o cafezinho` vs `drive:pautas editoriais o cafezinho`: **1.090 casados, 2.462 FALTANDO no Drive** (acervo-100 nunca completou por tpslimit/timeout 45min) → fila faz top-up antes de apagar.
- `~/legacy` vs `drive:Backup_Total/legacy`: **53.984/53.984 locais casados**; rc=1 por causa de 12.051 arquivos que SÓ existem no Drive ('+ ') — inofensivo p/ apagamento local.
- `Outros/Negocios Priscila/legenda trailer ressurrection` vs `drive:Workspace_Vivo/Outros/Negocios Priscila/legenda trailer ressurrection`: **27/27 casados, 0 diferenças** (pasta inteira é entregas prontas; docs/filme palestina ficam locais).
- `Outros/Jornais do dia`: Drive tem 30,49 GiB/1.175 arquivos; local 5,7G só de recentes (0 PDFs >21d) → nada a fazer.

## Gate de apagamento (offload_item.sh)

`rclone copy` → `rclone check --combined` → apaga SOMENTE se: rc=0 OU (rc=1 E missing=0 E diff=0 E matched>0 — rc=1 pode ser só sobra no destino; matched>0 prova que o combined não veio vazio de crash de rede). Deleção via `rclone delete` + `rclone rmdirs` com as MESMAS flags do copy. Carimbo JSONL em `~/gdrive_offload/CARIMBOS.jsonl` com ok:true/false e bytes. Falha = item pulado, local intacto.

## Mount ~/GDrive (systemd user)

- Unit `~/.config/systemd/user/gdrive-mount.service`: Type=notify, `rclone mount drive: /home/migueldorosario/GDrive --vfs-cache-mode writes --vfs-cache-max-size 2G --vfs-cache-max-age 24h --dir-cache-time 12h --umask 022`, Restart=on-failure, `Environment=PATH=/home/migueldorosario/.local/bin:/usr/bin:/bin`.
- **PEGADINHA 1:** rclone 1.73 no Ubuntu 20.04 falha com `fusermount3: executable file not found` (quer fuse3; só há fuse2). Cura: `ln -s /usr/bin/fusermount ~/.local/bin/fusermount3` + PATH no unit (systemd user NÃO lê o PATH do bashrc).
- **PEGADINHA 2:** testar mount com pipe (`rclone mount ... | head`) mata o daemon e a listagem aborta com "Término de conexão causada por software" — teste via serviço ou log em arquivo.
- Prova final: mountpoint OK + ls lista a raiz do shared drive + escrita/leitura/remoção de `.prova_mount_zm_20260830.txt` OK.

## Caches (−7G)

Apagados: `~/.cache/google-chrome` 2,5G · `~/.config/google-chrome/OptGuideOnDeviceModel` 4G (modelo de IA on-device do Chrome; re-baixa se precisar) · `~/.npm/_cacache` · updater/uv/node-gyp/Tectonic · `AG/claude-desktop_amd64.deb` 159M (instalador re-baixável) · tar.gz Casa da Moeda 136M (conferido no Drive). **Mantido:** `~/.cache/whisper` 1,8G (modelos de transcrição que as missões de vídeo podem precisar; re-baixa é cara). **Service Worker 4,3G:** só apaga com Chrome FECHADO (`sw_purge_quando_fechar.sh`, cron */30, flag SW_PURGE_DONE).

## Crons novos (backup em `~/bin/crontab.bak_pre_dell_leve_20260830`)

```
40 15 * * * backup_cerebro_diario.sh  # CEREBRO_BACKUP_12H_20260830 (12h/12h c/ o 03:40)
50 6 * * * rclone copy ~/.dsh drive:Backup_Total/DSH_Dell_memoria --exclude deepseek_env --exclude ponte_amizade_env --exclude settings.yaml --exclude .anonymous-user-id  # DSC_MEMORIA_DRIVE_20260830
*/30 * * * * sw_purge_quando_fechar.sh  # SW_PURGE_CHROME_20260830
```

## DSC/DSH no Drive

`drive:Backup_Total/DSH_Dell_memoria`: sessions (36M) + profiles (1,9M) + `pacote_dsc/pacote_dsc.tar.gpg` (1043 bytes, cifrado — o mesmo do DSC-013 no repo). 99 arquivos, rc=0. Envs de texto plano e settings.yaml EXCLUÍDOS (§82). NOTA: symlinks de node_modules do profile não sobem sem -L (inofensivo).

## Fila (rodar_fila.sh, nohup — sobrevive à sessão)

1. `AG/mapa videos` → `drive:Dados_Frios/Dell_leve_20260830/mapa_videos` (2,2G)
2. `AG/Outros/pautas editoriais o cafezinho` → `drive:pautas editoriais o cafezinho` (15G, top-up 2.462)
3. `~/legacy` → `drive:Backup_Total/legacy` (11G, copy é no-op; delete direto)
4. `AG/Outros/Negocios Priscila/legenda trailer ressurrection` → `drive:Workspace_Vivo/Outros/...` (7,9G, idem)

Ao fim grava `DF_ANTES/DF_DEPOIS.txt` e deixa ponteiros `*_MOVIDO_PARA_O_DRIVE.txt` nos lugares. Velocidade alvo: `--bwlimit 10M`, tpslimit 8.

## Lições

1. **DECLARADO ≠ EXISTE** (2ª vez): "Outros está no Drive" do acervo-100 estava INCOMPLETO p/ pautas (2.462 faltantes) — sempre `rclone check` antes de apagar.
**RETIFICAÇÃO 11:30:** o item acima sobre pautas estava INVERTIDO — '- ' no combined = existe SÓ NO DRIVE. Drive pautas = SUPERCONJUNTO (3.552/28,5 GiB vs 1.090/15G local). Gate corrigido: bloqueia '+ ' (só-local) e '* ' (diff).
2. `rclone check` rc=1 não significa "local sem backup": '+' (sobras no destino) são seguras; gate deve olhar missing/diff/matched, não só rc.
3. fusermount3 symlink + PATH no unit (acima).
4. Monitor/arquivos quentes (sync de 15 em 15min): Edit tool falha por "modified since read" — inserção via python atomica resolveu.
5. `rclone --daemon` pode devolver rc=0 mesmo com falha tardia do filho — verificar com `mountpoint` + ls real.
6. Sessão paralela (índice GDrive) trabalhando em `Outros/indices/` ao mesmo tempo → mantive indices local e coordenei pela ponte antes de escrever no Drive.

## Restauração (receitas)

```bash
rclone copy "drive:pautas editoriais o cafezinho" "/home/migueldorosario/Downloads/Antigravity Google/Outros/"
rclone copy "drive:Backup_Total/legacy" "/home/migueldorosario/legacy"
rclone copy "drive:Workspace_Vivo/Outros/Negocios Priscila/legenda trailer ressurrection" "/home/migueldorosario/Downloads/Antigravity Google/Outros/Negocios Priscila/"
rclone copy "drive:Dados_Frios/Dell_leve_20260830/mapa_videos" "/home/migueldorosario/Downloads/Antigravity Google/"
```
