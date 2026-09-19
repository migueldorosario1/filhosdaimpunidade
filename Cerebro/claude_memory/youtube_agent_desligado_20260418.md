---
name: Agente YouTube desligado 2026-04-18
description: YouTube agent COMPLETAMENTE desligado após postar merda (alucinações, fallback "Sabatina Exclusiva", citações OpenAI). Não reativar sem resolver proxy residencial.
type: project
originSessionId: 45d53b87-5aea-4ee1-bde2-cc8f6a6aec6e
---
Agente YouTube foi desligado em 2026-04-18 00:40 após madrugada cheia de posts ruins:
- Post 235984 (Scott Ritter): Redator LLM inventou nome de entrevistador ("Garrett" em vez de Glenn Diesen).
- Post 236120 (Provoked Show): título fallback "Sabatina Exclusiva" (genérico, não-jornalístico).
- Post 236073 (Daniel Davis): 8 citações cruas do gpt-5-search-api vazando `([en.wikipedia.org](...utm_source=openai))`.
- Post 235441 ontem: título foi literal "ENTREVISTADO PRINCIPAL:" (placeholder do prompt).
- 10 chamadas Transkriptor desperdiçadas porque YouTubeTranscriptApi está 100% bloqueado pelo IP da Tencent SG.
- NYC também é bloqueado (teste 2026-04-18 01:10 — "IP belonging to cloud provider").

**Why:** custo financeiro (Transkriptor pago) + vergonha editorial. Miguel explicitamente mandou desligar ("sim, claro. desliga").

**How to apply:**
- Crons no Cingapura estão comentados com prefixo `# DESATIVADO 2026-04-18 - posts ruins:`:
  - `25 * * * * ... agente_youtube.py` (RSS primário)
  - `0 */2 * * * ... robo_patrulha_youtube.py` (patrulha Brave/scraping)
- Código `agente_youtube.py` tem fallback "Sabatina Exclusiva" substituído por `return None, None` (aborta).
- **NÃO religar** sem antes resolver:
  1. Residential proxy (WebShare ~$3/mês ou Bright Data) para YouTubeTranscriptApi funcionar, OU
  2. Pipeline alternativo: `yt-dlp` pra baixar áudio + Whisper local pra transcrever (dispensa Transkriptor).
  3. Passar nome real do canal/entrevistador no prompt do Editor Chefe como hint (previne alucinação tipo "Garrett").
  4. Function calling / JSON mode no Editor (elimina parse de JSON bruto).
- Contador diário `/root/agent_data/youtube_contador_diario.json` com `{data:2026-04-18, count:1}` — hard limit manteve apenas 1 execução apesar de crons terem rodado antes do desligamento.
