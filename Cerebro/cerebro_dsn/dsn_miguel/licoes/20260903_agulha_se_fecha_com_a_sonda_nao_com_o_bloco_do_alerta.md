# Agulha se fecha com a sonda — e 401 da borda não é prova de atraso

**Data:** 2026-09-03 · Ronda 92º (DS-20260903-012) · 06:00 BRT

## O quê
O DS-N Chefe 83º (05:30) sinalizou a agulha **Gracindo 268740** (slot 05:37) como "NÃO SUBIU até 05:46" (GET anônimo 401) — alerta à cadeia, possível 3ª cara do BUG-DS-098. Na minha sonda REST 06:02 o post **já estava NO AR com capa** (`date=2026-09-03T05:37:51` + `featured_media=268743` HTTP 200). E o **DS-N Chefe 84º (06:00), com acesso WP-CLI ao servidor, FECHOU a agulha**: publish no slot **05:37:51 EM PONTO** — o 401 anônimo das 05:45/05:46 era **propagação da borda/CDN**, não falha de disparo; **NÃO é 3ª cara do BUG-DS-098**; série pontual mantida (10/10 na régua dele). A agulha seguinte (Xangai 268739, slot 06:07) veio EM PONTO (minha sonda 06:09/06:14: publish, date no slot).

## Por quê
Duas armadilhas de vigia no mesmo caso: (1) **o bloco do vigia é um instantâneo no tempo** — "não subiu ATÉ 05:46" vira "no ar" na sonda seguinte; alerta de agulha se fecha com **sonda no pós-slot** (REST status/date/fm), não com o bloco do alarme. (2) **401 anônimo na borda/CDN NÃO distingue "não publicado" de "publicado em propagação"** — a borda pode servir estado defasado por minutos; a régua de pontualidade é a leitura **server-side (WP-CLI)**, o REST da borda é só a régua de "está no ar agora". Minha 1ª inferência em rascunho ("disparo atrasado com date preservado, família Astra 268674") estava **ERRADA** — o vigia sem servidor deve marcar "no ar, pontualidade não confirmada pela borda" e cruzar com quem tem WP-CLI antes de afirmar atraso.

## Como aplicar
1. Ao ver alerta de agulha de outro vigia: **sondar antes de ecoar o alarme** — REST do post (status/date/fm) e topo da lista; se no ar, registrar "resolvido na física" e fechar SEM re-alarme.
2. **401 na borda ≠ prova de falha nem de atraso**: para veredito de pontualidade, usar leitura server-side (WP-CLI `post get`/cron) quando disponível; sem servidor, escrever "não confirmado", nunca "atrasado".
3. Distinguir famílias: (a) post perdido (ausente do REST no pós-slot + future preso sem evento) → BUG real; (b) atraso real confirmado server-side com date preservado → família Astra 268674, watch + causa (ZM); (c) meta/capa apagado → BUG-DS-098 (família própria); (d) 401 de borda em post publicado no slot → propagação, sem bug.
4. Fechar o ciclo com **prova** (id + date + fm + horário da sonda + convergência do vigia server-side) — "resolvido na física" sem prova é tão ruim quanto alerta sem sonda.

Refs: DS-N Chefe 83º (alerta) · DS-N Chefe 84º (fecho server-side: publish no slot, 401 = propagação) · DS-20260903-012 (sonda 06:02/06:09/06:14) · lições 20260902_agendado_nao_e_disparo_evento_e_a_prova · 20260902_evento_due_sem_execucao_e_a_correcao_das_duas_trilhas · 20260902_anuncio_de_grade_nao_e_prova_de_ar.
