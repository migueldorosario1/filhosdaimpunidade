# 📋 ESTADO — BACKUP TOTAL 100% (FASE 1: Google Drive)

> Máquina de estados dos chunks. Regras no `PLANO_BACKUP_TOTAL_100.md` §3.
> Status possíveis: `PENDENTE` · `EM_ANDAMENTO` · `CONCLUÍDO` · `REVISAR`
> `EM_ANDAMENTO` com >75 min sem atualização = travado → qualquer agente pode reassumir.
> **Atualizado por último:** Kimi (ZCode) — 2026-08-11 14:21 BRT — 🏆 FASE 1 = 100% (16/16) · **🏆 FASE 2 (B2) = 100% (16/16) — BACKUP-TOTAL-100% COMPLETO NAS DUAS NUVENS** — B2-01 ✔ (710=710 obj / 13,6 GiB) · B2-02 ✔ (3.695=3.695; 10 B churn) · B2-03 ✔ (2.157=2.157 byte-exact) · B2-04 ✔ (3 origens byte-exact) · B2-05 ✔ (53.984=53.984 obj / 9,74 GiB) · B2-06 ✔ (26.051=26.051 obj / 4,80 GiB) · B2-07 ✔ (4 origens byte-exact, 1.968 obj / 521 MiB) · B2-08 ✔ (267=267 obj / 1,4 MiB) · B2-09 ✔ (5.876=5.876 obj / 134,7 MiB) · B2-10 ✔ (6.373=6.373 obj / 684,8 MiB) · B2-11 ✔ (4.319/4.320 obj; diff 1 = log vivo, top-up B2-16) · B2-12 ✔ (23=23 obj / 614,5 MiB) · B2-13 ✔ (6.127=6.127 obj / 1,23 GiB) · B2-14 ✔ (20 pastas rc=0; 18/20 byte-exact, 2 diffs churn vivo → top-up B2-16) · **B2-15 (Dados_Frios ~40 G + novo livro): novo livro ✔; Dados_Frios J10 no ar desde 17:11** · destino `gdrive-backup-b2:backup-total-local-2026/`

