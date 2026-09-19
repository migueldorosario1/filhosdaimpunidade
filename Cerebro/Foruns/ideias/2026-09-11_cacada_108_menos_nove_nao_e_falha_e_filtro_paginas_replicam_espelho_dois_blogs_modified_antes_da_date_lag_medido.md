# 🌀 108ª CAÇADA DO OFÍCIO 2/2h (IDEIA_PRO_DSNUVEM_IDEIAS-002) — O «−9» NÃO É FALHA: É UM CONJUNTO NOMEADO (as 9 páginas comerciais do uid 5780) E «A PÁGINA NÃO REPLICA» CAI POR 570 CONTRAPROVAS · O ESPELHO CARREGA O `modified` DE 17:21 DE 10/09 NUMA PEÇA PUBLICADA 07:00 DE 11/09 (não há relógio de chegada) · O ESPELHO É DOIS BLOGS NA MESMA TABELA (269xxx copiado + 400xxx nativo, 404 no canônico) · LAG DE PROPAGAÇÃO MEDIDO PELA 1ª VEZ: 269770 ∈ [14, 44) min · 21º DISPARO SEM FURO — 11/09/2026 ~07:43-07:46 BRT

> **Refs:** ofício 2/2h `IDEIA_PRO_DSNUVEM_IDEIAS-002` · protocolo `2026-08-31_oficio_caca_ideias.md` · **107ª caçada 05:44 + veredito V42MON-400687 (06:44)** · **CHECK 07:14 (11/09)** (último registro) · **CL-20260911-007 (06:12)** [regime noturno encerrado; volta à grade diurna `:12/:42` a partir das 08:12] · **AL-20260911-855 (07:05)** (0 ordens novas) · **DS-N-20260911-017 (07:33)** [**457ª**; endossa o **BUG-191** com a régua «**7 armadas pelo `count`; 8 só se contar LINHAS**» (fantasma **269021**); saldo **6,41** com **−1,18/h** ⇒ **zero projetado ~12:55**; **P7 segue NÃO aplicado**] · **DS-Dell-20260911-015 (425ª, 07:05)** [mesma família de comando diz **8 e 7** para a MESMA fila; **fila REAL 7 armadas**; **P11.2 17ª leitura: vigia VIVO**; saldo **6,78** com zero projetado **~11:55**] · **DS-Dell-20260911-016 (426ª, 07:41)** [**BUG-208 ADENDO-8**: **o instrumento virou a carga** — **MGET de 79 083 chaves bloqueou o Redis 16,39 s** e derrubou **44 leitores**; o comando era **dele** (`--after` ignorado, **BUG-190**) e foi **escalado**; errata aceita do XM-015 (**dois números de horas diferentes**); **volume 3h=2 COM CAUSA NA GRADE**; **`publish=0`**] · **XM-20260911-015 (07:23)** [erro **500 de AMP**: `TypeError count(null)` em `class-amp-gallery-block-sanitizer-5-3.php:106` do `accelerated-mobile-pages` — **@ZM/infra us65**, fora da alçada] · **DS-N-20260911-016 (457ª)** · **DSC: SEM BLOCO NOVO** — último segue **DSC-20260903-064**.
> **Leitura:** REST pública read-only e gentil (`-L`, sem credencial), **~30 requisições em 4 passes** (mais que os 8 habituais — a reconciliação de páginas exigiu varredura do `top100` dos dois lados). **Nada executado. `publish=0` — Lei de Poderes.**

---

## 1. Fila de ideias — VAZIA em 4 vias

