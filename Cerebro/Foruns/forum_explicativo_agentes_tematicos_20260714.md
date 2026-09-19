# Fórum Explicativo: Ecossistema de Agentes Temáticos (Julho 2026)

Este documento atua como o manual oficial e guia de auditoria para o ecossistema de **Sites Temáticos Autônomos** operando na infraestrutura do servidor de Nova York (NYC - `198.199.121.136`). 

O objetivo deste fórum é centralizar as informações arquiteturais, as regras de negócio, a política de indexação e o mapeamento dos scripts principais que foram compactados em [agentes_tematicos.zip](file:///home/migueldorosario/Downloads/Antigravity%20Google/Projeto%20Cafezinho%20Agentes/Foruns/agentes_tematicos.zip) para a análise e refatoração do Fable.

---

## 1. Visão Geral e Objetivos do Ecossistema

O ecossistema é composto por portais de nicho, construídos sob a arquitetura **Headless Astro + GitOps**, operados 100% por agentes autônomos Python rodando no servidor de Nova York.

| Site | URL / Domínio | Foco Editorial | Objetivo de Negócio |
| :--- | :--- | :--- | :--- |
| **Mundo Trilhos** | `https://mundodostrilhos.com` | Notícias ferroviárias, metroviárias e logística em Português. | Indexação orgânica acelerada e monetização via Google AdSense (Remuneração Google). |
| **Rail Post** | `https://railpost.news` | Notícias internacionais sobre infraestrutura de trens e ferrovias em Inglês. | Alcance global de nicho técnico e monetização programática. |
| **Discover Brazil** | `https://www.discoverbrazil.news` | Turismo brasileiro, cultura, culinária e guias de viagem em Inglês. | Atração de tráfego receptivo internacional e parcerias de afiliados/AdSense. |

### Metas Estratégicas
1. **Indexação Orgânica Total (`index,follow`)**: Ao contrário de outros projetos experimentais, todos os três sites temáticos devem ter seus conteúdos indexados imediatamente nos motores de busca (Google Search) para captação de tráfego orgânico.
2. **Remuneração AdSense**: A estruturação técnica do Astro atende rigidamente aos critérios do Web Vitals do Google, gerando páginas ultrarrápidas, sem JavaScript invasivo na renderização, prontas para aprovação rápida no Google AdSense.

---

## 2. Regras de Publicação e Frequência Diária

A frequência diária é restrita e monitorada para evitar spam e garantir a qualidade editorial.

* **Limite Rígido**: Exatamente **2 posts por dia** por site temático.
* **Mecanismo de Controle (`check_daily_post_limit`)**:
  - Antes de qualquer publicação, o agente consulta a pasta de blogs local (`src/content/blog/`) do repositório Astro e o arquivo de estado de publicação (`agent_data/estado_*.json`).
  - Conta o número de postagens cuja data corresponde ao dia de hoje (UTC/Local).
  - Se o total for $\ge 2$, a rodada é abortada silenciosamente, evitando sobrecarga de publicações.

---

## 3. Sistema Inteligente de Antiduplicação (Anti-Collision)

Para garantir que nenhuma matéria ou imagem repetida seja publicada nos portais, implementamos um sistema de segurança de dupla camada:

### A. Antiduplicação de Conteúdo (Fuzzy Title Match)
Em vez de comparar apenas slugs idênticos ou chaves primárias exatas, os agentes agora realizam uma comparação difusa (fuzzy match):
* **Algoritmo**: Utilização da biblioteca nativa `difflib.SequenceMatcher`.
* **Fluxo**: O agente varre os títulos de todos os arquivos `.md` presentes em `src/content/blog/` e no log histórico de memória (`PUB_MEMORY_FILE`).
* **Threshold de Bloqueio**: Se a similaridade de caracteres entre o título gerado e qualquer título histórico for **igual ou superior a 70% (0.7)**, a publicação é cancelada sob erro de duplicação.

### B. Antiduplicação de Imagens (MD5 Hashing)
Evita o reuso de fotos idênticas ou ilustrações similares baixadas da web ou geradas por IA:
* **Algoritmo**: Computação de hash MD5 (`hashlib.md5`).
* **Fluxo**: Ao baixar a imagem destacada (`img_url` ou arquivo local), o agente gera o hash MD5 dos bytes do arquivo.
* **Validação**: Compara contra uma lista acumulada de hashes MD5 das imagens presentes na pasta `public/hero/` do repositório.
* **Ação de Fallback**: Caso o hash já exista no repositório, o agente descarta a imagem repetida e associa o artigo à imagem de fallback padrão (`FALLBACK_HERO_IMAGE`) configurada para o portal.

---

## 4. Exclusão Crítica: O Caso do `cafezinho.news`

> [!WARNING]
> O domínio `cafezinho.news` **NÃO** faz parte do ecossistema de sites temáticos autônomos. Ele é apenas um espelho do portal principal (`ocafezinho.com`).

Para proteger a audiência e a integridade de SEO do domínio canônico (`ocafezinho.com`), foram impostas regras de isolamento no mirror:
1. **Bloqueio de Indexação**: Enforcamento de tags `noindex, nofollow` no cabeçalho HTML e no `robots.txt` para bloquear o Googlebot.
2. **Autenticação Básica**: Nginx configurado com autenticação restrita (`cafezinho` / `000`).
3. **Isolamento de Código**: Os scripts dos agentes temáticos não interagem e não compartilham chaves com a infraestrutura do mirror.

---

## 5. Mapeamento do Arquivo `agentes_tematicos.zip`

O arquivo [agentes_tematicos.zip](file:///home/migueldorosario/Downloads/Antigravity%20Google/Projeto%20Cafezinho%20Agentes/Foruns/agentes_tematicos.zip) contém os seguintes scripts copiados diretamente do servidor de Nova York para análise do Fable:

### Agentes Principais:
1. `MT_agente_ferroviario.py` (Mundo Trilhos): Gerencia a coleta, auditoria LLM, geração de imagem e GitOps para o portal Mundo dos Trilhos.
2. `agente_rail_post.py` (Rail Post): Executa a mesma rotina de publicação em inglês com foco na audiência internacional ferroviária.
3. `agente_turismo_embratur.py` (Discover Brazil): Responsável pela geração dos roteiros de viagem e pontos de lazer do Brasil em inglês.

### Dependências e Utilitários:
4. `agente_roteador_llm.py`: O roteador de inteligência do ecossistema, definindo ordens de ataque entre modelos (DeepSeek, Gemini, Qwen, GPT, Mistral) baseado na tarefa.
5. `carregar_chaves.py`: Módulo unificado para leitura e exportação de variáveis de ambiente (`.env.unificado`).
6. `gerador_imagem_editorial.py`: Pipeline de integração com geradores de imagem locais e APIs de IA.
7. `util_indexing.py`: Utilitário para acionamento de indexação imediata via Google Indexing API e ferramentas de busca.

---

> [!NOTE]
> Este arquivo ZIP e fórum servem de insumo para o Fable realizar análises profundas de arquitetura de software, refatoração de concorrência com `flock`, auditorias de qualidade de prompts e sincronização fina de concorrência.
