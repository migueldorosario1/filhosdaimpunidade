# 💾 CEREBRO_NODE — Backups Operacionais no Backblaze B2

> Índice canônico dos backups do Cafezinho (e demais portais) replicados no Backblaze B2.
> Criado: **2026-06-29 22:45 BRT** por Claude Code (`claude-opus-4-7`).

---


- **[06/09/2026] FAXINA DO ZCODE DELL (ZM/Qwen3.8-Max)** — `b2:failover-cafezinho1/faxina/zcode-dell/zm_20260906_faxina_zcode/`: 5 pacotes GPG AES256 (cli_dados 661M/14.833 arquivos · hot backup db.sqlite 444M, sha do conteúdo `913ad3d8…754b` · v2 53M · config 1,7M · updater .deb 141M) + manifest/README autossuficientes. Readback VALIDADO (sha256 7/7 + decifragem dos 4 tars + sqlite integrity ok/505 sessões). Passphrase alias `ZM_ZCODE_FAXINA_20260906_PASSPHRASE` (3 cofres, sha8 `da3c13f8`). Retirada pós-validação: −3.698 MB (arquivos >7d + caches regeneráveis + .deb já instalado) + poda do db vivo (155.816 parts/42.759 messages de sessões pré-23/08, linhas preservadas) → `~/.zcode` 4,7→2,1G, `~/.config/ZCode` 744M→4,9M. VACUUM pendente (Miguel, app fechado): `~/faxina_zcode_vacuum.sh` (−800 MB). [Manifesto+recibo](Memorias/MANIFESTO_ZM_BACKUP_ZCODE_20260906.md) · [Fórum](Foruns/forum_faxina_zcode_dell_20260906.md) · [Memória](Memorias/memoria_faxina_zcode_dell_20260906.md)
- **[27/08/2026] Mapa do disco + inventário de backups + plano de limpeza do Dell** — Fórum: `Foruns/forum_mapa_disco_limpeza_computador_20260827.md` · Memória: `Memorias/memoria_mapa_disco_backup_20260827.md`. Disco 86% (375G/460G). 🔴 GAP: Orlando Diniz 65G local × 434MB no B2 × ausente no Drive → F6 backup urgente. Limpeza potencial ~100-130G (.vercel/output 22G + .git_gordo 18G + snapshots DeepSeek 28G + caches). ZCode memories=2,4MB intocável. Aguarda 'vai' do Miguel.
## 🗺️ MAPA GERAL local × Drive × B2 (2026-08-05) — LEIA PRIMEIRO para "onde está cada coisa"

> **Referência canônica de localização de TODOS os arquivos e backups do ecossistema (máquina local do Miguel):**
> **`Cerebro/backup_total_2026/MAPA_GERAL_ARQUIVOS_E_BACKUPS_20260805.md`** (Kimi K3/ZCode, 05/ago/2026)
> Traz a tabela "ONDE ESTÁ CADA COISA" (local × Google Drive × Backblaze B2), inventário dos 16 buckets B2 com tamanhos, inventário das 16 pastas-raiz do Drive, buracos de backup e plano de limpeza do disco (~200G liberáveis).
>
> **Operação viva derivada:** BACKUP TOTAL 100% (ordem Miguel 05/ago) — plano `Cerebro/backup_total_2026/PLANO_BACKUP_TOTAL_100.md` · estado `ESTADO.md` · memória `Cerebro/Memorias/memoria_backup_total_2026.md` · fórum `Cerebro/Foruns/forum_backup_total_2026.md`. FASE 1 = Google Drive (em execução, cron 30/30 min); **FASE 2 = B2 🔒 aguardando ordem do Miguel** (provável bucket novo `backup-total-local-2026`).

---

## 🪣 Buckets dedicados a backup

| Bucket | Escopo | Criado | Política |
|---|---|---|---|
| **`cafezinho-backups`** | Backups operacionais do Cafezinho prod (`us65.serverdo.in`) | 2026-06-29 22:40 BRT | Retenção indefinida; backup local correspondente purgável após 7 dias |
| `Cafezinho-operacional` | Pré-existente, escopo histórico (verificar antes de reusar) | — | — |
| `Legacy-Cafezinho` | Arquivos legados do Cafezinho antigo | — | — |
| `failover-cafezinho1` | Réplica failover NYC | — | — |
| `Cerebro-Memorias` | Snapshots do Cerebro V3 | 2026-05-10 | manifesto em `root/agent_data/backblaze_index/` |
| `mayra-brain` | Memória LTM Mayra | 2026-04-21 | App key `mayranapraia` Read+Write |

