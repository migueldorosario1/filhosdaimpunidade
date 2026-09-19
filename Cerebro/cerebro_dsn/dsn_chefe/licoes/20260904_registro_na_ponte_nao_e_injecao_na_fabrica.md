# Registro na ponte ≠ injeção na fábrica (pauta Gonet — 2 janelas perdidas)

**Data:** 04/09/2026 (ronda 129º, 04:30) · **Autor:** DS Nuvem Chefe (DS-N Chefe)

## O quê
Nas rondas DS-N-20260903-035 (17:42, alvo ciclo nacional 19:25) e DS-N-20260903-040 (20:12, alvo ciclo nacional 21:25) eu registrei na ponte (de_dell) a reinjeção da pauta Gonet × relatório da PF, com tese, fontes e título — e o ciclo nacional NUNCA a processou: o ciclo das 19:26 rodou a pauta do coletor «Equipe de Lula usa pesquisas…» e nenhum ciclo subsequente produziu um rascunho Gonet (verificado por REST: zero posts com Gonet entre 03/09 20:00 e 04/09 04:30). A CL-20260904-005 (04:11) perguntou qual era o caminho concreto de injeção (arquivo? fila?) — e a resposta honesta é: **registro na ponte não é injeção na fábrica**. A fábrica (ciclo nacional/Fable, NYC /root/v4_labs, dono ZM) lê a fila de pautas do COLETOR dela; o bloco na ponte é lido por humanos/CL, não por máquina da fábrica.

## Por quê
Eu tratei "escrevi o bloco com o alvo HH:MM" como se fosse um mecanismo de entrega. Não era: o alvo virou promessa ao Miguel (via CL-128/133 e meus CHECKs) sem um canal de máquina que o cumprisse. Duas janelas (19:25 e 21:25 de 03/09) foram declaradas "reinjetadas" sem efeito. O dedupe do mesmo erro: a CL-133 já dizia "se a fábrica não recebe pauta externa por esse caminho, me diga qual é o caminho" — eu não verifiquei o caminho ANTES de declarar a injeção.

## Como aplicar
1. Antes de dizer "pauta X injetada para o ciclo HH:MM", confirmar QUAL mecanismo de máquina recebe a pauta (arquivo, fila, ordem cl, coletor) e ter PROVA de que o ciclo leu (rascunho criado com o tema). Sem isso: "registrada na ponte para ciência da CL", nunca "injetada".
2. Caminhos de máquina comprovados na casa para pauta externa virar matéria: (a) ordem cl da CL ao AGY-L com o conteúdo (padrão cl119 Conass 268888 — a CL/AGY montam o rascunho com capa e agendam sob Consenso Duplo); (b) redação humana do Miguel; (c) criação manual de draft pelo DSC/ZCode via CafezinhoBot (padrão 268576 6x1). O ciclo nacional da fábrica só escreve do coletor dela.
3. Item recusado que REPETE no ciclo vem do coletor (padrão documentado CL-090: coletor pol repetiu a mesma pauta 7x em 12h) — a limpeza na ORIGEM é dono ZM (fábrica NYC); na nossa borda, aplicar a marca `dedupe:pauta_recusada` (regra do feedback CL nº 59) para o ciclo pular.
4. Responder com honestidade quando perguntado ("qual é o caminho?"): "não confirmado / não tenho mecanismo" é resposta válida — e cobrar do dono da fábrica (ZM) o mecanismo real antes de prometer janelas ao Miguel.
