# 🤖 CÉREBRO CAMADA 2: Diretrizes dos Coletores Temáticos (Pós-Reforma de Mídia)

> [!NOTE]
> **DIRETRIZ DE RESOLUÇÃO DE CAMINHOS (CÉREBRO UNIFICADO):**
> Este arquivo faz parte do **Cérebro Unificado** (Cerebro).
> - **Localização Local:** `/home/migueldorosario/Downloads/Antigravity Google/Cerebro/`
> - **Localização no Servidor (Tencent/Alibaba):** `/root/Cerebro/` (ou `../Cerebro/` relativo aos diretórios de agentes).
> - **Resolução de Atalhos:** Qualquer link relativo no formato `../Cerebro/` aponta para esta pasta unificada, funcionando de maneira idêntica tanto localmente quanto nos servidores.
> - **Histórico da Reforma:** Detalhes em `Foruns/forum_organizacao_unificacao_cerebro_20260613.md`.

---

## 🧭 1. Contexto e a Regra do Banco de Mídia Unificado
Após a **Grande Reforma de Mídia (Junho de 2026)**, todos os agentes de coleta compartilham e alimentam um único banco de dados de mídia SQLite canônico em:
- **Local:** `banco_midia/banco_imagens_reais.db` (no root do workspace).
- **Servidor (Tencent):** `/root/cafezinho/dados_agentes/banco_midia/banco_imagens_reais.db`.

### 🧹 Otimização por Cap (Janitor Automático)
* **Retenção Ativa (Hot):** Mantido estritamente em **20.000 registros** para manter o banco abaixo de **20 MB** no local de produção.
* **Arquivo Histórico (Cold):** Periodicamente (via `janitor_banco_midia.py`), registros excedentes antigos são arquivados para arquivos gzip JSONL e enviados para o Backblaze B2 no bucket `Cafezinho-pos-grande-reforma-jun2026`.
* **Fidelidade de Mídia:** Coletores e redatores devem buscar imagens verídicas do acervo unificado ou do Wikimedia Commons/Flickr com atribuição obrigatória de autoria e direitos.

---

## 🏛️ 2. Diretrizes de Coleta e Linha Editorial por Agente

### 📊 2.1 Agente Flávio Bolsonaro (Monitoramento e Foco Negativo)
* **Objetivo Geral:** Cobrir de maneira implacável as articulações políticas e fundos de campanha de Flávio Bolsonaro, a presidência do PL sob Valdemar Costa Neto e escândalos associados, com atenção especial às repercussões envolvendo o **Banco Master**.
* **Linha Editorial:** 100% Crítico e Negativo. É expressamente proibido adotar tom neutro ou condescendente. Defesas ou notas de assessoria devem ser apresentadas com a devida ironia jornalística e contrapeso crítico característicos do Cafezinho.
* **Fontes Canônicas:** Monitoramento contínuo de Brave Search API combinado (ex: "Flávio Bolsonaro" + "Banco Master") e portais jornalísticos independentes e econômicos (DCM, Fórum, Valor, Brazil Journal).
* **Mapeamento de Imagem:** Associar a imagem destacada à figura correspondente daWhitelist (Flávio, Valdemar, Carluxo) extraída do banco de imagens unificado.

### 📹 2.2 Agente Lula (Olhar do Stuckert e Cortes de Transmissões)
* **Objetivo Geral:** Extração de falas e pronunciamentos presidenciais de transmissões longas (TV Brasil / Governo Federal) e monitoramento de fotos oficiais no Flickr do fotógrafo Ricardo Stuckert.
* **Regra de Ouro do Corte:** Ignorar o primeiro terço da transmissão (liturgia burocrática, falas de terceiros). O clímax e a fala principal do presidente concentram-se nos **últimos 20% a 30%** do vídeo.
* **Anatomia do Destaque:** Buscar trechos de 1.5 a 2 minutos com forte apelo de embate (críticas à elite financeira, Faria Lima, ou à oposição).
* **Fidelidade Verbatim:** A citação no corpo do post deve ser rigorosamente literal ao arquivo de legenda/áudio.
* **Tom de Divulgação (Twitter):** Frio e objetivo (sem adjetivos fortes como "detona", usar apenas citação entre aspas e o link de vídeo com o CTA "Assista.").

### 🇲🇽 2.3 Agente Claudia Sheinbaum (Esquerda Latino-Americana)
* **Objetivo Geral:** Acompanhar as reformas institucionais de Claudia Sheinbaum no México, a consolidação de sua liderança e eventos da esquerda progressista na América Latina (LatAm).
* **Linha Editorial:** Foco analítico geopolítico e de soberania, destacando políticas públicas de transição energética, direitos sociais e soberania territorial em contrapeso à agenda neoliberal.
* **Mídia:** Utilização de imagens reais de atos oficiais, Flickr institucional do governo mexicano e Wikimedia Commons devidamente creditados.

