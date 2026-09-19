# 🧠 VEREDITO V42MON-400677 — «Com a inflação baixa, o juro de 14% pode começar a cair» (10/09 14:07:10, cat 100007 Investimento) — arquiteto

> **Refs:** ofício `IDEIA_PRO_DSNUVEM_IDEIAS-V42MON-OFICIO` (ordem do Miguel 02/09 ~20h) · veredito anterior da série Investimento: **400651 (09/09 14:05, auditado)** · **400614 (07/09, auditado)** · **400511 (04/09)** · **400412 (dia 1, 03/09)** · vereditos Estatística de hoje: **400668/400664/400660/400657** · watcher de pedidos PARADO no 400328 (dono ZM) — **sonda REST cobre** (precedentes 400412/400504/400511/400614/400651) · gate de frescor `cc72eea4c` **SEGUE REGRESSADO** (3ª confirmação do dia) · nada em produção (**publish=0 — Lei de Poderes**).

## Veredito: 🟠 ATENÇÃO — nota 3 — **zero número inventado (4/4 conferidos na fonte primária), MAS a defasagem é PROVADA: o post publicado às 14:07 de 10/09 chama de «o que mudou hoje» um PTAX de 02/09 — 8 dias velho — quando a fonte já tinha o dado de 10/09. E é o 7º post de 7 na MESMA tese.**

---

## 1. Ficha do post (fatos verificados 14:13-14:20, REST espelho cafezinho.news)

- **ID 400677** · `publish` **2026-09-10T14:07:10 BRT** (cat **100007 Investimento**, `tags` vazio) · slug `com-a-inflacao-baixa-o-juro-de-14-pode-comecar-a-cair` · autor **5470** · **capa 400676 PRESENTE** (`v42-2026-09-10-bcb-432.png`, gerada 14:06:42 — **28 s antes** do post).
- **Meta `meta` = None/vazio** → **SEM_FICHA** (todos os 7 posts do cat 100007 têm meta vazio; contraste: o cat 100005 grava `v42_texto_sha256`).
- Corpo: **1.388 caracteres**, **0 links**, **0 `<hr>`**, **sem rodapé «Fontes primárias»** (a palavra «fontes» aparece só na frase «As fontes oficiais concordam no retrato»). Fontes são **inline**: BCB série 433, BCB série 432, FRED, PTAX/BCB.

---

## 2. ✅ O que está CERTO — verificação na fonte primária (API do BCB, não cruzamento de memória)

Conferi os números na **API oficial do Banco Central** (`api.bcb.gov.br/dados/serie/bcdata.sgs.<n>`), leitura própria desta ronda:

| Claim do post | Série | Fonte primária (lida agora) | Veredito |
|---|---|---|---|
| IPCA «0,88% em março» | 433 | **01/03/2026 = 0,88** | ✅ exato |
| IPCA «0,07% em julho» | 433 | **01/07/2026 = 0,07** | ✅ exato |
| «quatro meses seguidos de queda na inflação» | 433 | mar **0,88** → abr **0,67** → mai **0,58** → jun **0,16** → jul **0,07** | ✅ **VERDADEIRO** — claim NOVO e conferido |
| Selic «travada em 14% ao ano» | 432 | **14,00** (13-16/09/2026) | ✅ exato |
| «quase 10,4 pontos percentuais acima» | 432 + FRED | 14,00 − 3,63 = **10,37** | ✅ arredonda certo |
| «dólar a R$ 5,13 (PTAX/BCB, 02/09)» | 1 | 02/09 = **5,1273** → 5,13 | ✅ o valor bate — **mas a data é o achado nº 1 (§3)** |

**Zero número inventado. 4 de 4 claims centrais honram a fonte.** É o padrão da série: em 8 dias de auditoria do V4.2 (Estatística + Investimento) **nunca apareceu número inventado** — o defeito do sistema nunca foi o dado, é a **janela** e o **eco**.

**Ganhos desta edição (registro do que melhorou):**
- **Título CONDICIONAL:** «o juro de 14% **pode** começar a cair» — o defeito de **título assertivo contra corpo condicional**, que marquei nos vereditos anteriores (400511/400651), **NÃO recorreu**. Crédito.
- **Capa é gráfico real da própria série:** `v42-2026-09-10-bcb-432.png` = série 432 (Selic), gerada 28 s antes, com `alt_text` e `caption` consistentes com o título. **Zero ilusão de imagem** — o oposto do problema de capa que a casa já teve.
- **0 links no corpo** — sem publipost, sem âncora comercial, sem dofollow (contraste direto com a família BUG-195).

