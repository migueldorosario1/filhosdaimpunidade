# 🧠 VEREDITO V42MON-400660 — «IPCA desacelera a 0,07% em julho de 2026 com dólar estável e juro ainda alto» (10/09 04:35:41, cat 100005 Estatística) — arquiteto

> **Refs:** ofício `IDEIA_PRO_DSNUVEM_IDEIAS-V42MON-OFICIO` (protocolo `2026-09-03_oficio_inicial_acompanhamento_v42.md`) · veredito anterior desta série: **400657 (10/09 03:45, 🟠 2 — eco direto do 400641 + «balança comercial +16,22%» no lugar de importações totais + título «crescimento» com fato de queda)** · **400651 (09/09 14:24, 🟠 3)** · **400648 (🟠 3)** · **400644 (🟠 3)** · **400641 (🟠 3)** — este é o **2º veredito de 10/09** e o **1º do 400660** · pacote anti-eco DSC-051 v1.3/G11 (**SEM_VERSAO** — segue fora do código) · watcher `v42_espelho_watcher.py` parado no 400328 (dono ZM — religação; **a sonda REST do DS-N segue sendo a única linha de detecção**, pegou o 400660 ~9 min pós-publish, sem pedido formal em `v42_monitor/pedidos/`).

## Veredito: 🟠 ATENÇÃO — nota 3 — **ECO DIRETO de ~20h antes (mesmo stem `inflacao_primaria`) que INTRODUZIU um erro de rótulo inexistente na peça de origem** + **contradição interna no mesmo texto**. **Zero número inventado**: os 6 valores do corpo conferem 1:1 com o rodapé. O defeito não é o dado — é a **reprise que reescreve o rótulo**.

## 1. Ficha do post (fatos verificados 04:43-04:46, REST espelho cafezinho.news)

- **ID 400660** · publish **2026-09-10T04:35:41 BRT** (cat **100005 Estatística**, tag 100006) · slug **`v42-20260910-inflacao_primaria`** · link `cafezinho.news/v42-20260910-inflacao_primaria.htm` · autor **5470** · **featured_media 400659 PRESENTE** (capa `bcb-bcb-433-bar-8`, 2560×1361, alt do gerador BCB) · **meta `v42_texto_sha256` PRESENTE** (ficha do pacote anti-eco parte (a) honrada).
- **Texto integral (≈1.500 caracteres + rodapé de 3 séries):**

> A inflação oficial (IPCA) subiu apenas 0,07% em julho de 2026 […] avançou apenas 0,07% […] **desaceleração de 56,25% frente ao ritmo do mês anterior**. No mesmo dia 9 de setembro de 2026, a taxa oficial do dólar (PTAX) foi cotada a 5,0979 reais, com variação de 0,24% sobre o dia anterior. No acumulado de doze meses até setembro de 2026, o dólar PTAX recuou 1,25% […].
> **O IPCA de 0,07% em julho de 2026 veio depois de uma variação mensal 56,25% maior no mês imediatamente anterior** […]. [moldura sobre Fed, Selic alta, crédito caro e rentismo]
> Fontes primárias: **BCB/BCB_1 Dólar PTAX** — último 5.0979 BRL/USD em 2026-09-09 · 12m −1,25% · período anterior +0,24% · **BCB/BCB_433 IPCA mensal** — 0.07 % m/m em 2026-07-01 · período anterior −56,25% · **IBGE/IBGE_IPCA_GERAL** — 0.07 % m/m em 2026-07-01 · período anterior −56,25%.

## 2. 🔴 Achado nº 1 — ECO DIRETO: 400660 é a reprise do 400644 (09/09 08:36), ~20h antes

Comparação lado a lado (REST dos dois posts):

| | 400644 (09/09 08:36) | 400660 (10/09 04:35) |
|---|---|---|
| slug | `v42-20260909-inflacao_primaria` | `v42-20260910-inflacao_primaria` |
| capa | 400643 `bcb-bcb-433-bar-7` | 400659 `bcb-bcb-433-bar-8` |
| IPCA jul/26 | 0,07% m/m | 0,07% m/m |
| variação vs mês anterior | −56,25% | −56,25% |
| PTAX | 5,0856 (08/09) · 12m −1,94% | 5,0979 (09/09) · 12m −1,25% |
| fontes | BCB_1 + BCB_433 + IBGE_IPCA_GERAL | BCB_1 + BCB_433 + IBGE_IPCA_GERAL |

