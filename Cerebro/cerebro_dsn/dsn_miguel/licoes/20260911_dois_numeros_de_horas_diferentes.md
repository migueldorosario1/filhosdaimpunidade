# DOIS NÚMEROS DE HORAS DIFERENTES — comparar contagens de instantes distintos como se fossem o mesmo instante

**Data:** 2026-09-11 (ronda 426ª DS-Dell) · **Refs:** BUG-20260910-DS-191, `XM-20260911-015`, bloco `DS-Dell-20260911-015` (425ª), lição `20260911_a_lista_soma_o_sticky_a_contagem_nao.md`.

## O QUE ACONTECEU

Na ronda 425ª eu medi, às **07:05**, que a fila de agendados de 11/09 tinha **7 peças** (`--format=count` e SQL concordando) e escrevi que **quatro blocos da casa** (CL-20260911-007, AL-20260911-852/854, DS-N-20260911-015) «anunciavam **8 armadas** onde o SQL diz **7**» — tratando isso como **falso positivo coletivo simultâneo** causado pelo sticky 269021.

O **XM-20260911-015** (07:23) contestou e estava certo: o **269770 publicou às 07:00:00**. Antes das 07:00 a fila tinha **8 peças de verdade** (o 269770 incluído); depois das 07:00, **7**. Ou seja: os blocos que escreveram «8» **mediram antes** da publicação e **não erravam pelo motivo que eu apontei** — a diferença entre os números era **o fluxo da fila ao longo do tempo**, não o sticky.

**Dois defeitos distintos que eu embaralhei em um:**

- **O defeito real (BUG-191):** a **listagem CSV** soma o sticky 269021 (que é `publish`) e devolve **8 linhas** onde o `count` diz **7** — o fantasma é **estrutural** e não depende da hora. Canário: `linhas − count = 1` = número de sticky.
- **O que eu inventei:** chamar de erro coletivo a diferença **8 → 7**, que era apenas a **publicação do 269770 às 07:00** reduzindo a fila. **Medição de 07:05 comparada com declaração de 06:xx** — instantes diferentes.

## POR QUE ACONTECE (o mecanismo do meu erro)

Uma fila é uma **variável que se move**. Comparar duas fotos sem carimbo de hora transforma **fluxo** em **discrepância** e discrepância em **acusação**. Foi exatamente o que eu fiz: peguei o meu número (07:05), peguei o número dos outros (sem hora na frase) e concluí «eles contam errado» — quando a leitura correta era «**a fila mudou entre as duas medições**».

Família próxima das lições de instrumento, mas **não é** o instrumento respondendo à pergunta errada: é **o analista comparando respostas certas de perguntas feitas em horas diferentes**.

## RÉGUAS QUE FICAM

1. **Todo número de fila vai com carimbo de hora.** Sem hora, o número não é comparável com nada.
2. **Antes de chamar de divergência, perguntar: o objeto se moveu entre as duas medições?** Se sim, a hipótese nula é **mudança real**, não erro alheio.
3. **Separar sempre as duas perguntas:** «o instrumento infla a contagem?» (estrutural — testável a qualquer hora, e o sticky prova) × «a fila mudou?» (temporal — testável só com duas medições datadas).
4. **Ao corrigir outro agente, verificar primeiro se ele mediu em outro instante.** A errata é minha: o meu bloco 425ª imputou erro coletivo onde havia **duas medições de horas diferentes**.
5. **Corrigir por append, com o número, e não defender a frase antiga** — 3ª vez em 7 rondas que faço isso (416ª, 421ª, esta).

## FRASE DE BOLSO

**Numa fila, a diferença entre dois números pode ser o mundo andando — não alguém contando errado.** Quem compara sem hora transforma o movimento em culpa.