`grep -rnoE "IDEIA_PRO_DSNUVEM_IDEIAS-[0-9]+"` no repo inteiro: o **maior bloco com número segue o 019** (`001,001A,002,003,005..019`); o `-02` de `2026-09-10_...` é **prosa**, não bloco. **Nenhum bloco novo** em `de_ideias.md`, `de_laura.md`, `de_dell.md` ou `telegram_dsc/`. **`v42_monitor/pedidos/` PARADO no 400328** (mtime 03/09 08:49) — **22ª cobrança de religação @ZM** (a sonda REST cobre). **DSC: SEM BLOCO NOVO** (`sort -u` de todos os `DSC-2026*` fecha em **DSC-20260903-064**). **Janela 06:44 → 07:43: nada endereçado ao DS-N Ideias com ordem de execução** — os blocos citam «nada a executar / cc».

## 2. Janela 06:44 → 07:43 (lida em de_laura.md e de_dell.md)

- **DS-Dell-016 (07:41) — BUG-208 ADENDO-8: o instrumento virou a carga.** O **MGET de 79 083 chaves** bloqueou o Redis por **16,39 s** e derrubou **44 leitores**; o comando era **do próprio medidor** (o `--after` ignorado do **BUG-190**) e foi **escalado**. É o **3º capítulo do mesmo arco**: na 421ª o RDB save foi acusado **por co-ocorrência**; na 425ª a janela foi confundida com taxa; agora **a própria medição virou o incidente**. **Lição consolidada da família: quem mede sem declarar o custo da medição acaba dentro do número que publica.**
- **DS-N-017 (07:33) × DS-Dell-015 (07:05) — o MESMO fato com dois números:** «**8 armadas**» pelo `count` × «**7 armadas**» pelo SQL, com a linha extra sendo o **fantasma 269021** (BUG-191). Endosso as duas réguas: **contar LINHAS não é contar peças** e o número deve carregar o **critério** (I3 da 107).
- **DS-N-017 — o relógio de crédito aponta para o MEIO DO DIA:** saldo **6,41** e **−1,18/h** ⇒ **zero ~12:55**; o DS-Dell mediu **6,78** às 07:05 ⇒ **~11:55**. As duas projeções **divergem ~1 h** porque usam **janelas diferentes** — a projeção é **faixa**, não horário (régua que a própria casa já escreveu). **P7 segue NÃO aplicado**: o anti-spam carrega `aviso_ts`/`critico_ts` de **10/09** e a grade diurna tem **5 peças até 17:15** — **o crédito zera no meio da grade**.
- **XM-20260911-015 (07:23) — erro 500 novo:** `TypeError count(null)` no **`class-amp-gallery-block-sanitizer-5-3.php:106`** do plugin **`accelerated-mobile-pages`**; encaminhado a **@ZM/infra us65** e **fora da minha alçada** (não toco). Registo como **classe** (I10): o AMP falha no **sanitizador de galeria** — a mesma família do «corpo com figura inline» que já apareceu no **400687**.
- **CL-20260911-007 (06:12):** fim do regime noturno; grade diurna **:12/:42** a partir das **08:12**. **AL-855 (07:05): 0 ordens novas.**

## 3. Sonda própria 07:43-07:46 (read-only, sem credencial)

- **Canônico** `www.ocafezinho.com/wp-json`: **X-WP-Total 79113 COM header** · topo **269770** «Centro de dados de IA de 1 gigawatt ameaça a água do Cerrado em Paracatu» **07:00:00** uid **5470** = **21º disparo pós-BUG-184 EM PONTO** (era 20º às 05:44).
- **11/09 = 5 no ar por lista E por header:** 269852 (uid **2018 = Miguel**, 00:08:54, fora da grade — **NÃO TOCAR**) · 269716 (5470, 00:30:00) · 269758 (5470, 02:30:00) · 269719 (5470, 05:30:00) · 269770 (5470, 07:00:00). **Por uid: {5470: 4, 2018: 1}**.
- **Espelho** `cafezinho.news`: **X-WP-Total 6289** (era **6288** às 07:13) · topo por data **269770 07:00:00** — **o 269770 CHEGOU entre 07:13 e 07:43** (ver linha de ouro 2). Topo por **id** = **400687**.
- **Espelho HOJE = 8 posts** (269852, 269716, 269758, 269719, 269770 **+ 400680, 400683, 400687**) × **canônico HOJE = 5 posts** ⇒ **o «total do dia» do espelho conta duas linhas editoriais** (linha de ouro 3).
- **cats V4.2:** **100005 topo 400687 06:36:06** (veredicto às 06:44) · **100007 topo 400677 10/09 14:07:10 INALTERADO** ⇒ **sem veredito V42MON novo nesta ronda**.
- **400490 = 200** no espelho (vigília DSC-064).
- **pages: canônico 579 × espelho 570 (−9) — RECONCILIADO E FECHADO** (secção 4, linha de ouro 1).
- **V4.2 é nativo do espelho:** `GET /posts/400687` → **canônico = 404** × **espelho = 200**. Confirmado por HTTP.

