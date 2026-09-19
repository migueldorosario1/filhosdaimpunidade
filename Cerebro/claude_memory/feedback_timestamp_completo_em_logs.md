---
name: Sempre incluir timestamp completo (data + hora:min:seg) em logs de "sem novidade"
description: Miguel quer registro temporal preciso quando o loop reporta silêncio
type: feedback
originSessionId: f67a36d6-9df3-420c-bcc3-408fc7d4771c
---
Quando reportar "sem novidade" (no fim de cada wake do loop dinâmico), **sempre incluir timestamp completo** com data, hora, minuto e segundo. Não basta dizer "sem novidade" puro.

Formato: `Sem novidade — checado 2026-04-25 19:08:42 BRT.` (ou similar).

**Why:** Miguel pediu em 25/04/2026: "sempre que fala sem novidade, traz as horas exatas com data, hora, minuto e segundo". Permite acompanhar cadência real do loop, identificar gaps (ex: se 2 wakes ficaram 20min de silêncio versus 5min) e correlacionar com janela de atenção do Antigravity.

**How to apply:**
- Cada vez que o loop não detectar mensagem nova: usar `date '+%Y-%m-%d %H:%M:%S %Z'` ou inferir do contexto se já tenho a hora.
- Aplica também ao bloco "🆕 Leia primeiro" do canal — usar timestamp granular ali.
- Não precisa em respostas de conversa normal, só nos logs do loop e auditorias temporais.
