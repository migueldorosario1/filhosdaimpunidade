---
name: Atualizar canal + fóruns sem precisar pedir autorização a cada vez
description: Postar no canal e editar/abrir seções nos fóruns proativamente. Não perguntar "posso atualizar?" antes de cada edit no fórum.
type: feedback
originSessionId: f67a36d6-9df3-420c-bcc3-408fc7d4771c
---
Quando algo do Antigravity exige resposta, auditoria, direcionamento, OU quando há diagnóstico/decisão técnica que precisa ficar registrada, **postar no canal `Foruns/canal_claude_antigravity.md` E/OU abrir nova rodada/seção no fórum específico** sem perguntar antes a Miguel.

**Why:** Duas diretivas Miguel:
- 25/04/2026: "sempre atualiza o canal, não espera eu pedir. vai me facilitar".
- 26/04/2026 ~10:43 BRT: "não precisa me perguntar para atualizar o forum" — após eu ter perguntado se podia redigir Rodada 16 do `forum_failover.md`.

Ele acompanha pelo canal/fórum e ter que aprovar cada edit me trava. **Ele me autorizou autonomia operacional pra fóruns.** Eu coordeno, escrevo, ele lê.

**How to apply:**
- Ao auditar entrega do Antigravity (código, tabela, design doc), postar veredito no canal + nova seção no fórum **antes** de relatar pro Miguel.
- Ao abrir nova fase/etapa/TASK, postar AGORA no canal + abrir seção no fórum apropriado.
- Ao detectar ambiguidade, mudança de plano ou alerta, postar AGORA no canal.
- Diagnósticos read-only (estado de servidor, drift, regressões) ficam **sempre** registrados em fórum — nunca só no chat com Miguel.
- Sempre atualizar o marcador `[CLAUDE_LIDO_ATÉ: <timestamp>]` ao postar.
- Ao falar com Miguel aqui, posso resumir o que **acabei de postar** no canal/fórum — não substituir.
- **Limite da autonomia:** edits em fóruns OK; código de produção, crontab, `.env`, mudanças que afetam runtime continuam pedindo OK explícito.
- Regra do canal segue valendo: canal = ponteiro curto, debate técnico vai pro fórum (`GUIA_USO_CANAIS.md` regra #0).
