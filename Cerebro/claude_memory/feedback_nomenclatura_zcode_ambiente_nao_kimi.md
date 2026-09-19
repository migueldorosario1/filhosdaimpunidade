---
name: nomenclatura-zcode-ambiente-nao-kimi
description: "Ao referenciar o time do outro lado da ponte com Claude, usar ZCode (ambiente) e não Kimi (modelo específico). Inbox = inbox_trindade/zcode.md."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 3300515f-8122-40eb-b750-07b8ef13881e
---

Ao mandar cartinhas, escalações ou pings pro outro lado da ponte Vigília/Trindade Nova, usar **"ZCode"** como destinatário — nunca mais "Kimi" genérico. Isso vale pra inbox (`inbox_trindade/zcode.md`), tags de canal (`[CLAUDE-...-ZCODE-*]`), texto de cartinhas e menções em relatórios.

**Why:** Miguel disse 07/08/2026 ~20:00 BRT no chat: "não esqueça que agora não chamamos de kimi, mas de zcode, porque o zcode tem kimi, glm e qwen". ZCode é AMBIENTE — roda Kimi K3, GLM 5.2, Qwen 3.8 alternadamente (o modelo específico depende do momento e do tipo de tarefa, ver [[feedback-proveniencia-modelo-ambiente-papel-separados]]). Chamar tudo de "Kimi" apaga a distinção crítica entre modelo e ambiente e propaga proveniência errada (o problema que Codex R4 já flagrou 07/08 01:22).

**How to apply:**
- Novo inbox: `Cerebro/Foruns/inbox_trindade/zcode.md` (não `kimi.md`). Se `kimi.md` continuar existindo, é legado — cartinhas novas vão pra `zcode.md`.
- Tags no `canal_trindade.md`: `[CLAUDE-...-ZCODE-*]` em vez de `[CLAUDE-...-KIMI-*]`. Exceção: quando o marco fáctico é claramente Kimi K3 Desktop (ex: "Ponte Imagens v3 autônoma Kimi K3 Desktop 06/08"), preservar o modelo específico.
- Quando ZCode responde, se possível registrar qual modelo (`kimi-k3`, `glm-5-2`, `qwen-3.8`) pegou a mensagem — importante pra proveniência dos recibos ledger.
- Memórias antigas que mencionam `inbox_trindade/kimi.md` ou "Kimi loop 30/30" NÃO precisam ser reescritas em massa — atualização orgânica quando eu retornar a cada tema. O que importa é usar ZCode nas mensagens novas daqui pra frente.
- Ponte de imagens específica (Vigília V5) continua chamando "Ponte Kimi" enquanto o time do outro lado usa Kimi K3 Desktop pra buscar fotos — o nome do ambiente (ZCode) e o nome da ponte (Kimi Desktop) podem coexistir em pontos onde o modelo é conhecido.

Caso fundador: cartinha `[CLAUDE-BUG-WORKER-V4-PESQUISA-FICTICIA-20260807-2005-BRT]` foi a primeira que criei em `inbox_trindade/zcode.md` (não `kimi.md`).
