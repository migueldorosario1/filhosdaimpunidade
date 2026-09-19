# Prompt Master para Pesquisa Paralela (GPT & Claude)

**Copie e cole o texto abaixo para os agentes:**

***

**Sua missão:**
Atue como um Especialista Sênior em Geopolítica, Economia e Cultura de Massa focado no Mercado de Petróleo. Nossa equipe técnica de agentes autônomos já mapeou e liberou a arquitetura de acesso a várias bases de dados essenciais, cujas credenciais e endpoints estão abaixo. 

Preciso que você conduza uma pesquisa profunda e extensa, combinando dados estatísticos frios, anedotas históricas da indústria e cultura pop. Seu objetivo final é consolidar essa pesquisa em um formato Markdown massivo e detalhado, que deverá ser salvo (ou estruturado para que eu salve) em um arquivo na nossa pasta `Foruns/` (sugestão de nome: `forum_pesquisa_profunda_petroleo_20260711.md`).

---

### 1. Contexto de Infraestrutura e Credenciais (Para o seu uso no Python/APIs, se necessário):
*   **Fontes Globais Abertas:** U.S. EIA API (balanço mundial e inventários), JODI-Oil Database (mensal), IEA e OPEC (relatórios abertos e MOMR).
*   **Fontes Brasil:** Portal de Dados Abertos ANP (produção do pré-sal "Do Poço ao Posto"), API Comex Stat (`api-comexstat.mdic.gov.br`) e IBGE PIA-Produto.
*   **Atalho de Datalake:** "Base dos Dados" via BigQuery para cruzar ANP e ComexStat.
*   **Alfândega Chinesa (GACC):** Nosso servidor em Beijing (Tencent Cloud, IP `82.156.167.218`, usuário `ubuntu`, alias `beijing`) já contém os robôs `cdp_v3.py` e `final_level3.py` na pasta `/home/ubuntu/` prontos para raspar o fluxo alfandegário dinâmico.

---

### 2. O Que Eu Quero no Artigo/Estudo Final:

**A. Hard Data, Economia e Geopolítica:**
*   Quero números atualizados de produção global, demanda, exportação e preços (Brent e WTI).
*   Detalhe a diferença fundamental, química e comercial, dos tipos de petróleo (Leve/Doce vs. Pesado/Ácido).
*   Faça um raio-x do Brasil (Peso do Pré-sal, imposto de exportação de março de 2026, refinarias e fluxo de importação vs exportação).
*   Crie uma seção longa e imersiva sobre a crise geopolítica de 2026 (bloqueio do Estreito de Ormuz, Guerra do Irã), detalhando o choque logístico que disparou o frete marítimo, o impacto global na inflação e o pico de preços (acima de US$ 130).

**B. Alma, História e Cultura (Storytelling):**
*   **Citações Reais:** Frases marcantes de líderes, executivos da OPEP, estadistas e historiadores sobre o petróleo ("O sangue da civilização", etc.).
*   **Anedotas e Histórias:** Traga histórias de bastidores de grandes choques do petróleo (1973, 1979 ou a descoberta do pré-sal).
*   **Filmes, Séries e Livros:** Quero uma curadoria profunda da cultura pop sobre o tema.
    *   *Séries & Filmes:* Forneça sinopses ricas, diretores, atores e roteiristas. **Crucial:** Descreva *cenas específicas* (ex: o diálogo genial entre George Clooney e Christopher Plummer em *Syriana*, o monólogo "I drink your milkshake" do Daniel Day-Lewis em *Sangue Negro/There Will Be Blood*). 
    *   *Livros:* Obras essenciais como *O Prêmio* (Daniel Yergin), detalhando seus principais insights.

Não economize caracteres. Seja enciclopédico, literário e jornalístico. Quando terminar, formate tudo em um belíssimo Markdown focado na alta legibilidade para consumo no nosso Cérebro de agentes.
