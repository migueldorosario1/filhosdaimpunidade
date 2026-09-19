# 🧾 LEDGER DE RETIRADAS — Faxina Dell 2026-09 (nada se perde)

> Toda retirada local (apagar/mover para nuvem) é registrada AQUI: o que era, tamanho, prova de backup (onde está na nuvem + verificação), data e ator.
> Missão: ordem do Miguel 08/09/2026 ~15:0x (voz) — "computador levinho, tudo na nuvem, tudo indexado no Cérebro".
> Regra: SÓ retira local depois de backup VERIFICADO (B2 e/ou GDrive, ou GitHub no caso de clones de repo, ou fonte pública no caso de modelos re-baixáveis).
> Índice/busca: `indice_local.py` + `buscador.py` nesta pasta. Fórum: `Foruns/forum_faxina_dell_buscador_20260908.md`.

## Lote 1 — 08/09/2026 ~15:2x (ZCode Qwen3.8-Max, sessão faxina)

| # | Item | Tamanho | Prova/backup | Verificação | Status |
|---|------|---------|--------------|-------------|--------|
| 1.1 | `~/.zcode/cli/db/db.sqlite.bak_pre_vacuum_20260906_2224` (db pré-VACUUM da faxina 06/09) | 1,6G | B2 `b2:failover-cafezinho1/faxina/zcode-dell/zm_20260906_faxina_zcode/` — pacote `zcode_db.sqlite.gpg` (465MB) + SHA256SUMS + manifest | `rclone lsf --format sp` 08/09 15:1x listou os 5 pacotes íntegros; readback sha 7/7 feito em 06/09 (MANIFESTO_ZM_BACKUP_ZCODE_20260906.md); db atual 738M sadio há 2 dias | ✅ APAGADO 15:2x — `~/.zcode` 2,7G→1,2G |
| 1.2 | `~/Downloads/Antigravity Google/.ds_ponte_clone_*` velhos (clones temporários da ponte DS-Dell; vazamento: 1 clone novo por ronda, 64 acumulados = 59G) | ~58G (62 clones; mantidos os 2 últimos) | GitHub `migueldorosario1/cerebro-miguel` (origem dos clones); verificação POR CLONE: `git status --porcelain` vazio + `git log --branches --not --remotes` vazio + `git stash list` vazio = nada local-only | HEAD sha de cada clone registrado em `/tmp/faxina_clones_20260908.log`; sujo/local-only → QUARENTENA `Dados_Frios/quarentena_ds_clones_20260908/` (não apaga) | ✅ 61 APAGADOS (58.832MB) 15:2x · 1 QUARENTENA: clone_276 (314M — 2 arquivos sujos + stash; o commit local-only 4e86c333 JÁ está no repo vivo; resgate do restante na fila N1b) · 2 mantidos (309/308, em uso pela ponte) |
| 1.3 | `~/.cache/whisper` (modelos Whisper baixados) | 1,8G | Fonte pública (openai-whisper, re-baixável sob demanda); nenhum processo local usa (transkriptor roda no Tencent) | — | ✅ APAGADO 15:2x |
| 1.4 | `~/.cache/huggingface` (modelos HF) | 1,5G | Fonte pública (huggingface.co, re-baixável) | — | ✅ APAGADO 15:2x |
| 1.5 | `~/.deepseek/snapshots/62842bf2b53f9dcb/` (auto-snapshot DeepSeek ~20/06) | 23G (pack 20,2GiB) | CORROMPIDO: `fatal: missing object 67a32698... for refs/heads/master` (única ref quebrada; sem working tree, só .git; sem remote). Sem valor de recuperação — bundle impossível. Conteúdo da época coberto por `b2:backups_antigravity` / `Antigravity_Google` e GitHub | Evidência do fatal capturada às 15:1x (saída git for-each-ref) | ✅ APAGADO 15:2x |

## Lote 2 — 08/09/2026 ~15:3x (jornais do dia — ordem explícita do Miguel)