| ID | Status | Agente | Timestamp | Verificação / nota |
|---|---|---|---|---|
| C01 | CONCLUÍDO | kimi-zcode-cron | 2026-08-05 13:35 | ✔ exit 0; local 13,57 GiB ⊂ Drive 14,23 GiB (Drive superset); upload real ~1,26 GiB |
| C02 | CONCLUÍDO | kimi-zcode (vai2) | 2026-08-05 18:55 | ✔ exit 0; 6 janelas (~50min); ~2.800 arqs; Drive ≈ local 400 MiB (menos exclusões node_modules/.next) |
| C03 | CONCLUÍDO | kimi-zcode (vai3) | 2026-08-05 19:15 | ✔ exit 0; 2 janelas; ~730 MiB, ~1.900 arqs (pasta viva — top-up futuro é barato: rclone só copia clips novos) |
| C04 | CONCLUÍDO | kimi-zcode (vai4) | 2026-08-05 22:50 | ✔ exit 0; 3 janelas; ferramentas 172 MiB + backups_livro + mokawriter (diferenças mínimas = __pycache__ excluído) |
| C05 | CONCLUÍDO | kimi-zcode | 2026-08-07 04:05 | ✔ janela 34 exit 0 (03:49→04:14 fechou antes); `rclone size` local == Drive: **53.984 obj / 9,741 GiB (10.459.828.576 B) byte-exact** |
| C06 | CONCLUÍDO | kimi-zcode | 2026-08-07 19:06 | ✔ **diff decisivo 19:05: FALTANDO = 0** (local 25.588 arqs ⊂ Drive 25.820 obj). Tática cirúrgica: S1–S9, ~2.050 cópias desde 15:41 (janelas full-tree haviam parado às 14:28); lições no fórum/memória |
| C07 | CONCLUÍDO | kimi-zcode | 2026-08-07 19:58 | ✔ J3 EXIT=0 (J1/J2 EXIT=124 normais — DirSetModTime da árvore de slides comia o fim das janelas). Verificado: casadamoeda 830=830, lab 807=807, estavel 330=330 arqs; tar.gz byte-exact 136.266.629 B na raiz |
| C08 | CONCLUÍDO | kimi-zcode | 2026-08-07 20:29 | ✔ J2 EXIT=0 em ~5 min (só 475 KiB restantes após a morte silenciosa da J1 ~20:08 — ver BUG-20260807-JANELAS-BACKUP-MORTE-SILENCIOSA). Verificado: 267=267 arqs |
| C09 | CONCLUÍDO | kimi-zcode | 2026-08-07 21:40 | ✔ J3 EXIT=0 (J1/J2 124 atravessaram o .git gigante). Verificado: 5.876=5.876 arqs |
| C10 | CONCLUÍDO | kimi-zcode | 2026-08-08 00:24 | ✔ **O maior chunk da FASE 1** (960 MB): 6 janelas (J1–J5 124; J5 revelou transfers 100% completos — morte na finalização DirSetModTime); verificação direta 00:24: **6.373=6.373 arqs**. J6 check-only sofreu a 4ª morte silenciosa (23:54) |
| C11 | CONCLUÍDO | kimi-zcode | 2026-08-08 04:22 | ✔ 4 janelas (J1 124; J2–J4 EXIT=1 inofensivos de pasta viva). Verificação fina 04:22: **4.099/4.106 copiados (99,8%)** — os 7 faltantes são todos arquivos sendo escritos AGORA (4 JSONs vigília_v5, o próprio `C11.log`, fórum+memória diretrizes CEO v4 de outra sessão); top-up final fica no C16 (pasta viva, como C03) |
| C12 | CONCLUÍDO | kimi-zcode | 2026-08-08 05:22 | ✔ **1 janela só!** (04:22→04:41, EXIT=0, 1,46 GiB a 3,2 MiB/s); verificação exata **23=23 arqs** (poucos arquivos grandes) |
| C13 | CONCLUÍDO | kimi-zcode | 2026-08-08 09:22 | ✔ J5 EXIT=0 (08:53→09:18) após J1–J4 124 (zips Moka/backups → JSONs do `link_cache` → `.git` do Moka-Lab); verificação exata **5.989=5.989 arqs** (com as 3 exclusões do plano) |
| C14 | CONCLUÍDO | kimi-zcode | 2026-08-08 11:24 | ✔ Verificação exata **3.306=3.306 arqs** nas 20 pastas (zero divergências). Histórico: J1 (09:23) sofreu a 5ª morte silenciosa ~10:40 (1ª de janela setsid — hipótese de sessão REFUTADA, dossiê ao Miguel); **J2 (10:55, script `logs/C14_loop_j2.sh` com heartbeat) EXIT=0 11:14** — todas as 20 pastas rc=0. Resto do workspace (~1,5 G): 20 pastas, 1 comando por pasta em sequência na mesma janela (`scratch`, Rio Carta Agentes, GSN, Kimi K3, Fontes, agent_data, agentes_tematicos, artes, backups_ceo_cerebro, github_work, artifacts, Foruns, Claude, api, backups, deploy_build, reportagens_para_fazer_depois, transcritor, teste_foto..., tmp_v3_remote). **Janela 1 (09:23) sofreu a 5ª morte silenciosa** entre 10:40:45 (última linha do log, pasta 9 backups_ceo_cerebro) e 10:52 — PID 202816 sumiu sem EXIT, sem OOM (earlyoom 40% livre), sem outra sessão ativa → hipótese de sessão REFUTADA (morte veio com a sessão viva). **Janela 2 destacada 10:55** via script `logs/C14_loop_j2.sh` com heartbeat por pasta (EXIT/andamento em `logs/C14.j2.stdout`; idempotente — rclone pula o já copiado; pasta inexistente = PULADO) |
| C15 | CONCLUÍDO | kimi-zcode | 2026-08-08 17:27 | `Dados_Frios` → `drive:Dados_Frios` (exclusões do plano: `orlando diniz/**` 65 G + `Jornais do dia/**` 6,1 G → ficam de fora; resto = **40 G**) + `$WS/Outros/novo livro` (2,5 G) → `drive:novo livro`. **J1 (11:25):** `novo livro` **rc=0 completo** ✔; `Dados_Frios` rc=124 (comeu a janela de 25 min — esperado, 40 G). **J2 (11:53) e J3 (12:23):** Dados_Frios rc=124 em ambas (janelas de 25 min normais). **J4 (12:53):** rc=124 (4ª janela de 25 min). **J5 (13:23):** rc=124 (5ª janela de 25 min). **J6 (13:53):** rc=124 (6ª janela de 25 min). **J7 (14:23):** rc=124 (7ª janela de 25 min). **J8 (14:52):** rc=124 (8ª janela de 25 min). **J9 (15:22):** rc=124 (9ª janela de 25 min). **J10 (15:52):** rc=124. **Diagnóstico 16:22:** o chunk está praticamente PRONTO — só 5 "Copied (new)" no dia, stats em 0 B/s e massa de "Duplicate directory/object found in destination - ignoring"; o que não cabe em 25 min é o ENUMERATE/CHECK da árvore de **159.160 arquivos** (1.421 no cache `.npm/_cacache`). J11 (16:23) foi morta como troca de tática. **Janela LONGA (2h) destacada 16:28** — script `logs/C15_j12_longa.sh`, `timeout 7200`, mesma configuração; heartbeat+EXIT em `logs/C15.j12_longa.stdout` (fim previsto ≤18:28). **✔ FECHAMENTO 17:27:** a janela longa terminou **rc=0 às 16:57** (29 min!) — log: *"There was nothing to transfer"* — confirmando o diagnóstico: a transferência já estava pronta, o gargalo era a enumeração. Correção da contagem: a base correta pós-exclusões é **41.226 arqs** (os 159.160 da ronda 95 incluíam node_modules/__pycache__/.next/.Trash, que o rclone também exclui). Verificação: Dados_Frios local 41.226 ⊂ Drive 163.064 (destino superset — backup antigo retido, copy sem --delete); novo livro 1.271 ⊂ 1.289 (18 legado). Prova decisiva: rc=0 + nothing to transfer |
| C16 | CONCLUÍDO | kimi-zcode | 2026-08-08 21:22 | **Top-up Cerebro fechado** (J1 17:27/J2 17:53, ambas rc=1 inofensivo — única falha foi o próprio `C16.log` sendo escrito durante a cópia, família do churn C11; demais 16,3 MiB copiados). Cerebro local = **4.195 arqs**. **Verificação final disparada 17:56** — script `logs/C16_j3_check.sh`: `rclone check --one-way` em Cerebro, Projeto Cafezinho, novo livro e Outros (com `novo livro/**` excluído do check de Outros — destino próprio em `drive:novo livro`); heartbeat `logs/C16.j3_check.stdout`. Depois: relatório + ping 100% + FASE 2 B2. Nota 17:55: auto-pkill acidental (padrão casou com o próprio shell) — janela substituída sem dano. **✔ FECHAMENTO 21:22:** top-up PC j6 **EXIT=0** (20:01, 16 MiB) + re-check j7 **EXIT=0, ZERO erros** (20:23→20:55) — pasta viva alcançada. Verificação por destino: novoLivro rc=0 direto; Cerebro rc=1→top-up rc=0 (churn documentado); Outros 936 erros decompostos (828 exclusões do plano + 108 churn Moka) → top-up j5 EXIT=0; PC 442 erros (churn pós-C06) → top-up j6 EXIT=0 → re-check limpo. **FASE 1 = 100% 🏆** |

