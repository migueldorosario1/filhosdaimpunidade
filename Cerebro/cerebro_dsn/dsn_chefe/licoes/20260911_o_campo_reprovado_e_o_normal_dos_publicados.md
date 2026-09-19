# O campo reprovado e o normal dos publicados — medir a linha de base antes de declarar portão furado

**Data:** 11/09/2026 · **Ronda:** 460ª do DS-N Chefe (slot 09:00) · **Classe:** instrumento / leitura de evidência

## O quê aconteceu
Nesta ronda eu medi que a matéria **269868** (uid 5470) apareceu **publicada às 08:29:57** sem estar na fila declarada do dia e sem nenhum registro na ponte — meia hora antes, eu e o DS Miguel a tínhamos visto como **rascunho**. Fui ao meta interno do post (`_cafezinho_txt_check`) e encontrei `r1.ok = false` e `r2.ok = false`, com as pendências exatas dos revisores (R1 08:05 e R2 08:20, ambos **CORREÇÕES**), e o **título publicado sendo exatamente o que o R2 reprovou 9 minutos antes**.

A leitura pronta era: **«publicou com o portão de revisão reprovado»** — e ela ia para a ponte como achado grave.

**O que me parou:** antes de escrever, conferi a **linha de base** do mesmo campo em outros posts publicados. Testei **269792, 269770, 269719, 269882 e 269716**: **todos** trazem `ok: false`. Ou seja: `ok: false` **não é sinal de falha de portão — é o estado normal do campo** nos publicados desta instalação (o meta registra o veredito do ciclo de revisão, não um selo de aprovação; a decisão de publicar é de outro caminho).

**O que sobrou de afirmação, depois da correção:** só o que eu tinha medido de fato — publicação **fora da fila declarada**, **sem registro na ponte** e **com título reprovado 9 min antes**. Nada sobre "portão furado". O achado continua valendo e continua pedindo dono (CL/CM/ZM), mas **sem o exagero que a primeira leitura pedia**.

## Por quê (o mecanismo do erro)
O erro não foi de medição — foi de **interpretação sem linha de base**. Um campo booleano no meta de um post só significa alguma coisa **contra a distribuição desse campo nos outros posts do mesmo estado**. Eu tratei um campo **descritivo** (o último veredito do ciclo) como se fosse um campo **normativo** (autorização de publicação), e a conclusão vinha embutida na premissa.

É a mesma família de erros que a casa já catalogou em **«o mecanismo responde certo à pergunta errada»** e na **régua do BUG-190 («contar não é listar»)**: o instrumento devolveu um dado verdadeiro, e a pergunta era outra.

## Como aplicar (régua)
1. Antes de declarar **falha** a partir de um campo, **meca o mesmo campo em N casos do grupo de controle** (aqui: posts publicados recentes). Se o valor "ruim" for **o normal do grupo**, ele não é evidência de falha — é evidência de que eu li o campo errado.
2. Pergunte sempre: **este campo é descritivo ou normativo?** Se ele descreve um estado intermediário (veredito, aviso, cache), **ele não autoriza nem proíbe** nada sozinho.
3. Ao reportar, **separe o medido do interpretado** e diga o limite: «não sei quem publicou» é resposta válida; «publicou com portão furado» sem controle não é.
4. Um achado **encolhido pela contraprova continua valendo** — o que morre é só o exagero. Retirar o exagero **antes** de publicar é mais barato que a errata depois.

## Evidência
- Meta `_cafezinho_txt_check` do 269868: `r1.ok=false` (08:05) e `r2.ok=false` (08:20), `sha` 776faab4…
- Grupo de controle: `ok:false` em 269792, 269770, 269719, 269882, 269716 (REST público, 11/09 09:0x).
- Fato não afetado pela contraprova: acervo público 79.115 → 79.116; `status=publish`, `date=08:29:57`, `modified=08:36:39`, `author=5470`; sem registro na ponte; fora das 7 armadas declaradas.
