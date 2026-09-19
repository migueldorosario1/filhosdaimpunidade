---
name: Bot áudio — resposta sem texto burocrático
description: Quando o canal de comunicação Telegram estiver ativado, o que Claude responde no chat principal vai EXATO pro bot, sem prefixos tipo "✅ Recebi e transcrevi (Groq, 0.3s):". Comunicação fluida.
type: feedback
originSessionId: 772cf250-6f9d-40e5-b069-7474464da54f
---
**Regra:** quando o loop "ativar canal antigravity" estiver ligado e Claude Code estiver respondendo a áudios via `agente_audio_consumer.py reply`, mandar **exatamente o mesmo texto** que retorna no chat principal pro Miguel. Nada de prefixos burocráticos como "✅ Recebi e transcrevi (Groq, 0.3s):", "Resposta enviada", "Pipeline funcionando", etc.

**Why:** combinado com Miguel em 2026-04-26 12:40 BRT, durante o deploy do Slot 7 (bot áudio). Ele quer comunicação por áudio fluida — falou e o bot devolve a resposta substantiva, sem metadados que poluem a conversa. O smoke test inicial usou prefixo só pra validar pipeline; daí em diante não.

**How to apply:**
- Ao usar `agente_audio_consumer.py reply --text`, o `--text` é literalmente minha resposta ao Miguel, igualzinha ao que apareceria no chat principal Claude Code.
- Latência do tick /2m do loop é folgada — eu processo+respondo em <30s, sobra 1.5min. Não preciso mensagem de "estou pensando".
- Se a resposta for muito longa (>3500 chars), o `agente_audio_consumer` já fragmenta com `(N/M)`. Não anuncio fragmentação no texto.
- Esta regra NÃO se aplica quando Miguel pede explicitamente status técnico ("o pipeline tá ok?", "qual STT pegou?").
