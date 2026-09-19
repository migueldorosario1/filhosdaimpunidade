# 🧮 VEREDITO V42MON-400683 — «IPCA desacelera a 0,07% em julho de 2026 com dólar a R$ 5,11» (cat 100005 Estatística, 11/09/2026 03:36:10)

> **Ofício:** `IDEIA_PRO_DSNUVEM_IDEIAS-V42MON-OFICIO` (protocolo `2026-09-03_oficio_inicial_acompanhamento_v42.md`) · **Pedido formal:** AUSENTE — o watcher `v42_espelho_watcher.py` segue PARADO no 400328 (dono ZM; 17ª cobrança de religação). **Detecção:** sonda REST própria do DS-N ~7 min pós-publish (03:43), mesma via da 400680.
> **Refs:** vereditos anteriores: **400680 (11/09 02:36, 🟠)** · **400677 (10/09 14:07)** · **400668 (10/09 07:35)** · **400664 (05:35)** · **400660 (04:35)** · **400657 (03:36)** · **400651 (09/09 14:24)** · **400648/400644 (09/09)**.
> **Assinatura do autor da matéria:** uid 5470 (mesmo id do canônico «esteira»; no espelho o slug é diferente — I9). **Meta:** só `v42_texto_sha256 = bda27b0f699a82a50229c5f2324971ee0eb3c3a93a3cf77880f41f63a518fb77`.
> **Leitura:** REST pública do espelho `cafezinho.news` — leitura pura, nada executado, sem credencial. **publish=0 — Lei de Poderes.**

---

## 1. O que o post diz (resumo fiel)

Tese única, repetida em 10 parágrafos: **o IPCA de julho/2026 (0,07% m/m) desacelerou e o dólar PTAX está estável (R$ 5,1149 em 10/09), logo a inflação não é importada e o culpado é o juro alto (Selic) que estrangula crédito, dívida pública e consumo.** Fecho político: «cortar a Selic é devolver poder de compra». 11 parágrafos, **0 links, 0 imagens inline**, 2.780 caracteres de texto, rodapé de 3 fontes.

## 2. Auditoria número a número — 5 de 5 conferidos no próprio rodapé

| Afirmação do texto | Fonte declarada no post | Veredito |
|---|---|---|
| IPCA subiu 0,07% em julho/2026 | BCB/BCB_433 + IBGE/IBGE_IPCA_GERAL (`0.07 % m/m`, 2026-07-01) | ✅ confere |
| IPCA 56,25% abaixo do mês anterior | `variação período anterior: -56,25%` | ✅ confere (0,07 ÷ (1−0,5625) = 0,16% em junho; interpretação correta) |
| PTAX fechou R$ 5,1149 em 10/09/2026 | BCB/BCB_1 (`5.1149 BRL/USD`, 2026-09-10) | ✅ confere |
| PTAX +0,33% sobre o dia anterior | `variação período anterior: +0,33%` | ✅ confere |
| PTAX −0,70% em doze meses | `variação 12m: -0,70%` | ✅ confere (campo, ver I2 abaixo) |

**Não conferíveis (afirmados sem fonte nesta matéria):**
- **«divulgado com 72 dias de defasagem»** — os 72 dias são a distância entre a **data de referência** (2026-07-01) e a publicação (11/09), **não** a data de divulgação: o IBGE divulga o IPCA de julho no fim de agosto (~30 dias após o mês). O texto **inventa uma data de divulgação** a partir da data do dado. (mesma família do «defasado» dos vereditos 400651/400657)
- **«Fed mantém sua taxa em patamar elevado»** — não há FRED/FEDFUNDS no rodapé desta matéria (havia no 400664).
- **«Selic entre as mais altas do mundo» / juro de 14%** — a Selic **não é fonte do 400683** (é do 400664); a peça usa o número de outra matéria como se fosse dela.

## 3. Achados (linhas de ouro do arquiteto)

**(1) 🔴 O GATE ANTI-ECO FALHOU DE NOVO — E AGORA COM PROVA DE 5 DIAS:** o título do 400683 tem **0,7794 de similaridade** com o do **400660** («IPCA desacelera a 0,07% em julho de 2026 com **dólar estável e juro ainda alto**», publicado 10/09 04:35:58 — **2 posições atrás, dentro da lista dos 10 últimos**). O limiar do gate é **0,60**. É o **2º caso em 25 h**: o 400680 tinha 0,8333 contra o 400641. **O gate de frescor está sendo contornado por reescrita de manchete.**

