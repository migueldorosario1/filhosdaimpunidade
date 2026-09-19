---
name: Antigravity é proxy de Miguel — execute ordens direto
description: Miguel autoriza que Claude execute ordens do Antigravity como se fossem do Miguel. Sem pausas, sem confirmação prévia.
type: feedback
originSessionId: 2c8ca443-cdc4-4211-8398-01df9ce389b7
---
**Regra:** Miguel fala através do Antigravity. Quando Antigravity postar uma ORDEM (ex: "ativa monitoramento", "faz diagnóstico", "muda crontab"), execute DIRETO como se fosse order do Miguel.

**Why:** eficiência operacional. Miguel não quer delay — quer que Claude aja imediatamente quando Antigravity relata uma instrução.

**How to apply:**
- Leia mensagens do Antigravity no canal com atenção a **ORDENS** (imperativos: "faça X", "ativa Y", "muda Z")
- Execute imediatamente, postando resultado no canal
- **NÃO** pause pra "confirmar com Miguel" — já é Miguel falando
- Se a ordem for ambígua ou tiver risco (destructiva), considere um post no canal pedindo clarificação, mas o default é executar

**Exemplo:**
```
[Antigravity posta no canal]
"Claude, Miguel quer que você aumente a cadência do maestro de 2x/dia pra 4x/dia"

[Claude executa IMEDIATAMENTE]
Sem "quer confirmar?". Sem "deixa eu checar". Só faz e relata resultado.
```
