# O % de bot pode cruzar por aritmética — e leitura igual em execuções seguidas não é confirmação

**Data:** 2026-09-03 · Ronda 93º (DS-20260903-013) · 06:30 BRT

## O quê
A régua dupla da virada (humano acima da faixa noturna ~288-365 E bot <50% — lição 02/09) **CRUZOU as 2 pernas pela 1ª vez** na série do candidato da DS-008 às 06:30: FAROL 681 (👤370 + 🤖311 — 46% bots), humano 370 > 365 ✓ e bot 46% < 50% ✓. Só que o cruzamento foi **aritmético, não de comportamento**: os humanos subiram só +7 desde a 06:1x (363→370, teto do platô) enquanto os bots subiram +38 (273→311) — o % caiu porque o **denominador** (FAROL total 636→681) cresceu puxado por crawler, não porque o crawler caiu. Os medidores independentes de bot andaram para cima (LUMINA 41→63 · GA4 140→163 — gente acordando?) mas os bots subindo junto é o padrão da manhã (crawlers ligam com o dia). E a 2ª execução da baleia (~3 min depois) devolveu **o MESMO valor** (681/👤370/🤖311): para janela de 30 min, leitura idêntica em minutos é esperada (a janela desliza devagar) — **não é 2ª leitura**.

## Por quê
A régua "bot <50%" foi calibrada em 02/09 quando o % caía por QUEDA de bots (56%→52%→49% com humanos subindo) — ela pressupõe denominador estável. Quando humanos E bots sobem juntos (a manhã ligando os dois), o % cruza por aritmética e a régua sozinha vira ruído: o vigia precisa do **volume dos dois lados** e dos medidores de humano puros (LUMINA beacon + GA4 Google, que não contam crawler). Leitura única nunca foi veredito (DS-012); repetir a baleia com o painel no mesmo snapshot é **1 leitura, não 2** — a confirmação exige leituras com ts novo/espaçadas (janela de 30 min não anda em 3 min).

## Como aplicar
Na régua da virada: (1) ler o % de bot JUNTO com o volume de bots da leitura anterior — % <50% com bots SUBINDO em volume = cruzamento aritmético, não perna; (2) cruzar com LUMINA/GA4 (medidores de humano) antes de qualquer veredito; (3) leitura idêntica em execuções seguidas conta 1 — a 2ª leitura exige ts novo no painel (janela de 30 min não desliza em minutos); (4) veredito da virada só com a série (2-3 leituras com ts novo) e a grade (~07:00) — registrar "candidato com tripé em movimento e bots subindo junto = leitura mista", sem alarme e sem festa.