**Credenciais:**
- Master key: `Outros/chaves/backblaze_b2.env` (gitignored)
- App key `cafezinho-backups-rw` (Read+Write+List+Delete restrita ao bucket): `Outros/chaves/backblaze_cafezinho_backups.env` (gitignored)

---

## 📦 Conteúdo do bucket `cafezinho-backups`

### `camada3_20260628/` — Backup pré-otimização imagens WP (Camada 3)

| Campo | Valor |
|---|---|
| **Data do backup** | 2026-06-28 17:40 BRT |
| **Data do upload B2** | 2026-06-29 22:45→23:00 BRT (concluído em ~15min @ ~9-11 MB/s) |
| **Tamanho** | 4.7 GB (literal data 4.92 GB pelos stats do rsync) |
| **Arquivos** | **11.324** variants (thumbnails/medium/large/-scaled) — número inicial 12.105 era estimativa; contagem real do backup é 11.324 |
| **Validação integridade** | sha1 cruzado em 3 amostras: 100% match B2 ↔ local |
| **Origem** | `us65.serverdo.in:/var/www/ocafezinho/backup_camada3_20260628_174001/` |
| **Path B2** | `b2://cafezinho-backups/camada3_20260628/` |
| **Hash de integridade** | SHA1 nativo do B2 (validado automaticamente pelo `b2 sync`) |

**O que é:** Cópia integral das variantes de imagem ANTES da otimização in-place via `pngquant --quality=65-85` + `jpegoptim --max=85`. Permite rollback total ou parcial caso alguma imagem otimizada tenha ficado degradada.

**Contexto da Camada 3:**
- Camada 3 da limpeza profunda do WP Cafezinho executada em 28/jun (sessão Claude Code 28/06 17:40 → 29/06 01:30 BRT)
- Ganho ao otimizar: **2.98 GB liberados** in-place no disco de produção
- Estratégia: variantes de imagem do WP comprimidas com qualidade 65-85 (PNG) / max 85 (JPG), `-strip-all` para remover EXIF
- Risco residual coberto por este backup: degradação visual imperceptível em alguns posts

**Rollback (aplicado em 2026-06-29 23:32→23:35 BRT — `02:32→02:35 UTC`):** Backup local restaurado para os paths originais em `/var/www/ocafezinho/wp-content/uploads/` via `rsync -a --no-owner --no-group` + `chown -R www-data:www-data` nas pastas `2023/2024/2025/2026`. Disco do prod: 147G → 150G (+3GB ≈ 2.98 GB esperados). Validação pós-rollback:
- sha1 de 3 amostras (`2025/01/image-17-150x91.png`, `2026/03/dalle-sanders…`, `2025/05/image-6-768x429.png`) coincide com o backup original ✅
- Ownership `www-data:www-data` ✅
- Homepage `https://www.ocafezinho.com/` HTTP 200 (522ms) ✅
- Imagem amostra pública HTTP 200 (507ms) ✅

**Decisão Miguel 29/jun 22:25 BRT:** priorizar fidelidade visual original sobre ganho de disco; backup local pode ser purgado em 7 dias (06/jul) já que está no B2. Ver `Cerebro/CEREBRO_NODE_AGENDA_LEMBRETES.md`.

**Purga backup local executada 2026-07-07 09:12 BRT** por Claude Code após verificação de integridade:
- Contagem: 11.324 arquivos local ≡ 11.324 no B2 ✅
- SHA1 sample 3/3 matches (`06628f5e...`, `5a8bf097...`, `6f8d7366...`) ✅
- `rm -rf /var/www/ocafezinho/backup_camada3_20260628_174001/` no `us65.serverdo.in`
- Disco: 152G → 147G (−5 GB liberados no `/dev/vda2`)
- Smoke pós-purga: homepage `https://www.ocafezinho.com/` HTTP 200 (700ms) ✅
- Cópia B2 preserva rollback futuro por retenção indefinida (custo ~$0.28/ano).

---

## 🔄 Como restaurar do B2 (procedimento padrão)

