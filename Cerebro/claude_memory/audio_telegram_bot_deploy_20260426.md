---
name: Bot Telegram áudio Cafezinho — deploy 2026-04-26
description: Pipeline bidirecional Miguel↔Claude via @cafezinho_claudebot. Recebe áudio → cascata STT 4 níveis → Claude lê JSONL e responde via Bot API. Deploy concluído 12:40 BRT.
type: project
originSessionId: 772cf250-6f9d-40e5-b069-7474464da54f
---
## O que foi entregue (Slot 7, 2026-04-26)

Bot Telegram bidirecional pra Miguel mandar áudio do celular e Claude Code responder pelo mesmo canal.

### Arquivos no Tencent (`/root/`)
- `bot_audio_input.py` (204 linhas) — long-polling Telegram, filtra `chat_id=1894890759`, dedupe por `telegram_message_id`, salva OGG + JSONL atômico (flock)
- `agente_audio_monitor.py` (379 linhas) — daemon polling 3s, cascata STT **Groq → xAI Scribe v2 → OpenAI Whisper → Transkriptor (com util_cost_guard)**, logrotate por tamanho 10MB, notificação proativa via Bot API quando cascata inteira falha
- `agente_audio_consumer.py` (192 linhas) — CLI utility: `list-pending`, `reply --audio-file X --text Y`, `mark-read`, `send-message`. Fragmenta resposta em chunks de 3500 chars com sufixo `(N/M)`
- `start_audio_pipeline.sh` — wrapper idempotente (`pkill || true; sleep 1; nohup ... &`) usado no `@reboot` e nos 2 keepalives
- `/root/audio_uploads/` — pasta de áudios + `processing_log.jsonl`

### Crontab deployado (3 linhas)
```
@reboot /root/start_audio_pipeline.sh > /root/start_audio_pipeline.log 2>&1
*/5 * * * * pgrep -f bot_audio_input.py >/dev/null || /root/start_audio_pipeline.sh >> /root/start_audio_pipeline.log 2>&1
*/5 * * * * pgrep -f agente_audio_monitor.py >/dev/null || /root/start_audio_pipeline.sh >> /root/start_audio_pipeline.log 2>&1
```

### Chaves no `.env.unificado` (append em 2026-04-26 11:42)
- `TELEGRAM_AUDIO_BOT_TOKEN=8681428356:AAGcaGAjFMVAPNgdCawx3K6mHOhS3HxcUtM`
- `NOTIFICATION_CHAT_ID=1894890759` (mesmo chat_id do Augusto/admin_chat_id.txt)
- Reusa `GROQ_API_KEY`, `XAI_API_KEY`, `OPENAI_API_KEY`, `TRANSKRIPTOR_API_KEY` já existentes.

## Smoke test 2026-04-26 12:37 BRT (passou)
- Áudio 6s → bot baixou em 0.5s → monitor pegou em 1s → **Groq transcreveu em 0.3s** (1º nível da cascata) → JSONL `pending` → `agente_audio_consumer.py reply` mandou resposta → Telegram entregou (`message_id=4`) → JSONL `claude_replied`.
- **Latência total: ~4s do envio até a transcrição.**

## Convenção de uso (Miguel pediu 2026-04-26 12:40 BRT)
Quando o loop "ativar canal antigravity" estiver ligado, Claude Code responde via bot Telegram com **exatamente o mesmo texto** que retorna no chat principal — sem prefixos burocráticos tipo "✅ Recebi e transcrevi (Groq, 0.3s):". Comunicação fluida.

## Como usar (operacional)
- **Verificar fila pendente:** `ssh -p 38422 ubuntu@43.156.151.165 "sudo /root/venv/bin/python /root/agente_audio_consumer.py list-pending"`
- **Responder a um áudio:** `ssh ... "sudo /root/venv/bin/python /root/agente_audio_consumer.py reply --audio-file audio_<ts>.ogg --text 'sua resposta'"`
- **Logs:** `/root/bot_audio_input.log`, `/root/agente_audio_monitor.log`, `/root/start_audio_pipeline.log`

## Histórico de decisões (parecer Antigravity 2026-04-26 11:40 BRT, autorizado)
- Cascata STT: **Groq primeiro** (latência), xAI canônico como 2º, OpenAI rede, Transkriptor (caro+diarização) como último com cost_guard
- Supervisão: keepalive cron `*/5` em vez de systemd (coesão com infra)
- Dedupe por `telegram_message_id` (Telegram retenta se rede pisca)
- Conversão ffmpeg OGG→MP3 só pré-Transkriptor (lazy)
- Fragmentação 3500 chars em vez de PDF (UX)
- Logrotate por tamanho 10MB
- Notificação proativa em falha total da cascata

## Fórum de origem
`Foruns/forum_audio_telegram_bot.md` — desenho, conflitos com tutorial original, decisões §2, plano §3, parecer Antigravity §5.
