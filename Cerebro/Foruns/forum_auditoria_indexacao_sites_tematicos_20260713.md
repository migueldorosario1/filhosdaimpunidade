# 🩺 Fórum — Auditoria de Indexação e Conformidade dos Sites Temáticos (2026-07-13)

> **Status:** ✅ **Concluído e Homologado**  
> **Escopo:** Configuração de SEO, segurança e infraestrutura do enxame de agentes temáticos em NYC.

---

## 📋 1. Visão Geral da Rede de Portais Satélites

A rede de portais satélites e experimentos de publicação foi completamente auditada e estabilizada no ambiente de produção de Nova York (NYC). O objetivo principal desta rodada foi garantir que os sites temáticos primários sejam indexados pelo Google para captação orgânica de audiência, enquanto o espelho sandbox `cafezinho.news` permanece protegido por senha e com bloqueios explícitos contra indexação para evitar canibalização SEO do domínio canônico `ocafezinho.com`.

---

## 📂 2. Mapeamento da Infraestrutura e Diretórios (NYC Droplet: 198.199.121.136)

Toda a infraestrutura foi centralizada no diretório `/agentes_tematicos/`, garantindo o desacoplamento completo da infraestrutura legada do WordPress:

| Portal | Domínio Principal | Repositório GitHub | Diretório no Servidor NYC | Indexação (Google) | Limite Diário |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Mundo Trilhos** | `https://mundotrilhos.com` | `migueldorosario1/mundo-trilhos` | `/agentes_tematicos/mundo_trilhos/` | `index,follow` (BaseHead.astro) | Max 2 posts/dia |
| **Rail Post** | `https://railpost.news` | `migueldorosario1/rail-post` | `/agentes_tematicos/rail_post/` | `index,follow` (BaseHead.astro) | Max 2 posts/dia |
| **Discover Brazil** | `https://discoverbrazil.news` | `migueldorosario1/discover-brazil` | `/agentes_tematicos/discover_brazil/` | `index,follow` (Nativo) | Max 2 posts/dia |
| **Cafezinho News** | `https://cafezinho.news` | N/A (Droplet `159.65.177.60`) | `/var/www/cafezinho-news/` | `noindex,nofollow` (Nginx Header) | N/A (Espelho) |

---

## 🔒 3. Políticas de Indexação e Acesso do Espelho Cafezinho News

Para garantir que o espelho `cafezinho.news` (hospedado no droplet secundário `159.65.177.60`) não concorra com a audiência canônica de `ocafezinho.com`, foram implementadas duas barreiras de segurança:

1. **Proteção por Senha (Basic Auth Nginx):**
   * **Login:** `cafezinho`
   * **Senha:** `000` (gerada via `openssl passwd -apr1` no arquivo `/etc/nginx/.htpasswd_cafezinho`).
2. **Bloqueio Explícito de Indexação:**
   * Injeção de cabeçalho HTTP Nginx: `add_header X-Robots-Tag "noindex, nofollow, noarchive" always;`.
   * Retorno HTTP 404 explícito para requisições de sitemaps XML gerados dinamicamente.
   * `robots.txt` com regra restritiva `Disallow: /`.

---

## ⚙️ 4. Regras de Controle de Publicação e GitOps

* **Limite de Publicações:** Implementação da função `check_daily_post_limit` que analisa tanto o histórico em JSON quanto o diretório de conteúdos local (`src/content/blog/`). O limite é estrito para **2 posts por dia** por agente.
* **Automação Headless:** As alterações nos arquivos Markdown e imagens geradas são sincronizadas com o GitHub via GitOps utilizando a credencial unificada `GITHUB_TOKEN_AIATOLAH_KIMI` configurada no ambiente unificado de produção.
* **Identidade de Commits:** Padronizada globalmente no servidor como `AIATOLAH KIMI <kimi@cafezinho.news>`.

---

> [!NOTE]
> Todos os testes de build local do Astro e push remoto foram validados com sucesso. A infraestrutura agora encontra-se em modo autônomo perene.
