---
name: API REST do Manus — protocolo de chamada validado 25/04
description: Endpoint, header e body mínimo pra disparar pesquisas no Manus via API direto
type: reference
originSessionId: f67a36d6-9df3-420c-bcc3-408fc7d4771c
---
API REST do Manus validada por Claude Code em 2026-04-25 ~17:30 BRT.

**Endpoint:** `POST https://api.manus.ai/v2/task.create`

**Header de auth:** `x-manus-api-key: <chave>` (NÃO Authorization Bearer — Bearer espera JWT, a chave Manus é formato `sk-...`).

**Body mínimo:** `{"message": {"content": "..."}}`

**Resposta sucesso:**
```json
{"ok": true, "task_id": "...", "task_url": "https://manus.im/app/<id>", "task_title": "..."}
```

**Doc oficial:** https://open.manus.im/docs (v2 ativa, v1 deprecated)

**Onde buscar a chave:** Miguel tem chave Manus disponível na conta dele (~20k créditos disponíveis em 25/04). Em sessão local salvei em `/tmp/manus_key_session.sh` com `export MANUS_API_KEY=...` — apaga ao reboot. Pra sessão nova, pedir a Miguel ou ler de `/tmp/` se ainda existir.

**NÃO fazer:**
- Gravar a chave em arquivo persistente do projeto.
- Gravar em `memory/`.
- Logar em comando inline visível em `git log`.

**Exemplo curl validado:**
```bash
source /tmp/manus_key_session.sh && curl -sS -X POST https://api.manus.ai/v2/task.create \
  -H "Content-Type: application/json" \
  -H "x-manus-api-key: $MANUS_API_KEY" \
  -d '{"message":{"content":"prompt aqui"}}'
```

**Custo:** cada task consome créditos (não há GET barato pra validar key). Pings mínimos custam ~1-5 créditos. Pesquisas profundas 200-500 créditos. Estimar antes de disparar pesado.

**Como recuperar resultado:** task_url retorna painel web (precisa login). Pra pegar via API, ver doc — provavelmente endpoint tipo `task.get` ou polling. Não testei ainda.