---

## 3. 🔴 Achado nº 1 — DEFASAGEM PROVADA: «o que mudou hoje» é 02/09, e o dado de 10/09 já existia

O parágrafo central diz, textualmente:

> «O que mudou **hoje**: com o dólar a R$ 5,13 (PTAX/BCB, **02/09**)…»

O post foi publicado **10/09 às 14:07**. A série 1 do BCB (PTAX venda), lida agora na fonte primária, tem:

| Data | PTAX venda |
|---|---|
| 02/09 | 5,1273 ← **o que o post usa** |
| 03/09 | 5,0962 |
| 04/09 | 5,1253 |
| 08/09 | 5,0856 |
| 09/09 | 5,0979 |
| **10/09** | **5,1149** ← **disponível no banco no momento da publicação** |

Três consequências, todas verificáveis:
1. **O rótulo «hoje» é factualmente falso** — o dado é de 8 dias antes do publish.
2. **O dado fresco estava disponível.** Não é caso de «não havia dado novo»: o ponto de **10/09 (5,1149)** existia na série no instante da publicação. O motor escolheu o velho.
3. **O dado congelado viajou.** Esse mesmo `5,1273 @02/09` já tinha sido usado no **400614 (07/09)** — lá com a data declarada corretamente. Em 07/09 ele tinha 5 dias; em 10/09, **8 dias**. O post novo **herdou o dado velho do post anterior**.

**Por que isso aconteceu — a causa está no repo, não em opinião:** o gate de frescor `cc72eea4c` (o rodapé auto-verificável com variação de janela/período anterior) **segue revertido**. Prova desta ronda: `git diff --stat cc72eea4c HEAD -- cerebro/Foruns/v42_monitor/nyc_codigo/` = **1 arquivo mudou, 1 inserção, 15 deleções** (`ciclo_v42.py`), e `grep "Var:" cerebro/Foruns/v42_monitor/nyc_codigo/*.py` = **0 ocorrências**. **3ª confirmação do dia** (caçada 100 12:44 · DS-N 427ª 14:05 · esta).

**Sem esse gate, nada no pipeline compara a data do dado com a data de publicação.** O 400677 é a prova material: o instrumento não mentiu o número — mentiu a **idade** dele.

---

## 4. 🔴 Achado nº 2 — ECO: 7 posts de 7 na MESMA tese; o rodízio existe numa vertical e não na outra

Listei **todos** os 7 posts do cat 100007 (Investimento) desde o dia 1:

| ID | Data | Título |
|---|---|---|
| 400353 | 03/09 09:59 | O relógio do juro real de dois dígitos começou a correr |
| 400358 | 03/09 10:01 | Banco Central segura os juros em 14% com inflação no menor nível |
| 400412 | 03/09 14:05 | Inflação quase sumiu, mas o juro de 14% ainda vale no Brasil |
| 400511 | 04/09 14:04 | Inflação baixa abre caminho para juros menores |
| 400614 | 07/09 14:03 | Juros altos no Brasil fazem o dólar recuar e o real ganhar força |
| 400651 | 09/09 14:05 | Inflação cai e juros altos seguem travando seu dinheiro |
| **400677** | **10/09 14:07** | **Com a inflação baixa, o juro de 14% pode começar a cair** |

**7 de 7 = a mesma tese (Selic-14 × desinflação). Zero rodízio em 8 dias.**

O contraste é o que dá o diagnóstico, e é novo como evidência: o **cat 100005 (Estatística) RODA 3 teses** — os slugs provam a rotação (`politica_monetaria_comparada` → `inflacao_primaria` → `comercio_sul_sul` → volta). O **rodízio de teses que a DSC-051 mandou instalar funciona numa vertical e não foi para a outra.**

E o número-set é literalmente o mesmo entre dois posts separados por 3 dias: **0,88 / 0,07 / 14 / 3,63** no 400614 (07/09) e no 400677 (10/09). Par semântico quase gêmeo: **400412«Inflação quase sumiu, mas o juro de 14% ainda vale» × 400677 «Com a inflação baixa, o juro de 14% pode começar a cair»** — a mesma frase, com o sinal trocado.

---

## 5. 🔴 Achado nº 3 — SEM_FICHA persiste no cat 100007

`meta` = **vazio** nos **7/7** posts do Investimento. Não há `v42_texto_sha256`, não há ficha de ciclo (quem, seeds, custo, `evento_cron`). A pergunta «este post saiu de cron ou de mão humana?» **continua sem resposta no artefato** — 8 rondas depois do veredito do dia 1 (400412). O cat 100005 grava sha256; o cat 100007 não grava nada.

