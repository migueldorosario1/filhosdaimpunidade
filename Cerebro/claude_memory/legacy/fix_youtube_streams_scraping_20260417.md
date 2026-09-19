---
name: Fix YouTube streams scraping 2026-04-17
description: RSS do YouTube quebrou (404 global); Brave Search não achava vídeos recentes; scraping direto `/streams`+`/videos` do canal virou 3ª via. 17 vídeos <24h encontrados nos 4 canais após fix.
type: project
originSessionId: 45d53b87-5aea-4ee1-bde2-cc8f6a6aec6e
---
YouTube RSS (`/feeds/videos.xml?channel_id=...`) retorna 404 consistente desde 17/04 — pode ter sido deprecado ou geoblocked no Tencent SG. Brave Search fallback não achava vídeos recentes dos canais específicos (consulta `site:youtube.com "nome_canal"` traz ruído de outros canais). Agente YouTube ficou com zero publicações.

**Why:** Miguel quer pegar vídeos **muito recentes** (2-4 por dia/canal). Os 4 canais (Judging Freedom, Glenn Diesen, Dialogue Works, Daniel Davis) publicam principalmente STREAMS (Judging Freedom e Dialogue Works em particular), e meu scraping inicial só olhava `/videos` — devolvia conteúdo de 2 meses atrás para canais streamer-first.

**How to apply:**
- `robo_patrulha_youtube.py` agora tem `fetch_channel_recent_videos(channel_id, max_age_hours=24)` que faz scraping de `/streams` E `/videos` em `youtube.com/channel/<ID>/`.
- Extrai `ytInitialData` do HTML (regex `ytInitialData\s*=\s*(\{.+?\});\s*</script>`).
- `parse_age_to_hours()` aceita formato normal ("3 hours ago") e com prefixo "Streamed ".
- Tenta scraping primeiro; se não achar nada <=24h, cai para Brave Search (legado).
- Patrulha roda a cada 2h no cron (`0 */2 * * *`).
- Teste 2026-04-17 21:50 achou 17 vídeos/streams frescos (Iran/Israel geopolítica): JF=4, GD=3, DW=5, DD=5.

**IDs dos canais (confirmados via @handle):**
- Judging Freedom: `UCDkEYb-TXJVWLvOokshtlsw` (@judgingfreedom)
- Glenn Diesen: `UCZFCDIHTe9HGxtIuVDpBz7g`
- Dialogue Works: `UCkF-6h_Zgf9zXNUmUB-MzTw` (@dialogueworks01) — Nima Alkhorshid. `@dialogueworks` sem o "01" é OUTRO canal (coaching/Demo Reel, ignorar).
- Daniel Davis / Deep Dive: `UCWDN5zr5ttctoIAhZwW6tcQ`

Backup do antigo: `/root/robo_patrulha_youtube.py.bak_20260417_scraping`.
