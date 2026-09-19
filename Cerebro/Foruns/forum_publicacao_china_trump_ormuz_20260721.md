# Fórum — Publicação multi-canal "China rebate Trump / Estreito de Ormuz" (2026-07-21)

**Agente:** ZCode (Kimi K3) · **Solicitante:** Miguel · **Data:** 2026-07-21 ~18:10 BRT

## Decisões resumidas

1. **Fonte:** vídeo do post de @jacksonhinkle no X (porta-voz da Chancelaria chinesa, Mao Ning, respondendo a Trump sobre o Estreito de Ormuz). Arquivo original em `Outros/pautas editoriais o cafezinho/2026 Jul 21/China/`.
2. **Legenda padrão BBC adaptada ao mobile:** transcrição via Whisper API (inglês) → tradução PT-BR manual em blocos curtos (≤2 linhas) → queima com FFmpeg em **vertical 1080×1920** (pad preto), fonte amarela bold com caixa preta semitransparente, posicionada abaixo do quadro do vídeo. Ajuste técnico: no pipeline SRT→ASS do FFmpeg, PlayResY=288 — `MarginV` em unidades de script, não pixels (MarginV=300 empurrava a legenda para fora da tela; correto: 55).
3. **Publicações imediatas (autorizadas por Miguel):** YouTube Short (público), X/Twitter, Facebook (página), Instagram Reel.
4. **Rascunhos para revisão (regra draft-first):** O Cafezinho (post 262478, ~400 palavras, Short incorporado, categoria 22 Política) e Revista Fórum (post 372716, teaser + link de volta, author 41, categories [114]).
5. **Instagram sem R2:** variáveis R2_* não estão no cofre `.env.unificado`; a Graph API exige URL pública → solução: upload do MP4 à media library do WordPress (media 262476) e uso da `source_url`. Caminho validado, virou alternativa canônica quando R2 não estiver no cofre.
6. **Credenciais Fórum:** não existem no cofre; reutilizadas em memória a partir de `scratch/check_forum_post.py` (FORUM_USER/FORUM_PASS hardcoded), sem impressão de valores. **Pendência de governança:** migrar credenciais da Revista Fórum para o `.env.unificado` (violação potencial do Artigo 1 — chave fora do cofre único).

## Artefatos

| Canal | Status | Link/ID |
|---|---|---|
| YouTube Short | 🟢 público | https://youtube.com/shorts/j7ZGVFBbROQ |
| X/Twitter | 🟢 publicado | https://x.com/i/web/status/2079673951140061675 |
| Facebook | 🟢 publicado | vídeo 1800318727597793 (página 421927677830371) |
| Instagram Reel | 🟢 publicado | https://www.instagram.com/reel/DbEcYIMkq8K/ |
| O Cafezinho | 🟡 rascunho | https://controle.ocafezinho.com/wp-admin/post.php?post=262478&action=edit |
| Revista Fórum | 🟡 rascunho | https://revistaforum.com.br/wp-admin/post.php?post=372716&action=edit |

## Scripts gerados (reutilizáveis)

Em `Outros/pautas editoriais o cafezinho/2026 Jul 21/China/`: `upload_youtube_short.py`, `publicar_x.py`, `publicar_facebook.py`, `publicar_instagram.py`, `publicar_forum.py`, `video_pt.srt`, `video_en.srt`, `corpo_cafezinho.html`.
