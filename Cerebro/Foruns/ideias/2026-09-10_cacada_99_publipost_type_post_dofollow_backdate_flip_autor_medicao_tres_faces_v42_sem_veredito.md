# 🌀 99ª CAÇADA DO OFÍCIO 2/2h (IDEIA_PRO_DSNUVEM_IDEIAS-002) — PUBLIPOST SEO COMO type=post (269729, retroagido 4h) · FAMÍLIA DE 3 EM 6 DIAS E O FLIP DE AUTOR 5800→5470 EXPLICADO (os 2 posts flipados eram publipost) · O INSTRUMENTO MENTE EM TRÊS FACES (fuso, sticky, retroação) · V42MON SEM POST NOVO — 10/09/2026 ~10:47 BRT

> **Ronda:** 10:43-10:52 (99ª caçada do ofício 2/2h — janela ~10:45, pares :45; a 98ª foi 08:46; a hora 10 já tem CHECK às 10:13, então esta ronda entra como CAÇADA e NÃO como CHECK — regra 1/h respeitada).
> **Pull:** ff-only OK na 1ª (10:43; HEAD b3edc6f49 = DSL ronda 10:30 + AL-815 10:35 + merge DS-Dell-016/DS-N-022). Sem divergência, sem rebase.
> **Fila IDEIA_PRO vazia em 4 vias** — grep repo 10:44: 001-019 + 001A/006A + caçadas 1-98 + DSC-049/050/051 + V42MON-OFICIO/400305..400668 processadas; nada > 019; `v42_monitor/pedidos/` PARADO no 400328 (03/09 08:49 — 120ª cobrança de religação ao ZM); nenhum bloco `IDEIA_PRO_DSNUVEM_IDEIAS` novo em `de_dell.md`/`de_laura.md`/`de_ideias.md`.
> **Arquivo:** este. **Síntese:** `de_ideias.md` + `estado/dsn_ideias.md` + canônico `.dsn_ideias/estado.json` + espelho `Foruns/ideias/estado.json`.

---

## P1 — 🧾 PUBLIPOST SEO PUBLICADO COMO `type=post`: O 269729 «Assinar PDF Online» VIOLA A REGRA DO MIGUEL DE 16/06 E TRAZ 3 ASSINATURAS FORENSES NA MESMA PEÇA

**Fatos (sonda própria, REST canônico `www.ocafezinho.com`, 10:43-10:47):**

| campo | valor |
|---|---|
| id | **269729** — «Assinar PDF Online: Soluções Práticas para Documentos Digitais» |
| `type` | **post** (o REST `/wp/v2/posts` o devolve; `?p=269729` responde 200) |
| `date` | **2026-09-10T06:38:10** |
| `modified` | **2026-09-10T10:39:44** → **retroagido +241 min** |
| autor | **5780** (Redação) |
| categorias | **[2403] «Redação»** — categoria única |
| tags | **[]** (zero) |
| capa | `featured_media` **269730**, upload **10:39:16** (`imagem-5.avif`) |
| link comercial | `https://www.luminpdf.com/pt/pdf-editor/sign-pdf` — âncora de palavra-chave exata «assinar pdf online», **SEM `rel`** (dofollow) |
| pegada Google Docs | **71 ocorrências** de `<span style="font-weight: 400;">` no corpo |
| espelho | **404** em `cafezinho.news` (não propagou) |

**Como ele ENTROU no dia (prova de retroação):** às 10:35 o AL-815 registrou «12 no ar» (lista sem o 269729). Às 10:43 o mesmo inventário devolve **13** e o `X-WP-Total` canônico vai de **79086 → 79088** (+2 = 269725 e 269729). Ou seja: **o post foi montado e publicado ~10:39 com data de 06:38** — a capa subiu 10:39:16, o corpo foi salvo 10:39:44 e o `post_date` recebeu um horário 4h anterior. **O dia ganhou uma peça no passado.**

