# Memória — Moka Video: transcrição da casa via Transkriptor (Moka 4.0)

> **Data:** 2026-08-01 (tarde/noite BRT) · **Autor:** ZCode (Kimi K3) · **Execução:** aprovada por Miguel ("sim") após apresentação do plano V2.
> **Fórum-irmão (Tema Duplo):** `Foruns/forum_moka_video_transcricao_transkriptor_plano_v2_20260801.md`
> **Commit:** `1da872b` em `migueldorosario1/moka` (main) — "feat(Moka 4.0): transcricao da casa"
> **Estado:** ✅ EM PRODUÇÃO (www.mokareader.com), E2E validado com 2 vídeos reais.

---

## 1. O problema (origem)

Miguel, no app instalado (PWA), tentou ler `youtube.com/watch?v=NDjn1j0d0vs` (podcast As Cunhãs, entrevista Alexandre Padilha, 46 min). O caminho serverless falhou e mostrou mensagem de desenvolvedor ("Vercel/Whisper/npm/yt-dlp/localhost:3100"). Decretos do Miguel nesta conversa:

1. **"Não quero você usar o localhost"** — motor local banido do app público.
2. **"Tem que transcrever qualquer vídeo em qualquer língua do mundo"** — produto de assinatura.
3. Ceticismo quanto a proxy residencial para escala empresarial.
4. Perguntou se dava pra usar **o IP do próprio internauta com autorização** e lembrou: **"a gente tem a API do Transcripto"**.

## 2. Investigação (tudo testado, nada de suposição)

### 2.1 IP do usuário — inviável (prova por CORS)

| Endpoint YouTube | CORS? | Consequência |
|---|---|---|
| `GET /api/timedtext` (dados da legenda) | ✅ `access-control-allow-origin` refletido | browser PODE baixar legenda |
| `GET /watch` (entrega URLs assinadas das legendas) | ❌ sem header | browser NÃO obtém o mapa das legendas |
| `POST /youtubei/v1/player` (URLs de áudio) | ❌ 403 + sem CORS | browser NÃO obtém áudio |

Não existe permissão concedível pelo usuário que destrave isso (diferente de câmera/localização). As únicas vias "com consentimento" são software instalado (banido) ou extensão de navegador (contra o "não passa por loja"; não roda em mobile). **Enterrado.**

### 2.2 Transkriptor — o ativo esquecido

- Chave existente: `TRANSKRIPTOR_API_KEY` (`Outros/chaves/agentes_labs/.env.unificado`).
- Código de produção diário dos agentes Cafezinho: `agents_labs/youtube_v2/util_youtube_transcript.py` (diarização obrigatória, cost guard, gate <100 chars/min, cache 14d).
- Base: `https://api.tor.app/developer` · submit `POST /transcription/url` · polling `GET /files` (lista) · conteúdo `GET /files/{order_id}/content`.
- **Smoke no vídeo do Miguel:** 202 → Completed em **140s** → **491 segmentos, 45.813 chars, 4 speakers** (SPK_1–4), pt-BR limpo. Custo ≈ $0,006/min × 46,3 min ≈ **$0,278**.
- Descoberta: o vídeo **tinha** legenda ASR — quem falhou foi o IP de datacenter do Vercel (YouTube bloqueia), não a ausência de legenda.

### 2.3 Formas dos JSON (medidas ao vivo)

- `/files` item: `{file_id, file_name, parent_folder_id, order_id, created_at, status, minutes}` — `file_name` é o TÍTULO do vídeo (não serve de chave de cache); **a lista completa é lenta (~2 min, 1028 jobs na conta) e sensível a rate-limit** → inútil para polling.
- `GET /files/{order_id}` (item único): **~2s** — serve para polling de status. ✅
- Segmento do content: `{text, StartTime, EndTime, VoiceStart, VoiceEnd, Speaker}` — tempos em **milissegundos**.

