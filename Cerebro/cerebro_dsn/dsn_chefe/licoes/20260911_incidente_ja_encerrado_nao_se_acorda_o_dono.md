# LIÇÃO — 2026-09-11: incidente JÁ ENCERRADO, com dono e sem decisão urgente, não fura a cadência de 4/4h (ronda 447ª)

## O quê
Às 02:15 de 11/09 o DS-Dell abriu o BUG-20260911-DS-208 (o object cache do us65 falha
FECHADO: `RedisException` → `wp_die()` → leitor recebe 500/503; 135 erros entre 02:00 e
02:04; 3.512 erros 5xx em 24 h = 1,13% do tráfego). Às 02:30 eu tinha na mão um 🔴 com
número grande, prova de código e proposta de correção — e a decisão de mandar ou não
mensagem avulsa ao Telegram do Miguel (a regra permite "🔴 alerta crítico/incidente" em
qualquer ronda).

Mandei? NÃO. E declarei a decisão por escrito na ponte no mesmo bloco (item 4 do
DS-N-20260911-006), para que ela fosse auditável em vez de parecer omissão.

## Por quê (o critério, não a intuição)
O que autoriza furar a cadência **não é a gravidade histórica do defeito** — é existir
**decisão pendente que perca valor em minutos**. Checando os três fatos medidos:
1. **A janela fechou sozinha** às 02:05 (0 erro de 02:05 em diante, medido pelo Dell) e a
   minha sonda externa às 02:36-02:42 deu **0 × 5xx em 26 requisições**.
2. **A causa já tem dono natural** (infra us65/ZM) e o que se pede ao Miguel é **aval**,
   não ação minha nem dele no minuto.
3. **O padrão do defeito é diurno, não da madrugada**: a pior hora de 10/09 foi **11h
   (2.093 erros)**, em pleno expediente. O relatório das **04:00** chega **antes** do pico
   provável e depois de o Miguel acordar.

Pior hora para acordar alguém é quando **nada pode ser feito a mais** por ter acordado.
"Incidente" e "emergência" não são sinônimos: emergência é incidente **com relógio**.

## Como aplicar
Antes de furar a cadência por um incidente, responder três perguntas nesta ordem:
1. **Está em curso?** (janela aberta agora, ou já fechou?) — fechada ⇒ cai para relatório.
2. **Existe decisão/campo de ação que perde valor em minutos?** (algo se degrada se
   esperarmos 90 min?) — não ⇒ cai para relatório.
3. **O dono já sabe?** (o bloco com a prova já está na ponte, com dono nomeado?) — sim ⇒
   cai para relatório; o meu papel passa a ser **levar prioridade**, não repetir o alarme.
Se as três respostas forem "não/sim", **a mensagem avulsa é ruído** — e ruído derruba a
confiança justamente no dia em que o alarme verdadeiro tocar.
**Obrigação que sobra (e não é opcional):** registrar a decisão e o critério **no mesmo
bloco** em que se mediu o incidente; levar o assunto como **item nº 1 do próximo 4/4h**;
e **medir do lado de fora** o que a própria física alcança (foi assim que o 5xx virou
"fechado e não medido" em vez de "presumido").

## Verificação
Ronda 447ª (02:38): bloco DS-N-20260911-006 itens 2, 3 e 4 (watch do 02:30 fechado;
sonda externa 0 × 5xx; parecer com P2/P4 primeiro e encaminhamento para as 04:00).
Adendo ao BUG-208 no `CEREBRO_NODE_BUGS_ATIVOS.md` com o limite declarado (não tenho o
nginx de us65). Sonda `/tag/japan/feed` = 404 por slug inexistente — **nem todo 404 da
lista de "derrubadas" é vítima do incidente**.
