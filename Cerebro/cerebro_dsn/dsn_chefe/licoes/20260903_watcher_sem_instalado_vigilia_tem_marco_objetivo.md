# Vigília com marco objetivo: watcher no ar sem "INSTALADO" não é "feito" (DSC-062)

**Data:** 2026-09-03 (ronda 02:30 — 77º CHECK, DS-N-20260903-005)

## O quê
O DSC-20260903-062 (FALA DO MIGUEL ~01:5x) montou a cadeia automática do V4.2: watcher no tencent (`~/v42_investimento_teste/watcher_v42.sh`, cron */10, auto-expira) que detecta as creds sozinho → extrai o script do Ideias do repo canônico → cria o cron do teste (14:00 dias úteis, com backup do crontab) → se desliga e loga "INSTALADO". Minha missão na cadeia: avisar o Miguel no Telegram QUANDO INSTALAR. Na ronda 02:30 o log do watcher mostrava apenas "watcher rodando" (ciclos 02:03/02:10/02:20/02:30) — sem a linha INSTALADO, porque as creds ainda não foram espelhadas (aguarda o ACK do ZM escolhendo a casa entre o plano NYC do DSC-060 e a cadeia do DSC-062).

## Por quê
A tentação da vigília é transformar "o mecanismo está no ar" em "a missão está cumprida". Não está: minha entrega é acionada por MARCO (a linha "INSTALADO" no log do watcher), não por tempo decorrido nem por o watcher estar rodando. Avisar o Miguel antes do marco seria falso aviso (e queimaria a confiança de quem pediu "solução automática que eu não precise fazer nada"); não conferir o log seria negligência de vigia.

## Como aplicar
1. Toda vigília minha tem gatilho objetivo e escrito: log com palavra-chave ("INSTALADO"), slot de cron (268714 03:49:51), post no espelho (1º teste V4.2), etc.
2. Enquanto o gatilho não dispara, a entrega da ronda é o REGISTRO HONESTO do estado (log conferido, o que falta para o marco: ACK do ZM + espelhamento das creds) — nunca reportar "feito" pelo que ainda não aconteceu (mesma régua da vigília da promulgação de 01/09 e do "restauro ≠ publish" da 01:00).
3. Quando o marco aparecer, avisar o Miguel com PROVA (a linha do log / o post no espelho) e assinatura completa.
4. Conferir o log em CADA ronda 30/30 enquanto a vigília estiver aberta (a cadeia pode instalar a qualquer momento entre os ciclos de 10 min do watcher).

## Atualização (ronda 03:00 — 78º CHECK, DSC-063)
O OK TRIPLO do Miguel na GUI (~02:4x, DSC-063) APROVOU o desenho V4.2 e AUTORIZOU a instalação da fase teste no espelho — mas o log do watcher às 03:00 segue "watcher rodando", SEM "INSTALADO". Lição que se soma à de cima: **a aprovação do dono move o PROCESSO, não o estado técnico** — o aval do Miguel é mais um elo da cadeia (não o último): falta o ACK do ZM escolhendo a casa + o espelhamento das creds ESPELHO_WP_* no cofre tencent (msg 144 do DSC). Vigiador com marco objetivo não confunde "autorizado" com "instalado": o gatilho do meu aviso ao Miguel continua sendo a linha INSTALADO no log (ou o 1º rascunho _v42_* no espelho), e a entrega honesta da ronda é o registro do estado real com o que falta. Como aplicar: quando uma ordem passar por vários elos, escrever o estado de CADA elo (aprovado ✓ · ACK do instalador pendente · creds não espelhadas · watcher rodando) em vez de resumir pelo elo mais recente.
