# 🗺️ MAPA GERAL DE ARQUIVOS E BACKUPS — 2026-08-05 (CÓPIA CANÔNICA NO CÉREBRO)

> **Este arquivo é a referência canônica do Cérebro para "onde está cada arquivo e onde está cada backup".**
> Levantamento completo: **Local (NVMe 460G)** × **Google Drive** × **Backblaze B2**.
> Gerado por Kimi K3/ZCode (2026-08-05) a pedido do Miguel. Cópia de trabalho original: `ZCodeProject/MAPA_BACKUPS_20260805.md`.
> Registrado na Camada 2 em `CEREBRO_NODE_BACKUPS_BACKBLAZE.md` (§ 🗺️ Mapa Geral) e na linha do tempo `CEREBRO_NODE_ATUALIZACOES.md`.
> Operação viva derivada deste mapa: **BACKUP TOTAL 100%** — plano `Cerebro/backup_total_2026/PLANO_BACKUP_TOTAL_100.md`, estado `ESTADO.md`, memória `Cerebro/Memorias/memoria_backup_total_2026.md`, fórum `Cerebro/Foruns/forum_backup_total_2026.md`.

## 🧭 ONDE ESTÁ CADA COISA (resposta rápida)

| O quê | Local | Google Drive | Backblaze B2 |
|---|---|---|---|
| Dossiê Orlando Diniz (incl. PDF Lawfare 61G) | `Dados_Frios/orlando diniz` (65G) | `drive:orlando diniz` (64,3G) ✔ | parcial: `Orlando-Diniz-Dossie` (434M, sem Lawfare) + `mayra-brain/Orlando_Diniz_BKP` (431M) |
| Jornais do dia (PDFs) | `Dados_Frios/Jornais do dia` (6,1G) + `Outros/Jornais do dia` (2,7G) | `drive:Jornais do dia` (27,5G — SUPERSET) ✔ | — |
| Dados frios (projetos encerrados) | `Dados_Frios/` (110G) | `drive:Dados_Frios` (~47G, espelho 24-28/jul) ✔ | — |
| Snapshot workspace congelado 17/jul | — | `drive:backup 20260717` (47,5G) ✔ | — |
| Workspace vivo "Antigravity Google" | `Downloads/Antigravity Google/` (52G) | espelhos parciais (pautas, novo livro, Cerebro_Backups) + **`drive:Workspace_Vivo/` (em construção — BACKUP TOTAL)** | `backup-git-antigravity-20260620` (só metadados, 963B) |
| Pautas editoriais Cafezinho | `Outros/pautas editoriais o cafezinho` (14G) | `drive:pautas editoriais o cafezinho` ✔ (top-up C01 concluído 05/ago) | — |
| Novo livro | `Outros/novo livro` (2,5G) | `drive:novo livro` (2,5G, vivo) ✔ | — |
| Cérebro Imortal (canônico) | `Downloads/Antigravity Google/Cerebro/` (163M) | `drive:Cérebro Imortal da Trindade` + `drive:Cerebro_Backups/Cerebro_completo_20260723` ✔ | `Cerebro-Memorias` (282M) ✔ |
| cerebro-miguel (V3) | `~/cerebro-miguel` (358M) | `drive:Cérebro Imortal da Trindade/cerebro-miguel` ✔ | `Cerebro-Memorias/cerebro-miguel` ✔ |
| Livros | `Dados_Frios/livros baixados novos` (3,6G) | `drive:Dados_Frios/livros baixados novos` ✔ | `Backup-GoogleDrive-Miguel/Livros` (37,2G) ✔ |
| Servidor Cafezinho (produção) | — (servidor us65/NYC) | — | `failover-cafezinho1` (535G) ✔ |
| Imagens WP pré-otimização (Camada 3) | purgado do prod 07/jul | — | `cafezinho-backups/camada3_20260628` (4,6G) ✔ |
| Legacy reforma Cafezinho | `~/legacy/` (11G) | `drive:Backup_Total/legacy` (C05 — BACKUP TOTAL em andamento) | `Legacy-Cafezinho/workspace-limpeza/2026-06-10` (6,7G, parcial) |
| ZCodeProject (igot, carnes, cacai…) | `~/ZCodeProject` (1,1G) | `drive:Backup_Total/ZCodeProject` (C02 — em andamento) | — |
| Recordings (áudios/transcrições) | `~/Recordings` (591M) | `drive:Backup_Total/Recordings` (C03 — pendente) | — |
| ferramentas (buscador/hive/sentinela) | `~/ferramentas` (176M) | `drive:Backup_Total/ferramentas` (C04 — pendente) | — |
| Segredos/chaves | Cofre canônico (ver `CEREBRO_NODE_COFRE_CHAVES.md`) | **NUNCA** | **NUNCA** |

