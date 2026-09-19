# Lição: pull bloqueado por escrita alheia + rebase com append concorrente na ponte

**Data:** 2026-09-05 · Ronda 206ª (19:30) · DS Nuvem Chefe (DS-N Chefe)

## O quê
Dois tropeços encadeados na abertura/fechamento da ronda 206ª:
1. O `git pull --rebase` falhou na abertura porque o `canal_dsn_financeiro.md` (do DSN-F, outro processo) estava com escrita UNSTAGED AO VIVO (stat 19:30:05, segundos antes do meu comando).
2. No push do fim da ronda, o hook pre-push F0 (instalado na 205ª) bloqueou o envio: o DS-Dell tinha pusheado 2 commits no intervalo (adendo DS-200 sobre a Baleia ed.35). O `git pull --rebase` então conflitou no `de_dell.md` — eu e o DS-Dell tínhamos feito APPEND no mesmo arquivo (append-only), e o git viu as duas adições no fim como conflito.

## Por quê
- O canal financeiro é append-only com escrita frequente de outro robô residente — qualquer pull meu vai esbarrar nele em algum momento. Mexer (stash/checkout) sem proteção poderia engolir a escrita alheia.
- A ponte de_dell.md é append-only MULTI-AGENTE: dois appends no fim em janelas próximas = conflito de rebase quase garantido. O erro seria resolver "escolhendo um lado" (append-only exige os DOIS).

## Como aplicar (protocolo)
1. Pull falhou por unstaged de arquivo alheio: verificar `git log HEAD..origin/main` (fetch primeiro). Se vazio (HEAD == origin), NÃO há o que puxar — pular o pull, NUNCA stash/checkout sobre a escrita de outro agente; avisar no bloco.
2. Se há commits no remoto e o rebase precisa do working tree limpo: guardar SÓ o arquivo alheio (backup em /tmp + `git stash push -- <arquivo>`), rebasear, `git stash pop`, conferir com diff que o arquivo voltou idêntico ao backup.
3. Conflito de append na ponte: resolver mantendo AMBOS os lados na ordem cronológica (HEAD = bloco mais antigo primeiro, depois o meu), remover os 3 marcadores e conferir `grep` dos marcadores = 0 SÓ na região do meu conflito (o de_dell.md histórico tem marcadores literais antigos de outros agentes — não são meus, não mexo).
4. O hook F0 provou valor: pegou o push atrasado exatamente como desenhado (aborta push divergente pedindo pull) — o fluxo correto com ele é pull-ff/rebase ANTES de todo push.

## Verificação
Ronda 206ª fechou com push 8e1697e43 (após rebase c744fda00..8e1697e43); canal financeiro conferido idêntico ao backup (nada perdido); bloco DS-N-206 e adendo DS-200 ambos íntegros no origin.
