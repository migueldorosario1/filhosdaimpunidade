---
name: Desencaixe de ~1h7min entre timestamps do canal e hora real
description: Descoberto 25/04 ~17:55 BRT — timestamps postados estavam adiantados em relação ao sistema
type: project
originSessionId: f67a36d6-9df3-420c-bcc3-408fc7d4771c
---
Em 2026-04-25 ~17:54:55 BRT (hora real do sistema, fuso -03 sem horário de verão), descobri que os timestamps que eu vinha postando no `Foruns/canal_claude_antigravity.md` estavam **adiantados em ~1h7min** em relação à hora real.

Exemplos: minha mensagem "19:02 BRT" foi feita quando o sistema marcava ~17:55 BRT.

**Why:** Provavelmente o Antigravity postou primeiro com timestamp em fuso diferente (talvez UTC+1 ou inventado) e eu sincronizei junto. O canal todo do dia 25/04 tem timestamps adiantados ~1h.

**How to apply:**
- Daqui pra frente, **sempre rodar `date '+%Y-%m-%d %H:%M:%S %Z'`** antes de postar timestamp no canal — não copiar o ritmo do Antigravity.
- Não tentar "corrigir" os timestamps antigos do canal — append-only é regra dura, e a sequência relativa entre mensagens já está clara pela ordem física.
- Se Miguel pedir auditoria temporal de algum evento, lembrar que mensagens do dia 25/04 estão ~1h7min adiantadas em relação à hora real do sistema.
- Quando Antigravity postar timestamp adiantado: tudo bem, ele faz o que faz; eu uso minha hora real e a sequência continua coerente pela ordem.
