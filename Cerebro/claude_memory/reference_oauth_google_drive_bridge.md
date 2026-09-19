---
name: reference-oauth-google-drive-bridge
description: "OAuth Google Drive Bridge — credenciais Desktop App OAuth criadas por Miguel 23/05 12:09 BRT pra Claude Code editar docs Drive. Credenciais ficam no Tencent /root/.config/claude_drive/oauth_client.json, NÃO no Cérebro."
metadata:
  type: reference
  originSessionId: tick-23-loop-23mai
---

# OAuth Google Drive Bridge — Claude Code ↔ Drive

**Criado:** 2026-05-23 12:09 BRT por Miguel (Google Cloud Console)
**Projeto Google Cloud:** "Claude Drive Bridge" (criado pelo Miguel)
**Tipo de cliente:** Desktop App (OAuth 2.0)
**Modo de publicação:** Testing (apenas Miguel autorizado como test user)

## Por que existe

MCP Google Drive do Claude Code só tem `read_file_content`, `create_file`, `copy_file` — sem update/append. Pra editar docs existentes (ex: forum trindade aberto), montamos ponte via OAuth próprio + Python REST API.

## Onde estão as credenciais

**Tencent:** `/root/.config/claude_drive/oauth_client.json` (chmod 600, owner root)

Arquivo contém:
- `client_id` (termina em `.apps.googleusercontent.com`)
- `client_secret` (formato `GOCSPX-...`)
- `redirect_uris`: `http://localhost`, `urn:ietf:wg:oauth:2.0:oob`

**NÃO reproduzir valores aqui no Cérebro nem em canais.** Cofre §82.

## Onde fica o token (após autorização)

**Tencent:** `/root/.config/claude_drive/token.json` (a criar após Miguel autorizar)

Contém:
- `access_token` (expira em 1h)
- `refresh_token` (longa duração, usado pra renovar access automático)

## Como funciona

1. Helper Python `~/scripts/drive_bridge.py` (a criar) usa googleapiclient
2. Lê `oauth_client.json` + `token.json`
3. Refresca access_token automaticamente quando expira
4. Permite: editar doc, anexar texto, criar revisões, listar drives

## Escopos autorizados

- `https://www.googleapis.com/auth/drive` (acesso total Drive)
- `https://www.googleapis.com/auth/documents` (edição Google Docs)

## Fluxo de autorização inicial

1. Claude gera URL de autorização com client_id + redirect_uri + scope
2. Miguel abre URL no browser, autoriza no consent screen
3. Browser redireciona pra `http://localhost?code=4/0AeWvxe...` (erro "site inacessível" esperado)
4. Miguel copia URL completa, cola pro Claude
5. Claude extrai `code` da URL, troca por `access_token + refresh_token` via `oauth2.googleapis.com/token`
6. Salva token em `/root/.config/claude_drive/token.json` chmod 600

## Como revogar

Miguel acessa: https://myaccount.google.com/permissions
Localiza "Claude Bridge" → Remove acesso.
Tokens ficam inválidos imediatamente.

## Quando atualizar essa memória

- Quando o helper Python estiver pronto e em produção → atualizar path do script
- Quando setar cron de uso → linkar pro cron
- Se trocar de Test pra Production (verificação Google) → atualizar status
- Se adicionar/remover escopos → atualizar lista acima

## Tentativa Kimi-Beijing OAuth (23/05 12:45 BRT) — falhou por GFW

Tentamos replicar o setup OAuth pro Kimi-Beijing escrever direto no Drive. Tokens emitidos com sucesso (refresh_token novo via `prompt=consent`). Helper Python (`/root/cerebro_trindade/root/kimi_drive_bridge.py`) deployado. **Mas:** primeiro teste de refresh do access_token retornou `OSError: [Errno 101] Network is unreachable` ao tentar `oauth2.googleapis.com`. Causa: Alibaba/Beijing está atrás do Great Firewall — saída pra Google bloqueada.

Decisão Miguel 12:50 BRT: **manter ponte via Claude (Tencent/Singapura, fora do GFW)** em vez de tentar proxy/VPN. Kimi-Beijing escreve no `forum_trindade.md` local; loop Aiatolah (10min) copia delta Kimi pro Doc.

**Infra Kimi-Beijing dormente:**
- `/root/cerebro_trindade/.config/kimi_drive/oauth_client.json` (mesmo client_id que Claude)
- `/root/cerebro_trindade/.config/kimi_drive/token.json` (refresh_token separado)
- `/root/cerebro_trindade/root/kimi_drive_bridge.py` (helper idêntico ao do Claude)

**Pra ativar no futuro:** instalar proxy HTTP no Beijing apontando pra Tencent ou outro nó fora do GFW, e modificar helper pra usar `http_proxy`/`https_proxy` env var.

## Relacionado

- [[reference_forum_trindade_google_drive]] — doc Drive específico que motivou a ponte
- [[feedback_credenciais_nunca_em_forum_canal]] — regra §82 cofre

— Inscrito por Claude Maestro 2026-05-23 12:13 BRT (ordem direta Miguel) · atualizado 12:51 BRT (Kimi-Beijing OAuth bloqueado por GFW)
