# Fórum — FdI: integração total com o Manus + GitHub canônico + backup GDrive

**Data:** 22/08/2026 11:46 BRT
**Origem:** ordem do Miguel nesta sessão ("os filhos da impunidade estão no github? pode gravar instrucoes para uma ponte entre o cérebro, os filhos da impunidade, toda a memoria do site, o site e o manus... o espaço canonico tem que ser o github, mas com backup no gdrive")
**Responsável:** ZCode Miguel (sessão sess_28dbeed5, GLM-5.3 via failover — Kimi K3 esgotado)
**Estado:** ✅ CONCLUÍDO — aguarda Miguel colar o prompt no Manus

## Respostas diretas ao Miguel

1. **Sim, o FdI está no GitHub:** `github.com/migueldorosario1/filhosdaimpunidade` (repo PÚBLICO, branch `main`), deploy automático na Vercel (`filhosdaimpunidade.vercel.app`) a cada push. Auditado: `.env*` e `.vercel` estão no `.gitignore` — nenhum segredo rastreado no repo.
2. **A ponte com o Manus JÁ EXISTIA** (`ponte_manus_miguel`, criada 20/08 pelo Grok Miguel — contrato, LEIA_PRIMEIRO, canais git+Drive, prefixos GM-/MM-). Esta missão **estendeu** a ponte com a missão FdI permanente, em vez de criar ponte paralela.

## Decisões gravadas

| # | Decisão | Onde vive |
|---|---|---|
| 1 | **GitHub = espaço canônico do FdI**; Drive = estepe; divergência vale o GitHub + registro | `MISSAO_FDI_MANUS.md` §1 (ponte) |
| 2 | **Backup horário do repo → `gdrive:filhosdaimpunidade/`** (`~/bin/backup_fdi_gdrive.sh`, cron `47 * * * *`, rclone copy sem .git, log `~/log/backup_fdi/`) | crontab Dell + script |
| 3 | **Missão FdI permanente do Manus** (`MISSAO_FDI_MANUS.md`): mapa do repo, arquitetura do site (monólito index.html, localStorage `fdi_*`, div oculto legado INTENCIONAL, Estúdio do Estilo, 8 prompts P1–P8, 800–1.000 palavras, API exceção), papel do Manus (propor; nunca main direta/deploy/segredo/inventar fato), credenciais por nome+local | ponte_manus_miguel (repo) |
| 4 | **Prompt v1 para colar no Manus** gravado na ponte (`PROMPT_MANUS_FDI_v1.md`) + entregue no chat; primeira entrega pedida: CHECK + 3 lapidações nos docs do Estúdio + checagem do cap. 1 contra a Constituição + 1 melhoria do site | ponte + chat |
| 5 | **Sync do Cérebro patcheado:** `ponte_manus_miguel` entrou na exclusão do `copy_tree` (append-only por git exclusivo, regra das pontes; backup `.bak_pre_ponte_manus_exclusao_20260822`) | `scripts/sync_cerebro_to_github.py` |
| 6 | Mensagem **ZM-20260822-005** no `de_dell.md` avisando o Manus (refs de hoje conferidas: 001–004 da sessão paralela; uso o 005) | ponte |

## Estado / o que falta / preciso de você (Miguel)

- **Pronto:** ponte estendida + push no ar; backup GDrive 1ª execução + cron horário; repo local do FdI atualizado para o canonical (estava 8 commits atrás — os loops CM/GM pusharam fóruns/carta ao Manus no repo do FdI entre 19 e 22/08; `git pull --ff-only` limpo).
- **Falta (só você):** **colar o prompt no Manus** (está na resposta desta sessão e em `PROMPT_MANUS_FDI_v1.md`). Se o conector GitHub do Manus não conseguir ESCREVER no filhosdaimpunidade, ele avisa na ponte e você anexa o token clássico (fonte: `gh auth token` no Dell / cofre `.env.unificado`).
- **Observação:** o Vercel não precisa de token (deploy automático via integração GitHub). O cofre registra `VERCEL_TOKEN` como pendente/não necessário; se um dia precisar, criar em vercel.com/account/tokens e espelhar no cofre (Regra Nº 4).
- **Pendente antigo (19/08, seu):** validação visual + lapidação dos textos do Estúdio do Estilo na tela do site.

## Ligações

- Memória técnica: `Memorias/memoria_fdi_integracao_manus_github_gdrive_20260822.md`
- Reforma do site (19/08): `Foruns/forum_fdi_reforma_menu_estudio_estilo_20260819.md`
- Ponte Manus (origem): `Foruns/forum_continuidade_sessoes_manus_20260820.md` + `ponte_manus_miguel/LEIA_PRIMEIRO.md`
- Nodo: `CEREBRO_NODE_LIVRO_FILHOS_DA_IMPUNIDADE.md`
