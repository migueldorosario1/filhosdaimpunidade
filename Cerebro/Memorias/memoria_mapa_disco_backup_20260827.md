# 📊 MEMÓRIA TÉCNICA — Mapa do disco Dell + inventário de backups + plano de limpeza

**Data:** 27/08/2026 ~13:45 BRT · **Sessão:** ZCode/GLM-5.3 · **Fórum irmão:** `Foruns/forum_mapa_disco_limpeza_computador_20260827.md`

## Comandos usados (reprodutíveis)

- Disco/partições: `df -h / /home` · `lsblk -o NAME,SIZE,FSTYPE,MOUNTPOINT`
- Grandes blocos: `du -sh /home/migueldorosario/* /home/migueldorosario/.[!.]* | sort -rh`
- Antigravity Google: `du -sh "AG"/* | sort -rh` + ocultos `du -sh .[!.]*` (foi assim que os 67G "escondidos" apareceram: `.git` 28G + `.vercel` 22G + `.git_gordo_20260620` 18G)
- Git: `git count-objects -vH` → `size-pack: 27.38 GiB`; remote = `github.com/migueldorosario1/filhosdaimpunidade`
- Remotos: `rclone listremotes` → 11 remotos: `drive: gdrive: b2: b2-labs: masterb2: gdrive-backup-b2: b2_orlando: b2-tematicos: legacy-cafezinho: reforma_tencent_cafezinho: r2:`
- Medidas B2: `rclone size gdrive-backup-b2:Cerebro-Memorias` = 598,5 MiB / 16.575 obj; `b2_orlando:Orlando-Diniz-Dossie` = 434,5 MiB / 94 obj (idem no gdrive-backup-b2)
- Drive: `rclone lsd gdrive: --max-depth 1` e `rclone lsf "gdrive:Dados_Frios" --dirs-only` — **`orlando diniz` NÃO existe no Drive** (directory not found)

## Números crus (27/08 13:20-13:45)

### Disco
- `/dev/nvme0n1p3` 460G total · **375G usados · 62G livres · 86%**

### Home (top 25)
```
110G Dados_Frios          106G Downloads (=105G Antigravity Google)
 28G .deepseek             13G .local      13G .config     11G legacy
9,4G .gemini               7,0G .pyenv      6,5G .cache    5,9G Android
5,6G .npm                  4,2G .zcode      3,8G .nvm      2,7G ZCodeProject
2,1G .grok                 1,9G .codex      1,5G .android  1,4G .rustup
1,3G .mozilla              888M snap        746M .unsloth  671M .gradle
521M .antigravity          481M .apify      430M cerebro-miguel
```

### Dentro dos blocos
- `Dados_Frios`: orlando diniz **65G** (61G `doc lawfare oab`, 3G vídeos teste) · Rio Carta 11G · Backups_workspace 9,2G (2× refatoração 4,1G) · Jornais do dia 6,1G · Agentes Labs 5G · livros 3,7G · Bella Cia 2,3G · scratch 2,2G · mapario 2,2G · GSN 1,9G · Cafezinho Agentes 726M · zip dossiê 364M
- `Antigravity Google` (105G): **`.git` 28G · `.vercel` 22G (tudo em `output/`) · `.git_gordo_20260620` 18G** · Outros 27G (pautas editoriais 15G, Jornais do dia 5,7G, novo livro 2,5G, Aplicativos 1,8G, Negócios Priscila 1,7G) · Projeto Cafezinho Agentes 5,5G · agent_data 2,1G · Cicero 956M · moka 616M · scratch 582M · aiatolah 275M · **Cerebro 266M** · casadamoeda ~500M · claude-desktop.deb 159M · casadamoeda_backup tar.gz 130M
- `.deepseek`: **snapshots 28G** (2 hashes de jun/20 e jun/22) · sessions 61M
- `.gemini`: antigravity-browser-profile **6,6G** · antigravity 1,8G · antigravity-cli 1,2G
- `.config`: google-chrome **12G** · ZCode 632M · Antigravity.bak 218M+166M · chrome-data 204M
- `.local`: lib 7,1G · share 5,3G · bin 528M
- `.cache`: google-chrome 2,1G · whisper 1,8G · mozilla 1,1G · playwright 646M · huggingface 464M
- `.npm`: _cacache **5,3G** · _npx 393M
- `legacy/`: cafezinho_Legacy20260610 5,3G · outros_Rio_Carta_velho 4,1G · staging 138M · instaladores 109M · resto <100M cada
- `ZCodeProject`: moka-app 876M · igot 765M · mutirao_midia_v4 254M · cafezinhomediagroup 213M · dados_carnes 180M · cacai_teste 151M

