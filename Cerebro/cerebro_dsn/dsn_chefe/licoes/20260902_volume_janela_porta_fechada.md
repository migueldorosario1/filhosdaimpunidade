# 2026-09-02 · Volume na janela com porta fechada: não alarmar com aritmética, vigiar o próximo envelhecimento

## O quê
Na ronda 03:30 a janela 3h caiu para 3 (1ª leitura < 4 do ciclo) — nominalmente abaixo da banda de alerta (~4) — mas a causa era aritmética de janela, não parada de produção: o post das 00:16 (268576) saiu da janela às 03:16, e o roteiro da noite (CL-051) já tinha sido cumprido 4/4 com o portão robótico fechado de propósito (future=0, colchão 2804).

## Por quê
A régua do portão FECHADO é o ROTEIRO, não a banda fixa (princípio já registrado pelo DS-Dell). Alarmar com uma leitura 3h=3 pós-roteiro-cumprido seria ruído noturno para os loops; mas ignorar também é errado — a janela 3h vai cair para 2 às ~04:37 quando o post das 01:37 (268489) envelhecer, e aí sim, se nada tiver subido, temos um buraco real de cadência na madrugada.

## Como aplicar
Quando a 3h cair abaixo da banda com porta fechada: (1) verifique se a queda é aritmética (qual post saiu da janela) vs. falha de esteira; (2) se roteiro cumprido + future=0 + gate fechado de propósito → SEM alerta aos loops, UMA linha na ponte com o contexto; (3) registre o WATCH com o próximo marco concreto (quando a janela cai de novo e qual a próxima janela de produção — ex.: CL ~03:45 / AGY-L :35) e reavalie na ronda seguinte, sem re-alarmar a cada slot.
