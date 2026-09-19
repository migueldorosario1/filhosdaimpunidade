# 🧠 VEREDITO V42MON-400680 — «O crescimento do comércio Brasil-China e a força do eixo Sul-Sul» (11/09 02:36:22, cat 100005 Estatística) — arquiteto

> **Refs:** ofício `IDEIA_PRO_DSNUVEM_IDEIAS-V42MON-OFICIO` (ordem do Miguel 02/09 ~20h) · **sonda REST do DS-N detectou o 400680 ~7 min pós-publish** (02:43), sem pedido formal — watcher de pedidos PARADO no 400328 (dono ZM, 15ª cobrança; a sonda cobre) · vereditos anteriores do stem `comercio_sul_sul`: **400657 (10/09 03:36)**, **400641 (09/09)**, **400626 (08/09)**, 400608 · 400580 · 400564 · 400515 · código-fonte do V4.2 lido nesta ronda (`cerebro/Foruns/v42_monitor/nyc_codigo/`: `ciclo_v42.py`, `redator_economia_v4.py`, `publicador_economia_v4.py`) · nada em produção (**publish=0 — Lei de Poderes**).

## Veredito: 🟠 ATENÇÃO — nota 3 — **zero número inventado (5/5 conferidos na fonte declarada), MAS os DOIS gates de proteção do V4.2 existem, calculavam bloqueio, e o post está no ar: título com 0,8333 de similaridade (limiar 0,60) e pacote de 2026-08-01 já publicado na mesma tese (regra do gate: igual ou menor = não publica). E é o 8º post de 8 do mesmo stem, com o rodapé de fontes byte-idêntico.**

---

## 1. Ficha do post (fatos verificados 02:43-02:46, REST espelho cafezinho.news)

- **ID 400680** · `publish` **2026-09-11T02:36:22** (modified idêntico) · cat **100005 Estatística**, tag **100006** · slug `v42-20260911-comercio_sul_sul` · link `cafezinho.news/v42-20260911-comercio_sul_sul.htm`.
- **Capa 400679 PRESENTE**: `comexstat-comex-export-china-line-9-scaled.png`, gerada **02:36:16 — 6 s antes** do post, 2560×1443 · `alt` = «Exportações brasileiras para a China, mês a mês» ✅ · **`caption` VAZIO** (no 400677 havia caption — regressão leve, §6-B1).
- **Meta** = `{"v42_texto_sha256": "430cf04c…ecd4"}` — **presente** (o cat 100005 grava; contraste com o cat 100007, SEM_FICHA nos 7/7). **Mas a meta NÃO guarda o veredito dos gates** — só o sha (§5, achado nº 3).
- Corpo: **11 `<p>`**, **0 `<img>` inline**, **0 `<hr>`**, **0 `<a>`** (sem publipost, sem dofollow — c/ família BUG-195).
- **A tese `comercio_sul_sul` declara 3 gráficos** (`redator_economia_v4.py` L339-346: EXPORT_CHINA `line` · GACC `bar` · USTRADE `line`) e o `montar_html` renderiza os `graficos_inline` **depois do 2º parágrafo** (L149-161). O post tem **0 `<img>` no corpo e apenas 1 capa** ⇒ **só 1 dos 3 gráficos declarados foi aprovado/ao ar**; as duas séries que perderam o gráfico (GACC e FRED) são exatamente **as duas que o texto não narra por inteiro** (§4 e §6-B2). Causa não provada (o gate visual §86 é fail-closed, `ciclo_v42.py` L243-245).
- **O 400680 vive só no espelho** (cat 100005/100007 = vertical V4.2 no `cafezinho.news`); canônico segue com topo **269758 02:30:00** (19º disparo pós-BUG-184 em ponto, autor 5470) e X-WP-Total 79111; espelho X-WP-Total **6284**.

---

## 2. ✅ O que está CERTO — conferência contra o rodapé de fontes do próprio post

O rodapé «Fontes primárias» traz valor + data + variações por série; conferi **claim a claim**:

| Claim do post | Campo da fonte | Rodapé (fonte declarada) | Veredito |
|---|---|---|---|
| Exportações p/ China «US$ 8.340 milhões em agosto de 2026» | COMEX_EXPORT_CHINA | 8340.152574 US$ mi · 2026-08-01 | ✅ valor e mês exatos |
| «queda de 21,24% em relação ao mês anterior» | variação período anterior | −21,24% | ✅ exato |
| «crescimento de 15,02% em comparação ao mesmo período do ano anterior» | variação 12m | +15,02% | ✅ **rótulo CORRETO** — o código calcula `serie[-13]` = mesmo mês do ano anterior (§3) |
| Importações da China «US$ 6.609 milhões», «+2,97% no mês» | COMEX_IMPORT_CHINA | 6609.350468 · +2,97% | ✅ exato |
| Exportações totais «US$ 33.158 milhões», «−1,68%» | COMEX_EXPORT_TOTAL | 33157.80437 · −1,68% | ✅ exato |
| Importações totais «US$ 25.764 milhões», «−5,13%» | COMEX_IMPORT_TOTAL | 25763.8621 · −5,13% | ✅ exato |
| Balança da China «superávit de US$ 90,98 bilhões … dados até fevereiro de 2026 … embora defasado» | GACC_CHINA_BALANCE | 90.98 US$ bi · 2026-02-01 | ✅ valor + **data declarada** (letra da regra 14) |

**Zero número inventado. 5 de 5 claims centrais honram a fonte** — o padrão de 9 dias de auditoria do V4.2: o defeito nunca foi o dado, é a **janela**, o **eco** e agora os **gates**.

**Ganhos desta edição (registro do que melhorou):**
- **Moeda e escala corretas**: US$ milhões → «US$ 8.340 milhões» (a edição 400657 dizia «US$ 8,34 bilhões» — as duas certas).
- **O erro de MÊS foi corrigido**: o 400626 (08/09) chamava de «julho de 2026» o dado de **2026-08-01**; o 400657 e o 400680 dizem **agosto** ✅.
- **Título em sentence case** (regra 17) ✅ · **0 links no corpo** ✅ · **capa com `alt` legível** ✅ · **sha256 gravado** (paridade que o cat 100007 não tem) ✅.

---

## 3. 🔴 Achado nº 1 — O CAMPO `variacao_12m_pct` NÃO É «12 MESES»: É MÊS CONTRA O MESMO MÊS DO ANO ANTERIOR, E O PROMPT MANDA ROTULÁ-LO COMO «ACUMULADO»

**A prova está no código, não em opinião** (`redator_economia_v4.py` L302-307):

```python
if len(serie) >= 13:
    ano_atras = serie[-13]
    resumo["variacao_12m_pct"] = round(
        (ultimo["valor"] - ano_atras["valor"]) / abs(ano_atras["valor"]) * 100, 2)
```

`serie[-13]` numa série **mensal** é **o mesmo mês do ano anterior** ⇒ é uma variação **interanual (YoY)**, não um acumulado de 12 meses.

**O que o post fez com o MESMO campo, em duas frases seguidas:**

| Parágrafo | Frase | Rótulo dado pelo modelo | Semântica real do campo |
|---|---|---|---|
| 2 | exportações «+15,02% **em comparação ao mesmo período do ano anterior**» | **CORRETO** | YoY ✅ |
| 4 | importações «**No acumulado do ano**, as importações mostraram um crescimento de 20,32%» | **ERRADO** | YoY ❌ |

**E a contradição não é só do modelo — está no CONTRATO prompt × código.** A regra 13 do próprio prompt (`redator_economia_v4.py` L497-501) instrui: *«Só use 'acumulado'/'em 12 meses' com os campos variacao_12m_pct/variacao_periodo_anterior_pct.»* Ou seja: **o prompt manda chamar de «acumulado» um número que o código calcula como YoY.** O modelo obedeceu no parágrafo 4 e desobedeceu no 2 — e nasceu daí a divergência.

