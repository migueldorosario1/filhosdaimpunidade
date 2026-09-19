# Cartão de Bolso — Publicação na Revista Fórum via API REST (28/06/2026)

Este cartão de bolso autocontido serve de instrução direta para qualquer agente autônomo (ou sessão de chatbot) aprender a publicar matérias e gerenciar imagens no WordPress da Revista Fórum sob o perfil de Miguel do Rosário.

---

## 1. Credenciais e Endpoints

*   **URL de Acesso WP Admin:** `https://revistaforum.com.br/forumlogin/`
*   **Login de Usuário:** `migueldorosario`
*   **Senha Web (WP Admin):** `mdforum`
*   **Senha de Aplicação (Application Password Active):** `0N2F YvTl Mbnu drgx qTdJ 9yiL`
*   **Streamyard.com:** User: `redacao@revistaforum.com.br` | Senha: `@forum21`
*   **Endpoint de Posts:** `https://revistaforum.com.br/wp-json/wp/v2/posts`
*   **Endpoint de Mídias:** `https://revistaforum.com.br/wp-json/wp/v2/media`

---

## 2. Metadados do Post (Blog O Cafezinho)

Para que a publicação seja corretamente enquadrada no blog de Miguel na Revista Fórum, os seguintes metadados de taxonomia devem ser informados:
*   **Autor (`author`):** `41` (ID correspondente ao usuário `migueldorosario`).
*   **Categorias (`categories`):** `[114]` (ID correspondente à categoria **"O Cafezinho"** na Revista Fórum).
*   **Status (`status`):** `draft` (para moderação e rascunhos) ou `publish` (para publicação imediata).

---

## 3. Gestão e Upload de Imagens (Regras Estritas)

1.  **Upload Binário Puro:** O upload de mídias para `/wp-json/wp/v2/media` exige o envio dos bytes brutos da imagem no corpo da requisição (payload binário bruto). Não use `multipart/form-data`.
2.  **Headers Exigidos:**
    *   `Content-Disposition: attachment; filename="analise_redacao.jpg"`
    *   `Content-Type: image/jpeg` (ou tipo correspondente).
3.  **Vínculo como Imagem Destacada:** Preencher a chave `featured_media` do post com a ID numérica da mídia retornada no upload.
4.  **Alinhamento no Corpo do HTML:** Inserir a tag `<img>` dentro do conteúdo HTML (`content`) envolvida em um parágrafo centralizado com as classes CSS nativas do WordPress (`aligncenter size-large` ou `size-full`) para garantir responsividade no tema da Revista Fórum:
    ```html
    <p style="text-align: center;">
      <img src="{media_url}" alt="Legenda" class="aligncenter size-large" width="600" />
    </p>
    ```

---

## 4. Diretriz Editorial de Publicação Dupla (Teaser)

As publicações na Revista Fórum devem seguir a regra do **Teaser casada com O Cafezinho**:
1. A matéria completa deve ser publicada no portal **O Cafezinho** primeiro.
2. Na Revista Fórum, publica-se apenas a **metade (teaser/truncado)** do texto.
3. No final da matéria na Revista Fórum, insere-se um link direcionando o leitor: *"Continue a ler no [portal Cafezinho](LINK)..."*.

Para especificações detalhadas do fluxo, consulte o nó correspondente do Cérebro: [CEREBRO_NODE_PUBLICACAO_DUPLA_WP.md](file:///home/migueldorosario/Downloads/Antigravity%20Google/Cerebro/CEREBRO_NODE_PUBLICACAO_DUPLA_WP.md).

---

## 5. Links de Referência no Workspace

*   **Tutorial de API Detalhado (com script Python completo):** `Projeto Cafezinho Agentes/Foruns/forum_tutorial_publicacao_api_revista_forum_20260628.md`
*   **Post de Teste Validado no wp-admin:** `https://revistaforum.com.br/wp-admin/post.php?post=363629&action=edit`

— Antigravity, 2026-06-28
