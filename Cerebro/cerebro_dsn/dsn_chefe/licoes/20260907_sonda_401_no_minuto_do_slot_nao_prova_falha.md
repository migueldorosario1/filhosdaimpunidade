# Lição 2026-09-07 — Sonda REST com 401 no minuto do slot NÃO prova falha de disparo (ronda 300ª)

## O quê
Na ronda 300ª (slot 20:30, 07/09), o post agendado 269373 (ONU/IA, future 20:30:00 com evento no cron) respondeu **HTTP 401** à sonda REST per-ID feita às 20:31 — exatamente 1 minuto após o horário do disparo. Pelo padrão da série (401 = future/private/draft), a leitura inicial parecia indicar "não saiu no minuto". A re-sonda às 20:36 retornou **HTTP 200, status `publish`, date 20:30:00** — o post estava no ar.

## Por quê
O WordPress mantém a `post_date` ORIGINAL agendada (20:30:00) mesmo quando o cron dispara com pequeno atraso (próximo tick), e camadas de cache/CDN podem servir o estado anterior ("future") por 1-5 minutos após a publicação. Ou seja: sonda única no minuto do slot pode pegar o intervalo entre o disparo real e a propagação — e o 401 aí é LAG, não FALHA.

## Como aplicar (protocolo de vigília de disparo)
1. Sonda per-ID SEMPRE com cache-buster (`?cb=<timestamp>`).
2. Sonda no minuto do slot que retornar 401 (ou 404) NÃO é prova de falha: **re-sondar 3-5 minutos depois** antes de avisar "não saiu" na ponte (evita alarme falso — a casa já teve 3 alarmes falsos no dia por outros motivos; falso alarme de disparo desgasta a confiança na vigília).
3. Declarar "EM PONTO" só com confirmação: REST per-ID `publish` + `date` = horário agendado (o `date` mantém o horário original mesmo com lag de cron).
4. Falha real = re-sonda após 5-10 min ainda 401/404 + sem o post na lista pública — aí sim avisar o watch (DS-Dell/CL).
