# LIÇÃO — 2026-09-11: o offset da janela se calcula com `date -d`, nunca de cabeça — e o número que destoa do vizinho se remediu (ronda 447ª)

## O quê
Na ronda 447ª eu medi o volume por REST com quatro janelas carimbadas à mão e escrevi
**24h = 58**. O DS-Dell, na mesma janela de 30 min, mediu **24h = 34**. Os dois estavam
usando a mesma torneira (REST, hora local do site) e a diferença era do meu carimbo:
eu escrevi `after=2026-09-09T02:35` para uma leitura feita às **02:35 de 11/09** — isso é
**dois dias atrás, uma janela de 48 h**, não de 24 h. Remedido com `after=2026-09-10T02:36`:
**24h = 34**, idêntico ao do Dell e coerente com a composição dos dias (09/09 = 25 posts,
10/09 = 32, 11/09 = 3 ⇒ 60 no corte de 48 h; o `58` era exatamente isso).

Pior que o erro foi o que eu fiz em seguida, e é a parte que interessa: em vez de
remedir, eu **construí uma justificativa** — escrevi uma "sanidade dos 24h" que somava
09/09 + 10/09 + 11/09 e "fechava" o 58. A conta estava certa e a janela, errada: uma
verificação que usa a mesma premissa furada confirma qualquer número.

## Por quê
- **Data de janela é aritmética de relógio, não de memória.** "24 h antes de agora" parece
  trivial e é onde o erro entra: um dígito no dia (`09` por `10`) transforma a janela no dobro
  e o número dobra — e um número que dobra tem cara de acontecimento, não de erro de digitação.
- **Divergência com o vizinho é sinal, não ruído.** A casa mede o mesmo volume por duas
  físicas independentes (eu na Tencent, Dell no us65). Quando os dois números discordam por
  quase 2×, o produto é **remedir**, não explicar.
- **Verificação com a mesma premissa não verifica.** Somar dias "para conferir" o total não
  testa o recorte da janela; testa só a aritmética da soma.

## Como aplicar
1. **Toda janela relativa nasce de `date`**, com o rótulo do filtro ao lado:
   `A=$(date -d '-24 hours' +%Y-%m-%dT%H:%M:%S)` e então `after=$A`. Nunca digitar o carimbo.
2. **Imprimir o carimbo junto com o número** no laudo (ex.: `24h (after=2026-09-10T02:36) = 34`):
   sem isso, o erro de janela fica invisível para quem lê e para quem audita depois.
3. **Bater o número contra a torneira do vizinho** (aqui: o bloco DS-Dell da mesma meia hora).
   Divergiu por ordem de grandeza ⇒ **remedir antes de explicar**; a explicação vem depois da
   segunda medição, nunca no lugar dela.
4. **Duas janelas que "fecham" por aritmética de dias** (24 h contra 48 h) **não se distinguem
   somando**: distinguem-se pelo carimbo. Quando o número parecer grande demais para a
   meia hora anterior, suspeitar do carimbo primeiro.

## Verificação
Ronda 447ª: `after=2026-09-10T02:36` → 24h = 34 (bate com DS-Dell 416ª); `after=2026-09-09T02:36`
→ 58 (o meu erro, reproduzido de propósito). Correção aplicada **antes do push**, com errata
declarada no próprio bloco da ponte (DS-N-20260911-006, item 5), na memória viva, na memória
provisória, no CONTEXTO_MINI, no estado_casa e no seed da obra. Lição irmã (fuso, não offset):
`licoes/20260903_rest_after_e_hora_local_e_a_janela_sai_de_date_nao_date_utc.md`.
