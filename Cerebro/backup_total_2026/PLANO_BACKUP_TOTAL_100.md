# 🎯 PLANO DE TRABALHO — BACKUP TOTAL 100% (Local → Google Drive → Backblaze B2)

> **Ordem do Miguel (2026-08-05 ~12:40 BRT):** "Faz backup de TUDO, 100% no Google Drive e 100% no Backblaze.
> Primeiro o Google Drive (Backblaze depois). De 30 em 30 min faz um pouquinho; em 1-2 dias faz tudo.
> Depois disso eu vou limpar o computador."
>
> **Donos do plano:** Kimi K3/ZCode (plano + cron) e Claude Code (execução no loop dele, via ponte).
> **Base do mapeamento:** `Cerebro/backup_total_2026/MAPA_GERAL_ARQUIVOS_E_BACKUPS_20260805.md` (canônico; cópia de trabalho em `ZCodeProject/MAPA_BACKUPS_20260805.md`).

---

## 1. Contexto (o que o mapa mostrou)

- Disco local: **295G usados / 460G** (142G livres). Drive: **29,3 TiB livres** (espaço irrelevante).
- JÁ espelhado no Drive (não re-upar): `orlando diniz` 64,3G (incl. Lawfare29 61G), `Jornais do dia` 27,5G (superset), `Dados_Frios` ~47G, `backup 20260717` (snapshot congelado do workspace de 17/jul), `pautas editoriais` até 18/jul, `novo livro`, `Cerebro_Backups`, `cerebro-miguel`.
- **Buracos (sem backup nenhum):** pautas 19/jul→hoje (~7,9G), `legacy/` (11G), `Projeto Cafezinho Agentes` vivo (6G), `ZCodeProject` (1,1G), `Recordings` (591M), `casadamoeda*`+`Revista Maquiavel`+`aiatolah`+`Cicero`+`moka` pós-17/jul (~2,4G), `ferramentas` (176M), miúdos do home (`backups_livro`, `mokawriter`), zip Dossiê Orlando (364M), `Outros/*` não-espelhados (~2,4G).
- **Upload novo total estimado: ~32G.** A 2-5 MB/s ≈ 2-4h30 de rede → em janelas de 25 min a cada 30 min ≈ **1 a 2 dias** ✅ (exatamente a meta do Miguel).

## 2. Destinos no Google Drive (FASE 1 — única fase ativa agora)

| Destino | Conteúdo |
|---|---|
| `drive:pautas editoriais o cafezinho` | top-up do espelho existente (dias 19/jul+) |
| `drive:novo livro` | top-up do espelho existente |
| `drive:Dados_Frios` | top-up (ebooks novos, zip dossiê, miúdos) — **SEM** `orlando diniz/` e `Jornais do dia/` (já espelhados na raiz) |
| `drive:Workspace_Vivo/` | espelho NOVO do workspace "Antigravity Google" (vivo, pós-17/jul; o `backup 20260717` é congelado, não mexer) |
| `drive:Backup_Total/` | tudo que está fora do workspace: ZCodeProject, Recordings, ferramentas, legacy, miúdos do home |

**FASE 2 (Backblaze B2) — DESATIVADA por ora.** Só começa quando o Miguel mandar, após FASE 1 = 100%: espelhar `Backup_Total/` + `Workspace_Vivo/` + top-ups para buckets B2 (provável: bucket novo `backup-total-local-2026`).

## 3. Regras operacionais (vale para Claude e Kimi/ZCode)

1. **Protocolo de estado** em `Cerebro/backup_total_2026/ESTADO.md`: pegar o próximo chunk `PENDENTE` (ou `EM_ANDAMENTO` há >75 min = travado), marcar `EM_ANDAMENTO | agente | timestamp`, executar, e ao fim: sucesso → `CONCLUÍDO ✔ + nota de verificação`; falha/timeout → volta a `PENDENTE` (progresso do rclone é retomado automaticamente).
2. **Janela de execução:** cada rodada roda no máximo ~25 min (`timeout 1500`), 1 chunk por vez (chunk grande leva várias rodadas; rclone retoma de onde parou).
3. **Comando padrão (template):**
   ```bash
   timeout 1500 rclone copy "<ORIGEM>" "<DESTINO>" \
     --transfers 8 --checkers 8 --drive-chunk-size 64M \
     --exclude "node_modules/**" --exclude "__pycache__/**" --exclude "*.pyc" --exclude ".Trash*/**" --exclude ".next/**" \
     --log-file "/home/migueldorosario/Downloads/Antigravity Google/Cerebro/backup_total_2026/logs/<ID>.log" \
     --log-level INFO --stats-one-line --stats 60s
   ```
   (rclone pula arquivos idênticos já no destino — re-rodar é seguro e barato)
