# 🗳️ MEMÓRIA — Compilação de pesquisas eleitorais divulgadas em 24–25/08/2026 (Quaest + demais institutos)

> **Missão:** pedido do Miguel em 25/08/2026 ~20:48 — "reunir todas as pesquisas Quaest divulgadas hoje e ontem, em todos os estados, para presidente e para governador (diferenciando quem é do Lula, quem é do Flávio), e outras pesquisas se tiver".
> **Método:** 3 sub-agentes de pesquisa web (WebSearch/WebFetch) + checagem direta. REGRA DE OURO cumprida: nenhum nome próprio/número saiu de memória de modelo — tudo tem URL de fonte. Janela estrita: divulgadas em 24/08 (segunda) e 25/08 (terça). Fora da janela = marcado † (contexto).
> **Executor:** ZCode/Qwen 3.8 (coleta) → ZCode/Kimi K3 (consolidação, após troca de modelo a pedido do Miguel ~23h).
> Fórum-irmão (Tema Duplo): `Foruns/forum_pesquisas_eleitorais_24_25_agosto_2026_20260825.md`

---

## PARTE 1 — PRESIDENTE

### 1.1 Nacional — BTG/Nexus (11ª rodada) — divulgada 24/08 (ÚNICA nacional na janela)
- **Contratante:** Banco BTG Pactual (R$ 164.888,89). **Campo:** 21–23/08, telefone (CATI), 27 UFs. **Amostra:** 2.006 (16+). **Margem:** ±2 p.p., 95%. **Registro:** BR-09028/2026. Estatístico Neale El-Dash.
- **Espontânea:** Lula 38 · Flávio 31 · Renan Santos 2 · Caiado 2 · Zema 2 · outros 4 · B/N 6 · NS 15.
- **Estimulada 1ºT (sem Marçal):** Lula 41 (40) · Flávio 37 (36) · Caiado 5 · Renan Santos 3 · Zema 3 · Cury 2 · Samara 1. B/N 5 · NS 3.
- **Estimulada 1ºT (com Marçal):** Lula 40 · Flávio 34 · Caiado 5 · Marçal 4 · Renan 3 · Zema 2 · Cury 2 · Samara 1 · Rui Costa Pimenta 1 · Clariana Barão 1.
- **2º turno:** Lula 46 × Flávio 45 (anterior 47×45) · Lula 46 × Caiado 42 · Lula 47 × Zema 40 · Lula 47 × Renan Santos 35.
- **Rejeição:** Lula 49 · Flávio 48. **Voto definitivo:** 80% (recorde da série). **Governo Lula:** aprova 48 × desaprova 49.
- **URLs:** PDF íntegra https://static.poder360.com.br/uploads/2026/08/Pesquisa-BTG-Nexus-Eleicoes-24-ago-2026.pdf · https://www.poder360.com.br/poder-eleicoes/lula-tem-46-contra-45-de-flavio-no-2o-turno-diz-btg-nexus/ · https://www.nexus.fsb.com.br/estudos-divulgados/pesquisa-btg-nexus-de-intencao-de-votos-para-presidente-do-brasil-24-de-agosto-de-2026/

### 1.2 Quaest por estado (encomendadas pela Globo/afiliadas; presencial; 95%)
**Onda 1 — divulgadas 24/08 (campo 20–23/08; ±3 p.p.):**

| UF | Registro TSE | Amostra | 1ºT sem Marçal (%) | 1ºT com Marçal (%) |
|---|---|---|---|---|
| AL | AL-05503/2026 + BR-09091/2026 | 804 | Lula 44 · Flávio 29 · Renan 2 · Caiado 1 · Cury 1 · Samara 1 · Rui 1; B/N 10 · ind. 11 | Lula 45 · Flávio 30 · Renan 2 · Marçal 1 · Cury 1 |
| MA | MA-02558/26 + BR-01389/2026 | 900 | Lula 58 · Flávio 20 · Caiado 2 · Renan 2 · Cury 1 · Grassi 1 | Lula 57 · Flávio 20 · Marçal 1 |
| PR | PR-05388/2026 | 804 | Flávio 41 · Lula 23 · Caiado 5 · Zema 3 · Renan 2 · Cury 1 · Edmilson 1 | Flávio 42 · Lula 24 · Marçal 4 · Caiado 3 |
| RN | RN-00876/2026 | 804 | Lula 54 · Flávio 20 · Renan 2 · Caiado 2 · Cury 1 · Zema 1; B/N 11 · ind. 9 | Lula 56 · Flávio 19 · Marçal 1 |
| RS | RS-06875/2026 | 900 | Flávio 34 · Lula 28 · Caiado 3 · Zema 2 · Renan 2 · Cury 2 · Grassi 1; ind. 18 · B/N 10 | Flávio 34 · Lula 29 · Marçal 2 |
| SC | SC-00517/2026 + BR-07160/2026 | 804 | Flávio 45 · Lula 20 · Renan 4 · Zema 3 · Cury 3 · Caiado 3 · Samara 1 | Flávio 45 · Lula 20 · Marçal 2 |

**Onda 2 — divulgadas 25/08 (campo 21–24/08; ±3 p.p., SP ±2):**

