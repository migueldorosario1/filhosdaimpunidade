# Consolidação do Pipeline Estatístico & Relatório de Mitigação Comex Stat

## 1. Topologia da Rede e Gestão de Credenciais

A infraestrutura global do **Agente Estatístico Global** opera de forma descentralizada por meio de três nós estrategicamente distribuídos para mitigar latência e contornar restrições geográficas:

1. **Tencent Cingapura (Primary Gateway - `43.156.151.165`):**
   * **Papel:** Banco de dados master SQLite (`stats.sqlite3`) e ingestão passiva de envelopes atômicos em JSON.
   * **Rotinas Locais:** Coleta direta de dados nacionais brasileiros (BCB SGS, IBGE SIDRA e ComexStat).
2. **NYC (Secondary Gateway - `198.199.121.136`):**
   * **Papel:** Coleta de dados ocidentais (EUA/Europa/Org. Internacionais - FRED, BEA, BLS, Eurostat, IMF).
   * **Rotinas Locais:** Empacotamento de observações em envelopes canônicos JSON em `/root/agent_data/stats/raw/incoming/` e sincronização via `rsync` com a Tencent a cada 10 minutos.
3. **Beijing (Secondary Gateway - `82.156.167.218`):**
   * **Papel:** Coleta de dados aduaneiros da China (GACC).
   * **Rotinas Locais:** Execução do scraper legado, empacotamento em JSON e sincronização via `rsync` com a Tencent a cada 10 minutos.

### Inventário de Credenciais (Carregadas via `chaves_novas.env`)
* **FRED API Key:** `cd897f3157d38b17c1be04a7a5931cb6` (Ativa no nó NYC)
* **BEA API Key:** `EEC02E93-3D66-4882-9DCA-B83662B4F877` (Ativa no nó NYC)
* **BLS API Key:** `badbd2e3e5ba407aa6f40dd010f31b7f` (Ativa no nó NYC)
* **EIA API Key:** `XgtjVvn3w0cXq4FI9T7l1drRTxQU4LyXDFqy93rG` (EIA v2 Open Data)
* **USDA FAS API Key:** `AGROBR_USDA_API_KEY` (Mapeada via biblioteca `agrobr`)
* **Census API Key:** `CENSUS_API_KEY` (U.S. Census Bureau International Trade)

---

## 2. Mitigações e Correções de Pipelines Ativos

Várias inconsistências em APIs públicas foram tratadas no código do coletor unificado (`agente_coletor_estatistico.py`) e nos arquivos de configuração (`fontes_estatisticas.json`):

* **Inconsistência do Eurostat (`une_rt_m`):**
  * *Problema:* A série de desemprego mensal retornava sucesso (HTTP 200), mas com 0 registros.
  * *Causa:* O filtro geográfico padrão `geo=EA` (Euro Area) não possuía registros na série histórica dessa tabela.
  * *Correção:* Substituição do parâmetro por `geo=EU27_2020` na URL de filtros do JSON de configuração.
  * *Comércio Extra-UE27:* Correção da série mensal de balança comercial `teiet210` aplicando obrigatoriamente o parâmetro de parceiro `partner=EXT_EU27_2020` para evitar retorno zerado.
* **Ajuste IBGE SIDRA:**
  * *Problema:* A API do SIDRA passou a retornar erro HTTP 400 (Bad Request) ao omitir o filtro territorial para séries agregadas.
  * *Correção:* Injeção do nível territorial nacional `/n1/all` diretamente na constante `BASE` de `ColetorIBGESidra` em `agente_coletor_estatistico.py`.
  * *Resiliência temporal:* Refatoração da identificação de chaves temporais na resposta SIDRA buscando dinamicamente comprimentos de 4 e 6 dígitos em chaves prioritárias (`D2C`, `D3C`, `D1C`).
* **Depreciação no Python 3.12+ (UTC Datetime):**
  * Subsituição de todas as chamadas deprecadas `datetime.utcnow()` por formatos timezone-aware explícitos (`datetime.now(timezone.utc).isoformat()`), garantindo conformidade com o padrão ISO 8601 com offsets UTC explícitos (`+00:00`).

---

## 3. Diagnóstico e Resolução da API do Comex Stat

