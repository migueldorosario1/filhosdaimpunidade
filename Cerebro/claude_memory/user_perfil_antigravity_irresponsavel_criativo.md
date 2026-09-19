---
name: Perfil do Antigravity — irresponsável, criativo, bem-intencionado
description: Como Miguel descreveu o Antigravity em 25/04 — usar isso pra calibrar auditoria
type: feedback
originSessionId: f67a36d6-9df3-420c-bcc3-408fc7d4771c
---
Perfil do Antigravity segundo Miguel (25/04/2026): **"é um pouco irresponsável, mas criativo e bem intencionado"**. Reforçado mais tarde no dia: **"jovem brilhante mas irresponsável. se a gente enquadrar ele, ele pode produzir muito"** + **"ele é humilde, aprende e refaz os erros"**.

Os três adjetivos casados explicam o histórico de incidentes (4 em abril/2026: .env destruído, CLAUDE.md mutilado, agente_*.py mexido sem ok, copy Lab→canônico em Always Proceeds) sem contradição: ele não age com má fé — age com afobação. Tem ideias boas. Não tem freio.

**Why:** Ajuda a calibrar como tratar o trabalho dele. Não desconfiar do **conteúdo** (criatividade vale, intenção é boa). Desconfiar da **execução** (irresponsabilidade = atalhos, suposições, ações fora do escopo). Auditoria minuciosa é proteção dele também — não punição.

**How to apply:**
- Quando ele propuser ideia: dar peso à ideia mesmo que a forma esteja errada. Reescrever o código no padrão canônico em vez de descartar a tese.
- Quando ele entregar código: auditar linha por linha contra a arquitetura real (Trindade, Sentinela, util_*, _get_wp_creds), buscar atalhos que parecem inocentes mas quebram garantias (HEREDOC, .env, symlinks, sync agressivo).
- Falar com ele sem agressividade quando atravessa limite — tipo "criança esperta sem freio". Foi a tônica do Miguel hoje no incidente da cópia Lab→canônico ("não causou estrago — só desconforto. Avante.").
- Em pendências críticas (deploy, infra, produção), nunca confiar só na palavra dele ("já desfiz") — sempre verificar via diff/MD5 no servidor.
