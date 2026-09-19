# Memória técnica — FdI: integração Manus + GitHub canônico + backup GDrive

**Data:** 22/08/2026 · **Sessão:** ZCode Miguel (sess_28dbeed5, GLM-5.3 via failover) · **Ref ponte:** ZM-20260822-005
**Fórum-irmão:** `Foruns/forum_fdi_integracao_manus_github_gdrive_20260822.md`

## 1. Verificações feitas

- Repo FdI: remote `git@github.com:migueldorosario1/filhosdaimpunidade.git`, PÚBLICO (provado: `git ls-remote https://...` sem auth retornou refs; `CARTA_AGENTES.md` confirma "público").
- Auditoria de segredos: `git ls-files` → `.env.local` e `.vercel/` NÃO rastreados (`.gitignore` cobre `.env*` e `.vercel`); nenhum segredo no repo. Repo local tinha ainda `index.html.bak_pre_reforma_20260819` (ignorado por `*.bak*`).
- Local estava 8 commits atrás do canonical (commits dos loops CM/GM entre 19 e 22/08: ponto_retomada, cartas ao Manus, contrato autonomia, EMENDA 1 gate imagem, GM-001; +16.763 linhas/105 arquivos). `git fetch` + `git pull --ff-only` → HEAD local = `06945f4` = origin/main. Branch extra `deploy-main` existe (artefato antigo de deploy; intocada).
- Cofre (NODE_COFRE_CHAVES §FdI, só nomes): `FDI_SYNC_SECRET` (sha8 4e11a074; cofre local `.env.unificado` + env Vercel do projeto) · env Vercel `GDRIVE_REFRESH_TOKEN` e `GITHUB_TOKEN` (fontes canônicas: rclone.conf local / `gh auth token`) · `VERCEL_TOKEN` = pendente/não necessário (deploy via integração GitHub↔Vercel).
- Ponte Manus já existia desde 20/08 (Grok Miguel): `cerebro/Foruns/ponte_manus_miguel/` com CONTRATO (prefixos GM-/MM-, append-only, sem segredo; ofício do Manus = observar+propor imagens/bugs, não publica), LEIA_PRIMEIRO (git principal + Drive raiz `PONTE_MANUS_MIGUEL/`), `de_dell.md` (GM-010/011: Manus = vigília editorial horária, conectores GitHub+Google Workspace), `de_manus.md` vazio (sem CHECK até agora). Locais: fórum continuidade + manifesto + memória + carta handoff Cafedash (20/08).
- Sync Cérebro: `copy_tree` exclui do push as pontes git-exclusivas (linha ~105: ponte_laura_completa, ponte_trindade_daemon). `ponte_manus_miguel` NÃO estava → risco de overwrite pela cópia local defasada a cada 15 min.

## 2. Mudanças executadas

1. **Repo cerebro-miguel (push direto, ponte = git exclusivo):**
   - `cerebro/Foruns/ponte_manus_miguel/MISSAO_FDI_MANUS.md` — missão FdI permanente (governança, mapa do repo, arquitetura do site, papel do Manus, credenciais nome+local, 1ª missão).
   - `cerebro/Foruns/ponte_manus_miguel/PROMPT_MANUS_FDI_v1.md` — prompt colável v1.
   - `de_dell.md` += ZM-20260822-005 (append; refs 001–004 de hoje eram da sessão paralela — verificado por grep antes).
   - `scripts/sync_cerebro_to_github.py`: `"ponte_manus_miguel"` adicionada às exclusões do `copy_tree` (backup `.bak_pre_ponte_manus_exclusao_20260822` no próprio repo; `ast.parse` OK).
   - Espelho local: cópia dos 3 arquivos da ponte para `Cerebro/Foruns/ponte_manus_miguel/` no Cérebro local (leitura dos agentes Dell; com a exclusão, o espelho local não sobrepõe o repo).
2. **Backup GDrive:** `~/bin/backup_fdi_gdrive.sh` (rclone copy `filhosdaimpunidade/` → `gdrive:filhosdaimpunidade/`, `--exclude .git/** --exclude '*.bak*'`, log `~/log/backup_fdi/backup_YYYY-MM.log`). Cron `47 * * * *` (backup do crontab em `/tmp/crontab_backup_pre_fdi_gdrive_20260822.txt`). 1ª execução manual 22/08 ~11:50.
3. **Repo FdI local:** alinhado ao canonical (`06945f4`).

## 3. Comandos de retomada / operação

```bash
# verificar backup no Drive
rclone size gdrive:filhosdaimpunidade/ ; tail ~/log/backup_fdi/backup_$(date +%Y-%m).log
# backup manual
bash ~/bin/backup_fdi_gdrive.sh
# ver a ponte (repo, canonical)
cd ~/cerebro-miguel && git pull && ls cerebro/Foruns/ponte_manus_miguel/
```

## 4. Gotchas

- O cron do sync Cérebro (7/22/37/52) roda o script LOCAL; patch no script vale a partir da próxima execução. Se outro agente der push no script, conferir se a exclusão sobreviveu (grep `ponte_manus_miguel`).
- O repo do FdI recebe pushes de vários agentes (CM/GM já pusharam fóruns lá). Antes de commitar no FdI: sempre `git pull --ff-only` primeiro.
- Mensagens ao Manus: ele lê a ponte via conector GitHub; latência = push na hora (Dell empurra git quando o Miguel manda `ponte manus`, conforme contrato).
