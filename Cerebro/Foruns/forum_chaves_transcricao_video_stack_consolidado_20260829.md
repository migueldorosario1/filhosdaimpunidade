# Fórum — Chaves de transcrição/download de vídeo: stack consolidado no Cérebro

> **Data:** 2026-08-29, madrugada (~00:41→01:00 BRT)
> **Sessão:** ZCode/Qwen 3.8 (Dell)
> **Tema Duplo:** memória técnica `Memorias/memoria_chaves_transcricao_video_stack_20260829.md`
> **Origem:** ordem do Miguel 29/08 ~00:41 — "a gente mencionou o transkriptor e outras formas de transcrever vídeo... você deu uma lista de programas para conseguir chave... Vamos conseguir as chaves agora desses programas, porque vai ser bom ter tudo no cérebro para quando precisar baixar vídeo baixar a transcrição". A conversa de referência é a do Moka Vídeo (27-28/08): `forum_moka_ousadia_20260825.md` (adendos de 27/08) + esteira NYC (adendos 246+ do fórum v4_labs).

## A lista original (pesquisa de 27/08, adendo 2 do fórum Moka Ousadia)

Supadata · Transkriptor · TranscriptAPI · AssemblyAI · (e a YouTube Data API v3, que já tinha chave própria). Foi isso que o Miguel lembrou como "a lista de programas para conseguir chave".

## Estado do stack ao final desta sessão

| Serviço | Estado | Prova |
|---|---|---|
| **YouTube Data API v3** (`ZCODE_MOKA_YOUTUBE`) | ✅ já estava pronta desde 27/08 | intake + 2 espelhos, sha8 `8b37fadc` |
| **iProyal** (`IPROYAL_PROXY`) | ✅ pronta (recarga 27/08, US$ 11,90/2 GB) | usada ao vivo na rota de transcrição do Moka |
| **AssemblyAI** (`ASSEMBLYAI_API_KEY`, sha8 `77f59e59`) | ✅ **NOVIDADE da sessão: a MESMA chave do LLM Gateway vale pra transcrição** | sonda `GET api.assemblyai.com/v2/transcript?page_size=1` → HTTP 200 (conta tem 1 transcrição); custo zero na sonda |
| **Transkriptor** (`TRANSKRIPTOR_API_KEY`) | 🔴 morta — assinatura do Miguel encerrada | diagnóstico 27/08; variável mantida no lugar pra não quebrar a cascata reserva do NYC |
| **Supadata** (`SUPADATA_API_KEY`) | ⏳ **ÚNICA PENDÊNCIA** — conta existe, chave ainda não capturada | ver abaixo |
| **TranscriptAPI** | ❌ não contratada de propósito | free do Supadata cobre o escopo (só legendas existentes) |

## Supadata — o que aconteceu e o que falta

- Conta grátis criada pelo Miguel em **27/08 14:57** via Google OAuth (histórico do Chrome prova; org `532670f6-3d4e-4c9c-8aa6-f92afec8ca48`; ele chegou a abrir a página `api-key-test`).
- A sessão **sumiu deste PC** (varredura 29/08: zero cookies do Supadata em qualquer perfil do Chrome, zero localStorage; o cookie de sessão era descartável). Ou seja: precisa logar de novo — no Chrome dele ou no painel que deixei aberto.
- **Deixei o login pronto no painel do navegador do ZCode (aba aberta):** Supadata → "Google" → e-mail `migueldorosario@gmail.com` já preenchido e ACEITO pelo Google (conta certa, a página avançou pra senha). **Falta só o Miguel digitar a senha do Google ali.**
- Quando o login completar: a página cai no dashboard → aba API Keys (org acima) → copiar a chave → me entregar (aqui no chat, no Telegram ou colar no `~/cofre_intake/cofre_intake.env`).

### Receita pronta para quando a chave chegar (qualquer sessão executa)

1. **Teste sem gastar crédito:** `GET https://api.supadata.ai/v1/transcript` SEM url, header `x-api-key: <chave>` → **400 = chave boa; 401 = chave ruim** (sonda provada no botão "▶ Testar" do Moka, adendo 4 do fórum Moka Ousadia).
2. **Gravar (Regra 4, backup antes):** `SUPADATA_API_KEY=<valor>` em `~/cofre_intake/cofre_intake.env` + nos DOIS `.env.unificado` (`Projeto Cafezinho Agentes/root/` e `Outros/chaves/agentes_labs/`) + `/root/chaves.sh` do NYC (ssh `nyc`). Backup `.bak_pre_supadata_<data>` em cada um.
3. **Conferir espelhos por sha8** (nunca exibir valor) e registrar o sha8 aqui e no nodo do Cofre.
4. **Prova E2E barata:** transcrever 1 vídeo CURTO com legenda (1 crédito) no pipeline NYC (`youtube_transcription_fallbacks.py` já tem `_provider_supadata`, cascata `[supadata, transkriptor]` no ar desde 28/08).
5. Opcional: colar a chave também nas ⚙️ do Moka (seção 🎬, campo Supadata) pra transcrição BYOK do app.

## Decisões desta sessão

1. **AssemblyAI não precisa de chave nova** — a existente cobre transcrição (provado). Fim da pendência "AssemblyAI sem E2E" do adendo 3 do fórum Moka Ousadia (o adapter do Moka aceita a mesma chave, padrão `Authorization: <chave>`).
2. **Transkriptor fica marcado de morto** no Cérebro; a variável NÃO foi renomeada pra não quebrar a cascata NYC que ainda a lê como reserva — se o Miguel re-assinar um dia, cola a chave nova por cima (Regra 4).
3. **TranscriptAPI não entra** — redundante com o free do Supadata.
4. **Mapa do stack gravado no nodo do Cofre** (`CEREBRO_NODE_COFRE_CHAVES.md`, seção "🎬 Stack de transcrição/download de vídeo") — qualquer sessão futura acha tudo por lá.

## Como baixar vídeo/transcrição HOJE (guia rápido)

- **Legenda de YouTube (maioria dos casos):** innertube client ANDROID + proxy iProyal — implementado na rota `/api/ingest` do Moka (3 ambientes, mokareader.com incl.) e no pipeline `youtube_v2` do NYC. Sem chave nenhuma.
- **Metadados/ficha oficial:** `ZCODE_MOKA_YOUTUBE` (YouTube Data API v3), 10 mil unidades/dia grátis.
- **Vídeo SEM legenda:** Supadata (quando a chave chegar; 2 créditos/min no Whisper deles, IP deles baixam — mata o bot-check) · AssemblyAI US$ 0,37/h (download nosso, via innertube+proxy) · Whisper worker NYC.
- **Bot-check do YouTube:** residencial (iProyal/Dell) passa; datacenter (NYC/Vercel) precisa do proxy. Receita completa na memória [[youtube-transcricao-innertube-api-v3-proxy-20260827]] do ZCode e na memória técnica desta sessão.

## O que aconteceu / o que falta / o que preciso do Miguel

- **Aconteceu:** stack inteiro auditado e consolidado no Cérebro; AssemblyAI validada pra transcrição (novidade); mapa gravado no nodo do Cofre; login do Supadata deixado na tela de senha com o e-mail certo já aceito.
- **Falta:** a senha do Google no painel (30 segundos, só o Miguel pode fazer) → capturar a chave → seguir a receita acima (testar, gravar nos 4 cofres, E2E barato).
- **Preciso do Miguel:** digitar a senha na aba aberta do ZCode (ou, se preferir, logar no Chrome dele, copiar a chave em dash.supadata.ai e me passar). Nada mais — o resto da missão está pronto pra executar.
