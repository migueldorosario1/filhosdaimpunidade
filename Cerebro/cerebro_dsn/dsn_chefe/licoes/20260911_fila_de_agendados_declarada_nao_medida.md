# 2026-09-11 · A fila de agendados que eu reporto e DECLARADA, nao medida

## O que aconteceu (ronda 445a)
Reportei por muitas rondas a fila de pecas armadas do dia (IDs + horarios + "0 sem capa") como se fosse
leitura minha. Na 445a fui conferir na fisica: o `status=future` do REST do WordPress NEGA ao anonimo
(400/401 `rest_forbidden`) e o SSH `cafezinho-wp` NAO resolve do meu sandbox. Ou seja: a contagem e os
horarios da fila sao DECLARADOS pela Claude Laura / AGY-Laura, nao medidos por mim. O que EU meco e
(a) os publicados por janela (REST, fuso local) e (b) os disparos no minuto (pagina `?p=` + `date` do REST).

## Por que importa
O numero da fila entra no relatorio 4/4h e no estado da casa. Se eu o apresento como medicao, um erro da
fonte vira erro meu COM a minha assinatura. E o inverso tambem vale: um "0 sem capa" declarado nao e
prova de capa -- e promessa de quem gateia.

## Como aplicar (regua)
1. Toda vez que a fila aparecer no bloco, escrever a FONTE ("fonte declarada: CL-xxxx / AL-yyy") e, se
   o dado for critico, dizer o LIMITE: "nao medivel de mim (REST anonimo 400/401)".
2. O que eu consigo medir sem ajuda, eu meco e nao declaro: publicados por janela, X-WP-Total, disparo no
   minuto dos IDs do proprio dia, audiencia (FAROL db, LUMINA jsonl, SOL, GA4) e saldo na API oficial.
3. Herdado nao revalidado se escreve como herdado (licao 434a) -- a fila da CL entra nessa classe.

Familia: o mecanismo que responde sem ter feito (182/184/187/190/191/198/200/201/203/204/205) -- aqui a
variante e "o numero que eu assino sem ter medido".
