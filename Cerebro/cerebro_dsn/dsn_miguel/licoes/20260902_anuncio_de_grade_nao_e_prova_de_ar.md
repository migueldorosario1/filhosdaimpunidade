# Anúncio de grade não é prova de ar — 02/09/2026 (DS-023, 62º CHECK)

## O quê
A CL-20260902-074 (carimbo 14:55, ronda 14:42) escreveu "no ar 20 (…Se Eu Fosse Você 14:18 · Anthropic 268594 14:58)" — mas o texto saiu ANTES de 14:58 existir. Às 15:07, três sondas independentes mostraram o contrário do anúncio: WP-CLI status=future com post_date 14:58:00 já passado · REST include=268594 → vazio (cache-busted) · REST posts?after=14:20 → 0 · feed pubDate topo = SEF3 14:18:51 (17:18:51Z). Nada foi publicado entre 14:18:51 e 15:07 — o 1º slot perdido do dia (7 disparos em ponto antes).

## Por quê
"no ar" num bloco pode significar o PLANO da grade (o que está agendado/conferido), não o FATO (o que o servidor publicou). Bloco com hora futura escrita por engano como fato já aconteceu na casa (carimbo textual ≠ commit time — lição do XM-023); aqui a variante é pior porque mistura intenção com realidade: quem lê a ponte acredita que o post subiu. E o future PRESO com post_date no passado é o 1º sintoma de parada do DISPARADOR de agendados (wp-cron/escalonador) — o dígito do future não muda quando o disparador morre; só a sonda do ar mostra.

## Como aplicar
1. Diante de "no ar" para um post com slot futuro ou recente: sondar SEMPRE — REST include=<ID> (com cache-buster), REST posts?after=<hora do slot>, feed pubDates; com acesso, WP-CLI post status/post_date.
2. Diferenciar: re-slot (post_date MUDOU — Emenda 5 remarcou, ex. 268664 14:13→16:56) × disparador parado (post_date no passado, status ainda future) × portão fechado (future=0, decisão de dono).
3. Registrar como watch/anomalia com hora + 3 fontes; não criar BUG- antes do veredito no próximo slot (aqui: Viveros 15:18); avisar os donos (AGY-L/CL esteira · ZM escalonador/wp-cron) com o pedido de verificação e previsão.
4. Volume 3h pode seguir ≥4 (sem alerta formal) mesmo com o disparador parado por ~1h — o colchão e o future íntegro não são o diagnóstico; a janela deslizante é (sem disparo às 15:18/15:38, 3h cai p/ ≤3 ~15:35).
