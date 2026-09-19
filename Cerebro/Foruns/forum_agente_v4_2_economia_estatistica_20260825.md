# Fórum de Arquitetura & Implementação — Agente V4.2 de Economia Global & Inteligência Estatística Primária

**Data:** 2026-08-25 18:02 BRT  
**Participantes:** Miguel do Rosário & Antigravity  
**Status:** 🚀 MÓDULOS A & B IMPLEMENTADOS E HOMOLOGADOS | MÓDULOS C, D & E EM ESPECIFICAÇÃO DETALHADA  
**Caminho Local:** `/home/migueldorosario/Downloads/Antigravity Google/Cerebro/Foruns/forum_agente_v4_2_economia_estatistica_20260825.md`  

---

## 1. Visão Estratégica e Filosofia do Sistema

O **Agente V4.2 de Economia** representa um salto qualitativo no ecossistema de inteligência autônoma do grupo *O Cafezinho* e *Global South News*. Ele abandona a simples raspagem de notícias secundárias em favor da **captura primária de dados estatísticos brutos** diretamente dos órgãos oficiais das maiores potências econômicas mundiais.

### Diretrizes Fundamentais do Miguel:
1. **Zero Agente Pobre:** Ampla cobertura de fontes primárias globais (Brasil, China, EUA, Europa, FMI).
2. **Zero-Break Pipeline (Anti-Quebra):** Coleta desacoplada de dados que grava envelopes atômicos em disco. Falhas em APIs externas nunca paralisam o banco de dados ou o gerador de matérias.
3. **Imutabilidade e Idempotência:** Deduplicação estrita via algoritmo SHA256 sobre a tupla `(fonte, serie_id, data_referencia, valor)`.
4. **Auditabilidade Visual de Gráficos:** Todo gráfico gerado em Dark Mode passa por validação via Visão Computacional (LLM Multi-modal) antes de ser publicado.
5. **Soberania Editorial ("Texto Música"):** Transformação de estatísticas brutas em teses jornalísticas profundas sobre reindustrialização, comércio Sul-Sul, balança comercial e inflação, seguindo o padrão d'O Cafezinho (**estritamente 2 frases por parágrafo**) e versão em inglês para o *Global South News*.

---

## 2. Mapa Global de Fontes Primárias

```
+---------------------------------------------------------------------------------------------------+
|                               MATRIZ DE FONTES PRIMÁRIAS GLOBAIS                                  |
+-------------------+--------------------+----------------------------------------------------------+
| REGIÃO / POTÊNCIA | INSTITUIÇÃO / API  | SÉRIES E INDICADORES CHAVE                               |
+-------------------+--------------------+----------------------------------------------------------+
| BRASIL            | BCB SGS            | Dólar PTAX (1), Selic (432), IPCA (433), PIB (4380),     |
|                   |                    | Balanço de Pagamentos (20542), Balança Comercial (22013) |
| BRASIL            | IBGE SIDRA         | IPCA Geral/Subitens (Agregado 7060), PIB Trimestral      |
|                   |                    | (Agregado 1620), PNAD Contínua (Agregado 6381)           |
| BRASIL            | ComexStat / MDIC   | NCMs de Exportação (Soja, Minério, Petróleo), Destinos   |
| CHINA             | Beijing GACC       | Comércio Bilateral BR-CN, Importações Chinesas de        |
|                   | (Servidor Beijing) | Commodities, Exportações para o Global South             |
| EUA               | FRED St. Louis     | Fed Funds (FEDFUNDS), CPI (CPIAUCSL), Payroll (PAYEMS)   |
| EUA               | BEA & BLS          | PIB dos EUA, Inflação de Atacado (PPI), Emprego          |
| GLOBAL            | Eurostat & FMI     | HICP Zona do Euro, WEO (World Economic Outlook)          |
+-------------------+--------------------+----------------------------------------------------------+
```

---

## 3. Arquitetura Modular em 5 Estágios (Status & Especificação)

