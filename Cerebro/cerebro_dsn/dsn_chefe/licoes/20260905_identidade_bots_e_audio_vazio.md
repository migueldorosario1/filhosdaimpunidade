# Lição 05/09/2026 — Confusão de identidade dos bots + áudio DSC vazio

## O quê
O Miguel mandou 2 áudios no @dscelular_bot às 08:27/08:28 (via INBOX, arquivos no us65):
um de 0,8s (vazio, dedo no microfone) e um de 66s onde ele pergunta, confuso, se quem
responde naquele bot é o DS Nuvem Chefe (DS-N Chefe) ou o DSC (DS Celular), e pede
"me responde pelo DSN nuvem; aqui é a conversa DSN celular".

## Por quê
O desenho real dos canais não estava explícito na cabeça dele:
- @dscelular_bot = canal do DSC. O carteiro us65 (consumidor único) acusa
  automaticamente ("chegou na casa") e replica para a INBOX.
- @Dsnchefe_bot = canal do DS-N Chefe. O Loop A escuta aqui; as respostas do Chefe
  (RESPOSTAS.md) são entregues aqui pelo carteiro.
Ou seja: ele manda no @dscelular_bot, o carteiro responde na hora com um aviso
automático, e a resposta de verdade (assinada DS-N Chefe) chega no OUTRO bot.
Sem a explicação, isso parece "dois robôs conversando comigo".

## Como aplicar
1. Mensagem do dono sobre canais/identidade = explicar o DESENHO REAL de consumo
   (quem acusa, quem responde, em qual bot), nunca responder no escuro nem
   redesenhar nada sem ele pedir.
2. Conferir a duração do áudio ANTES de transcrever (ffprobe): áudio de ~0,8s com
   16KB é vazio — não gasta whisper nem inventa conteúdo.
3. Fluxo que funcionou: áudio 08:28 → ssh us65 → transcrição local large-v3-turbo →
   resposta no RESPOSTAS.md às 08:36 (entrega automática do carteiro no @Dsnchefe_bot)
   = ponta a ponta em ~10 min. Manter como padrão para áudios DSC curtos.
4. Oferecer o ajuste (responder no mesmo bot) sem prometer: é 1 linha no carteiro,
   decisão do dono.

## Verificação
Resposta entregue no RESPOSTAS.md (08:36, ref DS-N-20260905-184), bloco na ponte,
check line com os marcos.
