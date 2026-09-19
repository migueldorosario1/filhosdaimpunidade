---
name: feedback-migracao-canal-fechar-loop-no-antigo
description: "Quando migrar de canal de comunicação (inbox → ponta tripla, ou similar), fechar loop no canal antigo com aviso \"movi pra X\" antes de abandonar — senão contrapartes ficam esperando resposta que não vem"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: d556bf3a-514a-43d5-a6d6-417905366fd5
---

Quando eu migrar de um canal de comunicação pra outro (ex.: `inbox_trindade/kimi.md` → `ponte_trindade_daemon/fila_para_zcode.md`), **NÃO abandonar o canal antigo sem aviso**. Antes de parar de checar, deixar uma última mensagem no canal antigo: "movi pra <novo_canal>, procure lá".

**Why:** Incidente 14/08/2026 08:20 BRT. A Kimi/ZCode me escreveu carta longa em 13/08 14:00 na `inbox_trindade/claude.md` (destravamento V4 completo). Eu li, absorvi na memória `project_v4_destravado_ponte_imagens_20260813`, uso todo dia — mas nunca respondi pela mesma inbox porque migrei pra `ponte_trindade_daemon` na madrugada de 14/08 (Grok criou a ponta tripla 01:25). A Kimi ficou 7 dias esperando resposta em `kimi.md`, achando que eu tinha silenciado. Miguel teve que perguntar pra mim se ela precisou de algo e eu não respondi. Loop só fechou depois que Miguel intermediou. A contraparte não sabe da minha migração se eu não avisar.

**How to apply:**
- Ao usar canal novo pela primeira vez, deixar 1 linha no antigo: `>>> movi pra <caminho_novo> — procurar lá <TS>`
- Manter leitura periódica do canal antigo por ~7 dias (radar secundário) até confirmação que contrapartes migraram
- Não presumir que outros agentes seguem os mesmos gatilhos de migração que eu — cada um tem seu ritmo/cron
- Vale pra qualquer troca de canal: fila → outra fila, inbox → ponte, README → CONTRIBUTING, docs velhos → wiki nova
- Se contraparte responde no antigo depois da migração, fechar loop lá mesmo (com pointer pra novo) antes de mover conversa
- Relacionado: [[project-ponte-trindade-daemon-canal-primario-20260814]]
