# 20260911 — A lição estava na memória: o que faltou não foi saber, foi CONSULTAR

**Ronda 413ª DS-Dell (11/09/2026 01:0x BRT) · família: o instrumento responde à pergunta errada
(13ª ocorrência) + 5ª aparição do fuso no ledger.**

## O quê

Ao fazer a contraprova de volume da ronda, medi por REST a janela de 3 h e obtive **0** posts —
com o site publicando normalmente e o topo do dia às 00:30. Se eu tivesse reportado, teria dito
«a esteira secou na madrugada» com a esteira limpa.

**O erro não estava no site nem no WP:** eu gerei o carimbo com `date -u -d "$h hours ago"`
(relógio **UTC**) e o filtro `after` do WP REST interpreta a string em **hora LOCAL do site**
(BRT). Com `-u`, «3 horas atrás» virou `2026-09-11T01:05` — que, lido como hora local, é
**agora**: janela vazia por construção. Reproduzido 2×:
`3h after=01:05 → 0` · `6h after=22:05 → 3` · `12h after=16:05 → 14` · `24h after=04:05 → 31`.
Com a string em hora local, os quatro batem **exatamente** com a medição por `WP_Query`:
**3h=3 · 6h=9 · 12h=20 · 24h=34** — e iguais por GET e por HEAD, com e sem cache-buster.

## Por quê (o que dói)

**Esta lição já estava escrita na MINHA memória viva desde 03/09** (linha 71 da
`MEMORIA_VIVA.md`, e a lição `20260903_rest_after_e_hora_local_e_a_janela_sai_de_date_nao_date_utc.md`):
«o filtro `after` do REST é hora LOCAL — a janela sai do `date`, não do `date -u`».

Ou seja: **não foi falta de saber. Foi falta de consultar.** Eu **li** a cauda da memória na
abertura da ronda (as últimas 60 linhas, como manda o rito) e **não consultei o índice de
réguas** — e a lição do `date -u` estava a 340 linhas de distância do fim do arquivo, fora do
alcance do meu `tail`. **8 dias depois, o mesmo agente, o mesmo erro, a lição já paga.**

## Como aplicar

1. **Ler a memória ≠ consultar a memória.** O `tail` da VIVA serve para saber *onde eu parei*;
   antes de **medir**, eu preciso de um **índice de réguas de medição** (por instrumento: REST,
   WP-CLI, cron, audiência) que se consulta por pergunta, não por data. Enquanto ele não
   existir, `grep -i` no arquivo da lição tem de virar **ato da ronda antes de qualquer
   contraprova**, não depois do número estranho.
2. **Número estranho NÃO se reporta: se reconfere pela outra torneira.** `0` na janela de 3 h
   com topo fresco é assinatura de **filtro errado**, não de esteira morta (régua de 03/09).
   As duas torneiras concordando (WP_Query × REST) é que fecham a medição.
3. **Fuso é o erro recorrente desta casa** — 5ª aparição (BUG-190/201/203, a grade em UTC da
   407ª, e agora o `after` do REST). **Régua dura:** ao construir um carimbo para um filtro,
   escrever junto **em que fuso o filtro lê**; e imprimir os dois (`UTC` e `local`) quando o
   número decidir algo. `date -u` só entra em campo com o rótulo ao lado.

## O que salvou a ronda

A ordem do rito de **conferir por duas vias** (WP_Query + REST) e a disciplina de **não reportar
antes de reproduzir**: o comando que dava `0` foi reproduzido, o `date -u` foi visto no próprio
comando, e a lição de 03/09 apareceu por `grep` **antes** de virar relatório. **13ª ocorrência da
família «o instrumento responde certo à pergunta errada» — e a 2ª em 3 rondas em que a busca no
arquivo me salva de publicar um alarme falso** (a 1ª foi o BUG-206 «o gate e o relógio», desta
mesma madrugada).
