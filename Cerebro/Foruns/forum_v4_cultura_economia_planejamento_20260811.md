# Fórum — V4 Cultura + V4 Economia: planejamento (verificado no NYC canônico)

**Data:** 2026-08-11 ~10:45 BRT
**Sessão:** ZCode GLM-5.2 (Kimi/Qwen esgotados 🔴🔴, fallback final)
**Status:** 🔄 PLANEJAMENTO + PESQUISA — aguarda Miguel aprovar execução
**Tipo:** Tema Duplo (este fórum + memória técnica a gravar na execução)

---

## Missão (Miguel, 11/08)
Criar duas verticais novas no pipeline V4 do site O Cafezinho (ocafezinho.com):
- **V4 Cultura** (categoria WP **79** — já existe no site)
- **V4 Economia** (categoria WP **43** — já existe no site)

## Decisões do Miguel (11/08)
- **Cadência: 4 em 4 horas** para Cultura E Economia (mais devagar que as 3 verticais atuais de 30 min — "respirar mais devagar").
- **Reaproveitar fontes** dos agentes econômicos antigos (legacies/backups).
- "Começar devagarzinho" com esses dois.

---

## 1. Verificação canônica — SSH NYC (`nyc` = `198.199.121.136`) — CONFIRMADO

O V4 em operação (canônico) tem **3 verticais** em `/root/`:
- `nacional` — section `politica` — cat WP **22** — freshness 24h
- `geopolitica` — section `geopolitica` — cat WP **5003** — freshness 72h
- `ciencia` — section `tecnologia` — cats WP **19936/735/30/5008** — freshness 7d

**Arquitetura canônica** (cadeia pós-cutover 09/08/2026):
```
cron 30min → coletor.py <editoria>          → estoque_<section>.json   (COLETA)
          → v4_vertical_intake.py <section> → v4_verticals/<db>.sqlite3 (BANCO DE CONTEÚDOS)
          → v4_vertical_draft_worker.py <vertical>                      (REDATOR + gates)
              → codigo.v4_vertical_redactor_runtime (alias → contrato editorial)
              → draft WordPress                                            (PUBLICAÇÃO)
```

**Cron V4 ativo (NYC):** geopolitica `0,30` · ciencia `10,40` · nacional `20,50` (a cada 30 min, lock por vertical).

**Timestamps NYC (11/08):** `v4_vertical_draft_worker.py` 142 KB (11/08 02:35) · `v4_vertical_redactor_runtime.py` 9,5 KB (11/08 02:35) · `coletor.py` 39 KB (09/08) · `v4_vertical_intake.py` 11 KB (27/07).

### Os 5 "parafusos" para uma vertical nova nascer
1. **`coletor.py`** — editoria nova (`cul`/`eco`) + fontes RSS/queries próprias → `estoque_<section>.json`
2. **`v4_vertical_intake.py`** — entrada em `POLICY` (TTL), `DATABASES`, e `argparse choices`
3. **`CONFIG` do `v4_vertical_draft_worker.py`** — bloco `db`/`section`/`label`/`category_ids`/`freshness_hours`
4. **`EDITORIA_ALIASES` do `v4_vertical_redactor_runtime.py`** — `cultura→v4_cultura`, `economia→v4_economia`
5. **Contrato editorial** em `v4_labs/contratos/` + ramificação em `write_briefing()` do worker
6. *(aux)* linha no **cron** + categoria WP (ambas já existem)

---

## 2. Estado de cada vertical

### V4 CULTURA — briefing pronto, falta encanamento
- ✅ `v4_labs/contratos/v4_cultura_v1.md` (5,9 KB, briefing nobre desde 17/07) — no NYC
- ✅ `v4_curadoria_cultura_v1.json` + `v4_curadoria_cultura_v2.json` + 3 `v4_cultura_lab_*.json`
- ✅ Categoria WP Cultura = **79** (existe)
- ❌ Falta: editoria `cul` no coletor + intake (POLICY/DATABASES/choices) + CONFIG worker + alias runtime + fontes RSS culturais + cron

