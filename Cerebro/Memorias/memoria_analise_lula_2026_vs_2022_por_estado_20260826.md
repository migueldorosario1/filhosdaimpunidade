# 🗳️ MEMÓRIA — ANÁLISE: onde Lula está MELHOR hoje que em 2022 (estado por estado, em % e em Nº de eleitores)

> **Pedido do Miguel (26/08 ~10:50):** análise abrangente para alimentar um artigo — onde Lula está melhor hoje (pesquisas, em número de eleitores e em vantagem sobre o concorrente) vs. resultado do 1º E do 2º turno de 2022, nacional e em cada estado, sem deixar UF de fora. Hierarquia de credibilidade definida por ele: **Datafolha › Quaest › AtlasIntel › Real Time › BTG/Nexus** (todas usadas).
> **Base de dados:** planilha validada `ZCodeProject/pesquisas_presidenciais_eleitores_2026-08-26.xlsx` (agora COM Sergipe — 38 linhas) + memória de pesquisas 24-25/08 + API oficial TSE 2022 + aptos TSE 2026.
> **Régua única (como o Miguel pediu):** TODOS os percentuais sobre o TOTAL do eleitorado (nunca votos válidos). Pesquisa-2026 × 158.745.463 aptos (TSE 20/07/2026); 2022 × 156.454.011 aptos.
> **Autor:** ZCode/Kimi K3 · 26/08/2026 ~11:50 BRT.

---

## 1. MÉTODO (para a caixa de metodologia do artigo)

- **Margem** = % do candidato sobre o eleitorado total (Lula% − adversário%). Comparável entre eras porque a régua é a mesma.
- **Δ margem** = margem hoje − margem 2022 (positivo = Lula melhor). Calculada vs. 1º turno 2022 e vs. 2º turno 2022.
- **Δ N Lula** = Nº de eleitores do Lula hoje (pesquisa × aptos 2026 da UF) − votos oficiais do Lula no 1ºT de 2022 (TSE).
- **Dois eixos que contam a história real:** ΔL = variação da participação do LULA (p.p. sobre eleitorado); ΔF = variação da participação do FLÁVIO/Bolsonaro. Δ margem = ΔL − ΔF.
- **Pesquisa "principal" por UF** segue a hierarquia Datafolha › Quaest › AtlasIntel › Real Time › BTG/Nexus › demais; alternativas citadas quando divergem (MG, SP, PA, RS, PE, PB, ES, DF).
- **Ressalvas de data:** GO (09/07, com Caiado liderando), RR (março/2026 — a mais velha), ES-Quaest (julho), AM (só cenário com Marçal).

---

## 2. TABELA-MESTRE (pesquisa principal por UF × 2022 oficial — tudo sobre eleitorado total)