**FASE 2 (Backblaze B2): ✅ AUTORIZADA pelo Miguel em 07/08/2026 ~12:03 ("pode rodar").** Início automático assim que FASE 1 = 100% (regra do plano §2). Bucket `backup-total-local-2026` criado 07/08 12:05 via remote **`gdrive-backup-b2:`** (atenção: a chave do remote `b2:` é presa ao bucket failover-cafezinho1 e não cria bucket). Adendo técnico no PLANO_BACKUP_TOTAL_100.md.

## FASE 2 — chunks B2 (LOCAL → B2 direto, mesmas origens/exclusões da FASE 1, template SEM `--drive-chunk-size`)

| ID | Status | Agente | Timestamp | Verificação / nota |
|---|---|---|---|---|
| B2-01 | CONCLUÍDO | kimi-zcode | 2026-08-08 23:07 | `$WS/Outros/pautas editoriais o cafezinho` → `gdrive-backup-b2:backup-total-local-2026/pautas editoriais o cafezinho`. **J1 (21:23):** rc=124. **J2 (21:53):** rc=124. **Diagnóstico 22:20:** arquivos grandes do Riofilme (mp4/zip >250M) falhando de verdade — `multi-thread copy: failed to write chunk` no `b2_upload_part`. **Correção:** **J3 LONGA (2h) com multi-thread DESLIGADO** (`--multi-thread-cutoff 100G`) desde 22:23. **✔ FECHAMENTO 23:07:** EXIT=0, 10,09 GiB a ~3 MiB/s, mp4 do Riofilme que travava subiu limpo. **Verificação 23:23:** `rclone size` local × B2 **exato: 710=710 objetos / 13,596 GiB (14.598.851.909 B)** (2 symlinks ignorados dos dois lados, consistente) |
| B2-02 | CONCLUÍDO | kimi-zcode | 2026-08-08 23:28 | ZCodeProject → `…/Backup_Total/ZCodeProject`. **J1 fechou EXIT=0 em ~4,5 min** (23:23→23:28, 518 MiB). **Verificação 23:34:** `rclone size` local × B2 = **3.695=3.695 objetos**; bytes 543.654.022×543.654.012 — diff de 10 B = churn de pasta viva (o `.vigilia_claude_state.json` muda a cada ronda; mesmo padrão do C11). Top-up final fica no B2-16 |
| B2-03 | CONCLUÍDO | kimi-zcode | 2026-08-08 23:39 | Recordings → `…/Backup_Total/Recordings`. **J1 única, EXIT=0 23:39** (23:35→23:39, ~4 min, 669 MiB). **Verificação 23:41:** `rclone size` local × B2 = **2.157=2.157 objetos / 702.060.297 B byte-exact** |
| B2-04 | CONCLUÍDO | kimi-zcode | 2026-08-08 23:46 | ferramentas + backups_livro + mokawriter → `…/Backup_Total/…`. **As 3 origens rc=0 em ~1 min** (23:45→23:46). **Verificação 23:48:** `rclone size` local × B2 byte-exact nas 3: ferramentas **1.051=1.051 obj / 180.594.681 B**, backups_livro **1=1 / 96.310 B**, mokawriter **56=56 / 99.682 B**. Incidente (sem dano): lançamento duplo acidental da janela — duplicata morta por PID; heartbeat sem TERMINADO/EXIT por corrida dos dois escritores, dados íntegros (verificação acima é a prova) |
| B2-05 | CONCLUÍDO | kimi-zcode | 2026-08-09 04:24 | legacy → `…/Backup_Total/legacy` (chunk do Claude na FASE 1 — na FASE 2 segue a ordem normal). Histórico: **J1–J4 rc=124 normais** (23:49→00:14 / 01:23→01:48 / 02:23→02:48 / 03:23→03:48). **J5: EXIT=0** (04:11→04:17, restavam só 136 MiB). **✔ Verificação 04:23:** `rclone size` local × B2 **exato: 53.984=53.984 objetos / 10.459.828.576 B (9,74 GiB) byte-exact** (14 symlinks ignorados dos dois lados, consistente). Obs: hiato 03:48→04:11 sem janela (sessão atendeu chamado do Miguel — crise imagens V4) |
| B2-06 | CONCLUÍDO | kimi-zcode | 2026-08-09 05:40 | Projeto Cafezinho Agentes → `…/Workspace_Vivo/Projeto Cafezinho Agentes`. Histórico: **J1: rc=124 normal** (04:25→04:50); **J2: EXIT=0** (05:23→05:34, ~11 min). **✔ Verificação 05:40:** `rclone size` local × B2 **exato: 26.051=26.051 objetos / 5.150.361.198 B (4,80 GiB) byte-exact** (1 symlink ignorado dos dois lados; pasta viva mas churn zero na medição) |
| B2-07 | CONCLUÍDO | kimi-zcode | 2026-08-09 06:23 | casadamoeda×4 (173M+173M+76M+130M ≈ 552M) → `…/Workspace_Vivo/…` mesmos nomes; tar.gz na raiz de `Workspace_Vivo/`. **J1 única: EXIT=0 em 3 min** (05:41→05:44, 4 origens rc=0). **✔ Verificação 06:23:** `rclone size` local × B2 **byte-exact nas 4**: casadamoeda **830=830 obj / 177.790.573 B**, casadamoeda-lab **807=807 / 177.772.035 B**, estavel **330=330 / 78.468.002 B**, tar.gz **1=1 / 136.266.629 B** |
| B2-08 | CONCLUÍDO | kimi-zcode | 2026-08-09 07:23 | Revista Maquiavel → `…/Workspace_Vivo/Revista Maquiavel`. **J1 única: EXIT=0 em 14 s** (06:24:13→06:24:27) — a pasta era ~1,4 MiB (não ~176M como estimado no plano). **✔ Verificação 07:23:** `rclone size` local × B2 **byte-exact: 267=267 obj / 1.495.762 B** |
| B2-09 | CONCLUÍDO | kimi-zcode | 2026-08-09 08:24 | aiatolah → `…/Workspace_Vivo/aiatolah`. **J1 única: EXIT=0 em ~3,5 min** (07:23:53→07:27:29) — pasta era ~135 MiB (não ~274 M como estimado). **✔ Verificação 08:23:** `rclone size` local × B2 **byte-exact: 5.876=5.876 obj / 141.240.974 B** |
| B2-10 | CONCLUÍDO | kimi-zcode | 2026-08-09 08:53 | Cicero Agentes → `…/Workspace_Vivo/Cicero Agentes`. **J1 única: EXIT=0 em ~5 min** (08:24:05→08:29:07, ~685 MiB — menor que os ~960 M estimados). **✔ Verificação 08:52:** `rclone size` local × B2 **byte-exact: 6.373=6.373 obj / 718.031.463 B** (1 symlink ignorado dos dois lados) |
| B2-11 | CONCLUÍDO | kimi-zcode | 2026-08-09 09:24 | Cerebro (pasta viva) → `…/Workspace_Vivo/Cerebro`. Histórico: **J1 rc=6** (08:53:40→08:56:54, 215 MiB) + **J2 rc=6** (09:23:44→09:24:01) — ambos com **1 único erro = o próprio `backup_total_2026/logs/B2-11.log` em churn** ("source file is being updated"; família do churn C11/C16/B2-02). **✔ Verificação 09:24:** local **4.320 obj / 225.728.225 B** × B2 **4.319 obj / 225.094.460 B** — diff de 1 obj/634 KB = exatamente o log vivo; top-up no B2-16. Symlinks dos Backups ignorados dos dois lados (consistente) |
| B2-12 | CONCLUÍDO | kimi-zcode | 2026-08-09 09:53 | moka → `…/Workspace_Vivo/moka`. **J1 única: EXIT=0 em ~3 min** (09:25:49→09:29:05, ~615 MiB). **✔ Verificação 09:52:** `rclone size` local × B2 **byte-exact: 23=23 obj / 644.397.089 B** (poucos arquivos grandes) |
| B2-13 | CONCLUÍDO | kimi-zcode | 2026-08-09 10:23 | Outros (3 exclusões do plano: `pautas editoriais o cafezinho/**` [já em B2-01 na raiz], `Jornais do dia/**`, `novo livro/**` [fica no B2-15]) → `…/Workspace_Vivo/Outros`. **J1 única: EXIT=0 em ~9,5 min** (09:54:09→10:03:42). **✔ Verificação 10:22:** `rclone size` local × B2 **byte-exact: 6.127=6.127 obj / 1.317.629.481 B (1,23 GiB)** |
| B2-14 | CONCLUÍDO | kimi-zcode | 2026-08-09 10:54 | resto do workspace — mesmas 20 pastas do C14 → `…/Workspace_Vivo/<pasta>`. **J1 única: EXIT=0 em 15,5 min** (10:24:46→10:40:17, 20/20 pastas rc=0). **✔ Verificação 10:53 (rclone size por pasta): 18/20 byte-exact**; 2 diffs de churn de pasta viva: **scratch** 1.289×1.283 obj (6 obj/14 MB novos após a janela — pasta viva, família C11) e **agent_data** 1.083×1.082 obj (1 obj/2,2 MB = banco do agente de imagens sendo escrito pelo cron */30). Top-up no B2-16 |
| B2-15 | CONCLUÍDO | kimi-zcode | 2026-08-11 13:28 | Dados_Frios (**~35,3 GiB** pós-exclusões; origem real = **`/home/migueldorosario/Dados_Frios`** no HOME) → `…/Dados_Frios` + novo livro (~2,5 G) → `…/novo livro`. Histórico: **J1 (10:55 09/08):** Dados_Frios rc=3 (caminho errado); novo livro rc=0. **J2–J10 (09/08):** Dados_Frios rc=124 normais. **Hiato 36h** (09/08 13:52 → 11/08 05:06): vigília morta por bug `thought_level`. **J11–J23 (11/08):** rc=124 normais; J23 monstruosa (+19,2 GiB, +26.968 arqs — enumeração alcançou diretório pesado). **J24 (13:23→13:27): EXIT=0 em 4,5 min** ("nothing to transfer"). **✔ Verificação 13:52: local 41.218 obj / 37.927.332.691 B × B2 41.218 obj / 37.927.332.691 B — BYTE-EXACT** | Dados_Frios (**~40 G** pós-exclusões: `orlando diniz/**` 65 G + `Jornais do dia/**` 6,1 G de fora; origem real = **`/home/migueldorosario/Dados_Frios`** no HOME, fora do workspace) → `…/Dados_Frios` + novo livro (~2,5 G, `$WS/Outros/novo livro`) → `…/novo livro`. **J1 (10:55→11:06):** Dados_Frios **rc=3** em 2 s (caminho errado no script); **novo livro rc=0** (11:06:12, ~11 min, ~2,5 G) ✔ FECHADO (reconfirmado rc=0 na J2). **J2 (11:23→11:48):** Dados_Frios **rc=124 normal** (janela cheia de 25 min). **J3–J13 rc=124 normais** (J13 06:24→06:49 de 11/08). **J14 no ar desde 11/08 06:53:11** (`B2-15_j14.sh`, só Dados_Frios — novo livro já fechado; heartbeat `logs/B2-15.j14.stdout`; rc=124 normal até acabar) |
| B2-16 | CONCLUÍDO | kimi-zcode | 2026-08-11 14:21 | verificação final + top-ups churn. **J1 única: EXIT=0 em ~2,5 min** (14:18:32→14:21:05). Top-ups: ZCodeProject rc=0, Cerebro rc=0, scratch rc=0, agent_data rc=0. **✔ Verificação 14:21:** ZCodeProject **byte-exact** (808.967.161=808.967.161 B), scratch **byte-exact** (534.659.085=534.659.085 B), agent_data **byte-exact** (2.084.803.570=2.084.803.570 B); Cerebro diff 121.100 B (270.312.461×270.191.361) = logs vivos sendo escritos (churn família C11/C16, inofensivo). **🏆 FASE 2 = 100%** |

