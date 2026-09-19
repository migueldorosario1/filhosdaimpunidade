# 🌀 100ª CAÇADA DO OFÍCIO 2/2h (IDEIA_PRO_DSNUVEM_IDEIAS-002) — A ORDEM DO DONO EXECUTOU O QUE A CAÇADA 99 APONTOU (269729 virou PÁGINA às 12:19) · MAS 1 DE 3: OS DOIS PUBLIPOSTS DE 05/09 SEGUEM `type=post` COM 37 E 6 ÂNCORAS DE AFILIADO DOFOLLOW · E O LINK COMERCIAL SOBREVIVEU À CORREÇÃO (a metade SEO ficou de fora) · O ESPELHO AINDA NÃO TEM A PÁGINA (404, com teste de controle) · V42MON SEM POST NOVO — 10/09/2026 ~12:44 BRT

> **Ronda:** 12:43-12:5x (100ª caçada do ofício 2/2h — a 99ª foi 10:47; a hora 12 já tem CHECK às 12:14, então esta ronda entra como CAÇADA e NÃO como CHECK — regra 1/h respeitada).
> **Pull:** ff-only OK na 1ª (12:43; HEAD 2fe41b42c = LEDGER Lote 10 / faxina ZM 12:4x).
> **Fila IDEIA_PRO vazia em 4 vias** — grep repo 12:43: 001-019 + 001A/006A + caçadas 1-99 + DSC-049/050/051 + V42MON-OFICIO/400305..400668 processadas; nada > 019; `v42_monitor/pedidos/` PARADO no 400328 (03/09 08:49 — 121ª cobrança de religação ao @ZM); nenhum bloco `IDEIA_PRO_DSNUVEM_IDEIAS` novo em `de_dell.md`/`de_laura.md`/`de_ideias.md`.
> **Arquivo:** este. **Síntese:** `de_ideias.md` + canônico `.dsn_ideias/estado.json` + espelho `Foruns/ideias/estado.json` (328 = 328, `diff -q` OK na abertura).
> **Produção:** `publish=0` (Lei de Poderes). Nada tocado por mim.

---

## P1 — ✅ A CAÇADA 99 ACHOU, O DONO DECIDIU, O ZM EXECUTOU: O 269729 VIROU PÁGINA — E EU VERIFIQUEI POR MIM, NÃO POR RELATO

**O que aconteceu (janela 12:14→12:43, lida em `de_laura.md` e `de_dell.md`):** o publipost que a **minha caçada 99** isolou às 10:47 («Assinar PDF Online», `type=post`, link comercial dofollow, 71 spans Google Docs, retroagido 4 h) **saiu da lista de posts por ordem direta do Miguel no chat do ZCode**:

| bloco | quem | o que | carimbo |
|---|---|---|---|
| **ZM-20260910-006** | ZM (ZCode/Qwen) | avisa que o 269729 é conteúdo promocional e «não é meu para gatear» | 12:15 |
| **ZM-20260910-007** | ZM | `wp post update 269729 --post_type=page` — **1ª tentativa BLOQUEADA pelo mu-plugin cafezinho-protecao-editorial (motivo=`post_publicado_por_humano`)**, liberada pela porta `CAFEZINHO_EDITORIAL_HUMAN_OVERRIDE=1` (a ordem do dono É a intervenção consciente) | 12:22 |
| **ZM-20260910-008** | ZM | e-mail ao Gabriel ENVIADO: «conteúdo comercial entra como PÁGINA, não como post» — notícia/editorial = post; comercial/promocional/serviço de terceiros = página | 12:26 |
| **DS-N-20260910-026** | DS-N Chefe | o «14→13» **não é perda**: o 269729 saiu da lista de POSTS | 12:30 |
| **DS-Dell-20260910-020** | DS-Dell | fecha o BUG-192 **no mérito por decisão do dono, não por código** | 12:34 |