| UF | Registro TSE | Amostra | 1ºT sem Marçal (%) | 1ºT com Marçal (%) |
|---|---|---|---|---|
| SP | SP-06946/2026 ⚠️(ver divergência) | 1.800 | Flávio 30 · Lula 29 · Caiado 4 · Zema 3 · Renan 3 · Cury 2 · Samara 1 · Rui 1 · Grassi 1; ind. 13 · B/N 12 | Lula 30 · Flávio 30 · Marçal 4 · Caiado 3 · Renan 3 · Cury 2 |
| RJ | RJ-08748/2026 + BR-09895/2026 | 1.302 | Flávio 31 · Lula 29 · Renan 2 · Caiado 2 · Zema 2 · Cury 1 · Samara 1; ind. 16 · B/N 16 | Flávio 33 · Lula 31 · Renan 2 · Marçal 1 · Caiado 1 · Cury 1 · Zema 1 |
| MG | MG-04060/2026 (1ª fonte citou BR-09818/2026) | 1.506 | Flávio 31 · Lula 30 · Zema 7 · Caiado 3 · Renan 3 · Cury 1; ind. 17 · B/N 8 | Lula 31 · Flávio 31 · Zema 6 · Marçal 3 · Renan 3 · Caiado 2 |
| PE | PE-07828/2026 | 1.302 | Lula 54 · Flávio 19 · Caiado 3 · Renan 2 · Cury 1 · Zema 1; ind. 11 · B/N 9 | Lula 55 · Flávio 19 |
| DF | DF-06256/2026 | 1.104 | Lula 28 · Flávio 26 · Caiado 13 · Cury 3 · Zema 3 · Renan 3 · Samara 2; B/N 10 · ind. 12 | Lula 30 · Flávio 28 · Caiado 11 · Renan 3 · Cury 2 · Marçal 2 · Zema 3 |
| PB | PB-07850/2026 | 804 | Lula 50 · Flávio 21 · Caiado 3 · Renan 2 · Zema 1 · Cury 1 · Samara 1; B/N 13 · ind. 8 | Lula 55 · Flávio 22 · Cury 2 · Caiado 2 · Renan 2 · Zema 1 · Marçal 1 |
| MT | MT-04846/2026 + BR-00817/2026 | 804 | Flávio 43 · Lula 26 · Caiado 4 · Renan 3 · Zema 2 · Cury 1 · Samara 1; B/N 6 · ind. 14 | Flávio 41 · Lula 26 · Caiado 4 · Marçal 4 · Renan 2 |
| MS | MS-00793/2026 + BR-04312/2026 | 804 | Flávio 33 · Lula 27 · Caiado 5 · Renan 4 · Cury 3 · Zema 2 · Samara 2 · Clariana 1; B/N 10 · ind. 13 | Flávio 35 · Lula 27 · Marçal 5 · Caiado 4 · Renan 3 · Cury 3 |
| TO | TO-02161/2026 | 804 | Lula 37 · Flávio 32 · Caiado 7 · Renan 3 · Cury 2 · Zema 1 · Samara 1 · Grassi 1 · Clariana 1; B/N 5 · ind. 10 | Lula 39 · Flávio 32 · Caiado 7 · Marçal 4 · Renan 2 · Cury 1 |
| AM | BR-06252/2026 | 804 | (só cenário com Marçal divulgado) | Lula 38 · Flávio 35 · Marçal 2 · Renan 2 · Cury 1 · Caiado 1 · Zema 1; B/N 8 · ind. 12 |
| AP | BR-08827/2026 | 804 | Lula 36 · Flávio 33 · Renan 3 · Cury 2 · Caiado 2 · Zema 1 · Rui 1; B/N 8 · ind. 14 | Lula 36 · Flávio 32 · Renan 3 · Cury 2 · Marçal 2 · Caiado 2 |
| RO | RO-05711/2026 + BR-00490/2026 | 804 | Flávio 45 · Lula 25 · Caiado 3 · Renan 3 · Zema 2 · Cury 1 · Grassi 1 · Clariana 1 | Flávio 46 · Lula 25 · Caiado 2 · Renan 2 · Zema 2 · Marçal 2 |

- **Voto definitivo (Quaest):** SP 75% · RJ 80% · PB 82% · MT 78% · MS 70% · TO 78% · AM 80% · AP 74% · RO 79%.
- **Desaprovação do governo Lula por UF (Quaest):** MS 55 (aprova 39) · TO 44 (49) · RS 55 (38) · AP 47 (46) · AM 43 (54).
- **GO e AC estavam na pauta TSE da Quaest mas NÃO foram publicados nesta rodada** (verificado no quaest.com.br e sitemaps do G1 — esperar próximos dias).
- **Quaest NACIONAL: nenhuma na janela** (última: 14/08; série Genial/Quaest de agosto saiu 05/08).
- URLs-base: G1 25/08 resumo https://g1.globo.com/politica/eleicoes/2026/pesquisa-eleitoral/noticia/2026/08/25/quaest-veja-os-numeros-da-eleicao-para-presidente-nos-estados.ghtml + G1 estaduais (SP/RJ/MG/PE/PB/MT/MS/TO/AM/AP/RO/DF/AL/MA/PR/RN/RS/SC).