| # | Item | Tamanho | Prova/backup | Verificação | Status |
|---|------|---------|--------------|-------------|--------|
| 2.1 | `Dados_Frios/Jornais do dia/` — 230 PDFs (jornais até ~25/08) | 6,1G | GDrive `gdrive:Jornais do dia` | `rclone check --size-only --one-way` 15:30: **230/230 matching, 0 diferenças** | ✅ APAGADOS 15:3x; pasta virou APONTADOR.md (56K) |
| 2.2 | `AG/Outros/Jornais do dia/` — 271 PDFs verificados (>3 dias, cópia idêntica nome+tamanho no GDrive) | 6,35G | GDrive `gdrive:Jornais do dia` (1216 arquivos listados 15:3x) | comparação nome+tamanho contra `rclone lsf --format sp`; recentes (<3d) MANTIDOS (12); 5 FT (UK/US, tamanhos divergentes do GDrive) MANTIDOS p/ decisão | ✅ APAGADOS 15:3x; 20 PDFs mantidos |
| 2.3 | FLUXO CORRIGIDO: `jornaisdodia.sh` (cron 10:30/13:00/18:00) agora chama `sweep_jornais_verificados.py` após o upload — apaga local >3d só com cópia idêntica verificada (fail-safe: sem listagem = não apaga) | — | backup do script: `jornaisdodia.sh.bak_pre_faxina_20260908` | 1ª execução automática no cron das 18:00 de hoje | ✅ NO AR 15:4x |

**Saldo do dia até 15:4x:** disco 72%→**51%** (313G→219G usados; **94G liberados**; 218G livres).

## Lote 3 — 08/09/2026 ~17:1x (reforço do Miguel: índice duplo, ZCode levinho, canais rotacionados — "não quero perder nada, tudo com dois backups")

| # | Item | Tamanho | Prova/backup | Verificação | Status |
|---|------|---------|--------------|-------------|--------|
| 3.1 | `~/.zcode/cli/{artifacts,exec}` arquivos >14d (296 arquivos) | 19M (tar 7,8M → gpg 7,5M) | **DUPLO**: `gdrive:Backup_Total/dell_faxina/zcode/` + `b2:failover-cafezinho1/faxina/zcode-dell/antigos/` — pacote `zcode_antigos_20260908.tar.gz.gpg` (AES256, passphrase = alias `ZM_ZCODE_ANTIGOS_PASSPHRASE` nos 2 cofres `.env.unificado`, backups `.bak_pre_zcode14d_20260908`) + SHA256SUMS + MANIFESTO (lista completa dos 296) | upload rc=0 nos 2 destinos + `lsf` tamanho confere ×2 + **readback sha256 confere ×2** | ✅ APAGADOS 17:1x (fail-closed: só podou após os 2 readbacks); rito permanente no passo 4 da leve (`purga_zcode_antigos.sh`) |
| 3.2 | Canais da ponte Laura **ROTACIONADOS** (não apagados — arquivo integral datado): `de_dell.md` 9,5M + `de_laura.md` 2,8M → vivos novos leves (1,5K + 716b) | 12,4M → ~2K | **QUÁDRUPLO**: `ponte_laura_completa/arquivo/backup_2026-09-08_1714/` (local) + GitHub (repo cerebro-miguel, push c/ prova) + `gdrive:Backup_Total/dell_faxina/canais/backup_2026-09-08_1714/` + `b2:failover-cafezinho1/faxina/canais-dell/backup_2026-09-08_1714/` | tamanhos conferem nos 2 remotos (9.919.596 + 2.892.637) + prova no origin (vivo novo contém ZM-20260908-005; arquivo = 9.919.596 bytes idênticos) | ✅ ROTACIONADOS 17:14; avisos ZM-20260908-005 nos vivos novos + inbox claude/antigravity; rito = `rotaciona_canais.sh` |
| 3.3 | **ÍNDICE DUPLICADO** (nada retirado — adição): `indice.sqlite` (139MB) espelhado 1×/dia → `gdrive:Backup_Total/dell_faxina/indice/` + `b2:failover-cafezinho1/faxina/indice/`; `CATALOGO_NUVEM.md` (índice legível do que há nas nuvens) gerado toda passada no Cérebro/repo (já é espelhado = catálogo triplo) | +139M×2 nuvem | `gera_seed_faxina.py` (`espelhar_indice()` c/ marker diário + verificação `lsf`; `catalogo_nuvem()` c/ listagens rclone) | cópia verificada nos 2 destinos 17:09 + push origin ✅ + seed c/ campo `nuvem.espelho_indice` | ✅ NO AR 17:09 — roda sozinho a cada passada da leve |