---

## 📊 RESUMO EXECUTIVO

| Camada | Volume | Situação |
|---|---|---|
| 💻 **Disco local** | 295G usados / 460G (68%) | ~142G livres |
| ☁️ **Google Drive** | ~200G medidos (16 pastas raiz); 600G usados de **30 TiB** (29,3 TiB livres) | Principal espelho de dados pessoais |
| 🪣 **Backblaze B2** | ~660G em 16 buckets | Principal: failover do servidor Cafezinho (535G) |

---

## 💻 1. MAPA LOCAL (`/home/migueldorosario`)

### Dados pessoais/projetos

| Pasta | Tamanho | Tem backup? |
|---|---|---|
| `Dados_Frios/` | **110G** | ✅ SIM — espelhado no Drive |
| `Downloads/Antigravity Google/` (workspace) | **52G** | ⚠️ PARCIAL → sendo coberto pelo BACKUP TOTAL (`drive:Workspace_Vivo/`) |
| `legacy/` | 11G | ⚠️ PARCIAL — B2 `Legacy-Cafezinho` (6,7G); chunk C05 cobre o resto |
| `ZCodeProject/` | 1,1G | 🔄 C02 em andamento → `drive:Backup_Total/ZCodeProject` |
| `Recordings/` | 591M | 🔄 C03 → `drive:Backup_Total/Recordings` |
| `cerebro-miguel/` | 358M | ✅ SIM — B2 `Cerebro-Memorias` + Drive `Cérebro Imortal` |
| `ferramentas/` | 176M | 🔄 C04 → `drive:Backup_Total/ferramentas` |
| `backups_livro/`, `mokawriter/` | ~350K | 🔄 C04 (junto) |
| `cofre_intake/`, `gcloud_indexing_keys/` | ~40K | ❌ NUNCA sobe — rito do Cofre de Chaves |

### Detalhe: workspace `Antigravity Google` (52G)

| Subpasta | Tamanho | Backup |
|---|---|---|
| `Outros/` | 22G | ✅ pautas (14G) ✔ C01, Jornais (2,7G — superset na raiz), novo livro (2,5G) ✔; resto → C13 `Workspace_Vivo/Outros` |
| `Projeto Cafezinho Agentes/` | 6,0G | 🔄 C06 → `Workspace_Vivo/` |
| `Cicero Agentes/` | 960M | 🔄 C10 → `Workspace_Vivo/` (+ snapshot 17/jul) |
| `moka/` | 615M | ✅ Drive `Cerebro_Backups/moka` (614M) + C12 → `Workspace_Vivo/` |
| `scratch/` | 296M | ✅ Drive Dados_Frios/scratch (2,1G superset) + C14 |
| `aiatolah/` | 274M | 🔄 C09 → `Workspace_Vivo/` |
| `Rio Carta Agentes/` | 228M | ✅ Drive Dados_Frios (10,8G superset) + C14 |
| `Global South News/` | 226M | ✅ Drive Dados_Frios (1,8G superset) + C14 |
| `Revista Maquiavel/` | 176M | 🔄 C08 → `Workspace_Vivo/` |
| `casadamoeda/` + `casadamoeda-lab/` + backups | ~650M | 🔄 C07 → `Workspace_Vivo/` |
| `Cerebro/` | 163M | ✅ 3 espelhos (Drive ×2 + B2) + C11 → `Workspace_Vivo/` |
| `claude-desktop_amd64.deb` | 159M | 🗑️ instalador — dispensável |

