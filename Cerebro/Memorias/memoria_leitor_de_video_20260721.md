# 🧠 MEMÓRIA — Leitor de Vídeo: novo produto Cafezinho (2026-07-21)

> Log técnico completo da ideia do Miguel. Fórum resumido: `Foruns/forum_leitor_de_video_20260721.md`.
> Nodo (Camada 2): `CEREBRO_INDEX_LEITOR_VIDEO.md`.

## 1. Origem
Pedido do Miguel por voz→texto em 2026-07-21, sessão ZCode/Kimi. Transcrição bruta (trechos):
- "um leitor de vídeo. Você coloca o link do vídeo lá, ele assiste o vídeo"
- "ele identifica quem são os personagens e ele transcreve tudo"
- "te entrega um resumo em dois minutos — um vídeo de uma hora e meia, duas horas"
- "um resumo pequeno, médio, grande"
- "você pode perguntar qualquer coisa, ele pesquisa o contexto"
- "vão ser dois produtos do Cafezinho: o Moka Reader e o leitor de vídeo"

## 2. Visão do produto
**Leitor de Vídeo** (nome provisório): app web (irmão do Moka Reader) que transforma vídeo longo em conhecimento navegável:

| Etapa | Entrada | Saída |
|---|---|---|
| 1. Ingestão | link do vídeo (YouTube etc.) | arquivo/áudio + metadados |
| 2. Transcrição | áudio | texto completo **com timestamps** |
| 3. Personagens | transcrição (+ áudio) | lista de quem fala/aparece, com trechos-âncora |
| 4. Resumo | transcrição | resumo em **3 tamanhos (P/M/G)** |
| 5. Q&A | pergunta do usuário | resposta com **busca no contexto** (trechos do vídeo) |

Meta de UX do Miguel: vídeo de 1h30–2h → resumo disponível em **~2 minutos**.

## 3. Pipeline técnico conceitual

### 3.1 Ingestão
- MVP: **YouTube** (maior fonte de links). Extrair áudio (`yt-dlp` server-side ou equivalente) + metadados (título, canal, duração, thumbnail).
- **Atalho de custo**: se o vídeo tiver **legendas oficiais/auto-geradas**, usar como transcrição base (grátis e instantâneo) — Whisper só quando não houver legenda.
- Links diretos (mp4) e outras plataformas: fase 2.

### 3.2 Transcrição
- Whisper (API ou self-hosted) com timestamps por segmento.
- Vídeo de 2h → transcrição ~15–20k palavras → ~25–30k tokens. Viável em janelas de contexto modernas, mas Q&A deve usar busca, não dump integral (ver 3.5).

### 3.3 Identificação de personagens
- **Diarização** (quem fala quando) sobre o áudio — speakers `SPEAKER_1..N`.
- **Nomeação**: cruzar com nomes citados na própria fala (NER + auto-referência) e metadados do vídeo; usuário pode renomear speakers.
- Rosto/reconhecimento visual: fase 2 (se necessário).

### 3.4 Resumo P/M/G
- Três níveis de síntese sobre a transcrição (chunked, map-reduce para vídeos longos):
  - **Pequeno**: ~5–8 linhas (o essencial).
  - **Médio**: ~1 página (tópicos principais).
  - **Grande**: resumo estruturado por seções/capítulos, com timestamps clicáveis.
- Reuso direto do padrão `summarizeStream` do Moka (ai-client multi-provider BYOK).

### 3.5 Q&A com contexto
- Busca sobre a transcrição (RAG leve: chunks + embeddings, ou BM25 simples no MVP) → trechos relevantes + pergunta → resposta com citação de timestamp.
- É o equivalente ao AskModal do Moka ("pergunte qualquer coisa"), com o corpus = transcrição do vídeo.
- Alinha com a **Fase 2 (RAG) do ROADMAP do Moka** — mesma tecnologia, corpus diferente.

## 4. Relação com o Moka Reader
- Filosofia compartilhada: **BYOK** (chave da IA no dispositivo), local-first, resumo/perguntas, i18n.
- Reuso possível: `packages/ai-providers`, `ai-client`, padrões de UI (modais, barra de progresso, aviso de tokens), Supabase sync.
- Decisão pendente: **app novo no mesmo monorepo** (`apps/video/`) vs repo separado. Inclinação técnica: mesmo monorepo npm workspaces, reaproveitando packages.

## 5. Custos e limites (a definir na sprint)
- Transcrição de 2h: custo de Whisper por minuto de áudio — precificar.
- Resumo + Q&A: tokens do provider do usuário (BYOK), com aviso explícito (padrão Moka).
- Rate limits: fila de processamento; barra de progresso por etapa (padrão `.tts-prep-bar`).

## 6. Estado
- **2026-07-21:** ideia registrada (fórum + memória + nodo criado `CEREBRO_INDEX_LEITOR_VIDEO.md`). Nenhuma linha de código. Próximos passos: nome/domínio, decisão de stack, sprint de MVP (link → transcrição → resumo P/M/G).

— ZCode/Kimi, 2026-07-21