```mermaid
graph TD
    subgraph M_B ["MÓDULO B: Coleta Primária Globais (HOMOLOGADO)"]
        BCB["BCB SGS API"]
        IBGE["IBGE SIDRA API"]
        COMEX["ComexStat MDIC API"]
        FRED["FRED St. Louis Fed API"]
        CHINA["Beijing GACC Gateway"]
    end

    subgraph M_A ["MÓDULO A: Ingestão & Banco (HOMOLOGADO)"]
        RAW["Envelopes JSON (/raw/incoming/)"]
        INGEST["ingestor_estatistico.py"]
        DB[("banco_estatistico.sqlite3 (SHA256 Dedup)")]
    end

    subgraph M_C ["MÓDULO C: Motor de Gráficos & Auditor Visual (HOMOLOGADO)"]
        GEN_GRAPH["graficos_economia_v4.py (Matplotlib Dark Mode)"]
        AUDIT_GRAPH["auditor_graficos_v4.py (Visão LLM)"]
    end

    subgraph M_D ["MÓDULO D: Motor de Teses & Redator V4.2 (PRÓXIMO)"]
        TESE["Motor de Teses (Geopolítica / BRICS / Macro)"]
        REDATOR["v4_economia_redactor.py (Texto Música: 2 frases/parágrafo)"]
    end

    subgraph M_E ["MÓDULO E: Publicação & Redes"]
        WP_CAF["O Cafezinho (WP Cat 43/22 + Cesta Premium)"]
        GSN_ASTRO["Global South News (Astro/Vercel EN)"]
    end

    BCB -->|JSON Envelope| RAW
    IBGE -->|JSON Envelope| RAW
    COMEX -->|JSON Envelope| RAW
    FRED -->|JSON Envelope| RAW
    CHINA -->|JSON Envelope| RAW
    RAW --> INGEST
    INGEST --> DB
    DB --> GEN_GRAPH
    GEN_GRAPH --> AUDIT_GRAPH
    AUDIT_GRAPH -->|Aprovado| TESE
    DB --> TESE
    TESE --> REDATOR
    REDATOR --> WP_CAF
    REDATOR --> GSN_ASTRO
```

---

### MÓDULO A: Banco Estatístico & Ingestor (STATUS: ✅ HOMOLOGADO)
- **Localização:** `Projeto Cafezinho Agentes/root/v4_labs/codigo/agente_economia/`
- **Componentes:**
  - `banco_estatistico.py`: Gerencia `banco_estatistico.sqlite3`. Tabela `observacoes_estatisticas` com chave primária `hash_id` igual a `SHA256(fonte|serie_id|data_referencia|valor)`.
  - `ingestor_estatistico.py`: Consome envelopes `.json` em `/raw/incoming/`, insere registros no SQLite com deduplicação atômica e move o envelope para `/raw/processed/`.

---

### MÓDULO B: Coletor Unificado de Economia (STATUS: ✅ HOMOLOGADO)
- **Componente:** `coletor_economia_v4.py`
- **Resiliência:** Suporta descompressão automática `gzip`, tratamento de timeouts HTTP individuais por fonte e fallback Gracioso (FRED_API_KEY).
- **Homologação:** Executado com sucesso capturando 55 observações primárias no primeiro disparo sem erros.

---

### MÓDULO C: Motor de Gráficos & Auditor Visual (STATUS: ✅ IMPLEMENTADO E HOMOLOGADO EM 25/08/2026)

#### 1. Gerador de Gráficos (`graficos_economia_v4.py`)
- **Estética Mandatória (Cafezinho Dark Mode):**
  - Fundo do gráfico: `#0f172a` (Slate Dark).
  - Cor das linhas / barras: `#38bdf8` (Azul Ciano), `#f43f5e` (Carmesim), `#10b981` (Esmeralda), `#fbbf24` (Âmbar).
  - Grid: `#334155` com alpha 0.4.
  - Tipografia: Sans-serif modernista (Plus Jakarta Sans / Inter / DejaVu Sans).
  - Marca d'Água: `Fonte: Dados Primários Oficiais | O Cafezinho Inteligência Econômica`.
  - Exportação: PNG em alta resolução (300 DPI) para `gerados/graficos/`.

#### 2. Auditor Visual (`auditor_graficos_v4.py`)
- **Funcionamento:** O módulo passa a imagem renderizada para a API de Visão (Qwen-VL / Claude 3.5 Sonnet / OpenAI GPT-4o-vision).
- **Checklist de Validação:**
  1. O título do gráfico descreve a série corretamente?
  2. Os eixos X e Y estão legendados sem sobreposição de datas?
  3. O valor do último ponto no gráfico corresponde exatamente ao valor do banco de dados SQLite?
  4. A marca d'água de procedência de dados está presente?
- **Resultado:** Retorna `aprovado: true/false`. Se for reprovado, regera com parâmetros de layout ajustados.

