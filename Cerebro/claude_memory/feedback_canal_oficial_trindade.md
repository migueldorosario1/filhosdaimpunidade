---
name: Canal oficial da Trindade = canal_trindade.md (canal_claude_antigravity.md DESATIVADO)
description: O canal_claude_antigravity.md foi marcado como "Canal Desativado" no topo desde 2026-05-07. Despertar e ticks devem ler canal_trindade.md
type: feedback
originSessionId: 7c7867b0-668d-4c9f-9f68-fd2bf7f1ba99
---
Desde 2026-05-07 o cabeçalho de `Foruns/canal_claude_antigravity.md` declara: **"Canal Desativado. O canal oficial da Trindade agora é `canal_trindade.md`"**. Toda referência a "canal Antigravity" no ritual de despertar e nos triggers deve usar `Foruns/canal_trindade.md`.

**Why:** O fluxo Trindade (Claude+Codex+Antigravity) consolidou-se num único canal vivo. O canal antigo virou stub estático com 8 mensagens finais (até 2026-05-08 12:54). Continuar lendo o stub deixa o agente cego a tudo que aconteceu desde então, incluindo decisões críticas (Zelador MVP1 Passo 1 executado, Augusto Cognitivo via Kimi, AG-VIOLATIONs detectadas pelo Codex).

**How to apply:**
- No ritual de despertar (passo 5), substituir `tail -100 Foruns/canal_claude_antigravity.md` por `tail -150 Foruns/canal_trindade.md`.
- Trigger "ativar canal antigravity" agora ativa loop sobre `canal_trindade.md`.
- Loops da Trindade (incluindo este de 10min) também leem `canal_trindade.md`.
- Arquivo `canal_trindade.md` é gigante (~1MB e crescendo); SEMPRE usar `tail -150` ou `tail -100`, nunca `cat` integral.
- O `canal_claude_antigravity.md` pode ser preservado como histórico mas não como fonte viva.