### ~/.zcode (4,2G)
```
1,3G cli/db (db.sqlite 1,3G + shm/wal)   1,2G cli/agents (47 sessões, 09/jul→)
703M cli/exec (365)                       683M cli/artifacts (240)
 92M cli/log   71M cli/plugins  224M v2 (legado ACP)   2,4M cli/memories (371 .md) ← A MEMÓRIA DE VERDADE
```

## Mapa de backup (medido)

| Fonte | Conteúdo | Estado |
|---|---|---|
| `gdrive:` | Backup_Total, Cerebro_Backups, Dados_Frios (Rio Carta, Agentes Labs, Cafezinho Agentes, GSN, mapario, scratch, Jornais, livros, Bella Cia…), Legacy_2026_08_06, Cofres, Cérebro Imortal da Trindade, PONTE_DRIVE_LAURA/MANUS/Spark | 🟢 vivo (ago/2026) |
| `gdrive-backup-b2:` | Cerebro-Memorias 598MB · Orlando-Diniz-Dossie 434MB · backup-git-antigravity-20260620 · backup-total-local-2026 · Agents-Labs-Cafezinho · Cafezinho-operacional · Cafezinho-pos-grande-reforma-jun2026 · Legacy-Cafezinho · Legacy-Miguel · Backup-GoogleDrive-Miguel · bancodemidiageral · cafezinho-backups | 🟢 estrutura ampla |
| `b2_orlando:` | Orlando-Diniz-Dossie 434MB | 🔴 incompleto vs 65G local |
| `b2:` / `b2-tematicos:` / `b2-labs:` / `r2:` / `legacy-cafezinho:` / `reforma_tencent_cafezinho:` / `drive:` | específicos | não medidos nesta ronda |
| `masterb2:` | — | ⚠️ listagem vazia/timeout — investigar |
| GitHub | `cerebro-miguel` (sync 15 min) · `filhosdaimpunidade` (remote do AG .git) | 🟢 |

## Gaps de backup (riscos)

1. 🔴 Orlando Diniz lawfare 61G sem backup (só 434MB de 65G) — F6 urgente
2. 🟡 ZCode histórico (~3,9G) sem backup externo
3. 🟡 .deepseek/snapshots 28G sem backup
4. ⚠️ masterb2: possivelmente abandonado

## Plano (detalhe no fórum)

F0 prudência → **F6 backup Orlando (primeiro!)** → F1 limpeza segura ~30G (.vercel/output 22G + npm cache 5,3G + .cache seletivo) → F2 snapshots DeepSeek +28G via b2_arquivo → F3 .git_gordo +18G (após check B2) → F4 legacy/duplicatas +11-17G → F5 ZCode enxuto ~3G (memories INTOCÁVEL). Total ~100-130G.

## Estado final

- **O que aconteceu:** diagnóstico 100% medido ao vivo; Tema Duplo gravado; nada apagado; monitor atualizado.
- **O que falta:** "vai" do Miguel; execução F0-F6; confirmar gdrive:Backup_Total; investigar masterb2:.
- **Preciso do Miguel:** autorização (sugestão: F6+F1 na mesma noite).
