# Fórum: Consolidação do Banco Eleitoral do Cérebro & Padronização Metodológica de Percentual de Votação

**Data:** 2026-07-27  
**Autor:** Antigravity AI (Google DeepMind Team)  
**Status:** Concluído / Operacional  

---

## 1. Resumo Executivo & Diretivas

Atendendo à orientação do áudio do Miguel, executamos a estruturação e consolidação do **Banco Eleitoral do Cérebro** (`Cerebro/banco_eleitoral.db`), unificando os dados das eleições municipais e estaduais do TSE utilizados nos portais **Rio Carta**, **Ceará Digital / Cícero** e **Mapa Rio**.

Adicionalmente, padronizamos a métrica e a explicação pública dos percentuais de votação em toda a interface do usuário.

---

## 2. Estrutura do Banco Eleitoral do Cérebro

- **Arquivo:** `Cerebro/banco_eleitoral.db`
- **Script Ingestor:** `Cerebro/banco_eleitoral_cerebro.py`
- **Total de Registros Iniciais:** 3.840 candidatos (Vereadores, Prefeitos, Deputados Estaduais, Deputados Federais, Senadores e Governadores) em 276 municípios do RJ e CE.

### Tabela `candidatos_eleicao`
- `ano`: Ano do pleito (ex: 2024, 2022).
- `uf`: Unidade da Federação ("RJ", "CE").
- `municipio` / `municipio_slug`: Nome e slug do município ou estado.
- `cargo`: Cargo concorrido ("Vereador", "Prefeito", "Deputado Estadual", "Deputado Federal", "Senador", "Governador").
- `votos_validos`: Votos nominais válidos recebidos pelo candidato.
- `total_votos_validos_local`: Total de votos nominais válidos apurados na eleição para aquele cargo no município/estado.
- `pct_votos_validos`: Percentual exato em relação aos votos válidos nominais locais (`(votos_validos / total_votos_validos_local) * 100`).
- `criterio_percentual`: Metodologia textual armazenada com cada registro: `"Votos nominais válidos do candidato divididos pelo total de votos válidos apurados na eleição local (1º turno)."`

---

## 3. Padronização da Explicação Metodológica na Interface

Em todos os portais (**Rio Carta**, **Ceará Digital / Cícero**, **Mapa Rio**), os componentes de cabeçalho da cidade (`HeaderCidade.astro`) e páginas de perfil de parlamentares/tags (`[tag].astro`) foram atualizados para incluir a nota clara e legível:

> **"* O percentual equivale aos votos válidos do candidato sobre o total de votos válidos apurados na eleição no município (1º turno)."**

---

## 4. Registro no Catálogo de Bancos de Dados

O arquivo `Cerebro/MEMORIA/CATALOGO_BANCOS_DE_DADOS.md` foi devidamente atualizado para refletir a adição do `Cerebro/banco_eleitoral.db` como Single Source of Truth para consultas eleitorais dos agentes autônomos.
