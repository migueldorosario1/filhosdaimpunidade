# 7ª caçada 2/2h do ofício — a retomada revelou o quirk vivo; a fila do YouTube pediu SLA

> **Autor:** DS Nuvem Ideias (DS-N Ideias) · **Ronda:** 06:43–06:47 BRT (01/09/2026)
> **Refs:** IDEIA_PRO_DSNUVEM_IDEIAS-002 (ofício 2/2h) · protocolo `2026-08-31_oficio_caca_ideias.md` · **CL-20260901-007 (06:12)** — 🚨 quirk P1 face 2 URGENTE: 5 casos/24h (268451/268458 hoje; 268366/268393 ontem + 1º da série); "a Ideia-003 P1 deixou de ser design e virou urgência" · **DS-20260901-013 + DS-N-110 (06:30)** — 🎉 grade matutina chegou: esteira retomou 06:03 (268448 OpenAI) após 2h47 de silêncio pós-reboot; alerta de volume ENCERRADO (3h=3); reboot 3ª confirmação (uptime 3:00, boot ~03:31); Redis PONG 06:31 (OBS encerrada); face 2 recorrente na grade · **DSL-20260901-001 (06:06)** — Baleia manhã entregue ("268448 reabriu antes de qualquer re-alarme") · **DSC-20260901-003 (04:20)** — Ronnie Lessa/Record: fila YouTube PENDENTE desde 04:16 (5º CHECK do chefe às 06:30) · **CL-005/006 (04:12/05:12)** — 268437 Viveros sem capa, "fica para a manhã" · caçada 6 (borda de régua, ficha de boot, catch-up, PPS, mapa de fontes) · IDEIA-003 (P1 trio de datas + verificador de virada; P3 Banco Ouro) · 2ª caçada (prova de vida dos irmãos)

---

## 1. Problemas em curso na janela 04:47 → 06:47 (com ref)

### P1. Quirk P1 face 2 — 5 casos/24h: o design virou urgência (CL-007)
- Ref: **CL-007 (06:12)** — "268451 `date 06:24:21` com `modified 06:04:21`; 268458 `date 06:47:04` com `modified 06:07:05` — posts publicados às 06:04/06:07 com data +20/+40 min à frente (mesmo padrão dos 268366/268393 de ontem). **O feed só os lista quando a data chega. A Ideia-003 P1 (trio de datas + pós-publish síncrono) deixou de ser design e virou urgência: 5 casos em 24 h**" · **DS-013 (06:30)** — "268451/268458 no ar (permalink 200) mas com data futura; ZM: aplicar o fix da face 2 (post_date=now no publish)" · **DS-N-110 (06:30)** — "quirk P1 face 2 VIVO: 5 casos/24h, URGENTE p/ ZM".
- Fato: o fix da face 2 já está desenhado (Ideia-003 P1: trio de datas + normalização imediata), mas continua sendo aplicado como correção posterior (o maestro já normalizou 268366/268393 na noite) — e o padrão se REPETE no primeiro retorno da esteira. Falta: (a) a caneta imediata nos 2 casos de hoje, (b) uma régua de recorrência que torne o caso visível ANTES de virar série, (c) a triagem PRÉ-publish para a classe não nascer mais.

### P2. Reboot 03:31 — 3ª confirmação, causa pendente; o custo foi 2h47 de silêncio
- Ref: **DS-013 (06:30)** — "uptime 3:00 às 06:31 → boot ~03:31 (3ª confirmação); load 2,63/2,56/2,66 saudável; leitor nunca caiu; causa com ZM (dmesg/journalctl)" · **DSL-001 (06:06)** — "268448 NO AR 06:03:19 — esteira retomou após 2h47 de silêncio pós-reboot; 'reabriu antes de qualquer re-alarme'" · **DS-N-110 (06:30)** — alerta encerrado (série 3h: …1→1→1→3).
- Fato: a esteira se auto-recuperou (sem catch-up formal, sem `prev pós-boot` da caçada 6 P2 — a grade matutina simplesmente chegou). O custo do reboot foi 2h47 de fila parada; a régua avisou 1× e a vigília paciente funcionou — mas 2h47 é o "tempo de auto-recuperação" da casa hoje, e ele não é medido nem tem alvo.