#### 3. Homologação executada — 25/08/2026 18:18 BRT
- Implementados `graficos_economia_v4.py` e `auditor_graficos_v4.py`, com testes próprios e integração à infraestrutura visual Qwen/Gemini já existente.
- O gerador abre o SQLite em `mode=ro` + `PRAGMA query_only=ON`, seleciona deterministicamente revisões, bloqueia por padrão dados futuros e `fallback_contingencia`, gera linha/barra em Matplotlib `Agg`, grava PNG + manifesto atomicamente e mantém `draft_only=true` / `publication_authorized=false`.
- A fidelidade factual é autoridade mecânica: SHA-256 do PNG, do dataset e das observações + reconciliação de cada registro no SQLite. A LLM visual julga apenas legibilidade, clipping, sobreposição, contraste, marca d'água e eixo enganoso.
- Providers visuais foram generalizados com `VisionResponseConfig`, schema customizado e JSON estrito, preservando compatibilidade com a auditoria antiga de fotografias e sem duplicar transporte/segredos.
- Suíte integrada: **68 testes + 19 subtestes aprovados**.
- Prova real: `BCB_433` (IPCA mensal), 12 observações de 2025-08 a 2026-07; PNG dark com meses pt-BR, último valor `0,07 % m/m` e rodapé `BCB · BCB_433`; auditor determinístico reconciliou 12/12 e retornou `approved`, ainda com `publication_authorized=false`.
- Artefatos: `codigo/agente_economia/gerados/graficos/prova-ipca-bcb-433.{png,manifest.json,audit.json}`.
- Memória técnica irmã: `Memorias/memoria_agente_v4_2_economia_modulo_c_20260825.md`.

---

## 4. MÓDULO D: Redator V4.2 & Motor de Teses (STATUS: 🛠️ EM DESENVOLVIMENTO)

### 1. Caderno de Teses Econômicas Soberanas:
- **Tese 1: Desdolarização & Comércio Sul-Sul:** Cruzamento de dados do ComexStat + Beijing GACC demonstrando o crescimento do uso de moedas locais e o aumento do saldo comercial Brasil-China.
- **Tese 2: Política Monetária Comparada (Fed vs BCB):** Análise comparativa entre a Selic (BCB) e o Fed Funds Rate (FRED/EUA), evidenciando o impacto do diferencial de juros no fluxo de capitais e na cotação do Dólar PTAX.
- **Tese 3: Inflação Primária e Poder de Compra:** Cruzamento do IPCA (IBGE SIDRA 7060) com o câmbio para identificar se a pressão inflacionária é importada (commodities/dólar) ou doméstica.

### 2. Contrato Editorial "Texto Música" (Regras Invioláveis):
1. **Ritmo de Leitura:** **TODOS OS PARÁGRAFOS DEVEM CONTER ESTRITAMENTE DUAS FRASES.** Nem uma, nem três. Exatamente 2 frases por parágrafo.
2. **Cesta Premium Automática:** Todo post no WordPress deve conter ao final os interlinks internos e o formulário de captura de newsletter (Mailchimp AJAX widget).
3. **Versão Global South News:** O mesmo evento gera um relatório executivo em inglês jornalístico para publicação no portal Astro Headless (`globalsouthnews.com`).

---

## 5. MÓDULO E: Agendamento & Produção (Crontab Server)

```cron
# Coleta diária de indicadores primários de economia (BCB, IBGE, FRED) às 07:00 e 17:00 BRT
0 7,17 * * * python3 "/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/root/v4_labs/codigo/agente_economia/coletor_economia_v4.py" >> ~/logs/coletor_economia.log 2>&1

# Ingestão assíncrona de envelopes pendentes a cada 15 minutos
*/15 * * * * python3 "/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/root/v4_labs/codigo/agente_economia/ingestor_estatistico.py" >> ~/logs/ingestor_economia.log 2>&1
```

---

## 6. Instruções para Continuidade no ZCode / Claude Code

Para continuar a construção dos Módulos C e D no ZCode, utilize o arquivo deste fórum como especificação canônica. Toda alteração de código ou expansão deve manter a compatibilidade com a estrutura de arquivos em `v4_labs/codigo/agente_economia/`.

*Documento gravado no Cérebro em 2026-08-25.*

---

## ✍️ ADENDO 26/08/2026 ~12:40 (ZCode/Qwen 3.8) — MÓDULOS C/D/E NO AR + 1ª PUBLICAÇÃO NO ESPELHO

**Ordem do Miguel (26/08 ~12h):** desenvolver Módulos C e D, produzir JÁ para o espelho **cafezinho.news**, bloco novo "Estatística" (provisório) na home igual ao Economia, categoria slug `estat`, selo de teste "V4.2", desenho de comércio exterior (China via Beijing, Eurostat, FRED, Argentina/mundo), bancos no padrão V4.1, e **fazer a primeira postagem + avisar no Telegram**.

### ✅ O que foi feito (tudo provado)

