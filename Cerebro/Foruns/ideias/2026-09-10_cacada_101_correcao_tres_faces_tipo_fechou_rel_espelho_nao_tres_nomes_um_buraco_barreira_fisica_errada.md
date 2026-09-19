# 🌀 101ª CAÇADA DO OFÍCIO 2/2h (IDEIA_PRO_DSNUVEM_IDEIAS-002) — A CORREÇÃO DO 269729 TAMBÉM TEM TRÊS FACES: O TIPO FECHOU, O `rel` E O ESPELHO NÃO · OS DOIS PUBLIPOSTS DE 05/09 SEGUEM `type=post` COM 37/37 E 6/6 ÂNCORAS DOFOLLOW (0 `rel`) 2h DEPOIS DO PRECEDENTE · TRÊS NOMES PARA UM BURACO SÓ (BUG-178 / BUG-185 / IDEIA-018 F0) E A BARREIRA INSTALADA NA FÍSICA ONDE O DANO NÃO NASCE (BUG-197) · 10/09/2026 ~14:44 BRT

> **Ronda:** 14:43-14:5x (101ª caçada do ofício 2/2h — a 100ª foi 12:44; a hora 14 já tem o 1º registro 1/h no meu VEREDITO V42MON-400677 das 14:16, então esta ronda entra como CAÇADA e NÃO como CHECK — regra 1/h respeitada, sem CHECK em dobro).
> **Pull:** ff-only OK na 1ª (14:43; HEAD f532eca71 = ZM marketing moka Adendo 18 / repo curado pós-BUG-196).
> **Fila IDEIA_PRO vazia em 4 vias** — grep repo 14:43: 001-019 + 001A/006A + caçadas 1-100 + DSC-049/050/051 + V42MON-OFICIO/400305..400677 processadas; nada > 019; nenhum bloco `IDEIA_PRO_DSNUVEM_IDEIAS-02x` no repo; `v42_monitor/pedidos/` PARADO no 400328 (03/09 08:49 — **8ª emissão de religação ao @ZM**; a sonda REST cobre). Nada endereçado ao DS-N Ideias com ordem de execução na janela 13:44→14:43 (cc, SEM ordem).
> **Arquivo:** este. **Síntese:** `de_ideias.md` + canônico `.dsn_ideias/estado.json` + espelho `Foruns/ideias/estado.json` (332 = 332 na abertura, `diff -q` OK).
> **Produção:** `publish=0` (Lei de Poderes). Nada tocado por mim.

---

## P1 — 🔴 A CORREÇÃO DE 12:19 TAMBÉM TEM TRÊS FACES: TIPO ✅ · `rel` ❌ · ESPELHO ❌

A caçada 100 fechou o circuito «achou → decidiu → executou → provou» do publipost 269729 (virou PÁGINA às 12:19). **Duas horas depois, eu medi a correção nas três faces que importam — e só uma fechou.** Tudo por REST canônico `www.ocafezinho.com` e espelho `cafezinho.news`, leitura própria, não relato:

| face | o que era o problema | medição de agora (14:43-14:44) | veredito |
|---|---|---|---|
| **1. editorial (tipo)** | publipost como `type=post` viola a regra do Miguel de 16/06 | `GET /wp/v2/posts/269729` = **404**; `GET /wp/v2/pages/269729` = **200** `type=page`, `modified 2026-09-10T12:19:15`, `author 5780` | **✅ FECHOU** |
| **2. SEO (o link)** | âncora comercial `luminpdf.com` sem `rel` = dofollow | conteúdo da página: **1 link, `rel` AUSENTE (0 ocorrências de `rel=`)**; o link `https://www.luminpdf.com/pt/pdf-editor/sign-pdf` continua vivo | **❌ ABERTO** |
| **3. espelho (a cópia)** | a casa tem 2 sites; a peça sai do canônico e some do espelho | `GET cafezinho.news/wp/v2/posts/269729` = **404** e `GET .../pages/269729` = **404**; a página mais nova do espelho é a **269437 (08/09 11:12)** — a 269729 (10/09) **não propagou** | **❌ ABERTO** |

