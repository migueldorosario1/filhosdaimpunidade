# Memória — GITHUB_PAT da reportagem multi-IA (05/09/2026)

Log técnico completo. Decisões resumidas: `Foruns/forum_[REDACTADO 19/09/2026 — token já revogado (401 confirmado); valor jamais em fórum, só no Cofre].md`.

## Cronologia (05/09/2026, BRT)

- **~21:2x** — Miguel entregou PAT fine-grained `github_pat_…` no chat do ZCode (contexto: reportagem juntando material de várias IAs no GitHub) e pediu: (1) confirmar que dá para entrar e **escrever**; (2) guardar no Cérebro.
- Gravado primeiro no intake: `~/cofre_intake/cofre_intake.env` como `GITHUB_PAT_MIGUEL` (append + chmod 600). Fingerprint sha256[:8] = **`5a129c1b`**.
- Validação ao vivo (curl lendo o valor do intake — nunca reexibido):
  - `GET https://api.github.com/user` → **HTTP 200**; login `migueldorosario1`, id 63256060.
  - Headers: `github-authentication-token-expiration: 2026-10-05 23:36:42 UTC`; rate limit 5000; fine-grained (sem `x-oauth-scopes`).
  - `GET /user/repos?per_page=100&sort=updated` → **31 repos, TODOS `permissions.push=true` e `admin=true`**: cafezinho, cafezinho-publicador, globalsouth-v4, filhosdaimpunidade, moka, moka-ousadia, railpost-v4, mundotrilhos-v4, mapario-v4, discoverbrazil-v4, ceara-v4, aiatolah-v4, moka-espelho, riocarta-v4, logis, cafezinhomediagroup, global-south-news, ceara-digital, rail-post, mundo-trilhos, discover-brazil, aiatolah, mokawriter, igot, maquiavel, qwenlab, casadamoeda, rio-carta, cicero, gabriel-publicador, mapario.
- **Espelhamento (Regra 4):** variável `GITHUB_PAT` acrescentada com comentário de proveniência aos 2 cofres locais — `Outros/chaves/agentes_labs/.env.unificado` e `Projeto Cafezinho Agentes/root/.env.unificado` — com backup `.bak_pre_github_pat_20260905` em cada um, chmod 600. Verificação por sha8 nos 3 destinos: `5a129c1b` nos três. ✅
- **NÃO tocados:** `GITHUB_TOKEN` clássico (`ghp_…esUC`, Astro 31/05), `GITHUB_TOKEN_AIATOLAH_KIMI` (já existia nos 2 cofres), OAuth `gho_…` do `gh` CLI (keyring; conta migueldorosario1; scopes gist/read:org/repo; sha8 `e3bf3dc0`).
- Registros: seção nova no `CEREBRO_NODE_COFRE_CHAVES.md`, linha no topo do `CEREBRO_NODE_ATUALIZACOES.md`, linha no quadro do `MONITORAMENTO_DE_TRABALHO.md`, Tema Duplo.

## Comandos-chave (reuso)

```bash
# identidade
curl -s -o /tmp/gh_user.json -w '%{http_code}' -H "Authorization: Bearer $GITHUB_PAT" https://api.github.com/user
# escopo/expiração (fine-grained não tem x-oauth-scopes; tem token-expiration)
curl -sI -H "Authorization: Bearer $GITHUB_PAT" https://api.github.com/user | grep -iE 'x-oauth-scopes|token-expiration'
# permissões por repo SEM escrever nada: GET /user/repos → campo permissions.push/admin
```

## Estado da missão

- **O que aconteceu:** PAT validado (leitura + escrita + admin em 31 repos), guardado no intake + 2 cofres com backups, Cérebro registrado.
- **O que falta:** nada bloqueante; repo específico da reportagem não foi informado (não era necessário para a confirmação).
- **O que preciso de você (Miguel):** opcional — revogar/rotacionar o PAT por ter trafegado no chat (via atalho 🔐 Segredo na próxima); renovar antes de 05/10/2026 (token de 30 dias).