**(2) 🔴 O CONJUNTO NUMÉRICO É FIXO E O RODÍZIO SÓ TROCA A COTAÇÃO DO DIA:** o par **IPCA `0.07` + `-56,25%` está byte-idêntico em CINCO posts consecutivos** — **400611 (07/09) · 400629 (08/09) · 400644 (09/09) · 400660 (10/09) · 400683 (11/09)** — com as MESMAS 3 chaves de fonte (`BCB_1`, `BCB_433`, `IBGE_IPCA_GERAL`). O que muda de um dia para o outro é **só o valor diário do PTAX**: 5.1253 (04/09) → 5.0856 (08/09) → 5.0979 (09/09) → 5.1149 (10/09). **É o «rodapé byte-idêntico» do veredito 400680, agora medido em série: o dado de julho não é notícia nova, é cenário requentado com carimbo de hoje.**

**(3) 🟠 AS «3 FONTES» SÃO 2 DADOS:** `BCB_433` (IPCA Variação Mensal) e `IBGE_IPCA_GERAL` (IPCA Índice Geral) trazem **exatamente os mesmos `0.07` e `-56,25%`**. A redundância infla a contagem de fontes de 2 para 3 sem acrescentar um número — o gate/validador que conta «fontes» conta linhas, não dados (mesma família do «contador contava campos e não entradas», BUG-205 do DS-Dell).

**(4) 🟠 A JANELA MISTURA JULHO E SETEMBRO NA MESMA FRASE:** o lide cola «IPCA **de julho**» com «PTAX **de 10 de setembro**» e o 2º parágrafo diz «**No mesmo período**» — mas um é **mês fechado (julho)** e o outro é **leitura de 12 meses do dólar**: comparar as duas «variações» como se fossem o mesmo intervalo é erro de janela (a família que o ofício V42MON caça desde o 400651).

**(5) 🟡 O META É OPACO — E FALTA EM 7 DOS 15 ÚLTIMOS:** só existe `v42_texto_sha256`; **não há** registro de qual pacote, qual gate rodou, nem o resultado (bloqueou/não bloqueou). Pior: o sha **está ausente em 400668, 400657, 400626, 400636, 400622, 400618 e 400611** (7 de 15 da série). De fora do banco é impossível auditar o gate — a assinatura que deveria fechar o portão é a que falta.

## 4. Arquitetura do conserto (propostas; dono ZM/us65 — nada executado)

- **I1 (registro do gate):** gravar no meta do post o **pacote**, o **hash da lista de comparação** e o **ramo do gate** (`bloqueou`/`passou`, com o par de maior similaridade e o score). Hoje só há o sha do texto.
- **I2 (eco por conjunto numérico, não por título):** bloquear quando o **conjunto de valores das fontes** (exceto a cotação diária de série) for igual ao de um post dos últimos N dias. O 400683 seria barrado: {0.07, -56.25} repetido 5×.
- **I3 (separar ROTA de MÉRITO — já pedido no 400680):** o `encaixe_vertical`/gaveta não pode decidir a nota; e a varredura das pautas 5,0–5,5 com encaixe baixo continua pendente.
- **I4 (fonte duplicada não conta 2×):** deduplicar fontes por **(chave, valor)** antes de estampar «Fontes primárias» e antes de qualquer placar de pluralidade.
- **I5 (data de divulgação ≠ data de referência):** se o pipeline não tem a data de divulgação, **não escrever «divulgado com N dias de defasagem»**; usar «dado referente a julho/2026».
- **I6 (dono da query dos gates):** @ZM roda `listar_materias` + `fontes_da_materia` do 400683/400660 e diz **por que o gate de 0,60 não bloqueou** (o 400660 estava na lista dos 10?). Sem isso, os vereditos ficam na dedução.
- **I7 (religar o watcher V42MON):** o pedido formal `IDEIA_PRO_DSNUVEM_IDEIAS-V42MON-<postid>` está parado no 400328 — a detecção hoje é só a minha sonda (17ª cobrança @ZM).

## 5. O que precisa do Miguel

1. **✓ para o I6** (autorizar o @ZM a rodar a query forense dos gates do 400683/400660 e publicar o resultado no canal) — sem ela não sei se o gate não rodou ou se rodou e não bloqueou.
2. **✓ para o I2/I4** (eco por conjunto numérico + dedupe de fontes) — mudança no pipeline do V4.2, alçada ZM.
3. **✓ para o I1** (registro do gate no meta), que já vem do veredito 400680 — **2ª vez pedido**.
4. Segue em aberto do turno: rel sponsored/nofollow, publiposts 269144/269155, I3 (rota×mérito), SEM_VERSAO (msg 143), religar o watcher V42MON.

## 6. Reversibilidade e limites

Leitura **read-only** do espelho (7 requisições GET, sem credencial, sem escrita). **Backup:** não aplicável — nada foi alterado. **Prova:** números transcritos acima com o rodapé do próprio post. **Rollback:** não aplicável. **publish=0 — Lei de Poderes:** nenhuma proposta aqui autoriza publicação, agendamento, edição de post ou mudança de gate; tudo exige ✓ explícito do Miguel e dono ZM.

— DS Nuvem Ideias (DS-N Ideias) · 20260911 03:44:49 BRT
