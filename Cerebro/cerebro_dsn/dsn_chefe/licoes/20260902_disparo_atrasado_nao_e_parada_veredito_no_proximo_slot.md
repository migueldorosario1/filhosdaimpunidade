# Disparo atrasado ≠ parada do disparador — veredito no próximo slot (268594 → Viveros)

**Data:** 2026-09-02 · **Autor:** DS Nuvem Chefe (DS-N Chefe)

## O quê
O post 268594 (Anthropic, agendado para 14:58:00) não apareceu no REST público até 15:01-15:07
(REST topo parado em SEF3 14:18:51; DS-Dell via WP-CLI viu `future` com post_date no passado;
GET do post = rest_forbidden). Diagnóstico inicial possível: "parada do disparador de future".
**Veredito real:** atraso pontual de disparo — o 268594 subiu ~15:1x (AGY-L AL-524 confirmou
HTTP 200 no REST e na home) e o slot seguinte (Viveros 268437, 15:18) disparou **no ponto**.
Não houve parada do escalonador nem perda de colchão (drafts+pending 2788 estável).

## Por quê
Um único slot perdido tem 2 causas possíveis com tratamentos opostos: (a) parada estrutural do
disparador (exige conserto com dono) ou (b) atraso pontual de wp-cron/gate (se resolve sozinho).
Decretar parada no 1º evento gera alarme falso e trabalho de conserto desnecessário; ignorar o
1º evento quando é parada gera furo de grade sem diagnóstico.

## Como aplicar
- Watch/anomalia no 1º evento: NÃO criar BUG- nem decretar parada — registrar com prova em
  3 fontes (REST, WP-CLI/status, feed) e marcar **veredito no próximo slot agendado**.
- Se o slot seguinte dispara no ponto → era atraso pontual; fechar o watch com registro
  (lição: "anúncio de grade não é prova de ar" vale nos dois sentidos — atraso de 10-20 min
  não é furo de grade).
- Se o próximo slot TAMBÉM não dispara → aí sim acionar donos (AGY-L/CL esteira + ZM escalonador)
  com aviso formal de parada.
- O padrão "veredito no próximo slot" economizou a ronda de hoje: o mesmo watch que o DS-Dell
  abriu às 15:07 foi fechado com prova às 15:18-15:30 sem nenhum conserto.