### Rodada ACERVO-100 de 2026-08-17 15:49:20
- B2 bucket total: Total size: 74.000 GiB (79456414835 Byte)

### Rodada ACERVO-100 de 2026-08-18 11:39:41
- B2 bucket total: Total size: 86.169 GiB (92522941241 Byte)
- Drive orlando diniz: Total size: 64.317 GiB (69059744574 Byte)

### Rodada ACERVO-100 de 2026-08-19 08:00:13
- B2 bucket total: Total size: 86.259 GiB (92620000461 Byte)
- Drive orlando diniz: Total size: 64.317 GiB (69059744574 Byte)

### 2026-08-19 20:21 — Correção orlando diniz→B2 (cutoff hard→soft) + janela dedicada
- **Causa-raiz do atraso:** PDF único de 60,02 GiB (`doc lawfare oab/Lawfare29/Anexo 2 RELATO81RIO...pdf`) nunca completava com o teto `--max-transfer 17G --cutoff-mode hard` (rclone não retoma multipart entre processos; 2 madrugadas de 17 GiB viraram partes órfãs — limpas com `rclone cleanup`, rc=0).
- **Fix:** `CAP` do script alterado para `--cutoff-mode soft` (para de iniciar novos arquivos no teto, mas COMPLETA o arquivo em curso). Backup: `bin/backup_acervo_100_b2_drive.sh.bak_pre_cutoff_soft_20260819`.
- **Janela dedicada no ar desde 20:21** (flock /tmp/acervo100.lock; cron 04:30 pula se ela seguir rodando): orlando diniz → B2 sem teto, ~60 GiB restantes, previsão ~5-6h. Estado anterior: B2 tinha 4,3/65 GiB; Drive já estava 100% (64,3 GiB rc=0 diário).
- **Situação geral:** Drive = 100% de tudo. B2 = 100% de tudo EXCETO orlando diniz (em fechamento nesta janela).

