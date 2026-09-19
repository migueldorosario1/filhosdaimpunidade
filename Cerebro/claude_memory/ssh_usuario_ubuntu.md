---
name: SSH Tencent usa usuario ubuntu, não root
description: O servidor Tencent (Cingapura) bloqueia login root direto — usar sempre ubuntu@43.156.151.165 com sudo para comandos root.
type: feedback
originSessionId: a6af224d-901d-4c7d-ab75-58b5eae63f5b
---
NUNCA usar `root@43.156.151.165` para SSH. O servidor bloqueia root silenciosamente e devolve prompt de senha falso.

Usar sempre: `ssh cingapura` (alias configurado em `~/.ssh/config`) ou `ssh -i ~/.ssh/id_rsa -p 38422 ubuntu@43.156.151.165`

Para comandos que precisam de root, usar `sudo`.

**Why:** O Ubuntu no servidor está configurado para bloquear login direto de root na porta SSH. Isso causou múltiplos "Permission denied" até ser diagnosticado pelo Antigravity (2026-04-11).

**How to apply:** Em todo comando SSH para o Tencent, trocar `root@` por `ubuntu@` e prefixar comandos com `sudo` quando necessário.
