# 🎬 Fórum — Vídeo Diário Multirrede ("grava uma vez, publica em tudo")

**Data:** 2026-07-23 · **Autor:** ZCode/Kimi a pedido do Miguel · **Memória técnica pareada:** `MEMORIA/memoria_video_diario_multirrede_20260723.md`

## O pedido do Miguel (voz → texto)

Miguel grava **um vídeo por dia** e já assinou um serviço de corte de silêncio. Quer: legendar o vídeo, gerar os textos e **publicar todo dia em todas as redes** (Facebook Reels, Instagram, TikTok, X, YouTube Shorts) + um post diário no Cafezinho. Pediu plano de trabalho e reunião das credenciais.

## Decisões tomadas nesta sessão

| Pergunta | Decisão |
|---|---|
| Nível de automação | **Híbrido** — começa com aprovação no Telegram (vídeo legendado + 5 textos; Miguel responde "vai"); após 1–2 semanas estável, migra para 100% automático |
| Instagram | **Reels** (não feed) — mesmo vídeo vertical do TikTok/Shorts, maior distribuição orgânica |
| Kwai (rede chinesa lembrada pelo Miguel) | **Fora do fluxo por ora** — Kwai não tem API pública de postagem; alternativas eram kit manual no Telegram ou robô clicador arriscado |

## Inventário de credenciais (verificado nesta sessão)

**Já existem (sem valores aqui — Artigo 1):**

