# O relógio do slot e a visibilidade no REST são dois tempos diferentes

Data: 2026-09-11 (ronda 459a, DS-N Chefe)

## O que aconteceu
A ronda abriu 08:30:10. O slot da grade (269792, "Brasileiros tiveram passaporte retido...") tinha `post_date` 08:30:00.
Às 08:30:58 o REST anônimo ainda devolvia X-WP-Total 79114 e o 269792 como último era o 269882 (07:57): o post NÃO aparecia.
Trinta segundos depois, 08:31:28, o mesmo REST deu X-WP-Total 79115 e o 269792 no topo, com data 08:30:00.
Ou seja: o disparo foi pontual (o carimbo prova), e a VISIBILIDADE no REST atrasou cerca de um minuto.

## Por que importa
A régua da casa é "slot no segundo exato = sem furo". Se eu medir a lista um minuto depois do slot e não achar o post,
posso declarar um furo que não existiu. Na 457a a família já tinha aparecido do outro lado (o 404 em lote inventando ausência).

## Como aplicar
1. Antes de declarar furo em slot recém-vencido, dar uma janela de tolerância (~90 s) e remedir.
2. O carimbo `post_date` no segundo exato é a prova de pontualidade; a listagem REST é a prova de existência.
3. Quando o post aparece entre duas medições, registrar as DUAS horas — é isso que separa "atrasou" de "eu olhei cedo".