**Minha verificação independente (REST canônico `www.ocafezinho.com`, 12:43-12:44) — não aceitei o relato:**

| prova | resultado |
|---|---|
| `GET /wp/v2/posts/269729` | **404** (não é mais post) |
| `GET /wp/v2/pages/269729` | **200** · `type=page` · `date 2026-09-10T06:38:10` · `modified 2026-09-10T12:19:15` · autor **5780** · link `.../assinar-pdf-online-solucoes-praticas-para-documentos-digitais/` |
| `X-WP-Total` dos posts | **79090 → 79089** (−1) |
| posts de 10/09 (`after=2026-09-10T00:00:00`) | **13** (era 14 com o 269729) |
| HTML da página nova | responde 200 e o link comercial **continua lá** |

**Leitura de arquiteto — o acerto e o resto:**
1. **O circuito funcionou de ponta a ponta e é a prova de valor da caçada:** a caçada 99 isolou a peça às 10:47 (com `type`, autoria, retroação, âncora e pegada Docs) → o dono decidiu → o ZM executou às 12:19. **Da detecção à correção: ~1 h 32 min.** Nada disso teria nome se a régua de 16/06 tivesse continuado só como memória.
2. **O guard da casa funcionou como desenhado:** a proteção editorial **bloqueou** a mudança de tipo de um post publicado por humano — e a mudança só passou pela **porta de intervenção humana consciente** que o próprio plugin prevê. **Registrar: o §130 provou-se em produção, com ordem do dono como chave.**
3. **Mas o conserto é de UMA peça, não da classe** — e é aqui que esta caçada avança a 99 (P2).

---

## P2 — 🔴 O QUE A ORDEM NÃO ALCANÇOU: OS OUTROS DOIS PUBLIPOSTS (05/09) SEGUEM `type=post`, COM 37 E 6 ÂNCORAS DE AFILIADO DOFOLLOW

A régua da caçada 99 achou **3 publiposts em 6 dias**. O dono corrigiu **o mais novo**. **Os outros dois continuam exatamente como estavam** — e eu conferi um por um agora:

| post | data | autor | `type` atual | âncoras externas | `rel` das âncoras |
|---|---|---|---|---|---|
| **269144** «Os 11 produtos mais vendidos na Shopee» | 05/09 16:43:30 | 5470 | **post** | **37** (`s.shopee.com.br`, de afiliado) | **AUSENTE em 37/37** |
| **269155** «Como encontrar iPhone barato» | 05/09 18:39:33 | 5470 | **post** | **6** (`s.shopee.com.br` + 1 CDN) | **AUSENTE em 6/6** |
| **269729** (corrigido) | 10/09 06:38:10 | 5780 | **page** ✅ | 1 (`luminpdf.com`) | **AUSENTE — o link sobreviveu** |

**Duas conclusões que só a verificação direta dá:**
1. **A regra chegou, a varredura não.** O e-mail ao Gabriel (ZM-008) **define a regra** e cita **um caso-escola**; não existe — em nenhum ofício — o passo que **procura os outros casos**. Se a regra de 16/06 já pedia «varredura recorrente a cada tick §53», a de 10/09 pedia a mesma coisa por outro caminho: **as duas viraram memória, nenhuma virou mecânica.** Os dois posts de 05/09 estão no ar, indexáveis, com **43 âncoras comerciais dofollow somadas**.
2. **A correção de tipo NÃO corrigiu o link.** O 269729 virou página — bem feito, saiu do feed, da home, do volume do dia e da timeline — mas a âncora `luminpdf.com` **continua sem `rel`**, ou seja, **segue dizendo ao Google «passe autoridade por este link»**. **A metade do problema que a ordem do dono resolveu foi a editorial; a metade SEO ficou intacta.** Não é crítica à decisão (a ordem foi clara e foi cumprida): é o registro de que **a regra prática «comercial = página» é necessária e não é suficiente** — falta a segunda cláusula, que é a do `rel`.

