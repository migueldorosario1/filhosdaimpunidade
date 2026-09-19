# 🔎 VEREDITO V42MON-400629 — «Inflação de julho surpreende e expõe perda de força do câmbio» (08/09/2026 10:35:40, cat 100005, família `inflacao_primaria`) = 🟠 ATENÇÃO 3 — PTAX «variação 12m: -0,89%» NÃO reproduz na fonte citada (BCB SGS: -6,11%) = 2ª série com defeito de fonte no V4.2 · eco de família 7ª peça em 6 dias · SEM_VERSAO mantido

> **Refs:** ofício `IDEIA_PRO_DSNUVEM_IDEIAS-V42MON-OFICIO` (protocolo `2026-09-03_oficio_inicial_acompanhamento_v42.md`) · vereditos anteriores: **400626 (08:50 08/09, 🟠 3)** · 400622 (07:52, 🟠 3) · 400614/400618 (07/09, 🟠 3) · **400490 (01:50 04/09, 🟠 6 — ECO com 400305 do mesmo dia)** · 400545 (19:47 04/09, 🟠 4) · pacote anti-eco DSC-051 v1.3/G11 (SEM_VERSAO, cobrança consolidada) · caçada 76 (10:52 08/09) · watcher `v42_espelho_watcher.py` parado no 400328 (dono ZM — 73ª emissão de religação; sonda REST do DS-N cobre).

## 1. Dados do post (sonda REST espelho cafezinho.news 10:46-10:48)

- **ID:** 400629 · **cat:** 100005 (Estatística/V4.2) · **tags:** [100006] · **slug:** `v42-20260908-inflacao_primaria`
- **link:** https://cafezinho.news/v42-20260908-inflacao_primaria.htm
- **date_gmt:** 2026-09-08T13:35:40 (= **10:35:40 BRT**) · modified igual (sem edição pós-publish)
- **meta:** `{"v42_texto_sha256": "2a6f48256e50619c3d1acf7538182a29d17ce192fbdf50a90f06c36b1727350f"}` — **só sha256, SEM ficha de ciclo** (quem/seeds/custo/evento_cron — pendência mantida)
- **título:** «Inflação de julho surpreende e expõe perda de força do câmbio» (73c)
- **lead:** «IPCA mensal de julho de 2026 recuou para 0,07%, mas o câmbio desvalorizado pressiona os preços domésticos.»

## 2. Números do corpo × rodapé G3 × verificação externa (BCB SGS — fonte citada no rodapé)

| Número no post | Rodapé (G3, 3 linhas) | Verificação externa | Veredito do número |
|---|---|---|---|
| IPCA julho 0,07% m/m | BCB/BCB_433 — último 0.07 em 2026-07-01 | **BCB SGS 433**: julho = 0.07 ✓ (maio 0.58 · junho 0.16) | ✅ HONRA a fonte |
| «variação mensal caiu 56,25%» | variação período anterior: -56,25% | (0,07−0,16)/0,16 = **-56,25%** ✓ | ✅ HONRA a fonte |
| PTAX R$ 5,1253 em set/2026 | BCB/BCB_1 — último 5.1253 em 2026-09-04 | **BCB SGS 1**: 04/09/2026 = 5.1253 ✓ (última sessão — 07/09 feriado) | ✅ HONRA a fonte (data correta) |
| «leve alta de 0,57% na comparação diária» | variação período anterior: +0,57% | (5,1253−5,0962)/5,0962 = **+0,57%** ✓ (03/09→04/09) | ✅ HONRA a fonte |
| «Em doze meses... queda de 0,89%» | **variação 12m: -0,89%** | **BCB SGS 1**: 04/09/2025 = 5,4587 → 04/09/2026 = 5,1253 = **-6,11%** ❌ | 🔴 **NÃO reproduz** (ver §3) |

Rodapé: 3 linhas (G3 formal, **20º seguido**) — MAS 2 linhas redundantes (BCB_433 e IBGE_IPCA_GERAL carregam o MESMO número 0.07/2026-07-01: são o mesmo índice por 2 provedores; G3 deveria contar séries ÚNICAS — pendência já registrada no veredito 400583/14:47).

## 3. ACHADO PRINCIPAL 🔴 — PTAX «variação 12m: -0,89%» é um defeito de janela/medida (2ª série com defeito de fonte no V4.2; 2ª ocorrência na família)

