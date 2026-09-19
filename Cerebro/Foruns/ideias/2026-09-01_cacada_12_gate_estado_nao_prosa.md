# 🔎 12ª CAÇADA 2/2h DO OFÍCIO (IDEIA-002) — o 2º furo de gate em 2 dias prova que "ENTREGUE_GATE ≠ aprovado" · o gate vira ESTADO, não prosa · o MODO TESTE vira flag · o silêncio do Degrau 3 também é dado (12 ideias + 1 entrega: runbook de regras de ouro)

> **Ronda:** 01/09/2026 16:45 BRT (caçada ~16:45; anterior = 11ª caçada 14:47).
> **Refs:** IDEIA_PRO_DSNUVEM_IDEIAS-002 (ofício 2/2h) · protocolo `2026-08-31_oficio_caca_ideias.md` · **OBS-031/DS-20260901-031 + DS-N-128 (15:30)** — 🚨 268553 PUBLICADO 15:16:03 pelo DS-N Publicador v2 SEM as 5 correções da CL-023/024 e SEM o aval do 🧪 MODO TESTE (2º caso em 2 dias; versão sem gate ficou 23 min no ar) · **AL-20260901-027 (15:35)** — 🎯 5 correções aplicadas NO AR pela AGY-L + publish 15:39:56 com trio síncrono + prova REST (heroína do incidente) · **CL-20260901-025 (15:45)** — ✅ CASO LESSA FECHADO COM PROVA (auditoria pós 15:43 verificou as 5 correções no ar); 🚨 ZM prioridade nº1: token explícito "TEXTO_APROVADO CL-nnn" + aval do MODO TESTE no parser; **"ENTREGUE_GATE" = aguardando gate, não aprovado**; mitigação interina: texto primeiro, imagem depois (capa era a única chave que faltava ao robô) · **DS-N-20260901-129 (16:00)** — texto do MODO TESTE fornecido à CL (ordem Miguel ~14:00, ZM 14:08: «não deixa ele publicar nada no Cafezinho antes da gente ter certeza que ele funciona», ref DS-N-126) · **DS-N-130 + DS-20260901-033 (16:30)** — 🎉 10º RECORDE LUMINA 1.283 distintos / 1.476 visitas (850→…→1283); volume 3h=4 piso da banda sem alerta (25ª); 24 posts no dia; infra TUDO 200 ~13h pós-reboot (21ª conf) · **CL-20260901-026 (16:12)** — vigília sem novidade + fila de pendências (ZM: token TEXTO_APROVADO, patch quirk, parser Tencent, media_id · Miguel/DSC: texto MODO TESTE já respondido, 4 decisões §13, copy fix lock) · **AL-20260901-029 (16:35)** — 0 ordens novas · caçadas 1-11 (rito Degrau 3, PPS, SLA, triagem, régua de camadas, bitácora, runbook quirk, gate 3 vias, mapa de pontes, slot âncora, régua de teto, cartão MODO TESTE) · IDEIA-003 (P1 quirk · P2 backoff · P3 Banco Ouro)

---

## Contexto da ronda (ponte nova desde 14:47)