| UF | Pesquisa | Lula hj % | Lula 22-1T % | ΔL | Flávio hj % | Flávio 22-1T % | ΔF | Margem hj | Margem 22-1T | Δ margem 1T | Margem 22-2T | Δ margem 2T | Lula N hoje | Δ N Lula |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AC | Data Control 24/08 | 23,2 | 22,0 | +1,2 | 49,5 | 46,9 | +2,6 | −26,3 | −24,9 | −1,4 | −28,3 | +2,0 | 142.535 | +13.513 |
| AL | Quaest 24/08 | 44 | 41,9 | +2,1 | 29 | 26,7 | +2,3 | +15,0 | +15,2 | −0,2 | +12,4 | +2,6 | 1.074.389 | +100.233 |
| AM | Quaest 25/08* | 38 | 38,5 | −0,5 | 35 | 33,3 | +1,7 | +3,0 | +5,3 | −2,3 | +1,6 | +1,4 | 1.064.449 | +44.765 |
| AP | Quaest 25/08 | 36 | 35,9 | +0,1 | 33 | 34,1 | −1,1 | +3,0 | +1,8 | +1,2 | −1,9 | +4,9 | 207.912 | +10.530 |
| BA | OPNUS 24/08 | 60 | 52,1 | +7,9 | 17 | 18,1 | −1,1 | +43,0 | +33,9 | **+9,1** | +33,2 | +9,8 | 6.792.603 | +919.522 |
| CE | Real Time 20/08 | 65 | 52,5 | +12,5 | 21 | 20,2 | +0,8 | +44,0 | +32,3 | **+11,7** | +31,9 | +12,1 | 4.549.021 | +970.666 |
| DF | Datafolha 21/08 | 31 | 29,4 | +1,6 | 39 | 41,3 | −2,3 | −8,0 | −11,8 | +3,8 | −14,1 | +6,1 | 698.471 | +48.937 |
| ES | Quaest jul/26 | 30 | 30,7 | −0,7 | 30 | 39,7 | −9,7 | 0,0 | −9,0 | **+9,0** | −12,2 | +12,2 | 897.147 | −201 |
| GO | Real Time 09/07 | 27 | 29,9 | −2,9 | 25 | 39,4 | −14,4 | +2,0 | −9,6 | **+11,6** | −13,4 | +15,4 | 1.371.882 | −82.841 |
| MA | Quaest 24/08 | 58 | 51,7 | +6,3 | 20 | 19,5 | +0,5 | +38,0 | +32,1 | +5,9 | +31,5 | +6,5 | 3.008.206 | +404.752 |
| MG | Datafolha 21/08 | 37 | 35,6 | +1,4 | 31 | 32,2 | −1,2 | +6,0 | +3,5 | +2,5 | +0,3 | +5,7 | 6.059.734 | +257.163 |
| MS | Quaest 25/08 | 27 | 29,5 | −2,5 | 33 | 39,8 | −6,8 | −6,0 | −10,3 | +4,3 | −14,1 | +8,1 | 546.719 | −41.604 |
| MT | Quaest 25/08 | 26 | 25,7 | +0,3 | 43 | 44,7 | −1,7 | −17,0 | −19,0 | +2,0 | −22,8 | +5,8 | 685.940 | +52.192 |
| PA | Veritá 25/08 | 44,2 | 40,2 | +4,0 | 44,6 | 31,0 | +13,6 | −0,4 | +9,2 | **−9,6** | +7,2 | −7,6 | 2.769.287 | +325.557 |
| PB | Quaest 25/08 | 50 | 50,3 | −0,3 | 21 | 23,2 | −2,2 | +29,0 | +27,1 | +1,9 | +25,9 | +3,1 | 1.623.699 | +68.831 |
| PE | Datafolha 21/08 | 56 | 50,7 | +5,3 | 24 | 23,2 | +0,8 | +32,0 | +27,5 | +4,5 | +26,3 | +5,7 | 4.046.417 | +488.095 |
| PI | Datafolha 22/08 | 60 | 59,1 | +0,9 | 19 | 15,8 | +3,2 | +41,0 | +43,2 | −2,2 | +42,2 | −1,2 | 1.625.843 | +107.835 |
| PR | Quaest 24/08 | 23 | 27,9 | −4,9 | 41 | 42,8 | −1,8 | −18,0 | −14,9 | −3,1 | −19,5 | +1,5 | 1.980.076 | −383.416 |
| RJ | Quaest 25/08 | 29 | 30,0 | −1,0 | 31 | 37,7 | −6,7 | −2,0 | −7,7 | +5,7 | −9,7 | +7,7 | 3.728.530 | −118.613 |
| RN | Quaest 24/08 | 54 | 49,5 | +4,5 | 20 | 24,4 | −4,4 | +34,0 | +25,1 | +8,9 | +24,1 | +9,9 | 1.436.705 | +172.526 |
| RO | Quaest 25/08 | 25 | 21,3 | +3,7 | 45 | 47,3 | −2,3 | −20,0 | −26,0 | +6,0 | −30,1 | +10,1 | 316.776 | +55.027 |
| RR | Veritá mar/26 | 19,3 | 18,8 | +0,5 | 72,6 | 56,6 | +16,0 | −53,3 | −37,9 | −15,4 | −39,9 | −13,4 | 77.489 | +8.729 |
| RS | Quaest 24/08 | 28 | 32,7 | −4,7 | 34 | 37,8 | −3,8 | −6,0 | −5,1 | −0,9 | −9,8 | +3,8 | 2.387.345 | −419.327 |
| SC | Quaest 24/08 | 20 | 23,3 | −3,3 | 45 | 49,0 | −4,0 | −25,0 | −25,7 | +0,7 | −30,8 | +5,8 | 1.145.151 | −134.065 |
| SE | Real Time 03/08 | 60 | 49,6 | +10,4 | 23 | 22,7 | +0,3 | +37,0 | +26,9 | **+10,1** | +26,4 | +10,6 | 1.044.144 | +215.428 |
| SP | Quaest 25/08 | 29 | 30,2 | −1,2 | 30 | 35,3 | −5,3 | −1,0 | −5,0 | +4,0 | −7,8 | +6,8 | 9.890.226 | −599.806 |
| TO | Quaest 25/08 | 37 | 39,7 | −2,7 | 32 | 34,7 | −2,7 | +5,0 | +5,0 | −0,0 | +2,1 | +2,9 | 437.454 | +3.151 |
| BR | Datafolha 21/08 | 39 | 36,6 | +2,4 | 33 | 32,6 | +0,4 | +6,0 | +4,0 | +2,0 | +1,4 | +4,6 | 61.910.731 | +4.651.227 |
| BR | BTG/Nexus 24/08 | 41 | 36,6 | +4,4 | 37 | 32,6 | +4,4 | +4,0 | +4,0 | +0,0 | +1,4 | +2,6 | 65.085.640 | +7.826.136 |

