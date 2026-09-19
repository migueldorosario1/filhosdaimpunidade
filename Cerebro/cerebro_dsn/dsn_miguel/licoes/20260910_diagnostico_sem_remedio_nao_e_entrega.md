# 20260910 — Diagnóstico sem remédio acionável não é entrega

**O quê.** Nas rondas 377ª-379ª (madrugada de 10/09/2026) descrevi o BUG-20260909-DS-178
(11 remoções de blocos alheios no `de_dell.md` em ~24 h) com precisão crescente — prova por
commit, contagem de bytes, sha256, categoria corrigida — mas **sempre deixei a solução no
condicional**: «fix estrutural pendente», «pendência nº 1», «dono ZM». O Miguel falou três
vezes às 01:34/01:38/01:41 de 10/09: «Você tem que me dar a razão do bug, explicar em
detalhes e **me dar um prompt** para resolver… todo mundo tem que fazer isso»; e na escuta
1852: «**Pare de suspense**, o problema é esse e a solução é essa, cole esse prompt lá no
Z-code». Na ronda seguinte (380ª) entreguei o pacote fechado no bloco DS-Dell-005: problema
com prova + causa-raiz + **prompt executável** (guard `pre-push` com `comm -23` + protocolo
`pull --rebase`/append-only/união) + **teste que o guard tem de reprovar** + critério de
pronto auditável em 3 itens.

**Por quê.** Diagnóstico é metade do trabalho e a metade que não move nada. Quando o dono
pede solução, um registro tecnicamente correto que termina em «pendente com o dono» transfere
a ele o trabalho de projetar o remédio — e ele já disse que é exatamente isso que não quer.
A casa já tem o padrão certo: `BARRADA_NOTA_ALTA` nasceu de um caso e virou regra no mesmo
dia; a CL fechou o BUG-184 na causa com o código na mão e consertou a fila no mesmo turno.
Diagnóstico vira entrega quando termina em algo que o outro lado pode **colar, rodar e
verificar**.

**Como aplicar.**
1. Todo relato de bug do DS-Dell termina em **três campos obrigatórios**: (a) o problema em
   uma frase; (b) a causa-raiz; (c) **o remédio acionável** (prompt/código/comando pronto
   para colar) com **critério de pronto verificável**.
2. Se o remédio não é da minha alçada, entrego o **artefato** mesmo assim (prompt, script,
   checklist) endereçado a quem executa — não devolvo a tarefa em aberto.
3. **A prova de que uma trava funciona é o teste que ela reprova**: guard que nunca bloqueou
   nada é decoração; lock que avisa e não barra não é lock (paralelo: BUG-182).
4. Nada de «suspense» em relatório: números e nomes diretos. Prazo medido pelo relógio de
   quem depende da correção (o cron das 02:30), não pelo relógio da reunião.

**Famílias.** `20260910_sintoma_verdadeiro_conclusao_falsa` (DS-N Chefe) — mesma madrugada,
outro lado do mesmo problema: lá a conclusão sem prova; aqui a prova sem remédio.
`20260909_ponte_compartilhada_bloco_comido_restauro_chega_sozinho` — o bug que originou a
ordem.
