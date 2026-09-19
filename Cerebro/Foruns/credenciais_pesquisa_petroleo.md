# Credenciais e Infraestrutura - Mercado de Petróleo (Para Instruções do GPT)

Abaixo estão os acessos de infraestrutura e endpoints de dados oficiais que nossa equipe já mapeou. Utilize essas fontes como referência para extração de dados e automação de scripts Python quando necessário.

### 1. Servidor Alfândega Chinesa (GACC)
Temos robôs prontos para varrer os dados de importação e exportação da alfândega chinesa.
*   **Provedor:** Tencent Cloud (Beijing)
*   **IP do Servidor:** `82.156.167.218`
*   **Usuário SSH:** `ubuntu` (Alias configurado: `beijing`)
*   **Diretório de Trabalho:** `/home/ubuntu/`
*   **Scripts Operantes:** `cdp_v3.py` e `final_level3.py` (Robôs baseados em Playwright para contornar o iframe do portal GACC)
*   **Ambiente Python:** Virtualenv `/root/venv/` configurado com as dependências.

### 2. Endpoints Oficiais (Dados Globais e EUA)
*   **U.S. EIA (Energy Information Administration):** Possui API aberta e robusta, sendo a principal fonte para consultar balanço mundial, produção, estoques e refino. 
*   **JODI-Oil Database:** Base de dados mensal recomendada para o mercado de petróleo global.
*   **IEA / OPEC (MOMR):** Relatórios de mercado abertos mensais contendo previsões e dados consolidados.

### 3. Endpoints Oficiais (Brasil)
*   **Comex Stat (MDIC):** API oficial para fluxo de importação e exportação do Brasil.
    *   **Endpoint:** `api-comexstat.mdic.gov.br`
    *   *Dica de busca:* Filtrar por NCM `2709` (Óleos brutos de petróleo) e `2710` (Óleos de petróleo e derivados).
*   **ANP (Agência Nacional do Petróleo):** Portal de Dados Abertos para consultar planilhas dinâmicas de produção (foco na produção "Do Poço ao Posto" e peso do Pré-Sal).
*   **IBGE:** PIA-Produto (Pesquisa Industrial Anual) para verificação industrial da cadeia do petróleo.
*   **Atalho Datalake ("Base dos Dados"):** O acesso via Google BigQuery para projeto `basedosdados` é altamente recomendado no Python/R para cruzar tabelas da ANP, Comex Stat e IBGE de maneira unificada via SQL.