### 1.3 Real Time Big Data (recursos próprios; 95%)
- **SP** (24/08; campo 19–22/08; 2.000; ±2; BR-06537/2026): 1ºT Flávio 38 · Lula 33 · Renan 7 · Marçal 7 · Caiado 4 · Zema 3 · Cury 1; B/N 3 · ind. 3. **2ºT Flávio 49 × Lula 44.** Rejeição Lula 51 · Flávio 49. URL: https://www.poder360.com.br/poder-eleicoes/flavio-tem-49-contra-44-de-lula-no-2o-turno-em-sp-diz-pesquisa/
- **PB** (24/08; campo 19–22/08; 1.600; ±2; BR-08776/2026): 1ºT Lula 55 · Flávio 26 · Marçal 4 · Renan 3 · Caiado 3 · Zema 1. **2ºT Lula 59 × Flávio 32.** Rejeição Flávio 52 · Lula 37. URLs: https://www.cnnbrasil.com.br/eleicoes/real-time-big-data-lula-tem-55-e-flavio-26-no-1o-turno-na-paraiba/ · https://www.cnnbrasil.com.br/eleicoes/real-time-big-data-na-paraiba-lula-tem-59-no-2o-turno-flavio-32/
- **RS** (25/08; campo 20–24/08; 1.600; ±2; BR-02823/2026): 1ºT Flávio 40 · Lula 39 (empate) · Renan 7 · Marçal 5 · Caiado 2 · Zema 2 · Cury 1. **2ºT Flávio 52 × Lula 42.** Rejeição Lula 51 · Flávio 48 · Marçal 39. URLs: https://www.cnnbrasil.com.br/eleicoes/real-time-rs-flavio-lidera-2o-turno-e-empata-com-lula-no-1o/ · https://www.poder360.com.br/poder-eleicoes-2026/flavio-tem-52-contra-42-de-lula-em-eventual-2o-turno-no-rs-diz-pesquisa/

### 1.4 GERP — SP (25/08, 8h; campo 19–24/08; 1.800; ±2,3; SP-01477/2026; R$ 12.000)
- 1ºT: Flávio 38 · Lula 36 (empate técnico). **2ºT: Flávio 48 × Lula 41.** Rejeição Lula 48 · Flávio 40. Desaprovação Lula em SP 57 × 40.
- URL: https://www.poder360.com.br/poder-eleicoes-2026/flavio-tem-48-contra-41-de-lula-no-2o-turno-em-sp-diz-gerp/

### 1.5 Veritá — PA (25/08; campo 19–23/08; 1.525; ±2,5; PA-04167/2026 + BR-07588/2026; URA c/ reconhecimento de voz; iniciativa própria)
- 1ºT: **Flávio 44,6 × Lula 44,2 (empate técnico)** · Renan Santos 5,6 · demais <2; NS/NR 44. **2ºT: Flávio 50,9 × Lula 49,1 (empate técnico).**
- URL: https://opiniaoempauta.com.br/no-para-pesquisa-mostra-dr-daniel-perto-de-vencer-eleicao-no-primeiro-turno-49-x-41/

### 1.6 OPNUS/BNews — BA (24/08; campo 17–22/08; 1.200 presenciais; ±3; BA-04472/2026)
- **Espontânea:** Lula 58 · Flávio 15 · Caiado 1 · Renan 1; B/N 7 · NS/NR 18. **Estimulada:** Lula 60 · Flávio 17 · Caiado 3 · Renan 2 · Cury 1 · Marçal 1; demais 0; B/N 6 · NS/NR 8.
- Governo Lula na BA: aprova 65 × desaprova 31.
- URL: https://jornalgrandebahia.com.br/2026/08/pesquisa-opnus-bnews-na-bahia-jeronimo-tem-43-e-acm-neto-40-em-empate-tecnico-lula-alcanca-60-e-rui-costa-lidera-senado/

### 1.7 Data Control — AC (24/08; campo 17–22/08; 20 municípios; ±2,43; AC-03129/2026 + BR-00741/2026)
- Estimulada: **Flávio 49,5** · Lula 23,2 · Caiado 3,3 · Marçal 3,1 · Renan 2 · Samara 0,7 · Cury 0,6 · Zema 0,4; B/N 6,4 · NS 10.
- URL: https://ac24horas.com/2026/08/24/flavio-lidera-corrida-presidencial-no-acre-com-49-e-lula-tem-23/
- ⚠️ Pista inicial dizia "AtlasIntel Acre" — a matéria confirma **Data Control** (corrigido pela fonte).

### 1.8 Datafolha (CONTEXTO † — rodada nacional divulgada 21/08, recortes republicados 24–25/08)
- Nacional (BR-04496/2026; 2.058; 18–19/08; ±2): 1ºT Lula 39 × Flávio 33 (Caiado 5 · Renan 4 · Zema 3 · Cury 2); **2ºT Lula 47 × Flávio 43.** Aprovação Lula 47 × 50.
- Recortes: MG pres Lula 37 × Flávio 31 (Zema 10) · PE pres Lula 56 × Flávio 24 · SP 2ºT Flávio 47 × Lula 42 · DF pres Flávio 39 × Lula 31 · PI pres Lula 60 × Flávio 19.
- URLs: https://www.estadao.com.br/politica/eleicoes/pesquisa-datafolha-lula-tem-47-e-flavio-bolsonaro-soma-43-em-eventual-segundo-turno/ · https://www.poder360.com.br/poder-eleicoes-2026/lula-tem-47-e-flavio-43-em-2o-turno-diz-datafolha/

