# 🎬 Memória Técnica — Vídeo Diário Multirrede

**Data:** 2026-07-23 · **Autor:** ZCode/Kimi · **Fórum pareado:** `Foruns/forum_video_diario_multirrede_20260723.md`

## 1. Arquitetura-alvo

```
Miguel grava no celular → manda o vídeo no Telegram (bot Zizilinda)
  → listener Telegram baixa o arquivo (getFile, vídeos ≤20MB via Bot API; acima disso, link/arquivo)
  → upload R2 (URL pública)
  → transcrição (Transkriptor / Whisper OpenAI)
  → legendas assadas (Creatomate template SUBTITLES, vertical, palavra a palavra)
  → LLM gera 5 textos (TikTok / Reels / Shorts / X / post Cafezinho)
  → [MODO HÍBRIDO] kit de aprovação no Telegram (mesmo bot Zizilinda) → "vai"
  → disparo paralelo:
      FB Reels (Graph API) · IG Reels (Graph API + URL R2) · TikTok (Content Posting API)
      YouTube Shorts (Data API v3, token_youtube.json) · X (media upload + tweet)
      Post Cafezinho (WP REST)
  → relatório diário no Telegram (links, falhas, retry)
```

**Decisão de entrada (23/07, Miguel):** Telegram em vez de pasta vigiada. Bot **Zizilinda** (`@Zizilindabot`) validado nesta sessão: `getMe` OK, sem webhook configurado, chat do Miguel confirmado (2 updates recebidos, resposta enviada com sucesso). Token: `TELEGRAM_TOKEN_ZIZI` (cofre local). Guardar o `chat_id` do Miguel no cofre como `TELEGRAM_CHAT_ID_MIGUEL` na Fase 0.

## 2. Componentes existentes mapeados (Tencent `/root/`)

| Arquivo | Papel | Estado |
|---|---|---|
| `pipeline_cafezinho_to_tiktok.py` | Esteira WP→LLM→ElevenLabs→Creatomate→TikTok | Funcional (abr/2026); adaptar para vídeo do Miguel |
| `agente_tiktok.py` | `publicar_no_tiktok()` — usa `TIKTOK_ACCESS_TOKEN` | Funcional, sem cron |
| `agente_youtube_v2_publicador.py` | Publicador YT (backups mostram reativação 24/06) | Sem cron aparente |
| `token_youtube.json` | OAuth com `youtube.upload` + `youtube` scopes | Revalidar refresh |
| `tiktok_oauth.py`, `gerar_token_tiktok.py`, `pegar_token_tiktok.py` | Renovação de token TikTok | Disponíveis |
| `agente_creatomate_bridge.py` | Bridge Creatomate API | Disponível |
| `agente_roteador_llm.py` | Roteador LLM (gerar_texto) | Produção |

**Permissão relevante:** ssh `tencent` entra como `ubuntu`; `/root/.env.unificado` é 600/root — Fase 0 exige sudo ou execução como root.

## 3. Variáveis necessárias por rede (nomes apenas — Artigo 1)

| Rede | Variáveis | Hoje |
|---|---|---|
| FB Reels | `FB_PAGE_ID`, `FB_PAGE_ACCESS_TOKEN` | ✅ local · ❌ Tencent |
| IG Reels | `IG_USER_ID` + token da página FB (Graph API exige vídeo em URL pública → R2) | ✅ local · ❌ Tencent |
| TikTok | `TIKTOK_ACCESS_TOKEN` | ✅ Tencent · ❌ local |
| YouTube | `token_youtube.json` (arquivo, não env) | ✅ Tencent · ❌ local |
| X | `X_API_KEY`, `X_API_KEY_SECRET`, `X_ACCESS_TOKEN`, `X_ACCESS_TOKEN_SECRET` | ✅ local · ❌ Tencent |
| Render/legenda | `CREATOMATE_API_KEY`, `CREATOMATE_TEMPLATE_ID_SUBTITLES`, `CREATOMATE_TEMPLATE_ID_VERTICAL` | ✅ local · ❌ Tencent |
| Storage | `R2_*` (5 vars) | ✅ local · ❌ Tencent |
| Transcrição | `TRANSKRIPTOR_API_KEY` ou `OPENAI_API_KEY` (Whisper) | ✅ ambos |
| WP | `WP_SITE`, `WP_USER_CAFEZINHO`, `WP_PASS_CAFEZINHO` | ✅ ambos |

**Conclusão de credenciais:** nenhuma chave nova precisa ser comprada/criada para as 5 redes + WP. O trabalho é **espelhamento e smoke test** (Fase 0), não aquisição. Kwai não tem API pública de postagem (confirmado) — fora do fluxo por decisão do Miguel.

## 4. Detalhes técnicos por publicador

