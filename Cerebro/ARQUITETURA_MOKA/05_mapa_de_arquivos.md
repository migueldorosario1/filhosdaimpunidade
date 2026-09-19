# 05 — Mapa de Arquivos (local × GitHub)

Base local: `/home/migueldorosario/Downloads/Antigravity Google/` (= `$AG`)

## Moka (aplicativo)

| O quê | Local | GitHub |
|---|---|---|
| Vídeos de marketing (bruto + legendados) | `$AG/moka/marketing/` | (sem repo ainda) |
| API de pontos | `$AG/moka/pontos_api/app.py` | (sem repo ainda) |
| Schema | `$AG/Projeto Cafezinho Agentes/Foruns/moka_pontos_schema_v1.sql` | — |
| Plano de negócios | `$AG/Cerebro/PLANO_NEGOCIOS_MOKA/` | — |

## Agentes V4 (motor dos sites)

| O quê | Local | GitHub |
|---|---|---|
| Coletor/Produtor/Publicador/YouTube | `$AG/agentes_tematicos/v4/*.py` | (sem repo ainda) |
| Núcleo (llm, visão, imagem, telegram, storage, dedup, frontmatter, config) | `$AG/agentes_tematicos/v4/nucleo_*.py` | — |
| 40 wrappers por site | `$AG/agentes_tematicos/v4/<site>_<agente>.py` | — |
| Agente YouTube Cafezinho | `$AG/Projeto Cafezinho Agentes/agentes_cafezinho/youtube_cafezinho.py` | — |

## Configs e diretrizes (documento vivo)

| O quê | Local |
|---|---|
| Configs dos 8 sites | `$AG/agent_data/configs/<site>.json` |
| Contratos editoriais | `$AG/agent_data/contratos/<site>.md` |
| Canais YouTube Cafezinho | `$AG/agent_data/canais_cafezinho_youtube.json` |
| Curadoria Cafezinho | `$AG/agent_data/curadoria_cafezinho_youtube.json` |
| Blocklist de imagens | `$AG/agent_data/hero_blocklist.txt` |
| Bancos bruto/auditado | `$AG/agent_data/v4/<site>/{bruto,auditado}.jsonl` |

## Sites (repos de produção)

| Site | Local (`sites-v4/`) | GitHub (público) |
|---|---|---|
| Rio Carta | `…/sites-v4/riocarta` | `github.com/migueldorosario1/riocarta-v4` |
| GSN | `…/sites-v4/globalsouth` | `…/globalsouth-v4` |
| Mundo Trilhos | `…/sites-v4/mundotrilhos` | `…/mundotrilhos-v4` |
| Rail Post | `…/sites-v4/railpost` | `…/railpost-v4` |
| Discover Brazil | `…/sites-v4/discoverbrazil` | `…/discoverbrazil-v4` |
| Mapa Rio (pausado) | `…/sites-v4/mapario` | `…/mapario-v4` |
| Ceará Digital | `…/sites-v4/ceara` | `…/ceara-v4` |
| AIatolah | `…/sites-v4/aiatolah` | `…/aiatolah-v4` |

**Repos antigos congelados** (arquivo histórico): `migueldorosario1/{rio-carta, global-south-news, mundo-trilhos, rail-post, discover-brazil, mapario, ceara-digital, aiatolah}`

## Backups

| O quê | Local |
|---|---|
| Backup pré-refatoração (bundles+checksums) | `$AG/Backups/refatoracao_v4_tematicos_20260720_171637/` |
| Crontabs históricos | idem (`crontab_antes_*.txt`) |
| Reforma arquivos (dados frios) | `~/Dados_Frios/` (+ `~/bin/backup_semana_gdrive.sh`) |

## Cérebro

| O quê | Local |
|---|---|
| Índice mestre | `$AG/Cerebro/CEREBRO_INDEX_MASTER.md` |
| Plano de negócios | `$AG/Cerebro/PLANO_NEGOCIOS_MOKA/` |
| Arquitetura (este) | `$AG/Cerebro/ARQUITETURA_MOKA/` |
| Reforma de arquivos | `$AG/Cerebro/CEREBRO_INDEX_REFORMA_ARQUIVOS_20260722.md` |

## Vídeos de marketing no R2 (Cloudflare)

| Vídeo | URL pública (R2) |
|---|---|
| Anúncio principal (BBC, 4min07) | `https://pub-7c53d388419e4d44b17eace540ae7e22.r2.dev/moka/anuncio/moka_anuncio_bbc.mp4` |
| Corte 60s (TikTok/Reels) | `https://pub-7c53d388419e4d44b17eace540ae7e22.r2.dev/moka/anuncio/moka_anuncio_60s.mp4` |

Bucket: `R2_BUCKET` (creds em `.env.unificado`: R2_ACCESS_KEY/R2_SECRET_KEY/R2_ENDPOINT/R2_PUBLIC_URL). Upload feito em 23/07 via boto3.
