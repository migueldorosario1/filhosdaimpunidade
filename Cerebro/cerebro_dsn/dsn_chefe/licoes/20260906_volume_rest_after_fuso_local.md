# Lição — Filtro `after` do REST do WordPress compara com o post_date LOCAL, não UTC (ronda 225ª, 06/09 05:30)

**O quê:** na contagem de volume da ronda (REST canônico www.ocafezinho.com), usei `after=$(date -u -d '12 hours ago' ...)` (UTC) e a janela de 12h veio **5 posts** — quando a mesma janela, medida com fuso local, tem **9**. Quatro posts (269153 18:06 · 269155 18:39 · 269156 19:28 · 269158 19:48, todos de 05/09 BRT) sumiram da contagem sem terem saído do publish (prova: per-ID todos `publish` + HTTP 200).

**Por quê:** o parâmetro `after` do WP REST é comparado contra o `post_date` LOCAL do site (America/Sao_Paulo), não contra UTC — um valor sem fuso informado (ex.: `2026-09-05T20:30:00`) é interpretado como 20:30 BRT e corta os posts anteriores às 20:30 BRT mesmo que sejam posteriores às 20:30 UTC. Prova empírica por borda: `after=18:00` → 9 · `after=19:00` → 7 · `after=20:00` → 5 · `after=20:30` → 5 · `after=21:00` → 5 (todos em hora local).

**Como aplicar:** nas contagens de volume (3h/12h/24h) usar SEMPRE fuso local: `date -d 'N hours ago' +%Y-%m-%dT%H:%M:%S` (sem `-u`) — é o método da série (o DS-Dell marca "fuso local" e bate com os números históricos). Se usar `date -u`, a janela desliza para a direita em horas e SUBCONTA posts legítimos — o erro se disfarça de "borda" mas é filtro errado. Antes de declarar queda de contagem, conferir por ID os posts que deveriam estar na janela (método da lição do DS-Miguel: comparar lista, não só total).

**Verificação:** ronda 225ª 05:30: 12h UTC = 5 (errado) → 12h fuso local = 9 (correto, bate com a aritmética da borda 269146 17:08 saindo da janela das 10h da 224ª).