- **FB Reels:** Graph API `/{page-id}/video_reels` (fases: start → upload → finish). Requer token de página com `pages_manage_posts`.
- **IG Reels:** Graph API `/{ig-user-id}/media` com `media_type=REELS` e `video_url` apontando para R2 (`R2_PUBLIC_URL`); polling de status até `FINISHED` → `/{ig-user-id}/media_publish`. Fallback existente: `INSTAGRAM_MAKE_WEBHOOK`.
- **TikTok:** reusar `agente_tiktok.publicar_no_tiktok()`; novo fluxo injeta o arquivo do Miguel em vez do render Creatomate robótico. Token de longa duração já comprovado (bypass localhost documentado em `PENDENCIAS_TIKTOK.md`).
- **YouTube Shorts:** `videos.insert` via Data API v3; vídeo vertical ≤60s + `#Shorts` no título é classificado como Short automaticamente. Reusar `agente_youtube_v2_publicador.py`.
- **X:** mídia via `upload.twitter.com/1.1/media/upload.json` (chunked, categoria `tweet_video`) → `POST /2/tweets` com `media_ids`.
- **Cafezinho:** WP REST já em produção (`CEREBRO_NODE_PUBLICACAO_WP_CAFEZINHO.md`); LLM transforma a transcrição em artigo.

## 5. Modo híbrido (decisão do Miguel)

Kit diário no Telegram (bot existente — há vários tokens no cofre): vídeo legendado + 5 textos numerados por rede. Miguel responde "vai" (ou edita um texto). Critério de graduação para 100% automático: 10–14 dias consecutivos sem falha de publicação nem texto reprovado.

## 6. Riscos e pendências

1. **Espelhamento cofre → Tencent** é pré-requisito bloqueante (Constituição §2); exige root/sudo.
2. **Token YouTube**: verificar refresh real (campo `expiry` do JSON é do access token, não do refresh).
3. **Graph API Meta**: confirmar que o app Meta tem permissões de vídeo/Reels aprovadas (não só páginas) — smoke na Fase 0 revela.
4. **Custos Creatomate**: legenda assada = 1 render/vídeo/dia (templates já existem; custo conhecido do ecossistema).
5. **Pasta de entrada**: definir se fica local (máquina do Miguel) com watcher que sobe via ssh/rsync, ou direto no Tencent. Proposta inicial: local + rsync, pois o corte de silêncio roda no PC dele.
6. **Kwai**: sem API; reavaliar só se surgir parceiro oficial de posting (Metricool etc. não cobrem Kwai hoje).

## 7. Próximo passo concreto

Fase 0 (credenciais): espelhar FB/IG/X/Creatomate/R2/Transkriptor no `/root/.env.unificado` do Tencent + smoke tests por rede. Aguardando sinal verde do Miguel para executar.

## 8. TESTE REAL executado (2026-07-23 ~04:20 BRT) — trecho Kakay

**Artefato:** `ZCodeProject/cacai_teste/trecho_kakay_final.mp4` — 28,5s, 1080x1920, 7,3MB, fundo borrado + janela do Kakay (crop `1008:562:0:78`), legendas SRT limpas (dedup de triplicatas do auto-caption YT) queimadas com libass (`FontSize=10, MarginV=55` — **MarginV >~280 sai da tela sem erro**, PlayResY=288).

**Publicações confirmadas:**
- FB Reels: 3 fases Graph v21 (`/{page}/video_reels` start → PUT `rupload.facebook.com` → finish `video_state=PUBLISHED`). post `1547427120756582`, reel `1300253491960386`, status `published`, copyright limpo.
- IG Reels: `/{ig}/media` REELS com `video_url` → poll `status_code` → `media_publish`. media `18084575039206707`.
- URL pública do vídeo: **WP media library** `controle.ocafezinho.com/wp-content/uploads/2026/07/kakay-moraes-prudente-20260723.mp4` (GET anônimo 200). **R2 r2.dev está 403 para todo o bucket** — reativar acesso público no painel Cloudflare ou aposentar r2.dev do fluxo.

**Bloqueios confirmados (aguardam Miguel):**
1. **TikTok:** `TIKTOK_ACCESS_TOKEN` root-only no Tencent. Solução: Miguel rodar `sudo bash -c 'grep TIKTOK /root/.env.unificado >> /home/ubuntu/.env.unificado'` ou colar o token no cofre local. Pipeline `agente_tiktok.publicar_no_tiktok()` revisado e pronto (FILE_UPLOAD, `SELF_ONLY` no payload de teste — mudar para público na hora real).
2. **YouTube:** refresh do `token_youtube.json` falha com `invalid_client` (client secret inválido). Solução: rodar `gerar_token_youtube.py` (Tencent `/root/`) com login Google no navegador, ou criar novo OAuth client no Google Cloud Console. Upload testado até a etapa de auth; google-api-python-client presente no Tencent.
3. **Kwai:** fora do fluxo (decisão).

**X/Twitter:** não testado nesta rodada (Miguel listou só FB/IG/YT/TikTok para o trecho).