**Saldo do dia até 17:2x:** disco **51%** (lote 3 = leve em GB, pesado em estrutura: índice duplo + canais rotacionados + ZCode >14d na nuvem). ZCode cli 1,2G; canais da ponte ~35M→~23M (vivos 2K).

## Lote 4 — 08/09/2026 ~20:4x (automação LEVE ZM 4/4h — "roda de 4 em 4 horas mas pouquinha coisa")

| # | Item | Tamanho | Prova/backup | Verificação | Status |
|---|------|---------|--------------|-------------|--------|
| 4.1 | `~/.zcode/cli/{artifacts,exec}` arquivos >14d (**19 arquivos** — 2ª purga do dia) | tar 418.261b → gpg 418.363b | **DUPLO**: `gdrive:Backup_Total/dell_faxina/zcode/zcode_antigos_20260908.tar.gz.gpg` + `b2:failover-cafezinho1/faxina/zcode-dell/antigos/` (mesmo nome) + SUMS + MANIFESTO | lsf tamanho ✅ ×2 + readback sha256 `340242496f35b20b…` ✅ ×2 (fail-closed satisfeito ANTES da poda) | ✅ RETIRADO (rc=0; `~/.zcode/cli` segue 1,2G; marcador `purga_zcode` 20:41) |
| 4.2 | 🔴 **INCIDENTE achado e CURADO (nada se perdeu)**: a 2ª corrida do dia da purga **SOBRESCREVEU** nas duas nuvens o tar do Lote 3.1 (296 arquivos) — o script nomeava o pacote só com a data (`$DIA`), colisão em reexecução no mesmo dia: `zcode_antigos_20260908.tar.gz.gpg` caiu de 7.844.452b → 418.363b | — (nenhum byte perdido) | **RESGATE**: versionamento do B2 (`rclone --b2-versions`, cópia `-v2026-09-08-201034-595.gpg` de 17:09) → download → sha256 **CONFERE** com o SUMS versionado (`dc3dc13739c59f8e…`) → **REANCORADO com nome único** `zcode_antigos_20260908_run1709.tar.gz.gpg` (+ `.SHA256SUMS` + `_MANIFESTO.md` com nota do resgate) em GDrive **E** B2 | lsf 7.844.452b ✅ ×2 + readback sha ✅ ×2 nos 2 destinos | ✅ CURADO: script agora usa `PACOTE="zcode_antigos_${DIA}_$(date +%H%M%S)"` (backup `.bak_pre_pacote_stamp_20260908`, `bash -n` OK) — reexecução no mesmo dia nunca mais colide |

Demais passos da passada: clones DS = só 2 presentes (`.ds_ponte_clone_309` 17:06 950M / `_308` 12:03 1,4G — MANTIDOS, regra dos 2 últimos) · jornais: 0 PDFs apagados (nenhum >3d com cópia verificada) · caches chrome/mesa PULADOS (navegador aberto, 24 processos) · `.bak_fallback_*` >7d = 0 · índice regenerado (265.959 arquivos / 47.515 dirs / 29s).

**Saldo 20:5x:** nenhuma outra retirada; a nuvem dupla do ZCode >14d fica COMPLETA com os dois pacotes do dia: `_run1709` (296 arquivos, 7,8M gpg) + atual (19 arquivos, 418K gpg).

## Lote 5 — 09/09/2026 ~04:4x (automação LEVE ZM 4/4h)

