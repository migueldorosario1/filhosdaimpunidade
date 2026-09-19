# Agendado não é disparo — o evento é a prova (02/09/2026, ronda 70º / DS-20260902-031)

## O quê
O post 268691 (PEC 6x1) estava `future 2026-09-02 18:40:00` — estado de agendamento confirmado
no WP-CLI na ronda anterior (DS-030) — e NÃO disparou às 18:40. Às 18:44 seguia `future` e
`wp cron event list` não listava o evento `publish_future_post` do post: o cron de sistema
(`* * * * * wp cron event run --due-now`) RODA a cada minuto, mas sem evento na fila não há o
que rodar. A CL publicou na mão pelo `cafezinho-cl` às 18:45 e avisou o Miguel. Auditoria da CL:
15/16 posts em `future` tinham evento; o Oracle 268538 (20:09) também não tinha. Padrão novo: os
dois sem evento foram re-salvos com `wp post update --post_status=future --post_date=…` e o
`publish_future_post` não foi recriado em alguns caminhos (mu-plugin de re-slot ou wp-cli).
CL-082 nomeou como recorrência do BUG-DS-098 (mesma classe do furo 05:30 de 31/08 — ficha do
BUG-DS-100: "materialização sem gatilho").

## Por quê
A verificação de "agendado" tinha 1 camada só: o ESTADO (`post_status=future`). Mas future é
uma condição do post; o disparo é um EVENTO na fila do cron. Estado e evento são coisas
independentes — um post pode estar future sem evento (agendado que nunca sobe) e o cron pode
estar vivo sem ter o que disparar. O "verificador de virada" da CL olhou o estado e não pegou a
falta do evento em 4 minutos (18:40→18:44). É a extensão da lição de 02/09 "anúncio de grade não
é prova de ar" (DS-023): agora o PRÓPRIO future não é prova de ar — o future é o plano, o evento
é o gatilho, o ar no REST é o fato.

## Como aplicar
Verificação de slot em 3 camadas, sempre que um post "deveria ter subido":
1. ESTADO: `wp post get <id>` → `post_status=future` (agendado de verdade?)
2. EVENTO (a camada que faltou): `wp cron event list | grep publish_future_post` → o hook existe
   na fila com o GMT certo? Se future sem evento = agendado que nunca vai disparar sozinho.
3. AR: REST topo/permalink HTTP 200 com o post no topo (o fato consumado).

E ao re-salvar um future (troca de slot por frescor, correção de data — caminho que a casa usa o
dia inteiro): conferir se o re-save RECRIOU o evento; se não, agendar na mão
(`wp cron event schedule publish_future_post <gmt> --0=<id>`, sintaxe a validar com o ZM) ou
publicar manual com prova. Vigia também confere evento, não só status.

Refs: CL-20260902-082 · DS-20260902-031 · BUG-DS-098/100 · licoes/20260902_anuncio_de_grade_nao_e_prova_de_ar.md
