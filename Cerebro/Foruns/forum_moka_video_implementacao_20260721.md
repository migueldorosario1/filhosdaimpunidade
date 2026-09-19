# 🎬 Fórum — Moka Video: MVP implementado (2026-07-21)

> Tema: Leitor de Vídeo → **Moka Video** (nome oficializado pelo Miguel).
> Nodo (Camada 2): `CEREBRO_INDEX_LEITOR_VIDEO.md`.
> Memória técnica: `MEMORIA/memoria_moka_video_implementacao_20260721.md`.
> Fórum da ideia (mesmo dia, mais cedo): `Foruns/forum_leitor_de_video_20260721.md`.

## Decisões do Miguel (voz→texto, sessão ZCode/Kimi)

- **Nome:** "Moka Video" — mesma marca do Moka Reader ("Tem o Moka Reader e o Moka Video").
- **Design:** mesma diagramação do Moka, mesmo design, com os ícones.
- **Fontes:** YouTube, X/Twitter e Instagram.
- **Fluxo:** cola o link → o app baixa, lê, faz o **contexto político**, faz a **crítica**, e **aparece na tela uma explicação rápida** do que foi o vídeo, com **personagens** e **resumo regulável** ("vídeo de 3 horas, você vê um minuto e entende").
- **Estratégia:** primeiro um **site**; depois vira **aplicativo** (mesmo caminho do Moka).

## O que foi entregue (MVP funcional, mesmo dia)

- **Local do código:** `Outros/Aplicativos/MokaVideo/` (repo standalone, irmão da pasta `Moka/`). Decisão: fora do monorepo do Moka por ora — não arrisca a produção do Reader; reuso feito por cópia fiel dos pacotes (ai-providers simplificado, crypto, proxies).
- **Stack:** Next.js 14 + TS, App Router. Server-side só pra ingestão (yt-dlp + ffmpeg) e proxies BYOK.
- **Design:** tokens CSS idênticos ao Moka (porcelana/cobre/madeira, Fraunces/Literata/Figtree, CafezinhoLogo, ghost buttons, modais, sliders).
- **Pipeline:** meta (yt-dlp -j) → legendas oficiais/auto (json3/vtt, grátis) → fallback Whisper (download de áudio → ffmpeg 16k mono 24kbps em pedaços de 10 min → whisper-1, offsets de timestamp corrigidos).
- **Análises (BYOK, streaming, pt-BR):** ⚡ explicação rápida (auto ao abrir), 📖 resumo 1–10 min (slider, ~150 palavras/min, map-reduce p/ transcrições > 45k chars), 👥 personagens, 🏛️ contexto político, 🖊️ crítica, 📜 transcrição com tempos, 📤 compartilhar (Web Share/clipboard).
- **Local-first:** videoteca em IndexedDB; análises cacheadas (não gasta token de novo); cofre de chaves AES-GCM (padrão Moka) + chave Whisper opcional.

## Testes executados

- `tsc --noEmit` ✅, `next build` ✅ (5 rotas).
- Ingestão YouTube real: metadados ✅; legendas (Rick Astley, 16 segmentos mesclados, pt) ✅; Whisper end-to-end (Big Buck Bunny, 2 chunks, offsets corretos — vídeo sem fala, texto veio vazio/alucinado, comportamento esperado) ✅; erro 428 sem chave Whisper ✅; link inválido ✅.
- Chave OpenAI do cofre (`Outros/chaves/agentes_labs/.env.unificado`) usada só no teste, sem exposição de valor.

## Pendências / decisões abertas

- "Manda para o seu…" (frase cortada do Miguel): implementado como 📤 compartilhar/copiar. Se era WhatsApp/e-mail automático, fase 2.
- Deploy público: `/api/ingest` não roda em Vercel serverless (precisa yt-dlp/ffmpeg) → VPS (Tencent/Alibaba) ou servidor de ingestão dedicado.
- Instagram/X podem exigir login em alguns links — yt-dlp cobre conteúdo público; erros viram mensagens amigáveis.
- Fase 2: Q&A com contexto (RAG leve), diarização de vozes, adapters Anthropic/Gemini, i18n 12 idiomas, app Capacitor.

— ZCode/Kimi, 2026-07-21

---

## Adendo 19:00 — NO AR: GitHub + Vercel (a pedido do Miguel)