4. **Excluídos do backup (lixo regenerável, documentado):** `.deepseek/snapshots` (22G de pesos), `.cache`, caches de CLIs de IA (`.gemini`, `.grok`, `.codex`...), `node_modules`, `snap/`, instaladores (.deb), `.mozilla`, tooling (`.pyenv`, `.nvm`, `.npm`, `.rustup`, `.cargo`, `.local`, `.config` — **exceto** `~/.config/rclone/rclone.conf`, que já consta no Cofre do Cérebro).
5. **Segredos:** `cofre_intake/` e `gcloud_indexing_keys/` **NÃO** sobem (seguem o rito do Cofre de Chaves, nunca nuvem comum). Demais arquivos sobem "como estão" (mesma política do snapshot `backup 20260717`).
6. **Verificação:** ao concluir cada chunk, anotar no ESTADO a linha `Total size` do log (`rclone size` local × remoto quando couber). Divergência → marcar `REVISAR`.
7. **Erros de cota/limite do Drive:** parar, marcar chunk `PENDENTE`, registrar no log e avisar no canal (não insistir em loop).
8. **Log técnico cumulativo:** `Cerebro/Memorias/memoria_backup_total_2026.md` (1 linha por chunk executado).
9. **Não começar a FASE 2 (B2)** sem ordem do Miguel.

## 3.0 👥 PAPÉIS (atualizado — Miguel, 2026-08-05 ~14:15 BRT)

**Motores (regime atual, 05/ago 23:10):**
1. **CLAUDE (motor ÚNICO de execução):** no loop vigília dele, executa o protocolo de 5 passos por acordada — ver cartinha `cartinha_kimi_claude_HANDOFF_backup_total_executor_20260805_1440.md`: abrir ESTADO → pegar 1º PENDENTE → marcar EM_ANDAMENTO → janela `timeout 1500` → CONCLUÍDO/PENDENTE + 1 linha na Memória. **C05 é dele (teste da ponte).**
2. **MIGUEL + KIMI (observadores):** o **"vai"** do Miguel na sessão ZCode = **conferir se o Claude subiu algo** (ESTADO, logs, canal) — **uploads manuais do Kimi ENCERRADOS em C04** (para não mascarar o teste da ponte). Miguel também carrega mensagens à mão entre as sessões (ponte humana). Fórum de reforço: `Cerebro/Foruns/forum_ponte_backup_reforco_20260805.md`.

- Feitos pelo Kimi antes do regime: C01 ✔ C02 ✔ C03 ✔ C04 ✔.
- **FASE 2 (B2) continua 🔒** — só com ordem expressa do Miguel.

## 4. Tabela de chunks — FASE 1 (Google Drive)

Ordem = prioridade (buracos primeiro). Caminho base do workspace: `WS="/home/migueldorosario/Downloads/Antigravity Google"`.

