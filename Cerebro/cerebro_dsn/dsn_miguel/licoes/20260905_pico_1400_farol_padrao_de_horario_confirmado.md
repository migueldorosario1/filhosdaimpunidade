# Pico do FAROL às 14:00 é padrão de coletor, não público — veredito no recuo (190ª)

**Data:** 05/09/2026 · **Ronda:** DS-190 (DS-Dell, slot 14:30) · **Série:** DS-Dell

## O quê

O pico do FAROL às 14:00 virou **padrão de HORÁRIO confirmado na série DS-Dell** — não foi
público real, foi o coletor. A suspeita da 189ª (leitura única do API às 14:00: humanos
**1035**, 2,8x sobre os 371 das 13:35, com bots FLAT 336→341 e tripé mudo) teve o
**veredito no recuo da janela seguinte**: às 14:30 o humano caiu para **439** (-57,6% em
30 min) com bots estáveis (341→351) e LUMINA/GA4 andando pouco (LUMINA 67→59; GA4
186→211→195 com ts 14:00 = backlog conhecido, não gente).

## Por quê (assinatura do padrão)

1. **3ª ocorrência de padrão de horário na série**: 02/09 14:00 = 953 (lição «medidor
   solitário espera o tripé») · 05/09 14:00 = 1035 → 439 no recuo · mesma família do
   «pico fantasma 02:00» (04/09: 895 → 441).
2. **Gente real não triplica em 30 min de tarde** com o beacon andando só +12 e o GA4
   parado no backlog — o dígito sobe sozinho, sem o tripé acompanhar.
3. **2 leituras idênticas no mesmo minuto = a MESMA geração do farol**, não confirmação
   (farol gerado 14:00:01) — estabilidade do VALOR não é realidade do NÚMERO.
4. **2 vigias independentes convergiram**: minha leitura do API (14:30: 439h+351b) e o db
   do DS-N Chefe 196º (ts 14:00, gerado 14:25: 522h+347b, recuo do 955h da ts 13:30).
5. O pouso 439 sustenta o **degrau da tarde** (acima do vale do meio-dia ~371) — o recuo
   do pico não é queda do site; é o coletor voltando ao normal sobre um degrau real.

## Como aplicar

- **Leitura única nunca é veredito — para os DOIS lados**: dígito alto suspeito (pico) e
  dígito baixo suspeito (vale) só se confirmam no recuo da janela seguinte (~30 min).
- **Registrar SEM alarmar**: pico às 14:00 com bots flat + tripé mudo = coletor; não
  reportar degrau falso ao dono.
- **Fechar anomalia no recuo com o valor de pouso registrado** (aqui: 439 às 14:30) —
  o pouso vira o dado de referência da próxima ocorrência.
- Convergência de 2 vigias (API + db) fecha o caso no mesmo slot — o watch paralelo
  encurta o tempo de veredito.

## Estado

**CONFIRMADO/FECHADO** na DS-190 (14:30) — obs operacional da 189ª promovida a lição
formal. Arquivos irmãos: licoes/20260904_pico_fantasma_0200_e_o_coletor_nao_o_publico.md
(família 02:00) · lição 02/09 «medidor solitário espera o tripé» (VIVA).

## ADENDO 15:36 (DS-192) — GENERALIZAÇÃO «TOPO DE HORA»: não são só as 14:00

A obs operacional da 191ª (leitura 15:00 = humanos 1093 com bots FLAT e tripé mudo)
fechou na ronda seguinte: **15:30 = 384 humanos (-65% em 30 min), bots 332 FLAT** —
mesma assinatura do pico 14:00 (1035→439) e da família db (13:30 955h → 14:00 522h
firmado). **5ª ocorrência no dia** (db 13:30 955h · API 14:03 1035h · db 14:00 522h
firmado · API 15:00 1093h · pouso 384). Generalização da lição: **o FAROL dispara
~2-2,5x o nível real (~350-550) em LEITURAS DE MARCA (topo de hora OU :30, conforme a
torneira) e o db firmado ~25-30 min depois devolve o nível** — o que distingue o
degrau do pico é o TRIPÉ: pico de coletor tem LUMINA/GA4 imóveis (tripé mudo);
quando LUMINA (53→81) e GA4 (187→245) sobem JUNTO com o FAROL no nível real, é gente
de verdade — o degrau da tarde se sustenta com o tripé andando. Veredito sempre no
recuo (~30 min), nunca na leitura única; 2 picos no mesmo dia, 2 vereditos no recuo —
a régua se pagou 2x no dia. (obs da 191ª promovida a ADENDO formal — família
«medidor solitário» 02/09 + «pico fantasma 02:00» 04/09 + «pico 14:00» 05/09)

**ADENDO 06/09 (223ª DS-Dell) — o padrão repetiu no 1º dia de retomada:** leitura 08:00 (API CCTV ao vivo) = FAROL 1225/943h contra 688/380h às 07:33 (salto 2,5x) com bots FLAT (282 × 308) e tripé MUDO (LUMINA 46 < 60 · GA4 114 < 133) — a assinatura do coletor de topo de hora se repetiu no dia em que a esteira RETOMOU (2 posts 07:18/07:45 + mutirão até 09:40): produção e coletor são fatos independentes, a régua do medidor não muda com a saúde da esteira (família das lições 193ª + 215ª); 1ª ocorrência da família num dia de retomada pós-incidente — veredito no recuo (~30 min) como sempre. (obs da 223ª promovida a ADENDO — evidência de que o coletor não respeita calendário de produção)

**ADENDO 06/09 (224ª DS-Dell) — VEREDITO DO RECUO FECHADO: o salto 08:00 era coletor:** o pico das 08:00 (FAROL 1225/943h na 223ª) REGREDIU na leitura 08:30 (FAROL 722/354h — humanos -62% em 30 min) com pouso 354 ≈ o nível real da manhã (380 às 07:33; banda 325-380) — a promessa de veredito da 223ª FECHOU no recuo, 5ª confirmação diurna da família no 05-06/09 (14:00 1035→439 · 15:00 1093 · 02/09 953) e 1ª num dia de retomada pós-incidente: o coletor de topo de hora dispara independente da saúde da esteira (produção × público = fatos separados, lição 215ª) e o pouso no nível real é o que separa pico fantasma de degrau real — leitura única nunca é veredito para os DOIS lados. (obs da 224ª — fecho do veredito declarado na 223ª; família «medidor solitário» consolidada com o ciclo completo pico → recuo → pouso)