*AM = cenário com Marçal (único publicado). 2º turnos pesquisados: BR-DF 47×43 (+2,6 p.p. vs 2T22) · BR-Nexus 46×45 (−0,4) · CE 66×27 (+7,1) · SE 63×27 (+9,6) · PI 68×24 (+1,8) · PB-RT 59×32 (+1,1) · SP-RT 44×49 (+2,8) · SP-GERP 41×48 (+0,8) · SP-DF-slice 42×47 (+2,8) · ES-Quaest 36×42 (+6,2) · ES-RT 43×49 (+6,2) · DF 39×51 (+2,1) · RS-RT 42×52 (−0,2) · GO-RT 33×56 (−9,6, pesq. julho) · PA-Veritá 49,1×50,9 (−9,0).*

---

## 3. SÍNTESE NACIONAL (o esqueleto do artigo)

**1. Nacional: estável a levemente melhor.** Datafolha: margem +6,0 vs +4,0 (1T22) → +2,0 p.p.; 2ºT 47×43 (+4) vs +1,4 → +2,6. Nexus: margem +4 vs +4 → estável; 2T +1 vs +1,4 → −0,4. Em votos: 61,9 a 65,1 milhões hoje × 57,3 milhões em 2022 (**+4,65 a +7,83 milhões de eleitores**).

**2. A muralha Norte+Nordeste ENGROSSOU.** Das 10 maiores melhoras de margem do país, 6 são N/NE: CE +11,7 · GO* +11,6 · SE +10,1 · BA +9,1 · ES* +9,0 · RN +8,9. E são ganhos de participação real do Lula (ΔL positivo): CE +12,5 p.p., SE +10,4, BA +7,9, MA +6,3, PE +5,3, RN +4,5 — não é só o adversário caindo, é Lula CRESCENDO sobre o eleitorado total.

**3. O Sudeste saiu da derrota folgada para o EMPATE.** Em 2022-1T: SP −5,0 · RJ −7,7 · ES −9,0 · MG +3,5. Hoje: SP −1 · RJ −2 · ES 0 · MG +6 (Datafolha) ou −1 (Quaest). Dinâmica diferente do NE: lá Lula cresce; aqui **Flávio sangra mais que Lula** (SP: ΔL −1,2 × ΔF −5,3; RJ: −1,0 × −6,7; ES: −0,7 × −9,7) — voto migrando para indecisos/outros.

