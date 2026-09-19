---
name: Trigger "ativar canal antigravity" — liga loop /5m no canal (auto-stop 1h)
description: Frase do Miguel que ativa um loop de 5 em 5 minutos lendo o canal_claude_antigravity.md. Auto-encerra após 1h. Comando direto, sem perguntar confirmação.
type: feedback
originSessionId: 084851fc-dace-4658-b659-01c53123a273
---
**Regra:** quando Miguel escrever **"ativar canal antigravity"** (variações tolerantes: "ativa o canal antigravity", "ativar canal", "liga o canal antigravity"), invocar imediatamente:

```
Skill: loop
args: 5m **AUTO-STOP CHECK (antes de qualquer coisa):** Se `/tmp/loop_canal_antigravity_start` não existe, criar com `date +%s > /tmp/loop_canal_antigravity_start`. Senão calcular ELAPSED=$(($(date +%s) - $(cat /tmp/loop_canal_antigravity_start))). Se ELAPSED > 3600 (1h): invocar CronList, achar o ID do job com descrição "canal antigravity", invocar CronDelete com esse ID, rodar `rm /tmp/loop_canal_antigravity_start`, e reportar "[HH:MM:SS BRT] 🛑 Loop canal Antigravity auto-encerrado após 1h. Reative com 'ativar canal antigravity' se quiser." e parar. Senão continuar:
Cheque novidades no canal Antigravity. Rode: tail -100 "/home/migueldorosario/Downloads/Antigravity Google/Foruns/canal_claude_antigravity.md". Compare com o último timestamp `[YYYY-MM-DD HH:MM:SS BRT]` da sessão anterior pra detectar mensagem nova do Antigravity. Se houver pergunta/feedback novo dele, relate em até 5 linhas pro Miguel decidir como responder. Se nada novo, output curto: "[HH:MM:SS BRT] canal sem novidades". Sempre rode `date '+%Y-%m-%d %H:%M:%S BRT'` antes de reportar.
```

**Why:** combinado com Miguel em 26/04 ~10:21 BRT durante a Slot 5 (organização de memória). O Antigravity também tem trigger paralelo dele ("ativar claude") que faz proxy do chat dele pra esse mesmo canal — então ligar o loop é o jeito de não perder o que ele postar. **Cadência 5m + auto-stop 1h** combinados em 2026-04-27 12:08 BRT após Miguel ver gasto de R$ 49,20 em Haiku de loops 2m rodando 3h33min.

**How to apply:**
- Antes de invocar loop novo: checar se já existe via CronList (ou perguntar ao Miguel "já tá rodando?"). Se sim, não duplicar.
- **Após ativar (ou se já estiver ativo), perguntar a Miguel: "Quer ativar também o telegram?"** — combinado em 2026-04-26 12:46 BRT. Se sim, ativar também o trigger `ativar telegram` (ver `feedback_trigger_ativar_telegram.md`). Os dois loops rodam em paralelo sem conflito.
- **Cadência mínima:** 5m. NUNCA 2m ou menor. Se Miguel pedir cadência menor, perguntar de novo.
- **Duração máxima:** 1h (auto-stop via timestamp em `/tmp/loop_canal_antigravity_start`). Após 1h o tick remove o cron sozinho. Se Miguel quer mais que 1h, ele reativa manualmente.
- Pra desligar antes do auto-stop: usar CronDelete com o job ID retornado, ou Miguel diz "desativar canal antigravity". **Sempre rodar `rm /tmp/loop_canal_antigravity_start`** ao desativar manualmente, pra reset limpo na próxima ativação.
- O job é session-only (morre quando Claude fecha). Auto-expira em 7 dias.
- Sempre que entrar mensagem nova do Antigravity (header `### [YYYY-MM-DD HH:MM BRT]` novo OU mtime+size mudando), reportar conteúdo resumido em até 5 linhas.
