# Cofre GitHub — chaves de acesso administrativo

**Escopo:** tokens do GitHub (Personal Access Tokens, GitHub App tokens, chaves SSH pra push automatizado).

**Regra de segredo:** valores NUNCA são versionados. Ficam apenas em `.env` local (gitignored via regra `**/.env` no `.gitignore` raiz do repo). Só metadados sobem pra este LEIA-ME.

## Chaves guardadas

### `GITHUB_ADMIN` — PAT admin (conta migueldorosario1)

| Campo | Valor |
|---|---|
| Nome interno | `github-admin` |
| Entregue por Miguel | 2026-09-08 12:41:24 BRT |
| Guardada aqui em | 2026-09-08 12:55 BRT |
| Origem no Dell | `~/cofre_intake/cofre_intake.env` (chave `GITHUB_ADMIN`) |
| Registrada em | `~/cofre_intake/cofre_intake.meta.tsv` (linha `GITHUB_ADMIN github-admin github`) |
| SHA256 (12 chars, checksum de integridade) | `451cc98c571c` |
| Escopo | **Controle total** sobre a conta GitHub `migueldorosario1` (todos os repos, admin) |
| Uso previsto | Fallback / operações administrativas de emergência (rotação de tokens, gestão de repos, deploy keys, etc.) |
| Autorização de guarda | Miguel chat CLI 2026-09-08 ~12:44 BRT: "vai no cofre local, o intake, e guarda com cuidado a chave github-admin, que tem controle total sobre o github. talvez precisemos no futuro" |

**Como usar (quando autorizado):**
```bash
export $(grep -E '^GITHUB_ADMIN=' ~/cerebro-miguel/cerebro/Cofres/cofre_github/.env | xargs)
# depois: gh auth login --with-token <<< "$GITHUB_ADMIN"   (ou git remote com PAT embutido)
unset GITHUB_ADMIN   # sempre limpar após uso
```

**Confirmar integridade a qualquer momento:**
```bash
awk -F= '{print $2}' ~/cerebro-miguel/cerebro/Cofres/cofre_github/.env | tr -d '\n' | sha256sum | cut -c1-12
# deve devolver: 451cc98c571c
```

## Regras deste cofre

1. **Nunca commitar `.env`** — o `.gitignore` raiz do repo cobre `**/.env`, mas verifique com `git status` antes de qualquer commit no cerebro.
2. **Permissões estritas** — `700` no diretório, `600` no `.env`. Só o dono lê.
3. **Não copiar para outros paths sem autorização explícita** — chave admin é superfície de risco crítica; cada cópia é um vetor a mais.
4. **Rotação** — quando Miguel rotacionar a chave, atualizar `.env` e `.env` origem no `~/cofre_intake/`; atualizar sha256 aqui neste LEIA-ME; registrar a rotação no `intake.log` do cofre_intake.
5. **Expiração** — PATs do GitHub podem ter data de expiração. Verificar em https://github.com/settings/tokens quando necessário. Se esta chave for sem expiração (classic PAT admin), fica vigente até revogação manual.

---

**Última atualização:** 2026-09-08 12:55 BRT · Claude Miguel (`claude-opus-4-7`)
