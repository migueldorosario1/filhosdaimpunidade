# Memória — Transcrição YouTube no Moka: innertube + Data API v3 + proxy residencial (27/08/2026)

**Sessão:** ZCode/GLM-5.3 (Dell), fóruns: `forum_moka_ousadia_20260825.md` (seção 27/08) e `forum_youtube_pane_tripla_20260826` (contexto da pane).
**Missão:** destravar a transcrição de vídeos do YouTube no Moka Video (pane tripla: yt-dlp bloqueado nos 3 IPs + Transkriptor em pane + IProyal 402→recarregado mas bot-check persiste).

## Descobertas técnicas (todas provadas ao vivo)

1. **YouTube Data API v3 (chave do Miguel, `ZCODE_MOKA_YOUTUBE`):**
   - `videos.list` 200 (ficha oficial: título/canal/duração ISO8601 `PT#M#S`/descrição/thumbs maxres) — 1 unidade de quota
   - `search.list` 200 (regionCode=BR, order=date) — 100 unidades; cota 10.000/dia
   - `captions.list` 200 **com API key** (surpresa: lista faixas sem OAuth; idioma + kind vazio=manual)
   - `captions.download` **401 "API keys are not supported"** — só OAuth, e OAuth de terceiro só baixa legenda de vídeo próprio → API key NUNCA entrega texto de terceiros
   - `timedtext` nu (sem assinatura): HTTP 200 com **0 bytes** — trancado

2. **Innertube (`POST https://www.youtube.com/youtubei/v1/player?prettyPrint=false`):**
   - Body: `{"context":{"client":{"clientName":"ANDROID","clientVersion":"20.10.38","androidSdkVersion":30}},"videoId":ID,"contentCheckOk":true,"racyCheckOk":true}`
   - Responde `playabilityStatus.status:"OK"` + `videoDetails` (title/author/lengthSeconds/shortDescription/thumbnails) + `captions.playerCaptionsTracklistRenderer.captionTracks[].baseUrl` (assinada, ~323 chars)
   - `baseUrl&fmt=json3` devolve **srv3 XML** (`<p t="ms" d="ms">texto</p>`) na prática — parser próprio + decode de entities (&amp; por último)
   - Provas: Rick Astley pt-BR manual 60 blocos/1.883 chars; **g1 `5C-uvsijQXg` asr pt 127 blocos/2.230 chars** (pergunta completa ao Renan Santos)

3. **Bot-check é por CLASSE de IP:** residencial (Dell) = OK; datacenter (Tencent `43.156.151.165`) = `LOGIN_REQUIRED "Sign in to confirm you're not a bot"` MESMO via innertube. Vercel = datacenter → mesmo bloqueio.
   - **Solução:** undici `ProxyAgent` com o IProyal (`geo.iproyal.com:12321`, scheme http://). Tencent+proxy = OK com tracks. ~300KB/vídeo → 2GB ≈ 7 mil vídeos.

## Implementação (repo `moka-app`, branch `ousadia`, promovido a todos)

- `apps/web/src/app/api/ingest/route.ts`:
  - `youtubePlayerInnertube()` — player ANDROID; meta rica + tracks
  - `youtubeMetaApiKey()` — `YOUTUBE_API_KEY` opcional (aceita datacenter, sem proxy)
  - `youtubeMetaHttp()` — cascata: **API key → innertube → oEmbed → og:title** (oEmbed/og só se os 2 primeiros falharem)
  - `youtubeCaptionsHttp()` — cascata: **innertube(+proxy) → página HTML antiga**
  - `downloadCaptionTracks()` — rank pt>en>es, manual>asr; parse json3 OU srv3
  - `tubeFetch()` — undici fetch com `dispatcher: proxyAgent` quando `PROXY_RESIDENCIAL_URL` existe; cast `as unknown as Response` (tipos divergem, métodos idênticos)
  - `parseSrv3()` + `XML_ENTITIES` — XML de legenda
- `undici@8.10.0` adicionado ao `apps/web/package.json` (npm workspaces, JS puro)
- Commits: `670acdc` (innertube+cascata) → `19b11a8` (proxy residencial) → `56c85b1` (dbg temporário) → `8337140` (limpeza). Promovidos: `ousadia-mirror main`, `mirror main` (a6a36d1→8337140), `origin main` (363a6e0→8337140, fast-forward).
- Envs Vercel (3 projetos: prj_cAXX…, prj_Gt8y…, prj_fwv…): `YOUTUBE_API_KEY` + `PROXY_RESIDENCIAL_URL`, encrypted, production+preview.
  - **Pegadinha:** POST v10 com `target:["production","preview","development"]` juntos → ENV_CONFLICT; criar **1 target por chamada** funciona. E deployment criado ANTES do env não o enxerga (snapshot no build) → redeploy com `POST v12/deployments` `{"name","gitSource":{"type":"github","repoId":1347446125,"repo":"migueldorosario1/moka-ousadia","ref":"main"}}`.

## Provas finais (E2E `POST /api/ingest` com o vídeo do g1, 27/08 ~12:15)

- `moka-ousadia.vercel.app` → **200**, 19 segmentos, ficha oficial (119s, upload 2026-08-27, maxres)
- `moka-espelho.vercel.app` → **200**, 19 segs
- `mokareader.com` e `www.mokareader.com` → **200**, 19 segs (**canônico público com transcrição!**)
- Nota: mokareader.com responde 308 (redirect) — curl precisa `-L`.

## Cofres (Regra Nº 4)

- `ZCODE_MOKA_YOUTUBE`: cofre intake → 2× `.env.unificado` (backups `.bak_pre_youtube_moka_20260827`); sha8=8b37fadc nos 3
- Registrado em `CEREBRO_NODE_COFRE_CHAVES.md` (seção 27/08)

## O que falta / próximos passos

- Miguel testar a UX do Moka Video no espelho (barra %, LLM em uso, botão cancelar do `4d01f54` — nunca vistos por ele)
- Vídeos SEM legenda nenhuma continuam no caminho antigo (Whisper via worker NYC com yt-dlp bloqueado / Transkriptor desligado) — raro, mas em aberto
- Proxy IProyal: monitorar consumo (~300KB/vídeo; painel deles mostra tráfego)
- IDEA futura: `search.list` da key pode alimentar descoberta de vídeos (sabatinas do mutirão eleitoral)
