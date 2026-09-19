# Lição — O relatório 4/4h do Chefe sai pelo canal do Chefe (não pelo do DSC)

- **Data:** 2026-09-05 (identificada no áudio do Miguel 20:11:11, fix executado pelo DSC-us65 20:2x, verificada por mim na ronda 208º 20:36)
- **Refs:** ordem Miguel 20:11 (áudio via @dscelular_bot); fix DSH-us65 20:29; bloco DS-N-20260905-208

## O quê
O relatório 4/4h do DS Nuvem Chefe (DS-N Chefe) estava chegando ao Miguel pelo @dscelular_bot (canal do DSC), não pelo @Dsnchefe_bot (canal do Chefe). O Miguel notou a confusão: "esse relatório de 4 em 4 horas, ele é do DSN-Chefe, não do DSC... vamos ter que corrigir isso também".

## Por quê (causa raiz, provada pelo DSC-us65)
O `/home/ubuntu/ronda_dsn.sh` (Tencent) exportava `TELEGRAM_TOKEN_DSC_BOT`/`DSC_BOT_CHAT_ID` e a linha 39 do prompt da ronda mandava o curl de envio direto por esse par — ou seja, o relatório do Chefe saía pelo bot do DSC. O carteiro v1.2 do us65 já roteava certo (blocos Chefe → @Dsnchefe_bot); o buraco era só o curl direto da ronda.

## Como aplicar (o fix e a verificação)
1. O script e o prompt da ronda usam `TELEGRAM_TOKEN_DSN_CHEFE_BOT`/`DSN_CHEFE_BOT_CHAT_ID` (@Dsnchefe_bot — mesmo canal da escuta flash).
2. Conferir no script: comentário de auditoria + export das 2 vars do `.env.unificado` (bash -n OK; grep do curl antigo = 0).
3. Vigiar o 1º relatório no canal certo: 00:00 BRT (o 20:00/msg 209 foi o último pelo canal errado).
4. Backups do fix: `ronda_dsn.sh.bak_pre_canal_dsn_20260905_2021` + `ronda_dsn_prompt.md.bak_pre_canal_dsn_20260905_2021`.

## Lição geral
Cada robô com bot próprio (escuta, rondas, carteiro) precisa conferir QUAL par de vars o script de envio usa — um curl direto com as vars do bot errado entrega a mensagem do Chefe no canal do vizinho sem nenhum erro visível. Verificação barata: grep das vars TELEGRAM_TOKEN_* no script da ronda + conferir o canal de 1 mensagem real.

— DS Nuvem Chefe (DS-N Chefe) · 20260905 20:37 BRT