- **Fato:** o rodapé cita `BCB/BCB_1` (PTAX venda) com «variação 12m: -0,89%». Consultando a MESMA série na fonte pública do BCB (api.bcb.gov.br SGS série 1): **04/09/2025 = 5,4587 → 04/09/2026 = 5,1253 ⇒ variação 12m REAL = -6,11%**.
- **Âncora do -0,89%:** não reproduz em nenhuma janela padrão da série testada nesta auditoria: 12m calendário (-6,11% · -6,2% via 02/09/2025 p/ o 400490) · 1 mês (04/08 = 5,1053 → +0,39%) · mês anterior fechado (31/07 = 5,0773 → +0,95%) · ~1 semana (28/08 = 5,2005 → -1,45% · 01/09 = 5,1570 → -0,61%) · YTD (31/12/2025 = 5,5024 → -6,85%) · mesmo dia útil 2025 (05/09/2025 = 5,3968 → -5,03%).
- **Padrão sistemático — prova dupla na família:** o **400490** (03/09 23:35) publicou «variação 12m: -1,42%» — o real também ≈ -6,2% (02/09/2025 = 5,4680 → 02/09/2026 = 5,1273) — e o -1,42% bate **EXATO** com a janela **28/08→02/09** (5,2005→5,1273 = -1,41%) = ~3-4 sessões. No 400629, o -0,89% também aponta para âncora de ~1 semana (~26-27/08, PTAX ≈ 5,17), sem dia exato de trading. **Leitura de arquiteto: a camada de dados do V4.2 está rotulando como «12m» uma variação de janela CURTA (~3-7 sessões) — provavelmente consulta de janela com cache/âncora errada (mesma classe do caso ComexStat: número publicado sem conferência contra a série canônica) — dono @ZM/@DSC (motor de variações).** O post anterior mais próximo com PTAX-12m auditado pela casa: veredito 400622 (07:52) já registrava «FLAG variação 12m REINCIDENTE 2ª [PTAX −0,89%/Selic +0,00% vs −6,11%/−6,67% janela calendário]» — **o -0,89% do 400629 é o MESMO valor flagrado no 400622** = o defeito é estável na série PTAX do motor (não é caso isolado).
- **Impacto no corpo:** com o 12m real (-6,11% = dólar em queda = real mais FORTE), a tese do corpo «o câmbio desvalorizado pressiona os preços domésticos / risco de repasse cambial» fica em **tensão com o dado citado** — a queda do dólar é DESINFLACIONÁRIA; a «pressão» se apoia só no +0,57% diário (um blip). O título «expõe perda de força do câmbio» é ambíguo (se «câmbio» = dólar, o dado CONFIRMA a perda de força — mas então é alívio, não pressão; se = real, o dado CONTRADIZ) — incoerência título×corpo×dado na MESMA linha narrativa. O corpo é boilerplate da família (rentismo · juro real · «entrave histórico ao desenvolvimento») repetido independente da direção do dado.

## 4. ACHADO 2 — ECO DE FAMÍLIA estrutural: `inflacao_primaria` = 7ª peça em 6 dias (perna 3 do pacote anti-eco teria bloqueado)

- Série da família no cat 100005 (slug stem `inflacao_primaria`): **400305 (03/09 04:24) · 400490 (03/09 23:35) · 400545 (04/09 19:36) · 400567 (05/09 16:36) · 400583 (06/09 14:35) · 400611 (07/09 13:35) · 400629 (08/09 10:35)** = **7 posts em ~6 dias** (intervalos ~19-23h — cadência quase diária).
- **Conteúdo repetido com âncora única:** TODAS citam o MESMO IPCA de julho (0,07% / -56,25% — dados de 07-08/2026, sem dado novo de inflação no meio) e o PTAX mudando apenas de sessão (400490: 5,1273@02/09 · 400629: 5,1253@04/09). Ou seja: a família gira a MESMA tese (câmbio × inflação) com o MESMO âncora, atualizando só o último ponto do dólar.
- **Gate:** pernas 1-2 (intervalo 48h entre posts da família) não pegariam isoladamente (intervalo 400611→400629 = ~21h < 48h — pegaria); a **perna 3 (blocklist de família ≥2 posts/7d → 4-7d)** teria bloqueado o 400629 na origem. **Nova prova para o ✓ Miguel: o desenho PRONTO (DSC-051 v1.3/G11) teria parado este post.**
- Contexto do dia: 3 posts V4.2 em 08/09 = 3 famílias DIFERENTES (400622 politica_monetaria_comparada 07:36 · 400626 comercio_sul_sul 08:36 · 400629 inflacao_primaria 10:35) — sem eco ENTRE os posts de hoje, MAS cadência do cron irregular MANTIDA (intervalos 1h/2h; 400618→400622 tinha sido 17h no dia anterior — sem cadência fixa, dono @ZM/DSC).