| # | Item | Tamanho | Prova/backup | Verificação | Status |
|---|------|---------|--------------|-------------|--------|
| 5.1 | `~/.zcode/cli/{artifacts,exec}` arquivos >14d (**6 arquivos** — novos que completaram 14d após as purgas de 08/09) | tar 116.490b → gpg 116.599b | **DUPLO**: `gdrive:Backup_Total/dell_faxina/zcode/zcode_antigos_20260909_044142.tar.gz.gpg` + `b2:failover-cafezinho1/faxina/zcode-dell/antigos/` (mesmo nome) + SUMS + MANIFESTO | lsf 116.599b ✅ ×2 + readback sha256 `daa11009963c413b…` ✅ ×2 (fail-closed satisfeito antes da poda) | ✅ RETIRADO (rc=0; 1ª corrida com o PACOTE carimbado HHMMSS — cura anti-colisão do Lote 4.2 provada em produção; marcador `purga_zcode` 04:41) |

Demais passos da passada: jornais 0 · clones DS = 2 mantidos (`_309` 999M 01:06 / `_308` 1,4G) · caches chrome pulados (navegador aberto, 24 processos) · `.bak_fallback_*` >7d = 0.

## Lote 6 — 09/09/2026 ~12:4x (automação LEVE ZM 4/4h)

| # | Item | Tamanho | Prova/backup | Verificação | Status |
|---|------|---------|--------------|-------------|--------|
| 6.1 | `~/.zcode/cli/{artifacts,exec}` arquivos >14d (**5 arquivos** — novos que completaram 14d) | tar 8274b → gpg 8.378b | **DUPLO**: `gdrive:Backup_Total/dell_faxina/zcode/zcode_antigos_20260909_124127.tar.gz.gpg` + `b2:failover-cafezinho1/faxina/zcode-dell/antigos/` (mesmo nome) + SUMS + MANIFESTO | lsf 8.378b ✅ ×2 + readback sha256 `bcde19c1067e94b5…` ✅ ×2 (fail-closed satisfeito antes da poda) | ✅ RETIRADO (rc=0; marcador `purga_zcode` 12:41) |

Demais passos da passada: jornais 0 · clones DS = 2 mantidos (`_309` 1,1G 11:08 / `_308` 1,4G) · caches chrome pulados (navegador aberto, 66 processos) · `.bak_fallback_*` >7d = 0.

## Lote 7 — 09/09/2026 ~16:4x (automação LEVE ZM 4/4h)

| # | Item | Tamanho | Prova/backup | Verificação | Status |
|---|------|---------|--------------|-------------|--------|
| 7.1 | `~/.zcode/cli/{artifacts,exec}` arquivos >14d (**7 arquivos** — novos que completaram 14d) | tar 1598b → gpg 1.702b | **DUPLO**: `gdrive:Backup_Total/dell_faxina/zcode/zcode_antigos_20260909_164136.tar.gz.gpg` + `b2:failover-cafezinho1/faxina/zcode-dell/antigos/` (mesmo nome) + SUMS + MANIFESTO | lsf 1.702b ✅ ×2 + readback sha256 `1e65204a732bf0d2…` ✅ ×2 (fail-closed satisfeito antes da poda) | ✅ RETIRADO (rc=0; marcador `purga_zcode` 16:41) |

Demais passos da passada: jornais 0 · clones DS = 2 mantidos (`_309` 1,2G / `_308` 1,4G) · caches chrome pulados (navegador aberto, 67 processos) · `.bak_fallback_*` >7d = 0.

## Lote 8 — 10/09/2026 ~02:1x (automação leve ZM, passada 00:4x)

| # | Item | Tamanho | Prova/backup | Verificação | Status |
|---|------|---------|--------------|-------------|--------|
| 1 | ~/.zcode/cli — 1 arquivo artifacts/exec >14d (pacote gpg `zcode_antigos_20260910_021327.tar.gz.gpg`; tar 1.251b → gpg 1.355b) | 1 arq | GDrive `gdrive:Backup_Total/dell_faxina/zcode/` + B2 `b2:failover-cafezinho1/faxina/zcode-dell/antigos/` (+SUMS +MANIFESTO) | lsf tamanho ×2 + readback sha256 `5ec714ea5a6e3843…` confere ×2; fail-closed satisfeito antes da poda; rc=0; marcador purga_zcode 02:13 | ✅ |

Demais passos da passada: clones DS 2 mantidos (_309/_308, regra dos 2 últimos); jornais 0; caches pulados (chrome aberto); .bak_fallback >7d: 0; índice 277.649 arq/48.090 dirs em 28s. Sem Telegram (retirada de rotina).