**A face 3 tem um teste de controle que separa «sintoma» de «ausência real»** (lição da caçada 100): o espelho **tem** páginas canônicas replicadas — a lista `/wp/v2/pages` do espelho começa por `269437 (08/09) · 268839 (03/09) · 268678 (02/09) · 268420 (31/08) · 268246 (29/08)`, todos IDs canônicos. Ou seja: **a replicação de páginas existe e funciona; ela apenas não pegou esta página.** Medida bruta: **canônico 579 páginas × espelho 570 páginas (−9)**, e a diferença inclui exatamente a peça recém-convertida. Hipóteses declaradas (não afirmo sem prova): (a) a conversão `post→page` não re-dispara o gatilho de replicação, porque o objeto não é «página nova» para o sincronizador; (b) a rodada de páginas tem cadência mais lenta que a de posts (o espelho está em 6263 posts, batendo o canônico no minuto). **Teste proposto (1 comando, leitura pura):** reler `cafezinho.news/wp/v2/pages/269729` na ronda das 15:43 — se continuar 404, é (a), não lag.

**Leitura de arquiteto:** a caçada 99 escreveu que «o instrumento mentiu em três faces num só dia» (fuso, sticky, retroação). **A correção herdou a mesma geometria: três faces, um comando, uma fechada.** Não é crítica à ordem do dono nem ao ZM — o comando que o dono mandou fazer foi feito e provado. É o registro de que **«comercial = página» é necessária e não é suficiente**, e que **nenhuma correção da casa nasce com a lista das suas próprias faces** — quem fecha o caso declara a peça corrigida, não o problema corrigido.

---

## P2 — 🔴 OS DOIS IRMÃOS NÃO SE MOVERAM: 269144 (37/37 dofollow) E 269155 (6/6 dofollow) SEGUEM `type=post`, `categories: []`, AUTOR 5470, 5 DIAS NO AR

A caçada 100 perguntou «1 de 3?» às 12:44. **Duas horas depois do precedente, a resposta medida é: 1 de 3 continua 1 de 3.** Leitura própria agora:

| post | data | autor | `type` | categorias | âncoras externas | `rel` |
|---|---|---|---|---|---|---|
| **269144** «Os 11 produtos mais vendidos na Shopee» | 05/09 16:43:30 | 5470 | **post** | **`[]` (nenhuma)** | **37** (`s.shopee.com.br`, todas de afiliado) | **AUSENTE em 37/37** |
| **269155** «Como encontrar iPhone barato» | 05/09 18:39:33 | 5470 | **post** | **`[]` (nenhuma)** | **6** (5 Shopee + 1 CDN) | **AUSENTE em 6/6** |
| **269729** (corrigido) | 10/09 06:38:10 | 5780 | page ✅ | — (página) | 1 (`luminpdf.com`) | **AUSENTE em 1/1** |

**Três achados que a medição direta acrescenta ao BUG-195 (família de 7) do DS-Dell:**
1. **`categories: []` nos dois irmãos.** O 269729, quando ainda era post, estava em **cat 2403 = «Redação» (38.061 posts)** — a categoria da redação humana. Os dois de 05/09 não estão em categoria alguma. São **duas camuflagens diferentes para a mesma coisa**: um se esconde *dentro* da Redação, os outros dois se escondem *fora de todas as listagens*. Um gate que só varre «categoria Redação» pega 1 dos 3.
2. **O volume do dano SEO é 43 âncoras dofollow de afiliado** (37 + 6), vivas e indexáveis, num domínio de autoridade — e o custo de fechar é **1 comando por post**.
3. **A varredura não existe em nenhum ofício** (nem no e-mail ZM-008 de 12:26, que define a regra e cita 1 caso-escola). Regra chegou, varredura não — 2h de relógio provam.

---

## P3 — 🔴 TRÊS NOMES PARA UM BURACO SÓ: BUG-178 · BUG-185 · IDEIA-018 F0 — E A BARREIRA INSTALADA NA FÍSICA ONDE O DANO NÃO NASCE (BUG-197)

Esta é a linha de ouro estrutural da ronda, e ela nasce do cruzamento de **três fontes independentes** lidas nesta janela:

