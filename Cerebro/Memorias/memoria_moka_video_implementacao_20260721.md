# 🧠 MEMÓRIA — Moka Video: implementação do MVP (2026-07-21)

> Log técnico completo. Fórum resumido: `Foruns/forum_moka_video_implementacao_20260721.md`.
> Nodo (Camada 2): `CEREBRO_INDEX_LEITOR_VIDEO.md`. Ideia original: `MEMORIA/memoria_leitor_de_video_20260721.md`.

## 1. Pedido do Miguel (voz→texto, 2026-07-21 ~18h)

"Leitor de vídeo: joga o link, ele lê o vídeo em um minuto. Baixa o vídeo, lê, faz o contexto político, faz a crítica e aparece na tela uma explicação rápida do que foi o vídeo, os personagens, resumo — você regula: explicação maior/menor, 1 a 10 minutos. Vídeo de 3 horas, você vê 1 minuto e entende. Inicialmente um site, depois vira aplicativo. Mesmo sistema do Moka — bota **Moka Video**, mesmo nome, mesma diagramação do Moka, mesmo design, com os ícones. YouTube, e pode carregar de tweet e de Instagram também."

## 2. Decisões de arquitetura

| Decisão | Escolha | Motivo |
|---|---|---|
| Nome | **Moka Video** | oficializado pelo Miguel; família "Moka" (Reader + Video) |
| Casa do código | `Outros/Aplicativos/MokaVideo/` (standalone) | não tocar no repo de produção do Moka Reader (regra de backup/risco); reuso por cópia fiel |
| Stack | Next.js 14.2 + TS, App Router | paridade com o Moka; mesma tipografia/tokens |
| IA | BYOK multi-provedor (zai/openai/deepseek/together/kimi/qwen — adapter OpenAI-compatible) | mesmo padrão Moka; Anthropic/Gemini na fase 2 |
| Transcrição | legendas (json3 > vtt) → fallback Whisper (chunked) | custo zero quando há legenda; Whisper cobre o resto |
| Whisper | áudio → ffmpeg 16kHz mono 24kbps, segmentos de 600s (~1,8 MB) → whisper-1 verbose_json | limite da API é 25 MB; offsets de timestamp = índice × 600s |
| Persistência | IndexedDB (`moka-video/videos`) | local-first; análises cacheadas por tipo (`AnalysisKind`) |
| Chaves | cofre AES-GCM no localStorage + chave Whisper separada (`x-openai-key` no header, nunca persistida no servidor) | padrão Moka; BYOK integral |

## 3. Estrutura entregue

```
MokaVideo/
  src/app/page.tsx                home: campo de link + videoteca (cards 16:9)
  src/app/video/[id]/page.tsx     sala de leitura: ficha do vídeo, barra de ícones, painel
  src/app/api/ingest/route.ts     yt-dlp -j (meta) → legendas | Whisper (2 steps p/ progresso real)
  src/app/api/proxy/route.ts      proxy BYOK (allowlist anti-SSRF) — cópia do Moka
  src/app/api/proxy-stream/route.ts  proxy SSE — cópia do Moka
  src/components/                 CafezinhoLogo, SettingsModal (BYOK+Whisper), Markdown (leve)
  src/lib/ai/                     types/registry/transport/openaiCompatible (cópia fiel do @igot/ai-providers)
  src/lib/ai-client.ts            quickExplain, summarize (map-reduce), characters, politicalContext, critique
  src/lib/config.ts               cofre multi-entrada + whisperKey
  src/lib/crypto.ts               AES-GCM (salt próprio: moka-video-v1-salt-2026)
  src/lib/db.ts                   VideoRecord, dedupe por URL normalizada, formatTime
  public/                         cafezinho-logo.jpg, ícones, manifest.json
  README.md                       run local + notas de deploy
```

### Detalhes que importam