### 1.9 Média ponderada TVT News (25/08; 6 pesquisas: Datafolha, BTG/Nexus, Quaest 14/08, PoderData/Aya, Quaest 05/08, CNT/MDA)
- 1ºT: Lula 39,1 × Flávio 31,8 (Caiado 4,4 · Renan 3,9 · Zema 2,5 · Cury 1,8). 2ºT: Lula 45,1 × Flávio 41,2.
- URL: https://tvtnews.com.br/quem-esta-a-frente-nas-pesquisas-para-presidente/

### 1.10 Institutos SEM presidencial nova na janela (verificado explicitamente)
- **Paraná Pesquisas:** divulgou 25/08 baterias RJ/MT/RS/SP/GO/PR/BA — todas só Executivo Estadual + Legislativo Federal, SEM cenário presidencial (https://www.paranapesquisas.com.br/).
- **AtlasIntel:** nada na janela; pesquisa do PA estava suspensa/em análise no TSE (MP Eleitoral a favor da liberação, 22/08).
- **Futura/XP, Ipec nacional, CNT/MDA:** nada na janela. **PoderData/Indexa/Jota/Vox Brasil:** anunciadas "para esta semana" (UOL 24/08), nenhuma publicada em 24–25/08.

---

## PARTE 2 — GOVERNADOR (27 UFs)

Legenda de campo: 🔴 campo LULA · 🔵 campo FLÁVIO · ⚪ centro/independente/indefinido. (Classificação detalhada + fontes na PARTE 3.)

### Na janela 24–25/08 (21 UFs)

**SP — Quaest 25/08** (SP-06946/2026; 1.800; ±2): Tarcísio de Freitas (Republicanos) 🔵 **40** × Haddad (PT) 🔴 27. 2ºT: Tarcísio 47 × Haddad 30. · **GERP 25/08**: Tarcísio 50 × Haddad 32; 2ºT 55×36. Rejeição Haddad 48 · Tarcísio 27. Aprovação Tarcísio 60×33. · **Real Time 24/08** (SP-01347/2026): Tarcísio 52 × Haddad 35 (venceria no 1ºT); 2ºT 54×36. Senado RT: Derrite 18 · Tebet 17 · André do Prado 15 · Marina 14. · Datafolha†: Tarcísio 45.
**RJ — Quaest 25/08** (RJ-08748/2026; 1.302; ±3): Paes (PSD) 🔴 **37** · Douglas Ruas (PL) 🔵 14 · Garotinho (Republicanos) ⚪ 7 · William Siri (PSOL) 🔴 3. 2ºT: Paes 50×Ruas 20 · Paes 53×Garotinho 12. Senado: Benedita 10 · Jordy 7 · Crivella 6 · Monica Benicio 5 · Portinho 5 · Pedro Paulo 3 · Waguinho 2. · **Paraná Pesquisas 25/08** (RJ-02422/2026; 1.600; ±2,5): Paes 44,5 × Ruas 15,5 (venceria no 1ºT). Senado: Benedita 29,6 · Crivella 21 · Pedro Paulo 16,4. Gov. interino Ricardo Couto: aprovação 50,4×42,1. · Datafolha†: Paes 41 · Ruas 19 · Garotinho 9.
**MG — Quaest 25/08** (MG-04060/2026; 1.506; ±3): Cleitinho (Republicanos) 🔵 **29** · Patrus (PT) 🔴 11 · Kalil (PDT) 🔴* 10 · Simões (PSD) ⚪ 7 · Gabriel 5 · Roscoe 3. 2ºT: Cleitinho 48×Kalil 27 · 51×Patrus 26 · 49×Simões 17 · Kalil 42×Patrus 18. Senado: Marília Campos 15 · Carlos Viana 8 · Domingos Sávio 8 · Marcelo Aro 6. · Datafolha†: Cleitinho 32 · Patrus 12 · Kalil 12. (*Kalil: PDT nacional com Lula, mas FORA do palanque do PT-MG.)
**PE — Quaest 25/08** (PE-07828/2026; 1.302; ±3): Raquel Lyra (PSD) ⚪ **44** × João Campos (PSB) 🔴 36. 2ºT: Raquel 47×36. Senado: Marília Arraes 16 · Humberto Costa 13 · Mendonça 9 · Eduardo da Fonte 6 · Túlio 3. · Datafolha†: Raquel 47 × João Campos 40.
**BA — OPNUS/BNews 24/08** (BA-04472/2026; 1.200; ±3): Jerônimo (PT) 🔴 **43** × ACM Neto (União) ⚪~🔵 40 · Ronaldo Mansur (PSOL) 1 · José Estêvão (DC) 1; B/N 5 · ind. 9. 2ºT: Jerônimo 45 × Neto 44 (empate técnico); com apoiadores (Lula+Rui+Wagner): 51×39. Senado: Rui Costa (PT) 22 · Jaques Wagner (PT) 16 · João Roma (PL) 7 · Ângelo Coronel (REP) 6.
**PA — Veritá 25/08** (PA-04167/2026; 1.525; ±2,5): Dr. Daniel/Daniel Santos (Podemos) 🔵 **49,7** × Hana Ghassan (MDB) ⚪ 41,4 · Araceli (PSOL) 🔴 5,2. 2ºT: Daniel 54,4×45,6. Só 26,4% têm candidato definido. Senado: Éder Mauro (PL) 36,3 · Helder (MDB) 25 · Celso Sabino (PDT) 15,7 · Zequinha Marinho (POD) 14,7 · Chicão (União) 12,5. · ⚠️ AtlasIntel/Faciapa† 23/08 (PA-04533/2026): **Hana 48,6 × Daniel 40,5** (válidos 53,3×44,4) — DIVERGÊNCIA GRITANTE de 8 p.p. para cada lado entre institutos.
**RS — Quaest 24/08** (RS-06875/2026; 900; ±3): Zucco (PL) 🔵 **26** · Juliana Brizola (PDT) 🔴 23 · Gabriel Souza (MDB) ⚪ 9 · Maranata 2. 2ºT: Juliana 36×Zucco 33 · Juliana 32×Gabriel 24 · Zucco 33×Gabriel 22. Senado: Manuela 12 · Paulo Pimenta 9 · Van Hattem 9 · Sanderson 8 · Rigotto 8. · **Real Time 25/08** (RS-09640/2026): Juliana 38 × Zucco 32 · Gabriel Souza 19 · Maranata 4; 2ºT Juliana 45×Zucco 41. → Líder diverge por instituto.
**PR — Quaest 24/08** (PR-05388/2026; 804; ±3): Moro (PL) 🔵 **37** · Requião Filho (PDT) 🔴 21 · Sandro Alex (PSD) ⚪ 15. 2ºT: Moro 51×Requião 27 · Moro 48×Sandro 19 · Requião 37×Sandro 24. Senado: Curi 15 · Gleisi 11 · Filipe Barros 9 · Deltan 9 · Graeml 8 · Dr. Rosinha 6.
**SC — Quaest 24/08** (SC-00517/2026; 804; ±3): Jorginho Mello (PL) 🔵 **50** · João Rodrigues (PSD) ⚪ 17 · Merísio (PSB) 🔴 4 · Sodré 2. 2ºT: Jorginho 56×24 · 63×Merísio 16. Senado: Amin 19 · Carlos Bolsonaro 16 · Carol De Toni 12 · Décio Lima 9.
**DF — Quaest 25/08** (DF-06256/2026; 1.104; ±3): Celina Leão (PP) 🔵 **34** · Arruda (PSD) ⚪ 20 · Leandro Grass (PT) 🔴 13. 2ºT: Celina 42×Arruda 32 · Celina 52×Grass 24 · Arruda 44×Grass 26. Senado: Michelle Bolsonaro 25 · Leila do Vôlei 17 · Erika Kokay 12 · Bia Kicis 9. · Datafolha†: Celina 30 × Arruda 28.
**PB — Quaest 25/08** (PB-07850/2026; 804; ±3): Lucas Ribeiro (PP) ⚪ **38** · Cícero Lucena (MDB) ⚪ 19 · Efraim Filho (PL) 🔵 18 · Pedro Coutinho (DC) 2 · Camilo (PCO) 1; B/N 10 · ind. 12. Espontânea: 26×7×7. 2ºT: Ribeiro 47×Efraim 33 · Ribeiro 48×Lucena 29 · Lucena 39×Efraim 32. Senado: João Azevêdo 27 · Veneziano 17 · Nabor 9 · Queiroga 6 · Major Fábio 5. Gov. PB aprova 61×17. · **Real Time 24/08** (PB-07790/2026): Ribeiro 35 · Lucena 25 · Efraim 21; 2ºT Ribeiro 42×Lucena 35 · 46×Efraim 30. Senado: João Azevêdo 29 · Veneziano 23.
**MT — Quaest 25/08** (MT-04846/2026; 804; ±3): Wellington Fagundes (PL) 🔵 **27** · Otaviano Pivetta (Republicanos) ⚪ 23 · Dra. Natasha (PSD) ⚪ 8 · Laudicério (Agir) 2 · Milas (Missão) 2; B/N 29 · ind. 8. Senado: Mauro Mendes 24 · Janaína Riva 18 · Taques 8 · Zé Medeiros 6 · Fávaro 5. · ⚠️ **Paraná Pesquisas 24/08** (MT-02157/2026; 1.504; ±2,6): 1ºT **Pivetta 39 × Fagundes 35**; 2ºT Pivetta 44,3×Fagundes 40,8 (empate). Senado: Mauro Mendes 52,3 · Janaína 33,7. → Líder diverge por instituto.
**MS — Quaest 25/08** (MS-00793/2026; 804; ±3): Eduardo Riedel (PP) ⚪ **40** · Fábio Trad (PT) 🔴 13 · Delcídio (PRD) ⚪ 8 · Catan (Novo) 3 · Lucien (PSOL) 🔴 2. 2ºT: Riedel 54×Delcídio 23 · 59×Trad 22 · 61×Catan 13. Senado: Azambuja 22 · Cap. Contar 15 · Soraya 11 · Vander Loubet 9. Riedel aprovação 62×16; merece reeleição 66×24.
**TO — Quaest 25/08** (TO-02161/2026; 804; ±3): Prof. Dorinha (União) ⚪ **37** · Vicentinho (PSDB) ⚪ 28 · Laurez (PSD) ⚪ 7 · Ataídes (Novo) 3. Senado: Eduardo Gomes 14 · Gaguim 13 · Paulo Mourão 9 · Alexandre Guimarães 8 · Dimas 6 · Vanderlei Luxemburgo 5.
**AM — Quaest 25/08** (BR-06252/2026 p/ pres; 804; ±3): Omar Aziz (PSD) 🔴 **26** · Roberto Cidade (União) ⚪ 18 · Maria do Carmo (PL) 🔵 16 · David Almeida (Avante) ⚪ 15 · Daciolo 2 · Isael Munduruku 1. Senado: Eduardo Braga 25 · Cap. Alberto Neto 16 · Plínio Valério 13 · Wilson Lima 12.
**AP — Quaest 25/08** (AP-09438/2026; 804; ±3): Dr. Furlan (PSD) ⚪ **55** × Clécio (União) ⚪ 35 · Jairo Palheta 1. Senado: Rayssa Furlan 27 · Randolfe 19 · Lucas Barreto 18 · Alliny 9 · Favacho 7 · Capiberibe 4. Clécio aprovação 53×37.
**RO — Quaest 25/08** (RO-05711/2026; 804; ±3): Marcos Rogério (PL) 🔵 **24** · Adailton Fúria (PSD) ⚪ 21 · Expedito Netto (PT) 🔴 10 · Hildon Chaves (União) ⚪ 10; ind. 22. 2ºT: Rogério 40×Fúria 29 · 49×Expedito 23 · 47×Hildon 20 · Fúria 41×Expedito 18. Senado: Dr. Fernando Máximo 17 · Sílvia Cristina 11 · Bruno Bolsonaro Sheid 11 · Mariana Carvalho 10 · Gurgacz 5.
**RN — Quaest 24/08** (RN-00876/2026; 804; ±3): Allyson Bezerra (União) ⚪ **25** · Cadu de Lula/Carlos Eduardo (PT) 🔴 21 · Álvaro Dias (PL) 🔵 19 · Rodrigo Bolsonaro (Agir) 2 · Roberio (PSOL) 2; ind. 16 · B/N 14. 2ºT: Allyson 35×Cadu 34 · Allyson 35×Álvaro 30 · Cadu 36×Álvaro 31. Senado: Styvenson 16 · Zenaide 10 · Samanda 8 · Rafael Motta 8 · Cel. Hélio 5.
**MA — Quaest 24/08** (MA-02558/26; 900; ±3): Eduardo Braide (PSD) ⚪ **44** · Orleans Brandão (MDB) ⚪ 25 · Felipe Camarão (PT) 🔴 6 · Roberto Rocha 3. Senado: Roseana 16 · Weverton 11 · Lahesio 10 · Fufuca 9 · Eliziane 9 · Hilton 5. Brandão aprovação 54×30.
**AL — Quaest 24/08** (AL-05503/2026; 804; ±3): Renan Filho (MDB) 🔴 **42** × JHC (PSDB) ⚪ 40. 2ºT: empate 42×42. Senado: Arthur Lira 20 · Renan Calheiros 18 · Marina JHC 15 · Davino Filho 10.
**ES — Instituto Perfil ~25/08** (ES-07093/2026; campo/amostra/margem não informados na matéria): Lorenzo Pazolini (Republicanos) ⚪ **29,33** · Ricardo Ferraço (MDB) ⚪ 22,33 · Helder Salomão (PT) 🔴 7,67. URL: https://eshoje.com.br/politica/bastidores-da-politica/2026/08/eleicao-para-governador-no-es-pesquisa/

### Fora da janela estrita († contexto — 6 UFs sem pesquisa em 24–25/08)

**PI† — Datafolha 22/08** (PI-06656/2026; 826; 18–21/08; ±3; TV Clube): Rafael Fonteles (PT) 🔴 **56** × Joel Rodrigues (PP) ⚪ 21 · Dra. Lúcia (PSDB) 2 · Geraldo (PSTU) 2. Aprovação Fonteles 72. URLs: https://g1.globo.com/pi/piaui/eleicoes/2026/noticia/2026/08/22/datafolha-no-pi.ghtml
**CE† — Datafolha 13/08** (CE-04292/2026; 1.022; ±3): Ciro Gomes (PSDB) ⚪~🔵 **52** × Elmano (PT) 🔴 33; 2ºT Ciro 55×37. · **Real Time 20/08** (CE-08223/2026; 1.600; ±2): **EMPATE Elmano 44 × Ciro 44**; 2ºT Elmano 46×45. Senado: Cid (PSB) 27 · Cap. Wagner (União) 21 · Luizianne (Rede) 21. · Ipsos-Ipec 21/08: Ciro 43×35. → Institutos divergem forte. URLs: https://g1.globo.com/ce/ceara/eleicoes/2026/noticia/2026/08/13/datafolha-no-ceara-ciro-tem-52percent-contra-33percent-de-elmano.ghtml · https://www.gazetadopovo.com.br/eleicoes/2026/pesquisa-eleitoral-2026/real-time-big-data-governador-senador-ceara-agosto-2026/
**GO† — Paraná Pesquisas 18/08** (GO-01791/2026; 1.240; 14–17/08; ±2,8): Daniel Vilela (MDB) ⚪ **45,8** × Marconi Perillo (PSDB) ⚪ 24,9 · Wilder Morais (PL) 🔵 13,2 · Luis Cesar Bueno (PT) 🔴 2,3. URL: https://www.gazetadopovo.com.br/eleicoes/2026/pesquisa-eleitoral-2026/parana-pesquisas-governador-senador-goias-agosto-2026/ (⚠️ Paraná Pesquisas divulgou bateria GO em 25/08, mas só Legislativo — sem governo.)
**SE† — INOR 21/08** (reg. 04930/2026; 1.070; 13–16/08; ±3): Valmir de Francisquinho (Republicanos) ⚪ **46,73** × Fábio Mitidieri (PSD) ⚪ 31,59 · Ricardo Marques 7,76. URL: https://www.nenoticias.com.br/pesquisa-eleitoral-governador-sergipe-inor-2026/
**AC† — AtlasIntel/ac24horas 03/08** (AC-07815/2026; 997; 28/07–02/08; ±3): Mailza Assis (PP) ⚪ **35,2** × Alan Rick (Republicanos) ⚪ 33,1 · Tião Bocalom 18,5 · Thor Dantas 9,7. 2ºT: Mailza 44,5×42,2. URL: https://portalacre.com.br/2026/08/mailza-assis-lidera-com-35-em-nova-pesquisa-ao-governo-do-estado/
**RR† — nada desde abril** (Veritá 29/03–04/04; 1.030): Arthur Henrique (PL) 🔵 42,6 × Edilson Damião (Republicanos) ⚪ 22,5. URL: https://pt.wikipedia.org/wiki/Pesquisas_eleitorais_para_a_eleição_estadual_de_2026_em_Roraima

---

## PARTE 3 — CLASSIFICAÇÃO DE CAMPO (com fontes de alinhamento)

### 🔴 CAMPO LULA (apoio explícito com fonte)
- **Haddad (PT-SP), Patrus (PT-MG), João Campos (PSB-PE), Grass (PT-DF), Trad (PT-MS), Expedito Netto (PT-RO), Cadu de Lula (PT-RN), Felipe Camarão (PT-MA), Jerônimo (PT-BA), Elmano (PT-CE), Fonteles (PT-PI)** — partidos do palanque lulista; Elmano "com apoio de Lula": https://g1.globo.com/ce/ceara/eleicoes/2026/noticia/2026/08/22/como-racha-de-aliados-levou-ciro-e-elmano-a-lados-opostos-na-disputa-pelo-governo-do-ceara.ghtml
- **Eduardo Paes (PSD-RJ):** "compromisso é com Lula" — https://valor.globo.com/politica/eleicoes-2026/noticia/2026/08/20/paes-diz-que-nao-fara-campanha-com-caiado-no-rio-e-que-tem-compromisso-com-lula.ghtml
- **Omar Aziz (PSD-AM):** PT oficializou apoio — https://g1.globo.com/am/amazonas/eleicoes/2026/noticia/2026/08/01/pt-oficializa-apoio-a-candidatura-de-omar-aziz-ao-governo-do-amazonas.ghtml
- **Juliana Brizola (PDT-RS):** PDT 1º partido a cravar apoio a Lula — https://www.gazetadopovo.com.br/eleicoes/2026/pdt-e-o-primeiro-partido-a-cravar-apoio-a-reeleicao-de-lula/
- **Renan Filho (MDB-AL):** Lula declarou apoio — jornaldealagoas.com.br/eleicoes/2026/08/20/1325
- **Requião Filho (PDT-PR)** — pelo partido (PDT nacional com Lula).
- **Kalil (PDT-MG):** PDT nacional com Lula, MAS Kalil fora do palanque do PT-MG — https://www.otempo.com.br/eleicoes/2026/governadores/2026/7/27/pdt-minas-confirma-acordo-nacional-de-apoio-a-lula-mas-diz-que-kalil-ficara-fora-do-palanque-do-pt
- **Só pelo partido:** William Siri (PSOL-RJ), Araceli (PSOL-PA), Merísio (PSB-SC), Helder Salomão (PT-ES), Luis Cesar Bueno (PT-GO), Lucien (PSOL-MS), Roberio (PSOL-RN).

### 🔵 CAMPO FLÁVIO (apoio explícito com fonte)
- **Tarcísio (REP-SP):** https://correiobraziliense.com.br/politica/2026/08/7483018-tarcisio-apoia-flavio-bolsonaro-nossa-vida-aqui-vai-ser-mais-facil.html
- **Cleitinho (REP-MG):** "quem votar em mim tem que votar no Flávio" (G1/em.com 17/08).
- **Jorginho Mello (PL-SC):** https://correiobraziliense.com.br/politica/2026/05/7422242-governador-de-santa-catarina-reafirma-apoio-a-flavio-bolsonaro.html
- **Moro (PL-PR):** https://gazetadopovo.com.br/eleicoes/2026/flavio-bolsonaro-moro-fecham-apoio-eleicoes/
- **Zucco (PL-RS):** lançado por Flávio — https://g1.globo.com/rs/rio-grande-do-sul/eleicoes/2026/noticia/2026/04/11/pre-candidatura-zucco-pl-governo-rs.ghtml
- **Wellington Fagundes (PL-MT):** https://g1.globo.com/mt/mato-grosso/noticia/2026/02/25/flavio-bolsonaro-confirma-wellington-fagundes-como-pre-candidato-ao-governo-de-mato-grosso.ghtml
- **Marcos Rogério (PL-RO):** https://www.rondoniadinamica.com/noticias/2026/07/flavio-bolsonaro-destaca-marcos-rogerio-e-defende-parceria-com-rondonia,248793.shtml
- **Dr. Daniel (Podemos-PA):** lançado por Flávio — https://www.cnnbrasil.com.br/eleicoes/podemos-oficializa-candidatura-de-dr-daniel-ao-governo-do-para/
- **Celina Leão (PP-DF):** https://www.gazetadopovo.com.br/eleicoes/2026/celina-leao-reforca-apoio-a-flavio-e-michelle-bolsonaro-apos-atrito/
- **Douglas Ruas (PL-RJ):** "candidato de Flávio no Rio" — https://noticias.uol.com.br/eleicoes/2026/07/23/garotinho-na-urna-enfraquece-ainda-mais-ruas-candidato-de-flavio-no-rio.htm
- **Só pelo partido (PL, sem checagem individual):** Efraim Filho (PB), Álvaro Dias (RN), Maria do Carmo (AM), Roscoe (MG), Arthur Henrique (RR).
- **Ciro Gomes (PSDB-CE):** sem declaração de voto; aliado localmente ao PL/Federação União Progressista (G1 22/08) → arranjo de campo Flávio no estado.

### ⚪ CENTRO / INDEPENDENTE / INDEFINIDO
- **Raquel Lyra (PSD-PE):** neutralidade formal, gestos a Lula, descartou Caiado — https://jc.uol.com.br/politica/2026/08/20/raquel-lyra-evita-revelar-voto-para-presidente-mas-destaca-entregas-junto-ao-governo-lula-sou-grata.html
- **ACM Neto (União-BA):** sinalizou fim da neutralidade com viés Flávio, sem apoio formal — https://www.metro1.com.br/noticias/politica/176306
- **Eduardo Braide (PSD-MA):** "nem esquerda nem direita"; chapa com viés bolsonarista, neutralidade oficial — O Globo 10/07.
- **Garotinho (REP-RJ):** "candidatura sem apoio presidencial definido" — https://www.poder360.com.br/poder-eleicoes-2026/republicanos-oficializa-candidatura-de-garotinho-ao-governo-do-rio/
- **Só pelo partido (centrão):** Simões (PSD-MG), Arruda (PSD-DF), Lucas Ribeiro (PP-PB), Lucena (MDB-PB), Pivetta (REP-MT), Natasha (PSD-MT), Riedel (PP-MS), Delcídio (PRD-MS), Dorinha (União-TO), Vicentinho (PSDB-TO), Laurez (PSD-TO), Roberto Cidade (União-AM), David Almeida (Avante-AM), Furlan (PSD-AP), Clécio (União-AP), Fúria (PSD-RO), Hildon (União-RO), Sandro Alex (PSD-PR), Allyson (União-RN), João Rodrigues (PSD-SC), Gabriel Souza (MDB-RS), Brandão (MDB-MA), JHC (PSDB-AL), Hana (MDB-PA), Joel Rodrigues (PP-PI), Vilela (MDB-GO), Perillo (PSDB-GO), Francisquinho (REP-SE), Mitidieri (PSD-SE), Mailza (PP-AC), Alan Rick (REP-AC), Damião (REP-RR), Pazolini (REP-ES), Ferraço (MDB-ES).

---

## PARTE 4 — DIVERGÊNCIAS E LACUNAS REGISTRADAS

1. **Quaest SP — registro TSE:** BR-02096/2026 (matéria G1-SP) × SP-06946/2026 (resumo G1 + Poder360). Citados os dois.
2. **Quaest RS — enquadramento:** Poder360 titula "empate"; G1 mostra Flávio 34×28 à frente. Números idênticos.
3. **PA — institutos em guerra:** Veritá 25/08 dá Dr. Daniel 49,7×41,4 (quase 1º turno); AtlasIntel 23/08 dá Hana 48,6×40,5. Divergência de ~8 p.p. para lados opostos.
4. **MT — líder diverge:** Quaest Fagundes 27×23; Paraná Pesquisas Pivetta 39×35.
5. **RS — líder diverge:** Quaest Zucco 26×23; Real Time Juliana 38×32.
6. **CE — institutos divergem forte:** Datafolha 13/08 Ciro 52×33; Real Time 20/08 empate 44×44; Ipec 21/08 Ciro 43×35.
7. **Acre presidente:** pista inicial "AtlasIntel" → matéria confirma **Data Control**.
8. **BTG/Nexus espontânea:** não saiu nas matérias (PDF atrás de formulário) — obtida depois via PDF íntegra no Poder360.
9. **Lacunas:** Quaest GO e AC na pauta TSE mas não publicadas; ES sem ficha metodológica na matéria (Instituto Perfil); RR sem nada desde abril; PoderData/Indexa/Jota/Vox prometidas para a semana.
10. **Bloqueios técnicos:** UOL (Akamai 403), TSE PesqEle (403), SCC10 (Cloudflare), BNews (anti-bot) — contornados via fontes espelho.

---

## ESTADO DA MISSÃO
- **O que aconteceu:** compiladas TODAS as pesquisas divulgadas em 24–25/08/2026 (9 institutos, 21 UFs com governador + nacional), com campo Lula×Flávio classificado e sourced. Tema Duplo gravado; monitor atualizado.
- **O que falta:** Quaest GO/AC (na pauta, não publicadas); PoderData/Indexa/Jota/Vox (prometidas p/ a semana); espontâneas estaduais Quaest (não divulgadas nas matérias); ficha completa do Instituto Perfil (ES).
- **Do Miguel:** nada. Se quiser, próxima ronda pode: (a) transformar em matéria/bloco para o site; (b) monitorar diariamente as novas pesquisas até 04/10.

🕐 25/08/2026 23:22 · ZCode/Qwen 3.8 (coleta) + ZCode/Kimi K3 (consolidação)