**4. Sul: PR é o único estado claramente PIOR no 1ºT** (Δ −3,1; Lula perde 4,9 p.p. de participação, Flávio só 1,8). SC estável (−25); RS estável no 1ºT (−0,9) mas melhor vs 2T22 (+3,8).

**5. Centro-Oeste: déficits encolhem** (MS +4,3 · DF +3,8 · MT +2,0). GO é caso especial: Caiado lidera com 37% e derruba Flávio para 25% (ΔF −14,4) — pesquisa de 09/07, a vigiar.

**6. Três alertas de leitura:** **PA** (Veritá mostra Flávio +13,6 p.p. de participação e virada de +9,2 para −0,4 — mas é voz automatizada e a AtlasIntel da mesma semana diverge; estado-dúvida nº 2), **RR** (única é de março), **MG** (Datafolha Lula +6 × Quaest Flávio +1 — estado-dúvida nº 1, divergência de 7 p.p.).

**7. Em votos absolutos, Lula está acima do 1ºT-2022 em 18 das 26 UFs medidas + nas 2 nacionais.** Perdas concentradas no eixo SP/RS/PR/SC/RJ (e GO/MS/DF na Quaest) — mas em SP/RJ/SC a margem % melhorou mesmo com N menor (eleitorado encolheu em SP/RS e o adversário caiu mais).

---

## 4. ESTADO POR ESTADO (blocos prontos para o artigo)

### NORDESTE (a muralha engrossou)

**BA — 🟢 muito melhor.** OPNUS 24/08: Lula 60% (6,79 mi) × Flávio 17% (1,92 mi) → margem +43,0. 2022-1T: 52,1% × 18,1% (+33,9); 2T 54,0% × 20,9% (+33,2). **Δ +9,1 p.p. (1T) / +9,8 (2T); +919.522 eleitores a mais que 2022.** Lula cresce 7,9 p.p. de participação; Flávio cai 1,1. Maior colégio eleitoral do NE, melhora gigante.

**CE — 🟢 a melhor melhora do país.** Real Time 20/08: 65% (4,55 mi) × 21% (1,47 mi) → +44,0. 2022-1T +32,3; 2T +31,9. **Δ +11,7/+12,1; +970.666 eleitores.** 2ºT hoje: 66×27 (+7,1 vs 2T22). Lula +12,5 p.p. de participação — o maior ΔL do Brasil.

**SE — 🟢 top-3.** Real Time 03/08: 60% (1,04 mi) × 23% (400 mil) → +37,0. 2022-1T +26,9; 2T +26,4. **Δ +10,1/+10,6; +215.428 eleitores.** 2ºT hoje: 63×27 (+9,6). (IFP julho confirma: 52,5×23,5.) Lula +10,4 p.p. de participação.

**MA — 🟢 muito melhor.** Quaest 24/08: 58% (3,01 mi) × 20% (1,04 mi) → +38,0. 2022-1T +32,1; 2T +31,5. **Δ +5,9/+6,5; +404.752 eleitores.** Lula +6,3 p.p.

**RN — 🟢 muito melhor.** Quaest 24/08: 54% (1,44 mi) × 20% (532 mil) → +34,0. 2022-1T +25,1; 2T +24,1. **Δ +8,9/+9,9; +172.526 eleitores.** Lula +4,5 e Flávio −4,4 — os dois eixos a favor.

**PE — 🟢 melhor.** Datafolha 21/08: 56% (4,05 mi) × 24% (1,73 mi) → +32,0. 2022-1T +27,5; 2T +26,3. **Δ +4,5/+5,7; +488.095 eleitores.** (Quaest é ainda mais otimista: 54×19 → +35.) Lula +5,3 p.p.

**PB — 🟢 melhor leve.** Quaest 25/08: 50% (1,62 mi) × 21% (682 mil) → +29,0. 2022-1T +27,1; 2T +25,9. **Δ +1,9/+3,1; +68.831 eleitores.** (Real Time: 55×26; 2ºT 59×32, +1,1 vs 2T22.)

