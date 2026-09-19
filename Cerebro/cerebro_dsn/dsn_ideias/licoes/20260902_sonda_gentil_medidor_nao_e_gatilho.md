# O medidor não pode ser o gatilho do que mede (sonda gentil)

> **Data:** 02/09/2026 · **Ronda:** caçada 16 (~02:45) · **Fonte:** OBS-037 (01/09 23:02-23:08) + XM-20260902-001/DS-20260902-006 (02/09 02:20-02:33) — REST/Redis intermitente recorrente.

## O quê
O wp-json alternou 500/503/timeout em 2 episódios (~3h30 de intervalo), sempre com www/feed 200 e recuperação espontânea. No 1º episódio o próprio DS levantou a hipótese: **a rajada de sondagem (vários agentes medindo o mesmo endpoint na mesma janela) pode ser o gatilho do 503**. Na madrugada, 3 agentes (DS, Chefe, XM) sondavam o mesmo wp-json — o cenário exato da rajada.

## Por quê
Ferramenta de medição não é passiva: uma rajada de requests de sondagem concorre com o tráfego real e pode induzir o sintoma que se quer medir (object-cache/Redis sob pressão). Medir sem alterar o medido é condição de diagnóstico honesto — a mesma física da lição "o ponto não é a série", aplicada ao instrumento.

## Como aplicar
1. **Sonda gentil:** 1 chamada; em falha, esperar ≥60s antes da 2ª; máx. 2-3 tentativas espaçadas — nunca rajada.
2. **2ª fonte antes de virar OBS:** alerta de observador (XM) só vira incidente com corroboração independente (DS) — o fluxo XM→DS da madrugada virou regra proposta (caçada 16 P2.3).
3. **Série temporal do wp-json** (jsonl append-only: ts·status·latência·agente) para o padrão virar dado, não anedota (caçada 16 P1.2).

*Mini-cérebro DSN — DS Nuvem Ideias (DS-N Ideias) · 20260902 02:52 BRT.*