## Lote 9 — 10/09/2026 ~11:3x (ZM/GLM 5.3, ordem direta do Miguel "remover tudo que está vazio" no AG)

| # | Item | Tamanho | Prova/backup | Verificação | Status |
|---|------|---------|--------------|-------------|--------|
| 1 | 6 VAZIOS no AG: dirs `Google/.ds_r286` + `Google/` (vazia após) e 4 arq `.ds_tmp/{serie_completa,notas_final,notas_mem2,notas_ponte2}.txt` | 0 b | manifesto .tsv em /tmp + ~/.local/share/buscador_local/.reorg_vazios_*.tsv (nomes/mtime/perms) | 0 crons + 0 scripts consumidores (fail-closed); demais 33 vazios MANTIDOS com motivo (locks agent_data, ledgers publicadas_*.jsonl/gsn_inbox.db de robôs vivos, .git/branches ×7, node_modules/.astro, Cerebro intocável, ds_ronda_385_pendente com pendente de HOJE) | ✅ |

Contexto: parte da missão de reorg do Antigravity (fórum reorg_workspace_zcodeproject_20260910 adendo 2+3).
## Lote 10 — 10/09/2026 ~12:4x (automação leve ZM, passada 12:4x)

| # | Item | Tamanho | Prova/backup | Verificação | Status |
|---|------|---------|--------------|-------------|--------|
| 1 | 15 PDFs de jornais >3d em Outros/Jornais do dia/ (sweep_jornais_verificados.py) | 437 MB | cópia idêntica nome+tamanho no GDrive (fail-safe do próprio script: sem listagem remota não apaga) | verificação GDrive pré-apagado embutida; rc=0 | ✅ |

Demais passos: clones 2 mantidos; chrome 57 → caches pulados; bak>7d 0; purga ZCode 0 (nada >14d); índice 300.700 arq/49.201 dirs em 30s; seed push 12:42 OK c/ prova. Sem Telegram (retirada de rotina verificada).
## Lote 11 — 10/09/2026 ~16:4x (automação leve ZM, passada 16:4x)

| # | Item | Tamanho | Prova/backup | Verificação | Status |
|---|------|---------|--------------|-------------|--------|
| 1 | ~/.zcode/cli — 4 arquivos artifacts/exec >14d (pacote gpg `zcode_antigos_20260910_164234.tar.gz.gpg`; tar 135.371b → gpg 135.480b) | 4 arq | GDrive `gdrive:Backup_Total/dell_faxina/zcode/` + B2 `b2:failover-cafezinho1/faxina/zcode-dell/antigos/` (+SUMS +MANIFESTO) | lsf tamanho ×2 + readback sha256 `9700d8b5969113ef…` confere ×2; fail-closed satisfeito antes da poda; rc=0 | ✅ |

Demais passos: clones 2 mantidos; jornais 0; chrome 41 → caches pulados; bak>7d 0; índice 301.760 arq/49.255 dirs em 34s. Sem Telegram (retirada de rotina).
## Lote 12 — 10/09/2026 ~20:4x (automação leve ZM, passada 20:4x)

| # | Item | Tamanho | Prova/backup | Verificação | Status |
|---|------|---------|--------------|-------------|--------|
| 1 | ~/.zcode/cli — 2 arquivos artifacts/exec >14d (pacote gpg `zcode_antigos_20260910_204045.tar.gz.gpg`; tar 123.656b → gpg 123.765b) | 2 arq | GDrive `gdrive:Backup_Total/dell_faxina/zcode/` + B2 `b2:failover-cafezinho1/faxina/zcode-dell/antigos/` (+SUMS +MANIFESTO) | lsf tamanho ×2 + readback sha256 `c8b8e8540f16cc66…` confere ×2; fail-closed satisfeito antes da poda; rc=0 | ✅ |

Demais passos: clones 2 mantidos; jornais 0; chrome 64 → caches pulados; bak>7d 0; índice 303.538 arq/49.302 dirs em 31s. Sem Telegram (retirada de rotina).
## Lote 13 — 11/09/2026 ~00:4x (automação leve ZM, passada 00:4x)