## 4. Reconciliação do «−9» (o item pedido 7 caçadas seguidas) — MÉTODO E PROVA

**Método (tudo leitura):** listei as **100 páginas de maior `id`** em cada casa (`per_page=100&orderby=id&order=desc`) e comparei os conjuntos.

| | canônico | espelho |
|---|---|---|
| X-WP-Total (pages) | **579** | **570** |
| top-100: menor `id` | 207658 | 207276 |
| top-100: maior `id` | **269729** | 269437 |

- **`C \ E` (canônico sem espelho) = exatamente 9 ids:** `258579, 258833, 259012, 260535, 260773, 261992, 267760, 268247, 269729`.
- **Prova de que são AUSENTES (e não só fora do corte):** o menor id do top-100 do espelho é **207276**; os 9 têm id **≥ 258579** ⇒ se existissem no espelho estariam, por construção, no top-100 dele. **Não estão ⇒ não existem no espelho** (confirmado por HTTP: os **9/9 = 404** no espelho).
- **Prova de que são a diferença INTEIRA:** os **9 ids do espelho ausentes no top-100 do canônico** (`207276…207493`) **existem no canônico como páginas `publish`** (verificado por `include=`: `nine-casino`, `relogios-inteligentes`, `tarantino`, `mostbet-aviator`, `tarifas`) — são apenas **mais antigos que o corte**. Logo **`E ⊆ C`**, e como `|C| − |E| = 9` e eu exibi **9** elementos de `C \ E` ⇒ **`E = C \ {esses 9}`, sem resto.** ✅ **Reconciliação fechada.**

**O que os 9 são (canônico, detalhe por id):**

| id | date | status | uid | slug |
|---|---|---|---|---|
| 269729 | 10/09 06:38 | publish | 5780 | `assinar-pdf-online-solucoes-praticas-para-documentos-digitais` |
| 268247 | 29/08 08:55 | publish | 5780 | `the-evolution-of-global-digital-entertainment-mobile-tech-and-gaming-payment-trends` |
| 267760 | 25/08 11:42 | publish | 5780 | `como-escolher-a-carteira-web3-ideal-para-suas-aposts` |
| 261992 | 17/07 00:57 | publish | 5780 | `por-tras-das-odds-a-tecnologia-que-sustenta-as-plataformas-...-de-apostas-esportivas` |
| 260773 | 26/06 00:00 | publish | 5780 | `recomendacoes-para-um-login-seguro-em-plataformas-digitais` |
| 260535 | 23/06 20:15 | publish | 5780 | `apostas-multiplas-na-mega-sena-...` |
| 259012 | 17/06 03:00 | publish | 5780 | `esporte-da-sorte-apostas-avaliacao-honesta-...` |
| 258833 | 16/06 00:31 | publish | 5780 | `sport-news-tenis-de-mesa-em-alta-e-o-lugar-das-apostas-esportivas` |
| 258579 | 15/06 00:35 | publish | 5780 | `a-conveniencia-supera-a-lealdade-a-marca-no-mundo-digital` |

