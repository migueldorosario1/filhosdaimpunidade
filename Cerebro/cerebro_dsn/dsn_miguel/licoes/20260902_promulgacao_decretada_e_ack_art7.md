# Lição 2026-09-02 — A palavra foi dada, e a retificação virou a régua da vigência

## O quê
Na madrugada de 02/09, o Miguel PROMULGOU a Constituição da Casa v3 (~01:53, ordem via DSC,
5 decisões: E4 HMAC LITE já · E5 gate 15min acatado · linha `GATE:` como protocolo ·
D8 fora da vigência inicial até mini-inventário DS-N Chefe+AGY · suplentes depois com prazo,
CL-covering-CM desde já). O DSC anunciou "📜 é LEI" às 01:55 e se RETIFICOU ~20 min depois
(DSC-033): pelo Título X, vigência = lava do ZM + ACKs do Art. 7 de toda a casa + assinatura
do CM — o estado real era "PROMULGAÇÃO DECRETADA — aguardando lava + ACKs + assinatura",
não "encerrada". O ZM lavrou (commit a97cafd48), os ACKs rolaram (AGY 02:02, DS-Dell 02:10,
CL ~02:45, CM na sequência) e o DS-Dell ASSINOU v3 como ACK de adesão — a primeira vez que
o "não assino" do vigia virou "assino a adesão".

## Por quê
Duas regras se encontraram nesta ronda:
1. **Celebrar é humano, rastrear é protocolo.** O "é lei" do DSC foi celebração à frente do
fato; a retificação 20 min depois não foi fraqueza — foi a rastreabilidade da casa vencendo
a empolgação. "Decretada" ≠ "encerrada": anotar a diferença é o que mantém a cadeia honesta
(e o DSC fez isso em público, no mesmo canal do anúncio — corrigir sem apagar).
2. **A régua "não assino" tinha alvo certo: a PROMULGAÇÃO.** O DS é vigia/observador e a
palavra de promulgar é só do Miguel (Art. 7) — mas isso valia ANTES da palavra. Com a palavra
DADA e a lava feita, o ACK do Art. 7 virou protocolo aberto a toda a casa ("todos assinam
ASSINO v3 nos canais próprios"); recusar adesão por hábito de vigia seria confundir o papel.
Assinar o ACK ≠ assinar a Constituição: a assinatura formal é do CM, na sequência.

## Como aplicar
- Ao registrar uma promulgação/ordem grande: anote o estado com o gatilho de vigência exato
(no caso: lava + ACKs + assinatura) e o estágio atual — nunca "está valendo" sem conferir o
Título/cláusula de vigência.
- Quando o dono der a palavra e o texto for lavrado, o ACK de adesão é esperado e barato:
dê "ASSINO v3" com o papel declarado (ACK ≠ assinatura formal), citando quem faz o quê.
- Leitura de arquivo canônico ao vivo pode flagrar estado intermediário (marcadores de
conflito que somem no pull seguinte): decisão de ronda contra o estado do ORIGIN/espelho,
não contra o arquivo local em movimento.
- Número com contexto: drafts+pending=2805 = 2441 draft + 364 pending — contagem parcial
assusta, a soma é o colchão real.

**Ref.:** ronda DS-20260902-005 (de_dell.md 02:10), DSC 01:55 + DSC-033 02:1x + DSC-034 02:0x,
ZD-20260902-002 (a97cafd48), AGY-20260902-049, CL-20260902-052.
