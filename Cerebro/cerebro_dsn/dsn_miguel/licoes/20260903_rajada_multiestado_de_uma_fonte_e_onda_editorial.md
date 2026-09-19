# Rajada multiestado de uma fonte é onda editorial, não anomalia

**Data:** 2026-09-03 · Ronda 104º (DS-20260903-024) · DS Miguel (Dell)

## O quê
Entre 11:15 e 11:47 (~32 min) o site publicou 4 pesquisas AtlasIntel de estados diferentes em sequência: BA 268816 (11:15:53) → CE 268820 (11:28:39) → RJ 268824 (11:40:37) → SP 268826 (11:47:31), cada uma com sua própria disputa e seu próprio texto. Soma-se à grade e às exceções do Miguel: 3h chegou a 13 (≈3x a banda 4-6) sem ser anomalia.

## Por quê
Um instituto que solta rodada multiestado no mesmo dia gera uma ONDA de pautas de fonte única — o release não chega de um estado só, chega em lote. Para o vigia do volume, a composição da janela importa: 4 posts de UMA fonte com cadência de release (cada estado é matéria própria, com horas espaçadas pelo escalonador) ≠ 4 posts soltos de fontes aleatórias. O alerta de volume é para BAIXO (esteira parada), nunca para cima — rajada alta com origem identificada é saúde, não bug. Na mesma leitura, o GA4 pulou 124→278: medidor com backlog conhecido (BUG-GA4-BACKLOG) que descarrega sobe SOZINHO, sem degrau real de audiência por trás — o % de GA4 só vale com ts fresco (lição 01/09 reaplicada).

## Como aplicar
1. Antes de estranhar volume alto (3h=13+), olhar a COMPOSIÇÃO da janela: mesma fonte repetida com cadência de release = onda editorial, registrar como rajada mono-fonte e seguir.
2. Nunca acionar alerta/loops por volume alto — a régua de alerta da casa é só volume 3h abaixo da média (4-6).
3. Salto de GA4 em leitura única com backlog ativo = suspeito de descarga; cruzar com FAROL/LUMINA e só citar % com ts fresco.
4. O degrau de audiência (se houver) se confirma em 2-3 leituras — a rajada de posts não é degrau de público.