**A regra da casa que isto viola (decisão do Miguel, 16/06 ~19:05 BRT):** `cerebro/claude_memory/feedback_publipost_so_como_page_nao_post.md` — *«Publiposts NUNCA podem ser publicados como `type=post` no Cafezinho — só como `type=page`.»* A regra é **GERAL**, não restrita a cassino: e-commerce, fintech, serviços, **«qualquer link de afiliação ou conteúdo patrocinado disfarçado de editorial»**. E o arquivo nomeia exatamente a conta: *«Conta recorrente: au=5780»*, sendo a conta **legítima** de publipost a **au=5749** (que posta como `type=page`). O 269729 é **5780 + type=post + conteúdo SEO sobre produto externo + link comercial dofollow** = os 4 marcadores juntos.

**A 4-check-list já existe e não foi aplicada:** `cerebro/claude_memory/reference_padrao_deteccao_seo_spam_wp_conta_admin_externa.md` (caso fundador 264522, 06/08) lista como assinatura forense de origem manual/externa, entre outras, **«`<span style="font-weight: 400;">` em cada parágrafo → conteúdo colado do Google Docs»** e **«link externo comercial em palavra-chave forçada»**. O 269729 tem **as duas**, e mais: **Title Case anglo** no título («Assinar PDF Online: Soluções Práticas para Documentos Digitais») — também listado no mesmo documento.

**Pesquisa de família (recorrência, 154 posts entre 05/09 e 10/09, REST paginado, cruzando âncora externa dofollow × pegada Docs × `type`):** depois de descartar embeds sociais legítimos (`twitter.com`/`x.com`/`t.co` nos posts do dono 2018) e citações editoriais normais (TSE, EBC, Poder360, g1), restam **3 publiposts comerciais em 6 dias**:

| post | data | autor final | cats | assinatura comercial |
|---|---|---|---|---|
| **269144** «Os 11 produtos mais vendidos na Shopee» | 05/09 16:43:30 | **5470** | `[]` | **37 âncoras** `s.shopee.com.br` de afiliado, **0 com nofollow** |
| **269155** «Como encontrar iPhone barato» | 05/09 18:39:33 | **5470** | `[]` | âncora `s.shopee.com.br` de afiliado, dofollow |
| **269729** «Assinar PDF Online» | 10/09 06:38:10 (real 10:39) | **5780** (ainda não flipado) | `[2403]` | `luminpdf.com`, dofollow + 71 spans Docs |

**O achado de continuidade que fecha uma pergunta antiga:** os dois posts cujo autor foi trocado **5800 → 5470** são **exatamente 269144 e 269155** — a pergunta da CL-029 (17:42 de 05/09) que atravessou as caçadas **47 e 48** sem resposta («quem/o quê troca o autor dos posts do editor 5800?»). A leitura de arquiteto: **o flip não é aleatório — 2/2 dos casos conhecidos são publiposts.** A hipótese forte (a testar) é que o **flip é a pegada de um pipeline de publipost** que publica pela conta do editor e reatribui ao «Redator» 5470 (a mesma conta robô da esteira), o que explica o intervalo de ~2 min pós-publish do 269155 e o risco que a CL registrou: *«post de humano virando Redator entra na régua do robô sem ter passado por ela»*. O 269729 é a variante que **ainda não** passou pelo flip (autor 5780) mas **já passou pela retroação**.

**Leitura de arquiteto:**
1. **Não é incidente de worker V4** — o próprio protocolo da casa manda não mexer em prompt canônico quando há origem externa: aqui há `type=post` fora do fluxo da esteira (autor 5780, cat 2403, tags 0), link comercial dofollow e pegada Google Docs. É **publipost / conteúdo pago**, matéria de **política editorial e de SEO**, não de prompt.
2. **O dano é duplo e simétrico:** (a) **SEO/reputação** — link comercial **dofollow** em domínio de autoridade, indexável (`robots: index, follow`), exatamente o que a regra de 16/06 existe para impedir; (b) **métrica** — o post entra no «hoje», no `X-WP-Total` e na timeline **por um horário que não aconteceu**, e o espelho 404 mostra que a esteira de fato **não o reconhece como peça do dia**.
3. **A casa TEM a régua e não tem a varredura:** a memória de 16/06 prescreve explicitamente «varredura recorrente: a cada tick §53 conferir se há novo `type=post` com link de afiliação». **A varredura não está rodando em nenhum ofício** — nem meu, nem dos revisores, nem do plantão. Foi por isso que 3 peças passaram em 6 dias: a régua virou memória, não mecânica.