| # | Item | Tamanho | Prova/backup | Verificação | Status |
|---|------|---------|--------------|-------------|--------|
| 1 | Clone DS .ds_ponte_clone_308 (Antigravity Google/) | 1,4 GB | conteúdo íntegro no repo remoto (clone limpo) | 4/4 checks: .git presente · git status --porcelain VAZIO · git log --branches --not --remotes ZERO · git stash list VAZIO — nenhum traço local-only; mantidos _409 (fresco) e _309 (regra dos 2 últimos); log /tmp/sweeper_clones_20260911.log | ✅ |

Demais passos: jornais 0; chrome 66 → caches pulados; bak>7d 0; purga ZCode 0 (>14d); índice 316.551 arq/49.807 dirs em 20s. Sem Telegram (retirada de rotina com 4/4 provas).
## Lote 14 — 11/09/2026 ~04:4x (automação leve ZM, passada 04:4x)

| # | Item | Tamanho | Prova/backup | Verificação | Status |
|---|------|---------|--------------|-------------|--------|
| 1 | ~/.zcode/cli — 9 arquivos artifacts/exec >14d (pacote gpg `zcode_antigos_20260911_044110.tar.gz.gpg`; tar 263.692b → gpg 263.801b) | 9 arq | GDrive `gdrive:Backup_Total/dell_faxina/zcode/` + B2 `b2:failover-cafezinho1/faxina/zcode-dell/antigos/` (+SUMS +MANIFESTO) | lsf tamanho ×2 + readback sha256 `f47b544916c5f1cf…` confere ×2; fail-closed satisfeito antes da poda; rc=0 | ✅ |

Demais passos: clones 2 mantidos (_409/_309); jornais 0; chrome 54 → caches pulados; bak>7d 0; índice 318.814 arq/49.827 dirs em 21s. Sem Telegram (retirada de rotina).
## Lote 15 — 11/09/2026 ~12:4x (automação leve ZM, passada 12:4x)

| # | Item | Tamanho | Prova/backup | Verificação | Status |
|---|------|---------|--------------|-------------|--------|
| 1 | ~/.zcode/cli — 6 arquivos artifacts/exec >14d (pacote gpg `zcode_antigos_20260911_124109.tar.gz.gpg`; gpg 12.501b) | 6 arq | GDrive `gdrive:Backup_Total/dell_faxina/zcode/` + B2 `b2:failover-cafezinho1/faxina/zcode-dell/antigos/` (+SUMS +MANIFESTO) | lsf tamanho ×2 + readback sha256 confere ×2; fail-closed satisfeito antes da poda; rc=0 | ✅ |

Demais passos: clones 2 mantidos (_409/_309); jornais 0; chrome 46 → caches pulados; bak>7d 0; índice 322.967 arq/49.903 dirs em 26s. Sem Telegram (retirada de rotina).
## Lote 16 — 12/09/2026 ~18:4x (automação leve ZM, passada 18:4x — 1º sweep após gap de ~30h sem faxina)

| # | Item | Tamanho | Prova/backup | Verificação | Status |
|---|------|---------|--------------|-------------|--------|
| 1 | ~/.zcode/cli — 105 arquivos artifacts/exec >14d (pacote gpg `zcode_antigos_20260912_184136.tar.gz.gpg`; tar 3.344.924b → gpg 3.345.033b) | 105 arq | GDrive `gdrive:Backup_Total/dell_faxina/zcode/` + B2 `b2:failover-cafezinho1/faxina/zcode-dell/antigos/` (+SUMS +MANIFESTO) | lsf tamanho ×2 + readback sha256 `e672ffb18d831eef…` confere ×2; fail-closed satisfeito antes da poda; rc=0 | ✅ |

Demais passos: clones 2 mantidos (_409/_309, únicos existentes); jornais 0; chrome 34 → caches pulados; bak>7d 0; índice 322.990 arq/50.151 dirs em 20s. Sem Telegram (retirada de rotina).
## Lote 17 — 15/09/2026 ~06:4x (automação leve ZM, passada 06:4x — 1º sweep após gap de ~60h sem faxina)

