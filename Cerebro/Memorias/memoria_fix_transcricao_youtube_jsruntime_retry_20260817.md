# Memória técnica — Fix transcrição agente YouTube (JS runtime + retry sessão fresca)

**Data:** 2026-08-17 ~01:30–02:00 BRT · **Agente:** ZCode (Qwen 3.8)
**Fórum:** `Foruns/forum_fix_transcricao_youtube_jsruntime_retry_20260817.md`

## Diagnóstico (linha do tempo)

- Último URL-direto OK: 15/08 20:36 (`EN_sf5ugzUI`). A partir de 16/08 03:31, TODOS `transkriptor_falhou`
  (stats `agent_data/youtube_transcript_stats.jsonl`, 196 eventos).
- cron.log das rodadas 16/08: `No such file or directory: 'yt-dlp'` (fallback S3 morto) →
  `rodada: todos os candidatos da fila falharam` (3 rodadas).
- jornal 16/08: Kimi 429 "account suspended" (antes do crédito do Miguel) + proxy bot_check.

## Cadeia de falhas e correções

| # | Falha | Correção |
|---|---|---|
| 1 | `yt-dlp` ausente no PATH do cron (rodadas 16/08) | linha `PATH=.local/bin:…` no crontab (já feita 16/08, LAB) |
| 2 | yt-dlp novo exige runtime JS p/ YouTube; sem isso 403 no download | symlink `~/.local/bin/node` → `~/.nvm/versions/node/v22.22.2/bin/node` (ffmpeg já em `/usr/bin`) |
| 3 | yt-dlp pyenv 3.10.13 velho (2025.12.08) | `python3 -m pip install -U yt-dlp` → 2026.07.04 |
| 4 | upgrade do item 3 removeu `~/.local/bin/yt-dlp` | `~/.pyenv/versions/3.11.15/bin/python3 -m pip install --user --force-reinstall yt-dlp` |
| 5 | YouTube bot_check intermitente em IP residencial (mesmo download passou às 01:38, falhou 01:50) | `rodar_yt_dlp` agora tenta até 3× por provedor, sessão fresca cada (IP novo); `PROXY_TENTATIVAS` default 3, pausa 2s |

## Comandos/provas

- Duração via proxy: `rodar_yt_dlp(["--print","duration", …])` rc=0 (4541s) em `qsKP3lec7Vg`.
- Download 403 sem JS runtime; rc=0 com `--js-runtimes node` + sessão fresca (11 MB mp3).
- Prova final (PATH exato do cron `.local/bin:/usr/local/bin:/usr/bin:/bin`), vídeo `r5Yp-HgbJSk`:
  URL-direto Failed → fallback S3 → **13.032 chars, 91 segmentos, diarização True, US$ 0,098**.
- Telemetria: `agent_data/v4_cafezinho_youtube/telemetria_proxy.jsonl` (retry multiplica tentativas por op).

## Gotchas

- `pip install -U yt-dlp` num pyenv pode REMOVER o script user-install de outro pyenv (`.local/bin`).
  Sempre conferir se o binário sobreviveu após upgrade.
- `which yt-dlp` interativo ≠ resolução no subprocess do cron (ordem de PATH diferente) — testar com o PATH real.
- Transkriptor URL-direto falhando em TUDO desde 16/08 03:31 = problema do lado Transkriptor;
  S3 fallback é o caminho efetivo por ora. Reavaliar em 48h (~19/08 02:00).

## Arquivos

- `Projeto Cafezinho Agentes/agents_labs/youtube_v2/util_proxy_iproyal.py` (patch retry; backup `.bak_pre_retry_20260817`)
- `~/.local/bin/node` (symlink novo), `~/.local/bin/yt-dlp` (restaurado), pyenv 3.10.13 yt-dlp 2026.07.04
