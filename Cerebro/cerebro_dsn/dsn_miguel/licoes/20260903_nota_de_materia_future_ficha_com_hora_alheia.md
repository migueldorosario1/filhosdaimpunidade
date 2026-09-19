# Lição — 2026-09-03 · Nota de matéria ainda `future` vira ficha com hora alheia

## O quê
Na ronda DS-20260903-003 (01:05), a nota criativa da memória atribuiu ao post **268717**
(«Índia e Rússia discutem criar banco de desenvolvimento do bloco de Xangai») a hora de
publicação **00:48:42** — que na verdade era do **268728** (Mendonça/Vorcaro, slot 00:48).
Naquele momento o 268717 era `future` com slot **03:17**; ele só subiu de fato às
**03:17:00** (confirmado no REST topo da ronda 87º, 03:30). A entrada ficou na memória como
"inédita já notada" com hora de outro post.

## Por quê
A régua "agendado não é disparo — o evento é a prova" (lição 02/09) foi aplicada aos posts
da esteira, mas NÃO ao próprio caderno do vigia: a nota foi escrita olhando a grade/plano
(ou o topo do momento, confundindo o slot vizinho), não o fato no ar. Consequência prática:
a série "matérias já notadas" ganha uma entrada duplicável — quando o post subisse de
verdade (como agora, 03:17:00), o dedupe da série poderia pular a nota real por achar que
já foi notado, ou notar duas vezes com horas diferentes. Ficha com hora de outro post é
ruído de memória: corrompe contagem e rastreabilidade (append-only não apaga, então o erro
fica registrado e precisa de retificação explícita, como foi feito na DS-20260903-007).

## Como aplicar
1. Nota criativa de matéria SÓ depois de confirmar o post no REST (`per_page` recente:
   id + `date` + título) no momento da escrita — nunca com hora da grade planejada, do
   bloco de outro agente ou de memória do slot vizinho.
2. Se a matéria ainda é `future`, não notar como publicada; no máximo registrar "candidata
   a nota quando subir" sem hora inventada.
3. Ao achar erro de hora em entrada antiga da própria memória: retificar por APPEND (nova
   entrada com a hora real + ref à entrada errada), nunca editar/apagar a antiga.
4. Estender a verificação em 3 camadas (estado + evento + AR) também aos registros do
   vigia: o que eu anoto como fato precisa ter a mesma prova que eu exijo dos posts.

Refs: DS-20260903-003 (nota com hora alheia) · DS-20260903-007 (correção + 268717 no ar
03:17:00) · lição 20260902_agendado_nao_e_disparo_evento_e_a_prova.md.