### V4 ECONOMIA — briefing do zero, mas TESOURO de fontes legadas
- ❌ Sem `v4_economia*` no NYC (só `v4_politica_economia_v1.md` = briefing da vertical Nacional)
- ✅ Categoria WP Economia = **43** (existe)
- 🏆 **Tesouro encontrado** (agentes econômicos legados, pausados desde 19/06/2026):
  - **NYC `/root/agente_estatistico/`** (intacto): `agente_coletor_estatistico.py` (37 KB, 8 fontes funcionais) + `fontes_estatisticas.json` (16 KB — **catálogo canônico de fontes**) + `ingestor_estatistico.py` + `banco_estatistico.py` + `arquitetura_agente_estatistico.md`
  - **NYC `/root/agente_inflacao.py`** (V9 funcional — 13 produtos, IPCA por subitem, freshness IPCA/IPCA-15/IGP-M/IGP-DI)
  - **NYC `/root/cafezinho/portal_cafezinho/agente_inflacao.py`** (cópia) + `/root/cafezinho/dados_agentes/tematicos_postados_inflacao.json` (histórico)
  - **`agente_mercado.py`** (V9 funcional — Ibovespa brapi.dev + Dólar BCB 1 + Selic BCB 432) — [legacy local `legacy/cafezinho_Legacy20260610_20260717/root/agente_mercado.py`]
  - **6 coletores ComexStat no ZCodeProject** (`coletor_comexstat_carnes.py`, `coletor_corrente_comercio.py`, `coletor_corrente_paises.py`, `coletor_destino_carnes.py`, `coletor_destino_semestres.py`, `coletor_detalhe_ncm.py`) — funcionais jul/26
  - **`Dados_Frios/Agentes Labs/criativos/economia/`** — re-implementação modular (`coletor_bcb.py`, `coletor_ibge.py`, `coletor_comexstat.py`, `calendario.json`, `schema_bancos_criativos.py`) — rascunho shadow

### Catálogo de fontes por tema (para o coletor `eco`)
- **Inflação:** BCB SGS (IPCA 433, IPCA-15 7478, IGP-M 189, Focus 13522) · IBGE SIDRA (7060 subitens c315, 1737 var 63, 7062) · FRED CPIAUCSL · BLS · Eurostat prc_hicp_manr · IMF PCPIPCH/BRA
- **Emprego:** IBGE SIDRA PNAD tabela 6381 var 4099 · CAGED · FRED UNRATE · BLS LNS14000000 · IMF LUR/BRA
- **Comércio exterior:** ComexStat `api-comexstat.mdic.gov.br/general` (POST, funcional, rate-limit/backoff) · UN Comtrade · WTO · BCB SGS 20539
- **Mercado financeiro:** brapi.dev ^BVSP (BRAPI_TOKEN) · BCB SGS 1 (dólar PTAX) · BCB SGS 432 (Selic meta)
- **Câmbio:** BCB SGS 1 · FRED DEXBZUS
- **Commodities/agro:** FRED (DCOILWTICO, DCOILBRENTEU, GASREGW) · ComexStat NCM (27090010 petróleo, 1201 soja) · ANP · CONAB
- **Macro/PIB:** IBGE SIDRA (6561/1620) · BCB SGS 4380 · FRED GDP · BEA · IMF NGDP_RPCH

### ⚠️ Bug a EVITAR no V4
O `agente_estatistico` antigo: coletor escrevia em `raw/payloads/` mas o ingestor lia `raw/incoming/` → dados nunca entravam no SQLite. **No V4 o padrão `estoque→intake` das verticais atuais já está correto** — não reutilizar o Inbox quebrado.

### ⚠️ Atenção SIDRA
Códigos divergem entre docs (IPCA: 1419 vs 1737 vs 7060; PIB: 6561 vs 1620 vs 6784). **Padronizar validando com curl** antes de fixar no coletor.

---

## 3. Cron proposto (cadência 4h, decisão Miguel)
```
0  */4 * * *  cultura   (lock /tmp/v4_cultura.lock)    → cat WP 79
30 */4 * * *  economia  (lock /tmp/v4_economia.lock)   → cat WP 43
```
Offset de 30 min entre os dois para não concorrer no LLM.

---

## 4. O que aconteceu / o que falta / o que preciso do Miguel