**Por que isso importa mais do que parece:** o dano SEO não é teórico. O Cafezinho é domínio de autoridade e os 3 posts estão em `robots: index, follow`; 43 âncoras dofollow de afiliado num site de notícia é exatamente a assinatura que a régua de 16/06 foi escrita para impedir, e **cada dia no ar é um dia de link equity doado**. O custo de corrigir é de **1 comando por post** (`rel="sponsored nofollow"` ou o retorno a `type=page`), e **não apaga nada**.

---

## P3 — 🪞 O ESPELHO AINDA NÃO TEM A PÁGINA — E EU FIZ O TESTE DE CONTROLE PARA NÃO CONFUNDIR SINTOMA COM PROVA

O ZM-007 previu: «o espelho replica na próxima sync (o sync inclui `post_type=page`)». **Até as 12:44 ele não replicou.**

| sonda | resultado | leitura |
|---|---|---|
| espelho `GET /wp/v2/posts/269729` | **404** | esperado (deixou de ser post) |
| espelho `GET /wp/v2/pages/269729` | **404** | **a página não chegou** |
| **CONTROLE:** espelho `GET /wp/v2/pages?per_page=2` | **200 · X-WP-Total 570 · ids 269437, 268839** | **o endpoint existe e serve páginas** → o 404 do 269729 **é ausência real, não sintoma** |

**Régua aplicada (XM-027):** um 404 só é prova quando o mesmo endpoint responde 200 para outro objeto da mesma classe. **Aqui responde.** Portanto: o espelho está, neste instante, com **a página fora** enquanto o canônico já a serve — divergência canônica↔espelho **de conteúdo editorial** (não de posts), que se resolve na próxima rodada do sync; **se não resolver, é caso para o dono do sync (us65/ZM)**. Registro, não alarme — a janela entre a edição (12:19) e a sync é normal.

**Estado do espelho (12:44):** `X-WP-Total` posts **6260** (era 6259 às 12:14, +1); `400490` = **200** (vigília DSC-064, presente na 1ª tentativa); hoje no espelho (posts `after=10/09`) = **17**, sendo **13 do canônico espelhados + 4 da vertical V42MON** (400657 · 400660 · 400664 · 400668).

---

## P4 — 📊 A CASA NO SLOT E O V42MON (sem veredito novo — e por quê)

**Produção canônica (REST próprio, 12:43):** `X-WP-Total` **79089** · topo **269679** «Netanyahu processará o Haaretz por reportagem sobre alerta antes do 7 de Outubro» **11:30:00**, autor 5470 = **7º disparo pós-BUG-184, 6º no minuto** · **10/09 = 13 no ar** por autor: **5470 = 7** (269672 02:30 · 269661 03:30 · 269659 05:30 · 269671 07:00 · 269670 08:30 · 269678 10:00 · 269679 11:30) + **5780 = 5** (269711 08:31:30 · 269714 08:45:59 · 269720 09:58:40 · 269722 10:06:32 · 269725 10:18:11) + **2018 = 1** (269687 03:05:48, Miguel, **fora da grade, NÃO TOCAR**) = 7+5+1 = **13 ✓** (o 269729 saiu da conta por ser página).
**Esteira:** **8 armadas e vestidas** até 22:15 — 269693 13:00 · 269696 14:30 · 269697 16:00 · 269700 17:15 · 269705 18:30 · 269713 19:45 · 269727 21:00 (gate CL) · 269735 22:15.
**Volume 3h (09:44→12:44):** 269720 · 269678 · 269722 · 269725 · 269679 = **5, dentro da banda diurna 4-6** (sem alerta; a regra só alerta para baixo). 12h = 13 · hoje = 13.
**V42MON:** cat 100005 topo **400668** (10/09 07:35:56, `modified` idêntico ao `date` — **não foi retocado**) e cat 100007 topo **400651** (09/09 14:05:19) — **INALTERADOS**. `X-WP-Total` cat 100005 = 38 · cat 100007 = 6. **Sem post novo no espelho = sem veredito novo nesta ronda** (os SLAs base seguem cumpridos; o último veredito foi o 400668 na caçada 98).
**BUG-178 (pendência nº 1 da casa):** os meus arquivos estão **ÍNTEGROS na abertura** — caçadas 98 e 99 presentes 1×, `de_ideias.md` íntegro 1×; canônico == espelho (328 registros, `diff -q` OK). Na janela houve a **23ª remoção** (commit `e9a59a55d`): caíram o `DS-N-20260910-025` e o `DS-Dell-20260910-019` — **nenhum meu**; ambos os donos restauraram com prova (XM-025 preservou texto+SHA-256). **O guard `pre-push` corrigido/testado (BUG-185) continua sem instalação — presença não é conserto.**
**Contexto de medição (registro honesto, não é meu achado):** o FAROL fez **343 → 1.145 → 1.582 → 2.011** com GA4/LUMINA/SOL parados — **3 leituras altas sem confirmação do tripé** (família do contador de 30 min, precedente 03/09). Não declaro onda. E **BUG-194 (DS-Dell):** o sintoma «filesystem read-only» era **política de sessão, não disco** — **é a MESMA família do meu passo 6**, onde o write em `~/dsn_ideias/estado.json` é negado por estar fora do workspace (12ª medição nesta ronda).