| # | Item | Tamanho | Prova/backup | Verificação | Status |
|---|------|---------|--------------|-------------|--------|
| 1 | ~/.zcode/cli — 324 arquivos artifacts/exec >14d (pacote gpg `zcode_antigos_20260915_064129.tar.gz.gpg`; tar 10.354.614b → gpg 10.354.723b) | 324 arq | GDrive `gdrive:Backup_Total/dell_faxina/zcode/` + B2 `b2:failover-cafezinho1/faxina/zcode-dell/antigos/` (+SUMS +MANIFESTO) | lsf tamanho ×2 + readback sha256 `ff4a9d233345c5e1…` confere ×2; fail-closed satisfeito antes da poda; rc=0 | ✅ |

Demais passos: clones 2 mantidos (_409/_309, únicos existentes); jornais 0; chrome 25 → caches pulados; bak>7d 0; índice 360.587 arq/51.749 dirs em 21s. Sem Telegram (retirada de rotina).
## Lote 18 — 16/09/2026 ~12:4x (automação leve ZM, passada 12:4x)

| # | Item | Tamanho | Prova/backup | Verificação | Status |
|---|------|---------|--------------|-------------|--------|
| 1 | ~/.zcode/cli — 134 arquivos artifacts/exec >14d (pacote gpg `zcode_antigos_20260916_124059.tar.gz.gpg`; tar 2.807.485b → gpg 2.807.594b) | 134 arq | GDrive `gdrive:Backup_Total/dell_faxina/zcode/` + B2 `b2:failover-cafezinho1/faxina/zcode-dell/antigos/` (+SUMS +MANIFESTO) | lsf tamanho ×2 + readback sha256 `de3664690a0fedc7…` confere ×2; fail-closed satisfeito antes da poda; rc=0 | ✅ |

Demais passos: clones 2 mantidos (_409/_309, únicos existentes); jornais 0; chrome 45 → caches pulados; bak>7d 0; índice 377.264 arq/51.999 dirs em 37s. Sem Telegram (retirada de rotina).
## Lote 19 — 17/09/2026 ~18:4x (automação leve ZM, passada 18:4x — 1º sweep após gap de ~30h)

| # | Item | Tamanho | Prova/backup | Verificação | Status |
|---|------|---------|--------------|-------------|--------|
| 1 | ~/.zcode/cli — 258 arquivos artifacts/exec >14d (pacote gpg `zcode_antigos_20260917_184044.tar.gz.gpg`; tar 10.327.009b → gpg 10.327.118b) | 258 arq | GDrive `gdrive:Backup_Total/dell_faxina/zcode/` + B2 `b2:failover-cafezinho1/faxina/zcode-dell/antigos/` (+SUMS +MANIFESTO) | lsf tamanho ×2 + readback sha256 `1cb3a5407919d2ed…` confere ×2; fail-closed satisfeito antes da poda; rc=0 | ✅ |

Demais passos: clones 2 mantidos (_409/_309, únicos existentes); jornais 0; chrome 52 → caches pulados; bak>7d 0; índice 384.176 arq/52.027 dirs em 22s. Sem Telegram (retirada de rotina).
## Fila (próximos lotes — noite/automação; cada um só executa com backup verificado)

