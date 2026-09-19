# 🧹 FÓRUM — Mapa do disco + mapa de backups + plano de limpeza do computador (Dell do Miguel)

**Data:** 27/08/2026 ~13:45 BRT · **Sessão:** ZCode/GLM-5.3 · **Status:** 🔄 DIAGNÓSTICO E PLANO ENTREGUES — aguarda o "vai" do Miguel para executar as fases. **Nada foi apagado.**

## O pedido do Miguel (27/08 ~13:20)

"Confira o estado da memória do zcode. O programa não precisa ficar pesado. Basta ter boa memória guardada no gdrive, no backblaze. Faça um plano pra gente limpar o computador. Faça um mapa completo. Confira também memória do disco. Faça mapa do que temos backup."

## TL;DR (5 linhas)

1. **Disco: 375G usados de 460G (86%)** — 62G livres. Apertado, mas sem emergência.
2. **Memória do ZCode em si: 2,4 MB** (371 arquivos .md). Minúscula — o que pesa são os **restos de sessão**: banco db.sqlite 1,3G + transcripts de agentes 1,2G + exec 703M + artefatos 683M (total ~/.zcode = 4,2G).
3. **🔴 GAP CRÍTICO DE BACKUP: Dossiê Orlando Diniz = 65G local** (61G = `doc lawfare oab`) × **só 434 MB no B2** × **AUSENTE no Google Drive**. Não é candidato a limpeza — é candidato a **backup urgente** antes de qualquer outra coisa.
4. Limpeza segura e imediata (caches/regeneráveis): **~30G**. Com fases seguintes (histórico git duplicado, legados espelhados no Drive, snapshots DeepSeek arquivados): **~100-130G no total**, levando o disco de 86% → ~55-60%.
5. Infraestrutura de backup já é boa: **11 remotos rclone** (gdrive + 4× B2 + r2 + legados), Drive com Backup_Total/Cerebro_Backups/Dados_Frios/Cofres atualizados em ago/2026, Cérebro triplo (local 266M + B2 Cerebro-Memorias 598MB + GitHub cerebro-miguel 430M).

## Mapa do disco (460G total, 375G usados, 62G livres)

### Bloco | Tamanho | O que é | Backup?

| Bloco | Tam. | O que é | Backup |
|---|---|---|---|
| `Dados_Frios/orlando diniz` | **65G** | Dossiê: 61G `doc lawfare oab` + 3G vídeos | 🔴 **QUASE NENHUM** (B2 434MB; Drive não tem) |
| `Antigravity Google/.git` | **28G** | Histórico git do repo `filhosdaimpunidade` (mídia commitada) | 🟡 GitHub (remote) + B2 `backup-git-antigravity-20260620` |
| `.deepseek/snapshots` | **28G** | Snapshots DeepSeek CLI (2 pastas, jun/2026) | 🔴 Nenhum — arquivar antes de apagar |
| `AG/Outros` | **27G** | 15G pautas editoriais + 5,7G Jornais do dia + 2,5G livro + 1,8G Aplicativos | 🟡 Drive Backup_Total (a confirmar profundidade) |
| `AG/.vercel/output` | **22G** | Artefatos de `vercel build` CLI | 🟢 Regenerável — nenhum necessário |
| `AG/.git_gordo_20260620` | **18G** | Snapshot antigo do git gordo | 🟢 B2 `backup-git-antigravity-20260620` (confirmar integridade) |
| `Dados_Frios/Rio Carta Agentes` | 11G | Projeto Rio Carta (dados frios) | 🟢 Drive `Dados_Frios/Rio Carta Agentes/` |
| `legacy/` | 11G | Legacy de 17/07 (cafezinho 5,3G, Rio Carta velho 4,1G…) | 🟡 Drive `Legacy_2026_08_06` (a confirmar) |
| `.gemini` | 9,4G | **6,6G browser-profile Antigravity (cache!)** + 1,8G brain + 1,2G cli | 🟢 brain já vira fóruns/memórias; profile é cache |
| `Dados_Frios/Backups_workspace` | 9,2G | Refatoração v4 temáticos **2× (~4,1G cada, jul/20)** | 🟡 B2 também tem (backblaze_v4_tematics) |
| `.pyenv` + `.nvm` | 10,8G | Runtimes Python/Node | 🟢 Reinstalável |
| `Dados_Frios/Jornais do dia` | 6,1G | PDFs de jornais | 🟢 Drive `Dados_Frios` + **duplicado em AG/Outros (5,7G)** |
| `Android` + `.android` | 7,4G | SDKs/emuladores | 🟢 Reinstalável |
| `.config/google-chrome` | 12G | Perfil Chrome | 🔴 Sem backup (logins — sensível, NÃO subir pra nuvem) |
| `.npm/_cacache` + `.cache` | ~12G | Caches npm/whisper/mozilla/playwright | 🟢 Regenerável |
| `~/.zcode` | 4,2G | Ver seção própria abaixo | 🟡 db/agents/exec sem backup externo |
| `ZCodeProject` | 2,7G | moka-app 876M + igot 765M + mutirao_v4… (repos ativos) | 🟡 GitHub parcial (moka-app sim) |
| `.grok` 2,1G · `.codex` 1,9G · `.apify` 481M · `.unsloth` 746M · `.rustup` 1,4G | ~7G | Outros CLIs/runtimes | misto |
| `cerebro-miguel` | 430M | Repo git do Cérebro → GitHub | 🟢 GitHub (sync 15 min) |