---

## 💡 IDEIAS DA RONDA (100ª caçada)

**I1 — Varredura de publipost: agora ela é trivial, porque a regra virou explícita.** Com a cláusula de 10/09 («comercial/promocional/serviço de terceiros = página») escrita, o detector deixa de exigir juízo editorial e passa a ser **conferência de tipo**: `GET /wp/v2/posts?after=<hoje-7d>&per_page=100&_fields=id,type,date,author,content` → sinalizar post quando **2+** destes baterem: (a) âncora externa **sem `rel`**; (b) `>20` spans `<span style="font-weight: 400;">`; (c) `modified - date > 60 min`; (d) 0 tags e categoria única «Redação». **Achado de hoje = o teste que reprova:** rodar a régua sobre 05/09→10/09 tem de devolver **269144, 269155 e 269729**. 269729 agora é página (não deve aparecer); **269144 e 269155 devem** — e é essa a fila. **Prompt colável no Anexo A.** Dono: @ZM (mecânica) + DS-N Chefe (canônico).
**I2 — A segunda cláusula da regra: `rel="sponsored nofollow"` obrigatório em âncora comercial, seja post ou página.** A ordem do dono tirou o 269729 do feed, mas o link segue dofollow. **A regra de 16/06 e a de 10/09 ficam incompletas sem esta cláusula** — e ela é a única que trata o dano SEO, que o `type=page` não trata. Custo: 1 comando por caso. **Decisão do dono** (não executo).
**I3 — O tipo é a metade visível; o `rel` é a metade invisível — e os medidores da casa só olham a visível.** Nenhum dos nossos instrumentos (volume, grade, X-WP-Total, sticky, retroação) enxerga `rel`. **Sugestão de instrumento mínimo:** 1 chamada/semana listando âncoras externas sem `rel` em posts do dia/semana, no canal do Chefe.
**I4 — O ciclo «achado → decisão → execução → mas só do caso» tem nome e vale generalizar.** Em 24 h: 269729 (achado pela caçada 99, corrigido) e 813ce4dd/PF-emendas (pauta perdida, corrigida por prompt 6 — e ainda **sem prova no jornal**). **Invariante proposta:** toda correção nasce com **dois passos** — (1) o caso concreto; (2) **a consulta que encontra os irmãos do caso** e devolve a lista. **Sem o passo 2, a casa conserta o exemplo e mantém a classe.** É a mesma forma do BUG-183/188/178: o conserto pontual sem a varredura que prova a classe.
**I5 — BUG-194 (DS-Dell) e o meu passo 6 são o mesmo bug de plataforma, e agora estão medidos em duas físicas:** o sintoma «read-only» tem **duas causas com a mesma cara** (disco × política de sessão) e o diagnóstico honesto exige **o recibo da falha** (kernel/`dmesg` para disco; teste de escrita fora do workspace para política). **Proposta:** declarar a política de arquivos da sessão em 1 linha na abertura da ronda — e manter o **caminho de escrita de primeira classe dentro do workspace** (é o que me salva: o estado durável é o repo, não o `~/dsn_ideias`).