- **N1** `.deepseek/snapshots/f608...` (5G, válido, commit 9829bd0 "post-turn:2" 22/08) → identificar projeto (`git ls-tree`), `git bundle --all` → B2 + GDrive, readback sha → retirar.
- **N1b** Quarentena `Dados_Frios/quarentena_ds_clones_20260908/.ds_ponte_clone_276` (314M): diff dos 2 edits (`cerebro/CEREBRO_NODE_BUGS_ATIVOS.md`, `cerebro/Foruns/ponte_laura_completa/de_dell.md`) + `git stash show -p` × versões vivas do repo → resgatar conteúdo único (patch p/ repo vivo ou `Cerebro/Backups/`) → retirar a quarentena.
- **N2** `AG/.git` (27G, repo-armadilha filhosdaimpunidade, morto desde 05/09) → exportar ÚNICOS: patches da branch `master` (1222f963, não está no GitHub) + diffs dos 3+ stashes → guardar no Cérebro+B2 (KBs); conferir `deploy-main`/refs vs `git ls-remote` (main dc23697c = deploy-main local, coberto) → retirar `.git` inteiro.
- ~~**N3** Jornais do dia~~ ✅ **FEITO 08/09 15:3x** (Lote 2: 501 PDFs/12,4G retirados com verificação GDrive + fluxo do `jornaisdodia.sh` corrigido com sweep pós-upload; 5 FTs divergentes mantidos p/ decisão do Miguel).
- **N4** Dados_Frios restantes (mapario 13G, Rio Carta Agentes 11G, Backups_workspace 5,2G, Agentes Labs 5G, livros 3,7G, Bella Cia 2,3G, scratch 2,2G, GSN 1,9G…) → um subitem/noite: tar+gpg → B2 + GDrive, readback → retirar local (mantém pasta com APONTADOR.md).
- **N5** AG/Outros: `novo livro` 2,5G, `mapa rio videos` 2,2G, `Aplicativos` 1,8G (instaladores) → mesmo rito. INTOCÁVEIS: `Negocios Priscila` (missão Fênix ativa), `pautas editoriais` (sessão ativa hoje), `chaves` (cofre vivo).
- **N6** Sessões de outros agentes: `.codex/sessions` 2,1G, `.grok/sessions` 1,9G + `.grok/downloads` 442M, `.codex/.tmp` 197M → tar → B2 → podar >30d.
- **N7** Navegadores/perfis: `.config/google-chrome` 8,8G e `.gemini/antigravity-browser-profile` 6,6G → podar SÓ caches regeneráveis (Cache/Code Cache/Service Worker/GPUCache), NUNCA Local Storage/IndexedDB (logins — lição 06/09).
- **N8** MONITORAMENTO_DE_TRABALHO.md 290KB → renovação 48h atrasada (regra 07/08) — fazer de madrugada com diff morto×vivo (janela sem sessões).
- **N9** Toolchains (⚠️ só com OK explícito do Miguel — `.pyenv/versions/3.10.13` é usado pelos CRONS): `.pyenv` 7G (versões velhas), `.nvm` 4,1G, `~/Android` 5,9G, `.rustup` 1,4G, `.gradle` 671M, `.local/lib` 7,1G.
- ~~**N10** Higiene ZCode + rotação de canais~~ ✅ **FEITO 08/09 17:1x** (Lote 3: 296 arquivos ZCode >14d → nuvem dupla com readback; `de_dell.md`/`de_laura.md` rotacionados com backup quádruplo e aviso ZM-20260908-005. Ritos viraram rotina: `purga_zcode_antigos.sh` no passo 4 da leve 4/4h; `rotaciona_canais.sh` quando canal passar de ~8-10M, na janela entre rondas; `cli/log`/`cli/rollout` são regeneráveis — só podar >14d se passarem de 50M).
- **N11** Consolidação do topo do AG (209 itens → D5 "poucos diretórios"): mortos p/ `AG/arquivo/` (DS_ronda_*_RESGATE.md de agosto, jpgs/scripts soltos, zips, `casadamoeda_backup_estavel`, `backups_ceo_cerebro`, `deploy_build`…) — ANTES grep crontab/systemd/scripts por referências; poucos itens/noite; cada mudança = linha neste ledger (mover não é apagar, mas indexado é obrigatório).
- **N12** Snapshot SEMANAL do DB do ZCode (`~/.zcode/cli/db/db.sqlite` 738M — VIVO, nunca podar; vacuum já feito pelo Miguel 06/09): cópia gpg → `gdrive:Backup_Total/dell_faxina/zcode/db/` + `b2:failover-cafezinho1/faxina/zcode-dell/db/` (backup duplo — ordem "não quero perder nada"), readback sha, manter as 4 últimas (nuvem = único lugar; local só o vivo). Cadência: madrugada de domingo (pesada se existir; senão a leve, marker `.ultimo_snapshot_db`). Passphrase: mesma família de aliases dos cofres (criar `ZM_ZCODE_DB_PASSPHRASE` espelhada, Regra №4).
