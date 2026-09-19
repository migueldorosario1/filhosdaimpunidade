---
name: Arquitetura final do Agente YouTube (RSS primário + Brave fallback)
description: RSS oficial é o caminho principal (cron 25 * * * *), Brave é fallback (0 */2 * * *); histórico unificado em youtube_vistos.json.
type: project
originSessionId: b8d23953-06f2-4699-9a68-275c279163e9
---
**Arquitetura pós-deploy 2026-04-17 11:07:**

- **RSS primário**: `agente_youtube.py` (modo `monitorar_canais()` sem args) — cron `25 * * * *`, usa feed oficial `youtube.com/feeds/videos.xml?channel_id=...`, respeita `"ativo": true` no JSON. Log: `/root/agent_data/youtube.log`.
- **Brave fallback**: `robo_patrulha_youtube.py` — cron `0 */2 * * *`, busca `site:youtube.com "<nome>"` no Brave com `freshness=pd`, filtra vídeos por `channelId` real (baixa HTML). Log: `/root/agent_data/patrulha_youtube.log`.
- **Histórico unificado**: ambos escrevem e leem em `/root/agent_data/youtube_vistos.json` (63 IDs pré-populados no deploy pra bloquear backlog).

**Whitelist atual (4 canais de geopolítica gringos):**
- Judging Freedom `UCDkEYb-TXJVWLvOokshtlsw`
- Glenn Diesen `UCZFCDIHTe9HGxtIuVDpBz7g`
- Dialogue Works `UCkF-6h_Zgf9zXNUmUB-MzTw`
- Daniel Davis / Deep Dive `UCWDN5zr5ttctoIAhZwW6tcQ`

**Pipeline compartilhado `gerar_materia_yt(url)`:**
1. Transcrição: `YouTubeTranscriptApi().fetch(video_id, languages=['pt','pt-BR'])` (API v1.x, `.text` nos snippets) → fallback Transkriptor (token hardcoded no script)
2. Memória anti-repetição: lê últimas 3 entradas de `memoria_youtube.jsonl` e injeta no prompt do Redator
3. Editor → Redator (800 palavras HTML, padrão FT) → Revisor (higiene), via `agente_roteador_llm.router_gen`
4. Editor retorna `resumo_seo` (≤155 chars); gravado como `excerpt` e `_yoast_wpseo_metadesc` no post WP
5. Título passa por `titulo_utils.corrigir_capitalizacao_titulo`
6. Thumb `maxresdefault.jpg` → fallback `hqdefault.jpg`
7. Publica `status='publish'` (direto, apesar do print dizer "Rascunho")
8. Append em `memoria_youtube.jsonl` + ping Google Indexing via `indexador_google.notificar_google` (requer `agent_data/indexing_key.json`)
9. Notifica Augusto Bot

**Why:** Antes, o YouTube só funcionava via Brave porque os channel_ids no JSON estavam truncados (22 chars em vez de 24) — o Miguel nunca tinha testado RSS com IDs válidos. RSS oficial é gratuito, sem quota, mais rápido. Brave só socorre se RSS falhar.

**How to apply:** Quando o Miguel pedir pra adicionar canal, só mexer no JSON (com `channel_id` válido de 24 chars e `"ativo": true`). Se pedir pra pausar um canal, setar `"ativo": false` desliga só o RSS — Brave continua. Pra desligar tudo, deletar a linha do JSON ou comentar o cron do robo_patrulha.
