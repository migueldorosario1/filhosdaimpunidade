# 🧠 Memória — Emagrecimento do Workspace + Nuvem-First (2026-07-22)

> **Agente:** ZCode/Kimi | **Solicitante:** Miguel | **Fórum de decisões:** `../Foruns/forum_emagrecimento_workspace_nuvem_first_20260722.md`
> Log técnico completo: o que saiu de onde, para onde foi, e como o backup funciona.

## 1. Mapeamento inicial (disco 460G, 256G usados)

- `~/Downloads/Antigravity Google` = **153G** (a IDE não abria)
- `~/legacy` = 11G | resto leve
- Drive (`gdrive:` = `drive:`, mesmo Drive): 30TB total, ~472G usados
- Já existia no Drive: `backup 20260717` (47,5G, snapshot de 17/07), `Jornais do dia` (25G, arquivo mestre), `Cérebro Imortal da Trindade` (208M)
- **Buraco crítico:** `orlando diniz` local 63G vs 2,4G no Drive (`doc lawfare oab` local 61G vs 216M no Drive); `pautas editoriais o cafezinho` 14G ausente do Drive

## 2. O que foi movido (153G → 23G) — tudo para `~/Dados_Frios/`

### Bloco 1 (manhã/tarde) — 108G
| Origem (em `Antigravity Google/`) | Destino em `~/Dados_Frios/` | Tam. |
|---|---|---|
| `Outros/orlando diniz` | `orlando diniz/` | 63G |
| `Outros/pautas editoriais o cafezinho` | `pautas editoriais o cafezinho/` | 14G |
| `Outros/Jornais do dia` (PDFs) | `Jornais do dia/` | 6,1G |
| `Outros/Agentes Labs` | `Agentes Labs/` | 5G |
| `Outros/livros baixados novos` | `livros baixados novos/` | 3,6G |
| `Outros/Bella Cia Project` | `Bella Cia Project/` | 2,3G |
| `Outros/mapario` | `mapario/` | 2,2G |
| `Outros/Aplicativos` | `Aplicativos/` | 1,3G |
| `Backups` (raiz workspace) | `Backups_workspace/` | 9,2G |
| `Outros/Backups` | `Backups_outros/` | 561M |
| `Outros/Backup_Dossie_Orlando_Diniz_Completo.zip` | raiz | 364M |

### Bloco 2 (3 camadas aprovadas pelo Miguel) — ~23G
- **Camada 1 (frio óbvio):** `Rio Carta Agentes/server doin` (5,3G, tars 2018–2026), `Rio Carta Agentes/build_backups` (1,8G), `Projeto Cafezinho Agentes/legacy_reformado_20260717` (726M), `scratch/root_full_backup_20260616_0101.tar.gz` (1,2G), `scratch/dados_tse` (609M), mídias soltas do scratch → `Dados_Frios/scratch/midia/` (~430M), docs frios do Outros → `Dados_Frios/Outros_docs/` (analise politica curso, Projeto Casa da Moeda, Jornal da Forum, Manus, a grande reforma v2)
- **Camada 2 (builds):** `Projeto Cafezinho Agentes/sites-tematicos` (3,5G) e `sites-v4` (1,9G) → `Dados_Frios/Projeto Cafezinho Agentes/`
- **Camada 3 (.git gordo):** `Rio Carta Agentes/rio_carta` (3,9G, .git 2,4G) → `Dados_Frios/Rio Carta Agentes/`; `Global South News/gsn` (1,9G, .git 1,6G) → `Dados_Frios/Global South News/`; `Cicero Agentes/cicero` (735M) → `Dados_Frios/Cicero Agentes/`

### ⚠️ Correção no mesmo dia
`Outros/novo livro` (93M) foi movido por engano na Camada 1 e **devolvido imediatamente** ao workspace: é o projeto ATIVO do Vol. 1 "O Foragido" (esqueleto oficial, PLANO_DE_TRABALHO.md, sprint 22/07→05/08). **Nunca mover.**

## 3. O que PERMANECE no workspace (23G) — intocável

- Código vivo: `Rio Carta Agentes/root`, `Global South News/root`, `Cicero Agentes/root`, `aiatolah`, `Cerebro` (canônico!), `Projeto Cafezinho Agentes/{root,Foruns,scripts,agents_labs,agent_data,...}`
- `scratch/` — só os scripts de cron (jornaisdodia via Outros, limpa_diario, backup_reforma_local, enviar_baleia_azul_v2)
- `Outros/Jornais do dia/` — pasta-staging só com `jornaisdodia.sh` + log (cron 10:30/12:00 segue válido)
- `Outros/novo livro` — projeto ativo

## 4. Crontab alterado (22/07)

- **Comentados (tag `DESATIVADO 2026-07-22`):** `@reboot` painel CCTV v5 + `* * * * *` watchdog_painel.sh — ambos apontavam para `Projeto Cafezinho Agentes/Legacy20260610/` (inexistente desde 17/07, está em `~/legacy/cafezinho_Legacy20260610_20260717`). Painel estava morto há 5 dias.
- **Adicionado:** `0 3 * * * /home/migueldorosario/bin/backup_semana_gdrive.sh`
- Observação: `backup_reforma_local.sh` (horário, B2) referencia `A_GRANDE_REFORMA_LOCAL_20260610` — também inexistente; passo falha silenciosamente, demais passos OK. Não alterado (fora do escopo aprovado).

## 5. Como funciona o backup das 7 noites

- **Script:** `~/bin/backup_semana_gdrive.sh` (bash + rclone; validado `bash -n`)
- **Fila priorizada (17 itens):** `orlando diniz` → `Jornais do dia` → `pautas editoriais` → demais para `gdrive:Dados_Frios/<pasta>`; `orlando diniz` e `Jornais do dia` vão para suas casas canônicas já existentes no Drive (dedup automático: `rclone copy` pula idênticos por tamanho+mtime — "não repetir" garantido por construção)
- **Cota:** 17 GiB/noite (`--max-transfer`, cutoff soft); madrugada livre, após 08:00 limita a 5M (`--bwlimit "03:00,off 08:00,5M"`)
- **Estado:** `~/log/backup_semana_estado.txt` (item só vira DONE após `rclone check --one-way --size-only` passar); **Log:** `~/log/backup_semana_gdrive.log`
- **Previsão:** 131G ÷ 17 GiB ≈ 8 noites (dedup de orlando/jornais deve encurtar para ~7)
- **Bytes por noite:** parseados do `--use-json-log` (`stats.bytes`); se o parse falhar, a noite encerra conservadoramente

## 6. Pós-fila (não esquecer)

1. `rclone check` completo de cada par origem/destino
2. Só então `rm -rf ~/Dados_Frios` → disco cai para ~127G usados (27%)
3. Opcional: `rclone mount gdrive: ~/Drive --vfs-cache-mode full` (acesso sob demanda sem baixar)