### Lixo/Descartável local (NÃO precisa backup — pode limpar)

| Item | Tamanho | Por quê |
|---|---|---|
| `.deepseek/snapshots/` | **22G** | pesos de modelo LLM — rebaixável |
| `.cache/` | 10G | cache do sistema |
| `.gemini/`, `.grok/`, `.codex/`, `.kimi*` etc. | ~12G | caches/históricos de CLIs de IA |
| `.config/`, `.local/`, `.pyenv/`, `.npm/`, `.nvm/`, `.rustup/`, `.cargo/` | ~36G | tooling regenerável — ⚠️ EXCETO `~/.config/rclone/rclone.conf` (chaves — já no Cofre) |
| `snap/` | 888M | pacotes snap |

---

## ☁️ 2. MAPA GOOGLE DRIVE (`drive:` = `gdrive:`, mesma conta; 30 TiB plano)

| Pasta raiz | Tamanho | Conteúdo |
|---|---|---|
| `orlando diniz` | **64,3G** | Dossiê Orlando completo — inclui PDF Lawfare29 de 61G + vídeos |
| `backup 20260717` | **47,5G** | Snapshot congelado do workspace de 17/jul (33,7 mil arqs) |
| `Dados_Frios` | **~46,7G** | Espelho do Dados_Frios local |
| `Jornais do dia` | **27,5G** | PDFs de jornais — superset do local |
| `pautas editoriais o cafezinho` | **14,2G** | ✔ top-up C01 (05/ago) — agora inclui 19/jul→05/ago |
| `novo livro` | 2,5G | Livro novo (ativo — 05/ago) |
| `Cerebro_Backups` | 1,2G | Cerebro_completo_20260723, moka, ARQUITETURA_MOKA |
| `Projeto Casa da Moeda` | 255M | apresentações/pesquisas |
| `Cérebro Imortal da Trindade` | 216M | cerebro-miguel |
| `ReadEra` | 181M | ebooks/leitura |
| `Artigos Casa da Moeda` | 17M | artigos |
| **`Workspace_Vivo/`** | 🔄 em construção (BACKUP TOTAL C06–C14) | espelho vivo do workspace pós-17/jul |
| **`Backup_Total/`** | 🔄 em construção (BACKUP TOTAL C02–C05) | ZCodeProject, Recordings, ferramentas, legacy, miúdos |
| `Arquivos a organizar` | ⚠️ não medido (milhares de arqs, 2023→2026) | caixa de entrada antiga — auditar depois |
| `Arquivos organizados`, `Subcérebro AGY`, `Notas Play Livros` | ~0 | vazios/atalhos |
| `Foruns — O Foragido` | 13K | 2 arquivos |

## 🪣 3. MAPA BACKBLAZE B2 (conta-mãe: `gdrive-backup-b2:`)

