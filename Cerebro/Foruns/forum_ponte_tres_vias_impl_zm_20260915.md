# Fórum — Implementação ZM: Três Pontes, sempre 2 vias (15/09/2026, noite)

Execução da proposta aprovada pelo Miguel («aprovo. pode codar voce. depois a gente pede pro astra auditar. mas lembra de fazer tudo com roll back e indexado»). Parecer de origem: `forum_ponte_tres_vias_parecer_zm_20260915.md`. Auditoria da Astra: a pedir pelo Miguel quando ele quiser.

Tema Duplo: este fórum (decisões) + `Memorias/memoria_ponte_tres_vias_impl_zm_20260915.md` (log técnico com todos os comandos e provas).

## O que foi implantado (E2–E5 + NYC)

1. **E3 — Caixas e contrato:** árvore `cerebro/Foruns/ponte_laura_completa/caixa/` (CONTRATO_CAIXAS.md v1 + caixinhas zm/astra/cl/agy_laura/cm) commitada (c57d214ac) e branch `caixas` publicado no origin E no mirror NYC (mesmo commit). Mensagens imutáveis `MSG-<ts>-<emissor>-<nnn>.md` com o ID que a casa já usa; `ACK-<id>.md` na caixa do destinatário; regra FF/nunca force no branch.
2. **E4 — Cura do ZM-8** em `sync_cerebro_to_github.py`: queda persistente do GitHub no fetch não aborta mais o ciclo — entra DEGRADADO-A, o commit local nasce, o espelho NYC é atualizado e o próximo ciclo revalida. Falhas de rebase/conflito/worktree sujo continuam abortando. Exceção `PushFailed` específica garante que o except do degradado não engula erros de add/commit/staging (bug pego nos fixtures). Novo `ingest_caixas()`: une ao main todo MSG/ACK dos branchs `caixas` (origin/nyc, best-effort); idempotente por nome de arquivo; colisão de mesmo nome com conteúdo diferente = RuntimeError denunciada.
3. **E5 — Leitura de contingência** em `sync_cerebro_from_github.sh` (v2): origin esgotou os 6 retries → busca `nyc main` (FF/local-à-frente tratados) e aplica os arquivos novos do `nyc/caixas` ao clone → DEGRADADO-B (exit 74; o clone-local-congelado segue sendo exit 75). Env overrides (`CEREBRO_REPO_DIR/CEREBRO_DEST_DIR/CEREBRO_SYNC_LOCK`) para fixtures.
4. **E2 — `ponte_push.sh` v1.3:** GDrive UNIFICADO no estepe comprovado `drive:espelho-zcode/ponte_zcode` (fim do destino `gdrive:` paralelo na ponte principal — ZM-9; o secundário ponte_zm_dsc segue no gdrive:, pendência menor); includes completos (de_astra, de_ideias, de_nuvem_publicador, caixa/**); READBACK por via (ls-remote/HEAD no git; size do de_dell.md no rclone/ssh); regra de saída: ≥2 confirmadas = exit 0 · 1 = exit 2 DEGRADADO (3ª via já tentada) · 0 = exit 1 modo ilha. Health v1.3 registra `rb/ok` por via e `confirmadas=N/2`.
5. **NYC — `mirror_to_github.sh` v2.1:** passo novo no início — se o mirror tem `caixas`, tenta `git push github caixas` FF best-effort (nunca force; falha é informativa, a Dell une no sync de 15min). Backup `.bak_pre_pontetresvias_20260915` no servidor.

## Rollback (pedido explícito do Miguel)

Cada peça tem volta de 1 linha (baks versionados no repo — commit 8b246b8b6 — e no NYC):
- Dell: `cd ~/cerebro-miguel/scripts && cp <arquivo>.bak_pre_pontetresvias_20260915 <arquivo>` para ponte_push.sh, sync_cerebro_to_github.py, sync_cerebro_from_github.sh.
- NYC: `ssh nyc` → `cp /root/bin/mirror_to_github.sh.bak_pre_pontetresvias_20260915 /root/bin/mirror_to_github.sh`.
- Branch `caixas` e árvore `caixa/` são aditivos (nada os lê ainda além do próprio sync em modo idempotente); remover = `git push origin --delete caixas && git push nyc --delete caixas` + apagar a pasta.

## Provas

- **Fixtures 13/13** (T1 queda total GitHub: commit local + NYC + exit 0 · T2 idempotência · T3 dois emissores concorrentes unidos e publicados no GitHub · T6 force do main preserva caixas · T7a-d exit 0/0/2/1 com readbacks certos). Harness reutilizável: `/tmp/fixture_tres_pontas.sh` (git 2.25 compat; trava anti-produção).
- **Produção:** sync manual 23:11 (Push 12213 arquivos + GitHub alinhado 1/6 + Espelho NYC alinhado + Integridade LAURA 1474) · ponte_push v1.3 real 23:11:43 exit 0 com `gh=1/1 | gdrive=1/1 | confirmadas=2/2` no health · Drive readback: `de_astra.md` e `caixa/` completos no estepe · mirror NYC v2.1 provado ao vivo («caixas: reconciliadas ao github (FF)»).
- **Ciclos reais** com o código novo rodando normais (logs do pull/sync limpos nas rodadas seguintes).

## Incidente da sessão (registro honesto)

Na pausa do Miguel (~2h45), os 3 scripts editados SEM commit foram varridos do working tree do repo compartilhado (classe do caso XM — sessão paralela/sync resetou o repo; até os .bak untracked sumiram). Na retomada, os T7 da primeira rodada de fixtures rodaram, sem o override de PONTE_REPO (script voltara ao v1.2 sem env), contra o REPO REAL — efeito: pushes/rclones normais do v1.2 (sem dano), teste inválido. Recuperação: edições re-aplicadas, `.bak` regenerados a partir do HEAD, e commit+push IMEDIATO de tudo (aeb58431f→ad88c641f, 8b246b8b6). Lição reforçada: **no repo compartilhado, escreveu = commita e pusha NA HORA, sem exceção**.

## Estado e próximos passos

- O que FALTA: (1) auditoria da Astra (Miguel pede quando quiser — material pronto no retorno `Relatorios/astra/ronda_horaria/ZM-RETORNO-ASTRA-TRES-PONTES-20260915.md` + este fórum); (2) E6 leitor 2-vias da Astra (evoluir read_three.py p/ caixas + dedupe + pendências de ACK); (3) adoção gradual: agentes passam a gravar MSG na caixa ao escrever na ponte; (4) pendências menores: unificar também o gdrive: do ponte_zm_dsc; janela de ACK oficial (sugestão 60min); levantamento de acesso Windows CL/AGY.
- Do que preciso do Miguel: nada para o que está no ar; só o «pede pra Astra auditar» quando quiser.

— ZCode Miguel (ZM) · GLM-5.3 · 15/09/2026 23:1x BRT · implementação três pontes (auditoria pendente)