---

## 6. Bandeiras leves (corrigir no prompt — não é alucinação)

- **B1 «a poupança rende menos da metade dos 14% atuais»** — a poupança é 0,5%/mês + TR, o que dá ≈ **6,2% a 7,2%/ano** dependendo da TR. Está **na borda** do «menos da metade» (7%): o texto afirma sem declarar a TR. Trocar por um número datado ou declarar a hipótese de TR.
- **B2 «pelo Tesouro Direto, dá para começar com cerca de R$ 30»** — claim sem âncora datada inline. Verificar e datar, ou remover o valor.
- **B3 sem rodapé «Fontes primárias»** — as fontes são inline (bom), mas não há bloco verificável no fim (o rodapé que o `cc72eea4c` traria). 0 `<hr>`, 0 links.
- **Positivo que fecha o balanço:** o corpo **não** traz a classe «data-sem-suporte» nem «dia-da-semana errado» que já apareceram na série. As classes data/dia-da-semana/%-de-%/moeda/janela somam **0 recorrências** neste post.

---

## 7. Arquitetura — 5 ideias (nada executado; propostas em rascunho)

**I1 — Estender o rodízio de teses ao cat 100007.** O rodízio já funciona no 100005 (3 stems girando). O Investimento roda a mesma tese 7/7. É o item de **maior efeito pelo menor custo** desta onda: reaproveitar o mecanismo existente, sem inventar nada.

**I2 — Gate de frescor POR SÉRIE (o conserto do achado nº 1).** Regra: **todo número carrega (valor, série, data) no banco; antes de publicar, o gate lê o último ponto da MESMA série e, se existe ponto mais novo que o usado, o texto não pode rotular aquele dado como «hoje»**. Esse gate pega o 400677 **exatamente**: o ponto de 10/09 (5,1149) estava no banco, e o texto usou 02/09 dizendo «hoje». É o **irmão do gate anti-eco de 2 pernas** — mesma família «comparar o texto com o corpus real em vez de confiar no gerador». Substitui, com vantagem, a dependência do `cc72eea4c` revertido.

**I3 — «O que mudou hoje» vira campo verificável.** Se `data_do_dado ≠ data_de_publicação`, o parágrafo é **renomeado** («O que mudou desde 02/09») ou bloqueado. Hoje o rótulo é texto livre gerado pelo modelo — e o modelo errou.

**I4 — Ficha de ciclo no meta do cat 100007** (paridade com o `v42_texto_sha256` do 100005): quem, seeds, custo, `evento_cron`. Sem isso, toda auditoria minha começa adivinhando.

**I5 — Watcher `CATS = [100005, 100007]`** (rascunho R2 da caçada 28, ~10 linhas, **nunca aplicado**). Minha sonda REST pegou este caso 6 min após o publish — mas isso é **vigília humana fazendo o trabalho do watcher**. O conserto estrutural segue pendente (dono ZM), 8ª cobrança.

---

## 8. Riscos e reversibilidade (protocolo da casa: backup → prova → registro → rollback escrito)

- **Nada foi executado.** Este veredito é **leitura e análise**: REST público de leitura + API pública do BCB + `git diff`/`grep` no repo. **publish=0.**
- **Backup:** não há artefato a preservar — nenhum arquivo de produção, código ou meta foi tocado.
- **Prova:** todos os números deste arquivo têm fonte datada (API BCB lida nesta ronda; REST espelho; `git diff cc72eea4c HEAD`).
- **Rollback escrito:** o rollback de qualquer ideia acima é **não aplicá-la**; nenhuma delas toca runtime. I1-I5 são propostas para o **✓ do Miguel** e execução pelo dono do pipeline (DSC/ZM) — **nunca por mim** (Lei de Poderes: não tenho credencial de WordPress e não devo procurá-la).
- **Segredos:** nenhum valor de chave/credencial neste arquivo (§82 respeitado).

---

## 9. Síntese em uma linha

**O V4.2 não alucina número — ele envelhece dado sem avisar:** o 400677 publica «o que mudou hoje» com PTAX de 02/09 enquanto o dado de 10/09 dormia na série, e é o 7º de 7 posts na mesma tese; dois consertos baratos fecham os dois buracos (gate de frescor por série e rodízio de tese no Investimento), e ambos esperam o ✓ do Miguel.

---

— DS Nuvem Ideias (DS-N Ideias) · arquiteto de brainstorms · veredito V42MON-400677 · nada em produção (Lei de Poderes).
