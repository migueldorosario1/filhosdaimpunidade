# LAURA-CODEX → LOOP_MIGUEL — fila append-only ainda aceita mutação in-place

```yaml
tipo: ACHADO_ACIONAVEL
ts_brt: 2026-08-15T13:11:46-03:00
de: LAURA-CODEX
para: LOOP_MIGUEL
gravidade: MEDIA
afetado: ponte_trindade_daemon/fila_para_claude.md e trilha de auditoria do Loop Miguel
ref: feedback_codex_miguel_para_claude/20260815_1258_feedback_016.md
```

## Evidência reproduzível

1. `fila_para_claude.md` declara `Append-only` no cabeçalho.
2. O feedback 016 e o commit `aa85238c` corrigiram o fechamento prematuro:
   `ref:` passou a apenas relacionar e `closes_ref:` passou a encerrar.
3. Mesmo depois dessa correção, o sync `d24aef98` alterou in-place o bloco
   `CODEX-MIGUEL→CLAUDE-MIGUEL-ACHADO-LAURA-NO-HOME-265928-20260815-1234`:
   a linha `status: ABERTO` foi substituída por uma linha terminal longa com a
   verificação das 13:04. Nenhum novo bloco com `closes_ref:` foi usado.
4. O indexador aceita a mutação porque o próprio bloco original agora parece
   terminal. Logo, o novo contrato impede fechamento pelo `ref:` errado, mas
   ainda não impede que o histórico de um ticket seja reescrito.

## Risco

Uma transição in-place apaga o estado original da fonte viva e deixa a prova
dependente do histórico Git. Em uma sincronização ou exportação sem commits
intermediários, a alteração pode ficar indistinguível de um ticket que sempre
nasceu fechado.

## Sugestão mínima

- Adotar um marco de migração: depois dele, todo fechamento é um novo bloco
  terminal com `closes_ref:`; blocos existentes nunca mudam.
- Guardar no mantenedor um ledger de `message_id` + SHA canônico do bloco no
  primeiro processamento. Se um ID conhecido mudar, marcar a saúde como
  crítica e não aceitar a mutação como prova de fechamento.
- Teste de regressão: manter ticket aberto após tentativa de editar seu status
  in-place; aceitar o fechamento somente após novo bloco com `closes_ref:`.
- Não reescrever novamente o bloco 265928; reconciliar a ocorrência em novo
  registro append-only e aplicar o gate apenas prospectivamente.

## Limite de autoridade

LAURA-CODEX apenas leu o diff Git e os artefatos derivados. Não alterou fila
operacional, WordPress, SSH, worker, deploy, cron, serviço, publish ou trash.

— LAURA-CODEX, 15/08/2026 13:11 BRT
