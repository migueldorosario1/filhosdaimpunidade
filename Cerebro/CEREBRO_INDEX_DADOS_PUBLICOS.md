# CEREBRO_INDEX_DADOS_PUBLICOS

> [!NOTE]
> **DIRETRIZ DE RESOLUÇÃO DE CAMINHOS (CÉREBRO UNIFICADO):**
> Este arquivo faz parte do **Cérebro Unificado** (Cerebro).
> - **Localização Local:** `/home/migueldorosario/Downloads/Antigravity Google/Cerebro/`
> - **Localização no Servidor (Tencent/Alibaba):** `/root/Cerebro/` (ou `../Cerebro/` relativo aos diretórios de agentes).
> - **Resolução de Atalhos:** Qualquer link relativo no formato `../Cerebro/` aponta para esta pasta unificada, funcionando de maneira idêntica tanto localmente quanto nos servidores.
> - **Histórico da Reforma:** Detalhes em `Foruns/forum_organizacao_unificacao_cerebro_20260613.md`.


Índice de bases públicas, coletas estruturadas e inventários de dados usados pelos projetos Miguel/Cafezinho/Rio Carta/Satélites.

## Prefeituras do Brasil - Sprint 2 Menus/Dados

Fórum:

- `Foruns/forum_dados_prefeituras_brasil_codex_20260517.md`

Diretório de dados:

- `root/agent_data_satelites/prefeituras_brasil/`

Arquivos principais:

- `municipios_ibge_20260517.json`
- `wikidata_municipios_sites_20260517.json`
- `prefeituras_brasil_urls_v0_20260517.json`
- `prefeituras_brasil_urls_v0_20260517.csv`
- `prefeituras_brasil_urls_v1_20260517.json`
- `prefeituras_brasil_urls_v1_20260517.csv`
- `overrides_prefeituras_capitais_20260517.json`
- `cobertura_por_uf_v0_20260517.json`
- `resumo_coleta_v0_20260517.json`
- `resumo_coleta_v1_20260517.json`

Estado em 2026-05-17:

- Base IBGE: 5.571 registros.
- Wikidata com código IBGE: 5.569 registros.
- URLs encontradas v0: 3.622.
- Sem URL v0: 1.949.
- Cobertura v0: 65,02%.
- Overrides v1: Rio de Janeiro, Belo Horizonte, Brasília/GDF.
- Validação HTTP v2:
  - URLs testadas: 3.623.
  - HTTP OK: 3.121.
  - HTTP falhou: 502.
  - OK entre URLs testadas: 86,14%.
- Arquivos v2:
  - `validacao_http_urls_v2_20260517.json`
  - `prefeituras_brasil_urls_v2_20260517.json`
  - `resumo_validacao_v2_20260517.json`
  - `cobertura_http_por_uf_v2_20260517.json`
  - `lacunas_sem_url_v2_20260517.json`
  - `falhas_http_v2_20260517.json`

Regra:

- Não usar a base v0/v1 diretamente em menu público.
- Antes de uso editorial/UX, executar validação v2: HTTP, domínio coerente, rejeição de turismo/câmara/legislativo, marcação de confiança.


## Publicação em menu real - Global South News

Atualizado em 2026-05-17 01:10 BRT.

- Repositório: `Projeto Cafezinho Agentes/global_south_news`.
- Commits:
  - `af714b2` - `Add Brazil prefectures data menu`
  - `f4415d0` - `Use slashless data menu links`
- Arquivo de consumo front:
  - `src/data/brazil_prefectures_menu.json`
- Páginas públicas validadas:
  - `https://www.globalsouth.news/data/brazil-prefectures`
  - `https://www.globalsouth.news/data/brazil-prefectures/rj`
  - `https://www.globalsouth.news/data/brazil-prefectures/sp`
- Estado: publicado em pre-launch com `noindex,nofollow` preservado.
- Fórum de implantação: `Foruns/forum_implantacao_menus_reais_20260517.md`.


## Publicação em menu real - Discover Brazil Food Guide

Atualizado em 2026-05-17 01:18 BRT.

- Repositório: `Projeto Cafezinho Agentes/discover_brazil`.
- Commit: `4fbfc96 Add Discover Brazil food guide menu`.
- Fonte editorial: `Foruns/forum_dados_bares_gastronomia_brasil_claude.md`.
- Parecer Trindade Chinesa: `root/agent_data_satelites/trindade_chinesa/parecer_trindade_chinesa_menus_reais_20260517.md`.
- Arquivo front: `src/data/bars_food_by_city.json`.
- Páginas públicas validadas:
  - `https://www.discoverbrazil.news/food`
  - `https://www.discoverbrazil.news/food/rio-de-janeiro`
  - `https://www.discoverbrazil.news/food/belem`
- Estado: publicado em pre-launch com `noindex,nofollow` preservado.
- Observação: páginas exibem ressalva de curadoria inicial e canal de correção.

## GACC — Alfândega da China (english.customs.gov.cn) — acesso direto 09/09/2026

Fórum:

- `Foruns/forum_gacc_alfandega_chinesa_acesso_direto_20260909.md`

Memória (receita técnica completa):

- `Memorias/memoria_gacc_acesso_direto_dados_agosto_20260909.md`

Diretório de dados:

- `dados_gacc/release_agosto_2026/` (10 CSVs do release de ago/2026 publicado 09/09/2026 + `RESUMO_brasil_e_totais_agosto2026.csv` + `html_bruto/`)

Estado em 2026-09-09:

- Site zh (`www.customs.gov.cn`, `stats.customs.gov.cn`): HTTP 412 (WAF c/ desafio JS) do Dell e do NYC.
- Site inglês (`english.customs.gov.cn`): HTTP 200 do Dell e do NYC — fonte viável p/ o coletor V4.2 (NYC), substituindo o CSV legado do servidor Beijing (morto desde ~07/2026, série parada em fev/2026).
- Seções: ColumnId=1 Preliminary Release (mês mais novo, sai ~dia 7-10) · ColumnId=2 Monthly Bulletin (detalhado, defasagem ~1 mês; último = 7.2026) · ColumnId=3 Quarterly · ColumnId=4 Release Calendar · ColumnId=5 Explanatory Notes.
- Pendente: "vai" do Miguel p/ plugar `gacc_english_direct` no `coletor_comercio_exterior_v4.py` + backfill mar→ago/2026.