## 3. Arquitetura construída

```
[App PWA] → POST /api/ingest (Vercel, serverless)
  step "meta"       → oEmbed/watch (título, canal, thumb) + probe de legendas
  step "transcript" → 1) legendas YouTube (grátis, instantâneo)
                      2) sem legenda → motor da casa:
                         a) cache Tencent hit → entrega na hora
                         b) processing de outro usuário → reusa order_id
                         c) novo → conta+saldo → submit Transkriptor → 202 {orderId}
  step "status"     → polling (12s): cache → /files/{id} → content → gate
                      qualidade → salva cache → DEBITA pontos → entrega
```

**Cache/fila server-side:** tabela `transcricao_jobs` no SQLite da API de pontos (Tencent), endpoints novos `GET/POST /transcricao/job` com auth `x-moka-motor-key` (server-to-server). Vídeo já transcrito nunca é re-submetido ao Transkriptor → custo marginal zero.

**Débito:** via `POST /consumir` do gateway (existente), por entrega, com `recurso_ref=order_id` e `custo_usd` calculado (dur/60 × $0,006). Sem saldo → 402 com link `/experimente`. Sem conta → 401 pedindo login no 🪙.

**Idioma:** submit SEM campo `language` → Transkriptor auto-detecta (validado pt-BR no vídeo 46min e EN no "Me at the zoo").

## 4. Preços por duração (ao vivo em `precos_acoes`)

| Faixa | Ação | Pontos | Custo máx. Transkriptor | Margem aprox. |
|---|---|---|---|---|
| até 15 min | `transcricao_video_15min` | 20 (~R$1,82) | $0,09 | ~73% |
| até 1h | `transcricao_video_1h` | 45 (~R$4,10) | $0,36 | ~51% |
| até 3h | `transcricao_video_3h` | 110 (~R$10,00) | $1,08 | ~40% |

Inseridas com `sqlite3 INSERT` no DB ao vivo (backup `moka_pontos.db.bak_pre_transcricao_20260801`). Mudança de preço = 1 SQL UPDATE. Duração desconhecida no submit (oEmbed não tem) → saldo mínimo 20 pts no submit, débito pela duração REAL na entrega.

## 5. Arquivos alterados/criados

**Moka-Lab (commit `1da872b`):**
- `apps/web/src/lib/video/transkriptor.ts` (NOVO) — tkSubmit/tkJobStatus/tkSegments/tkDuration/tkQualityOk + motorGetJob/motorUpsertJob/motorSaldo/motorDebit + TIER_LIMITS. `PONTOS_BASE` default `https://www.mokareader.com/api/pontos` (mesmo domínio do site → TLS válido; o cert do `sslip.io` falha no python/requests).
- `apps/web/src/app/api/ingest/route.ts` — helpers handleTranscricaoSubmit/handleTranscricaoStatus/entregaTranscricao/debitaTranscricao; IngestBody +`orderId`+`conta`; branch serverless reescrito.
- `apps/web/src/app/video/page.tsx` — polling (12s, timeout 45min), estágio `listening` ("Ouvindo o vídeo… 🎧", "seus pontos só são descontados quando o texto fica pronto"), retomada via `localStorage("mokavideo.pendingJobs")`, erro com link (`/experimente`), **removidos** probeLocalIngest/LNA cards/badges de motor local.
- `apps/web/src/lib/video/db.ts` — `TranscriptSegment.speaker?`, `transcriptSource+"transkriptor"`, `transcriptText()` com `[SPK_N]:`.

**Tencent (`/home/ubuntu/moka/pontos_api/`):**
- `app.py` — bloco "12. Transcrição de vídeo" (tabela + 2 endpoints + auth). Backup `app.py.bak_pre_transcricao_20260801`. Restart: uvicorn via `setsid nohup` (não é systemd — processo morre se a máquina reiniciar; **débito técnico: criar unit systemd**).
- `.env` — `MOKA_MOTOR_KEY` (hex 32B) adicionada.

