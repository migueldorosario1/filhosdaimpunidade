# Fórum — Moka Video: transcrição em escala via Transkriptor (plano V2)

> Data: 2026-08-01 · Autor: ZCode · Status: **✅ FASE 1 EXECUTADA E EM PRODUÇÃO** (mesmo dia, à noite)

## Contexto

Miguel tentou ler `youtube.com/watch?v=NDjn1j0d0vs` (As Cunhãs — entrevista Alexandre Padilha) no app instalado e recebeu a mensagem técnica do caminho serverless. Na conversa ele decretou:

1. **Nada de localhost** no produto (motor local localhost:3100 banido do app público).
2. O app **tem que transcrever qualquer vídeo em qualquer língua** — é produto de assinatura.
3. Desconfiou que proxy residencial não escala ("para milhares de pessoas não vai dar certo") e perguntou por duas saídas: **IP do próprio usuário (com autorização)** e **a API do Transkriptor, que já temos**.

## Investigação (testes, não opinião)

### IP do usuário — IMPOSSÍVEL em web app (testado)

| Endpoint YouTube | CORS p/ browser? | Resultado |
|---|---|---|
| `api/timedtext` (dados de legenda) | ✅ `access-control-allow-origin` confirmado | browser pode baixar legenda |
| `/watch` (entrega as URLs assinadas das legendas) | ❌ sem header CORS | browser bloqueado — e **não existe permissão concedível** |
| `youtubei/v1/player` (entrega URLs de áudio) | ❌ HTTP 403 + sem CORS | browser bloqueado |

Conclusão: consentimento não destrava — o navegador não tem mecanismo. Únicas vias com consentimento = software instalado (banido) ou extensão (contra "não passa por loja", sem mobile).

### Transkriptor — VALIDADO AO VIVO ✅

- Chave: `TRANSKRIPTOR_API_KEY` em `Outros/chaves/agentes_labs/.env.unificado` (linha 45) — existe.
- Código de produção: `Projeto Cafezinho Agentes/agents_labs/youtube_v2/util_youtube_transcript.py` (usado diariamente pelos agentes; diarização obrigatória, cost guard, gate qualidade <100 chars/min, cache 14d).
- **Teste com o vídeo exato que falhou pro Miguel:** submit HTTP 202 → Completed em **140s** → **491 segmentos, 45.813 chars, 4 speakers** (SPK_1–4: as 3 apresentadoras + convidado). Preview limpo, pt-BR correto. Custo do teste ≈ US$ 0,006/min.
- Bônus dos testes: o vídeo do Miguel **tinha** legenda ASR no YouTube — o que falhou foi o YouTube bloqueando o IP de datacenter do Vercel, não a ausência de legenda.

## ✅ O QUE FOI CONSTRUÍDO (Fase 1 — commit `1da872b`, "Moka 4.0")

**Arquitetura final (sem localhost, sem proxy residencial):**

```
[app] → /api/ingest (Vercel)
   ├─ YouTube COM legenda acessível → grátis, instantâneo
   └─ SEM legenda → Transcrição da casa (Transkriptor)
        1. Cache Tencent (SQLite transcricao_jobs) — hit = entrega na hora
        2. Miss → checa pontos → submit Transkriptor → 202 pending
        3. Cliente faz polling step "status" (12s) → "Ouvindo o vídeo… 🎧"
        4. Completed → gate qualidade → salva cache → DEBITA pontos → entrega
```