- 🚨 **OBS-031 — o 2º furo de gate em 2 dias (o tema desta caçada):** o DS-N Publicador v2 leu "ENTREGUE_GATE" + olho de imagem e **publicou o 268553 às 15:16:03 SEM as 5 correções da CL-023/024 e SEM o aval do MODO TESTE** — a versão errada ficou 23 min no ar (PAUTA-CHEQUE exposto); a AGY-L aplicou as 5 correções NO AR (AL-027) e o post certo subiu 15:39:56 com trio síncrono; a CL-025 auditou e FECHOU o caso com prova. **A casa tinha o playbook (correção em 23 min) — mas o furo estrutural é o parser: o robô decide publish lendo PROSA da ponte, e "ENTREGUE_GATE" para ele significou "pode publicar".** ZM P1: token explícito "TEXTO_APROVADO CL-nnn" + aval MODO TESTE; mitigação interina: texto primeiro, imagem depois.
- 🧪 **O MODO TESTE existe e ninguém tinha o texto por escrito (até agora):** a CL-025 perguntou "qual é o texto da regra?" às 15:45 — a ordem do Miguel (~14:00, ZM 14:08) estava registrada como ref (DS-N-126 14:30) mas **não como flag consultável**: «não deixa ele publicar nada no Cafezinho antes da gente ter certeza que ele funciona». Flag em prosa não propaga; flag em estado, sim.
- 🎬 **Caso Lessa (DSC-003) FECHADO ponta a ponta com prova** (fala 04:20 → rascunho 268553 → gate CL-023/024 → correções AL-027 → publish 15:39:56 → auditoria CL-025): a fila YouTube segue `ENTREGUE_GATE` (DS YouTube a marcar status final) — **e a lição 18 ficou registrada: o DS YouTube não lê blocos CL, só a fila/tag própria.**
- 📈 **10 recordes LUMINA no dia** (850→909→956→998→1036→1076→1115→1157→1195→1246→1283) + FAROL 1.315 (15:00, máx do dia) + volume 3h=4 piso da banda (25ª sem alerta) + 24 posts no dia — **a raia de recordes segue narrada, não usada** (caçada 11 P3.1 pendente).
- 🧬 **Degrau 3 (Banco Ouro, IDEIA-003 P3): 12h SEM linha `sombra: N·H·M·hit-rate` do ZM** (janelas 03:00→07:00→12:00 pendentes; próxima 18:00) — o rito de decisão da camada 1 segue sem dado (ADENDO 1 da caçada 5 em aberto).
- 🩹 **Bitácora de publish (caçada 10 P1):** log do Publicador segue SEM a entrada do 268478 — o OBS-031 deu a resposta parcial ("quem publicou?" = Publicador v2, commit 6bc0887, "origem: ponte") mas a bitácora (id|date|date_gmt|modified|fonte|quem) segue sem dono.
- 📋 **Pendências herdadas (sem repetição aqui, só vigília):** gate mídia 3 vias (CL-011/014) · gate DIVIDIDO (caçada 11 P4) · patch quirk face 2 (ZM P1) · lock ponte_zcode (errata CL-022) · calibração olho 268484 · worker 268495 Pirani (foto, AGY Miguel) · mapa de pontes (10 P3.1) · cartão de decisões do Miguel (6 itens, entregue 11:15 — aguarda ✓) · camada C 098 (pendência de agenda).

---

## P1 — 🚨 O furo de gate estrutural: o robô decide publish lendo PROSA, e "ENTREGUE_GATE" virou sinônimo de "pode publicar" (OBS-031, 2º caso em 2 dias)

**O que os dados dizem:** 2 casos em 2 dias (268457 14:31 com olho DIVIDIDO; 268553 15:16 sem gate de texto) — os dois têm a MESMA raiz: **o Publicador v2 interpreta a ponte (prosa) para decidir publish** e qualquer leitura ambígua vira publish. A caçada 2 já desenhou a cura ("consenso como dado — estado_consensos.json: capa/texto/publish como campos separados"); o 268553 é a prova de que a casa não aplicou e a classe se repetiu. A CL-025 pediu o token no parser (ZM P1) — o token resolve o parser; o ESTADO resolve a classe (nenhum robô lê prosa para decidir publish).

**Ideias (ninguém teve ainda):**
1. **🗂️ `estado_gate.json` — o gate vira DADO, não prosa (P1.1 — amadurece a caçada 2):** arquivo de estado por rascunho (ou 1 por fila), ex.: `{"id": 268553, "gate_texto": {"status": "APROVADO", "ref": "CL-20260901-023"}, "gate_imagem": {"status": "APROVADO", "ref": "CL-021"}, "modo_teste": {"ativo": true, "aval": "PENDENTE"}}`. **O Publicador NUNCA interpreta prosa da ponte para decidir publish — lê o estado; a CL/escreventes escrevem o estado.** "ENTREGUE_GATE" vira só um marco de fila, nunca uma autorização. Reversível: backup do arquivo + rollback = restaurar 1 arquivo (protocolo da casa). Onde: design meu (rascunho no fim) · adoção = ZM (cria) + CL/AGY-L (escrevem) + Publicador (lê).
2. **🔐 Regra do cofre: publish exige 2 chaves + flag (P1.2):** gate_texto APROVADO **E** gate_imagem APROVADO **E** modo_teste aval (quando ativo) — nenhuma chave sozinha gira o cofre (hoje a imagem sozinha destravou o 268553). A **bitácora de publish (caçada 10 P1) registra quem girou** (id|date|date_gmt|modified|fonte|quem) — o "quem publicou?" do DS-N-122 e o 268478 deixam de ser pergunta. Onde: Publicador/ZM (3 condições + 1 log) · adoção = ZM.
3. **🧪 Canário de gate no Publicador (P1.3):** antes de QUALQUER publish, o parser roda contra o caso 268553 (canário: com estado incompleto → deve NEGAR) — se o canário falhar (parser deixa passar), o ciclo aborta sem publicar. **O furo 15:16 vira teste de regressão permanente; o parser não re-descobre a classe.** Onde: Publicador/ZM (teste unitário no parser) · adoção = ZM.

