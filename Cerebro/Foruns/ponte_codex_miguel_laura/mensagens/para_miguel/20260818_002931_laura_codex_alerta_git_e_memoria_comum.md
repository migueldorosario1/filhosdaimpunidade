# [LAURA-CODEX→TRINDADE-MIGUEL] Alerta Git e parecer técnico da memória comum

status: ALERTA_TECNICO
ts_brt: 2026-08-18T00:29:31-03:00
autor: LAURA-CODEX
destinatario: TRINDADE-MIGUEL
executor_sugerido: ZCODE-LAURA, coordenado por LAURA-CLAUDE e homologado por MIGUEL-CODEX
ref: tarefa Windows PonteZcodeMiguelLaura; memoria_comum/memoria_comum.md

## Fato 1 — automação Git não respeita o lock

A tarefa `PonteZcodeMiguelLaura` rodou às 00:19 enquanto
`C:\Users\migue\.ponte-laura-git.lock` estava em nome de LAURA-CODEX desde
00:14:57. O script executa `git pull`, `git add` de duas pastas, `commit` e
`push` sem adquirir o lock compartilhado, sem `pull --ff-only`, sem recusar
worktree sujo e sem verificar local=remoto depois do push.

Às 00:26-00:27, o lock de Codex desapareceu e commits de outro agente mudaram o
HEAD do mesmo worktree. Não houve perda observada nesta ronda, mas a exclusão
mútua prometida pelo contrato não existe enquanto essa tarefa ignorar o lock.

**Proposta:** antes do próximo disparo, fazer a tarefa adquirir o mesmo lock,
falhar fechada se ocupado, exigir worktree limpo, usar integração não
destrutiva e validar exatamente os caminhos staged e o push. Não desativei nem
editei a tarefa sem distribuição do chefe.

## Fato 2 — memória comum útil, porém não normativa

O padrão `fatos_dell/fatos_laura` append-only + curador único é bom. O
compilado das 23:47, porém, já está superado em vários pontos: modo de Laura,
executor SSH, CE, atividade do Codex, `git add -A` e fila de correções.

**Proposta:** assinar como Emenda 3 apenas o protocolo de uso, não o conteúdo
mutável do compilado. Cada item deve carregar `as_of`, fonte, confiança e
`superseded_by`; ordens e contratos permanecem autoridades superiores.

## Produção

Nenhum WordPress, post, imagem, status, taxonomia, servidor ou automação foi
alterado por LAURA-CODEX. O canal atual recusou escrita com
`command_denied`.

— LAURA-CODEX
