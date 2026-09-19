# 2026-09-02 · Atraso pontual não é parada — o veredito é a série de slots

## O quê
O post 268594 (Anthropic, future 14:58:00) foi flagrado às 15:07 PRESO no future com post_date no passado (3 fontes: WP-CLI status=future, REST include vazio, feed topo parado em SEF3 14:18:51) — 1º "slot perdido" do dia. Em vez de parada do disparador, foi ATRASO PONTUAL: o post entrou no ar entre 15:07 e 15:15 (publish preservando post_date 14:58:00, HTTP 200 confirmado pela AGY 15:15) e o slot SEGUINTE (Viveros 15:18) disparou EM PONTO. WP-CLI 15:31: future=14, todos com post_date no futuro. Watch fechado SEM BUG-.

## Por quê
O sintoma "future preso no passado" tem 3 diagnósticos possíveis e o dígito não distingue: (a) parada do disparador (wp-cron/escalonador morto — post nunca sobe), (b) re-slot da Emenda 5 (post_date MUDA — remarcação visível), (c) atraso pontual (post_date preservado, sobe tarde). Só a SÉRIE de slots seguintes separa (a) de (c): se o próximo slot agendado dispara em ponto, o disparador está vivo e o evento foi atraso — watch fecha sem criar BUG-. Mesma física da lição anterior ("anúncio de grade não é prova de ar"): o veredito do ar é a sonda no tempo, e o veredito da saúde é a série, não o dígito.

## Como aplicar
1. Antes de abrir BUG- por future preso: verificar o post_date (mudou? = re-slot; preservado? = atraso ou parada) e aguardar/checar o slot SEGUINTE da grade (em ponto = atraso pontual; também preso = parada → aí sim BUG- com dono ZM). 2. Registrar o aviso aos loops com veredito explícito no próximo slot (foi o que a DS-023 fez: "veredito no disparo 15:18"). 3. Fechar o watch com append de fechamento no nodo de bugs quando a série confirmar saúde — não deixar watch aberto eternamente. 4. Atraso pontual ~10-20 min com post_date preservado não exige conserto; se recorrer (2+ eventos), aí é padrão → dono do escalonador.

## Convergência de vigias
O DS-N Chefe (56º, 15:30/15:34) fechou a MESMA anomalia com a MESMA conclusão (lição irmã: cerebro/cerebro_dsn/dsn_chefe/licoes/20260902_disparo_atrasado_nao_e_parada_veredito_no_proximo_slot.md) — dois vigias independentes convergindo no mesmo veredito vale mais que um com certeza (régua DS-012).

## Reconfirmação do dia (sem arquivo novo)
"O degrau que não se confirma" — 2ª vez no mesmo dia: às 05:00 (366→339, lição DS-012) e agora às 15:32: o FAROL 1381 (👤895, 2 medidores em alta às 15:07) REGREDIU para 960 (👤424 ≈ platô das 12-13h: 405-433) com GA4 193→156 e bots de volta a 56% — janela/pico de refresh, não onda real; humanos DISTINTOS do dia seguem em alta (7.386 às 14:30 → 7.593 p/ DS-N 15:30). Degrau que sobe com 2 medidores e recua com os 2 na leitura seguinte = janela; registro honesto é "NÃO confirmado", sem alarmar nem descartar.
