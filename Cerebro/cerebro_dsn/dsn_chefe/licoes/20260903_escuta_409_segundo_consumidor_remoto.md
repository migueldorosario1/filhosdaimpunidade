# Escuta com 409 persistente = 2º consumidor do bot (02/09 19:40 → 03/09)

Data: 03/09/2026 (ronda 03:30, 79º CHECK). Achado de vigília do Loop A.

## O quê
O log da escuta (`~/ds_nuvem_chefe/escuta.log`) mostra HTTP 409 Conflict do Telegram
getUpdates de forma PERSISTENTE desde 02/09 19:40:02 (~661 ocorrências até 03:32,
cadência de ~1 a cada 42s = o backoff de 30s + tentativa). O 409 do Telegram significa
"terminated by other getUpdates request" — outro consumidor está disputando o MESMO bot
(@Dsnchefe_bot, token TELEGRAM_TOKEN_DSN_CHEFE_BOT).

## Por quê
Verificação feita na ronda: (a) só UM processo escuta.py roda nesta Tencent (PID único,
systemd ds-nuvem-chefe-escuta, single-loop `getUpdates offset+1 timeout=25` — conferido
no código, linhas 202-204); (b) `ss` mostra só 1 conexão ESTAB ativa com Telegram daqui;
(c) maira_bot.py usa OUTRO bot (@mayranpraia_bot) — não conflita. Logo o 2º consumidor é
REMOTO. Suspeito nº 1: o `carteiro-dsn-chefe.service` no us65 (criado pelo ZM ~20:20 de
02/09 para entregar meus blocos de RESPOSTAS.md "na hora") — SE ele também der getUpdates
no @Dsnchefe_bot, viola a regra da casa (Loop A = consumidor ÚNICO). O início dos 409s
(19:40 de 02/09) coincide com a migração do bot. us65 não resolve por DNS nesta sandbox —
não confirmei o processo de lá (não confirmado, resposta honesta).

Evidência de impacto: MESMO durante o conflito, mensagens chegaram e foram respondidas
flash (19:40:58 e 21:14:20, lat 2s — as "Oi" e "Não usa *" do INBOX). INBOX sem msg nova
pós-21:14 de 02/09 → sem perda confirmada, mas o risco é real: consumidor duplo rouba
mensagens (offset avança no lado errado) e o 409 é o sintoma.

## Como aplicar
1. O daemon tem backoff próprio e segue vivo (heartbeat 1x/h) — NÃO reiniciar à toa nem
   mexer no offset à mão; a escuta vence o slot eventualmente.
2. Reportar ao ZM/DSC: o carteiro do us65 deve VIGIAR O REPO (RESPOSTAS.md), nunca dar
   getUpdates — só a escuta tencent consome o bot (regra permanente).
3. Watch: se o Miguel mandar mensagem e não houver resposta flash em ~1 min, escalar na
   hora (CONTEXTO_MINI 03:30 já instrui o plantão a avisar o Chefe).
4. Ronda de abertura: além do git pull + canal raiz, dar uma olhada no tail do escuta.log
   — "ativo" no systemctl não diz que o getUpdates está vencendo.

## Update 04:00 (80º CHECK, 03/09) — evidência endureceu
- Ocorrências: 661 (03:32) → **701 (04:00)** — o 409 NÃO parou; cadência estável ~42s.
- Trecho 03:30–04:01: **100% das tentativas de getUpdates com 409** (só o heartbeat 03:30:45 passou) — ou seja, há trechos em que a escuta fica sem ler NADA; as leituras acontecem só nas janelas em que o consumidor remoto libera o long poll (prova: 21:14:20 "msg respondida flash lat=2s" entre 409s contínuos).
- Escuta.py confirmado (grep): token = TELEGRAM_TOKEN_DSN_CHEFE_BOT, bot exclusivo @Dsnchefe_bot, single-loop — 1 processo local (PID 3355105, systemd desde 17:04 02/09), crontab ubuntu sem entrada de escuta.
- Suspeito nº 1 reforçado pela linha histórica da ponte (de_laura ~20:20 02/09, ZM): o `carteiro-dsn-chefe.service` (us65) foi criado com a descrição "escuta Miguel (flash-ack honesto...)" — se ele dá getUpdates no @Dsnchefe_bot, é a fonte exata (início dos 409s 19:40 ≈ ativação do serviço). us65 segue fora do alcance desta sandbox — NÃO CONFIRMADO (resposta honesta mantida).
- Estado: sem perda de mensagem confirmada (INBOX sem msg nova pós-21:14 02/09), mas risco de mensagem presa cresce a cada hora de conflito. Contenção = elo humano/remoto (ZM/Dell conferir o us65); localmente a escuta segue viva com backoff próprio — não mexer.
