---
name: Fix Agente YouTube RSS 2026-04-17
description: Deploy do agente YouTube novo — RSS primário + Brave fallback + fix transcript API + histórico unificado.
type: project
originSessionId: b8d23953-06f2-4699-9a68-275c279163e9
---
Deploy 2026-04-17 11:07 BRT no servidor Tencent. Cinco correções empilhadas que impediam o agente YouTube de funcionar direito:

1. **channel_ids truncados** (22 chars em vez de 24) no `canais_youtube.json` — Opera Mundi `UCCd_Ff61MvUq5K2Lq5y_w` era inválido → RSS retornava 404. Substituído pelos 4 canais corretos (Judging Freedom, Glenn Diesen, Dialogue Works, Daniel Davis/Deep Dive).
2. **YouTubeTranscriptApi v1.x API**: o código usava `YouTubeTranscriptApi.get_transcript()` (removido). Trocado para `YouTubeTranscriptApi().fetch()` + `.text` nos snippets. Isso parou o fallback cego pro Transkriptor (que queimava crédito em todo vídeo com legenda PT-BR disponível).
3. **Histórico unificado**: `robo_patrulha_youtube.py` usava `yt_historico_patrulha.json` (separado). Trocado para `youtube_vistos.json` (mesmo do `monitorar_canais()`) — evita publicação duplicada entre RSS e Brave.
4. **`youtube_vistos.json` pré-populado** com 63 IDs (3 históricos Brave + 15 vídeos atuais de cada um dos 4 canais) pra impedir que o primeiro run do RSS publicasse o backlog inteiro.
5. **Cron atualizado**: RSS primário `25 * * * * agente_youtube.py`, Brave fallback mantido `0 */2 * * * robo_patrulha_youtube.py`. Ambos compartilham histórico.

**Why:** Antes do deploy, o sistema só tinha Brave funcional (RSS quebrado pelos IDs inválidos). Depois, o RSS passou a ser primário — gratuito, sem quota, rápido (200-400ms por canal). Brave virou plan B.

**How to apply:** Se pedirem pra monitorar canal novo, checar se o channel_id tem 24 chars (UC + 22). Se pedirem pra pausar um canal sem deletar, setar `"ativo": false` — desliga só o RSS, Brave ainda roda até deletar do JSON ou comentar o cron.