Os dados do comércio exterior brasileiro são expostos oficialmente via API REST do MDIC no endpoint `https://api-comexstat.mdic.gov.br/general` via requisições `POST`. Durante a operação, duas vulnerabilidades críticas de estabilidade foram diagnosticadas e mitigadas:

### A. Bug de Cruzamento de Anos (Silent Failures)
* **Comportamento:** Consultas de períodos que cruzam o fim do ano civil (ex: de abril de um ano a março do ano seguinte) falham silenciosamente na API do Comex Stat, retornando payloads vazios ou truncados sem disparar erro HTTP no nível do protocolo.
* **Resolução Aplicada:** O script `fetch_eu_data.py` e o coletor unificado foram arquitetados para **fracionar as requisições em blocos anuais que não cruzem a barreira de 31 de dezembro**. Os dados são posteriormente agrupados e mesclados em memória antes de serem persistidos.

### B. Restrição Severa de Rate Limit (HTTP 429)
* **Comportamento:** A API do MDIC possui limites estritos de requisições concorrentes, gerando erros HTTP 429 com frequência sob requisições sequenciais rápidas.
* **Resolução Aplicada:** Implementação de uma rotina robusta de requisição com **retry e backoff exponencial** na função `http_request` do `agente_coletor_estatistico.py`, com pausa inicial e progressão até um limite de segurança (16 segundos de pausa entre tentativas).

---

## 4. Conclusões e Plano de Ação Recomendado

### Conclusões Operacionais
O pipeline unificado do Agente Estatístico Global atingiu maturidade arquitetural por meio do padrão **Inbox (escrita local em JSON nos nós secundários e consolidação mestre via rsync na Tencent)**. Contudo, APIs governamentais (como MDIC Comex Stat e IBGE SIDRA) são altamente voláteis e carecem de notificações prévias sobre mudanças de schemas e parâmetros obrigatórios.

### Próximos Passos Sugeridos
1. **Monitoramento Automatizado de Erros Silenciosos:**
   * Implementar testes de integridade semanais na Tencent (`stats.sqlite3`) para verificar se séries históricas importantes (como Comex Stat e Eurostat) apresentam gaps temporais superiores a 45 dias.
2. **Alertas de Erros Físicos (Alertas Ativos):**
   * Configurar o script de ingestão (`ingestor_estatistico.py`) para enviar um alerta imediato ao Telegram caso encontre arquivos corrompidos ou com registros zerados na pasta `/root/agent_data/stats/raw/incoming/`.
3. **Caching de Consultas Comex Stat:**
   * Para evitar erros HTTP 429 durante execuções repetidas ou depuração local, introduzir um mecanismo de cache local para requisições de anos anteriores (que são imutáveis após a consolidação anual pelo MDIC).
4. **Alinhamento Cron dos Nós Secundários:**
   * Garantir que as rotinas de rsync do nó NYC e Pequim estejam programadas com buffers adequados pós-coleta para assegurar a consistência dos envelopes recebidos na Tencent.

---

## 5. Auditoria de Publicação: Soja Brasil-China e Segurança Alimentar (Junho/2026)

Em 24 de junho de 2026, foi redigido e publicado um rascunho de editorial no WordPress sobre a dependência da soja chinesa da produção brasileira (comércio bilateral, segurança alimentar e suinocultura).

* **Post ID:** `260583` (status: `draft`)
* **Link de Edição:** `https://controle.ocafezinho.com/wp-admin/post.php?post=260583&action=edit`
* **Padrão Utilizado:** Padrão Ouro v10 (exatamente 6 parágrafos, exatamente 2 sentenças por parágrafo).
* **Imagens Anexadas:**
  * **Gráfico 1 (FOB por produto):** Mídia ID `260584` (definido como imagem destacada do post e exibido no conteúdo).
  * **Gráfico 2 (Produção mundial):** Mídia ID `260582` (exibido no conteúdo).
* **Categorias:** Economia (43), China (4996), Agro (5070), Comércio Exterior (14029).
* **Tags criadas/associadas:** Soja (ID 288), Segurança Alimentar (ID 11210), Sul Global (ID 5111).
* **Cesta Premium:** Newsletter AJAX e interlinking contextual com o post anterior de petróleo (`260557`) inseridos com sucesso.
