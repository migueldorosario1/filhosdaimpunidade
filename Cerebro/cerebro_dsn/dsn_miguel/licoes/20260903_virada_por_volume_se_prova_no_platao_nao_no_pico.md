# Lição 2026-09-03 — Virada por volume se prova no platô, não no pico (DS-20260903-016, 96º CHECK)

## O quê
A virada da manhã confirmada por VOLUME às 07:00 (FAROL 725, 👤449 — 7ª leitura) não se prova
repetindo o pico — prova-se pela série NÃO voltar ao platô anterior. Nas leituras seguintes os
humanos foram 408 (07:30) e 406 (08:00): o dígito caiu ~10% em relação ao pico, mas ficou 3
leituras seguidas ACIMA da faixa noturna (324-368) — é platô NOVO, não retorno à curva. No mesmo
08:00, GA4 (177→161→146) e LUMINA (68→54) recuaram com ts defasado enquanto o FAROL humano
segurava.

## Por quê
Manhã é rampa ruidosa: o pico das 07:00 tinha humanos +79 (gente acordando em bloco, perto da
grade ~07:00); depois a rampa ASSENTA no platô alto — e é o medidor de humano puro do FAROL
(servidor, mesma torneira da série) que discrimina o "assentou em cima" do "caiu de volta".
GA4 e LUMINA andam com atraso de janela (ts ~25-30 min atrás) e o LUMINA é beacon ruidoso
(~13% dos humanos do FAROL): recuo deles na mesma leitura em que o FAROL humano sustenta é
perna atrasada de medidor, não contra-sinal. Veredito construído em série continua se
desmontando só em SÉRIE no tripé (2-3 leituras contrárias com o FAROL humano cruzando a faixa).

## Como aplicar
- Depois de um veredito de virada com volume, o teste das rondas seguintes é o PLATÔ
  (2-3 leituras ≥ limite superior da faixa anterior), nunca a repetição do pico.
- Dígito abaixo do pico mas acima da faixa = SUSTENTAÇÃO, não recuo.
- GA4/LUMINA recuando com FAROL humano firme = registrar "perna atrasada (ts defasado)" e
  confirmar na leitura seguinte; não virar contra-veredito.
- Só SÉRIE no tripé desmonta: FAROL humano caindo abaixo da faixa + GA4/LUMINA juntos no recuo.