### P3. Fila YouTube: Ronnie Lessa PENDENTE 2h30+ — executor sem sinalizar (5º CHECK da vigília)
- Ref: **queue_youtube.md** — "[01/09/2026 04:16 BRT] Ronnie Lessa … STATUS: PENDENTE" · **DS-N-110 (06:30)** — "DSC-003 com 5º CHECK meu: fila PENDENTE desde 04:16 (2h14), DS YouTube ainda não marcou BAIXANDO; próximo marco: BAIXANDO → rascunho → gate CL → Publicador" · **DS-013 (06:30)** — 5º CHECK do DS-Dell na DSC-003, mesma conclusão.
- Fato: a ordem é do Miguel (04:20), o dedup foi conferido pelo DSC (04:16), e 2h30 depois o executor não marcou nem BAIXANDO — sem prova de vida do robô, a vigília (que já conta 5 CHECKS) não sabe se é lentidão, fila perdida ou robô parado. A auditoria da 2ª caçada já mostrou o DS YouTube com "casca viva e saída invisível" (reporte não reflete o estado real). Falta uma régua de progresso da fila, não mais vigília.

### P4. 268437 (Viveros, pessoa central) — a manhã chegou e ele continua sem capa
- Ref: **CL-005 (04:12)** — "268437 «Artilharia do Brasileirão tem Viveros no topo com 17 gols» sem capa — pessoa central (Emenda 12); não caço contextual de madrugada; fica para a variação do robô ou AGY Miguel na manhã (Flickr oficial do clube)" · **CL-006 (05:12)** — "fila do worker segue só com 268437 (Viveros — pessoa central, Emenda 12: para a manhã)" · **DS-013 (06:30)** — grade matutina entregou 268448/268451/268458 — o pessoa central NÃO saiu.
- Fato: "fica para a manhã" foi dito às 04:12 e às 05:12; a manhã chegou (06:03) e o 268437 continua sem capa na fila. A classe pessoa central é a única que a casa aceita adiar — porque a fonte oficial não é mapeada de antemão (caçada 6 P4: mapa de fontes canônicas por entidade, ainda não semeado).

### P5. Alerta de volume encerrado pela grade — post-mortem não vira dado
- Ref: **DS-N-110 + DS-013 (06:30)** — "alerta ENCERRADO: série 3h …1→1→1→3; a vigília uptime × fila × grade funcionou como previsto no DS-109; sem re-alarme (padrão da casa)" · **DSL-001 (06:06)** — "o 268448 reabriu antes de qualquer re-alarme" · lição 268301 (calibrar pelo contexto).
- Fato: o alerta de hoje (3h=1 por 5 rondas, 2h47 de silêncio, encerrado pela grade matutina) é o 2º caso completo da classe "alerta vs contexto" (o 1º foi o da noite, DS-N-096). A casa aprendeu a NÃO re-alarmar; o que falta é o alerta virar dado: duração, causa, o que o encerrou — para a régua calibrar sozinha na próxima ocorrência.

### P6. Degrau 3 do Banco Ouro — janela 03:00 ainda sem a linha do ZM (ADENDO 1 segue aberto)
- Ref: caçada 5 P1 (rito do Degrau 3) · ADENDO 1 (03:14) — quem consolida o jsonl é o ZM; eu consolido o bloco ao Miguel com N≥20/24h · caçada 6 P6 (espelho no CONTEXTO_MINI) · próxima janela de leitura: **07:00**.
- Fato: a linha `sombra: N·H·M·hit-rate` das janelas 03:00 (e, pela ausência registrada, 04:00/05:00/06:00) não foi publicada; o rito segue dependente do maestro lembrar — e a janela de 24h para o N≥20 escorrega a cada ciclo.

---

## 2. Ideias criativas (1-3 por problema — curto ≤1d · médio ≤1sem · longo ≤1mês)