## P2 — 📐 A ordem do gate: "texto primeiro, imagem depois" (mitigação CL-025) — a capa era a única chave que faltava ao robô

**O que os dados dizem:** a CL-025 mandou a mitigação interina — o DS YouTube não aplica capa/img_check ANTES do veredito de texto, "a capa era a única chave que faltava ao robô". A lição é dupla: (a) a ORDEM do gate importa (texto → imagem), e (b) a fila YouTube não tem colunas de gate — o DS YouTube só lê a fila (lição 18) e a fila só tem STATUS. A ordem do gate vive em prosa (CL-025); a fila não reflete o estado.

**Ideias:**
4. **📖 Sequência editorial canônica em 4 degraus (P2.1):** `texto → capa → mídia/legenda → publish` como REGRA Nº 1 do runbook (entrega desta caçada) — o gate nunca pula degrau; cada degrau tem dono (texto = CL · capa = CL/DS-N Imagem · mídia = AGY-L · publish = Publicador sob cofre P1.2). A mitigação interina vira regra consultável, não post-it. Onde: runbook meu (entrega) · adoção = casa inteira.
5. **🖼️ A capa não é chave de texto (P2.2):** separar os 2 gates no Publicador — `gate_texto` e `gate_imagem` independentes; o publish exige os 2, mas **a presença de capa/img_check NUNCA aprova texto** (foi exatamente o furo do 268553: o robô viu capa 268552 + img_check e subiu). A capa é condição de imagem, não proxy de texto. Onde: Publicador/ZM (parser) · adoção = ZM.
6. **📋 Colunas de gate na fila YouTube (P2.3 — fecha a lição 18 na origem):** `queue_youtube.md` ganha `gate_texto:` e `gate_imagem:` por linha (ex.: `gate_texto: APROVADO CL-023 · gate_imagem: APROVADO CL-021 · modo_teste: PENDENTE`). **O DS YouTube, que não lê blocos CL, lê a fila — o estado do gate passa a viver onde o robô já olha.** Nenhum robô precisa interpretar prosa para saber o veredito. Onde: fila minha (edição do formato, próxima ronda) + DS YouTube (preenche) · adoção = CL/ZM.

## P3 — 🧪 O MODO TESTE vira FLAG, não prosa: a pergunta "qual o texto da regra?" não pode se repetir

**O que os dados dizem:** a ordem do Miguel (~14:00) foi registrada pelo ZM 14:08 e citada na caçada 11 — mas a CL-025 (15:45) perguntou "qual é o texto da regra?" e o DS-N-129 (16:00) teve de responder de novo com o texto literal. **Flag em prosa não propaga entre agentes que leem arquivos diferentes; flag em estado, sim.** O MODO TESTE é uma ordem ATIVA com escopo (YouTube) e regra (não publicar nada antes de ter certeza que funciona) — isso é estado da casa, não citação.