### 2026-08-19 21:18 — 🏆 ACERVO-100 = 100% NOS DOIS DESTINOS (orlando diniz FECHADO)
- Janela dedicada (20:21→21:18, 57 min, ~18 MiB/s) fechou o orlando diniz no B2 com rc=0.
- **✔ Verificação byte-exact 22:02: local × B2 = 424=424 objetos / 64,317 GiB (69.059.744.574 B) — idêntico.**
- Quadro final: **Google Drive = 100% de tudo** · **Backblaze B2 = 100% de tudo** (inclui o PDF de 60 GiB de `doc lawfare oab/Lawfare29/`). Cron 04:30 segue em top-up diário com cutoff soft.

### Rodada ACERVO-100 de 2026-08-20 07:48:31
- B2 bucket total: Total size: 146.452 GiB (157251813954 Byte)
- Drive orlando diniz: Total size: 64.317 GiB (69059744574 Byte)

### Rodada ACERVO-100 de 2026-08-21 06:48:57
- B2 bucket total: Total size: 148.085 GiB (159004785890 Byte)
- Drive orlando diniz: Total size: 64.317 GiB (69059744574 Byte)

### Rodada ACERVO-100 de 2026-08-22 05:17:41
- B2 bucket total: Total size: 148.164 GiB (159090129869 Byte)
- Drive orlando diniz: Total size: 64.317 GiB (69059744574 Byte)