**Aconteceu:**
- Verificação canônica NYC ✅ (3 verticais, arquitetura, cron, timestamps)
- Mapeamento dos 5 parafusos ✅
- Catálogo de fontes econômicas por tema ✅ (reaproveitado dos legados)
- Briefing de cultura localizado ✅ (existe no NYC)
- Tesouro econômico localizado ✅ (NYC + legacies + ZCodeProject)

**Falta (execução, após aprovação):**
1. Baixar versões canônicas do NYC para o espelho local (`v4_vertical_draft_worker.py` etc.)
2. Escrever `v4_economia_v1.md` do zero + revisar `v4_cultura_v1.md`
3. Plugar os 5 parafusos em cada vertical (local, com backup `.bak_pre_v4_*`)
4. Fontes RSS culturais para a editoria `cul`
5. Dry-run (`V4_REDACTOR_DRY_RUN=1`)
6. Deploy NYC janela por janela
7. Cron por último (4h)

**Preciso do Miguel:**
1. **Abordagem:** contratos primeiro, ou encanamento + contratos juntos em dry-run?
2. **Cultura — imagem IA:** confirmar cota? (default: acervo V4 + Flickr primeiro, IA 20%)
3. **Economia — enriquecimento estatístico:** gráficos BCB/ComexStat nos posts, ou só texto jornal?
4. **Confirma cadência 4h** ambos (`0 */4` cultura, `30 */4` economia)?

---

## ADENDO 11/08 ~11:05 — +3 verticais (Meio Ambiente, Esporte, Saúde), cadência 8h

**Nova decisão do Miguel (11/08):** adicionar 3 verticais a mais, cadência **8h** (ainda mais lento que Cultura/Economia 4h). Total agora: **5 verticais novas**.

| Vertical | Cat WP | Cadência | Briefing/contrato | Fontes |
|---|---|---|---|---|
| Meio Ambiente | **582** ✅ (bônus 5102 = "previsão do tempo") | 8h | ❌ criar `v4_meio_ambiente_v1.md` | Do zero — 8 canônicas BR |
| Esporte | **1271** ✅ (bônus 2026 = "Copa do mundo 2026") | 8h | ❌ criar `v4_esporte_v1.md` | 🏆 legado `copa_v2` |
| Saúde | **258** ✅ | 8h | ❌ criar `v4_saude_v1.md` | Do zero — 8 canônicas BR |

**Confirmação taxonomia WP** (`taxonomia_wordpress.json`, 2026-05-07): as 3 categorias já existem — nada a criar no site.

### Estado das fontes (caça aos legacies)
- **Esporte:** 🏆 agente legado `copa_v2` em `Dados_Frios/Projeto Cafezinho Agentes/legacy_reformado_20260717/agents_labs_legacy/copa_v2/` — `diretriz_copa.json` rico (domínios ouro FIFA/CBF/ESPN/GloboEsporte/Lance, RSS Google News, Brave queries, capitalização nomes próprios Neymar/Vinícius/Endrick/Messi/Mbappé, fact_check fail-close). Base sólida — **ampliar de "só Copa 2026" para esporte geral**.
- **Saúde:** ❌ nenhum agente legado. **Do zero** — 8 fontes canônicas: Min. Saúde (`gov.br/saude/pt-br/assuntos/noticias/rss`), Agência Brasil ciência (`agenciabrasil.ebc.com.br/rss/ciencia/feed.xml`), G1 ciência-e-saúde (`g1.globo.com/rss/g1/ciencia-e-saude/`), Folha cotidiano/ciencia-e-saude, CONASS (`conass.org.br/feed/`), ANVISA (`portal.anvisa.gov.br/rss`), OPAS/OMS (`paho.org/pt/rss-feed/5610/all`), Google News (dengue/sarampo/SUS).
- **Meio Ambiente:** ❌ nenhum agente legado dedicado (só `robo_coleta_matriz_energetica` com petróleo/transição tangencial). **Do zero** — 8 fontes: G1 Natureza (`g1.globo.com/rss/g1/natureza/`), Globo Clima, Min. MMA (`gov.br/mma/pt-br/assuntos/noticias/rss`), Agência Brasil, InfoAmazonia (`infoamazonia.org/pt-br/feed/`), (oeco) (`oeco.org.br/feed/`), Estadão Sustentabilidade, Mongabay (`news.mongabay.com/feed/`). APIs futuras (fora do padrão RSS): INPE Queimadas, TerraBrasilis PRODES/DETER, MapBiomas.