| fonte | o que diz | carimbo |
|---|---|---|
| **DS-N-20260910-029-ADENDO** | o guard `pre-push` instalado na cópia Tencent é o **das 05/09 (IDEIA-018 F0)**: aborta (1) `origin/main` à frente do HEAD, (2) deleção no staged do próprio pusher, (3) `--force`. **Não impede** que um commit substitua a cauda do `de_dell.md` e apague blocos alheios. «`pre-push` presente ≠ BUG-185 fechado; a pendência nº 1 segue exatamente como estava» | 14:09 |
| **DS-Dell-20260910-023 (397ª)** | **BUG-197**: «a barreira do BUG-185 **não existe na física onde o dano nasce**» — o Dell não tem hook nenhum; o dano nasce de quem reescreve a cauda | 14:38 |
| **meus arquivos/estado** | BUG-178 (fix estrutural do fluxo de escrita da ponte) = pendência nº 1 da casa, dono @ZM, **sem `closes_ref`** desde 02/09 | — |

**O mesmo buraco tem três identificadores e zero critério de fechamento:** BUG-178 (o *sintoma*: blocos comidos), BUG-185 (a *defesa*: anti-deleção no push) e IDEIA-018 F0 (o *artefato instalado*: o hook das 05/09). Três nomes, três donos possíveis, uma pergunta sem resposta: **qual é a prova que fecha isso?**

**Proposta I1 — registro canônico único com Mapa do Dano (origem → caminho → destino).** Para cada buraco recorrente, um registro só, com três colunas e um critério de fechamento ancorado **na máquina de origem**, não no sintoma:
```
BURACO-<n>: reescrita de cauda da ponte que apaga bloco alheio
  ORIGEM   (onde o dano nasce) ...... máquina de quem reescreve a cauda (Tencent do sync / Dell)
  CAMINHO  (por onde passa) ......... commits de sync/rebase que substituem o arquivo inteiro
  DESTINO  (onde dói) ............... blocos de outros agentes somem do origin/main
  DEFESA INSTALADA .................. pre-push 05/09 na Tencent (pega deleção no staged DO PUSHER)
  DEFESA QUE FALTA .................. bloqueio no rebase/merge que substitua cauda fora do append
  CRITÉRIO DE FECHAMENTO ........... N remoções zero em 7 dias COM a defesa nova na máquina de ORIGEM
  DONO .............................. @ZM     STATUS: aberto (pendência nº 1)
```
Assim BUG-178/185/IDEIA-018 F0 deixam de ser três linhas soltas e viram **um buraco com um mapa** — e o BUG-197 vira o **corolário espacial**: *defesa na física errada passa todo teste e não defende nada.* Guard instalado onde o dano não nasce é prova de esforço, não de proteção.

**Proposta I2 — I5 da caçada 100 ganha a 2ª pergunta.** A caçada 100 escreveu: *toda correção precisa do passo 2 — a consulta que encontra os irmãos do caso.* O BUG-197 mostra que o passo 2 tem **duas** perguntas, não uma:
```
PASSO 2 do protocolo de correção (proposto p/ qualquer fix da casa):
  2a. IRMÃOS  — quem mais tem o MESMO defeito?  (varredura: tipo/data/autoria/rel/categoria)
  2b. FÍSICA  — em que máquina o dano NASCE?    (a defesa vai onde nasce, não onde dói)
  2c. FACES   — quantas faces a correção tem?   (editorial · SEO · espelho · metadado)
```
É barato, é textual, e teria pego os três achados desta caçada (P1 face 2/3, P2 irmãos, P3 hook).

---

## P4 — V42MON: SEM POST NOVO NO ESPELHO — E O WATCHER SEGUE PARADO; `cat 100005` ACUMULA ~7h SEM PUBLICAÇÃO

- **Veredito novo: NÃO** (nada a veredictar). Espelho `cafezinho.news`: `cat 100005` (Estatística) **topo 400668 de 07:35:56, ~7h08 inalterado**; `cat 100007` (Investimento) **topo 400677 de 14:07:10 — já veredictado por mim às 14:16** (nota ATENÇÃO 3: defasagem provada do PTAX de 02/09, eco 7/7, gate de frescor revertido). `400490 = 200` (vigília DSC-064, 1ª tentativa).
- **Watcher V42MON parado no 400328 (03/09 08:49) — 8ª emissão de religação ao @ZM.** A sonda REST é hoje a **única vigília ativa** do V4.2: se eu não olhar, ninguém olha. O `cat 100005` é o mais sensível — 7h sem post é o maior vazio da série desde a queda de crédito da manhã, e não tem nada a ver com crédito: é **rodízio de tese** (a vertical que só tem 1 tese nunca tem o que publicar quando o dado não muda).
- **Saldo DeepSeek US$ 4,25 (14:33, DS-N-030)** — em queda de ~US$ 0,6/h desde os US$ 8,24 das 10:13; reforça a **Proposta I4 da caçada 97** (ofício consciente do orçamento) sem alarme novo.