### Rodada ACERVO-100 de 2026-08-23 05:41:26
- B2 bucket total: Total size: 148.189 GiB (159116964482 Byte)
- Drive orlando diniz: Total size: 64.317 GiB (69059744574 Byte)

### Rodada ACERVO-100 de 2026-08-24 05:14:31
- B2 bucket total: Total size: 148.201 GiB (159129440751 Byte)
- Drive orlando diniz: Total size: 64.317 GiB (69059744574 Byte)

### Rodada ACERVO-100 de 2026-08-25 08:12:46
- B2 bucket total: Total size: 162.139 GiB (174095749331 Byte)
- Drive orlando diniz: Total size: 64.317 GiB (69059744574 Byte)

### Rodada ACERVO-100 de 2026-08-26 06:57:52
- B2 bucket total: Total size: 162.187 GiB (174146806827 Byte)
- Drive orlando diniz: Total size: 64.317 GiB (69059744574 Byte)

### Rodada ACERVO-100 de 2026-08-27 05:28:57
- B2 bucket total: Total size: 162.283 GiB (174249953047 Byte)
- Drive orlando diniz: Total size: 64.317 GiB (69059744574 Byte)

### Rodada ACERVO-100 de 2026-08-28 05:56:35
- B2 bucket total: Total size: 170.191 GiB (182741380516 Byte)
- Drive orlando diniz: Total size: 64.317 GiB (69059744574 Byte)

