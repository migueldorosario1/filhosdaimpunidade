# Fórum — PLANO: Faxina Contínua Autônoma dos Discos (varredura 07/08 + proposta)

> [!CAUTION]
> **OVERRIDE CANÔNICO DE 11/08/2026:** a autonomia destrutiva proposta abaixo está superada. Com 15 dias ou menos de inatividade, nada pode ser tratado como lixo; depois de mais de 15 dias, o item é apenas elegível para consulta e qualquer movimentação ou descarte exige autorização explícita de Miguel. Tudo deve ser indexado item por item antes da ação. Ver `Memorias/memoria_missao_faxina_diaria_legacy_20260811.md`.

> **Data:** 2026-08-07 ~11:20 BRT · **Autor:** Kimi K3 / ZCode · **Status:** 🟢 MISSÃO DIÁRIA REATIVADA POR MIGUEL EM 11/08/2026
> **Memória (censo técnico completo):** `Memorias/memoria_plano_faxina_continua_droplets_20260807.md`
> **Ordem do Miguel (voz, ~11:05):** "faz uma varredura em todo o sistema, vê se tem arquivo crescendo indefinidamente sem autolimpeza — evidentemente vai dar problema. O DO já tá quase cheio. Tem que levar pro Backblaze (criei um bucket novo; já tem o dos temáticos). Sistema automático/autônomo de backup + limpeza, droplets de NY bem enxutos o tempo inteiro, sem precisar de mim, usando telemetria. Pensa num plano primeiro."

> **Nova ordem de 11/08/2026:** fazer uma auditoria diária para identificar legacy no local e nos servidores. Retirada só entra em pauta depois de mais de 15 dias de inatividade comprovada, indexação integral e consulta explícita a Miguel; Backblaze, verificação e rollback continuam obrigatórios após a autorização.

## 1. Diagnóstico (censo read-only 07/08 ~11:10 BRT)

| Servidor | Disco | Status | O que cresce sem limpeza |
|---|---|---|---|
| **rio-ag** 159.89.185.209 (satélites) | 21G/24G = **87%** | 🟠 | git packs: riocarta **2,5G** + cicero **2,4G** + gsn **1,4G** (heroes versionados, crescem a cada push); `.npm` **1,1G** (cache descartável); `ceara_publication_audit.jsonl` **214MB** |
| **NYC** 198.199.121.136 (produção V4) | 38G/48G = **79%** | 🟡 | `.cache/pip` **4,2G** + puppeteer 627M (descartáveis); `backups/` **1,2G** (73 pastas históricas, fora do B2); `log_rotas_llm.jsonl` 167MB; `gsn_hourly_cron.log` **143MB**; `robo_coleta_*.log` ×4 ~40MB; `banco_custos_*.jsonl` ~34–56MB/mês; 797× `briefing_execucao.json.used_*` |
| **Tencent** 43.156.151.165 | 72G/118G = **64%** | 🟡 | `backups/` **9,2G** (midia 2,8G + 4× `andre_mendonca` 431M cada de 26/06 + snapshots) — **não estão no B2**; `Legacy/` 3,9G |
| ServerDo (cafezinho-wp) | 47% (via vigia) | 🟢 | fora da varredura SSH (banner timeout), vigia monitora |
| Espelho 159.65.177.60 | 20% | 🟢 | `/var/www` 7,2G (WP, cresce devagar) |
| Droplet-util 142.93.48.252 | 38% | 🟢 | journald 487MB (limitar) |
| 174.138.36.31 (riocarta-wp legado) | — | ⚫ | inacessível (morto) — decisão pendente |
| 159.89.237.100 (GSN WP zumbi) | — | ⚫ | sem chave — zumbi pago, decisão pendente |

## 2. Classes de crescimento (o que o archiver V4 NÃO cobre — ele só cuida dos 8 bancos sqlite)

- **A. Caches descartáveis** (não precisam de backup): pip 4,2G (NYC), npm 1,1G (rio-ag), puppeteer/whisper ~770M
- **B. Logs/jsonl crescentes**: gsn_hourly_cron 143MB, robo_coleta ×4, log_rotas_llm 167MB, banco_custos mensais, audit cicero 214MB, eleicoes 32MB
- **C. Backups locais históricos fora do B2**: Tencent 9,2G, NYC 1,2G, `.bak_*` espalhados (ex.: 60MB banco_imagens)
- **D. Git packs com imagens versionadas**: 6,3G no rio-ag, 1,5G no NYC — `git gc` periódico (compacta, não perde conteúdo)
- **E. journald**: droplet 487MB — limitar `SystemMaxUse`

## 3. O que já existe (não reinventar)

- **Archiver V4** (`v4_regional_db_archiver.py`, cron diário 04:35 BRT nos 8 bancos) — bancos cobertos desde hoje
- **Vigia de discos** (cron :42, droplet) — telemetria viva dos 6 servidores, 🟠85/🔴95 → Telegram
- **rclone + B2**: `failover-cafezinho1/faxina/` (usado 06/08), `site-tematicos`, + bucket novo que o Miguel criou (nome a confirmar)
- **Regra de ouro da faxina (06/08)**: indexar → B2 → verificar → apagar. E **§115**: nenhum arquivo cresce indefinidamente

## 4. Proposta — "Faxina Contínua" (3 peças)

1. **`faxina_continua.py`** — 1 script genérico por servidor, cron diário, política declarativa (JSON) por classe de alvo. Classe A: purge direto. Classes B/C: copiar p/ B2 → **verificar tamanho/contagem** → só então truncar/apagar local. Falha na verificação = não toca + alerta. Cada corrida grava relatório jsonl.
2. **Telemetria reativa**: vigia :42 ganha gatilho — servidor cruzar 🟠85% → dispara faxina extra na hora (fora do cron); 🔴95% → faxina emergencial + Telegram.
3. **Fases**: **Shadow** (semana 1: roda diário só relatando o que faria — zero ação) → **Canário** (semana 2: só classe A + journald, 1 servidor) → **Pleno** (semana 3+: tudo, todos os servidores acessíveis).

## 5. Organização B2 proposta

`failover-cafezinho1/faxina/<servidor>/<classe>/<aaaa-mm>/` (ou o bucket novo do Miguel como raiz — **decisão 1**). Logs gzipados, retenção local 30 dias, B2 permanente (~20GB/ano ≈ US$0,12/mês — irrelevante). `site-tematicos` segue para os temáticos.

## 6. Faxina pontual IMEDIATA recomendada (antes do sistema, risco baixo)

- **rio-ag 87%→~70%**: purge npm (1,1G), audit 214MB → B2 + rotacionar, `git gc` nos 3 repos (−2 a −3G estimado)
- **NYC 79%→~70%**: purge pip (4,2G), backups/ 1,2G → B2 (verificar) + limpar
- **Tencent 64%→~56%**: backups/ 9,2G → B2 (verificar, ainda não espelhados) + limpar
- Sempre com a regra de ouro. ~15–18G recuperados sem perder nada.

## 7. Decisões que preciso do Miguel

1. **Bucket destino**: qual o nome do bucket novo? (ou uso `failover-cafezinho1/faxina/`)
2. **Autoriza a faxina pontual imediata** (item 6) nos 3 servidores?
3. **Retenção padrão**: logs 30d local + permanente no B2; caches purge semanal — OK?
4. **`git gc` semanal** nos repos dos servidores — OK? (compacta, não perde conteúdo)
5. Zumbis (174.138.36.31 morto, 237.100 sem chave): ficam FORA do faxineiro — decidir desligamento depois?
