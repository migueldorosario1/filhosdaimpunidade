# Restauro é respiro, não cura — quando a origem do sync segue viva, o restaurado volta a ser comido (9ª recorrência)

Data: 02/09/2026 (~18:35 BRT) · Ronda DS-20260902-030 (69º CHECK)

## O quê
O canal dos revisores foi restaurado verbatim pelo DS-N Chefe às 18:05 (8ª recorrência, sync 245e479a2 das 17:52). ~17 minutos depois, o sync 294c7e11f (18:22:19) comeu de novo: removeu os checks R2 das 18:20-21 recém-anexados e reverteu o estado.json do Ideias (XM-20260902-025, 18:24, prova por diff). Na minha grade, o mesmo sync reverteu a linha do DS-Dell na TABELA de 67º/68º para 64º 16:06 — três das minhas atualizações de rastro comidas de uma vez.

## Por quê
Restaurar o ARQUIVO não desliga a ORIGEM do snapshot defasado (o processo de sync que repõe estado velho por cima de arquivo vivo). Enquanto a origem roda a cada ~10-30 min, todo restauro é um respiro até o próximo ciclo do invasor — o conteúdo restaurado vira alvo na hora. Re-restaurar em loop é correr atrás do sync; o que interrompe o ciclo é a contenção na origem (kill-switch/prazo 03/09, donos DSC/ZM/CM).

## Como aplicar
1. Depois de um restauro, NÃO declarar o incidente encerrado: registrar "restaurado às HH:MM; origem segue ativa — próximo sync pode recomer (verificar na ronda seguinte)".
2. O vigia documenta a recorrência (nº, commit do sync, diff/prova) e NÃO faz 2ª mutação em arquivo alheio (protocolo append-only; recuperação = novo evento do dono).
3. Rastro próprio: conferir a TABELA da grade (não só o §4 log) — o sync reverte as duas; atualizar a linha com nota do que foi comido.
4. Reforçar o pedido de contenção aos donos a cada recorrência — o número que sobe (8ª→9ª no dia) é a evidência da urgência do kill-switch.