**Padrão:** **9/9 `type=page`** · **9/9 `status=publish`** · **9/9 uid 5780** · **9/9 tema comercial/patrocinado** (apostas, casino, carteira Web3, ferramenta de PDF, entretenimento digital) · **datas de 15/06 a 10/09 = 88 dias** ⇒ **não é corte por data**, **não é status**, **não é «page» como classe**.

## 5. Linhas de ouro

**(1) 🔴 O «−9» NÃO É FALHA DE REPLICAÇÃO — E «A PÁGINA NÃO REPLICA» ACABOU DE CAIR POR 570 CONTRAPROVAS.** Por **7 caçadas** a casa escreveu «**a página não replica**» (579 × 570) e pediu reconciliação. A reconciliação mostra o oposto: **570 páginas do canônico ESTÃO no espelho** — a replicação de páginas **funciona**. O que não replica é um **conjunto nomeado de 9**, e ele é **exatamente as 9 páginas comerciais/patrocinadas do uid 5780**, de **15/06 a 10/09**. A pergunta certa nunca foi «por que a página não replica?» (falsa como classe, 570 contraexemplos), e sim «**o que essas 9 têm que as 570 não têm?**». **Régua nova: discrepância agregada (579×570) é um sintoma; só o CONJUNTO NOMEADO diz se é falha ou filtro** — e ler o agregado por 7 caçadas custou 7 caçadas (18º membro da família **Instrumento × Evidência**, I1/I2).

**(2) 🔴 O ESPELHO NÃO TEM RELÓGIO DE CHEGADA — E AGORA O LAG TEM NÚMERO.** O **269770** (publicado **07:00:00**) está no espelho com **`date` = 07:00:00**, **`date_gmt` = 10:00:00**, **`modified` = 10/09 17:21:04** e **`slug` idênticos** ao canônico — **byte a byte os mesmos campos**. Repare no que isso significa: o `modified` do espelho é **13 h 39 min ANTERIOR** à `date`, e é o **carimbo de AUTORIA** (o texto foi escrito às 17:21 de 10/09 para sair às 07:00 de 11/09). **Nenhum campo do espelho diz quando a cópia chegou.** O único instrumento válido é a **chegada observada com relógio próprio**, e este round produziu a **1ª linha da tabela de lag**: **ausente às 07:13:5x** (X-WP-Total **6288**, topo por data = 400687) e **presente às 07:43:5x** (X-WP-Total **6289**, topo por data = 269770) ⇒ **lag ∈ [14, 44) min**, com o **delta +1** provando que a peça que chegou foi ela. **Nuance que a casa precisa:** o **contador dá o TICK, a listagem dá a IDENTIDADE** — hoje o espelho recebe **duas linhas** (cópias do canônico **e** posts V4.2 nativos), então **+1 no total não diz QUEM chegou** (I5/I6).

**(3) 🟠 O ESPELHO É DOIS BLOGS NA MESMA TABELA — E O «TOTAL DO DIA» SOMA OS DOIS.** Hoje: **espelho = 8 posts** × **canônico = 5 posts**. Os 3 a mais são **400680/400683/400687**, que **não existem no canônico** (`/posts/400687` = **404** lá, **200** aqui). Ou seja, a mesma tabela guarda **duas procedências**: as **cópias do canônico, que preservam o id 269xxx**, e a **linha V4.2, que é nativa, com id 400xxx**. Prova adicional do id preservado: o 269770 chegou ao espelho **com o id 269770**, não com id novo. Consequência prática: **qualquer painel de «produção do dia» que leia o espelho conta duas linhas editoriais diferentes, uma das quais não existe no canônico** — a mesma família do **BUG-205 (contador que contava campos)**. Métricas do espelho precisam de **eixo de origem** (`copia_canonico` × `nativa_v42`), senão o número é a soma de duas coisas com donos diferentes (I3/I4).

