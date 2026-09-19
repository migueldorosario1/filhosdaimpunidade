# 🗂️ CEREBRO_INDEX — REFORMA DE ARQUIVOS 2026-07-22 ("Onde está cada pasta?")

> **[NODO_REFORMA_ARQUIVOS_20260722]** — Índice canônico da reforma de arquivos de 22/07/2026.
> **Quem procurar qualquer arquivo que "sumiu" do workspace: CONSULTE ESTE ÍNDICE PRIMEIRO.**
> Nada foi deletado. Tudo foi **movido** (mesmo disco) para `~/Dados_Frios/` e será espelhado no Google Drive ao longo de ~7 madrugadas (cron 03:00).
> Fórum: `Foruns/forum_emagrecimento_workspace_nuvem_first_20260722.md` | Memória técnica: `Memorias/memoria_emagrecimento_workspace_nuvem_first_20260722.md`

## Legenda de locais

| Sigla | Caminho |
|---|---|
| **WS** | `/home/migueldorosario/Downloads/Antigravity Google/` (workspace da IDE — era 153G, ficou 23G) |
| **DF** | `/home/migueldorosario/Dados_Frios/` (área de espera fora da IDE — 131G, fila de upload) |
| **GD** | Google Drive via `rclone` (remote `gdrive:` = `drive:`; 30TB) |

---

## A) MOVIDOS: WS → DF (e destino futuro no GD)

| Onde estava (WS) | Onde está agora (DF) | Tam. | Destino no Drive (7 noites) |
|---|---|---|---|
| `Outros/orlando diniz` | `DF/orlando diniz/` | 63G | `gdrive:orlando diniz` (casa canônica, dedup) |
| ↳ `doc lawfare oab` (61G — crítico, só existia local!) | `DF/orlando diniz/doc lawfare oab/` | 61G | `gdrive:orlando diniz/doc lawfare oab` |
| `Outros/pautas editoriais o cafezinho` | `DF/pautas editoriais o cafezinho/` | 14G | `gdrive:pautas editoriais o cafezinho` |
| `Outros/Jornais do dia` (PDFs; script ficou no WS) | `DF/Jornais do dia/` | 6,1G | `gdrive:Jornais do dia` (casa canônica, maioria já lá) |
| `Outros/Agentes Labs` | `DF/Agentes Labs/` | 5G | `gdrive:Dados_Frios/Agentes Labs` |
| `Outros/livros baixados novos` | `DF/livros baixados novos/` | 3,6G | `gdrive:Dados_Frios/livros baixados novos` |
| `Outros/Bella Cia Project` | `DF/Bella Cia Project/` | 2,3G | `gdrive:Dados_Frios/Bella Cia Project` |
| `Outros/mapario` | `DF/mapario/` | 2,2G | `gdrive:Dados_Frios/mapario` |
| `Outros/Aplicativos` | `DF/Aplicativos/` | 1,3G | `gdrive:Dados_Frios/Aplicativos` | ⚠️ **DEVOLVIDO 22/07 (Miguel): Moka + MokaVideo voltaram ao workspace (projetos ativos); pasta retirada da fila de backup.**
| `Outros/Backups` | `DF/Backups_outros/` | 561M | `gdrive:Dados_Frios/Backups_outros` |
| `Outros/Backup_Dossie_Orlando_Diniz_Completo.zip` | `DF/Backup_Dossie_Orlando_Diniz_Completo.zip` | 364M | `gdrive:Dados_Frios/` |
| `Backups` (raiz do WS) | `DF/Backups_workspace/` | 9,2G | `gdrive:Dados_Frios/Backups_workspace` |
| `Rio Carta Agentes/server doin` (tars 2018–2026) | `DF/Rio Carta Agentes/server doin/` | 5,3G | `gdrive:Dados_Frios/Rio Carta Agentes/server doin` |
| `Rio Carta Agentes/build_backups` | `DF/Rio Carta Agentes/build_backups/` | 1,8G | `gdrive:Dados_Frios/Rio Carta Agentes/build_backups` |
| `Rio Carta Agentes/rio_carta` (projeto + .git 2,4G) | `DF/Rio Carta Agentes/rio_carta/` | 3,9G | `gdrive:Dados_Frios/Rio Carta Agentes/rio_carta` |
| `Projeto Cafezinho Agentes/sites-tematicos` | 🔁 **DEVOLVIDO ao workspace 2026-07-22** (crons de produção 9h15–9h45: ceara-digital, global_south_news, cafezinho) | 3,5G | fora da fila do backup |
| `Projeto Cafezinho Agentes/sites-v4` | `DF/Projeto Cafezinho Agentes/sites-v4/` | 1,9G | `gdrive:Dados_Frios/Projeto Cafezinho Agentes/sites-v4` |
| `Projeto Cafezinho Agentes/legacy_reformado_20260717` | `DF/Projeto Cafezinho Agentes/legacy_reformado_20260717/` | 726M | `gdrive:Dados_Frios/Projeto Cafezinho Agentes/legacy_reformado_20260717` |
| `Global South News/gsn` (projeto + .git 1,6G) | `DF/Global South News/gsn/` | 1,9G | `gdrive:Dados_Frios/Global South News/gsn` |
| `Cicero Agentes/cicero` | 🔁 **DEVOLVIDO ao workspace 2026-07-22** (cron produção 10h) | 735M | fora da fila do backup |
| `scratch/root_full_backup_20260616_0101.tar.gz` | `DF/scratch/` | 1,2G | `gdrive:Dados_Frios/scratch/` |
| `scratch/dados_tse` | `DF/scratch/dados_tse/` | 609M | `gdrive:Dados_Frios/scratch/dados_tse` |
| `scratch/*.mp4, *.mp3, imagens soltas` | `DF/scratch/midia/` | ~430M | `gdrive:Dados_Frios/scratch/midia` |
| `Outros/analise politica curso` | `DF/Outros_docs/analise politica curso/` | 304M | `gdrive:Dados_Frios/Outros_docs/` |
| `Outros/Projeto Casa da Moeda` (⚠️ já existia no GD: `gdrive:Projeto Casa da Moeda`) | `DF/Outros_docs/Projeto Casa da Moeda/` | 256M | `gdrive:Dados_Frios/Outros_docs/` |
| `Outros/Jornal da Forum` | `DF/Outros_docs/Jornal da Forum/` | 152M | `gdrive:Dados_Frios/Outros_docs/` |
| `Outros/Manus` | `DF/Outros_docs/Manus/` | 142M | `gdrive:Dados_Frios/Outros_docs/` |
| `Outros/a grande reforma v2` | `DF/Outros_docs/a grande reforma v2/` | 121M | `gdrive:Dados_Frios/Outros_docs/` |