### ZCode em detalhe (o pedido central: "não precisa ficar pesado")

| Parte | Tam. | Papel |
|---|---|---|
| `cli/memories` | **2,4 MB** | **A memória de verdade** (371 .md indexados no MEMORY.md por projeto) — manter |
| `cli/db/db.sqlite` | 1,3G | Banco de sessões/tarefas (tasks-index etc.) |
| `cli/agents` | 1,2G | Transcripts completos de 47 sessões (09/jul→) |
| `cli/exec` | 703M | Stdouts persistidos (365 pastas) |
| `cli/artifacts` | 683M | Artefatos de sessões (240) |
| `cli/log` + `plugins` | 163M | Logs + plugins oficiais |
| `~/.zcode/v2` | 224M | Legado ACP (restauração de sessões antigas) |

**Conclusão:** a memória viva do ZCode é irrisória (2,4 MB). O "peso" é histórico de sessões → política correta = **arquivar histórico antigo no B2 e manter local só o recente** (ex. >30-45 dias), sem nunca tocar em `memories/`.

## Mapa de backups (o que já está guardado)

- **gdrive:** (Drive principal): `Backup_Total`, `Cerebro_Backups`, `Dados_Frios` (com Rio Carta, Agentes Labs, Cafezinho Agentes, GSN, mapario, scratch, Jornais, livros…), `Legacy_2026_08_06`, `Cofres`, `Cérebro Imortal da Trindade`, `PONTE_DRIVE_LAURA` — datas vivas em ago/2026.
- **gdrive-backup-b2:** (B2 geral): `Cerebro-Memorias` (598 MB, 16,5k obj), `Orlando-Diniz-Dossie` (434 MB), `backup-git-antigravity-20260620`, `backup-total-local-2026`, `Agents-Labs-Cafezinho`, `Cafezinho-operacional`, `Cafezinho-pos-grande-reforma-jun2026`, `Legacy-Cafezinho`, `Legacy-Miguel`, `Backup-GoogleDrive-Miguel`, `bancodemidiageral`, `cafezinho-backups`.
- **b2_orlando:** `Orlando-Diniz-Dossie` (434 MB — **incompleto**).
- **Outros remotos:** `b2-labs:`, `b2-tematicos:`, `legacy-cafezinho:`, `reforma_tencent_cafezinho:`, `r2:`, `b2:failover-cafezinho1`, `drive:` (secundário), `masterb2:` (não listou — investigar depois).
- **Cérebro:** tripé local (266M) + B2 (598M) + GitHub `cerebro-miguel` (430M, push a cada 15 min).

### Gaps de backup (riscos reais)

1. 🔴 **Orlando Diniz lawfare 61G** — quase nada guardado (434 MB). Prioridade máxima.
2. 🟡 **ZCode histórico** (db+agents+exec+artifacts ~3,9G) — sem backup externo.
3. 🟡 **`.deepseek/snapshots` 28G** — sem backup; valor histórico discutível, arquivar e decidir.
4. 🟡 Diversos `.config`/perfis — sensíveis (não subir pra nuvem por conter logins); aceitar risco ou cifrar.

## Plano de limpeza (fases — nada executa sem o "vai")