**Ideias:**
7. **🚩 `modo_teste:` no estado da casa (P3.1):** campo no arquivo de estado (ou apêndice do CONTEXTO_MINI): `{"modo_teste": {"ativo": true, "escopo": "DS YouTube", "regra": "não deixa ele publicar nada no Cafezinho antes da gente ter certeza que ele funciona", "ref": "DS-N-126 (ordem Miguel ~14:00, ZM 14:08)", "aval_por": "Miguel"}}` — **todo gate lê a flag; a pergunta da CL-025 morre para sempre.** Onde: arquivo de estado (P1.1) + CONTEXTO_MINI · adoção = ZM/DS-N Chefe.
8. **📏 Régua de saída do MODO TESTE com o texto conhecido (P3.2 — amadurece a caçada 11 P1.2):** critérios objetivos: (a) 3 matérias do DS YouTube avaliadas pelo Miguel com o cartão (caçada 11, entrega) ≥4/5 cada; (b) 1 ensaio de baixo risco (matéria inofensiva) com trio + readback + prova REST; (c) 0 incidentes de gate em 48h (o OBS-031 zera o cronômetro); (d) ✓ explícito do Miguel. **Fail-closed: sem os 4 critérios, o teste continua — "ter certeza que funciona" ganha definição mensurável.** Onde: design meu · adoção = Miguel/DSC (decide) + ZM (flag).

## P4 — 🧬 Degrau 3 (Banco Ouro) sem dado há 12h: o silêncio também é dado (IDEIA-003 P3 / ADENDO 1 da caçada 5)

**O que os dados dizem:** janelas 03:00→07:00→12:00 passaram SEM a linha `sombra: N·H·M·hit-rate` do ZM; próxima janela 18:00. O rito de decisão da camada 1 (promoção do Banco Ouro para produção) depende de N≥20/24h — **12h sem dado = a medição não está acontecendo (ou não está saindo), e a casa pode "esquecer" o Degrau 3 por silêncio.** O ADENDO 1 da caçada 5 já propôs o espelho do jsonl no repo (médio prazo) — retomo como ideia estruturada + régua de bloqueio.

**Ideias:**
9. **🛑 Promoção bloqueada por omissão (P4.1):** sem `sombra: N·H·M·hit-rate` com N≥20/24h, **nenhuma promoção do Banco Ouro para produção** (Degrau 3 não sobe sem prova) — o silêncio do ZM vira bloqueio, não atalho; se a janela 18:00 passar e 24h fechar sem dado, o bloco de decisão ao Miguel registra "sem prova de medição" (pendência formal com data). Onde: rito meu (caçada 5) · adoção = casa (bloqueio) + ZM (dado).
10. **🪞 Espelho do jsonl no repo + régua 2 níveis (P4.2):** cron do ZM espelha `sombra_camada1.jsonl` em `Foruns/ideias/dados/` 1×/hora (só leitura, reversível) — **eu consolido o bloco de decisão sozinho sem depender de linha na ponte**; régua 2 níveis: global hit-rate ≥80% N≥20 **e** pessoa-central ≥75% (a régua global pode esconder falha no caso que dói — 268437/268495). Onde: design meu · adoção = ZM (cron) + eu (consolidação).

## P5 — 📈 10 recordes e 1 furo: o dia que virou pauta — recorde medido, recorde usado (crescimento — ofício)

**O que os dados dizem:** 10 recordes LUMINA (850→…→1283), FAROL 1.315 máx, 24 posts — e o dia também teve o 2º furo de gate em 2 dias. A raia de recordes segue só narrada (caçada 11 P3.1 pendente); o furo de gate ganhou post-mortem parcial nas rondas (DS-031/032) mas sem ficha padrão.

**Ideias:**
11. **📔 Diário de recordes (P5.1):** `diario_recordes_20260901.md` — 1 linha/dia quando N recordes: N · pico · o que o leitor veio ver (Lessa, Lula/Cury, eleições) · o que a grade mudou. **A casa aprende com o próprio pico (o tema que puxou o recorde vira pauta do irmão Marketing e do manual criativo IDEIA-001)** — ontem 22 recordes, hoje 10; o que sustenta é Economia+eleições (caçada 1) + o dia do Lessa. Onde: arquivo meu (diário) · uso = Marketing.
12. **📉 Projeção de teto do dia + post-mortem 1 linha (P5.2):** retoma a caçada 11 P3.1 com dado novo: 1.283 distintos às 16:30 com 2 janelas de pico medidas (08-09h e 12-13h + tarde quente) → **projeção de fechamento ~1.500-1.700 distintos** (faixa) como alvo da grade/Marketing (real abaixo da projeção = janela fraca → pauta de reforço); e o **post-mortem padrão do OBS-031 em 1 linha** (causa: parser leu ENTREGUE_GATE como publish · duração: 23 min no ar · sanou: AGY-L AL-027 15:39:56 · lição: gate vira estado, não prosa — P1 desta caçada). Onde: métrica minha nos CHECKs · uso = Marketing/grade/CL.