- **Perna 1 do gate anti-eco (48h mesmo stem de slug) TERIA BLOQUEADO:** o stem `inflacao_primaria` é IDÊNTICO (só muda o prefixo de data), intervalo ≈ **19h59**. A família completa do gerador: **400611 (07/09) → 400629 (08/09) → 400644 (09/09) → 400660 (10/09)** = **4 dias seguidos com o mesmo stem**.
- **Perna 2 (fontes ∩ números ∩ tese vs 48h) TAMBÉM:** as **3 mesmas séries** e o **mesmo par IPCA 0,07% / −56,25%**; a tese (IPCA×câmbio e juro alto) é a mesma.
- **Perna 3 (blocklist de família ≥2 posts/7d) TAMBÉM.**
- **7ª prova do dia em que as 3 pernas bloqueariam juntas** (400636/400641/400644/400648/400651/400657/**400660**) — pacote **SEM_VERSAO** mantido; o ✓ Miguel da msg 143 segue o desbloqueio.

## 3. 🔴 Achado nº 2 — a reprise INTRODUZIU o erro de rótulo (número certo, sujeito errado)

- O rodapé traz, nas séries BCB_433 e IBGE_IPCA_GERAL: «variação período anterior: **−56,25%**». O −56,25% é **a queda da variação de julho (0,07%) frente à de junho (0,16%)** — (0,07−0,16)/0,16.
- O **400644 de ontem escrevia o rótulo CERTO**: «Essa marca representa uma **queda de 56,25% em relação ao mês anterior**».
- O **400660 troca o rótulo**: «veio depois de uma **variação mensal 56,25% maior no mês imediatamente anterior**» — o mês anterior **não** foi 56,25% maior; a **queda é** de 56,25%. Mesma classe do «balança comercial +16,22%» do 400657 e do «IPCA segundo o Banco Central» do 400651: **o valor é fiel à fonte, o sujeito da frase não é.**
- **Contradição interna:** o próprio 400660, no 1º parágrafo, escreve o rótulo **correto** («desaceleração de 56,25% frente ao ritmo do mês anterior») e, no 2º, o **errado**. O texto afirma as duas coisas.
- **Padrão novo e duro desta série:** a reprise diária **preserva os números e reescreve os rótulos** — e é na reescrita que o erro entra (400641 correto → 400657 errado; 400644 correto → 400660 errado). **O eco não é só redundância: é vetor de mutação.** O gate anti-eco é, portanto, também um **gate de correção**.

## 4. 🟠 Achado nº 3 — janela mista e defasagem do fato-âncora

- **Janela mista na abertura:** a 1ª frase cola o IPCA **mensal** de julho (0,07%) com a variação **12 meses** do PTAX (−1,25%) — duas janelas diferentes na mesma oração (classe do 400644/400651).
- **Defasagem do fato-âncora:** o IPCA de **julho/2026** (divulgado em meados de agosto) é usado em **10/09** como prova presente para pedir corte de Selic; o único dado fresco é o **PTAX de 09/09**. O corpo data o IPCA (o leitor não é enganado), mas o **ângulo é de agosto**. Alvo da **P0 variação-12m/âncora móvel do motor** (6ª cobrança consolidada @ZM).
- **Fed e Selic sem fonte:** «o Fed mantém política restritiva» e «Brasil com uma das Selic mais altas do planeta» não têm série no rodapé — moldura editorial, não crédito; nenhum número de Selic é afirmado (o 14% não aparece aqui).

## 5. ✅ O que o post acerta (crédito conferido)

- **6 de 6 valores do corpo batem 1:1 com o rodapé** (0,07% · −56,25% · 5,0979 · +0,24% · −1,25% · 12m); **zero número inventado**.
- **Rodapé presente e auto-verificável**: 3 séries nomeadas e datadas + `v42_texto_sha256` na meta.
- **Unidades/moedas corretas** (BRL/USD rotulado; % m/m explícito).
- **Capa presente** (400659) — o BUG-184 não alcança o cat 100005.
- **Título honesto e com o fato primeiro:** «IPCA desacelera a 0,07% em julho de 2026…» — diferente do 400657, a **porta** (ZD-20260903-001) aqui abre para o fato certo.

## 6. Donos e pendências (nada em produção — Lei de Poderes)

- **@ZM (código DSC-051, cat 100005):** (a) o gate anti-eco de **48h mesmo stem** existe desenhado e **não está no gerador** — prova de hoje: `inflacao_primaria` 09/09 08:36 → 10/09 04:35 (e 4 dias seguidos); (b) **perna nova proposta nesta ronda:** quando o stem repete, o gerador deve **comparar corpo novo × corpo anterior** e exigir **mesmos pares número↔série e rótulo verificado** — divergência de rótulo = quarentena (o eco é vetor de mutação, §3); (c) **P0 variação-12m/âncora móvel** (6ª) e **P0 ComexStat** (4ª).
- **@ZM:** religar o watcher `v42_espelho_watcher.py` — `pedidos/` parado no 400328; a sonda REST do DS-N cobre (detectou o 400660 ~9 min pós-publish).
- **✓ Miguel:** «vai» do pacote anti-eco **SEM_VERSAO** (msg 143) — o **400660 é a 7ª prova** em que as 3 pernas bloqueariam (400636/400641/400644/400648/400651/400657/400660).
- **SLA base:** 400657 CUMPRIDO (03:45); novo **SLA base = 400660 (publish 04:35:41, veredito 04:45 — ~10 min)**.
- **Arquivo:** este veredito + caçada 97 (`2026-09-10_cacada_97_...md`) + síntese na ponte `de_ideias.md` + estado canônico/espelho.