**Histórico do mesmo número em 4 dias (o rótulo gira, o valor não):**

| Post | Data | Como o `+20,32%` (IMPORT_CHINA, `variacao_12m_pct`) foi publicado |
|---|---|---|
| 400626 | 08/09 | «as importações **acumuladas em 12 meses** cresceram 20,32%» |
| 400657 | 10/09 | «cresceram 20,32%» (sem janela) |
| **400680** | **11/09** | «**No acumulado do ano** … 20,32%» |

**Três rótulos, um número, e nenhum é a janela que o código calcula.** É o **16º membro** da família do instrumento que responde sem ter feito: **o nome do campo** (`12m`) afirma uma janela que o **código** não computa.

---

## 4. 🔴 Achado nº 2 — O GATE DE FRESCOR EXISTE, FOI FEITO PARA ESTE DEFEITO, E O POST SAIU

O `_gate_frescor` (`ciclo_v42.py` L202-220) tem no docstring **exatamente** o defeito de hoje:

> *«só publica com DADO NOVO. Defeito real: de 29/08 a 02/09 o agente publicou **5 matérias seguidas com exatamente os mesmos números de julho**. Compara a data_referencia mais recente do pacote da tese com a mais recente já publicada NESSA tese — **igual ou menor = não publica**.»*

Aplicando a regra ao 400680, com o rodapé do próprio post:

| Item | Valor |
|---|---|
| `nova_max` = dado mais novo do pacote da tese | **2026-08-01** (seis das sete séries; GACC 2026-02-01, EUROSTAT 2026-06-01) |
| `publicada_max` = dado mais novo já publicado na tese `comercio_sul_sul` | **2026-08-01** (o 400657, publicado 10/09, tem **o mesmo rodapé**) |
| Regra | `nova_max <= publicada_max` ⇒ **return False, "sem_dado_novo"** ⇒ `publicar = False` |
| Resultado observado | **publicado 11/09 02:36:22** ❌ |

**A prova material de que não havia dado novo é a mais forte possível:** o rodapé «Fontes primárias» de **400626 (08/09) · 400657 (10/09) · 400680 (11/09)** é **byte-idêntico** (normalizado: 1.251 caracteres, sha256 `abe63512b77734cd…`, conferido nas 3 leituras desta ronda). **O gate bloqueia por desenho; o post saiu.**

**Duas causas candidatas, e a query que decide (dono ZM):** (a) o run de produção **não passou por este gate/histórico** (outro caminho de publicação); ou (b) o histórico **não tinha** `publicada_max` para a tese porque o campo persistido tem **outro nome** — o gate lê `ultima_data` no pacote da redação (L209) e `data_referencia` nas fontes guardadas (`_historico_publicacoes` L190-193): **dois nomes para o mesmo dado**, e a costura entre eles é o ponto exato onde o gate pode ficar cego. **Prova pedida:** `BancoProducaoV42.listar_materias(tese=comercio_sul_sul)` + `fontes_da_materia(400657)` e conferir se `data_referencia = 2026-08-01` está gravada. Nada disso é acessível de fora — e é por isso que a auditoria externa não fecha o caso.

---

## 5. 🔴 Achado nº 3 — O GATE DE TÍTULO EXISTE, TINHA O GÊMEO NA LISTA, CALCULOU 0,8333 (LIMIAR 0,60) — E O POST SAIU

O gate anti-repetição de título (`ciclo_v42.py` L127-158 e L448-464) manda ao LLM os **10 últimos títulos publicados** (`titulos_evitar=historico["titulos"][:10]`, L444), exige diferença, **regenera 1×** e **bloqueia** se a similaridade Jaccard persistir **≥ 0,60** (`bloqueio_titulo = eco_titulo >= 0.60`, L451).

Reproduzi o cálculo **com a própria função do repo** (`jaccard_palavras`, L243-248), sobre os títulos que a lista dos 10 últimos continha em 11/09 02:36:

| Título comparado | Jaccard | |
|---|---|---|
| 400677 «Com a inflação baixa, o juro de 14% pode começar a cair» | 0,0000 | |
| 400668 «O impacto da Selic elevada no desenvolvimento econômico brasileiro» | 0,0000 | |
| 400657 «Crescimento do comércio Brasil-China e sua influência no Sul Global» | 0,3000 | |
| **400641 «Crescimento do comércio Brasil-China e a força do Sul-Sul»** | **0,8333** | **≥ 0,60 ⇒ o gate regenera e bloqueia** |
| 400636 / 400629 | 0,0000 / 0,0833 | |

O 400641 **estava** entre os 10 últimos publicados antes do 400680 (publicado 09/09 07:37; entre ele e o 400680 há só 7 posts: 400644, 400648, 400651, 400657, 400660, 400664, 400668 — todos na lista que usei). O título do 400680 é **o do 400641 com «O» na frente e a palavra «eixo»** — e passou.

**Corolário do método:** o veredito do gate **não vai para o artefato**. A `meta` do post tem **só** o `v42_texto_sha256`: não há `titulo_similaridade_max`, não há `similar_de`, não há `frescor`/`motivo`. **De fora do banco, é impossível saber se o gate rodou** — o gate responde sem deixar prova. Este é o mesmo buraco que a régua **I3** («o número carrega a lista») e o registro **I1** («Instrumento × Evidência») vêm pedindo há caçadas.

---

## 6. 🟠 Achado nº 4 — ECO CONGELADO: 8 POSTS DE 8 NO MESMO STEM, O MESMO CONJUNTO NUMÉRICO E A MESMA ABERTURA

Todos os posts do stem `comercio_sul_sul` desde o dia 1:

| ID | Data | Título |
|---|---|---|
| 400515 | 04/09 17:36 | Crescimento do comércio Brasil-China e a importância do Sul-Sul |
| 400564 | 05/09 14:36 | Crescimento do comércio Brasil-China e suas implicações para o Sul Global |
| 400580 | 06/09 12:37 | China compra mais do Brasil e amplia superávit com o mundo |
| 400608 | 07/09 09:36 | Crescimento do comércio Brasil-China e o fortalecimento do Sul-Sul |
| 400626 | 08/09 08:36 | O crescimento das exportações brasileiras para a China em 2026 |
| 400641 | 09/09 07:37 | Crescimento do comércio Brasil-China e a força do Sul-Sul |
| 400657 | 10/09 03:36 | Crescimento do comércio Brasil-China e sua influência no Sul Global |
| **400680** | **11/09 02:36** | **O crescimento do comércio Brasil-China e a força do eixo Sul-Sul** |

- **8 de 8 = a mesma tese, e 4 títulos começam literalmente com «Crescimento do comércio Brasil-China».** O rodízio de teses roda (os 3 stems se alternam) — **mas quando o stem volta, os DADOS voltam com ele**: o rodapé é o mesmo, byte a byte, em 400626/400657/400680.
- **A abertura é moldura vazia e ecoa entre edições:** «Análise do aumento do comércio entre Brasil e China e seu impacto no Sul Global.» (400680) · «Análise do aumento das exportações brasileiras para a China em 2026.» (400657) · «Análise das exportações brasileiras para a China e seu impacto no comércio.» (400626). **É exatamente a «frase-moldura vazia antes do dado» que a regra 18 proíbe** — e a primeira frase deveria trazer **fato + número + período**.
- **O gate anti-eco só compara TÍTULO** (Jaccard ≥0,60). **Nada no pipeline compara o CONJUNTO NUMÉRICO** ou o rodapé de fontes entre edições — então a repetição de dados passa limpa por construção.

---

## 7. 🟠 Achado nº 5 — A QUEDA QUE A EDIÇÃO DE 08/09 REPORTAVA DESAPARECEU, E O MESMO DADO VIROU «FORÇA»

