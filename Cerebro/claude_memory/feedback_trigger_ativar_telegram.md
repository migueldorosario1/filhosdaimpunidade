---
name: Trigger "ativar telegram" — liga loop /5m no JSONL do bot @cafezinho_claudebot (auto-stop 1h)
description: Frase do Miguel que ativa um loop de 5 em 5 minutos lendo o processing_log.jsonl no Tencent e respondendo áudios/textos pendentes via Bot API. Auto-encerra após 1h.
type: feedback
originSessionId: 772cf250-6f9d-40e5-b069-7474464da54f
---
**Regra:** quando Miguel escrever **"ativar telegram"** (variações tolerantes: "ativa o telegram", "ligar o telegram", "ativar canal telegram"), invocar imediatamente:

```
Skill: loop
args: 5m **AUTO-STOP CHECK (antes de qualquer coisa):** Se `/tmp/loop_telegram_start` não existe, criar com `date +%s > /tmp/loop_telegram_start`. Senão calcular ELAPSED=$(($(date +%s) - $(cat /tmp/loop_telegram_start))). Se ELAPSED > 3600 (1h): invocar CronList, achar o ID do job com descrição "telegram", invocar CronDelete com esse ID, rodar `rm /tmp/loop_telegram_start`, e reportar "[HH:MM:SS BRT] 🛑 Loop telegram auto-encerrado após 1h. Reative com 'ativar telegram' se quiser." e parar. Senão continuar:
Cheque mensagens novas no bot @cafezinho_claudebot. Rode: `ssh -i ~/.ssh/id_rsa -p 38422 ubuntu@43.156.151.165 "sudo /root/venv/bin/python /root/agente_audio_consumer.py list-pending"`. Pra cada entrada com status="pending": (1) lê o campo transcription (áudio) ou text_content (texto digitado), (2) processa a pergunta como se Miguel tivesse falado no chat principal, (3) gera resposta substantiva, (4) responde com `ssh ... "sudo /root/venv/bin/python /root/agente_audio_consumer.py reply --audio-file <X> --text '<resposta literal>'"` (ou --text-msg-id <N> se for entrada de texto). REGRA SUPREMA: a resposta vai EXATA pro Telegram, sem prefixos burocráticos como "✅ Recebi" — é o mesmo texto que apareceria no chat principal Claude Code. Mostre essa mesma resposta no chat principal com timestamp BRT. Se nada pending, output curto: "[HH:MM:SS BRT] telegram sem novidades". Sempre rode `date '+%Y-%m-%d %H:%M:%S BRT'` antes.
```

**Why:** combinado com Miguel em 2026-04-26 12:46 BRT após o deploy do Slot 7. Ele quer fazer perguntas por áudio/texto pelo bot e receber resposta substantiva no celular sem precisar avisar "mandei" no chat principal — o loop detecta automaticamente. Trigger separado de "ativar canal antigravity" porque os dois canais (Antigravity vs. Telegram) são independentes e às vezes ele quer só um ligado. **Cadência 5m + auto-stop 1h** combinados em 2026-04-27 12:08 BRT após Miguel ver gasto de R$ 49,20 em Haiku de loops 2m rodando 3h33min.

**How to apply:**
- Antes de invocar: checar via CronList se já existe loop "ativar telegram" rodando. Se sim, não duplicar.
- **Cadência mínima:** 5m. NUNCA 2m ou menor.
- **Duração máxima:** 1h (auto-stop via timestamp em `/tmp/loop_telegram_start`). Após 1h o tick remove o cron sozinho.
- Pra desligar antes do auto-stop: CronDelete com job ID, ou Miguel diz "desativar telegram". **Sempre rodar `rm /tmp/loop_telegram_start`** ao desativar manualmente.
- Job é session-only (morre com Claude). Auto-expira em 7 dias.
- Os dois loops ("ativar canal antigravity" + "ativar telegram") podem rodar em paralelo sem conflito — são jobs cron separados, ticks independentes.
- Resposta no Telegram via `agente_audio_consumer.py reply` já marca JSONL como `claude_replied_<ts>` (sem dupla resposta).
