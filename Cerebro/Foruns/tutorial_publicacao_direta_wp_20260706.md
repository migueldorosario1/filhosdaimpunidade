# Tutorial Completo: Publicação Direta via REST API no WordPress

Este documento serve como um guia definitivo (e prompt) para ser colado em outras IAs, ensinando como publicar artigos diretamente nos sites da rede (O Cafezinho, Revista Fórum, Global South News, etc.) via API REST do WordPress.

## 1. Visão Geral da API do WordPress

O WordPress possui uma API REST nativa. Para publicar, você precisa de:
1. **URL do Endpoint**: `https://{SEU_SITE.COM}/wp-json/wp/v2/posts`
2. **Endpoint de Mídia** (para imagens): `https://{SEU_SITE.COM}/wp-json/wp/v2/media`
3. **Autenticação**: Basic Auth usando `Usuário` e `Application Password`.

## 2. Credenciais disponíveis (somente no cofre `.env.unificado`)

As senhas são *Application Passwords* usadas via Basic Auth. **Nunca copie o valor para este tutorial ou para scripts.** Carregue as variáveis do cofre canônico `Projeto Cafezinho Agentes/root/.env.unificado`.

### O Cafezinho
* **URL Base:** `https://controle.ocafezinho.com`
* **Endpoint de Posts:** `https://controle.ocafezinho.com/wp-json/wp/v2/posts`
* **Usuário atual:** variável `WP_USER_CAFEZINHO` (`redacao-nova`, validado em 27/07/2026)
* **Senha:** variável `WP_APP_PASSWORD_CAFEZINHO` ou `WP_PASS_CAFEZINHO`

### Global South News
* **URL Base:** `https://globalsouth.news`
* **Usuário/senha:** variáveis `GSN_WP_USER` / `GSN_WP_PASS`

### Discover Brazil
* **URL Base:** `https://discoverbrazil.news`
* **Usuário/senha:** variáveis `DISCOVER_BRAZIL_WP_USER` / `DISCOVER_BRAZIL_WP_PASS`

### Mapa Rio
* **URL Base:** `http://mapario.com.br`
* **Usuário/senha:** variáveis `MAPA_RIO_WP_USER` / `MAPA_RIO_WP_PASS`

### Rio Carta
* **URL Base:** `https://riocarta.com`
* **Usuário/senha:** variáveis `WP_USER_RIOCARTA` / `WP_PASS_RIOCARTA`

### Revista Fórum
* **URL Base:** `https://revistaforum.com.br` (Nota: a URL exata pode variar caso usem URL de controle, mas o padrão REST é sempre seguido por `/wp-json/wp/v2/posts`).
* *(O método para publicar na Revista Fórum é idêntico ao do Cafezinho; a IA só precisará receber do usuário final o Application Password e Usuário da Fórum).*

## 3. Como Publicar (Passo a Passo para a IA)

### Passo 1: Fazer Upload da Imagem Destacada (Opcional, mas recomendado)
Antes de criar o post, você pode enviar a imagem destacada para obter o `id` numérico da mídia.

```python
import requests
import os
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv("Projeto Cafezinho Agentes/root/.env.unificado")

url_media = "https://controle.ocafezinho.com/wp-json/wp/v2/media"
auth = HTTPBasicAuth(
    os.environ["WP_USER_CAFEZINHO"],
    os.environ["WP_APP_PASSWORD_CAFEZINHO"],
)

headers = {
    "Content-Disposition": "attachment; filename=imagem-destacada.jpg",
    "Content-Type": "image/jpeg"
}

with open("imagem.jpg", "rb") as f:
    res = requests.post(url_media, auth=auth, headers=headers, data=f)

media_id = res.json().get("id") # Guarde este ID para usar no post
```

### Passo 2: Publicar o Post
Com a mídia carregada (ou mesmo sem), construa o payload final.

```python
import requests
import os
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv("Projeto Cafezinho Agentes/root/.env.unificado")

url_posts = "https://controle.ocafezinho.com/wp-json/wp/v2/posts"
auth = HTTPBasicAuth(
    os.environ["WP_USER_CAFEZINHO"],
    os.environ["WP_APP_PASSWORD_CAFEZINHO"],
)

# Payload em JSON com os dados da publicação
payload = {
    "title": "Seu Título Aqui",
    "content": "<!-- wp:paragraph --><p>Aqui vai o texto da matéria em HTML limpo.</p><!-- /wp:paragraph -->",
    "status": "draft", # Use 'publish' para publicar direto, 'draft' para rascunho
    "categories": [5087], # IDs numéricos das categorias
    "tags": [12, 34], # IDs numéricos das tags
    "featured_media": media_id # (Opcional) O ID obtido no Passo 1
}

res = requests.post(url_posts, auth=auth, json=payload)

if res.ok:
    print("Post publicado ou salvo como rascunho. URL:", res.json().get("link"))
else:
    print("Erro na publicação:", res.text)
```

## 4. Estrutura do Payload (Dicionário de Campos Úteis)

Ao fazer a requisição POST para `/wp/v2/posts`, as IAs podem usar os seguintes parâmetros no JSON:
* `title`: String com o título.
* `content`: String com o HTML da matéria (pode usar blocos Gutenberg ou tags HTML padrão).
* `excerpt`: String com o resumo (linha fina).
* `status`: `"publish"` (publicado), `"draft"` (rascunho), `"private"`, `"pending"`.
* `categories`: Array de inteiros com os IDs de categoria, ex: `[5087]` (Headline).
* `tags`: Array de inteiros para as tags do post.
* `featured_media`: ID numérico da imagem principal.
* `author`: ID numérico do autor (ex: `5470` para Redação).

## 5. Diretrizes Editoriais (Padrão Ouro v10)
Se a IA for responsável também pela formatação do texto:
* **Estrutura Visual:** Use código HTML semântico limpo, evitando spans inline vazios. Dê preferência a tags `<p>`, `<h2>`, `<h3>`, `<blockquote>`, e listas `<ul>`/`<li>`.
* **Cesta Premium e Retenção:** Inclua sempre as caixas de leitura complementar (interlinks `Leia mais / Leia também`) apontando para matérias correlatas e garanta a presença do formulário/caixa da newsletter no rodapé, maximizando a retenção do leitor.