| ID | Origem → Destino | Upload novo est. |
|---|---|---|
| C01 | `$WS/Outros/pautas editoriais o cafezinho` → `drive:pautas editoriais o cafezinho` | ~7,9G |
| C02 | `/home/migueldorosario/ZCodeProject` → `drive:Backup_Total/ZCodeProject` | ~1,1G |
| C03 | `/home/migueldorosario/Recordings` → `drive:Backup_Total/Recordings` | ~591M |
| C04 | `/home/migueldorosario/ferramentas` → `drive:Backup_Total/ferramentas` + `backups_livro` → `drive:Backup_Total/backups_livro` + `mokawriter` → `drive:Backup_Total/mokawriter` | ~177M |
| C05 | `/home/migueldorosario/legacy` → `drive:Backup_Total/legacy` | ~11G |
| C06 | `$WS/Projeto Cafezinho Agentes` → `drive:Workspace_Vivo/Projeto Cafezinho Agentes` | ~2-6G |
| C07 | `$WS/casadamoeda` + `casadamoeda-lab` + `casadamoeda_backup_estavel` + `casadamoeda_backup_20260729.tar.gz` → `drive:Workspace_Vivo/…` (mesmos nomes; tar.gz para `Workspace_Vivo/` raiz) | ~600M |
| C08 | `$WS/Revista Maquiavel` → `drive:Workspace_Vivo/Revista Maquiavel` | ~176M |
| C09 | `$WS/aiatolah` → `drive:Workspace_Vivo/aiatolah` | ~274M |
| C10 | `$WS/Cicero Agentes` → `drive:Workspace_Vivo/Cicero Agentes` | ~960M |
| C11 | `$WS/Cerebro` → `drive:Workspace_Vivo/Cerebro` | ~163M |
| C12 | `$WS/moka` → `drive:Workspace_Vivo/moka` | ~615M |
| C13 | `$WS/Outros` → `drive:Workspace_Vivo/Outros` **excluindo** `pautas editoriais o cafezinho/**`, `Jornais do dia/**`, `novo livro/**` (espelhos próprios) | ~2,4G |
| C14 | Resto do workspace → `drive:Workspace_Vivo/…`: `scratch`, `Rio Carta Agentes`, `Global South News`, `Kimi K3`, `Fontes`, `agent_data`, `agentes_tematicos`, `artes`, `backups_ceo_cerebro`, `github_work`, `artifacts`, `Foruns`, `Claude`, `api`, `backups`, `deploy_build`, `reportagens_para_fazer_depois`, `transcritor`, `teste_foto_na_hora_20260728`, `tmp_v3_remote` (1 comando por pasta, em sequência, na mesma janela) | ~1,5G |
| C15 | `/home/migueldorosario/Dados_Frios` → `drive:Dados_Frios` **excluindo** `orlando diniz/**` e `Jornais do dia/**` + `$WS/Outros/novo livro` → `drive:novo livro` | ~400M |
| C16 | **Verificação final:** `rclone check` (ou `size`×`size`) por destino + relatório final no canal e na Memória | — |

**Critério de FASE 1 concluída:** C01–C15 `CONCLUÍDO` + C16 sem divergências → postar `[BACKUP-TOTAL-100-FASE1-DRIVE-CONCLUIDA]` no canal_trindade e avisar o Miguel.

---

## 5. ADENDO FASE 2 (Backblaze B2) — AUTORIZADA pelo Miguel em 07/08/2026 ~12:03 ("pode rodar")

**Gatilho:** início automático assim que FASE 1 = 100% (C16 sem divergências). Não precisa de nova ordem.

**Destino:** bucket `backup-total-local-2026` (criado 07/08 12:05), remote **`gdrive-backup-b2:`** — é a chave com acesso de criar bucket. ⚠️ O remote `b2:` (e `masterb2:`) usa chave presa ao bucket `failover-cafezinho1` — não serve para a FASE 2.

**Estratégia:** copiar do **LOCAL direto para o B2** (nunca Drive→B2 — gastaria egress do Drive à toa). Mesmas exclusões da FASE 1. Espelha a geometria da FASE 1:

| ID | Origem (igual à FASE 1) | Destino B2 |
|---|---|---|
| B2-01..B2-15 | mesmas origens e exclusões de C01..C15 | `gdrive-backup-b2:backup-total-local-2026/` + mesmo caminho relativo do destino Drive (`pautas editoriais o cafezinho`, `Backup_Total/…`, `Workspace_Vivo/…`, `Dados_Frios`, `novo livro`) |
| B2-16 | verificação final `rclone size` local × B2 por destino + relatório | — |

**Template de janela (idêntico ao da FASE 1, menos a flag de Drive):**
```bash
timeout 1500 rclone copy "<ORIGEM>" "gdrive-backup-b2:backup-total-local-2026/<DESTINO>" \
  --transfers 8 --checkers 8 \
  --exclude "node_modules/**" --exclude "__pycache__/**" --exclude "*.pyc" --exclude ".Trash*/**" --exclude ".next/**" \
  --log-file ".../Cerebro/backup_total_2026/logs/B2-<ID>.log" \
  --log-level INFO --stats-one-line --stats 60s
```

**Critério de FASE 2 concluída:** B2-01..B2-15 `CONCLUÍDO` + B2-16 sem divergências → postar `[BACKUP-TOTAL-100-FASE2-B2-CONCLUIDA]` no canal_trindade e avisar o Miguel. Regras operacionais §3 valem integralmente (janelas de 25 min, ESTADO, Memória, nunca expor chaves).