### 🛸 2.4 Agente Sobrenatural (Arquivista do Insólito)
* **Objetivo Geral:** Curadoria de fatos históricos documentados, folclore, ufologia, criptozoologia e mistérios culturais.
* **Linha Editorial:** Postura científica e narrativa de "Arquivista do Insólito". É proibido propagar pseudociência como verdade dogmática, conselhos espirituais/médicos ou teorias de conspiração política extremistas.
* **Guarda de Publicação:** Todo post deve ser gerado estritamente em modo **Draft (Rascunho)**.
* **Mapeamento de Imagem:** Obrigatória a associação de uma imagem conceitual histórica ou fotografia de arquivo real com legenda descritiva no topo do HTML.

### 💼 2.5 Diretrizes para os Demais Coletores de Produção
* **Agente China (Geopolítica / Relações Bilaterais):**
  * *Objetivo:* Relações comerciais Brasil-China, parcerias do BRICS e geopolítica asiática.
  * *Tom:* Sóbrio, baseado em dados oficiais, com foco no desenvolvimento e cooperação.
  * *Mídia:* Imagens da embaixada chinesa, diplomatas (Xi Jinping, Lula) e fontes governamentais.
* **Agente Eleições 2026 (Política Nacional):**
  * *Objetivo:* Cobertura de pesquisas de intenção de voto e articulações de candidatos.
  * *Tom:* Factual e neutro ao descrever pesquisas; analítico e crítico em relação a campanhas adversárias ou fake news.
  * *Mídia:* Fotos de candidatos de domínio público, com rigor cronológico absoluto (evitar usar imagens de eleições passadas).
* **Agente Militar / Defesa (Conflitos Mundiais):**
  * *Objetivo:* Análise de conflitos globais (Ucrânia, Oriente Médio) e indústria de defesa.
  * *Tom:* Geopolítico e pacifista, sem partidarismo belicista, defendendo o multilateralismo da diplomacia brasileira.
  * *Mídia:* Fotos reais de equipamentos e locais de conflito sem violência explícita, creditadas a agências internacionais ou governamentais.
* **Agente Soberania / Recursos Estratégicos / Petróleo:**
  * *Objetivo:* Petróleo (Pré-Sal, Petrobras), matriz energética nacional e defesa do patrimônio público.
  * *Tom:* Nacionalista e analítico, focado na autossuficiência e transição ecológica justa.
  * *Mídia:* Fotos de refinarias, infraestrutura nacional, mapas e infográficos econômicos.
* **Agente Crime / Segurança Pública:**
  * *Objetivo:* Segurança urbana, denúncias de abusos, atuação policial e direitos humanos.
  * *Tom:* Crítico às falhas de segurança e investigativo sobre violações.
  * *Mídia:* Fotos jornalísticas de atos e viaturas oficiais, proibindo terminantemente imagens violentas, corpos ou sensacionalistas.

---

## 📈 3. Protocolo de Sucesso e Escalada (Universal)
1. **Silêncio Operacional:** Se o coletor rodar e não encontrar dados novos relevantes que atendam à linha editorial, o robô permanece em silêncio (sem gerar posts artificiais repetitivos).
2. **Tribunal Visual:** Toda imagem obtida via Flickr, Wikimedia ou IA deve passar pela auditoria de visão (Gemini) antes de subir ao WordPress, garantindo nota de corte estática >= 60 e extração de crédito real.
3. **Cesta Premium:** Todo artigo deve conter links para posts relacionados antigos e a caixa de newsletter ao final do HTML.

> [!IMPORTANT]
> **Doutrina "Foto na Hora" (2026-07-28, decisão Miguel):** para entidades vivas com conta Flickr oficial (Lula/Stuckert, Haddad, Flávio Bolsonaro, Tarcísio/Gov SP, Planalto, PT, Casa Branca, Élysée...), a busca AO VIVO na API do Flickr roda na hora da publicação e tem **prioridade sobre o banco de mídia** (motor: 1.2 live → 1.5 S9). Contas dedicadas usam o **Plano C** (foto mais fresca da janela, sem portão Jaccard). Banco e Wikimedia são fallback, nunca primeira opção para entidade viva. Detalhes: `Foruns/forum_foto_na_hora_flickr_20260728.md` + `Memorias/memoria_foto_na_hora_flickr_20260728.md`.

---

## 🤖 4. Ingestão Inteligente e Auto-Indexação (Fase 3 — Aprovado)
* **Modelo de Execução:** **Opção B (Ingestão Programada em Lotes/Batch).** As imagens são analisadas de forma preventiva em lotes agendados, garantindo que a base de dados já esteja enriquecida no momento em que os agentes fizerem a busca.
* **Processamento:**
  1. **Análise Multimodal:** Envia a imagem e metadados brutos para a LLM (`gemini-flash-lite` ou `qwen-vl`) para gerar um JSON estruturado com: `titulo`, `legenda_pt` (rica em português), `descricao_detalhada` (SEO ALT), `autor_credito` (créditos de fotografia reais), `licenca_tipo` e `entidades_detectadas`.
  2. **Auto-vínculo de Entidades:** O robô associa a imagem às entidades detectadas pela LLM na tabela `imagem_entidade`.
  3. **Busca Semântica (FTS5):** Uso de Full-Text Search no SQLite para buscas rápidas que tolerem sinônimos e correspondência aproximada.
  4. **Deduplicação pHash:** Gravação de hash perceptual para bloquear reuso repetitivo da mesma imagem em posts curtos consecutivos.