**Peças:**
- `apps/web/src/lib/video/transkriptor.ts` (novo) — submit/status/segmentos/cache/débito. Endpoints Transkriptor: POST `/transcription/url` (sem `language` = auto-detect — validado pt-BR e en), GET `/files/{orderId}` (status rápido ~2s; a lista `/files` é lenta demais p/ polling — 1028+ jobs, ~2min), GET `/files/{id}/content`.
- `apps/web/src/app/api/ingest/route.ts` — steps `transcript` (cache→submit) e `status` (novo, polling), mensagens 100% amigáveis, 401 (sem conta), 402 (saldo, com link /experimente).
- `apps/web/src/app/video/page.tsx` — polling com estágio "Ouvindo o vídeo… 🎧", retomada de job pendente (localStorage), **sonda localhost + cards LNA REMOVIDOS** do app público (decisão do Miguel).
- `apps/web/src/lib/video/db.ts` — `TranscriptSegment.speaker?`, `transcriptSource: "transkriptor"`, `transcriptText()` marca `[SPK_N]:` nas trocas de falante.
- **API de pontos (Tencent)**: endpoints `GET/POST /transcricao/job` (auth `x-moka-motor-key`) em `app.py` (deploy + restart; backup `app.py.bak_pre_transcricao_20260801`). Uvicorn roda via nohup/setsid (não é systemd!).
- **Preços ao vivo** (`precos_acoes`, backup `moka_pontos.db.bak_pre_transcricao_20260801`): `transcricao_video_15min`=20pts · `transcricao_video_1h`=45pts · `transcricao_video_3h`=110pts.
- **Env**: `TRANSKRIPTOR_API_KEY` + `MOKA_MOTOR_KEY` nos projetos Vercel `moka` e `moka-v3` (production). Motor key também em `Outros/chaves/agentes_labs/.env.unificado`.
- **Diarização**: segmentos trazem `speaker` (SPK_1…N) — resumo/personagens/crítica ganham atribuição de fala.

## ✅ E2E EM PRODUÇÃO (2026-08-01 ~17:30 UTC)

Conta de teste `zcode.e2e.20260801@gmail.com` (200 pts, usuario_id=7 — manter p/ testes):

| Teste | Resultado |
|---|---|
| Vídeo do Miguel (46,3 min) sem conta | 401 amigável "entre com sua conta de pontos ☕" |
| Mesmo vídeo com conta | **cache hit em 5,1s**, 491 segs, **debitado 45 pts** (saldo 200→155), custo registrado $0,278 |
| "Me at the zoo" (19s, inglês) | submit (sem language=auto-detect EN ✅) → 202 → polling → **debitado 20 pts** ($0,0019) |
| consumo no SQLite | 2 débitos `transcricao_video_1h`/`_15min` com `llm_usada=transkriptor` + `recurso_ref=order_id` ✅ |
| X/Twitter link | mensagem amigável "chegam em breve 🙏" ✅ |

## Plano V2 (fases seguintes — pendentes)

| Camada | Status |
|---|---|
| 1. Legendas diretas | ✅ em produção |
| 2. Transkriptor motor principal + pontos por duração | ✅ em produção |
| 3. Fallback yt-dlp→S3→Transkriptor (casos duros + **X/Twitter/Instagram**) | pendente — motorzinho no VPS |
| 4. Fila com aviso 🔔 (push notification) + X/Instagram | pendente |

**Débitos técnicos conhecidos:** (a) cobrança por entrega (cache hit paga igual — decisão: margem máxima, usuário recebe o produto); (b) duração desconhecida no submit (oEmbed não tem duração) → débito pela duração real na entrega; (c) sem idempotência forte no /consumir (proteção: videoteca dedupe + cache); (d) proxy residencial descartado (Transkriptor resolve o bloqueio); (e) `Moka-Producao/` snapshot stale — não recebeu nada disso.

## Registros relacionados

- Bugs: `CEREBRO_NODE_BUGS_RESOLVIDOS.md` → BUG-20260801-MOKA-VIDEO-MSG-TECNICA-PRO-INTERNAUTA, BUG-20260801-MOKA-BOTOES-PAGINA-DIZIAM-TRECHO
- Pesquisa fornecedores: `MEMORIA/memoria_moka_pesquisa_ia_fornecedores_20260722.md` (Groq $0,0007/min segue como alternativa barata quando já temos o áudio)
- Arquitetura: `ARQUITETURA_MOKA/01_visao_geral_aplicativo.md` (já previa Transkriptor→DeepSeek, 30 pts)
