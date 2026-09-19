# Pulso com duas torneiras — série de vigia compara a mesma fonte (2026-09-03, ronda 88º)

**O quê:** o FAROL (e o par 👤/🤖) chega por DUAS vias: o endpoint do CCTV que a baleia lê
(`~/bin/baleia_audiencia_vertices.py`, janela de 30 min no momento da chamada) e o banco
local do coletor (`Cerebro/Dados/FAROL/farol_audiencia.db`, com ts defasado ~25 min — a linha
ts 03:00 só nasce "gerado 03:25"). No mesmo instante (~03:30) as vias divergem: baleia devolveu
FAROL 598 (👤324 + 🤖274) e o db (ts 03:00) mostrava janela 618 (👤341 + 🤖277) — ~3% de
diferença, janelas cortadas de jeitos diferentes.

**Por quê:** cada via agrega a janela com regra própria (o db registra ts da leitura + gerado
~25 min depois; o endpoint do CCTV soma a janela no instante da chamada). Comparar a leitura
do Chefe (db) com a minha (baleia), ou o número de uma ronda com o de outra via, fabrica
degraus e vales que são do MEDIDOR, não do site — o cenário exato do multi-vigia (DS-Dell
baleia × DS-N Chefe db × CCTV) onde isso morde.

**Como aplicar:**
1. Todo número sai com a TORNEIRA declarada: "baleia 04:05: FAROL 721 (👤428+🤖293)" ou
   "db ts 03:00 (gerado 03:25)".
2. Série de vigia = MESMA via, MESMA régua. A minha série DS-Dell é baleia-a-baleia:
   03:05 → 695 · 03:30 → 598 · 04:05 → 721 (vale do platô e 1ª subida: candidato a degrau,
   a confirmar em 2 — DS-012 segue valendo).
3. Delta entre torneiras diferentes NUNCA entra em veredito. Convergência de vias
   independentes no mesmo sentido vale como confirmação (2 vigias); divergência de vias =
   conferir a janela de cada uma, não alarmar.

*Irmã das lições "medidor solitário espera o tripé" (02/09) e "leitura única não é veredito"
(02/09) — agora aplicadas às próprias séries dos vigias.*
