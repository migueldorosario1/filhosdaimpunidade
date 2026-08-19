# YT-PATRULHA — Transcrição do agente YouTube quebrada desde 16/08 03:31 (RESOLVIDO 17/08 ~01:50)

**Tag:** YT-PATRULHA
**Achado por:** ZCode (Qwen 3.8), a pedido do Miguel ("vai entrar matéria dele amanhã cedo?")
**Status:** ✅ RESOLVIDO com prova ponta a ponta

## Sintoma

Rodadas do agente YouTube Cafezinho (08/14/20h) sem produzir nada desde 15/08 à noite:
`rodada: todos os candidatos da fila falharam`. Transkriptor URL-direto → `status=Failed`
em tudo desde 16/08 03:31 (último sucesso 15/08 20:36). O fallback yt-dlp/S3, que deveria
salvar, também morria.

## Causas (3, em cascata)

1. **`yt-dlp` fora do PATH do cron** → `[Errno 2] No such file or directory: 'yt-dlp'` nas rodadas de 16/08.
   Corrigido 16/08 (linha PATH no crontab, `.local/bin` primeiro) — mas o problema 2 mascarou.
2. **yt-dlp novo (2026.07.04) exige runtime JavaScript p/ YouTube** (`No supported JavaScript runtime`);
   sem isso, formats degradam e o download toma **HTTP 403**. O util já tinha `--js-runtimes node`,
   mas `node` não estava no PATH do cron (vive no nvm). Fix: **symlink `~/.local/bin/node`** (v22.22.2).
   Bônus: o yt-dlp velho do pyenv 3.10.13 (2025.12.08) foi atualizado p/ 2026.07.04 — e durante esse
   upgrade o script `~/.local/bin/yt-dlp` SUMIU (pip removeu); restaurado com `--force-reinstall` user-install.
3. **YouTube marca IPs residenciais intermitentemente** (`Sign in to confirm you're not a bot`):
   o mesmo download passou às 01:38 e tomou bot_check às 01:50. Fix: `rodar_yt_dlp` agora tenta
   **até 3× por provedor com sessão fresca** (IP de saída novo) — `PROXY_TENTATIVAS` (default 3),
   backup `.bak_pre_retry_20260817`.

## Prova (17/08 ~01:55, PATH exato do cron)

`r5Yp-HgbJSk` (TV Fórum, 16 min): URL-direto Failed → fallback S3 → **MP3 11 MB baixado → upload S3 →
Transkriptor Completed → 13.032 chars, 91 segmentos, diarização OK, US$ 0,098**.

## Ressalva aberta

Transkriptor **URL-direto segue falhando** (lado Transkriptor, desde 16/08 03:31 — todos os vídeos).
Hoje o S3 fallback é o caminho efetivo. Se URL-direto não voltar em 48h, abrir chamado/avaliar.

## Arquivos tocados

- `Projeto Cafezinho Agentes/agents_labs/youtube_v2/util_proxy_iproyal.py` (retry 3× sessão fresca; backup `.bak_pre_retry_20260817`)
- `~/.local/bin/node` (symlink nvm v22.22.2), `~/.local/bin/yt-dlp` (restaurado), yt-dlp pyenv 3.10.13 → 2026.07.04
- Tema Duplo: `Foruns/forum_fix_transcricao_youtube_jsruntime_retry_20260817.md` + memória de mesmo nome