- **F0 — Prudência (30 min):** conferir integridade do `backup-git-antigravity-20260620` no B2; conferir `legacy/` × `gdrive:Legacy_2026_08_06`; rodar `rclone check` onde aplicável. Registrar tudo aqui.
- **F1 — Limpeza segura (~30G, zero risco):** apagar `AG/.vercel/output` (22G, regenera no próximo build); `npm cache clean --force` (5,3G); limpar `.cache` seletivo (chrome 2,1G, playwright, huggingface, mozilla); revisão snap antiga + journalctl.
- **F2 — Snapshots DeepSeek (+28G):** subir `.deepseek/snapshots` para novo bucket `b2_arquivo` (rclone, ~28G) e apagar local após checksum.
- **F3 — Git duplicado (+18G):** confirmar backup B2 do git gordo → apagar `AG/.git_gordo_20260620` (18G). O `.git` vivo (28G) NÃO se apaga; opcional depois: `git gc --aggressive` ou estratégia de split de mídia (decisão separada).
- **F4 — Legados espelhados (+11-17G):** `legacy/` (11G) e duplicatas (Jornais do dia em AG/Outros 5,7G; Backups_workspace refatoração duplicada 4,1G) após confirmação do Drive.
- **F5 — ZCode enxuto (+~3G):** arquivar agents/exec/artifacts/log >45 dias pro B2; `VACUUM` no db.sqlite; arquivar `v2` legado. **`memories/` intocável.**
- **F6 — URGENTE ANTES DE TUDO: backup do Orlando (+subir 61G):** `rclone copy "Dados_Frios/orlando diniz/doc lawfare oab" b2_orlando:Orlando-Diniz-Dossie/doc-lawfare-oab` (B2 aguenta; custa ~US$ 0,30/mês armazenar 61G). Rodar de madrugada.

**Resultado projetado:** ~100-130G liberados → disco sai de 86% para ~55-60%.

## O que aconteceu / o que falta / o que preciso de você (Miguel)

- **O que aconteceu:** mapa completo do disco e dos backups entregue (números acima, tudo medido ao vivo com du/df/rclone); fórum+memória+nodos gravados; nada apagado.
- **O que falta:** executar F0→F6 (com F6 primeiro na prática, backup Orlando); confirmar profundidade de `gdrive:Backup_Total`; investigar `masterb2:` vazio.
- **O que preciso de você:** o **"vai"** para começar (sugestão: **F6+F1 na mesma noite** — backup do Orlando + limpeza segura = risco zero e ~30G de volta).

---

## 🧹 ADENDO 1 — EXECUÇÃO INICIADA (27/08 14:40→15:05, "vamos fazer nessa sessão")

### F0 — prudência: descobertas que MUDARAM o plano

1. 🔴→✅ **Orlando JÁ TEM BACKUP COMPLETO**: `gdrive-backup-b2:backup-total-local-2026/Dados_Frios/orlando diniz` = **69.059.744.574 bytes / 424 objetos** vs local 69.059.965.758 / 424 (diferença 0,0003%) e **ZERO arquivos locais modificados desde 11/08** (data do backup total). O "gap crítico 65G sem backup" do mapa era **FALSO** — o mapa da manhã só olhou `b2_orlando` e o Drive, não o backup-total. Check checksum completo rodando → `/tmp/check_orlando_resultado.txt`. Upload de 65G para `b2_orlando` **cancelado** aos ~6 min (economia de ~2,5h de banda); pasta parcial `Orlando-Diniz-Dossie/dossie-completo-20260827` ficou no b2_orlando (retomável; redundância extra entre contas B2 = opcional, decisão futura do Miguel).
2. 🔴 **Backup do git gordo no B2 estava VAZIO**: `backup-git-antigravity-20260620` tinha **9 objetos / 963 bytes** (não os 18G prometidos). F3 estava travado num backup fantasma → **re-upload em andamento** (fila1, PID 1930693).
3. 🟡 **Espelho Drive do legacy é INCOMPLETO**: `rclone check` local×`gdrive:Legacy_2026_08_06` = **66.035 arquivos ausentes no Drive**, sendo **54.097 NÃO-node_modules** (MANIFESTs, INDEX.md, inventarios.json, zips, OGGs, prefight tgz). Legacy local **NÃO pode ser apagado** antes de re-upload (fila2).
4. ✅ `masterb2:` **não é vazio**: contém `failover-cafezinho1/` (mesmo conteúdo do `b2:failover-cafezinho1` do mapa). Mistério do "timeout" era listing lento.

### F1 — LIMPEZA SEGURA EXECUTADA (14:50): **+28G, disco 86% → 80%** (347G usados / 90G livres)