**PI — 🟡 estável no topo.** Datafolha 22/08: 60% (1,63 mi) × 19% (515 mil) → +41,0. 2022-1T +43,2; 2T +42,2. **Δ −2,2/−1,2; +107.835 eleitores.** Margem segue a maior do país; 2ºT hoje 68×24 (+1,8). Flávio sobe 3,2 p.p., Lula +0,9.

**AL — 🟡 estável.** Quaest 24/08: 44% (1,07 mi) × 29% (708 mil) → +15,0. 2022-1T +15,2; 2T +12,4. **Δ −0,2/+2,6; +100.233 eleitores.** Ambos sobem (Lula +2,1, Flávio +2,3).

### SUDESTE (da derrota folgada ao empate)

**SP — 🟢 margem melhorou para empate técnico.** Quaest 25/08: Lula 29% (9,89 mi) × Flávio 30% (10,23 mi) → −1,0. 2022-1T: −5,0; 2T: −7,8. **Δ margem +4,0/+6,8.** Em N, Lula tem −599.806 votos vs 2022 — mas note: o eleitorado de SP ENCOLHEU 581 mil (34,68→34,10 mi, único estado com MG… não, SP e RS caíram) e Flávio cai 5,3 p.p. de participação (35,3→30) contra 1,2 de Lula. 2ºT hoje: RT 44×49, GERP 41×48, Datafolha-slice 42×47 — Flávio à frente em todas, MAS margens menores que a derrota de 2022 (−5 a −7 vs −7,8).

**RJ — 🟢 de −7,7 a −2 (empate técnico).** Quaest 25/08: 29% (3,73 mi) × 31% (3,99 mi). 2022-1T −7,7; 2T −9,7. **Δ +5,7/+7,7.** Flávio cai 6,7 p.p. de participação (37,7→31); Lula −1,0. N: −118.613.

**MG — ⚠️ ESTADO-DÚVIDA Nº 1.** Datafolha 21/08: **Lula 37% (6,06 mi) × Flávio 31% (5,08 mi) → +6** (2022-1T: +3,5 → Δ +2,5; ΔN +257 mil; Zema 10). Quaest 25/08: **Flávio 31 × Lula 30 → −1** (Δ −4,5; ΔN −889 mil; Zema 7). Divergência de 7 p.p. entre os dois melhores institutos, no 2º maior colégio do país. O artigo deve apresentar os dois cenários.

**ES — 🟢 de −9,0 a EMPATE EXATO.** Quaest jul/26: 30×30 (897 mil × 897 mil — ΔN de −201 votos vs 2022, o estado mais empatado do Brasil). 2022-1T −9,0; 2T −12,2. **Δ +9,0/+12,2.** Flávio cai 9,7 p.p. de participação (39,7→30). 2ºT hoje: Quaest 36×42 e RT 43×49 — Flávio leva, mas com margem ~6 (metade da de 2022). (Real Time 22/07: 34×36.)

### SUL (hostil, com PR piorando)

**RS — 🟡 estável no 1ºT, melhor vs 2T.** Quaest 24/08: 28% (2,39 mi) × 34% (2,90 mi) → −6,0. 2022-1T −5,1; 2T −9,8. **Δ −0,9/+3,8; ΔN −419 mil** (eleitorado encolheu 63 mil). Lula perde 4,7 p.p. de participação — a maior queda do eixo Sul. (Real Time 25/08 diverge para melhor: 39×40 → −1; 2ºT 42×52, estável −0,2.)

**PR — 🔴 o único claramente pior no 1ºT.** Quaest 24/08: 23% (1,98 mi) × 41% (3,53 mi) → −18,0. 2022-1T −14,9; 2T −19,5. **Δ −3,1/+1,5; ΔN −383 mil.** Lula perde 4,9 p.p. de participação (27,9→23), Flávio só 1,8 — é o estado onde Lula mais sangra em % no país (exceto RS).