### P1 — face 2: caneta, régua e triagem (fechar a classe, não só os casos)
- **Ideia 1 (curto) — "caneta face 2":** normalizar JÁ os 2 casos de hoje (268451/268458): `wp post update <id> --post_date=now --post_date_gmt=now` (ou REST equivalente) — posts no ar mas com relógio errado (feed atrasa a listagem até a data chegar; a "matéria do futuro" fica invisível no feed). É a execução do fix já desenhado na Ideia-003 P1 — dono ZM, 5 min, reversível (backup do date antes).
- **Ideia 2 (curto) — "verificador estendido (cheque 2)":** o verificador de virada 1/1h (P1 camada A da Ideia-003, já vivo no maestro) ganha um 2º cheque no MESMO ciclo: post com `status=publish` e `date > now` fora da lista do feed → alerta face 2 (não só "future que não virou"). Hoje a face 2 só aparece quando alguém cruza date × modified na auditoria; o verificador a pega na hora.
- **Ideia 3 (médio) — "triagem pré-publish":** no Publicador, antes de gravar o post: comparar `date` × `date_gmt` × `modified`; divergência > 5 min → normaliza (`post_date=now`) no mesmo ciclo e loga a ocorrência. A face 2 deixa de ser classe de correção pós-fato e vira impossível de nascer — o quirk do `wp_publish_post` sem normalizar data (causa da série) morre na origem.

### P2 — reboot: ficha preenchida + alvo de auto-recuperação
- **Ideia 1 (curto) — "ficha de boot preenchida":** a caçada 6 P2 desenhou a ficha; o reboot de hoje já fornece o preenchimento-modelo: (1) zerou ~03:31 (uptime) · (2) sintomas no boot: wp-json 500 "Database Error", SSH fora 1-2 min, esteira parada 2h47 · (3) recuperação: 200 em ~2 min; esteira reabriu 06:03 SOZINHA. O ZM só precisa completar a linha "causa" (dmesg/journalctl) — a ficha vira o registro padrão da próxima ocorrência.
- **Ideia 2 (médio) — "alvo de auto-recuperação ≤ 30 min":** métrica nova `tempo de auto-recuperação pós-boot` (hoje: 2h47) com alvo ≤ 30 min via catch-up pós-boot (caçada 6 P2): quando `future=0` e `uptime<60min`, o Publicador re-agenda o próximo slot direto dos drafts (`prev pós-boot: próximo post X às Y`). O reboot deixa de custar quase 3 horas de fila parada.

### P3 — fila YouTube: SLA + heartbeat (prova de vida do executor)
- **Ideia 1 (curto) — "SLA da fila YouTube":** marcos com prazo na `queue_youtube.md`: PENDENTE→BAIXANDO ≤ 30 min após o dedup · BAIXANDO→ENTREGUE_GATE ≤ 4h. Estouro → 1 linha de escalada ao maestro (a vigília do chefe já conta 5 CHECKS sem sinal — a régua formaliza o que a vigília faz à mão). No caso Ronnie Lessa: 04:16 + 30 min = 04:46 era o prazo do BAIXANDO; estamos 2h atrasados — escalada já caberia.
- **Ideia 2 (curto) — "heartbeat `last_check:`":** cada ciclo do robô escreve 1 linha (`last_check: <ts>` + status lido) no fim da queue_youtube.md. PENDENTE por > 2h com last_check velho = robô parado (e a vigília sabe que é parada, não lentidão). É a prova de vida do DS YouTube que a auditoria da 2ª caçada mostrou faltar ("casca viva, saída invisível").

### P4 — pessoa central: semear o mapa de fontes com os casos de hoje
- **Ideia 1 (curto) — "primeiras 3 entradas do mapa":** o mapa de fontes canônicas por entidade (caçada 6 P4) nasce com os casos de hoje, todos com fonte oficial conhecida: **Viveros** → Flickr oficial do clube (a própria CL-005 citou) · **Eduardo Paes** → Agência Brasil / prefeitura do Rio · **Lula** → Agência Brasil / Fotos Públicas. Arquivo `estado/mapa_fontes_canonicas.md` (1 linha por entidade + regra de frescor Emenda 12). A classe pessoa central deixa de "esperar a manhã": o 268437 sai em 1 ciclo com a fonte pré-registrada.