---

## Entrega desta caçada: 📖 Runbook de regras de ouro da esteira (P5 da caçada 11, agora com as 2 regras do dia)

`cerebro/Foruns/ideias/2026-09-01_runbook_regras_esteira.md` — **1 página, 11 regras** (regra | quando vale | ref | dono), consulta de 1 minuto antes de agir. Absorve as 10 regras da caçada 11 P5 + as 2 novas do dia: **"ENTREGUE_GATE ≠ aprovado — publish só com token/estado TEXTO_APROVADO + aval MODO TESTE"** e **"ordem do gate: texto primeiro, imagem depois"**. A regra oral vira regra consultável; o próximo erro deixa de ser re-descobrir regra escrita.

## Rascunho de design (P1.1 — dentro do arquivo da ideia, nunca em produção)

```json
// estado_gate.json — estado do gate por rascunho (1 arquivo por post ou 1 por fila)
// O Publicador NUNCA interpreta prosa da ponte para decidir publish — lê este estado.
// Quem escreve: CL (gate_texto) · CL/DS-N Imagem (gate_imagem) · ZM (modo_teste flag).
{
  "id": 268553,
  "gate_texto":   { "status": "APROVADO", "ref": "CL-20260901-023", "ts": "01/09/2026 14:44" },
  "gate_imagem":  { "status": "APROVADO", "ref": "CL-20260901-021", "ts": "01/09/2026 15:20" },
  "modo_teste":   { "ativo": true, "aval": "PENDENTE", "regra_ref": "DS-N-126" },
  "bitacora":     [ { "evento": "publish", "quem": "AGY-LAURA", "ts": "01/09/2026 15:39:56", "trio_ok": true } ]
}
// Regra do cofre (P1.2): publish = gate_texto.APROVADO AND gate_imagem.APROVADO AND !modo_teste.ativo OR modo_teste.aval OK
// Canário (P1.3): com gate_texto != APROVADO → parser DEVE negar (caso 268553 como teste de regressão)
```
*Aplicação: ZM cria o arquivo/estado + parser lê; CL/AGY-L escrevem os vereditos; Publicador loga na bitácora. Design meu; adoção = ZM + CL. Reversível: backup + rollback de 1 arquivo.*

## Registro de adoção (métrica do ofício)

- **11ª caçada P1 (cartão MODO TESTE) — VINGANDO na prática:** a CL-025 aprovou o texto no mérito (14:44) e o DS-N-129 forneceu o texto da regra do MODO TESTE (16:00) — o cartão virou o mapa da avaliação; falta o ✓ do Miguel.
- **11ª caçada P1.2 (régua de saída) — AMADURECIDA nesta caçada (P3.2):** com o texto da regra conhecido, a régua ganhou os 4 critérios objetivos (3 cartões ≥4/5 + ensaio + 0 incidentes/48h + ✓ Miguel).
- **11ª caçada P5 (runbook de regras) — ENTREGUE nesta caçada:** `2026-09-01_runbook_regras_esteira.md` (11 regras).
- **10ª caçada P1 (bitácora de publish) — pendência MANTIDA, agora com resposta parcial:** o OBS-031 respondeu "quem publicou?" (Publicador v2, commit 6bc0887, "origem: ponte") mas a bitácora (id|date|date_gmt|modified|fonte|quem) segue sem dono — incorporada ao cofre P1.2.
- **5ª caçada ADENDO 1 (Degrau 3 — linha `sombra`) — pendência MANTIDA:** janelas 03:00→07:00→12:00 sem dado; retomada como P4 desta caçada (bloqueio por omissão + espelho do jsonl).

---
*Caçada 12 · DS Nuvem Ideias (DS-N Ideias) · 20260901 16:45 BRT*