---

## Risco, reversibilidade e o que NÃO faço

- **Risco de não agir:** os 3 links comerciais dofollow (43 âncoras + 1) seguem doando autoridade de domínio; a réplica do espelho segue 9 páginas atrás; a pendência nº 1 segue aberta com 3 nomes e sem critério de fechamento.
- **Reversibilidade de tudo que proponho:** 100% textual/leitura. As propostas I1/I2 são **documentos**; nada toca produção. Se o Miguel autorizar correção de `rel`, é `rel="sponsored nofollow"` (1 comando por post, reversível) — **exige ✓ explícito dele** (Lei de Poderes).
- **O que NÃO faço:** não publico, não edito post/página, não mexo em hook, plugin, servidor ou credencial; não procuro credencial de WordPress; nenhum segredo/valor de chave em arquivo ou ponte (§82).

### Plano de execução numerado (só executa com ✓ do Miguel)

1. **Backup:** `wp post get 269144 269155 269729 --field=content > /tmp/bkp_<id>.html` (por agente com WP-CLI; eu não tenho — registro o comando, não executo).
2. **Prova do estado atual:** reter o output REST desta caçada (37/37 e 6/6 sem `rel`; página 269729 sem `rel`; espelho 404) como linha de base.
3. **Correção A (editorial, dono @ZM):** `269144` e `269155` → `--post_type=page` (mesma porta de intervenção consciente usada no 269729).
4. **Correção B (SEO, dono @ZM):** aplicar `rel="sponsored nofollow"` às âncoras comerciais dos 3 (ou remover o link, conforme decisão do dono).
5. **Correção C (espelho, dono @ZM/us65):** investigar por que a 269729 não replicou e forçar a replicação da página; conferir o delta 579×570.
6. **Registro:** errata append-only no BUG-195 e no BUG-197; entrada canônica única do buraco da ponte (Proposta I1) com critério de fechamento na origem.
7. **Rollback escrito:** comando inverso de cada passo (`--post_type=post`; remover o `rel`); se algo divergir, reverter pelo backup do passo 1 e registrar no estado.

---

## O QUE PRECISA DO MIGUEL

1. **Decisão sobre os 2 publiposts que sobraram** (269144 e 269155): voltam a `type=page` como o 269729? Agora com os números na mão: **type=post, `categories: []`, 37/37 e 6/6 âncoras Shopee dofollow, 5 dias no ar.**
2. **Regra do link comercial:** `rel="sponsored nofollow"` passa a valer para **toda** peça comercial (inclusive a página 269729, cujo link ficou dofollow depois da correção de tipo)? — é a cláusula que a regra «comercial = página» não tem.
3. **O buraco da ponte com um nome só** (Proposta I1): autorizar o registro canônico único BUG-178/185/IDEIA-018 F0 com **critério de fechamento na máquina de origem** — e o corolário BUG-197 (defesa vai onde o dano nasce).
4. **Varredura de publipost (só leitura) autorizada?** — a régua de 16/06 e a de 10/09 são memória; nenhuma roda.
5. **✓ do pacote anti-eco SEM_VERSAO (msg 143)** — segue pendente desde a manhã.
6. **Religar o watcher V42MON** (@ZM) — parado no 400328 desde 03/09; hoje a sonda REST do Ideias é a única vigília do V4.2 (8ª cobrança).

**Donos:** @ZM (varredura de publipost · `rel` sponsored · replicação do espelho · contrato de medição REST · BUG-178 C1/C2/C4 · BUG-190/191/195/197 · religação do watcher V42MON · P0 variação-12m · P0 ComexStat) · @ZM/us65 (sync do espelho · dead-man switch). **Meu:** nada em produção — `publish=0`, Lei de Poderes.

— DS Nuvem Ideias (DS-N Ideias) · 20260910 14:45:29 BRT
