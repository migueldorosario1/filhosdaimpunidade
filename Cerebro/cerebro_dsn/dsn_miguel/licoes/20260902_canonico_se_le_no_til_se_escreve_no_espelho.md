# 2026-09-02 · O canônico se lê no ~, se escreve no espelho do workspace

## O quê
Nesta sessão o repo canônico `~/cerebro-miguel` ficou **read-only** para o agente
(`git pull` → "cannot open .git/FETCH_HEAD: Sistema de arquivos somente para leitura" —
o sandbox da sessão só grava dentro do workspace). O clone gravável com push para o
origin (github migueldorosario1/cerebro-miguel) é o **espelho dentro do workspace**:
`/home/migueldorosario/Downloads/Antigravity Google/cerebro-miguel`.

## Por quê
O ritual manda ler o canônico e escrever nele + push; se a escrita no `~/` falhar, a
ronda fica sem registro na ponte (ou o agente tenta "consertar" o repo errado e
perde tempo). O caminho de escrita é uma descoberta de INFRA da sessão, não um
capricho: leitura pode ser no `~/` (ou no espelho), escrita e push só no espelho do
workspace.

## Como aplicar
1. Na abertura da ronda: `git -C "$ESP" pull --ff-only origin main` no espelho
   (`ESP="/home/migueldorosario/Downloads/Antigravity Google/cerebro-miguel"`).
2. Append/blocos SEMPRE no espelho; conferir `git status` limpo antes de escrever
   (o daemon `sync` local commita snapshots — se houver mudança local alheia, não
   sobrescrever; append-only).
3. Commit pequeno por arquivo (ponte+grade no MESMO commit — regra-de-ouro) e push.
4. Se o `~/cerebro-miguel` voltar a aceitar escrita em outra sessão, o espelho
   continua sendo a via segura — origin vence o clone local (lição 04:30 reaplicada).
