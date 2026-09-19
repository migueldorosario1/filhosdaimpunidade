---
name: reference-cofre-github-pat-aiatolah
description: GitHub PAT fine-grained para repo migueldorosario1/aiatolah (Contents R/W). NÃO fica no Cérebro (§82). Está em /root/.env.unificado Tencent + backup Beijing como GITHUB_TOKEN_AIATOLAH_CLAUDE.
metadata: 
  node_type: memory
  type: reference
  originSessionId: 42789f13-00c9-4e70-9b8c-f37d93570ab6
---

# Cofre GitHub PAT Aiatolah — ponteiro (valores fora do Cérebro)

**Repo:** `migueldorosario1/aiatolah` (público, Astro, novo portal IA bilíngue)
**Tipo:** Fine-grained Personal Access Token (PAT)
**Recebido:** 2026-05-24 12:55 BRT (Miguel via chat)
**Expira:** 90 dias (rotacionar antes)
**Escopo testado:** admin/push/pull TODOS true no `aiatolah` apenas

## Onde estão os valores (NÃO aqui — §82 cofre)

- **Primário Tencent (`43.156.151.165:38422 ubuntu`):**
  - Arquivo: `/root/.env.unificado` (chmod 600, owner root)
  - Variáveis: `GITHUB_TOKEN_AIATOLAH_CLAUDE`, `GITHUB_USER_AIATOLAH`, `GITHUB_REPO_AIATOLAH`
- **Backup Beijing (`39.106.184.215:22 root`):**
  - Arquivo: `/root/cerebro_trindade/cofre/env_cofre_backup` (chmod 600)
  - Mesmo conteúdo

## Quando usar

- Escrever/editar arquivos no repo `aiatolah` via REST API
- Commitar mudanças
- Ler conteúdo (sem rate limit anônimo de 60req/h)
- NÃO usar pra outros repos — token escopado

## Como puxar (no Tencent)

```bash
source /root/.env.unificado
# Agora $GITHUB_TOKEN_AIATOLAH_CLAUDE disponível em env (não em ps aux)
curl -H "Authorization: Bearer $GITHUB_TOKEN_AIATOLAH_CLAUDE" https://api.github.com/repos/migueldorosario1/aiatolah/contents/forums
```

## Como ESCREVER um arquivo via API

PUT em `/repos/{owner}/{repo}/contents/{path}` com payload:
```json
{
  "message": "commit msg",
  "content": "<base64 do conteúdo>",
  "sha": "<sha atual se file existe (read antes pra pegar)>",
  "committer": {"name": "Claude Maestro", "email": "noreply@anthropic.com"}
}
```

## Limites do escopo

- ❌ NÃO escreve em outros repos (rio-carta, mundo-trilhos, global-south-news, etc)
- ❌ NÃO altera settings do repo
- ❌ NÃO mexe em GitHub Actions / webhooks
- ✅ Contents R/W no aiatolah apenas

## Cuidados (§82 + boas práticas)

- ❌ NUNCA copiar token pra canal_trindade/fóruns/MEMORY.md/Telegram
- ❌ NUNCA logar token em arquivo `.log`
- ❌ NUNCA expor em `ps aux` (usar variável de env, não `--header` literal)
- ✅ Rotacionar a cada 90 dias
- ✅ Revogar em github.com/settings/tokens se vazar
- ✅ Cada commit `committer` = "Claude Maestro" (rastreabilidade)

## Como revogar (emergência)

1. Miguel acessa https://github.com/settings/tokens
2. Encontra "Claude Maestro Aiatolah"
3. Revoke → token fica inválido imediatamente

## Histórico

- **2026-05-24 12:55 BRT** — recebido via chat
- **2026-05-24 12:56 BRT** — salvo Tencent + Beijing, auth validada (admin/push/pull OK em aiatolah)

## Relacionado

- [[feedback_credenciais_nunca_em_forum_canal]] — §82 cofre
- [[reference_cofre_ssh_serverdoin]] — outro cofre similar (Serverdo.in SSH)

— Inscrito por Claude Maestro 2026-05-24 12:56 BRT
