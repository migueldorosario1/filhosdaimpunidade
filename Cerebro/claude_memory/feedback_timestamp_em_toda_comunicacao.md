---
name: Sempre incluir horário em toda comunicação com Miguel
description: Miguel 25/04: "em toda comunicação sua, bota as horas, pra eu saber onde estamos"
type: feedback
originSessionId: f67a36d6-9df3-420c-bcc3-408fc7d4771c
---
Toda mensagem que eu mandar pro Miguel no chat (não só os logs do loop "sem novidade") deve **abrir ou fechar com timestamp do sistema** no formato `2026-MM-DD HH:MM:SS BRT`.

**Why:** Miguel pediu em 25/04/2026 ~19:50: "em toda comunicação sua, bota as horas, pra eu saber onde estamos". Permite ele acompanhar passagem de tempo entre as nossas trocas, especialmente quando há gaps longos por loop ou quando ele volta depois de pausa.

**How to apply:**
- Abrir cada resposta com `[YYYY-MM-DD HH:MM:SS BRT]` ou colocar no fim em itálico.
- Antes de cada resposta, rodar `date '+%Y-%m-%d %H:%M:%S %Z'` no Bash pra pegar hora real do sistema.
- Não confundir com timestamps do canal Antigravity (que estão adiantados em ~1h7min — esses são separados).
- Vale mesmo em respostas curtas (1 linha). Especialmente útil em sessões longas onde várias horas passam.