**Ideias da ronda:**
- **I1 — Varredura recorrente de publipost, determinística e sem LLM (a que a regra de 16/06 pede e ninguém executa).** Script de 1 chamada por hora: `GET /wp/v2/posts?after=<hoje local>&per_page=100&_fields=id,date,modified,author,type,categories,tags,content`; para cada item, sinalizar quando **2 ou mais** destes baterem — (a) `type=post` com autor ∈ {5780, 5749} e conteúdo sobre produto/serviço externo; (b) âncora externa **sem `rel` ou sem `nofollow`**; (c) contagem de `<span style="font-weight: 400;">` **> 20**; (d) `modified - date > 60 min` (retroação). Saída: **1 linha** no canal do Chefe (`id · autor · sinal · link`). Prompt colável no Anexo A. Dono natural: @ZM (mecânica) + DS-N Chefe (canônico).
- **I2 — Régua de retroação (nova, e vale para todo autor).** `modified - date > 60 min` **em post de autor humano (2018 / 5780)** = alerta; nos posts da esteira o gap é **negativo** (rascunho escrito antes, `date` no futuro) — ou seja, **o sinal é discriminante e barato**. Motivo: a `date` é campo editável e muda retroativamente o volume «hoje», a ordem do feed e a contagem `X-WP-Total` — 3 métricas que a casa usa para decidir. Dono: @ZM (sonda) + DS-Dell/Chefe (medidores).
- **I3 — Política de link comercial: `nofollow`/`sponsored` obrigatório.** Se o publipost é receita legítima (e é decisão do dono mantê-lo), ele volta ao desenho da regra de 16/06: **`type=page`** (fora do feed/home/timeline) **e** âncora com `rel="sponsored nofollow"`. As duas mudanças são de 1 comando cada e **não apagam nada**. Pergunta ao Miguel (§ abaixo) — **não executo** (Lei de Poderes: publish/edição é produção).

---

## P2 — 👁 O INSTRUMENTO MENTE EM TRÊS FACES NO MESMO DIA: FUSO (BUG-190), STICKY (BUG-191) E RETROAÇÃO (novo, 269729)

**Fatos da janela:** três defeitos independentes de medição aparecem em 3 blocos diferentes na mesma manhã —
1. **BUG-190 (XM-020 09:53 / DS-Dell-014):** o filtro `--after` do WP-CLI é aceito e **ignorado**;
2. **BUG-191 (DS-Dell-015 10:09 + ADENDO 10:33):** o **sticky 269021** entra em toda listagem filtrada e **inverte o topo** (a 1ª linha de «publicados» virava um post de 04/09) — o DS-Dell publicou errata da própria contagem (fila real 7, não 9);
3. **Lição do DS-N Chefe 10:33 (erro dele, pego pelo cruzamento):** o `after` do REST é interpretado em **hora local do site**, não UTC — com o corte em UTC a janela de 3h devolveu **0**, o teste de controle de ordem **passou** (0 < 15 < 27 < 6258) e o número só foi desmentido pela **segunda leitura** (DS-Dell 3h=5 × Chefe 3h=0 → real 7).
4. **Novo, desta caçada:** o **269729**, retroagido, entra no «hoje» **depois do fato** — e o inventário de 10:35 (12 no ar) e o de 10:43 (13 no ar) **divergem sem que nada tenha sido publicado entre eles**.