```bash
# 1) SSH no servidor de destino
ssh cafezinho-wp  # ou outro servidor

# 2) Autenticar b2 com app key restrita ao bucket
B2_APPLICATION_KEY_ID=<keyID> B2_APPLICATION_KEY=<key> b2 account authorize

# 3) Sync reverso (B2 → local)
b2 sync b2://cafezinho-backups/<path>/ /destino/local/

# 4) Verificar integridade
b2 file info b2://cafezinho-backups/<path>/<arquivo>  # mostra sha1
sha1sum /destino/local/<arquivo>                       # compara
```

---

## 📅 Política de retenção dos backups operacionais

- **No prod local:** mantido pelo tempo definido na sessão da intervenção (default 7 dias se não especificado).
- **No B2:** retenção indefinida (custo de storage B2 é baixo — ~$0.005/GB/mês).
- **Custo estimado** `camada3_20260628/`: 4.7 GB × $0.005 = **$0.024/mês** (~ $0.28/ano).

---

## 🔗 Links cruzados

- Snapshot da sessão que gerou: `Projeto Cafezinho Agentes/Ponto de Retomada/Claude Code/20260629_013000_sessao.md` (§ Limpeza Cafezinho — Camada 3)
- Memória da Camada 3 (a criar): `feedback_camada3_otimizacao_imagens_wp.md`
- Cerebro de chaves: `CEREBRO_NODE_CHAVES_E_LLMS.md`
- Tabela de bugs ativos: `MEMORIA_BUGS_ATUAL.md`

---

*Documento mantido por Claude Code. Atualizar a cada novo backup subido ao B2.*

---

## 🗃️ Backup local especial — purge drafts V4 mortos (2026-07-26, Kimi K3)

**Regra do Miguel:** *"nada pode morrer nunca"* — memória permanente, NÃO purgar mesmo após os 30 dias do trash WP.

| Item | Valor |
|---|---|
| JSON-mãe (90 drafts completos, author 5470, >48h) | `Cerebro/Backups/drafts_v4_purge_20260726_1534.json` |
| SHA-256 | `84636f64c26748b9adf6527e9f988e777a62d4a167eedfe9bf07e6c41a9827d6` |
| Índice navegável | `Cerebro/Backups/INDICE_drafts_v4_purge_20260726.md` |
| Script de restore | `Cerebro/Backups/restaurar_drafts_purge_20260726.py` (recria como draft, imprime mapa id_antigo→id_novo) |
| Replicação B2 | via espelho periódico do Cérebro (mesma estrutura) |

## 🛰️ GDrive como memória externa — Dell leve (2026-08-30, ZCode/GLM-5.3)

| Item | Valor |
|---|---|
| Ordem | Miguel 29/08 ~20h (prompt DS-Dell) — Dell leve p/ gravar/editar vídeo |
| Fórum | `Cerebro/Foruns/forum_gdrive_memoria_externa_dell_20260830.md` |
| Memória | `Cerebro/Memorias/memoria_gdrive_memoria_externa_dell_20260830.md` |
| Mount | `~/GDrive` (systemd user `gdrive-mount.service`; shared drive 30 TiB; vfs-cache 2G) |
| Prova de apagamento | `~/gdrive_offload/CARIMBOS.jsonl` (copy→check→delete; gate missing=0/diff=0/matched>0) |
| Crons novos | Cérebro 12h/12h (03:40+15:40) · memória DSH/DSC diária 06:50 → `drive:Backup_Total/DSH_Dell_memoria` · purge SW Chrome */30 |
| Pendência S2 | acervo-100 sobe `Outros/chaves` em texto plano p/ Drive+B2 (flag p/ cifrar/excluir) |


## 05/09/2026 — AST-20260905-011: journals Rio-ag, cópia SEM APAGAMENTO

Ordem direta de Miguel: indexar/registrar antes de copiar para Backblaze; nenhum original será retirado. Lote01 de17journals arquivados,432MiB, inventariado e registrado no Cérebro/GitHub antes do upload. Cifra localGPG/AES256/ZLIB; três objetos copiados ao prefixo `b2:failover-cafezinho1/faxina/rio-ag/journals/2026-09/astra_20260905_lote01/`. Download integral e hashes confirmados; pacote decifrado e17membros conferidos às07:54:07BRT. Cifrado94.203.743bytes; originais reconferidosintactos;0bytesliberados, disco96%.