| Rede/Serviço | Variáveis/Arquivo | Local |
|---|---|---|
| Facebook Página | `FB_PAGE_ID`, `FB_PAGE_ACCESS_TOKEN` | Cofre local `.env.unificado` |
| Instagram Business | `IG_USER_ID`, `INSTAGRAM_MAKE_WEBHOOK` | Cofre local |
| X/Twitter | `X_API_KEY`, `X_API_KEY_SECRET`, `X_ACCESS_TOKEN`, `X_ACCESS_TOKEN_SECRET`, `X_BEARER_TOKEN` | Cofre local |
| TikTok | `TIKTOK_ACCESS_TOKEN` (longa duração, bypass localhost) | `/root/.env.unificado` (Tencent) |
| YouTube | `token_youtube.json` (OAuth, escopo `youtube.upload`) | `/root/` (Tencent) |
| Creatomate | `CREATOMATE_API_KEY` + templates FB/IG/TikTok/YouTube/vertical/**subtitles** | Cofre local |
| Transcrição/voz | `TRANSKRIPTOR_API_KEY`, `ELEVENLABS_*`, OpenAI Whisper | Cofre local |
| Hospedagem pública de vídeo | R2 (`R2_PUBLIC_URL`) — criada exatamente para alimentar Graph API de Reels | Cofre local |
| WP Cafezinho | `WP_SITE`, `WP_USER_CAFEZINHO`, `WP_PASS_CAFEZINHO` | Cofre local + Tencent |

**Lacunas encontradas:**
1. Chaves FB/IG/X só existem no cofre **local** — falta espelhar no Tencent (Constituição §2).
2. Agentes `agente_tiktok`, `agente_youtube_v2_publicador`, `agente_twitter_video` existem no Tencent mas **sem cron**.
3. Token YouTube: última reativação registrada em 24/06 — revalidar refresh.
4. Kwai: zero credenciais (decidido: fora por ora).

## Plano aprovado (resumo das fases)

- **Fase 0 — Credenciais:** espelhar FB/IG/X → Tencent; smoke test de cada rede (fingerprint + HTTP 200, sem expor valores); revalidar token YouTube.
- **Fase 1 — Ingesta:** pasta vigiada → upload R2 (URL pública) → transcrição → **legendas assadas** via template Creatomate `SUBTITLES` → LLM gera 5 textos (TikTok, Reels, Shorts, X, post Cafezinho).
- **Fase 2 — Publicadores:** FB Reels (Graph API), IG Reels (Graph API + URL R2), TikTok (adaptar `pipeline_cafezinho_to_tiktok.py` para vídeo do Miguel), YouTube Shorts (reusar `agente_youtube_v2_publicador.py`), X (media upload).
- **Fase 3 — Orquestração:** cron diário no Tencent + bot Telegram de aprovação (modo híbrido) + relatório diário com links e retry de falhas.
- **Fase 4 — Pós-estabilização:** migração para 100% automático; reavaliar Kwai.

## Observações

- O pipeline TikTok existente gera vídeo **robótico** (WP → LLM → ElevenLabs → Creatomate). As 4 pendências estéticas de `PENDENCIAS_TIKTOK.md` (voz robótica, BGM, legendas, roteiro) **perdem relevância** no novo fluxo, pois o vídeo é do próprio Miguel.
- O motor de base (R2 + Creatomate + Graph API + TikTok API) está comprovadamente funcional — sessão de abril subiu vídeo de ponta a ponta.

## Adendo 2026-07-23 (mesma sessão) — Canal de entrada definido: Telegram

- Miguel decidiu que **não** usará pasta vigiada: ele grava no celular e **manda o vídeo pelo Telegram**.
- Bot escolhido: **Zizilinda** (`@Zizilindabot`). Controle confirmado nesta sessão via `TELEGRAM_TOKEN_ZIZI` (cofre local): `getMe` OK, sem webhook, mensagens de teste do Miguel recebidas e resposta "oi" enviada com sucesso.
- O bot passa a ter **dupla função**: (1) inbox de entrada do vídeo diário; (2) canal do kit de aprovação do modo híbrido.

## Adendo 2 — 2026-07-23 ~04:20 BRT — PRIMEIRO TESTE REAL DE PUBLICAÇÃO (trecho Kakay)

A pedido do Miguel, teste de ponta a ponta com a entrevista do **Kakay** ao Jornal da Fórum (vídeo `Od9sKT0q_Qk`, TV Fórum, 32min). Trecho 22:29–22:57 ("Moraes foi prudente ao punir a desobediência"), vertical 1080x1920 (fundo borrado), legendas amarelas assadas.

**Resultado por rede:**

| Rede | Resultado |
|---|---|
| **Facebook Reels** | ✅ **PUBLICADO** — `/reel/1300253491960386/`, copyright check limpo |
| **Instagram Reels** | ✅ **PUBLICADO** — media `18084575039206707` (vídeo servido pela biblioteca de mídia do WP Cafezinho) |
| **YouTube Shorts** | ❌ **BLOQUEADO** — `token_youtube.json` com `invalid_client` (client secret revogado/desatualizado). Precisa re-autorização OAuth (rodar `gerar_token_youtube.py` com login no navegador) |
| **TikTok** | ❌ **BLOQUEADO** — `TIKTOK_ACCESS_TOKEN` só existe em `/root/.env.unificado` (600/root) e o acesso SSH é `ubuntu` sem sudo. Precisa que o Miguel copie o token para `/home/ubuntu/.env.unificado` ou para o cofre local |

**Aprendizados operacionais (importantes para a Fase 1):**
1. **R2 público está QUEBRADO** — `pub-*.r2.dev` devolve 403 até em objetos antigos (acesso público desativado no painel Cloudflare). Biblioteca de mídia do WP Cafezinho provou ser **substituta perfeita** (upload REST → URL pública 200 aceita pela Graph API).
2. **FB Reels não precisa de URL pública** — upload binário direto em 3 fases (start → PUT rupload → finish). Funcionou de primeira.
3. Legendas: libass do ffmpeg usa PlayResY=288 — `MarginV` acima de ~280 joga o texto para fora da tela (bug mudo, sem erro). Usar MarginV ≤ 100.
4. O mesmo trecho serve para todas as redes: 1080x1920, <60s, ~7MB.

**Decisão de canal de vídeo grande (Miguel):** vídeo >20MB → Miguel sobe no Google Drive e manda o link na Zizilinda; vídeo pequeno → direto no Telegram.

## Adendo 3 — 2026-07-23 ~17:20 BRT — CICLO FECHADO: 4 REDES + R2

Mesmo trecho do Kakay, após destravos com o Miguel:

| Rede | Resultado final |
|---|---|
| **YouTube Shorts** | ✅ **PUBLICADO** — https://youtube.com/shorts/b0ROQUy_Wvw |
| **TikTok** | ✅ **Vídeo enviado aos rascunhos do app** (endpoint `inbox/video/init`, upload 201, publish_id `v_inbox_file~v2.7665695888135948289`) — Miguel finaliza com 1 toque no app |
| **R2** | ✅ **CONSERTADO pelo Miguel** (reativou o acesso público no painel; URLs `pub-*.r2.dev` respondendo 200 — invalida a nota de "R2 quebrado" do adendo 2) |

**Como cada bloqueio caiu:**
1. **SSH root no Tencent** funciona com a mesma chave (`ssh -p 38422 root@43.156.151.165`) — antes eu só usava o alias `ubuntu`. Isso destravou tudo.
2. **TikTok:** o `TIKTOK_ACCESS_TOKEN` original havia se PERDIDO na unificação do cofre (12/06) — não existia em nenhum env. Refeito o fluxo OAuth com PKCE (Miguel autorizou no navegador, colou a URL de callback). Access token 24h + **refresh token de 1 ano** salvos em `/root/.env.unificado`. Publicação DIRETA ainda bloqueada: app dev não auditado (`unaudited_client_can_only_post_to_private_accounts`) — mas o endpoint **inbox (rascunhos) funciona sem auditoria**. Fluxo adotado: automático até os rascunhos + 1 toque do Miguel. Para 100%: submeter o app à revisão do TikTok (fórum `forum_adesao_tiktok.md`, "Rota de Sangue Azul").
3. **YouTube:** `invalid_client` era porque `token_youtube.json` pertencia a um OAuth client ANTIGO (deletado); o `agent_data/client_secrets.json` (abr/2026) é de um client NOVO. Fluxo refeito localmente (servidor localhost:8090), token novo instalado em `/root/token_youtube.json` (backup `.bak_pre_renovacao_20260723`). Upload do Short funcionou de primeira.
4. **Dívida de segurança registrada:** `TIKTOK_CLIENT_KEY/SECRET` estavam hardcoded em `pegar_token_tiktok.py` e `update_env_tiktok.py` (violação do Artigo 1) e transitaram em chat — rotacionar o client secret no TikTok for Developers e manter só no cofre.