**Vercel (projetos `moka` E `moka-v3`, production):** `TRANSKRIPTOR_API_KEY`, `MOKA_MOTOR_KEY`.
**Cofre canônico:** `MOKA_MOTOR_KEY` também em `Outros/chaves/agentes_labs/.env.unificado`.

**Backups:** `Moka/backups/moka_V4.0_pre_transcricao_casa_2026-08-01.zip` (repo completo) + DB e app.py no servidor.

## 6. E2E em produção (2026-08-01 ~17:30–18:00 UTC)

Conta de teste `zcode.e2e.20260801@gmail.com` (usuario_id=7, 200 pts via convite MOKA-MGCJ5 — **manter para testes futuros**):

| # | Teste | Resultado |
|---|---|---|
| 1 | NDjn1j0d0vs sem conta | 401 "entre com sua conta de pontos ☕" ✅ |
| 2 | NDjn1j0d0vs com conta | **cache hit 5,1s**, 491 segs, `debitado:45`, saldo 200→155 ✅ |
| 3 | jNQXAC9IVRw (19s, EN) | submit sem language → auto-detect EN ✅, 202→polling→segs com SPK_1 ✅ |
| 4 | consumo SQLite | `transcricao_video_1h` 45pts/$0,278 e `transcricao_video_15min` 20pts/$0,0019, `llm_usada=transkriptor` ✅ |
| 5 | Link X/Twitter | "chegam em breve 🙏" ✅ |
| 6 | Seed do cache | NDjn1j0d0vs semeada com a order da manhã (46,3 min, 79.201 chars) — custo zero de re-processamento |

## 7. Decisões e trade-offs (registradas para o futuro)

1. **Cache hit cobra preço cheio** (não é grátis): cada entrega é uma venda do produto; custo marginal zero vira margem. Proteção contra double-charge: videoteca dedupe (IndexedDB) + cache server-side.
2. **Sem proxy residencial**: Transkriptor internaliza o anti-bloqueio (é o negócio deles). Escala = problema contratual deles.
3. **Sem idempotência forte no /consumir** (débito técnico aceito): risco de double-debit em polling concorrente é segundos-largo; mitigação real = dedupe da videoteca.
4. **Qualidade:** gate <100 chars/min rejeita SEM cobrar (regra dos agentes, anti-alucinação VAD).
5. **Localhost morto no app público:** `probeLocalIngest`/LNA permanecem em `config.ts` (dead code) para uso dev; a UI não chama mais.
6. **`Moka-Producao/` NÃO recebeu nada** (snapshot stale — fonte canônica é Moka-Lab).

## 8. Pendências (Fases 2+)

- **X/Twitter e Instagram** — motorzinho yt-dlp→S3→Transkriptor num VPS (o próprio script python dos agentes já faz o fluxo S3).
- **Push 🔔** quando a transcrição ficar pronta (PWA push).
- **Systemd unit** pro uvicorn da API de pontos (hoje nohup — não sobrevive a reboot).
- **Avaliar systemd/timer p/ reconciliar jobs `processing` órfãos** (se o usuário abandonar o polling, o job fica processing até outro usuário pedir o mesmo vídeo).
- Migrar leituras BYOK-Whisper antigas? Não — o caminho Whisper local (yt-dlp) ficou intacto para dev.

## 9. Lições

1. **Pergunte ao Cérebro antes de propor arquitetura:** o ativo decisivo (Transkriptor pago + script testado) já existia e quase foi ignorado em favor de proxies.
2. **Meça os endpoints antes de desenhar o fluxo:** a lista `/files` lenta (2 min) derrubaria qualquer design que a usasse para polling; o item único (2s) salvou.
3. **Teste TLS na stack certa:** o cert `sslip.io` passa no curl/edge mas falha no python/OpenSSL — por isso o default server-side usa o domínio do site.
