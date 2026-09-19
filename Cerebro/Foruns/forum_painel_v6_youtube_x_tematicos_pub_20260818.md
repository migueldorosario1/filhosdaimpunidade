# Fórum — Painel V6: YouTube × Temáticos — publicações separadas (ordem Miguel)

**Data:** 18/08/2026 ~21:10–21:30 BRT · **Autor:** ZCode/DeepSeek · **Sessão:** conversa "PAINEL V6: YOUTUBE × TEMÁTICOS" (ZCodeProject)

**Ordem do Miguel (voz):** as publicações dos TEMÁTICOS que apareciam na página /v6/youtube ficam melhor na página dos temáticos; a página YouTube deve mostrar os **últimos posts dos agentes YouTube** de cada site — incluindo o Cafezinho.

## O que mudou (`/home/ubuntu/cafezinho/v6/painel_cctv_v6.py` — Tencent)

1. **Central dos Temáticos (`/v6/tematicos`)** — card novo **"📰 Publicações nas últimas 24h"**: posts de hoje/ontem de cada temático via sitemap (código MOVIDO da página YouTube, idêntico; stat "posts hoje/ontem nos temáticos").
2. **Página YouTube (`/v6/youtube`)** — card **"🎬 Últimos posts dos agentes YouTube"** substituiu "🎬 Publicados nas últimas 24h":
   - ☕ **Cafezinho**: últimos 10 vídeos publicados (categoria Vídeos/28, REST autenticada; cache novo `yt_ult_caf.json` 10min).
   - 🌐 **Temáticos com agente YouTube** (GSN/Aiatolah/Mapa Rio): nova função `_posts_video_yt_tematico()` — detecta posts de vídeo pelo slug `youtube-*` no sitemap e puxa o título real da página do post (cache 30min). Aiatolah = 2 vídeos (pt/en do a9V1XgFOa5I).
   - GSN: nota — agente em modo **draft** no NYC, nenhum vídeo publicado no site ainda.
   - Mapa Rio: nota — agentes YouTube V4 **desativados desde 03/08** (ordem do Miguel), lista pronta p/ reativação.
   - Rodapé do card linka a Central dos Temáticos.

## Decisões técnicas
- "Post de agente YouTube" nos temáticos = slug `youtube-*` no sitemap (padrão do Aiatolah; GSN/Mapa Rio não publicam vídeos hoje).
- Cafezinho: de "últimas 24h" para "últimos 10 vídeos" (o pedido fala em "últimos posts"). Se preferir voltar à janela 24h, é 1 linha.

## Verificação (tudo provado)
- Teste funcional no servidor ANTES do deploy (import + asserts nas 2 funções) ✔
- `py_compile` Python 3.12 ✔ · `systemctl restart cctv-v6` ✔ (active)
- Rotas diretas 8084 e via nginx `http://43.156.151.165/v6/youtube` + `/v6/tematicos` = HTTP 200 ✔

## Backup / rollback
`painel_cctv_v6.py.bak_pre_yt_tematicos_20260818` (Tencent) — restaurar + restart reverte tudo.

**O que aconteceu:** separação aplicada e no ar. **O que falta:** validação visual do Miguel (http://43.156.151.165/v6/youtube e /v6/tematicos). **O que preciso de você (Miguel):** nada obrigatório — só conferir e dizer se quer ajustes (janela do Cafezinho, mostrar algo em GSN/Mapa Rio mesmo sem vídeo etc.).
