# Catálogo de Bancos de Dados do Cafezinho

Este documento centraliza o mapeamento de todos os bancos de dados estatísticos, analíticos, eleitorais e de mídia em operação no ecossistema de agentes do Cafezinho. 

## 1. Agente Estatístico Global
**Arquivo:** `agente_estatistico_global/stats.sqlite3`
**Script Gestor Principal:** `banco_estatistico.py` / `ingestor_estatistico.py`

É a "Single Source of Truth" para a ingestão contínua de dados macroeconômicos de fontes primárias.

### Schemas Principais
- `series`: (fonte, serie_id, nome, unidade, frequencia, pais, categoria, atualizada_em)
- `observacoes`: (fonte, serie_id, data, valor, valor_txt, raw_hash, coletada_em)
- `coletas_log`: Log de operações dos gateways (secundários em NYC/China ou primário).
- `envelopes_processados`: Controle de idempotência para ingestão.

---

## 2. Banco Eleitoral Unificado do Cérebro
**Arquivo:** `Cerebro/banco_eleitoral.db` (e legados `root/banco_tse.db`, `root/banco_eleicoes.db`)
**Script Gestor Principal:** `Cerebro/banco_eleitoral_cerebro.py` e `root/util_tse.py`

Contém a base unificada de dados eleitorais municipais e estaduais do TSE (Vereadores, Prefeitos, Deputados Estaduais, Deputados Federais, Senadores, Governadores), consolidando o Rio Carta, Ceará Digital/Cícero e Mapa Rio.

### Schemas Principais
- `candidatos_eleicao`: `(id, ano, uf, municipio, municipio_slug, cargo, sq_candidato, nome, nome_urna, slug, partido, numero, situacao, turno, votos_validos, total_votos_validos_local, pct_votos_validos, eleitores_aptos, pct_sobre_eleitorado, criterio_percentual)`
- `municipios_eleitorado`: `(uf, municipio, municipio_slug, ano, eleitores_aptos, comparecimento)`
- `estatisticas_resumo`: `(chave, valor, atualizado_em)`

> **Metodologia de Votação & Percentual Padronizado:** O percentual de votos (`pct_votos_validos`) é estritamente padronizado como o total de votos nominais válidos obtidos pelo candidato dividido pelo total de votos válidos apurados na eleição no município/estado (1º turno).
> **Uso Comum:** O `util_tse.py` e os componentes `HeaderCidade.astro` consome esses dados para renderizar perfis municipais, câmaras de vereadores, prefeituras e bancadas de deputados.

---

## 3. Banco Analítico e Histórico
**Arquivo:** `root/agent_data_analise/historico.db`
**Script Gestor Principal:** Agentes editoriais / Analytics

Rastreia e indexa análises geradas, evitando que pautas idênticas sejam abordadas continuamente ou que ideias de bootstrap sejam desperdiçadas.

### Schemas Principais
- `analises_passadas`: (run_id, data_iso, tese, titulo, post_id_wp, status [rascunho/publicada], palavras, fonte)

---

## 4. Bancos de Mídia e Conteúdo Bruto
- `root/estatal_news.db`: Acervo bruto focado em mídia estatal, comunicados oficiais (Planalto) e discursos.
- `root/agent_data/china_news.db`: Focado em despachos da Xinhua, SCMP, etc, gerenciado pelo *Agente China*.
- `root/agent_data/banco_midia/banco_imagens_reais.db`: Repositório visual cacheado e vetorizado para atrelar imagens de acervo a parágrafos de novas matérias.

---

## 5. CSVs e Dados Estruturados Avulsos (Diretório Root e Outros)
- `Outros/pautas editoriais/[DATA]/divida americana/divida_americana_30_anos.csv`: Tabela do *TIC Data* (Tesouro Americano) com países detentores da dívida ao longo dos últimos 30 anos (granular).
- `root/dados_globais_soja.csv`: Histórico agronegócio.
- `root/cruzamento_posts_audiencia_hora_diasemana.csv` / `root/ga4_por_hora_diasemana.csv`: Exportações analíticas geradas cruzando o GA4 e logs do WordPress.

---

## Como Atualizar Este Catálogo
Se criar um novo schema SQLite ou iniciar o rastreio sistemático de um novo arquivo JSONL/CSV crucial para a arquitetura, insira-o aqui para que os agentes autônomos compreendam onde ler ou injetar dados sem duplicar tabelas e processos.
