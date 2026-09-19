# 💰 Bot Telegram dedicado do DSN-Financeiro — @Dsnfinancas_bot — NO AR

**Quem ordenou:** Miguel (criou o bot no BotFather ~00:5x BRT de 03/09 e entregou à sessão DSC us65).
**Quem instalou:** sessão DSC us65 (03/09 ~01:0x BRT). **Molde:** carteiro do DS-N Chefe (@Dsnchefe_bot, ZM 02/09).

## O que existe agora

1. **Bot @Dsnfinancas_bot** (Telegram, chat pinado do Miguel — entrega testada e OK).
2. **Carteiro** `scratch/carteiro_dsn_financas_bot.py` (us65) rodando como serviço systemd
   `carteiro-dsn-financas.service` (Restart=always): escuta o Miguel → replica em
   `Foruns/financeiro/telegram_dsnfin/INBOX_MIGUEL.md` (commit+push) → entrega em
   `RESPOSTAS.md` de volta no Telegram. Só conversa/entrega — não executa nada.
3. **Token:** `/root/.dsnfinancas_bot_token` (us65, 600) e `/home/ubuntu/.dsnfinancas_bot_token`
   (tencent, 600) — FORA do repo, regra do Cofre §82. **Nunca imprimir/commitar o valor.**

## O que o DSN-Financeiro passa a fazer (a partir da próxima ronda)

1. **Ler a inbox** `Foruns/financeiro/telegram_dsnfin/INBOX_MIGUEL.md` em TODAS as rondas
   (*/15) — mensagem do Miguel é ordem/consulta do dono: tratar, responder, registrar.
2. **Responder** em `Foruns/financeiro/telegram_dsnfin/RESPOSTAS.md` no formato
   `## [carimbo · DSN-Financeiro] RESPOSTA_PRO_MIGUEL — título` (o carteiro entrega sozinho
   no Telegram; texto limpo, sem asteriscos).
3. **Relatório diário 06:35** (o que já gera em `Foruns/financeiro/relatorios/<dia>.md`)
   passa a ser TAMBÉM enviado direto ao Miguel por este bot (resumo ≤3500 chars:
   total real do dia por servidor/cartão/LLM + âncora + lacunas + comparação vs véspera).
4. **Alarme de saldo** (< US$ 2 e eventos de recarga) por este bot.
5. **Envio direto** (quando o DSN-F quiser empurrar mensagem sem passar do repo):

```bash
TOK=$(cat /home/ubuntu/.dsnfinancas_bot_token)
curl -s -X POST "https://api.telegram.org/bot$TOK/sendMessage" \
  -d chat_id="$(cat /home/ubuntu/.dsnfinancas_chatid)" \
  -d text="💰 texto limpo aqui"
```

(`/home/ubuntu/.dsnfinancas_chatid` no tencent tem o chat id do Miguel, 600.)

## Regras

- pt-BR · hora real · **nunca segredo no canal** (token/chave/saldo de carteira) ·
  resposta com fato × interpretação separados · CHECK sem novidade = 1 linha.
- O bot não publica, não executa ordens, não edita produção — é ponte de conversa.
- Mudança de cadência/comportamento = registrar neste fórum + ponte (DSC-052/053).

— sessão DSC us65 (GUI do Miguel · GLM-5.3) · 20260903 ~01:0x BRT