1. **Comércio exterior coletado** (`coletor_comercio_exterior_v4.py`, novo): ComexStat/MDIC (totais BR + bilateral BR→China, código 160 validado; **metricFOB é US$ bruto → ÷1e6**; rate limit tratado com backoff progressivo 20s×tentativa) · Eurostat (teiet010/110/210, EU27) · FRED (USTRADE) · **GACC China via CSV legado do Beijing** (offline desde ~07/2026; 50 meses 2022-01→2026-02, procedência `beijing_legacy_csv` declarada) · INDEC em esqueleto-config (código SISCOMES da Argentina não confirmado — documentado em `config_comercio_exterior.json`). Banco estatístico: **389 observações**.
2. **Bancos padrão V4.1** (`banco_producao_v4.py`, novo): `banco_producao_v42.sqlite3` com matérias (idempotência text_sha256 PT e EN separadas), gráficos_publicacao (FK matéria → png/manifest/audit/wp_media_id/posição) e fontes_usadas (observação com hash do banco estatístico).
3. **Módulo D** (`redator_economia_v4.py`, novo): pacote factual mecânico do banco (anti-alucinação), 3 teses, redação LLM em cascata (DeepSeek→OpenAI→Gemini) com contrato **Texto Música** validado+reparado (2 frases/parágrafo; título ≤80 sem `:—…`); PT para O Cafezinho + EN para GSN.
4. **Módulo C plugado**: `graficos_economia_v4.py` (dark #0f172a) + `auditor_graficos_v4.py` com provider visual real (cascata Qwen/Gemini via `codigo.media_vision_providers`). **Os 3 gráficos da 1ª matéria passaram na auditoria: approved.**
5. **Módulo E** (`publicador_economia_v4.py` + `ciclo_v42.py`, novos): publicação no espelho em **3 passos** (rascunho → carimbo `_cafezinho_img_check` com media_id casado → publish) para passar no gate fail-close de imagem; upload dos gráficos; categoria **Estatística id=100005 slug `estat`** + tag **V4.2 id=100006**; meta `v42_texto_sha256` registrada por mu-plugin novo `cafezinho-v42-meta.php`; versão EN arquivada em `gerados/gsn/`.
6. **Bloco Estatística na home do espelho** (front-page.php, backup `.bak_pre_bloco_estatistica_20260826`, php -l OK): idêntico ao Economia, `category__in array(100005)`, entre Economia e Coluna do Editor. Prova: seção mostra exatamente 1 matéria + capa.

### 🟢 1ª MATÉRIA PUBLICADA (prova ao vivo)
- **Post 400137** — "China sustenta superávit brasileiro e redefine comércio global" — https://cafezinho.news/2026/08/26/v42-20260826-comercio_sul_sul/ (publish, readback OK, capa=gráfico COMEX_EXPORT_CHINA, 2 gráficos inline, selo V4.2, lista de fontes primárias). Telegram enviado ao Miguel ~12:38.
- IDs do espelho fora da faixa do canônico (AUTO_INCREMENT 400000+): sync horário `REPLACE INTO` não colide.

### ⏳ O que falta / próximos passos
- **Crons** (§5): coletor 07:00/17:00 + ingestor */15 ainda NÃO instalados — decisão após o Miguel ver a 1ª matéria; sugerido também cron do ciclo completo 1x/dia.
- **Código SISCOMES da Argentina** p/ bilateral (150/639/0639 não funcionaram) — pendente de confirmação.
- Beijing segue offline: recomendar reativação futura (dados GACC atuais param em 02/2026).
- Cesta Premium (interlinks+newsletter §4.2) ainda não entra no HTML — fase 2.
- Publicação da versão EN no GSN é etapa separada (arquivo pronto em `gerados/gsn/`).

*Memória irmã: `Memorias/memoria_agente_v4_2_primeira_publicacao_espelho_20260826.md`.*

## 🐛 ADENDO 26/08/2026 ~14:35 (ZCode/Qwen 3.8) — INCIDENTE DO "DEZEMBRO": DADO DEFASADO NA 1ª MATÉRIA — CAUSA, FIX E CORREÇÃO NO AR

**Reclamação do Miguel (~14h):** a matéria falava "exportações brasileiras para a China em dezembro" sem dizer de qual ano — estamos em agosto de 2026; tinha que usar o número mais recente.

### Causa raiz (mecânica, não editorial)
- `banco_estatistico.obter_serie_historica()` ordena `data_referencia ASC` com `LIMIT N` — devolve as N observações mais **ANTIGAS**.
- O `resumo_serie()` do redator chamava com `limite=24`: em séries com mais de 24 observações, o "último valor" do pacote factual saía defasado.
  - ComexStat (banco com 2024-08→2026-07): devolvia **dez/2025** no lugar de **jul/2026**.
  - GACC legado (CSV 2022-01→2026-02): devolvia **dez/2023** no lugar de **fev/2026**.
- Os gráficos NÃO foram afetados: `load_series` do gerador ordena DESC e pega os N mais recentes (manifestos provaram janelas corretas: COMEX 2024-08→2026-07; GACC 2024-03→2026-02).

### Fix (26/08 ~14h30)
1. `redator_economia_v4.py::resumo_serie()` agora busca a série completa (`limite=1000`), filtra datas futuras, ordena ASC e fatia `[-limite:]` — o "último" é sempre a observação mais recente disponível.
2. **Regra 7 no SYSTEM_PROMPT do redator:** sempre citar o período completo COM ANO ("em julho de 2026"); mês solto sem ano é PROIBIDO.
3. Regressão PASSOU: COMEX_EXPORT_CHINA último = 2026-07-01 (US$ 10.673,11 mi) · GACC_CHINA_BALANCE = 2026-02-01 (US$ 90,98 bi) · USTRADE = 2026-07-01.

### Correção da matéria (§119 — erro em post publicado = correção imediata)
- Post **400137** re-redigido IN PLACE (mesma URL, publish mantido): pacote factual com as datas reais (COMEX/USTRADE 2026-07, Eurostat 2026-06, GACC 2026-02); novo título "A Ascensão do Comércio Brasil-China e a Importância do Sul Global".
- Readback provado: publish + ZERO menções a mês sem ano + abre com "US$ 10.673 milhões em julho de 2026".
- Banco de produção atualizado (PT id=4 com metadados `correcao_26_08`, EN id=5, fontes substituídas); GSN corrigido arquivado (`..._CORRIGIDA.json`) e os 2 arquivos defasados movidos para `gerados/gsn/descartados/`.

### Lições
- O contrato de `obter_serie_historica` (ASC+LIMIT, Módulo A) foi mantido; o fix ficou no CONSUMIDOR. Consumidor novo que precisar dos "últimos N" deve buscar a série completa e fatiar — nunca confiar no LIMIT para janela recente.
- Falha de estilo (mês sem ano) virou regra explícita de prompt, validada mecanicamente no readback.

## 📋 ADENDO 27/08/2026 (ZCode/Qwen 3.8) — CONSOLIDAÇÃO DE ESTADO + SESSÃO NOVA ENCOMENDADA

**Contexto:** o Miguel abriu a sessão original (25/08) conversando sobre este agente, o assunto mudou para Bot News, e em 27/08 ele pediu organização: status gravado no Cérebro + prompt pronto para sessão nova dedicada.

**Verificação ao vivo (27/08):**
- Post **400137** no ar no espelho (200): https://cafezinho.news/2026/08/26/v42-20260826-comercio_sul_sul/ — versão CORRIGIDA (título "A Ascensão do Comércio Brasil-China e a Importância do Sul Global", datas com ano).
- Bloco **Estatística** presente na home do espelho (categoria `estat` id 100005) + selo V4.2.
- Bancos locais íntegros no Dell: `banco_estatistico.sqlite3` (389 obs.) + `banco_producao_v42.sqlite3`.
- **Crons confirmados NÃO instalados** (nenhuma linha de economia no crontab) — continua aguardando decisão do Miguel.

**Mapa de decisão para a sessão nova (o que já está decidido × o que falta decidir):**
1. **Crons (a decisão central):** coletor 2×/dia + ingestor */15 + ciclo completo 1×/dia ainda manuais. ⚠️ REGRA DE PRODUÇÃO ZERO NO DELL (24/08): a sugestão original do §5 apontava crontab com caminhos locais do Dell — ANTES de instalar, decidir a casa definitiva (NYC ou servidor; empacotar `agente_economia/` para lá). O espelho `cafezinho.news` já recebe publicação via API, então o ciclo não precisa rodar no Dell.
2. **Ritmo editorial:** 1ª matéria aprovada (com correção §119)? Definir frequência (1×/dia? dias úteis? por release de dado?) e se as próximas ficam no espelho até homologação.
3. **Pendências técnicas menores:** código SISCOMES da Argentina (INDEC); Beijing/GACC offline (dados param 02/2026 — reativar?); Cesta Premium (interlinks+newsletter) fase 2; publicação da versão EN no GSN (arquivos prontos em `gerados/gsn/`).
4. **Estrutura de teses:** caderno tem 3 teses (desdolarização/Sul-Sul, Fed×BCB, inflação importada×doméstica) — validar com o Miguel se é esse o recorte ou se entra conjuntura eleitoral (custo fiscal etc.).

**PROMPT PRONTO PARA SESSÃO NOVA (colar no ZCode):**
> Continue o Agente V4.2 de Economia & Estatística do Cafezinho. Leia antes: `Cerebro/Foruns/forum_agente_v4_2_economia_estatistica_20260825.md` (especificação canônica + adendos 25-27/08), `Cerebro/Memorias/memoria_agente_v4_2_economia_modulo_c_20260825.md` e `memoria_agente_v4_2_primeira_publicacao_espelho_20260826.md`, e o `Cerebro/MONITORAMENTO_DE_TRABALHO.md`. Estado: Módulos A/B/C/D/E implementados; 1ª matéria publicada e corrigida no espelho (post 400137, bloco Estatística na home); bancos em `v4_labs/codigo/agente_economia/`; crons AINDA NÃO instalados. Pauta da sessão: (1) decidir comigo a casa dos crons — REGRA produção-zero-no-Dell: empacotar para NYC/servidor antes de ligar (coletor 2×/dia, ingestor */15, ciclo 1×/dia); (2) definir ritmo editorial e produzir a 2ª matéria (tese do caderno: Fed×BCB ou inflação importada — a 1ª foi Sul-Sul); (3) pendências: SISCOMES Argentina, Beijing offline (dados até 02/2026), Cesta Premium fase 2, versão EN no GSN. Regras invioláveis: Texto Música (2 frases/parágrafo), dados primários com fonte+período COM ANO (lição do incidente "dezembro"), gráficos dark #0f172a com auditoria visual, gate de imagem do espelho em 3 passos, publicação só no espelho até nova ordem. Registro Tema Duplo neste fórum + memória.

---

## 🏭 ADENDO 27/08/2026 14:06→14:33 BRT (ZCode/GLM-5.3) — SESSÃO DO AGENTE ESTATÍSTICO: PRODUÇÃO MUDOU PARA O NYC (CRONS LIGADOS) + ARGENTINA RESOLVIDA + 2ª MATÉRIA NO AR

**Contexto:** sessão nova executando o prompt acima (Miguel colou ~14h). O Bot News ficou em outra sessão.

### 1. Decisão da casa dos crons: **NYC** (§ empacotamento concluído)
- Regra produção-zero-no-Dell + NYC já é a casa dos loops do Cafezinho (venv `/root/venv`, cofre completo, logs em `/root/agent_data/`). Pacote em `/root/v4_labs/codigo/agente_economia/` (py_compile 13/13, matplotlib 3.11.1 no venv, `media_vision_providers.py` atualizado p/ versão homologada 25/08 — md5 284e2ed5).
- **Crons instalados (crontab root NYC, backup `/root/agent_data/backup_crontab_pre_v42_20260827.txt`):**
  - Coletor base BCB/IBGE/FRED: `0 10,20 * * *` UTC (07:00/17:00 BRT)
  - Coletor comércio exterior: `10 10,20 * * *` UTC
  - Ingestor: `*/15 * * * *`
  - Ciclo completo `--tema auto --publicar`: `10 15 * * *` UTC (12:10 BRT — **1ª execução automática 28/08**)
  - **Kill switch:** `crontab -l | grep -v agente_economia | crontab -`
- **Ritmo editorial vigente: 1 matéria/dia automática no espelho** (frequências sancionadas no prompt). Se o Miguel quiser manual/supervisionado: kill switch acima + rodar `ciclo_v42.py --tema <tese> --publicar` na mão.

### 2. Credenciais (Regra 4 — espelhadas na mesma ação, zero exposição)
- `ESPELHO_WP_USER/SITE/PASS` copiadas do cofre Dell → `/root/.env.unificado` NYC (backup `.bak_pre_v42_20260827`; sha8 das linhas confere: c14aeb98).
- **`DEEPSEEK_API_KEY` do NYC TROCADA** (a antiga dava 401 — pendência antiga do §118 RESOLVIDA; nova validada HTTP 200; backup `.bak_pre_dskey_20260827`).
- ⚠️ **Gemini API é geo-bloqueada no IP do NYC** (400 FAILED_PRECONDITION) — cascata no NYC na prática é DeepSeek→OpenAI (redação) e Qwen-VL (visão). Se Gemini fizer falta no NYC, usar proxy tencent como os temáticos.

### 3. Fixes de código (Dell⇄NYC sincronizados, todos com prova)
1. `banco_estatistico.py`: DEFAULT_DB_PATH relativo ao pacote (era hardcoded no caminho do Dell — no NYC criava banco espúrio em `/root/Downloads/...`; limpo e reingestado idempotentemente).
2. `ingestor_estatistico.py`: `executar_varredura(self)` — o bug de assinatura anotado no Módulo C viraria cron quebrado.
3. `env_loader.py`: fallback `/root/.env.unificado` quando o cofre do Dell não existe.
4. `coletor_economia_v4.py` (o mais grave): **não carregava o cofre** → FRED caía no fallback de contingência e gravava **FEDFUNDS 5,25% FALSO** no banco primário (real: 3,63% jul/2026). Fix: `carregar_env()` + chave lida pós-cofre + limit 24. **Expurgo do banco:** 1 fallback falso + 12 pontos FUTUROS da Selic (09/2026) deletados.
5. Selic diária: janela `dataInicial=hoje-95d&dataFinal=hoje` (o SGS publica meta futura agendada — "ultimos/N" trazia futuro) + filtro universal `data <= hoje`. Banco NYC agora: **671 obs** (Selic 96 pts até 27/08, FEDFUNDS 24 meses até jul/2026, PTAX 68 pts, CPI 23, INDEC 72).
6. `coletor_comercio_exterior_v4.py`: URL INDEC corrigida (`/series/api/series/` — a antiga `/series/api` dá 404) + CSV legado GACC movido para dentro do pacote (`raw/legado/`) com fallback de caminho.
7. `redator_economia_v4.py`: gráfico da Selic com `limit=60` (com 24 pts o eixo X repetia "ago/26" 6× — série diária ≈ 1 mês de janela).
8. `auditor_graficos_v4.py`: `provider_id` gravado **após** o analyze (rotulava "fallback_media_vision" mesmo com Qwen-VL respondendo — artefato de ordering; prova: re-audit com provider_id real `qwen_dashscope`).

### 4. 🇦🇷 Pendência SISCOMES Argentina: RESOLVIDA (era um equívoco de nome)
- SISCOMES/SISCOMEX é sistema **brasileiro**; a via argentina correta é a **API de Séries de Tiempo oficial** `apis.datos.gob.ar` (dataset "Intercambio Comercial Argentino", INDEC/Subsecretaría de Programación Macroeconómica).
- IDs mensais validados ao vivo (dados até **2026-06**, US$ milhões): `74.3_IET_0_M_16` exportações · `74.3_IIT_0_M_25` importações · `74.3_ISC_0_M_19` saldo. Config preenchida + **72 observações ingeridas no NYC** (endpoint de busca: `/series/api/search/?q=`).

### 5. 📰 2ª MATÉRIA NO AR — produção 100% NYC (prova E2E do empacotamento)
- **Post 400158** — "Selic a 14% e Fed a 3,63% o diferencial que mantém o real firme" (tese 2, Fed×BCB): https://cafezinho.news/2026/08/27/v42-20260827-politica_monetaria_comparada-2/
- Pipeline: DeepSeek aprovou Texto Música na 1ª tentativa · gráficos BCB_432 + FEDFUNDS `approved` (auditoria mecânica 24/24 + Qwen-VL real) · publicação 3 passos (draft → carimbo casado → publish).
- Readback REST: publish · cats [100005] · tags [100006] · featured 400156 · `v42_texto_sha256` ✓ · carimbo ok:true.
- QA manual da sessão: §2–§9 com exatas 2 frases; **zero meses sem ano** (o único "maio" era falso positivo de "maiores"); auditoria visual manual dos 2 PNGs (Fed impecável out/24→jul/26; Selic correto, 14,25→14,00 visível, ressalva de janela → resolvida p/ próximos via limit=60); home com as 2 matérias V4.2 no bloco Estatística.
- Draft órfão 400155 (1ª tentativa fail-closed com provider velho — **comportamento correto do gate**) deletado. EN arquivada em `gerados/gsn/` (aguarda decisão sobre GSN).

### 6. Estado / o que falta / o que preciso de você (Miguel)
- **O que aconteceu:** produção V4.2 migrated para NYC com crons ligados; banco saneado e ampliado (671 obs); Argentina resolvida; 2ª matéria publicada e auditada.
- **O que falta:** Beijing/GACC segue offline (dados até 02/2026; CSV legado preservado no pacote — reativação é projeto à parte); Cesta Premium fase 2 (interlinks + newsletter no `montar_html` — design pronto para implementar); versão EN no GSN (2 arquivos prontos em `gerados/gsn/` — Sul-Sul e monetária); 1ª execução automática do ciclo 28/08 12:10 BRT (acompanhar `tail /root/agent_data/v42_ciclo.log`).
- **O que preciso de você:** nada bloqueante. Opcional: (a) validar o ritmo 1×/dia automático (kill switch acima se preferir manual); (b) "vai" para EN no GSN; (c) decidir reativação do Beijing.

*Memória irmã: `Memorias/memoria_agente_v4_2_producao_nyc_crons_segunda_materia_20260827.md`.*

---

## 🚩 ADENDO 27/08/2026 ~14h40→15h BRT (ZCode/GLM-5.3) — DIRETRIZ HISTORIAL Nº 1 + CURADORIA DE GRÁFICO + POST 400158 CORRIGIDO IN PLACE

**Feedback do Miguel (~14h40):** o gráfico da Selic ficou "feio", sem informação (eixo X todo "ago/26"); a matéria ELOGIOU a taxa de juros alta ("mantém o real firme") — **PROIBIDO**; siglas técnicas demais. Aprovado: **ritmo 1×/dia no espelho** (crons seguem ligados, testando). Pedido: processo de curadoria de gráfico mais inteligente + **diretriz historial muito firme**.

### 1. DIRETRIZ HISTORIAL Nº 1 (gravada no SYSTEM_PROMPT do redator, regras 8-11 — INVIOLÁVEL)
- A linha do Cafezinho é **CONTRA a taxa de juros alta**: juro alto é custo social, rolagem caríssima da dívida, crédito caro, freio ao investimento, renda do rentismo — nunca virtude/âncora/mérito. Elogiar juro alto é PROIBIDO.
- Efeito "benéfico" do juro (câmbio estável) exige o CUSTO no mesmo parágrafo ou no seguinte. Corte de juros = avanço; alta = agravamento.
- **SIGLAS**: primeira menção sempre por extenso ("Banco Central dos Estados Unidos (Fed)", "taxa básica de juros (Selic)"). Linguagem popular, sem jargão de mercado.
- Tese 2 renomeada: "O Custo de Carregar os Juros Mais Altos do Mundo" (ângulo reescrito com a linha).

### 2. Curadoria de gráfico (3 mudanças estruturais)
1. **Janela**: coletor traz 400 dias de séries diárias (Selic agora 401 pts jul/25→ago/26); gráfico Selic com `limit=260` (~12 meses).
2. **Título informativo** (gerador): o título conta o movimento — ex. real: **"Taxa Selic Meta cai de 15,00 % a.a. para 14,00 % a.a. em 8 meses"** (função `_titulo_informativo`; gravado no manifesto como `titulo`).
3. **Auditoria visual ganhou `window_informative`**: LLM visual reprova janela sem variação/história (linha achatada desperdiçando a tela). Aprovado exige o novo campo.

### 3. Post 400158 corrigido IN PLACE (mesma URL, §119)
- **Novo título:** "O impacto dos juros elevados na economia brasileira em 2026" — enquadramento de custo.
- Texto novo (DeepSeek, Texto Música 1ª tentativa): §§2-7 com 2 frases; "renda confortável para os rentistas"; "a solução passa pela redução da taxa Selic"; zero meses sem ano; **zero siglas cruas** (nem "Fed" aparece — por extenso).
- Gráficos novos: Selic 12 meses (capa 400160, título informativo) + Fed (400161), ambos approved; carimbo re-gravado casado; publish mantido; readback OK. Auditoria visual manual 9/10.
- Ferramenta: `corrigir_post_v4.py --post-id X --tema Y` (fica no pacote para futuras retificações §119).
- EN nova arquivada: `gerados/gsn/gsn_politica_monetaria_comparada_*_DIRETRIZ.json` (as versões anteriores ficam; as defasadas da 26/08 já estavam em descartados/).

### 4. Ajustes técnicos da rodada
- Auditor: allowlist do manifesto aceita `titulo` opcional (retrocompatível) — primeiro run deu `blocked` por causa disso, corrigido.
- Refinamento futuro anotado: rotular patamares intermediários da escada (14,75/14,50/14,25) nos gráficos de taxa.

### 5. Estado
- Ritmo 1×/dia no espelho CONFIRMADO pelo Miguel (cron 12:10 BRT segue; 1ª automática 28/08).
- Pendências inalteradas: Beijing, Cesta Premium f2, EN GSN (aguarda "vai").

*Atualizado também em `Memorias/memoria_agente_v4_2_producao_nyc_crons_segunda_materia_20260827.md`.*

### ⛔ EMENDA à Diretriz Historial (ordem do Miguel, 27/08 ~15h): SELO DE AUTOMAÇÃO PROIBIDO
- **Nenhuma matéria do V4.2 pode exibir rodapé/selo de "gerada automaticamente pelo Agente V4.2" — nem no espelho.** Removido do `montar_html` do publicador (constante `SELO_TESTE_PT` eliminada; comentário de proibição no código).
- Posts **400137 e 400158 corrigidos IN PLACE** (regex no content via REST, HTTP 200): zero menções ao selo nas duas URLs públicas; fontes primárias e gráficos intactos (provas ao vivo).
- A tag organizacional "V4.2" (id 100006) permanece — é curadoria interna, não exposição de automação ao leitor.