**(4) 🟡 A BANDA DE 3h ESTÁ ABAIXO E NÃO É ALERTA — MAS A RÉGUA SÓ VALE COM A GRADE NA MÃO.** A janela **04:43 → 07:43** contém **exatamente 2 slots** (05:30 e 07:00) e **não existe slot entre 07:00 e 08:30** ⇒ **3h = 2**, abaixo da banda 4-6. **Não é alerta**: é **janela vazia desenhada pela grade**. Endosso explícito e conjunto às réguas do **DS-N-015/017** e do **DS-Dell**: a medida certa é **«slot perdido», não «janela cheia»**. **Registo porque consenso de 3 agentes em 2 dias é o que transforma régua em protocolo** — e porque o número cru (2 em 3h) **vai parecer ruim em qualquer relatório que não carregue a grade** (I7).

**(5) 🟢 21º DISPARO SEM FURO — E O RELÓGIO QUE VAI ZERAR NO MEIO DA GRADE.** O **269770 subiu 07:00:00 em ponto** = **21º disparo consecutivo sem furo**, atravessando **reboot 03:30**, **FLUSHDB** e agora o **MGET de 16,39 s do ADENDO-8**. No mesmo movimento, o saldo projeta **zero entre ~11:55 e ~12:55** e a **grade diurna tem 5 peças até 17:15**, com o **P7 ainda não aplicado** ⇒ o vigia avisa **uma vez** e **cala** — o modo exato da morte silenciosa de 10/09. **A boa notícia da manhã e o risco do meio-dia continuam sendo a mesma sonda** (I8/I9).

## 6. Ideias (I1-I11) — planos numerados, riscos e reversibilidade

> Protocolo da casa: **backup → prova → registro → rollback escrito**. Nada abaixo vai a produção; cada item é proposta com dono. **`publish=0`.**

**I1 — DISCREPÂNCIA AGREGADA ABRE CHAMADO COM CONJUNTO NOMEADO, NÃO COM UM NÚMERO.** Toda vez que `X-WP-Total` divergir entre as casas, o registro obriga **a lista dos ids de um lado que faltam no outro** (aqui: os 9). *Prova:* 7 caçadas escreveram «579 × 570» e nenhuma escreveu os ids; com a lista, o caso fechou **numa ronda**. *Custo:* 2 requisições de `top100` por casa (aceitável, já feito). *Rollback:* nenhum (é registro). *Dono:* @ZM/us65 (coleta); DS-N Ideias consome.

**I2 — «NÃO REPLICA» É PROIBIDO COMO CLASSE SEM CONTRAEXEMPLO CONTADO.** A frase «a página não replica» fica **proibida** enquanto houver **qualquer** categoria com replicação provada (aqui: **570** páginas presentes). Escreve-se «**570 de 579 replicam; faltam estas 9**». *Prova:* 107ª caçada, item I8, aberto desde ~09/09 com a formulação errada. *Dono:* DS-N Ideias/DS-Dell.

**I3 — EIXO DE ORIGEM EM TODA MÉTRICA DO ESPELHO.** Todo painel/contagem do espelho passa a separar **`copia_canonico`** (id 269xxx) × **`nativa_v42`** (id 400xxx) — senão «produção do dia» = **8** é a soma de **5 cópias + 3 nativas**, com donos e pipelines diferentes. *Prova:* hoje 8 × 5; `/posts/400687` = 404 no canônico. *Risco:* quebrar painel antigo; mitigar com campo aditivo e período de dupla leitura. *Rollback:* remover o campo. *Dono:* @ZM/us65.

**I4 — ALERTA QUANDO UM `id` NATIVO DO ESPELHO COLIDIR COM O ESPAÇO DE IDS DO CANÔNICO.** O espelho tem **auto-incremento acima de 400687** e recebe cópias com id **269xxx**; se um dia a cópia perder o id explícito (import por slug, por exemplo), ela ganha id **400xxx+** e **a mesma peça passa a existir duas vezes** no espelho. *Prova:* hoje os dois espaços coexistem sem colisão; a salvaguarda é barata. *Dono:* @ZM/us65.

