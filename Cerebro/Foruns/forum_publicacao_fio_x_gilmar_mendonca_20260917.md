# Fórum — Fio no X (Twitter) da matéria Gilmar Mendes x André Mendonça (17/09/2026)

- **Quem:** ZCode/GLM-5.3 (pedido direto do Miguel nesta quinta, 17/09/2026 ~10:4x)
- **O quê:** primeiro fio de 2 tweets publicado manualmente no X da conta @ocafezinho (87.842 seguidores) divulgando a matéria que o Miguel publicou hoje no Cafezinho.
- **Matéria:** https://www.ocafezinho.com/2026/09/17/gilmar-mendes-vai-para-cima-de-andre-mendonca-pixuleco-eleitoral/

## O que aconteceu (estado: CONCLUÍDO)

- Fio no ar e confirmado publicamente via oembed:
  - Tweet 1 (texto maior + capa da matéria): https://x.com/ocafezinho/status/2100583215094239416
  - Tweet 2 (reply com o link da matéria; o card do X puxa a imagem/capa sozinho): https://x.com/ocafezinho/status/2100583226011984141
- Formato pedido pelo Miguel e cumprido:
  - Tweet 1: emoji ⚖️ (justiça) no começo + título em caixa alta + abertura/substância da matéria (~1,2 mil caracteres, Long Post Premium) + imagem (capa oficial da matéria, gilmar-mendes-stf-15-09-2026.jpg).
  - Tweet 2: reply no tweet 1 com chamada "Leia a análise completa no Cafezinho" + link da matéria (o preview card exibe a capa automaticamente — não precisa subir imagem no tweet 2).
- Contexto: o pedido original era um fio da matéria do Xi Jinping (bandeira 🇨🇳 + link), mas o Miguel mudou de ideia porque a matéria do Xi ainda não foi publicada; ficou para depois. O molde do Xi (post_x_xi_jinping.py + fio_twitter_xi_jinping.txt, ambos de 18/07 no scratch/) foi reutilizado como base.

## Como foi feito (para replicar)

1. Credenciais: cofre unificado `Outros/chaves/agentes_labs/.env.unificado` → chaves `X_API_KEY`, `X_API_KEY_SECRET`, `X_ACCESS_TOKEN`, `X_ACCESS_TOKEN_SECRET` (conta @ocafezinho, OAuth 1.0a, tweepy 4.16.0). Nenhum valor de segredo sai do cofre.
2. Script versionado: `scratch/post_x_gilmar_mendonca.py` (mesma família dos publish_twitter_*.py e post_x_xi_jinping.py).
3. Imagem do tweet 1 = capa og:image da própria matéria (baixada de wp-content/uploads).
4. Confirmação pública: `curl -sL "https://publish.twitter.com/oembed?url=<url do tweet>"` (segurar o redirect com -L).

## Limitações e notas

- O access token não tem escopo de leitura de timeline (`get_users_tweets` retorna 401) — leitura de tweets próprios/da home não funciona com esse token; só escrita (create_tweet) e get_me. Não bloqueia publicações.
- O tweet 1 usa Long Post (acima de 280 caracteres), que exige Premium na conta — mesma praxe do fio do Xi Jinping de 18/07.

## O que falta / próximos passos

- Nada pendente para este fio. Se o Miguel pedir, o mesmo formato serve para a matéria do Xi Jinping quando ela for publicada (molde já pronto no scratch/).
- Métricas de engajamento do fio podem ser acompanhadas manualmente no X (a API de leitura está sem escopo no token atual).

## Adendo — Facebook (17/09 ~11:2x, mesmo turno)

- Post do Gilmar publicado na página O Cafezinho do FB (453.685 curtidores): texto igual ao tweet 1 + capa via /photos. URL: https://www.facebook.com/421927677830371/posts/1601804191985541
- 🔴 Link no 1º comentário BLOQUEADO: POST /{post_id}/comments retorna 403 "(#200) insufficient permissions" — o FB_PAGE_ACCESS_TOKEN vivo (cofre Dell, hash md5 84b9b3dda3) NÃO tem a permissão pages_manage_engagement (tem só a de publicar). Solução = Miguel regenerar o token no Graph API Explorer com 4 escopos (pages_show_list, pages_manage_posts, pages_read_engagement, pages_manage_engagement) — guia entregue a ele.
- Fallback aplicado no post do Gilmar: legenda editada (POST /{post_id} message=, 200 OK) com o link no fim do texto.
- Token FB do espelho tencent (/home/ubuntu/root_copy/.env.unificado, hash 71c83e1ed0) está MORTO (erro 190/460 — senha mudada): a substituir pelo novo quando o Miguel gerar (REGRA Nº 4).
- Pendência desteira 10 fios/dia (pedido do Miguel): X ok (só-escrita já basta); FB aguarda o token novo p/ 1º comentário. Esteira roda no tencent (fuso BRT, tweepy 4.16 presente).