A balança chinesa (GACC, 2026-02-01) traz no rodapé **três** informações: valor **90,98 bi** · `variação 12m +186,82%` · `variação período anterior −25,82%`. O que cada edição publicou:

| Post | O que o texto fez com o MESMO dado de fevereiro |
|---|---|
| 400626 (08/09) | «superávit de **90,98** bilhões. Esse número, no entanto, representa **uma queda de 25,82%** em relação ao período anterior.» ✅ duas faces |
| 400657 (10/09) | «…atingiu US$ 90,98 bilhões, mostrando a força da economia chinesa. Esse número reflete um **crescimento extraordinário de 186,82%**…» (só a face boa) |
| **400680 (11/09)** | «…registrou um superávit de US$ 90,98 bilhões. Esse número, **embora defasado, evidencia a força** da economia chinesa…» (**nenhuma das duas variações**) |

**Três enquadramentos para um número em quatro dias — «queda», «crescimento extraordinário» e «força» — e a edição de hoje é a mais pobre das três.** A letra da regra 14 (declarar a data do dado defasado) foi cumprida; o espírito («JAMAIS como recorde ou situação corrente») não: um superávit de **fevereiro**, caindo 25,82% no mês, é usado como evidência de **força corrente** em setembro.

---

## 8. 🟠 Achado nº 6 — TÍTULO/LIDE AFIRMAM «CRESCIMENTO» E «AUMENTO»; O NÚMERO MAIS NOVO DO CORPO É UMA QUEDA DE 21,24%

O título diz «**O crescimento** do comércio Brasil-China» e a 1ª frase, «**Análise do aumento** do comércio…». O dado **mais fresco** do corpo (variação período anterior, agosto/2026) é **exportações para a China −21,24%**. O «crescimento» repousa **só** no YoY (+15,02%) — e a única razão pela qual esse rótulo é correto é o §3 deste veredito. **Título assertivo contra o fato mais recente do corpo** é a mesma classe do feedback da CL sobre «prévia que virou passado» (título × lide × dado).

---

## 9. Bandeiras leves (corrigir no prompt/pipeline — não é alucinação)

- **B1 — `caption` da capa VAZIA.** No 400677 a capa tinha caption; aqui só há `alt`. Leitor de tela e crédito perdem.
- **B2 — 1 de 3 gráficos declarados.** A tese pede 3 (EXPORT_CHINA · GACC · USTRADE) e o corpo tem 0 `<img>` inline. As duas séries sem gráfico (GACC e FRED) são **as mesmas** que o texto não narra por inteiro — correlação registrada, causa a confirmar no gate visual §86.
- **B3 — `sha256` não auditável de fora.** O hash existe (bom), mas o corpo canônico é o JSON interno `{"titulo":…, "paragrafos":…}` (`ciclo_v42.py` L333-336); tentei **4 reconstruções** a partir do HTML (bruto, texto, texto normalizado, com e sem o rodapé) e **nenhuma bateu**. **Não afirmo que esteja errado** — afirmo que um terceiro **não consegue verificar** o selo sem a definição do corpo canônico.
- **B4 — «centralidade da China no comércio global» / «impacto no Sul Global».** Nenhuma das 7 séries do rodapé mede comércio global nem «Sul Global»: são enquadramento da tese (o `angulo` a declara), não dado. Registro como moldura, não como erro.
- **B5 — EUROSTAT (Balança Extra-UE27) e FRED (USTRADE) listados no rodapé e não usados no corpo.** O 400626 usou a FRED; o 400680 não.
- **B6 — não pude verificar a capa por visão:** o modelo em que rodo **não aceita imagem** nesta sessão. A capa está presente, com `alt` correto e 6 s antes do post, mas o passo «tribunal/visão» **não é meu** — dono do gate de imagem.

---

## 10. Arquitetura — 6 ideias (nada executado; propostas em rascunho)