- **GitHub:** repo privado `migueldorosario1/moka-video` (branch main, protocolo SSH) — fonte canônica do código, como no Moka.
- **Vercel:** projeto `moka-video` (time `miguel-do-rosario-s-projects`, orgId `team_QQzbgQTC569AoQxaur7tNLGj`). Deploy produção ✅ → **https://moka-video.vercel.app** (home 200 ✅, alias configurado).
- **Fallback serverless implementado:** na Vercel (sem yt-dlp) a rota `/api/ingest` usa caminho 100% HTTP — oEmbed p/ metadados + captionTracks p/ legendas. Metadados funcionam ✅ na Vercel.
- **Limitação descoberta e confirmada:** o YouTube **bloqueia/rate-limita** os endpoints de legenda (timedtext) vindos de IPs de datacenter (testado: 429 da Vercel; InnerTube WEB/ANDROID/IOS/TV sem tracks; PO token exigido). Ou seja: **no ar, a transcrição automática é instável**; o app mostra mensagem amigável explicando.
- **Solução arquitetural entregue:** `OPTIONS`+CORS aberto na `/api/ingest` + campo **"Servidor de ingestão"** nas ⚙️ — o site no ar pode apontar pra qualquer servidor com yt-dlp (VPS/local) e ter 100% das funções. Config fica no navegador (localStorage).
- **Uso completo hoje:** servidor local `localhost:3100` (yt-dlp + Whisper ✅). Próximo passo natural: subir a ingestão no Tencent/Alibaba com domínio HTTPS e apontar o site pra ele.

---

## Adendo 19:50 — V 0.2: sprint de UX das Configurações (feedback do Miguel)

Feedback por voz do Miguel usando o app: "estava configurando, cliquei fora sem querer, sumiu e não voltou… o salvar tem que ficar junto da chave… tem que ter testar conexão pra OpenAI… tem que ter o procurar modelo… servidor tem que ser mais simples de explicar… letras maiores… tem que explicar que é pra clicar no botão de configuração… colocar quem somos e um help".

Entregue (commit V 0.2, deploy em https://video.mokareader.com ✅):
- **Modal anti-fechamento-acidental:** backdrop e ESC não fecham mais; só ✕ ou "✓ Concluir". Rascunho (chave, modelo, whisper, servidor) fica guardado em memória e restaurado ao reabrir.
- **Botões junto dos campos:** 💾 Salvar + 🔌 Testar conexão embaixo de CADA campo (LLM, Whisper, servidor). Teste de conexão novo pra chave OpenAI/Whisper (GET /v1/models via proxy).
- **🔍 Procurar modelos:** GET {baseUrl}/models via proxy → chips clicáveis que preenchem o campo modelo.
- **Letras maiores** (campos 16,5px, textos 14–15,5px) e explicação do "Servidor de vídeo" em linguagem simples ("não mexa se ninguém te passou um endereço").
- **Onboarding:** home ganhou callout destacado "👋 Primeiro passo: clique na ⚙️" quando não há chave.
- **Páginas novas:** `/sobre` (Quem somos — Cafezinho, família Moka, princípios BYOK/local-first) e `/ajuda` (passo a passo + FAQ), linkadas no rodapé.
- Build ✅, rotas /sobre e /ajuda 200 em produção ✅. Local 3100 reiniciado com o build novo.

---

## Adendo 2026-07-22 — V 0.3: indicadores de chave salva em verde claro (feedback do Miguel)

Feedback por voz do Miguel: a parte que mostra a chave salva mascarada "está chamando pouca atenção" — pediu fundo "verdinho claro" nela, "mesma coisa do OpenAI" (campo Whisper).

Entregue (commit `a2f99b6`, deploy https://video.mokareader.com ✅, home 200):
- **Lista de chaves salvas** (`.entry`): fundo verde claro (#eaf7ea) + borda verde; chave em uso com verde mais forte (#dcf1dc/#4c9a52). Título novo: "✅ Chaves salvas neste navegador".
- **Chip novo no campo Whisper** (`.saved-chip`): quando há chave OpenAI salva, aparece "✅ Chave OpenAI salva: sk-…xxxx" em caixa verde — antes era só placeholder discreto no input.
- Build `tsc` ✓ + `next build` ✓ (6 rotas). Sem segredos expostos.

---

## Adendo 2026-07-22 — V 0.3: Entrar com Google + V 0.2.1 (fix FOUC)

- **V 0.3:** Login Google (Supabase, mesmo projeto do Moka Reader — conta única da família Moka). AuthButton na topbar das duas páginas. Allowlist do Supabase aceita video.mokareader.com (testado, 302 → Google). Sync da videoteca pra nuvem fica pra próxima sprint.
- **V 0.2.1:** FOUC ("meio segundo de site quebrado") corrigido — CSS dos componentes saiu do styled-jsx pro globals.css (render-blocking) + CSS crítico inline no layout.
