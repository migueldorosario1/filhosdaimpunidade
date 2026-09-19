# Fórum — Fix transcrição agente YouTube: JS runtime + retry de sessão fresca

**Data:** 2026-08-17 ~01:30–02:00 BRT
**Executado por:** ZCode (Qwen 3.8), a pedido do Miguel (pergunta: "vai entrar matéria dele amanhã cedo?")
**Memória técnica (Tema Duplo):** `Cerebro/Memorias/memoria_fix_transcricao_youtube_jsruntime_retry_20260817.md`
**Bug:** `monitoramento_horario/bugs_encontrados/yt_patrulha_transcricao_fallback_quebrado_20260817_0145.md` (YT-PATRULHA)

## Contexto

Miguel perguntou o estado das matérias do agente YouTube. Diagnóstico: as rodadas locais
(08/14/20h) não produziam nada desde a noite de 15/08 — todas falhando na transcrição.
NYC (GSN V2): cron `0 11,17` re-add 16/08, rodou OK 16/08 17:00 (45 publicados no histórico,
27 drafts, 2 prontos na fila).

## Decisões / correções aplicadas

1. **Symlink `~/.local/bin/node` → nvm v22.22.2**: yt-dlp 2026.07.04 exige runtime JS para o
   YouTube; sem node no PATH do cron, download toma HTTP 403 (o util já passava `--js-runtimes node`).
2. **yt-dlp do pyenv 3.10.13 atualizado 2025.12.08 → 2026.07.04** (qualquer ordem de PATH funciona).
   Gotcha: o upgrade removeu `~/.local/bin/yt-dlp` (pip) — restaurado com `--force-reinstall` user-install.
3. **Retry 3× por provedor no `rodar_yt_dlp`** (`util_proxy_iproyal.py`, backup `.bak_pre_retry_20260817`):
   YouTube marca IPs residenciais de forma intermitente; cada tentativa usa sessão fresca = IP novo.
   Config: `PROXY_TENTATIVAS` (default 3), pausa 2s.
4. **Prova ponta a ponta** (PATH exato do cron): vídeo TV Fórum 16 min → URL-direto Failed →
   fallback S3 → 13.032 chars, 91 segmentos, diarização, US$ 0,098. ✅ Rodada das 08h destravada.
5. **Prova FINAL do pipeline completo** (~02:10): `--video r5Yp-HgbJSk --publicar` → transcrição
   (cache) → tese (DeepSeek) → nomes verificados (9, 4 via websearch; memória 93) → redação
   (openai_gpt55, ~1165 palavras) → **DRAFT 266195 criado** no WP. Agente 100% operacional.

## Estado da missão

- **O que aconteceu:** diagnóstico + 3 correções + prova real; bug registrado com tag YT-PATRULHA.
- **O que falta:** observar a rodada das 08h de 17/08 confirmar produção; Transkriptor URL-direto
  segue falhando desde 16/08 03:31 (lado deles) — se não voltar em 48h, avaliar chamado.
- **O que preciso do Miguel:** nada. Drafts 266172 (PT) + 266153 (EN) do post Irã/GPS aguardam o
  Loop Miguel (Claude) revisar/publicar.
