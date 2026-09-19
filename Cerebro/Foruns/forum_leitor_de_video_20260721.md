# 🎬 Fórum Leitor de Vídeo — 2026-07-21 — NOVO PRODUTO do Cafezinho (ideia)

> Tema: ideia do Miguel (voz→texto) para um **novo produto** do ecossistema Cafezinho — o **Leitor de Vídeo**: cola o link, o app "assiste" o vídeo, transcreve, identifica personagens e entrega resumo + Q&A.
> Nodo de índice (Camada 2): `CEREBRO_INDEX_LEITOR_VIDEO.md`.
> Governança: este é o Fórum (decisões resumidas). Memória técnica completa: `MEMORIA/memoria_leitor_de_video_20260721.md`.

## A ideia (transcrição fiel do pedido)
1. Usuário **cola o link do vídeo** no app.
2. O aplicativo **"assiste" o vídeo**: transcreve tudo e **identifica quem são os personagens** (quem fala, quem aparece).
3. Entrega um **resumo em ~2 minutos** mesmo para vídeo de **1h30–2h**.
4. Resumo em **3 tamanhos: pequeno, médio e grande**.
5. **Q&A livre**: o usuário pergunta qualquer coisa e o app **pesquisa no contexto** do vídeo (busca sobre a transcrição).

## Decisões registradas
- Status: **IDEIA APROVADA como novo produto** — segundo produto do Cafezinho, ao lado do **Moka Reader**.
- Posicionamento: produto **irmão do Moka** — mesma filosofia (IA BYOK, local-first, resumo/perguntas), aplicada a vídeo.
- Nome provisório: **Leitor de Vídeo** (working title; nome de marca a definir pelo Miguel).
- Pipeline conceitual: link → áudio/vídeo → **transcrição com timestamps** → **diarização/identificação de personagens** → resumo P/M/G → **chat com contexto** (busca na transcrição).
- Monetização/plano: a discutir (Moka já tem página /premium; possível modelo compartilhado).

## Questões abertas (para quando a sprint começar)
- Fontes de vídeo suportadas no MVP: YouTube primeiro? Links diretos (mp4)? TikTok/Instagram?
- Transcrição: Whisper (local/API) ou legendas oficiais quando existirem?
- Identificação de personagens: por voz (diarização) + nomes citados na fala; rosto fica para fase 2?
- Stack: reaproveitar base do Moka (Next.js + ai-providers) ou app separado no mesmo monorepo?
- Custo: vídeo de 2h = transcrição longa; definir limites e avisos de tokens (padrão Moka).

## Pendências
- [ ] Definir nome de marca e domínio.
- [ ] Decidir stack e casa do código (monorepo Moka ou repo novo).
- [ ] Sprint de MVP: link → transcrição → resumo P/M/G.
- [ ] Fase 2: Q&A com contexto + identificação de personagens avançada.

— Registrado por ZCode/Kimi, 2026-07-21