**Padrão de coleta V4 confirmado:** RSS + Brave + Google News RSS + trafilatura (sem APIs externas hardcoded). Manter esse padrão para as 5 verticais novas.

### Cron completo proposto (8 verticais — 3 atuais + 5 novas)
```
# ATUAIS (30 min):
0,30  * * * *  geopolitica
10,40 * * * *  ciencia
20,50 * * * *  nacional
# NOVAS 4h (2):
0  */4 * * *   cultura       (cat 79)
30 */4 * * *   economia      (cat 43)
# NOVAS 8h (3) — janelas separadas, 3x/dia cada:
15 1,9,17  * * *  meio_ambiente  (cat 582)
15 2,10,18 * * *  esporte        (cat 1271)
15 3,11,19 * * *  saude          (cat 258)
```
Sem concorrência: cada slot em minuto/hora únicos, locks independentes (`/tmp/v4_<vertical>.lock`).

### Decisões pendentes do Miguel (atualizado para 5 verticais)
1. **Abordagem geral:** contratos primeiro, ou encanamento + 5 contratos juntos em dry-run?
2. **Cultura — cota imagem IA?** (default: acervo V4 + Flickr, IA 20%)
3. **Economia — enriquecimento estatístico** (gráficos BCB/ComexStat) nos posts, ou só texto? (default fase 1: texto)
4. **Confirma cron acima** (4h cultura/economia, 8h meio ambiente/esporte/saúde)?
5. *(novo)* **Esporte — escopo:** só futebol (Brasileirão/Libertadores/Copa/Seleção) ou esporte geral (F1, vôlei, basquete, tênis, olímpico)? O legado `copa_v2` é só Copa 2026 — ampliar quanto?

---

## ADENDO 11/08 ~11:25 — contratos editoriais escritos (5/5) ✅

**Decisões finais do Miguel (11/08, TODAS fechadas):**
- **Abordagem:** contratos primeiro ✅
- **Cultura — imagem:** Flickr + acervo V4, **sem IA** por enquanto ✅
- **Economia:** texto só (sem enriquecimento estatístico/gráficos nos posts) ✅
- **Cron:** confirmado (4h cultura/economia, 8h meio ambiente/esporte/saúde) ✅
- **Esporte:** escopo geral — todas as modalidades ✅

**Contratos escritos** no espelho local `Projeto Cafezinho Agentes/root/v4_labs/contratos/` (a deployar no NYC `/root/v4_labs/contratos/`):
- `v4_economia_v1.md` — novo · cat 43 · escopo macro/mercado/comex/cotidiano · **texto só** · distinção clara com a vertical Nacional
- `v4_meio_ambiente_v1.md` — novo · cat 582 · clima/biomas/água/fiscalização/povos indígenas · lastro INPE/MapBiomas/IBAMA
- `v4_esporte_v1.md` — novo · cat 1271 · escopo geral (futebol + F1/vôlei/basquete/tênis/olímpico) · fact-check fail-close · domínios ouro herdados do `copa_v2`
- `v4_saude_v1.md` — novo · cat 258 · SUS/surto/regulação/Anvisa/OPAS · sem alarmismo, sem negacionismo
- `v4_cultura_v1.md` — revisado (cabeçalho + categoria 79 + seção "Imagem destacada" Flickr+V4 s/ IA)

Todos seguem o molde canônico do V4 (Escopo/Tom/Faça/Não faça/Tese/Título/Exemplos/Critério de aceite), alinhados aos contratos `v4_internacional_v1.md`, `v4_politica_economia_v1.md`, `v4_ciencia_tecnologia_ia_v1.md` (lidos direto do NYC).

**Próxima fase (após Miguel ler/ajustar os contratos):** encanamento — os 5 parafusos (coletor `cul`/`eco`/`amb`/`esp`/`sad` + intake POLICY/DATABASES/choices + CONFIG worker + EDITORIA_ALIASES runtime) → dry-run → deploy NYC janela por janela → cron por último.

---

## 5. Continuidade
Para retomar em outra conversa: ler este fórum + SSH NYC para confirmar estado atual antes de mexer. Memória técnica (log de execução) será gravada quando a implementação começar.
