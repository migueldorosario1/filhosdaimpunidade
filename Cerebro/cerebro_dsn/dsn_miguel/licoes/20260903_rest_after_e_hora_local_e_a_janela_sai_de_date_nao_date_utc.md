# Lição 2026-09-03 — O filtro `after` do REST é hora LOCAL — a janela sai do date, não do date -u

## O quê
Na abertura da ronda 84ª (02:00 BRT), a 1ª sonda de volume usou `after` em UTC
(`date -u -d '3 hours ago'`) e o WordPress REST devolveu `x-wp-total: 0` —
com o topo do site mostrando 4 posts frescos (Dengue 01:57, Werder 01:26,
Mendonça 00:48, Ucrânia 23:51). Calibração empírica em seguida: com
`after=2026-09-02T23:00:00` (hora LOCAL de 3h atrás, sem sufixo de fuso) o
total bateu com a janela real — 5 posts (268424 EUA/China 23:09:11 ·
268710 Ucrânia 23:51:16 · 268728 Mendonça 00:48:42 · 268695 Werder 01:26:59 ·
268700 Dengue 01:57:03). O site publica `date` no fuso local (America/Sao
Paulo, −03) e `date_gmt` = date + 3h; o parâmetro `after` sem sufixo é
interpretado no fuso do site e comparado com a data local.

## Por quê
O WordPress REST (WP core, rest_date_query) converte o `after` assumindo o
timezone configurado do site — passar hora UTC sem o sufixo `Z` desloca a
janela em 3h e pode zerar a contagem mesmo com esteira viva. O dígito 0 é
barato de produzir e caro de interpretar: o vigia que alarmar "esteira morta"
com o topo fresco teria feito um falso positivo (alerta de volume na ponte +
Telegram) por causa de um filtro errado.

## Como aplicar
1. Sonda de volume SEMPRE com hora local: `date -d '3 hours ago'
   +%Y-%m-%dT%H:%M:%S` (sem `-u`), arredondada para HH:00 conforme o rito.
2. O contador certo é o header `x-wp-total` (capturar com `-D -` ou
   `-w "%header{x-wp-total}"`); dígito suspeito (0 ou salto) → listar os posts
   da janela (`per_page=15&_fields=id,date,title`) e conferir com o topo
   ANTES de alarmar.
3. Lembrar que post recuado a `future` (re-espaçamento da fila, não perda)
   sai da contagem de publicados — a janela mede o ar, não a intenção.
4. Se quiser janela em UTC de verdade, mandar o sufixo explícito (`...T05:00:00Z`)
   e lembrar que o site está em UTC−3.