- **I1 — Tirar o veredito dos gates de dentro do banco e gravar no `meta` do post.** Persistir `v42_titulo_similaridade_max`, `v42_titulo_similar_de`, `v42_frescor` e `v42_frescor_motivo` junto do `v42_texto_sha256`. **É o item de maior efeito pelo menor custo:** hoje o gate responde sem deixar prova; com 4 campos na meta, a auditoria externa (a minha) fecha o caso **sem** query interna. Mesma família da régua **I3**.
- **I2 — Alinhar o NOME do campo à CONTA (ou a conta ao nome).** Ou `variacao_12m_pct` passa a computar o acumulado de 12 meses de verdade, ou vira `variacao_mesmo_mes_ano_anterior_pct` e a **regra 13 do prompt** deixa de mandar rotulá-lo como «acumulado». O prompt e o código não podem discordar sobre o que um campo significa.
- **I3 — Gate anti-eco por CONJUNTO NUMÉRICO.** Se o rodapé de fontes (ou o multiset dos valores) de um post for **igual** ao de um post da mesma tese em ≤7 dias, o post é **reedição**: exige dado novo **ou** ângulo novo, ou não publica. Hoje o rodapé é byte-idêntico em 3 edições e nada no pipeline olha para ele.
- **I4 — Enforcement da abertura.** Regex simples barra `<p>` iniciado por «Análise de/do/da…» antes do primeiro número (a regra 18 já proíbe; falta o gate). Custo ~5 linhas, pega 3 edições deste stem de uma vez.
- **I5 — Frescor: um só nome para o mesmo dado.** O gate lê `ultima_data` no pacote e `data_referencia` no histórico; unificar o contrato (ou validar a costura com teste) — e registrar no recibo qual ramo rodou.
- **I6 — Ficha de ciclo no `meta` do cat 100005** (paridade com o que já existe): tese, quantos posts do stem em 7 dias, nº de gráficos aprovados/reprovados, `evento_cron`. Sem isso, toda auditoria começa adivinhando.

---

## 11. Riscos e reversibilidade (protocolo da casa: backup → prova → registro → rollback escrito)

- **Nada foi executado.** Este veredito é **leitura e análise**: REST público de leitura do espelho + leitura do código-fonte no repo. **publish=0.**
- **Backup:** não há artefato de produção a preservar — nenhum post, meta, código ou servidor foi tocado.
- **Prova:** todos os números deste arquivo têm origem datada — REST do espelho lido nesta ronda (02:43-02:46), rodapé de fontes do próprio post, `ciclo_v42.py`/`redator_economia_v4.py`/`publicador_economia_v4.py` (linhas citadas), e o cálculo Jaccard reproduzido com a função do repo.
- **Rollback escrito:** o rollback de qualquer ideia acima é **não aplicá-la**; nenhuma toca runtime. I1-I6 são propostas para o **✓ do Miguel** e execução pelo **dono do pipeline (DSC/ZM)** — **nunca por mim** (Lei de Poderes: não tenho credencial de WordPress e não devo procurá-la).
- **Segredos:** nenhum valor de chave/credencial neste arquivo (§82 respeitado).

---

## 12. Síntese em uma linha

**O V4.2 não inventou um número — mas os dois gates que a casa construiu para este defeito exato (título ecoado e dado repetido) calculavam bloqueio e o post está no ar:** título com **0,8333** (limiar 0,60, o gêmeo 400641 estava na lista) e pacote de **2026-08-01** já publicado na tese (rodapé **byte-idêntico** em 3 edições, sha `abe63512b77734cd`); **o campo `variacao_12m_pct` é YoY e o prompt manda chamá-lo de «acumulado»**; e **8 de 8 posts do stem repetem a mesma abertura e os mesmos números** — o conserto mais barato é gravar o veredito dos gates no `meta` do post e comparar o **conjunto numérico**, não só o título.

---

— DS Nuvem Ideias (DS-N Ideias) · arquiteto de brainstorms · veredito V42MON-400680 · nada em produção (Lei de Poderes).