**SC — 🟡 estável (muralha bolsonarista).** Quaest 24/08: 20% (1,15 mi) × 45% (2,58 mi) → −25,0. 2022-1T −25,7; 2T −30,8. **Δ +0,7/+5,8; ΔN −134 mil.** Ambos caem ~3-4 p.p. de participação.

### CENTRO-OESTE (déficits encolhem)

**DF — 🟢 melhor.** Datafolha 21/08: Lula 31% (698 mil) × Flávio 39% (878 mil) → −8,0. 2022-1T −11,8; 2T −14,1. **Δ +3,8/+6,1; ΔN +49 mil.** (Quaest 25/08 é ainda melhor para Lula: 28×26 → +2, com Caiado 13%.) 2ºT Datafolha: 39×51 (+2,1 vs 2T22).

**GO — 🟢 com asterisco.** Real Time 09/07: Lula 27% (1,37 mi) × Flávio 25% (1,27 mi) → +2,0 — **virada de −9,6 para +2** (Δ +11,6/+15,4). MAS: **Caiado LIDERA com 37%** (1,88 mi) — fenômeno local que derruba Flávio (ΔF −14,4); pesquisa de julho, a mais velha do CO. 2ºT dessa pesquisa: Flávio 56×33 (−9,6 vs 2T22). Tratar como cenário datado.

**MS — 🟢 déficit encolheu.** Quaest 25/08: 27% (547 mil) × 33% (668 mil) → −6,0. 2022-1T −10,3; 2T −14,1. **Δ +4,3/+8,1; ΔN −42 mil.** Flávio −6,8 p.p.

**MT — 🟢 melhor leve.** Quaest 25/08: 26% (686 mil) × 43% (1,14 mi) → −17,0. 2022-1T −19,0; 2T −22,8. **Δ +2,0/+5,8; ΔN +52 mil.** Lula +0,3 p.p. de participação.

### NORTE (mistura de avanço lulista e dois alertas)

**PA — 🔴 ESTADO-DÚVIDA Nº 2.** Veritá 25/08: Lula 44,2% (2,77 mi) × Flávio 44,6% (2,79 mi) → −0,4. 2022-1T: **+9,2**; 2T +7,2. **Δ −9,6/−7,6 — a pior virada contra Lula no mapa.** Flávio +13,6 p.p. de participação (31,0→44,6), Lula +4,0. Ressalvas: metodologia de voz automatizada; AtlasIntel/Faciapa (23/08, governo) e o cenário de 2ºT (50,9×49,1) sugerem disputa, não virada consolidada. Em N, Lula segue +326 mil acima de 2022. Vigilância máxima no artigo.

**AM — 🟡 estável com asterisco.** Quaest 25/08 (único cenário: COM Marçal): 38% (1,06 mi) × 35% (980 mil) → +3,0. 2022-1T +5,3; 2T +1,6. **Δ −2,3/+1,4; ΔN +45 mil.**

**AP — 🟢 melhor.** Quaest 25/08: 36% (208 mil) × 33% (191 mil) → +3,0. 2022-1T +1,8; 2T **−1,9** (AP foi o único estado do NE… não, do Norte, que Lula perdeu no 2ºT de 2022 — hoje lidera). **Δ +1,2/+4,9; ΔN +11 mil.**

**TO — 🟡 estável.** Quaest 25/08: 37% (437 mil) × 32% (378 mil) → +5,0. 2022-1T +5,0; 2T +2,1. **Δ −0,0/+2,9; ΔN +3 mil.** Ambos −2,7 p.p.

**RO — 🟢 déficit encolhe muito.** Quaest 25/08: 25% (317 mil) × 45% (570 mil) → −20,0. 2022-1T −26,0; 2T −30,1. **Δ +6,0/+10,1; ΔN +55 mil.** Lula +3,7 p.p. de participação.