[Índice e recibo final com hashes/recuperação/limites](Memorias/MANIFESTO_ASTRA_BACKUP_RIO_20260905.md) · [Inventário completo](Memorias/INVENTARIO_ASTRA_BACKUP_RIO_20260905.json) · [Fórum da missão](Foruns/FORUM_ASTRA_FASE1_DISCO_NASSIF_PENDENCIAS_20260905.md) · [Memória técnica](Memorias/MEMORIA_ASTRA_FASE1_20260905.md). Chave só no cofre pelo aliasASTRA_RIO_JOURNALS_20260905_PASSPHRASE, nunca noGit. Preservar a chave é requisito para recuperação; cópias dela verificadas nesta rodada são locais, sem presumir custódia externa. Não há ObjectLock/retenção imutável comprovados. Nenhuma contratação nova; custo incrementalB2não conciliado. Nenhuma retirada local autorizada apóseste backup.


[//]: # (AST-20260905-013 — adendo de indexação e responsabilidades)

## 05/09/2026 — índice para DS-N e ZM; Astra não remove

Miguel definiu o fluxo: Astra prepara, Miguel encaminha, DS-N revisa, ZM completa os testes e faz a eventual retirada autorizada. [Índice individual dos 17 candidatos e plano de recuperação](Memorias/PLANO_ASTRA_RETIRADA_REVISAO_DSN_ZM_20260905.md). Ganho nominal possível de 417.792.000 bytes alocados, cerca de 418 MB; espaço liberado pelo Astra: zero. Não há autorização geral para limpar outros diretórios.

O backup anterior preservou conteúdo, mas não ACLs/xattrs. [Complemento de metadados](Memorias/COMPLEMENTO_ASTRA_METADADOS_JOURNALS_RIO_20260905.json) de 30.361 bytes, SHA256 `f400b74fad8be24b47c5b7ee1e5530a5ba3668c04bece72031e9cf7e55cdac23`, registrado no GitHub `ecd19767a678709d496d16cb2f228f5f1c524415`. Não está dentro do pacote B2 original; nenhum upload extra nesta rodada. Teste de recuperação de permissões e legibilidade permanece obrigatório antes da retirada. Recado ao Miguel confirmado no Telegram, mensagem 40; não equivale a aprovação do tutor.

## 05/09/2026 20:24 — ZM fecha os gates e executa a retirada autorizada (5 de 17)

Ensaio de restauração provado em cópia isolada (Tencent): 17/17 conteúdo+dono/grupo+modo+ACL efetiva+crtime+mtime/atime ns, journalctl lendo os recuperados; backup B2 reconferido de ambiente independente. Revalidação ao vivo: o próprio journald já havia removido 12 dos 17 (vacuum por disco cheio; sem perda — lote01 cobria). Retirada executada dos 5 remanescentes com revalidação no ato: 225.492 KB liberados, 96%→95%, ativo+26 excluídos preservados, serviços íntegros. A causa estrutural segue: git packs 9,2G + journald voraz 1,4G; lote02 de backup dos 26 recomendado com urgência. [Fórum](Foruns/forum_faxina_rio_lote01_zm_20260905.md) · [Memória](Memorias/memoria_faxina_rio_lote01_zm_20260905.md) · [Relatório do ensaio](Memorias/zm_relatorio_ensaio_rio.json)

## 05/09/2026 21:1x — ZM lote02: TODOS os journals do Rio protegidos + tete instalado

Lote02 `b2:failover-cafezinho1/faxina/rio-ag/journals/2026-09/zm_20260905_lote02/`: 36 journals/1,5 GB (25 excluídos do plano original + novos do journald voraz) + inventário e manifesto DENTRO do tar (pacote autossuficiente). GPG AES256, passphrase própria alias ZM_RIO_JOURNALS_LOTE02_20260905_PASSPHRASE (3 cofres c/ backup). Readback na Tencent: shas idênticos, 36/36 conferidos, journalctl lendo. Após validação: drop-in SystemMaxUse=400M/MaxFileSec=30d + vacuum (−1,1 G) — journald do Rio deixou de ser voraz. [Manifesto+recibo](Memorias/MANIFESTO_ZM_BACKUP_RIO_LOTE02_20260905.md) · [Inventário](Memorias/INVENTARIO_ZM_LOTE02_RIO_20260905.json) · [Readback](Memorias/zm_relatorio_readback_lote02.json)