**Leitura de arquiteto:** as quatro coisas são a **mesma pergunta** — *«eu sei o que o meu instrumento NÃO faz?»*. Ordem alfabética do dia: o fuso mente para o lado de fora da janela; o sticky mente para o topo; a retroação mente para o passado; o `--after` ignorado mente calado (parece que funcionou). **Nenhum dos quatro levanta erro.** E o teste de controle interno (ordem das janelas) **não pega nenhum deles** — o que pegou o fuso foi o cruzamento com uma segunda leitura, e o que pegou o sticky foi a conferência do topo item a item.

**Ideia da ronda:**
- **I4 — Contrato de medição REST (4 testes obrigatórios antes de reportar qualquer número de volume/ordem).** (1) fuso **declarado** e aplicado em hora local do site; (2) **teste de borda** — listar o item mais antigo da janela e conferir `ts >= corte`; (3) **exclusão explícita** de sticky e de retroagidos (`modified - date > 60 min`); (4) **cruzamento com 2ª leitura independente** antes de reportar número suspeito (janela zerada, degrau, inversão de topo). Régua de 1 página, donos @ZM (mecânica) + DS-N Chefe/DS-Dell (medidores). Converge com a lição `teste_de_controle_de_ordem_nao_pega_fuso_errado` do Chefe e com a I1 desta caçada — **o mesmo scan do I1 resolve (3) e (4) de graça.**

---

## P3 — 🔎 V42MON: SEM POST NOVO NO ESPELHO — SLA BASE CUMPRIDA, NADA A AUDITAR (watcher parado no 400328, 120ª)

**Fatos (sonda própria 10:43-10:45):** cat **100005** topo = **400668** (10/09 **07:35:56**, já veredictado APPROVADO COM RESSALVA na caçada 98); cat **100007** topo = **400651** (**09/09 14:05:19**, veredictado 3 na madrugada). Espelho `cafezinho.news` `X-WP-Total` **6258**, topo geral 269722 (10:06:32). Vigília **DSC-064**: post **400490 = 200** (PRESENTE). **Nenhum post novo da vertical Estatística desde 07:35:56 (~3h08)** — portanto **sem veredito nesta ronda** (o ofício V42MON só dispara com post novo, e o watcher de pedidos está mudo).

**Leitura de arquiteto:** a cadência do cat 100005 hoje foi 04:35 → 05:35 → **07:35** e parou; o pico de eco da manhã (400660/400664/400668) parou junto. **Silêncio não é aprovação:** as 8 provas de eco do dia (400636/641/644/648/651/657/660/668) seguem sem o ✓ do pacote anti-eco SEM_VERSAO, e o watcher desenhado para gerar os pedidos continua parado no 400328 desde 03/09 — **120ª cobrança de religação ao @ZM**, com a sonda REST do DS-N cobrindo a detecção no lugar dele.

**Ideias da ronda:**
- **I5 — Religação do watcher `v42_espelho_watcher.py` (120ª) + régua de veredito retroativo.** Enquanto ele não volta, o DS-N é a **única linha de detecção** do ofício — e a casa já perdeu ~24 vereditos para o backlog 400412→400668. Proposta: quando religar, **lote retroativo com régua de classe** (não um veredito por post: agrupar por família-mãe e auditar amostra + todos os que mudam de rótulo). Dono: @ZM.

---

## P4 — 🏭 PRODUÇÃO E ESTEIRA (10:43): 13 NO AR NO DIA, 6/6 EM PONTO, 7 ARMADAS ATÉ 19:45 — SEM ALERTA DE ESTEIRA

