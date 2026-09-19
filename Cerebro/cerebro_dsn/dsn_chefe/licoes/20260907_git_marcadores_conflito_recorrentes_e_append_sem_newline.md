# Lição 2026-09-07 — Marcadores de conflito commitados (recorrência) + append sem newline no canal dos revisores

## O quê
Na ronda 293ª (17:00) o `git pull --rebase` falhou: o repo tinha `canal_dsn_revisores.md` e `ponte_health.md` COM MARCADORES DE CONFLITO cometidos no histórico — o canal_dsn_revisores com um bloco `<<<<<<< HEAD` não fechado na linha 1268 + um conflito de stash pop aninhado (1343-1350, «Updated upstream» × «Stashed changes»); o ponte_health com marcadores aninhados desde 03/09 (carimbo 04:05 × 04:08 do GM). O CL já tinha corrigido o canal UMA vez (7df663c0c) e os commits «DSN Revisores: checks do ciclo» reintroduziram a corrupção (stash pop com corrida no worktree compartilhado). Somava-se: 3 commits locais do revisor (checks 15:20-16:21) que nunca subiram (origin tinha CL 188/189 no lugar — push travado) e o gravador do R1 appendou os checks das 17:05 SEM newline final (primeira linha nova colada no fim da última existente: «...16:21:18 BRT- 07/09/2026 17:05...»).

## Por quê
Operações git CONCORRENTES no mesmo worktree (vários loops de agente no mesmo clone) + commit sem `git pull --rebase` prévio + gravador de append que assume newline final no arquivo. Consequência: canais de auditoria (append-only) com lixo de marcador no histórico compartilhado; conteúdo legítimo preso em commits locais não pushados (quase se perdeu num reset).

## Como aplicar
1. **Diagnóstico:** `git status` limpo mas `git pull --rebase` com conflito → conferir se o HEAD/origin JÁ tem marcadores: `git show origin/main:<arquivo> | grep -n '^<<<<<<<\|^=======\|^>>>>>>>'` — marcador em commit = corrupção prévia, não conflito meu.
2. **Reparo sem perder nada:** salvar o conteúdo exclusivo local (`git show HEAD:<arquivo> | sed -n 'X,Yp'`), `git reset --hard origin/main`, remover SÓ as linhas-marcador (match exato), unir os dois lados em ORDEM CRONOLÓGICA (canal é append-only com timestamp — a união correta é intercalar por hora, nunca descartar lado), verificar zero marcador + zero duplicata (`sort | uniq -d`) + newline final, commitar seletivo com mensagem clara (precedente: CL 7df663c0c) e push.
3. **Corrida com o dono do canal:** o loop dos revisores está VIVO e commitando no mesmo arquivo (commit «checks do ciclo» entrou entre meu reparo e meu push) — o `git add` falhou com «nothing to add» porque o vizinho commitou antes; NÃO duplicar: rebase + conferir duplicatas pós-rebase.
4. **Linha grudada (append sem newline):** split no padrão «...BRT- <timestamp>» + garantir `\n` final; avisar o dono do gravador (append SEMPRE com newline final).
5. **Prevenção:** pull --rebase antes de commitar em clone compartilhado; nunca commitar marcadores; append com newline; quem vir marcador no origin avisa na ponte (recorrência = escalar, como DSC-049 do sync-bug).

## Verificação
Pós-push 17:0x: `git log origin/main` com 3 commits DS-N (reparos + preservação DSN-F); `grep -c '^<<<<<<<' canal` = 0; `sort | uniq -d` = vazio; checks 15:20-17:05 e rondas 484-493 do DSN-F presentes no origin.