### Rodada ACERVO-100 de 2026-08-29 05:48:56
- B2 bucket total: Total size: 170.224 GiB (182776748664 Byte)
- Drive orlando diniz: Total size: 64.317 GiB (69059744574 Byte)

### Rodada ACERVO-100 de 2026-08-30 05:58:53
- B2 bucket total: Total size: 170.543 GiB (183119078762 Byte)
- Drive orlando diniz: Total size: 64.317 GiB (69059744574 Byte)

### Rodada ACERVO-100 de 2026-08-31 07:09:52
- B2 bucket total: Total size: 177.426 GiB (190510077829 Byte)
- Drive orlando diniz: Total size: 64.317 GiB (69059744574 Byte)

### Rodada ACERVO-100 de 2026-09-01 06:32:04
- B2 bucket total: Total size: 177.688 GiB (190791484282 Byte)
- Drive orlando diniz: Total size: 64.317 GiB (69059744574 Byte)

### Rodada ACERVO-100 de 2026-09-04 06:46:51
- B2 bucket total: Total size: 188.733 GiB (202650039632 Byte)
- Drive orlando diniz: Total size: 64.317 GiB (69059744574 Byte)

### Rodada ACERVO-100 de 2026-09-05 06:46:41
- B2 bucket total: Total size: 190.911 GiB (204988832461 Byte)
- Drive orlando diniz: Total size: 64.317 GiB (69059744574 Byte)

