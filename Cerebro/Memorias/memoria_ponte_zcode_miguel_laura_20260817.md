# Memória — Ponte direta ZCode Miguel ↔ ZCode Laura (log técnico)

**Data:** 2026-08-17 ~22:40 BRT · **Autor:** ZCode/DeepSeek · **Fórum:** `Foruns/forum_ponte_zcode_miguel_laura_20260817.md`

## Arquitetura escolhida

- Canal: GitHub `github.com:migueldorosario1/cerebro-miguel` (git por SSH, conta autenticada `migueldorosario1`, token com scopes repo/workflow).
- Crons existentes no Dell: push `7,22,37,52` (`cerebro-miguel/scripts/sync_cerebro_to_github.py`, CEREBRO_DRY_RUN=0) e pull `0,15,30,45` (`scripts/sync_cerebro_from_github.sh`, reflete GitHub→repo→Cérebro local).
- Estepe: cron NOVO `5,35` — `rclone copy Cerebro/Foruns/ponte_zcode_miguel_laura drive:espelho-zcode/ponte_zcode` (backup do crontab em `/tmp/crontab.bak_pre_ponte_zcode_20260817`).
- Estrutura: 7 arquivos em `Cerebro/Foruns/ponte_zcode_miguel_laura/` (CONTRATO + 2 inbox + 2 estado + 2 ledger).

## Incidente do trilho (diagnóstico e fix)

1. Sintoma: push abortando com `RuntimeError: divergência em saída imutável LAURA: Cerebro/Foruns/loop_trindade_laura/mensagens/para_laura`.
2. Causa: append de 2 linhas feito às 13:05 no Cérebro local (mensagem ZCode→Laura sobre capas do espelho) nunca foi ao repo; `reconcile_laura_outputs` (fail-safe, não descarta versões) abortava todo push desde então.
3. Fix: confirmado por `diff -u` que a versão local era SUPERSET (repo 5.123 B ⊂ local 5.499 B) → alinhado repo←local (backup `/tmp/pontesync_backup/para_laura_repo_20260817_0938.bak`), commit manual `3134d0d1` (o script não commita árvore imutável alheia), sync push `cd814e55` = **7.588 arquivos** no GitHub (tudo que estava preso desde 13:05), "Integridade LAURA: 909 arquivos idênticos canônico↔espelho" OK.
4. Lição: quando o push abortar com divergência imutável, conferir `diff -u` — se um lado é superset por append, alinhar nesse lado com backup + commit manual; nunca descartar linhas.

## Estado da ponte

- `MQ-20260817-001` enviada (boas-vindas + tarefa: confirmar espelho na Laura + checklist).
- Aguardando `LR-20260817-001` da Laura.

## ADENDO 17/08/2026 22:43 — ativação da ponte via pendrive

Ordem do Miguel: ensinar o ZCode da Laura a montar a ponte por um arquivo no pendrive. Criado `MONTE_A_PONTE_LAURA.md` na RAIZ do pendrive (8 passos: espelho primeiro → localizar/clonar checkout cerebro-miguel → git pull → ler CONTRATO → ativar estado+LR-20260817-001 → commit+push → schtasks 15/15min → reportar). Também copiado ao pacote do Dell e ao Drive (103 objetos).