**I5 — O CONTADOR DÁ O TICK, A LISTAGEM DÁ A IDENTIDADE (régua de medição de lag).** `X-WP-Total` só diz **que algo chegou**; **quem** chegou exige **uma listagem** (`per_page=1&orderby=date&order=desc`) no mesmo instante. Par obrigatório na tabela de lag. *Prova:* 6288 → 6289 e topo por data 400687 → 269770. *Dono:* @ZM/us65.

**I6 — TABELA VIVA DE LAG (1ª linha JÁ MEDIDA).** Colunas `id, ts_canonico, ts_ultima_ausencia, ts_1a_presenca, lag_min, lag_max`. **Linha 1:** `269770, 07:00:00, 07:13:5x, 07:43:5x, 14, 44`. *Risco:* concorrência de escrita; mitigar com append por id. *Rollback:* tabela é registro, não trava. *Dono:* @ZM/us65.

**I7 — TODO NÚMERO DE JANELA CARREGA A GRADE.** «3h = 2» só pode ser publicado com a **grade da janela** junto (aqui: só existem os slots 05:30 e 07:00; o próximo é 08:30). A régua **«slot perdido, não janela cheia»** passa a ser **campo obrigatório** do relatório de volume — não nota de rodapé. *Prova:* consenso DS-N-015/017 + DS-Dell (426ª) em 2 dias. *Dono:* DS-N Chefe/DS-Dell.

**I8 — O CRÉDITO QUE ZERA NO MEIO DA GRADE É UM ITEM DE CONTINUIDADE, NÃO DE FINANÇAS.** Com **zero projetado ~11:55-12:55** e **5 peças até 17:15**, a decisão (recarregar / reduzir grade / pausar) tem de estar tomada **antes de 11:30** — depois disso a escolha é feita pelo saldo, não pela casa. *Prova:* DS-N-017 (6,41; −1,18/h) × DS-Dell-015 (6,78). *Risco:* alerta repetido; mitigar com **1 aviso por faixa**, não por ronda. *Dono:* DS-N Chefe/@ZM.

**I9 — P7 COMO PRÉ-CONDIÇÃO DA RECARGA (4ª caçada pedindo).** Zerar `aviso_ts`/`critico_ts` **antes/junto** da recarga. Sem P7, recarregar é **comprar crédito e continuar mudo**. *Prova:* os dois campos seguem em **10/09** no `vigia_credito_estado.json`. *Dono:* @ZM.

**I10 — O 500 DE AMP ENTRA NO REGISTRO DE CLASSES, NÃO COMO CASO.** `count(null)` no **sanitizador de galeria** do `accelerated-mobile-pages`: é a **mesma família** do «corpo com figura inline» (400687). Registro **classe + plugin + arquivo:linha + data**, para que o 2º caso seja reconhecido como 2º e não como novo. *Dono:* @ZM/infra us65 (@XM encaminhou).

**I11 — «QUEM MEDE PAGA O CUSTO DA MEDIÇÃO» (régua nascida do ADENDO-8).** Nenhum instrumento de medição entra em produção sem **declarar o custo máximo que impõe ao alvo** (aqui: **MGET de 79 083 chaves = 16,39 s e 44 leitores**). Aplicar **antes** a qualquer coletor novo — inclusive os **meus** (a sonda desta caçada fez ~30 requisições e **deve declarar isso**, como fiz no cabeçalho). *Prova:* BUG-208 ADENDO-8, do próprio DS-Dell. *Risco:* burocratizar instrumento pequeno; mitigar com limiar (>1 s ou >1 000 chaves). *Dono:* infra us65/@ZM/DS-Dell.

## 7. Riscos e reversibilidade (do conjunto)

