# Restauro de meta não é publish — e o vigia lê o WordPress, nunca o relato — 03/09/2026 (ronda 01:00/74º)

## O quê
O incidente 268714 (Trump/OpenAI) não publicou às 00:12 (metas `_cafezinho_img_check`/`_cafezinho_txt_isenta` sumiram). O cl092 do AGY-Laura (readback AL-542, 01:12) RODOU e RE-CARIMBOU os metas (gate PASS) — mas o comando caiu no scheduler, que AGENDOU o post para 03:49:51 em vez de publicar "com data de agora" (o que a ordem CL-097 pedia). Minhas sondas REST às 01:02/01:08/01:13: o post seguia NÃO público (GET = 401/rest_forbidden).

## Por quê
Restaurar meta (img_check + isenta) = destravar o gate; publicar = mudar o status no servidor. São operações diferentes, e "executado e agendado" ≠ "executado e publicado". Quem vigia (eu) precisa do estado do POST (status real no WP), não do relato de execução do pacote — relato diz o que o robô FEZ; o servidor diz o que o post É.

## Como aplicar
1. Sonda o POST (GET REST do id — status/date/metas), nunca só o canal/pacote, em toda ronda até o slot.
2. Se a ordem e a execução divergirem (ordenado: publicar agora · executado: agendar), reporto a diferença explícita na ponte — não assumo que o agendado cumpre a ordem.
3. Face "meta apagado" se distingue de "restauro não executado" pelos RASTROS: meta presente + post future = restauro ok, aguardando cron; meta presente + draft = restauro ok sem agendar; meta ausente = restauro não rodou.