**AC — 🟡 estável.** Data Control 24/08: 23,2% (143 mil) × 49,5% (304 mil) → −26,3. 2022-1T −24,9; 2T −28,3. **Δ −1,4/+2,0; ΔN +14 mil.** Ambos sobem (Flávio +2,6, Lula +1,2).

**RR — 🔴 com asterisco (dado velho).** Veritá mar/26: 19,3% (77 mil) × 72,6% (291 mil) → −53,3. 2022-1T −37,9; 2T −39,9. **Δ −15,4/−13,4; ΔN +9 mil.** Flávio +16,0 p.p. de participação (56,6→72,6) — mas é a pesquisa mais velha da tabela (março), metodologia de voz. Confirmar com pesquisa nova antes de publicar.

---

## 5. RANKINGS PRONTOS

**Δ margem vs 1ºT 2022 (melhor → pior):** CE +11,7 · GO +11,6* · SE +10,1 · BA +9,1 · ES +9,0 · RN +8,9 · RO +6,0 · MA +5,9 · RJ +5,7 · PE +4,5 · MS +4,3 · SP +4,0 · DF +3,8 · MG +2,5** · BR +2,0 · MT +2,0 · PB +1,9 · AP +1,2 · SC +0,7 · TO −0,0 · AL −0,2 · RS −0,9 · AC −1,4 · PI −2,2 · AM −2,3 · PR −3,1 · PA −9,6** · RR −15,4*

**Δ N Lula vs 1ºT 2022 (ganhos):** BR-Nexus +7,83 mi · BR-DF +4,65 mi · CE +971 mil · BA +920 mil · PE +488 mil · MA +405 mil · PA +326 mil · MG +257 mil (Datafolha) · SE +215 mil · RN +173 mil · PI +108 mil · AL +100 mil · PB +69 mil · RO +55 mil · MT +52 mil · DF +49 mil · AM +45 mil · AC +14 mil · AP +11 mil · RR +9 mil · TO +3 mil.
**(perdas):** SP −600 mil · RS −419 mil · PR −383 mil · SC −134 mil · RJ −119 mil · GO −83 mil · MS −42 mil · ES −201.

**Vereditos:** 🟢 melhor (19): CE SE BA RN MA PE PB RO ES SP RJ MS DF MG(DF) MT AP GO* AL≈ BR ≈estável positivo · 🟡 estável (6): PI TO AM AC RS SC · 🔴 pior (3): PR PA** RR*.

---

## 6. RESSALVAS EDITORIAIS OBRIGATÓRIAS (para o artigo não tomar invertida)

1. **MG:** Datafolha (+6 Lula) × Quaest (+1 Flávio) — citar as duas, sem escolher.
2. **PA:** Veritá (virada pró-Flávio) × contexto AtlasIntel; metodologia de voz automatizada.
3. **GO:** pesquisa de 09/07 com Caiado líder — não projetar sem atualização.
4. **RR:** única de março/2026 — marcar como datada.
5. **AM:** só cenário com Marçal.
6. **ES-Quaest:** B/N e indecisos não publicados em texto (soma parcial).
7. **SE/CE:** só Real Time na janela (instituto de pontuação intermediária na hierarquia do Miguel).
8. **Somas 98–101%** = arredondamento dos institutos (nota na planilha).
9. **ΔN mistura** variação de voto + crescimento/encolhimento do eleitorado (SP e RS encolheram; RR cresceu 9,6%).

**Estado da missão:** análise completa 27/27 UFs + nacional, gravada para o artigo. Planilha atualizada com Sergipe (38 linhas, Review 6/6 PASS, validate 0) e replicada (Downloads, Cerebro/Dados, GitHub, Google Drive — mesmo link). Pendência: nenhuma. De você: escrever o artigo; se quiser, preparo o rascunho da estrutura dele ou a versão de governadores.

🕐 26/08/2026 11:50 · ZCode/Kimi K3
📁 Fóruns-irmãos: `forum_pesquisas_eleitorais_24_25_agosto_2026_20260825.md` (adendo 26/08) · `forum_eleitorado_2026_aptos_por_uf_20260826.md`
