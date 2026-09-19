# Queda de contagem por mudança de tipo não é perda de post

Data: 2026-09-10 12:30 BRT · Autor: DS Nuvem Chefe (DS-N Chefe) · Ronda 424a

## O quê
A contagem do dia caiu de 14 para 13 posts entre a ronda das 12:04 e a das 12:30, sem
nenhum post ter sido despublicado. Causa: o publipost 269729 foi reclassificado de
`post` para `page` por ordem direta do dono (executado no canônico com
`wp post update 269729 --post_type=page`, liberado pela porta de intervenção humana
consciente do mu-plugin de proteção editorial, depois de a primeira tentativa ter sido
barrada com motivo `post_publicado_por_humano`).

O endpoint de posts (`/wp-json/wp/v2/posts`) passou a não devolvê-lo — e o número do dia
"caiu". A peça continua no ar, com o mesmo conteúdo, em URL de página.

## Por quê importa
Um número de produção que cai é lido como incidente (post perdido, reversão, falha do
cron). Aqui não houve nada disso: houve mudança de TIPO. Se eu tivesse reportado "14 -> 13"
como perda sem conferir, teria alarmado o dono com um fato falso no mesmo dia em que a
ordem de reclassificar partiu dele.

## Como aplicar
1. Toda queda de contagem entre duas leituras se confere por ID, não por total: pegar a
   lista das duas janelas e ver QUAL ID saiu.
2. Antes de declarar perda, testar três hipóteses baratas: (a) mudou de `post_type`
   (post -> page, ou o inverso); (b) voltou a rascunho/futuro (mudança de `status`);
   (c) entrou em lixeira. Cada uma tem assinatura diferente no REST per-ID.
3. No relatório, separar sempre: "post que saiu do ar" ≠ "post que saiu da LISTA que eu
   consulto". A lista é um recorte (tipo + status), não o inventário do site.
4. Mudança de tipo feita pelo dono é ordem cumprida, não anomalia — e a regra que ela
   fixou (notícia/editorial = post; comercial/promocional/serviço de terceiros = página)
   vira critério editorial da casa, não só conserto pontual.

## Prova desta rodada
REST per-ID do 269729 = `post_type=page`, `status=publish`, URL em formato de página,
HTTP 200. As duas listas (12:04 e 12:30) diferem por um único ID — o mesmo 269729.
