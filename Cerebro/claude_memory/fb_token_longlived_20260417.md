---
name: FB_PAGE_ACCESS_TOKEN Long-Lived até 2026-06-16
description: Em 2026-04-17 Miguel emitiu Long-Lived Token do Facebook (válido até 16/06/2026) substituindo o Short-Lived que expirou em 2026-04-16.
type: project
originSessionId: 82c307d7-bd07-4c7a-8ed2-9e86b6fa4e22
---
Em 2026-04-17 o agente Facebook começou a retornar `OAuthException (code 463): Session has expired` — o token era Short-Lived (válido só até 2026-04-16). Miguel emitiu via Graph API Explorer um **Long-Lived Page Access Token** (validade: **16 de Junho de 2026**) e substituiu `FB_PAGE_ACCESS_TOKEN` em dois lugares:
- `.env` local no diretório raiz do projeto
- `/root/.env` no servidor Tencent (Cingapura) via scp

**Verificação:** `curl https://graph.facebook.com/v19.0/me?access_token=$TOKEN` retornou `{"name":"O Cafezinho","id":"421927677830371"}` — token válido.

**Why:** Short-Lived Tokens do FB expiram em dias/semanas e quebram produção. Long-Lived estende 60 dias. Ainda assim, o ideal é pedir um **Page Access Token Permanente (Expires: Never)** quando possível.

**How to apply:**
- Se o agente Facebook voltar a dar `OAuthException 463` ou erro de auth, checar validade do token em `https://developers.facebook.com/tools/debug/accesstoken/?access_token=$TOKEN`.
- **Renovação: atualizar o token em TRÊS lugares:**
  1. `.env` local do projeto
  2. `/root/.env` no Tencent
  3. **`/root/.env.unificado` no Tencent** ← *esse é o crítico. Agentes (postador_meta.py, agentes_facebook.py, gerador_meta_textos.py, gerador_fios_x.py etc) carregam .env.unificado PRIMEIRO; se existir, ignoram o .env. Então atualizar só o .env NÃO basta.*
- **Incidente 2026-04-17:** Miguel atualizou só `/root/.env`; agente continuou falhando com OAuthException 463 por várias horas porque `.env.unificado` ainda tinha token velho. Claude Code detectou divergência às 09:15 e sincronizou via `sed` no `.env.unificado`. curl teste: `200 {"name":"O Cafezinho","id":"421927677830371"}`.
- Backup criado: `/root/.env.unificado.bak_20260417_0918`.
- Próxima expiração esperada: **2026-06-16**. Agendar renovação antes.
- **Ideal futuro:** pedir Page Access Token permanente via app do Facebook Developer (Business/App settings).
