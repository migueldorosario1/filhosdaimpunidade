# Memória — Censo técnico completo da varredura de discos (07/08 ~11:10 BRT)

> [!CAUTION]
> **OVERRIDE CANÔNICO DE 11/08/2026:** este censo continua válido como fotografia histórica, mas qualquer proposta de purge ou limpeza autônoma está superada. Um item precisa ter mais de 15 dias contínuos de inatividade para ser apresentado a Miguel e ainda depende de autorização explícita; inventário integral é obrigatório inclusive para lixo autorizado. Ver `Memorias/memoria_missao_faxina_diaria_legacy_20260811.md`.

> **Fórum (plano + decisões):** `Foruns/forum_plano_faxina_continua_droplets_20260807.md` · **Autor:** Kimi K3 / ZCode
> **Método:** SSH read-only (`df`, `du -x -d1`, `find -size +30M -mtime -14`, `journalctl --disk-usage`, `docker system df`, `rclone lsd/lsl`). Zero escrita nos servidores.

## Censo por servidor

### NYC 198.199.121.136 — produção V4 — 48G: 38G usado (79%), 11G livre
- `/root` = 26G. Top: `venv` 7,7G · `.cache` **4,9G** (pip **4,2G** + puppeteer 627M + whisper 139M + yfinance 20K) · `agent_data` 2,8G · `.local/share` 2,8G · `gsn_remote` 1,9G (`.git` do gsn = **1,5G**) · `cicero_remote` 1,8G · `backups` **1,2G** (73 pastas `banco_midia_*_2026XXXX` + `midia/`) · `cafezinho` 581M · `V3` 514M · `legacy` 450M · `agente_estatistico` 370M
- Journal 107MB · `/var/log` 193MB (OK)
- Arquivos crescendo (>30M/14d): `log_rotas_llm.jsonl` 167MB (07/08) · `v4_verticals/ciencia_tecnologia_ia.sqlite3` 98MB · `banco_imagens_reais.db` 65MB + `.bak_20260807_034728` 60MB · `geopolitica.sqlite3` 44MB · `banco_midia_ouro_v3.db` 43MB · `banco_custos_2026-07.jsonl` 34MB
- Logs sem rotação: `gsn_remote/gsn/logs/gsn_hourly_cron.log` **143MB** · `robo_coleta_sobrenatural.log` 40MB · `robo_coleta_militar.log` 44MB · `robo_coleta_fantastico.log` 43MB · `robo_coleta_turismo.log` 41MB · `coletor_eleicoes.log` 32MB

### Rio-Carta-Agentes 159.89.185.209 — fábrica satélites — 24G: 21G usado (87% 🟠), 3,1G livre
- `/root` = 11G. Top: `riocarta_remote` 3,8G · `cicero_remote` 2,9G · `gsn_remote` 1,7G · `.npm` **1,1G** · `agentes` 654M · `agent_data_trilhos` 112M · `agent_data` 103M · `logs` 62M
- **Git packs (crescem a cada push — heroes versionados no git):** `riocarta_remote/rio-carta/.git/objects/pack/pack-48832c…` **2,52GB** (06/08) · `cicero_remote/cicero/.git/…/pack-0e8ca8…` **2,40GB** (07/08) · `gsn_remote/gsn/.git/…/pack-4a0e40…` **1,43GB** (07/08)
- `cicero_remote/cicero/logs/ceara_publication_audit.jsonl` **214MB** (audit por publicação)
- Journal 121MB · `/var/log` 171MB (OK)

### Droplet-util 142.93.48.252 — Central Alertas + agentes — 24G: 8,8G usado (38%), 15G livre
- `/root` = 2,1G: `gsn` 1,5G · `agentes` 373M · `agent_data_trilhos` 116M · `aiatolah` 104M
- Docker: 1 imagem 723MB (Kuma) + volume 4,9MB (OK)
- **journald 486,8MB** (limitar `SystemMaxUse=200M`)
- Packs pequenos: mundo-trilhos 103M, aiatolah 80M, rail-post 53M, discover_brazil 50M (06/08)

### Tencent 43.156.151.165 — 118G: 72G usado (64%), 42G livre
- `/root` = 29G: `backups/` **9,2G** · `venv` 7,6G · `Legacy/` 3,9G · `.local` 2,8G · `.cache` 951M · `agent_data` 803M · `V3` 542M
- `backups/` detalhe: `midia/` 2,8G · **4× `banco_midia_andre_mendonca_*_20260626` 431M cada (~1,7G)** · `v3_pipeline_snapshots` 346M · `ruins_r2_backup_20260623` 324M · soltos: `banco_midia_ouro_v3_pre_reclassificacao_20260728.db`, `.bak_*` de scripts
- Verificado: `andre_mendonca` **NÃO consta** no espelho B2 `cingapura/backups` (lsl vazio) → espelhar antes de limpar

### Demais
- **159.65.177.60** (espelho cafezinho.news): 77G, 16G usado (20%) — `/var/www` 7,2G. Saudável.
- **ServerDo cafezinho-wp**: SSH banner timeout da minha rota, mas **vigia mede 47–48%** — saudável. Reboot diário 03:31 conhecido.
- **174.138.36.31** (riocarta-wp legado): SSH timeout — morto (confirmado mapa 06/08).
- **159.89.237.100** (GSN WP zumbi): `Permission denied` (sem chave) — zumbi pago, decisão pendente do Miguel.

## Vigia de discos (cron :42) — última medição ao vivo
```json
{"NYC-failover (producao V4)": 79, "Rio-Carta-Agentes (satelites)": 87, "Espelho cafezinho.news": 20, "Tencent (paineis+Moka)": 64, "ServerDo WP Cafezinho": 48, "Central de Alertas (eu)": 38}
```
Alertas enviados: 0 nas últimas linhas do log (threshold 🟠85 — rio-ag 87% deveria ter apitado; verificar lógica de dedupe/threshold no `vigia_discos.py` na implementação).

## Buckets B2 mapeados (rclone local)
| Remote | Bucket | Conteúdo |
|---|---|---|
| `b2:` / `masterb2:` | `failover-cafezinho1` | principal: `/faxina` (06/08), `/backups`, `/cingapura` (espelho Tencent), `/criticos`, `/Cerebro_Backups`, `/livro-filhos-da-impunidade`… |
| `b2-tematicos:` | `site-tematicos` | só `/backups` |
| `b2_orlando:` | `Orlando-Diniz-Dossie` | dossiê |
| `b2-labs:` / `gdrive-backup-b2:` | vários | Agents-Labs, Backup-GoogleDrive-Miguel, Cafezinho-operacional, Cerebro-Memorias, Legacy-Cafezinho, Cafezinho-pos-grande-reforma-jun2026 |
| NYC remotes | `b2:`, `cafezinho_operacional:`, `legacy-cafezinho:`, `reforma_tencent_cafezinho:` | — |

**Bucket novo do Miguel (criado hoje, "só pro DO")**: ainda não aparece nos remotes rclone locais → confirmar nome + configurar chave no cofre/servers na implementação.

## Cruzamento com o que já existe
- **Coberto (não duplicar):** 8 bancos sqlite V4 → archiver diário 04:35 BRT (instalado hoje pela sessão Qwen, `--authorization-ref MIGUEL-20260807-CRON-DIARIO`).
- **Não coberto (escopo deste plano):** caches, logs/jsonl, backups locais históricos, git packs, journald, `.bak_*`, `.used_*`.
