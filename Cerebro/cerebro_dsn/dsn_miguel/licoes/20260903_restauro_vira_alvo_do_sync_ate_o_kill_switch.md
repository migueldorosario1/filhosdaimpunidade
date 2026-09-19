# 2026-09-03 — Restauro vira alvo do sync até o kill-switch

## O quê
O restauro que a DS-010 fez na minha MEMORIA_VIVA (commit f2305832e, 05:03, 2 linhas
verbatim) foi COMIDO ~4 minutos depois pelo sync aaf5da9f6 (05:07, "sync: 10252
arquivos", 21ª recorrência do dia). O XM-007 (Codex, 05:24) sinalizou as linhas
ausentes; eu confirmei o diff (f2305832e → aaf5da9f6 = exatamente 2 deleções, as 2
linhas mais novas) e re-restaurei por append na ronda 05:30 (91º CHECK).

## Por quê
A lição de 02/09 ("restauro é respiro, não cura") ganhou um detalhe: enquanto o
produtor do snapshot defasado (o `sync:` que roda em outra máquina) segue ativo,
QUALQUER conteúdo novo no caminho dele — inclusive o próprio restauro — vira alvo da
próxima passada. Restaurar não desliga a origem do defeito; só repõe o que ela comeu.
A sequência inteira (restauro 05:03 → sync 05:07 come → sinal 05:24 → re-restauro
05:30) cabe em 27 minutos: sem o XM-007 apontando o dono e sem o dono conferir na
ronda seguinte, a perda ficaria invisível (o arquivo "parece" íntegro porque termina
numa lição antiga).

## Como aplicar
1. Restauro é append verbatim com fonte citada (git show do commit que tinha o texto) —
   nunca reconstruir de memória (risco de "texto parecido", não idêntico).
2. Após restaurar, CONFERIR na ronda seguinte se o conteúdo segue no origin (a
   verificação é contra o ORIGIN, não contra o clone local — o clone congela).
3. Registrar a recorrência com o hash do sync que comeu, para o placar do kill-switch
   (DSC-049, prazo HOJE 03/09, aguarda ✓ do Miguel): a cura não é o append repetido,
   é desligar a origem.
4. Sinal de terceiro (XM) sobre arquivo MEU = ação de dono imediata, não watch.

— DS Miguel (Dell) · 20260903
