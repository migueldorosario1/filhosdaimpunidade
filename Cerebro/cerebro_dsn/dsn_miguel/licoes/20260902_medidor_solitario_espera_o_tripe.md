# 2026-09-02 — Medidor solitário espera o tripé (salto de FAROL não confirmado)

Ref.: DS-20260902-022 (de_dell.md 14:07) · ronda 14:00-14:03 · 02/09/2026

## O quê
O FAROL (servidor) saltou o humano de 423 (13:31) para 953 (14:00) — 2,3x em 30
minutos — com bots FLAT (501→480) e o resto do tripé MUDO: LUMINA 84 (vs 80) e
GA4 185 parado. Duas leituras seguidas (14:01 e 14:02) vieram IDÊNTICAS: o valor
é estável para a janela, não é erro de fetch. Mesmo assim, não virei o salto em
veredito: registrei "salto NÃO confirmado — veredito com janelas casadas (GA4 ts
14:30 + LUMINA 14:30 + série de 3 leituras)".

## Por quê
Cada medidor enxerga uma fatia diferente do mesmo site:
- FAROL mede o SERVIDOR (logs/contadores) — pode classificar crawler de IA com
  assinatura de navegador como "humano";
- LUMINA mede o BEACON (JS na página) — cobertura parcial (~9-19% dos humanos do
  FAROL), beacon novo ainda aquecendo;
- GA4 mede o Google com LAG de 30 min (ts 13:30 quando o FAROL já dizia 14:00).

Ou seja: o % GA4/FAROL e até um salto de 1 medidor viram ruído quando as janelas
não casam — a lição de 01/09 ("numerador e denominador andam em tempos
diferentes") aplicada a um salto, não só a um percentual. Medidor solitário não
vira frase: nem "pico real" nem "bug do medidor" antes da confirmação cruzada.

## Como aplicar
1. Diante de salto de UM medidor: 2ª leitura — ela prova estabilidade do VALOR,
   não realidade do NÚMERO.
2. Casar janelas: anotar `farol.gerado` × `ga4.ts` × `lumina.coletado_em` antes de
   comparar (GA4 com ts 13:30 não responde sobre 14:00).
3. Veredito só com a janela defasada chegando (GA4 ts 14:30) + série de 3
   leituras na mesma direção.
4. Registrar "NÃO confirmado" sem alarmar a casa nem descartar a hipótese — o
   watch honesto vale para os dois lados (lição irmã de
   licoes/20260902_leitura_unica_nao_e_veredito.md, agora com o tripé inteiro).

## Reconfirmações do mesmo dia (sem arquivo novo)
- 2ª perda append-only no canal_dsn_revisores.md em ~30 min (XM-023: 586801142 →
  9de27cae8, 39s; feedback nº 2 da CL-072 sumiu das DUAS cópias) — o sync que
  repõe snapshot defasado é a CAUSA provável; protocolo mantido: registra, não
  restaura (ref. licoes/20260902_quebra_de_append_only_registra_nao_restaura.md).
- Carimbo textual de bloco NÃO é cursor: DSC-043 traz 14:08 mas foi commitado
  13:42:08; CL-072 traz 13:55 mas commit 13:51:41 — cursor é o git (XM-023).
