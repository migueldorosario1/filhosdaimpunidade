# 2026-09-11 · O plantão lê só o TOPO do CONTEXTO_MINI — e o "novo" estava sendo gravado no FIM (ronda 452a)

## O que aconteceu
Ao atualizar o `CONTEXTO_MINI.md` nesta ronda eu fui conferir COMO o plantão (Loop A, resposta
em segundos ao Miguel) consome o arquivo, em vez de assumir. O código dele (`~/ds_nuvem_chefe/escuta.py`)
lê literalmente:

    def ctx(): return open(CTXF).read()[:6000]      # e o prompt usa ctx()[:3000]

Ou seja: **o plantão recebe os PRIMEIROS 3.000 caracteres do arquivo** — o topo.

O topo do arquivo, na hora desta ronda, era o bloco do **DS-N Chefe de 10/09 18:30**. O arquivo,
porém, tem 1.161 KB e 950 linhas, e as rondas **441a a 451a (10/09 21:xx → 11/09 04:32) foram
gravadas no FIM**, por append. Resultado medido: **o plantão respondeu ao Miguel por cerca de 10
horas com o estado da casa de 10/09 18:30** — 24 no ar, fila da véspera, saldo de crédito de outro
dia — enquanto o estado real era 3 no ar, fila de 9 armadas até 17:15 e outra realidade de custo.

## Por quê
- **O arquivo é lido por PREFIXO, não por inteiro.** Um arquivo que cresce por append só é "mais
  recente no fim" para quem lê o fim; para quem lê `[:3000]`, a informação nova simplesmente
  **não existe**. As duas convenções conviveram no mesmo arquivo sem ninguém medir a leitura.
- **O erro é invisível de fora.** Nada falha, nada alerta: o plantão continua respondendo com
  segurança e com números plausíveis — só que velhos. Um leitor que erra por dado velho é mais
  difícil de perceber do que um que erra por dado ausente.
- **Convenção sem dono é convenção que se quebra em silêncio.** O arquivo ficou 10 h fora de
  ordem porque uma ronda passou a usar `>>` e ninguém checou o topo; a checagem que faltava era
  boba — abrir o arquivo e ver a data da primeira linha.

## Como aplicar (régua)
1. **Antes de escrever num arquivo que outro agente LÊ, medir a leitura dele** (aqui: `[:3000]`).
   Onde entra o texto novo passa a ser decisão de engenharia, não de hábito.
2. **No `CONTEXTO_MINI`, o mais novo vai no TOPO** (prepend), com a data visível na primeira linha.
   Teste de 5 segundos: `head -c 300` do arquivo tem de mostrar a hora desta ronda.
3. **Todo arquivo state-of-the-world carrega a data no começo da primeira linha** — é o único
   carimbo que um leitor de prefixo consegue ver.
4. **Quando eu encontrar um arquivo com as datas fora de ordem, isso é achado de ronda** — vai no
   bloco da ponte, não fica só na memória.

Família: o instrumento responde à pergunta certa e o leitor faz a pergunta errada — variante
"o arquivo está correto e a leitura é que é curta".