- **Resumo regulável:** 1 min ≈ 150 palavras (pt-BR). Transcrição > 45k chars → map (bullets por chunk de 12k) → reduce com streaming. maxTokens = min(4000, alvo×2+600).
- **Auto-explicação:** vídeo sem análises + config OK → `quick` dispara sozinho ao abrir ("aparece na tela uma explicação rápida", pedido literal do Miguel).
- **Legendas:** prioridade pt > en > es; manual > automática; json3 > vtt; merge de segmentos picados em blocos ~14s/fim de frase; dedup de rolagem das auto-captions.
- **Ingestão em 2 chamadas** (`step: "meta"` rápido, `step: "transcript"` lento) → progresso real na UI ("conectando…", "capturando legendas…", "transcrevendo o áudio…").
- **Erros amigáveis:** link inválido (400), vídeo privado/login, URL não suportada, sem legendas sem chave Whisper (428 + `needsWhisperKey`).
- **Temp:** `mkdtemp` por requisição, `rm -rf` no `finally`.

## 4. Validação (2026-07-21)

- `npx tsc --noEmit` ✅ · `npx next build` ✅ (home 13,5 kB, /video/[id] 7,2 kB).
- Servidor local `next start -p 3100` (rodando).
- YouTube meta ✅ (`dQw4w9WgXcQ`).
- Legendas ✅ — Rick Astley: 16 segmentos mesclados, 344 palavras, timestamps 18,6s→207,9s.
- Whisper end-to-end ✅ — Big Buck Bunny (`aqz-KE-bpKQ`, sem legendas): download → 2 chunks → whisper-1 → 12 segmentos, offsets corretos (último start 618,3s). Vídeo sem fala → texto alucinado/vazio é comportamento esperado do Whisper em música.
- 428 sem chave Whisper ✅ · URL inválida ✅ · `/video/[id]` 200 ✅.
- Chave OpenAI: lida do cofre canônico `Outros/chaves/agentes_labs/.env.unificado` apenas em memória no teste; valor nunca exibido.

## 5. Limites conhecidos / fase 2

- **Vercel não serve** pra `/api/ingest` (sem yt-dlp/ffmpeg; maxDuration 300 exige plano pago). Deploy canônico: VPS (Tencent/Alibaba) ou ingestão dedicada.
- Instagram/X: yt-dlp cobre links públicos; privados/login viram erro amigável.
- Whisper em vídeo só com música alucina — mitigar na fase 2 com VAD ou aviso.
- Fase 2: Q&A com contexto (RAG leve, alinha com Fase 2 do ROADMAP do Moka), diarização/nomeação de vozes, Anthropic/Gemini, i18n (12 idiomas), TTS das análises, sync Supabase, app Capacitor.
- "Manda para o seu…" (cortado): hoje é 📤 share/clipboard; confirmar com Miguel se quer WhatsApp/e-mail automático.

— ZCode/Kimi, 2026-07-21

---

## Adendo 19:00 — Deploy GitHub + Vercel + fallback serverless

- Repo: `github.com:migueldorosario1/moka-video` (privado, main). Commit inicial "Moka Video MVP" + gitignore .vercel.
- Vercel: projeto `moka-video` → https://moka-video.vercel.app (deploy 35s, alias ok).
- **Fallback serverless na `/api/ingest`:** detecção de yt-dlp (`--version`, cacheada; `MOKA_DISABLE_YTDLP=1` força p/ teste). Sem yt-dlp → `youtubeId()` + `youtubeMetaHttp()` (oEmbed) + `youtubeCaptionsHttp()` (watch page → `"captionTracks"` regex → timedtext `&fmt=json3`, rank pt>en>es, manual>asr).
- **Achado de campo (importante p/ futuras sprints):** timedtext exige PO token / não-rate-limit; de IP residencial funciona intermitente (429 após rajada de testes), de IP Vercel falha sempre. InnerTube (WEB/ANDROID/IOS/TVHTML5) retornou 0 tracks nos testes. **Conclusão: scraping de legendas não é confiável em serverless — ingestão confiável exige yt-dlp em VPS.**
- **CORS aberto** (`Access-Control-Allow-Origin: *`, headers `Content-Type, x-openai-key`) + `ingestApiBase()` no cliente (`mokavideo.ingestServer` no localStorage; campo nas ⚙️). Site no ar ← aponta → servidor com yt-dlp = arquitetura final híbrida.
- Rate-limit transitório confirmado no reteste local (429 no timedtext; yt-dlp -j segue ok). O app cai graceful pro caminho Whisper (428 + mensagem).