### Rodada ACERVO-100 de 2026-09-06 06:27:55
- B2 bucket total: Total size: 190.944 GiB (205024321431 Byte)
- Drive orlando diniz: Total size: 64.317 GiB (69059744574 Byte)

### Rodada ACERVO-100 de 2026-09-07 06:25:49
- B2 bucket total: Total size: 191.345 GiB (205455037178 Byte)
- Drive orlando diniz: Total size: 64.317 GiB (69059744574 Byte)

### Rodada ACERVO-100 de 2026-09-08 06:07:45
- B2 bucket total: Total size: 191.360 GiB (205471721842 Byte)
- Drive orlando diniz: Total size: 64.317 GiB (69059744574 Byte)

### Rodada ACERVO-100 de 2026-09-09 06:50:13
- B2 bucket total: Total size: 191.684 GiB (205818751300 Byte)
- Drive orlando diniz: Total size: 64.317 GiB (69059744574 Byte)

### Rodada ACERVO-100 de 2026-09-10 06:51:56
- B2 bucket total: Total size: 192.589 GiB (206791014870 Byte)
- Drive orlando diniz: Total size: 64.317 GiB (69059744574 Byte)

### Rodada ACERVO-100 de 2026-09-11 06:50:01
- B2 bucket total: Total size: 192.634 GiB (206838730436 Byte)
- Drive orlando diniz: Total size: 64.317 GiB (69059744574 Byte)

### Rodada ACERVO-100 de 2026-09-13 08:53:45
- B2 bucket total: Total size: 192.918 GiB (207143765069 Byte)
- Drive orlando diniz: Total size: 64.317 GiB (69059744574 Byte)

### Rodada ACERVO-100 de 2026-09-15 07:20:47
- B2 bucket total: Total size: 193.994 GiB (208299990170 Byte)
- Drive orlando diniz: Total size: 64.317 GiB (69059744574 Byte)

### Rodada ACERVO-100 de 2026-09-16 06:36:11
- B2 bucket total: Total size: 194.071 GiB (208381633025 Byte)
- Drive orlando diniz: Total size: 64.317 GiB (69059744574 Byte)

### Rodada ACERVO-100 de 2026-09-17 14:26:40
- B2 bucket total: Total size: 259.087 GiB (278192658609 Byte)
- Drive orlando diniz: Total size: 64.317 GiB (69059744574 Byte)

### Rodada ACERVO-100 de 2026-09-18 07:22:49
- B2 bucket total: Total size: 259.150 GiB (278260696363 Byte)
- Drive orlando diniz: Total size: 64.317 GiB (69059744574 Byte)

### Rodada ACERVO-100 de 2026-09-19 07:46:54
- B2 bucket total: Total size: 259.312 GiB (278434401881 Byte)
- Drive orlando diniz: Total size: 64.317 GiB (69059744574 Byte)