---

## 🧷 O QUE PRECISA DO MIGUEL (decisão — não executo)

1. **Os dois publiposts que sobraram (decisão de mérito):** o 269144 (Shopee, 37 âncoras dofollow) e o 269155 (Shopee, 6) **ainda são `type=post`**, de 05/09. **Voltam a `type=page` como o 269729?** (a regra que o senhor promulgou ontem por ordem, hoje aplicada a 1 de 3).
2. **A segunda cláusula:** o link comercial leva `rel="sponsored nofollow"`? O 269729, já como página, **continua com o link dofollow** — a correção foi de vitrine, não de SEO.
3. **✓ do pacote anti-eco `SEM_VERSAO`** (msg 143) — segue de pé; o 400668 era a 8ª prova.
4. **Compromissos em cobrança (donos, não decisão):** @ZM — guard `pre-push` (BUG-178/185, pendência nº 1), varredura de publipost (I1), religar o watcher V42MON (parado no 400328 desde 03/09), P0 variação-12m (6ª), P0 ComexStat (4ª), regras de emenda do gate pós-17h (autorização pedida à CL, ZM-006-AUTORIZACAO); @ZM/us65 — sync do espelho (a página 269729 fora) e heartbeat/dead-man switch.

---

## ANEXO A — PROMPT COLÁVEL: VARREDURA DE PUBLIPOST (a que a régua de 16/06 pede e ninguém executa)

> **Problema:** a casa tem a régua de publipost desde 16/06 (`feedback_publipost_so_como_page_nao_post.md`: «publipost NUNCA como `type=post`, só como `page`»; conta recorrente `au=5780`, conta legítima `au=5749`) e a ampliou em 10/09 (e-mail ao Gabriel: notícia/editorial = post; comercial/promocional/serviço de terceiros = página). **Nenhuma varredura roda** — em 6 dias passaram 3 peças (269144, 269155, 269729) e a classe só foi tratada caso a caso. Prova: hoje o 269729 foi convertido a `page` por ordem do dono e **os outros dois seguem `type=post`**.
> **Solução:** script de 1 chamada por hora, sem LLM: `GET /wp-json/wp/v2/posts?after=<hoje-7d>&per_page=100&_fields=id,type,date,modified,author,categories,tags,content`. Sinalizar (2+ critérios): (a) âncora externa **sem `rel` ou sem `nofollow`** no conteúdo; (b) `>20` ocorrências de `<span style="font-weight: 400;">`; (c) `modified - date > 60 min`; (d) `tags` vazio e categoria única de Redação. Saída: **1 linha** por peça no canal do Chefe (`id · autor · sinal · type · link`). **Sem publicar, sem editar nada** — só leitura.
> **Teste que reprova (colar a saída):** rodar sobre `after=2026-09-05` → **TEM de listar 269144 (37 âncoras) e 269155 (6 âncoras)**; **NÃO pode listar 269729** (já é `page`); rodar sobre `after=2026-09-08` → **0 linhas** (controle negativo).
> **Pronto quando:** os 3 resultados acima aparecem colados e a entrada horária está no cron do host.

---

*Ronda 100 do ofício 2/2h. Pesquisa: repo (`cerebro/Foruns/`, ponte dos dois canais, memórias `claude_memory`) + sonda REST própria no canônico e no espelho. **Nada executado em produção — `publish=0`, Lei de Poderes.** Sem segredos (§82).*
