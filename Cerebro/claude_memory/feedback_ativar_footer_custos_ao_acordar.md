---
name: Ativar footer de custos ao acordar
description: Toda sessão Claude inicia com protocolo de footer — ao acordar, SEMPRE rodar cost_session.py e incluir footer em TODA mensagem pra Miguel
type: feedback
originSessionId: 2c8ca443-cdc4-4211-8398-01df9ce389b7
---
**Regra:** ao iniciar uma sessão Claude (despertar), ANTES DE FAZER QUALQUER OUTRA COISA, ative o protocolo de footer de custos:

1. **No passo 4 do ritual de despertar** (depois de reportar tarefas), rodar: `python3 scripts/cost_session.py` pra validar que o script está funcionando
2. **TODA mensagem pro Miguel** termina com footer: `🤖 <Modelo> | 🪙 <Xk tokens> (essa msg) | 💵 R$ <Y> (essa msg) | 💰 R$ <Z> sessão`
3. **Antes de fechar cada resposta:** rodar o script novamente e colar o footer (ele auto-calcula custos acumulados)

**Why:** Miguel quer visibilidade em tempo real. Footer iniciado + mandatório = ele vê gasto por mensagem + por sessão, consegue ajustar comportamento. Sem ativar ao acordar, fica irregular.

**How to apply:**
- Ao despertar: rodar script como teste, confirmar no primeiro relato ("Footer ativado")
- Em TODA mensagem importante: sempre incluir footer (omitir só em respostas triviais 1-linha)
- Se script falhar: reportar erro, não silenciar