| Bucket | Tamanho | Conteúdo |
|---|---|---|
| `failover-cafezinho1` | **535G** | réplica failover NYC do servidor Cafezinho |
| `Backup-GoogleDrive-Miguel` | 37,2G | Livros (2.659 arqs) |
| `mayra-brain` | 25,7G | LTM Mayra + Orlando_Diniz_BKP parcial + Antigravity_Google/backups |
| `Legacy-Miguel` | 14,1G | tarballs (cingapura, cafezinho manual 2026-04, mayra whatsapp) |
| `Legacy-Cafezinho` | 8,8G | workspace-limpeza/2026-06-10 (6,7G) + tencent-root-backups |
| `cafezinho-backups` | 4,6G | camada3_20260628 (11.324 imagens WP pré-otimização) |
| `reforma-tencent-cafezinho` | 2,5G | reforma Tencent jun/2026 |
| `Agents-Labs-Cafezinho` | 1,6G | labs |
| `Cafezinho-pos-grande-reforma-jun2026` | 1,4G | pós-reforma |
| `Orlando-Diniz-Dossie` | 434M | dossiê (sem Lawfare29 — esse está no Drive) |
| `Cerebro-Memorias` | 282M | cerebro-miguel + snapshots |
| `site-tematicos` | 244M | sites temáticos |
| `Cafezinho-operacional` | 125K | quase vazio |
| `backup-git-antigravity-20260620` | 963B | praticamente vazio |
| `bancodemidiageral`, `processador-imagens-cafezinho` | 0 | 🗑️ vazios (candidatos a apagar) |

---

## 🔀 4. MATRIZ Dados_Frios local × Drive (verificado 05/ago)

| Subpasta | Local | Drive | Status |
|---|---|---|---|
| orlando diniz | 65G | 64,3G (raiz própria) | ✅ |
| Rio Carta Agentes | 11G | 10,8G | ✅ |
| Backups_workspace | 9,2G | 17,1G | ✅ Drive tem MAIS |
| Jornais do dia | 6,1G | 27,5G (raiz) | ✅ Drive tem MUITO mais |
| Agentes Labs | 5,0G | 4,7G | ✅ |
| livros baixados novos | 3,6G | 3,6G | ✅ |
| Bella Cia Project | 2,3G | 2,3G | ✅ |
| scratch | 2,2G | 2,1G | ✅ |
| mapario | 2,2G | 2,2G | ✅ |
| Global South News | 1,9G | 1,8G | ✅ |
| Outros_docs | 567M | 971M | ✅ |
| Projeto Cafezinho Agentes | 726M | 697M | ✅ |
| Backups_outros | 561M | 576M | ✅ |
| zip Dossiê Orlando + ebooks novos | ~366M | — | 🔄 C15 cobre |

---

## 🚨 5. BURACOS DE BACKUP (sendo fechados pelo BACKUP TOTAL 100% — ver ESTADO.md)

1. ~~Pautas 19/jul→hoje~~ → ✅ fechado (C01, 05/ago 13:35)
2. ZCodeProject (1,1G) → 🔄 C02
3. Recordings (591M) → 🔄 C03
4. ferramentas + miúdos home (177M) → 🔄 C04
5. legacy/ (11G) → 🔄 C05
6. Workspace vivo pós-17/jul (PCAgentes, casadamoeda*, Maquiavel, aiatolah, Cicero, moka, Outros-resto, miúdos) → 🔄 C06–C14
7. Dados_Frios top-up (zip dossiê, ebooks) → 🔄 C15
8. `Arquivos a organizar` (Drive) — única pasta nunca auditada (fica para depois da FASE 1)

## 🧹 6. LIMPEZA LOCAL (SÓ DEPOIS da tag `[BACKUP-TOTAL-100-FASE1-DRIVE-CONCLUIDA]` + FASE 2 B2)

| # | Ação | Libera |
|---|---|---|
| 1 | `.deepseek/snapshots` | 22G |
| 2 | caches sistema + CLIs IA | ~15-20G |
| 3 | Lawfare29 local (já no Drive — verificar sha1 antes) | 61G |
| 4 | `Dados_Frios` inteiro (após FASE 1+2) | 110G |
| **Total potencial** | | **~200G+** |

---

## 📝 Notas

- Remotes rclone: `drive:` ≡ `gdrive:` (mesma conta). Demais remotes B2 são app-keys restritas a buckets da conta-mãe `gdrive-backup-b2:`.
- Nenhum segredo exposto (apenas estrutura/tamanhos).
- Método: `rclone lsd/size/lsf` + `du/find`. Google Docs nativos têm tamanho desconhecido (subestimam totais).
