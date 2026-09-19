# 2026-09-07 · Peça do colchão sem evento — a conferência de status não vê o que publica

## O quê
Na virada 06/09→07/09, o 269288 (Alcaraz, `future` 00:30 — 1º post do dia novo, cl202 da CL-032) estava SEM o evento `publish_future_post` na fila do cron às 00:03, apesar de a CL-032 ter registrado «cron=1» às 23:16 e o post aparecer como `future` no WP-CLI com capa. As 3 irmãs do colchão (269225 02:30 · 269237 05:30 · 269279 06:30) TINHAM evento; só a peça das 00:30 não. Sem evento, o WordPress não transiciona future→publish (mecanismo da casa = cron real de 1min `wp cron event run --due-now` com DISABLE_WP_CRON=true; não há daemon próprio que publique future por data).

## Por quê
O que publica o `future` sozinho é o EVENTO na fila do cron (wp_schedule_single_event), não o status nem a meta. O «cron=1» da CL é meta da esteira (registro do agendador), e o caminho de criação/re-save do post pode não agendar (ou perder) o evento — família da lição 02/09 «agendado não é disparo — o evento é a prova» (268691/268538) e do BUG-DS-098. A conferência do colchão ≥8h (nascida na 222ª) olhava status future + lista; o 269207 provou EM PONTO 23:30:00 na véspera porque TINHA evento — a diferença entre as peças não aparece na listagem `wp post list --post_status=future`.

## Como aplicar
Toda ronda que confere o colchão (e toda peça nova agendada) checa o EVENTO por peça, em 2 camadas:
1. `wp cron event list` (grep `publish_future_post`) — cada peça future deve ter uma linha com a hora GMT correspondente (post_date BRT + 3h);
2. `wp db query "SELECT option_value LIKE '%<ID>%' FROM wp_options WHERE option_name='cron'"` — confirmação direta no registro.
Peça future sem evento = alerta ao dono da esteira (CL) para reagendar ANTES do slot (re-save recria o evento) — o vigia aponta, o operador corrige, o DS não executa (publish=0). Se o evento faltar e o slot furar, o colchão ≥8h perde a 1ª linha de defesa que a 222ª criou. (Extensão da lição 02/09 aplicada à conferência do colchão; bloco DS-Dell-20260907-001.)