## B) FICARAM no WS (23G) — intocáveis

- `Cerebro/` (canônico) | `Outros/novo livro` (**projeto ATIVO Vol. 1 — nunca mover**)
- Código vivo: `Rio Carta Agentes/root`, `Global South News/root`, `Cicero Agentes/root`, `aiatolah/`, `Projeto Cafezinho Agentes/{root,Foruns,scripts,agents_labs,agent_data,dados_baleia_azul,...}`
- `scratch/` (só scripts de cron) | `Outros/Jornais do dia/` (staging: `jornaisdodia.sh` + log; cron 10:30/12:00 segue ativo)

## C) Movidos na reforma ANTERIOR (17/07) — referência cruzada

- `Projeto Cafezinho Agentes/Legacy20260610` → `~/legacy/cafezinho_Legacy20260610_20260717/` (5,3G) — **cron do Painel CCTV apontava aqui; desativado em 22/07**
- Demais legados 17/07: `~/legacy/` (11G total; ver `legacy/BACKUP_DRIVE_20260717`)

## D) Mecanismo do backup (7 noites)

- Script: `~/bin/backup_semana_gdrive.sh` | Cron: `0 3 * * *` | Cota ~17 GiB/noite | Estado: `~/log/backup_semana_estado.txt` | Log: `~/log/backup_semana_gdrive.log`
- Idempotente: pula arquivos idênticos já no GD. Item só vira DONE após `rclone check`.
- **Se algo voltar do DF para o WS (ou algo novo for ao DF):** atualizar a FILA no script e este índice. A reforma está EM ANDAMENTO.

## E) Regra de uso deste índice

1. Arquivo não está no WS? → procure na coluna "Onde está agora".
2. Achar em DF → está na fila de backup; após upload+check, existirá só no GD.
3. Não está nem em WS nem em DF → verificar `~/legacy/` (reforma 17/07) ou `gdrive:backup 20260717` (snapshot de 47,5G).
4. Nunca copiar de volta sem avisar: o destino final é o Drive; volta ao WS exige atualizar FILA do script + este índice.

---

## ERRATA 2026-07-22 (ZCode/Kimi): sites-v4 NÃO é dado frio

`Projeto Cafezinho Agentes/sites-v4` foi movido pela reforma, mas é **dado quente de produção**: é o working copy dos 8 repos `*-v4` de onde os agentes V4 publicam 4×/dia (cron 3h/13h + youtube 2:30/12:30). Foi **re-clonado do GitHub** de volta ao workspace (todos os commits íntegros, zero perda).

Ações de reconciliação executadas:
1. `sites-v4` **removido da fila** de `~/bin/backup_semana_gdrive.sh` (backup do script em `.bak_20260722`); `legacy_reformado_20260717` e `sites-tematicos` seguem na fila normalmente.
2. Cópia redundante em `~/Dados_Frios/Projeto Cafezinho Agentes/sites-v4` (1,9G, idêntica ao clone) **removida**.
3. `sites-v4` permanece no workspace como caminho canônico (`repository.local_path` dos configs).

---

## 🔁 Devoluções ao workspace (2026-07-22, ZCode a pedido do Miguel)

Quatro crons de produção (9h15 ceara-digital, 9h30 gsn, 9h45 cafezinho, 10h cicero) quebrariam na manhã de 23/07 porque suas pastas tinham ido para `~/Dados_Frios/`. Com aprovação do Miguel:

1. `Projeto Cafezinho Agentes/sites-tematicos` (3,5G) → de volta ao workspace (manteve os 10 subprojetos: ceara-digital, gsn, cafezinho, trilhos, riocarta etc.)
2. `Cicero Agentes/cicero` (735M) → de volta ao workspace
3. `sites-v4` (1,9G) **permanece** em Dados_Frios (nenhum cron usa)
4. Fila de `~/bin/backup_semana_gdrive.sh` atualizada (2 entradas removidas, backup `.bak_zcode_20260722`); os demais itens seguem a programação das 7 madrugadas (03:00)
