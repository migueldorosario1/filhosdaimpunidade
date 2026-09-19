---
name: Fix agente_observador — cópia servidor desatualizada (2026-04-17)
description: O agente_observador.py no servidor Tencent estava usando "from dotenv import load_dotenv" e crashava com ModuleNotFoundError; a versão local já usava carregar_chaves. Subido scp.
type: project
originSessionId: 82c307d7-bd07-4c7a-8ed2-9e86b6fa4e22
---
Em 2026-04-17 o Sentinela estava 100% morto — `ModuleNotFoundError: No module named 'dotenv'` em cada tick (`*/10 * * * *`), 30+ ocorrências acumuladas no `sentinela.log`. Causa: cópia do servidor desatualizada. Versão local já tinha migrado a linha 4 de `from dotenv import load_dotenv` para `from carregar_chaves import BASE_DIR, AGENT_DATA_DIR`.

**Fix:** `scp` do `agente_observador.py` local para `/root/agente_observador.py` no Tencent. Import testado OK com `/usr/bin/python3`. Primeira execução pós-fix às 07:10: *"✅ Checkup O.K. | O site está blindado, as IAs estão escrevendo limpo e sem repetições."*

**Why:** a cópia local do repositório é quem evolui primeiro. O servidor precisa ser sincronizado — nunca confie que o código no servidor é igual ao local sem conferir. O mesmo risco vale para outros scripts chamados com `/usr/bin/python3` no crontab.

**How to apply:**
- Se algum agente que usa `/usr/bin/python3` falhar com `ModuleNotFoundError: dotenv`, checar se a cópia do servidor está desatualizada e subir a local. Não instalar `dotenv` no sistema — a política é usar `carregar_chaves.py` (que já trata fallback).
- Em deploys amplos, considerar `sincronizar_servidores.sh` (rsync) em vez de edits pontuais, pra evitar drift entre cópias.