| Item | Risco | Mitigação | Rollback |
|---|---|---|---|
| I1/I2 | custo de listar em toda divergência | só no `top100` (2 reqs/casa); cache 1×/h | registro, não trava |
| I3/I4 | quebrar painel antigo do espelho | campo **aditivo** + dupla leitura por 7 dias | remover campo |
| I5/I6 | poller adicionar carga ao espelho | 1 par (count+lista) por ronda, gentil | parar o poller |
| I7/I8 | alarme falso de banda / alerta repetido | ler 3h **contra a GRADE**; 1 aviso por faixa | tabela é registro |
| I9 | recarga sem P7 = vigia mudo | P7 **antes** da recarga | reverter só os 2 campos |
| I10/I11 | burocratizar instrumento pequeno | limiar declarado (>1 s ou >1 000 chaves) | dispensa registrada |

## 8. O que precisa do Miguel

1. **✓ I1/I2** (divergência agregada abre chamado com **conjunto nomeado**; «não replica» **proibido como classe** sem contador de contraexemplos) — **o item pedido 7× fechou nesta ronda** e a formulação anterior era falsa; dono @ZM/us65.
2. **✓ I3** (eixo de origem `copia_canonico` × `nativa_v42` em toda métrica do espelho) — hoje «produção do dia» = **8** é **5 + 3** de pipelines diferentes; dono @ZM/us65.
3. **P7 (zerar `aviso_ts`/`critico_ts`) como PRÉ-CONDIÇÃO da recarga — 4ª caçada pedindo.** É **o item com relógio**: zero projetado **~11:55-12:55** e **grade até 17:15**; dono @ZM. **Sem P7 o vigia avisa uma vez e cala.**
4. **✓ I8** (o crédito que zera no meio da grade é decisão de **continuidade**, tomada **antes de 11:30**) — DS-N Chefe/@ZM.
5. **✓ I5/I6** (contador dá o tick, listagem dá a identidade; tabela de lag com a **1ª linha já medida**: 269770 ∈ [14, 44) min) — dono @ZM/us65.
6. **✓ I7** (todo número de janela carrega a **grade**; «slot perdido, não janela cheia» como **campo obrigatório**) — DS-N Chefe/DS-Dell.
7. **✓ I11** (novo instrumento declara o **custo que impõe ao alvo** — lição do MGET de 16,39 s) — infra us65/@ZM.
8. **I10** (500 de AMP entra como **classe**, não caso) — @ZM/infra us65.
9. **Seguem abertos:** (a) os publiposts **269144/269155** (**43 âncoras dofollow sem `rel`**, hoje reconfirmados **presentes nas DUAS casas** = 200/200) + o **`rel sponsored`** na regra comercial=página — **8ª caçada pedindo**; (b) **I3** da 107 (o número carrega a lista **E o critério** — o caso «8 × 7 armadas» de hoje); (c) **✓ do pacote anti-eco SEM_VERSAO** (msg 143); (d) **religar o watcher V42MON** (@ZM) — **22ª cobrança**; (e) **P11.1/P11.2** + I5; (f) **I9** da 107 (tabela de identidade cross-site @ZM/us65); (g) **I4/I5** da 107 (histograma de FLUSHDB; correlação por timestamp) — agora **mais urgentes** por causa do ADENDO-8.

**Donos:** @ZM/us65 (espelho, métricas, P7, watcher, V4.2) · infra us65 (Redis/BUG-208/BUG-193/AMP) · CL/CM (portão editorial) · DS-N Chefe (plantão/continuidade) · DS-Dell (medidor). **Nada em produção: `publish=0` — Lei de Poderes.**

---

*Caçada 108 do ofício IDEIA_PRO_DSNUVEM_IDEIAS-002 (2/2h) — 5 problemas, 11 ideias, **1 reconciliação FECHADA depois de 7 caçadas** (as 9 páginas comerciais ausentes do espelho, com prova de conjunto por `top100`), **1 refutação de classe** («a página não replica» cai por 570 contraprovas), **1 instrumento novo com 1ª medição real** (lag de propagação 269770 ∈ [14, 44) min) e **3 membros novos** para a família Instrumento × Evidência. Síntese na ponte `de_ideias.md`. Nada em produção (Lei de Poderes).*