Apagado: `AG/.vercel/output` 22G (regenerável) + `npm cache` 5,3G + `.cache` seletivo ~2,3G (mozilla 1,1G + ms-playwright 646M + ms-playwright-go 128M + huggingface 464M). **Mantido de propósito:** `.cache/whisper` 1,8G (não re-baixar modelo durante a fila de uploads) e `.cache/google-chrome` 2,1G (Chrome aberto no momento).

### Filas em andamento (log único: `/tmp/fila_backups_limpeza_20260827.log`)

- **fila1** (`/tmp/fila_backups_limpeza_20260827.sh`, setsid—sobrevive à sessão): [F3b] git gordo 18G → `gdrive-backup-b2:backup-git-antigravity-20260620` → [F2] `.deepseek/snapshots` 28G → `b2_arquivo:snapshots-deepseek` (remote **b2_arquivo criado na hora**, creds irmãs do b2_orlando; contas B2 DIFERENTES ⇒ server-side copy impossível).
- **fila2** (`/tmp/fila2_legacy_zcode_20260827.sh`, espera fila1): [F4-up] legacy 11G → `gdrive:Legacy_2026_08_06` (incremental, sobe os 66k faltantes) → [F5-up] `~/.zcode/cli/{agents,exec,artifacts,log}` >45d + `v2` + cópia do `db.sqlite` → `b2_arquivo:zcode-historico`; **apaga o histórico >45d local SÓ se os 4 uploads derem exit 0** (`memories/` INTOCADA).
- `--bwlimit 6M` em tudo (rede continua utilizável). ETA total ≈ 18:30–19:00.

### Pendências pós-fila (próxima sessão/ronda)

1. Com `rclone check` exit 0: apagar `.git_gordo_20260620` (+18G), `.deepseek/snapshots` (+28G), `~/legacy` (+11G) → disco ~55–60%.
2. `VACUUM` no `db.sqlite` SÓ com o app ZCode fechado.
3. Conferir `/tmp/check_orlando_resultado.txt` (prova checksum do dossiê) e registrar aqui.
4. Duplicatas ainda não tocadas: Jornais do dia em AG/Outros (5,7G), Backups_workspace 2× (~4,1G).
5. Incidente menor: shell desta sessão se matou com `pgrep -f` casando o próprio cmdline (lição: usar `/proc/*/cmdline` filtrado por nome exato de binário).

**Estado:** o que aconteceu (acima) · o que falta (pendências 1–4) · o que preciso do Miguel: nada por enquanto — decisões só se quiser completar o b2_orlando dedicado ou acelerar a banda.

---

## 🧹 ADENDO 2 — APAGÕES COM PROVA + rastreamento dos vivos (27/08 15:15→15:55, ordem Miguel "tudo com backup, indexado, pode apagar no local")

### ✅ Apagado local (com prova de backup ANTES de cada rm)

1. **Orlando Diniz 65G** — prova: `rclone check` local × `gdrive-backup-b2:backup-total-local-2026/Dados_Frios/orlando diniz` = **424/424 matching files, 0 differences, exit 0** (15:02). Manifesto completo (424 arquivos, tamanho+data p/ re-download) gravado em `Cerebro/Dados/manifesto_orlando_diniz_apagado_local_20260827.txt` (sobe pro GitHub pelo sync). Re-download se precisar: `rclone copy "gdrive-backup-b2:backup-total-local-2026/Dados_Frios/orlando diniz" "~/Dados_Frios/orlando diniz"`.
2. **`Backups_workspace/refatoracao_v4_tematicos_20260720_171120` 4,1G** (a cópia VELHA de 2) — prova: check checksum = **29/29 matching, exit 0**; a cópia mais recente `_171637` (4,1G) ficou local + B2.

**Disco: 80% → 65% (283G usados, 154G livres).** Acumulado do dia: 86% → 65% = **92G liberados**.

### 🗺️ Rastreamento dos arquivos VIVOS do dia a dia (NÃO apagar — ordem do Miguel)

| Caminho | O que é | Cópia de segurança |
|---|---|---|
| `~/ZCodeProject/` (moka-app, igot, scripts/coletores/análises) | workspace de trabalho diário | moka-app→GitHub `moka-espelho` · igot→GitHub `moka` · resto → backup-total-B2 `Backup_Total/ZCodeProject` |
| `Downloads/Antigravity Google/` (Cérebro, Projeto Cafezinho Agentes, ponte_cafezinho) | Cérebro canônico + produção agentes | Cérebro triplo (local+B2+GitHub) · Cafezinho Agentes→GitHub `filhosdaimpunidade` + gdrive |
| `~/cerebro-miguel/` | repo do Cérebro | GitHub (sync 15 min) |
| `~/cofre_intake/` + `.env.unificado` (2 cofres) | credenciais VIVAS | espelhamento da Regra Nº 4 |
| `~/.zcode/cli/memories/` | memória do ZCode | **INTOCÁVEL** (2,4 MB) |
| `~/.config/google-chrome` | logins | sem backup por decisão (sensível — não sobe pra nuvem) |

