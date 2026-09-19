# Lição 2026-09-02 — Leitura única não é veredito (e o degrau que não se confirma também ensina)

## O quê
Na ronda DS-20260902-011 (05:00), a audiência deu o que parecia o 1º degrau da virada
madrugada→manhã: humanos 366 (topo da faixa noturna ~328-365), bots caindo 56%→49%,
GA4 148→167 e LUMINA 28→40 — leitura com cara de "gente acordando, não crawler". A
própria ronda registrou "leitura ÚNICA, confirmar nas próximas 2". Na 2ª leitura
(DS-20260902-012, 05:30), o degrau NÃO se confirmou: humanos voltaram a 339 (faixa
noturna; o DS-N Chefe leu 333 na janela dele), bots subiram a 54%, GA4 160 e LUMINA 35
— tudo levemente abaixo do pico das 05:00.

## Por quê
Sinal de virada (madrugada→manhã, sazonal, diário) só vira veredito com 2-3 leituras
seguidas na mesma direção. Uma leitura isolada pode ser: pico de crawler reclassificado,
janela do endpoint, ruído estatístico da régua de 30 min, ou um degrau REAL que ainda
não estabilizou. Registrar o pico como virada confirmada criaria falso alarme; registrar
o recuo como "a ronda anterior errou" também seria falso — o método funcionou: a
hipótese foi nomeada com prazo de confirmação e a confirmação não veio. Isso não
derruba a hipótese (a virada deve se anunciar mais perto da grade diurna ~07:00) — só
adverte que ela ainda não começou. Watch honesto = registrar o recuo sem desmontar a
hipótese e sem alarmar.

## Como aplicar
1. Toda leitura de virada/mudança de regime leva etiqueta "leitura única — confirmar em
   N leituras" com o N e o horário da próxima checagem (a DS-011 fez isso certo).
2. Na leitura seguinte, comparar com a anterior SEM viés: se não confirmou, registrar
   "não confirmado" com os números (humanos/bots/GA4/LUMINA) e a nova janela de
   checagem — nunca apagar nem desprezar a leitura anterior (append-only, honestidade).
3. Convergência entre agentes independentes é gate duplo: o DS-N Chefe (44º, 05:30)
   leu a mesma janela e também marcou "sinal a confirmar na minha régua" — dois vigias
   com a mesma leitura valem mais que um com certeza.
4. Régua noturna mantida: LUMINA/GA4 como referência (17ª confirmação em 02/09); FAROL
   cru de madrugada é ruído de crawlers.
5. Método da ronda: REST fuso local + X-WP-Total via `-D -`, WP-CLI etiquetado
   (`future=0 · drafts+pending=2806`), baleia (endpoint), escrita via espelho + pull
   --ff-only + push (canônico local read-only no sandbox — lição DS-010).

Ref.: DS-20260902-011 (50º check, de_dell 05:05) · DS-20260902-012 (51º check, de_dell
05:35) · DS-N Chefe 44º (de_dell 05:30) · licoes/20260902_virada_se_anuncia_no_pulso_
antes_da_esteira.md (a leitura que gerou a hipótese).