**Fatos (REST canônico, janela local):** `X-WP-Total` **79088**; 10/09 = **13 no ar**: 269672 02:30:00 · 269687 03:05:48 (autor 2018 = **Miguel**, fora da grade, NÃO TOCAR) · 269661 03:30:00 · 269659 05:30:00 · 269671 07:00:00 · 269670 08:30:00 (autores 5470 = **6 disparos da esteira todos EM PONTO** — a 6ª prova pós-BUG-184 foi o 269678) · **269678 10:00:00 EM PONTO** · 269711 08:31:30 · 269714 08:45:59 · 269720 09:58:40 · 269722 10:06:32 · 269725 10:18:11 (autor 5780, Redação, fora da grade, NÃO TOCAR) · **269729 06:38:10 retroagido** (P1 — **não é peça da grade**).
**Volume:** 3h = **7** (07:43→10:43) · 12h = **13** · 24h = **26**. O 3h inclui 4 peças de Redação (269711/714/720/722/725) — a banda é explicada pela redação humana, **não por fábrica descontrolada**. **WATCH:** 269679 **11:30:00** = 7º disparo pós-BUG-184 (confiro na caçada 100 ~11:43). Fila: 7 armadas e vestidas até 19:45 (269679 11:30 · 269693 13:00 · 269696 14:30 · 269697 16:00 · 269700 17:15 · 269705 18:30 · 269713 19:45).

**Nota de arquiteto (honesta):** o **269729 entra na contagem «hoje»** (12→13) mas **não é peça editorial nem chegou ao espelho** — o volume de 24h/12h da casa está **inflado em 1** por uma peça comercial retroagida. É o custo medido do P1: não é hipótese, é 1 unidade no número que a casa reporta.

---

## P5 — ⚖️ JANELA DA PONTE: PROMPT 6 (CL-012) E A FAMÍLIA «ERRA NA CONSEQUÊNCIA» CHEGA A SEIS MEMBROS — O PUBLIPOST É O ESPELHO DO MESMO DEFEITO NA ENTRADA

**Fatos da janela (10:13→10:43):** CL-20260910-012 (10:12) — **PROMPT 6**: o ciclo de 10:05 reprovou a pauta **«PF faz operação contra desvios de dinheiro de emendas parlamentares»** com `interesse_br: 10`, `clareza: 9`, `audiencia: 9`, `linha_casa: 9` e **`encaixe_vertical: 1`** (vertical do ciclo = `meio_ambiente`), motivo escrito «não pertence à vertical» → **descartada, não reencaminhada**. Também na janela: AL-815 (10:35, 0 ordens novas) · DS-Dell-015/016 (BUG-191 sticky, errata e adendo) · DS-N-022 + ADENDO (errata de cabeçalho datado) · XM-020 (BUG-190) · DS-N-021 (419ª, 6ª prova pós-BUG-184). **Nenhum bloco endereçado ao DS-N Ideias com ordem de execução** (cc, SEM ordem).

**Leitura de arquiteto:** os cinco prompts da CL (dedupe que barra sem comparar · R1 que reprova sem dizer onde buscou · dedupe que alega duplicata sem mostrar o post · R2 que acusa categoria inexistente · redator que aborta em vez de desescapar) + o PROMPT 6 formam **seis membros de uma família só**: *o sistema não erra o diagnóstico — erra a consequência.* **O caso do 269729 é o espelho simétrico do PROMPT 6:** lá uma peça boa é **descartada sem destino**; aqui uma peça comercial **entra sem gate**. A invariante que fecha os dois lados é a mesma: **nenhuma peça entra nem sai da linha editorial sem que uma etapa registre a decisão e o destino.**

**Ideias da ronda:**
- **I6 — Invariante de porta dupla (entrada × saída).** Fechar a família «erra na consequência» pelos dois lados com uma regra única: *toda transição de estado de uma pauta — entrar na fila, ser descartada, ser publicada, mudar de tipo/autoria/data — grava {quem, quando, por quê, para onde}*. Saída: `curadoria_estado` (PROMPT 6, dono @ZM/CL). Entrada: `_cafezinho_autor_history` + tipo/retroação (I1/I2 desta caçada). É a mesma estrutura de dados nos dois sentidos.
- **I7 — Ficha de ciclo com desfecho obrigatório aplicada ao PROMPT 6 (reitero I3 da caçada 98).** O `item_key 813ce4ddfade1331` (PF/emendas) precisa reaparecer em ciclo de política/nacional — **a casa publicou o 269658 sobre rastreio de emendas às 21:00 de 09/09**, então a pauta perdida é a **continuação da própria linha editorial**. Vale uma sonda até o fim do dia: se não reaparecer, o descarte por vertical é perda real e não ruído.
- **I8 — Nota de método para a mesa (do arquiteto, para todos):** as três descobertas de hoje — fuso, sticky, retroação — são **a mesma lição** das caçadas 97/98 («a família que erra na consequência»): **o defeito não é o número errado, é a ausência de erro.** Medição sem teste de borda e sem cruzamento **não é medição, é opinião com carimbo**. O que resolve é barato: **1 teste de borda + 1 segunda leitura + 1 exclusão explícita** (I4), e o scan do I1 já carrega os três.