### 🚫 Não apaguei (e por quê)

- **`AG/Outros/Jornais do dia` 5,7G**: NÃO é duplicata da de Dados_Frios (rsync checksum: 250/250 arquivos divergem) e **NÃO está no backup-total** (0 objetos) → virou **gap de backup**: subir pro B2 antes de qualquer apagão. Pendência nova.
- **git gordo 18G / deepseek 28G / legacy 11G**: uploads ainda correndo (fila1 subindo git gordo às 15:50); apagar só com check exit 0 pós-upload.
- **AG/.git 28G (repo vivo)**: nunca apagar; `git gc`/split de mídia = decisão separada.

### Projeção com as filas terminando (+~60G): disco ~48–52%.

**Estado:** 86%→65% hoje · falta: apagões pós-fila (git gordo, deepseek, legacy — automático via checks da próxima ronda/sessão), subir AG/Outros/Jornais pro B2, VACUUM com app fechado. **Preciso do Miguel:** nada.

---

## 🧹 ADENDO 3 — ZCode + canais limpos + DeepSeek Harness instalado + git gordo apagado (27/08 15:51→16:10)

### 1. ~/.zcode (4,3G): análise e veredito
- Histórico >45d = só 141 arquivos miúdos (~0 GB) — o peso são sessões RECENTES de agosto (agents 1,2G) e o `db/db.sqlite` 1,4G. A fila2 continua subindo >45d pro `b2_arquivo:zcode-historico` conforme envelhece, mas hoje não há o que apagar.
- **VACUUM do db.sqlite (+~1G potencial): pendente — só com o app ZCode FECHADO** (instrução pra próxima sessão de manutenção).

### 2. Canais de comunicação: backup + faxina
- **Backup íntegro ANTES de tudo**: `b2_arquivo:canais-cerebro-20260827` = **68 MB / 4.276 objs** (Foruns + ponte_kwiki inteiros). Correção no caminho: o remote b2_arquivo havia nascido com a application key RESTRITA ao bucket Orlando (a fila F2 ia falhar — e falhou, ver abaixo); recriado com a key geral do gdrive-backup-b2.
- **inbox_trindade: 7,9M → 440K** — apagados anexos de trabalho antigos (PDFs EIDAS, HTMLs/prints pesqele, scrapers TSE, package.json) mantendo TODOS os .md dos canais. O canal em si (claude.md 136K etc.) está leve e VIIVO — não picotei de_dell.md (ACKs pendentes de outras pontas; ganho ~irrisório vs risco).
- **pacote_tematicos_laura zip 7,9M apagado** (está no backup B2).

### 3. ✅ GIT GORDO APAGADO (18G) — disco 65% → **61% (264G usados, 174G livres)**
Prova: `rclone check` = 32/32 matching, 0 differences, exit 0 contra `gdrive-backup-b2:backup-git-antigravity-20260620` (agora com 19,03 GB reais — o backup fantasma de 963 bytes virou verdadeiro). F3 CONCLUÍDO.

### 4. F2 (deepseek 28G): FALHOU na 1ª tentada (key restrita do remote antigo) → **fila3 re-disparada** (`/tmp/fila3_deepseek_20260827.sh`, espera fila2 terminar; remote já corrigido).

### 5. 🚀 DeepSeek Harness (dsh) INSTALADO E NO AR (pedido do Miguel)
- Via oficial npm: `npm i -g @deepseek-ai/dsh` → **v0.1.1-rc.2**, rodando: `dsh --profile web --no-open` → **http://127.0.0.1:3080 (HTTP 200 verificado)**, log `/tmp/dsh_web.log`. Repo-fonte clonado em `~/deepseek-harness` (estudo — é MIT/aberto).
- **Config: Settings → Models na UI → colar DeepSeek API key** (a do Miguel está no cofre `.env.unificado`; colar na UI é gesto manual). Developer preview — SEM garantia de compat; modelo V4 Flash primeiro (custo).
- Reiniciar se precisar: `dsh --profile web --no-open &`.

### Balanço do dia: **86% → 61% = 111 GB liberados** · ainda virão: deepseek 28G + legacy 11G + zcode (filas) → projeção ~45-48%.