### P5 — alerta vira dado: post-mortem + contexto declarado
- **Ideia 1 (curto) — "post-mortem de alerta":** ao encerrar um alerta de volume, 1 linha no estado (`estado/alerta_volume_historico.md`): `causa · duração · o que encerrou · lição`. O de hoje (causa: reboot pós-boot 2h47 · duração: 5 rondas · encerrou: grade matutina 06:03 · lição: vigília uptime×fila×grade funcionou) vira o 2º ponto da série — a régua calibra com dados, não com memória.
- **Ideia 2 (médio) — "contexto declarado no alerta":** a calibração 268301 (madrugada/reboot/fila/grade) vira campo no CHECK: `alerta_contexto: madrugada|pós-reboot|fila-parada|grade-prevista`. O alerta nasce classificado; a decisão de re-alarmar ou não deixa de depender de cada ronda redescobrir o contexto.

### P6 — Degrau 3: vigília mantida + lembrete formal ao ZM
- **Ideia 1 (curto) — lembrete:** as janelas 03:00/04:00/05:00/06:00 seguem sem a linha `sombra: N·H·M·hit-rate` (ADENDO 1 das caçadas 5/6); próxima janela **07:00** — registro aqui para o maestro publicar a linha de TODAS as janelas pendentes de uma vez (03:00→06:00 + 07:00) e o N≥20/24h fechar ainda hoje.

---

## 3. Alimentação do DS Nuvem Marketing (irmão)

- **Gancho (curto) — 268448 OpenAI US$ 1 bi:** "a IA que escreve os posts agora vende anúncios DENTRO da resposta" — o Cafezinho roteia barato-primeiro (DeepSeek/GLM, fallback em 8 provedores) para a resposta ficar barata E neutra; a matéria do retorno da esteira é o preço da ferramenta que escreve — boa ponte IA × jornalismo independente.
- **Pauta quente (curto) — 268458 Lula × Flávio Bolsonaro (negacionismo climático):** política da manhã; complementa o fio de confiabilidade com tom de colunista (manual IDEIA-001).
- **Fio de confiabilidade (médio) — "até o relógio reinicia":** reboot 03:31 → retomada 06:03 (2h47 documentada na Baleia da manhã, DSL-001); o Cafezinho volta e a régua conta a história com transparência — amadurece o gancho "o relógio não dorme" (caçada 5) e "o ranking não sobe sozinho" (caçada 6).
- **Contexto de audiência:** manhã aquecendo — LUMINA 58 (melhor marca do dia), 456 distintos/486 visitas às 06:30 (DS-N-110).

---

## 4. Métrica (acumulado das caçadas)

| Caçada | Propostas | Destaque |
|---|---|---|
| 1 (31/08 18:43) | ~15 | P1 errata 1-toque · P3 régua 2ª fonte |
| 2 (31/08 20:45) | ~14 | fila única de capas · prova de vida dos irmãos |
| 3 (31/08 22:45) | ~12 + E1-E5 | verificador de virada (ADOTADO — P1 Ideia-003) |
| 4 (01/09 00:47) | 6 (encomenda IDEIA-004) | ORIGENS + editora própria |
| 5 (01/09 02:47) | 9 | rito Degrau 3 · grade de previsão · régua de convergência |
| 6 (01/09 04:47) | 11 | borda de régua · ficha de boot · PPS · mapa de fontes |
| 7 (01/09 06:47) | 12 | caneta face 2 · verificador estendido · SLA da fila YouTube · alvo de auto-recuperação |

---

## 5. O que preciso do Miguel / da ponte

- **Do Miguel:** nada bloqueante — avaliar as ideias da caçada (rito E2 da Arquitetura: ✓/✗ em ≤2 rondas); lembretes vivos inalterados: ✓ da IDEIA-004 · 4 decisões da arquitetura (CL-041 §13) · X Premium · IG no debate do DS-N Redes · DSC-013 palavra-chave.
- **Da ponte:** ZM — **caneta face 2 (normalizar 268451/268458 + triagem pré-publish)** + causa do reboot (dmesg/journalctl) + linha `sombra` do Degrau 3 (03:00→06:00 pendentes; próxima 07:00) · DS YouTube — marcar BAIXANDO na fila Ronnie Lessa (SLA: prazo era 04:46) · CL — série `ram:` no CHECK (caçada 6 P5) · Publicador — `prev pós-boot` na próxima entrega (caçada 6 P2).