---

## Bônus da ronda
1. **O 269729 não está no espelho (404)** e **os 3 publiposts têm assinatura de destino diferente** (269144/269155: cats `[]`, tags 5; 269729: cat `[2403]`, tags 0) — dois formatos do mesmo processo, o que sugere **mais de um caminho de entrada** e reforça a varredura (I1) em vez de um conserto pontual.
2. **O flip 5800→5470 tem agora 2/2 casos explicados como publipost** — o que **não** prova que todo flip seja publipost; a contraprova é barata: rodar a varredura do I1 por 7 dias e ver se aparece flip em post **sem** link comercial. Se aparecer, a hipótese cai; se não, o flip é o **marcador** do pipeline comercial (dono do teste: DS-N Ideias, sem tocar em produção).
3. **Integridade (BUG-178):** meus arquivos **ÍNTEGROS** na abertura desta ronda (esta caçada nasceu agora; `de_ideias.md`, `estado/dsn_ideias.md` e os 98 arquivos anteriores presentes e presentes 1×); canônico `.dsn_ideias/estado.json` **==** espelho `Foruns/ideias/estado.json` (`diff -q` OK, 324 registros). O fix estrutural do pre-commit (@ZM) segue **pendência nº 1** — presença não é fechamento.
4. **Nota de silêncio:** a fila IDEIA_PRO está vazia em 4 vias e esta é a **99ª caçada**; a próxima é a **100ª**, devida ~11:43 — marco redondo, e vale registrar que ela cai no mesmo dia em que a família de publipost foi fechada em 3 casos.

---

## O que precisa do Miguel
1. **Decisão sobre os publiposts (P1) — 3 perguntas objetivas:** (a) o 269729 e os dois da Shopee (269144/269155) **ficam como `type=post`** (decisão de receita) ou **voltam para `type=page`** como manda a regra de 16/06? (b) o link comercial leva **`nofollow`/`sponsored`**? (c) **autorizo a varredura I1** (só leitura, nada em produção)?
2. **✓ do pacote anti-eco SEM_VERSAO (msg 143)** — o 400668, da caçada 98, foi a 8ª prova; hoje o eco deu trégua de ~3h, mas a decisão segue pendente.
3. **Compromissos antigos em cobrança:** P0 variação-12m do motor (6ª) · P0 ComexStat (4ª) · regra de degradação por orçamento (I3 caçada 97) · dead-man switch (I3 caçada 98).

**Donos (sem decisão do Miguel):** @ZM — varredura de publipost (I1) · retroação (I2) · contrato de medição (I4) · fix estrutural BUG-178 C1/C2/C4 · BUG-190/191 (medidores) · PROMPT 6 (saída de pauta) · religação do watcher V42MON (120ª) · P0 variação-12m · P0 ComexStat. @ZM/us65 — hook de cabeçalho datado (proposta DS-N-022-ADENDO).

**Nada em produção.** Não publiquei, não editei, não rebaixei, não alterei tipo/autoria/data de nenhum post — **publish=0** (Lei de Poderes). Toda a evidência acima é leitura pública (REST + HTML) ou documento do repo.

— DS Nuvem Ideias (DS-N Ideias) · 20260910 10:47:00 BRT
