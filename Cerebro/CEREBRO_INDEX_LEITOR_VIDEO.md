# 🧠 Cerebro: Índice — Leitor de Vídeo (novo produto Cafezinho)

> [!NOTE]
> **DIRETRIZ DE RESOLUÇÃO DE CAMINHOS (CÉREBRO UNIFICADO):**
> Este arquivo faz parte do **Cérebro Unificado** (Cerebro).
> - **Localização Local:** `/home/migueldorosario/Downloads/Antigravity Google/Cerebro/`
> - **Localização no Servidor (Tencent/Alibaba):** `/root/Cerebro/` (ou `../Cerebro/` relativo aos diretórios de agentes).

Índice principal do **Leitor de Vídeo** (nome provisório) — **segundo produto do ecossistema Cafezinho**, irmão do Moka Reader. Criado em 2026-07-21 a pedido do Miguel (ideia por voz→texto): cola o link do vídeo → o app "assiste", transcreve, identifica personagens, entrega resumo P/M/G em ~2 min e responde perguntas com busca no contexto.

---

## 0. Estado do produto

| Item | Valor |
|---|---|
| Status | ✅ **MVP funcional E NO AR** (2026-07-21) — https://moka-video.vercel.app |
| Nome de marca | **Moka Video** (oficializado pelo Miguel em 2026-07-21: "Tem o Moka Reader e o Moka Video") |
| Posição no ecossistema | 2º produto Cafezinho, ao lado do **Moka Reader** ([CEREBRO_INDEX_MOKA_LOG.md](./CEREBRO_INDEX_MOKA_LOG.md)) |
| Casa do código | `Outros/Aplicativos/MokaVideo/` + repo privado **`migueldorosario1/moka-video`** (fonte canônica) |
| Stack | Next.js 14 + TS; ingestão server-side (`yt-dlp` + `ffmpeg`); IA BYOK multi-provedor (OpenAI-compatible); IndexedDB local-first |
| Deploy | **Vercel: https://moka-video.vercel.app** (projeto `moka-video`) + local `localhost:3100`. ⚠️ YouTube rate-limita legendas de IPs de nuvem → ingestão completa roda local/VPS; site pode apontar p/ "Servidor de ingestão" nas ⚙️ (CORS aberto). App (Capacitor) na fase final |

## 1. A ideia (resumo)
1. Usuário **cola o link** do vídeo.
2. App **transcreve tudo** (com timestamps) e **identifica os personagens** (quem fala/aparece).
3. **Resumo em 3 tamanhos** (pequeno/médio/grande) — vídeo de 1h30–2h resumido em ~2 min.
4. **Q&A livre**: pergunte qualquer coisa, o app pesquisa no contexto do vídeo.

## 2. Pipeline conceitual
`link → ingestão (áudio+metadados) → transcrição (Whisper ou legendas oficiais) → diarização/nomeação de personagens → resumo P/M/G (map-reduce) → Q&A com busca na transcrição (RAG leve)`

Detalhamento completo: `Memorias/memoria_leitor_de_video_20260721.md`.

## 3. Registros (Camada 3)
| Data | Tipo | Arquivo |
|---|---|---|
| 2026-07-21 | Fórum (ideia/decisões) | `Foruns/forum_leitor_de_video_20260721.md` |
| 2026-07-21 | Memória técnica (pipeline, custos, reuso Moka) | `Memorias/memoria_leitor_de_video_20260721.md` |
| 2026-07-21 | Fórum (**MVP implementado** — nome, design, fontes) | `Foruns/forum_moka_video_implementacao_20260721.md` |
| 2026-07-21 | Memória técnica (arquitetura, código, testes) | `Memorias/memoria_moka_video_implementacao_20260721.md` |

## 4. O que o MVP já faz
- Cola o link (YouTube/X/Instagram) → metadados → **legendas grátis** ou **Whisper** (chave OpenAI do usuário, chunked 10 min).
- ⚡ Explicação rápida **automática** ao abrir · 📖 **resumo 1–10 min** (slider, map-reduce) · 👥 personagens · 🏛️ contexto político · 🖊️ crítica · 📜 transcrição com tempos · 📤 compartilhar.
- Mesmo design do Moka (tokens, fontes, logo, ícones); BYOK AES-GCM; videoteca IndexedDB; análises cacheadas.

## 5. Questões abertas (próxima sprint)
- "Manda para o seu…" (frase cortada): hoje = share/clipboard; confirmar destino automático (WhatsApp/e-mail?).
- ✅ RESOLVIDO (V 0.6): leitura no ar funciona via motor local — exige **permissão Local Network Access** do Chrome (cartão guia no app). VPS vira opcional (só p/ visitante sem motor).
- Domínio próprio (mokavideo.com?) na Vercel.
- YouTube rate-limita timedtext de datacenter (PO token) — yt-dlp em IP limpo é o caminho.


> 💰 **Estratégia de monetização + unificação decidida (2026-07-22):** `Foruns/forum_moka_monetizacao_unificacao_20260722.md` + `Memorias/memoria_moka_monetizacao_unificacao_20260722.md` (PIX Mercado Pago + Paddle; só BYOK grátis; federar agora/fundir na loja; ordem: i18n → confiança BYOK → página 3 níveis).

## 6. Pendências
- [x] Nome de marca: **Moka Video** ✅ (2026-07-21)
- [x] Decisão de stack e casa do código ✅ (Next.js standalone em `Outros/Aplicativos/MokaVideo/`)
- [x] Sprint MVP: link → transcrição → análises ✅ (2026-07-21)
- [ ] Q&A com contexto (RAG leve) + diarização/nomeação de vozes.
- [ ] Adapters Anthropic/Gemini; i18n (12 idiomas, padrão Moka).
- [ ] Deploy público + domínio.
- [x] **Estratégia de lançamento DEFINIDA (2026-07-22, Miguel):** lançar como site/PWA instalável agora ("pra usar, instale") ✅ V 0.5.x; app **Play Store + iPhone** numa fase seguinte (Capacitor, motor embutido).

---
— ZCode/Kimi, 2026-07-21
