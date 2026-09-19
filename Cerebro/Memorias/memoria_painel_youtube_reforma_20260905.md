# Memória técnica — Reforma /v6/youtube (colunas onde/link público confirmado/máquina da transcrição)

**Ref:** ZM-20260905-010 · 05/09/2026 20:22→20:5x BRT · ZCode (GLM-5.3)
Fórum-irmão: `Foruns/forum_painel_youtube_reforma_20260905.md`

## Contexto

Miguel reclamou da página http://43.156.151.165/v6/youtube: não mostrava onde foi publicado, usava "link com controle na frente" (domínio de edição, não o público) e não dizia qual máquina transcreveu (Transkriptor x Whisper x outro).

## Log técnico completo

1. **Diagnóstico**
   - Painel: tencent `/home/ubuntu/cafezinho/v6/painel_cctv_v6.py` (7597→~7800 linhas), serviço `cctv-v6` porta 8084 (rota interna SEM /v6; pública via IP:80).
   - `pagina_youtube()` (linha 6298) usava REST `WP_API=https://controle.ocafezinho.com/wp-json/wp/v2` cat 28 e o campo `link` cru → daí o "controle." nos links.
   - Página-irmã `/v6/transkriptor` já resolvia link público via endpoint PHP tokenizado (`lumina_token`, sha256 TOK_SHA) no cafezinho-wp 190.89.239.65 com `Host: ocafezinho.com`.
2. **PHP (cafezinho-wp `/var/www/ocafezinho/transkriptor_status.php`)**
   - Backup `.bak_pre_cat28_20260905`; novo modo `?t=<tok>&cat28=1&n=18` (ADITIVO; modo `ids=` intacto e testado em regressão).
   - Query: `wp_posts` JOIN `wp_term_relationships`/`wp_term_taxonomy` (taxonomy=category, term_id=28 = "Vídeos"; prefixo real do banco é `wp_`, o `wp db prefix` mente — mostrar `ocafezinhowp_`).
   - video_id: 1) `_thumbnail_id`→`_wp_attached_file` regex `yt-([A-Za-z0-9_-]{11})\.ext` (filename vem MINÚSCULO do WP); 2) attachments filhos com yt-; 3) embed/watch/youtu.be no post_content (case correto; devolvido também como `video_embed`). Padrão genérico `{11}\.ext` REMOVIDO — casava slugs "io-comercio.jpg"/"genebra-onu.jpg" (falso positivo descoberto no 1º teste).
   - Devolve por post: post_id, status, rotulo, titulo, quando, video_id, video_embed, link público `https://ocafezinho.com/AAAA/MM/DD/slug/`.
3. **Painel (bloco novo substituiu `def pagina_youtube` inteira; 8965→18979 chars)**
   - Helpers novos: `_yt_cat28_wp()` (chama o modo cat28, SSL sem verify + Host header, fail-open []), `_yt_artifacts_idx()` (lower→real das pastas `~/ds_youtube/artifacts/`), `_yt_maquina_transcricao()` (whisper.log|segments.jsonl → Whisper; *.json3 → legenda YouTube; ledger custos → Transkriptor), `_yt_confirma_publicos()` (ThreadPool 8, UA Chrome — WAF do site dá 403 p/ UA python; cache módulo 600 s).
   - `_cat28_fallback()`: REST antigo com `re.sub(r"^https?://[^/]+", "https://ocafezinho.com", link)` se o endpoint cair.
   - Tabelas 4 colunas nas abas Publicado/Rascunho + mini-tabelas nos temáticos (slug `youtube-<vid>` também vira video_id p/ coluna máquina); chips GSN/Rio Carta/Mapa Rio por vídeo via `publicacoes_videos.json` (case-insensitive).
   - Rascunho: "não público ainda". Legenda explicando as 3 colunas no topo da aba.
4. **Provas**
   - `python3.12 -m py_compile` OK (SyntaxWarning `\w` linha 7205 é PRÉ-EXISTENTE, não mexer); restart cctv-v6 ativo.
   - curl interno 8084/youtube e público IP/v6/youtube: HTTP 200, 58170 bytes idênticos.
   - Greps: 3× "Onde foi publicado"/"Transcrição por" · 0 `controle.ocafezinho.com/20` · 24 ✅ confirmado / 0 não-confirmou · 5 Transkriptor + 2 legenda + 1 Whisper (rascunho 269036 feijão `_ZyP-i3EK0o`) · 0 traceback.
   - Screenshot chrome headless (1440×2300) → Read vira CDN → analyze_image: 4 colunas renderizam, links verdes, sem defeito de layout. (Modelo de visão leu "28/09" no rodapé — erro de leitura; HTML real diz "gerado 05/09/2026 20:38".)

## Armadilhas anotadas (novas desta sessão)

- **WP loweriza filenames de attachment** (`yt-errxzmgualu.jpg`) → comparar video_id SEMPRE em lower (índice `{n.lower(): n}` do artifacts); o embed do conteúdo preserva o case original.
- **Regex genérico de 11 chars em filename = falso positivo garantido** (slugs de imagem com 11 chars); só casar com prefixo `yt-`.
- **`wp db prefix` do wp-cli reportou `ocafezinhowp_` mas as tabelas reais são `wp_`** — acreditar no `SHOW TABLES`, não no comando.
- **Confirmar link público exige UA de navegador** (WAF/Cloudflare 403 p/ UA python), senão tudo sai "não confirmou".
- O embed do post pode ser vídeo RELACIONADO, não o de origem: prioridade da capa yt- sobre o embed é intencional.

## Estado / próximos passos

- ✅ No ar; Miguel homologa visualmente.
- Vídeos Whisper recentes (vjUTYebq-ts CNN, rpFMvQfzY1U) ainda sem matéria publicada — aparecerão com 🤖 quando a CL publicar (rascunho-only).
- Rollbacks no fórum-irmão (1 comando cada lado).