## 5. Classes da régua (janela/medida/moeda/data/dia) e meta

- **Classe janela/medida: REINCIDENTE (3ª/4ª na série)** — «variação 12m» com âncora de janela curta (ver §3; precedentes: 400622 PTAX −0,89% · 400515/400626 «acumulado de 12 meses» para variação 12m).
- Moeda: 0 erro (BRL/USD consistente) · Data: 0 erro (PTAX 04/09 = última sessão correta; IPCA julho = último disponível em 08/09) · Dia: 0 erro.
- **Meta: só `v42_texto_sha256`, SEM ficha de ciclo** (quem/seeds/custo/evento_cron/cadência) — pendência mantida (a pergunta «o slot 10:35 foi cron ou manual?» não tem resposta no meta).
- Corpo: 0 número inventado vs ficha do rodapé (todos os demais números conferem) — a reforma segura a VERIFICABILIDADE do corpo; o defeito está na CAMADA DE DADOS (12m), não no redator.

## 6. VEREDITO FINAL — 🟠 ATENÇÃO 3 · SEM_VERSAO MANTIDO

**O post NÃO alucina número no corpo** (100% consistente com o rodapé e com o BCB SGS nas 4 verificações externas) — MAS **a linha «variação 12m» do rodapé NÃO reproduz na fonte citada** (-0,89% × -6,11% BCB; padrão de janela curta rotulada 12m, 2ª ocorrência na família e 3ª/4ª na série de classes) e **o eco de família é estrutural** (7ª peça em 6 dias com o mesmo âncora IPCA). **SEM_VERSAO: a reforma não está segurando o suficiente para liberar a versão** — o pacote anti-eco (DSC-051 v1.3/G11, pernas 1-3 + ficha de ciclo no meta) está PRONTO e aguarda o ✓ do Miguel.

**Cobranças consolidadas (renovadas, não repetidas em CHECK):**
1. **P0 NOVO — PTAX-12m com âncora de janela curta** (evidência dupla 400490/-1,42% e 400629/-0,89% vs BCB -6,1/-6,2%; mesmo valor -0,89% já flagrado no 400622) — conferir o motor de variações da camada de dados @ZM/@DSC (2ª série com defeito de fonte após ComexStat).
2. **P0 ComexStat** (3ª cobrança — 400515/400626/400626: 8,34 bi julho × 10,673 bi verificado pela casa) @DSC/ZM.
3. **Eco de família estrutural** — `inflacao_primaria` 7ª/6d (esta) + `comercio_sul_sul` 12ª desde 26/08 + `politica_monetaria_comparada` 11ª — o cron do V4.2 gira 3 famílias em cadência irregular (~1-23h) @ZM/DSC.
4. **Cadência irregular do cron** mantida (08/09: 07:36 → 08:36 → 10:35) @ZM/DSC.
5. **Ficha de ciclo no meta** (SEM_FICHA persiste) @ZM/DSC.
6. **Watcher V42MON religar** (73ª emissão; parado no 400328 desde 03/09 — a sonda REST do DS-N cobre: 400629 detectado ~11 min pós-publish; SLA 24h base 400629 CUMPRIDO ~16 min pós-publish; prazo ~09/09 10:35).

**Arquivo de ronda:** caçada 76 (`cerebro/Foruns/ideias/2026-09-08_cacada_76_10_no_ar_269416_1045_8a_prova_veredito_400629_ptax_12m_furado.md`). **Nada em produção (Lei de Poderes).**

— DS Nuvem Ideias (DS-N Ideias) · 20260908 10:52:40 BRT
