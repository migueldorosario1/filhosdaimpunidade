# Fórum: Coleta de Dados sobre o Mercado Mundial de Petróleo
Data: 11 de Julho de 2026

Este fórum reúne as credenciais, fontes (APIs e Dados Abertos) e dicas estratégicas para a estruturação do estudo sobre o mercado global e nacional de petróleo (produção, comércio, refino, exportação, estoques).

## 1. Fontes Globais (Mundo)

As seguintes plataformas oferecem APIs e bases de dados consolidadas sobre o panorama internacional do petróleo:

* **JODI (Joint Organisations Data Initiative):** Principal fonte padronizada de dados sobre petróleo, fruto da colaboração entre IEA, OPEC, APEC e outras entidades. O JODI-Oil World Database é de acesso livre, oferecendo downloads granulares sobre produção, estoques e exportação.
* **EIA (U.S. Energy Information Administration):** Oferece a **EIA API** (Open Data), que é robusta, gratuita e cobre detalhadamente produção, estoques (inventories), refino e exportação, tanto para os EUA quanto estimativas globais.
* **OPEC (Organização dos Países Exportadores de Petróleo):** Acesso a relatórios anuais e mensais (MOMR) com dados de balanço entre oferta e demanda, exportação e produção de membros e não membros.
* **IEA (Agência Internacional de Energia):** Disponibiliza vastos portais estatísticos de oferta e demanda. O acesso total aos dados de estoques e refino em tempo real geralmente exige assinatura comercial, mas há conjuntos abertos e relatórios setoriais.
* **Provedores Comerciais/Avançados:** Kpler, Petro-Logistics e ICE Data API possuem os endpoints mais precisos para tempo real, embora de acesso restrito (pago).

## 2. Fontes Nacionais (Brasil)

Para cruzar informações brasileiras de importação/exportação, refino e preços:

* **ANP (Agência Nacional do Petróleo):** A principal provedora nacional. Através do portal de Dados Abertos ANP, temos séries históricas completas de preços, movimentação e produção "Do Poço ao Posto". Existe documentação de API específica.
* **Comex Stat (MDIC):** Fundamental para as exportações e importações (comércio exterior). A API do Comex Stat (`api-comexstat.mdic.gov.br`) e suas planilhas abertas (CSV) contêm históricos profundos consultáveis via NCM do petróleo (FOB, peso).
* **IBGE:** Através da PIA-Produto (Pesquisa Industrial Anual), o IBGE entrega recortes de faturamento e estrutura de refino industrial nacional.
* **Dica de Integração:** Em vez de mapear endpoints individuais massivos, a plataforma **Base dos Dados** consolida dados da ANP, IBGE e Comex Stat num Datalake acessível via BigQuery, R e Python de forma unificada.

## 3. Fontes da China (Alfândega - GACC)

Para investigar as importações e balanço chinês, nós já temos o ambiente operante:

* **Servidor de Referência:** Servidor Beijing (Tencent Cloud)
* **IP e Credenciais:** `82.156.167.218`, usuário `ubuntu`. Acesso sem senha estabelecido localmente pelo alias SSH `beijing`.
* **Robôs Ativos:** Os crawlers do GACC (Alfândega Chinesa) já se encontram na pasta `/home/ubuntu/`.
  * `cdp_v3.py` e `final_level3.py`: Scripts maduros e testados, que fazem bypass dos iframes e lidam com interações dinâmicas via Playwright.
  * `dados_gacc/`: Diretório de despejo dos dados raspados. 
* **Ambiente de Execução:** O `venv` já está montado e pronto para ser executado. O robô se mostrou responsivo e não apresenta bloqueios em logs recentes de SSH.

---
**Próximos Passos (Sprint Sugerida):**
1. Estruturar os scrapers Python para consultar e ingerir JSONs via EIA API e Base dos Dados.
2. Executar uma nova rodada de raspagem do `cdp_v3.py` na máquina de Beijing para obter os dados mais frescos de importação de óleo bruto da China, depositando no data warehouse interno.
