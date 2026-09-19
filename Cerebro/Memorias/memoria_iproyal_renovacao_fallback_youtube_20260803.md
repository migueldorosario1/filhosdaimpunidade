# Memória — Renovação IPRoyal: credencial no cofre + fallback anti-bloqueio no agente YouTube

**Data:** 2026-08-03 ~15:50 BRT · **Autor:** Kimi K3 (ZCode) · **Fórum (Tema Duplo):** `Cerebro/Foruns/forum_iproyal_renovacao_fallback_youtube_20260803.md`

Log técnico completo da implementação. Fórum tem o resumo executivo; aqui está o como.

---

## 1. Auditoria prévia (onde a credencial estava — e onde não estava)

| Local | Achado |
|---|---|
| Cofre canônico `Outros/chaves/agentes_labs/.env.unificado` | ❌ 0 ocorrências IPROYAL |
| Espelho `Projeto Cafezinho Agentes/root/.env.unificado` | ❌ 0 ocorrências |
| `Global South News/root/chaves_gsn.env:30` | `# export IPROYAL_PROXY=` — comentada **e vazia** (sha8 `e3b0c442` = string vazia) |
| `~/.gemini/antigravity-cli/brain/5b55ae63-.../scratch/toggle_proxy.sh` | ✅ ÚNICO local com a credencial — user+pass em **plaintext** (violação Art. 1º), origem: ativação desktop AGY 03/07 |

Registros históricos relevantes no Cérebro: sessão `afcasYEu` (21/05, 7 dias, falhou em Beijing — timeout/reset); carta AGY 03/07 (proxy NYC no GNOME; sintaxe de estado `newyork`; PACER bloqueado pelo provedor → bypass `.gov`/`.gov.br`); AUTH-047 (16/06, YouTube destravado via IPRoyal).

## 2. Smoke da credencial renovada (03/08 ~15:35 BRT)

Leitura dos valores do `toggle_proxy.sh` (sem imprimir) + `curl -x <proxy> https://ipinfo.io/json`:
- **Resultado: HTTP 200** — exit `68.161.182.220` New York City (AS701 Verizon Business).
- Fingerprints: user `sha8:945b3368` · pass `sha8:9dd50483` · URL completa `sha8:ed44d32f` (len=117).
- Parâmetros de sessão no password: `session-XXXXXXXX_lifetime-30m_country-us_state-newyork`.

## 3. Gravação nos cofres

Bloco anexado aos DOIS cofres locais (canônico + espelho — o loader `nucleo_tematico/chaves.py` só alcança o espelho; bug de path do canônico `Outros/chaves/agentes_labs` fora do search path, anotado para a OPERAÇÃO COFRE ÚNICO):

```
IPROYAL_PROXY="http://<user>:<pass>@geo.iproyal.com:12321"
YOUTUBE_PROXY_MODE="fallback"
```

Verificação pós-gravação: sha8 idêntico (`ed44d32f`) nos dois arquivos. Valor nunca impresso em chat/fórum.

## 4. Helper `util_proxy_iproyal.py` (novo, 210 linhas)

Local: `Projeto Cafezinho Agentes/agents_labs/youtube_v2/util_proxy_iproyal.py` (mesmo dir do transcritor — já está no `sys.path` do agente).

- `_ler_var(nome)`: ambiente → espelho → canônico (sem dependência de imports do ecossistema).
- `modo()`: `off|fallback|always`; sem credencial → `off` forçado; valor inválido → `fallback`.
- `url_sessao_nova()`: regex `session-[A-Za-z0-9]+` → `session-<8 alnum aleatórios>` por chamada (rotação real, sticky só durante a chamada; demais parâmetros preservados).
- `classificar_erro(stderr)`: `bot_check|http_429|http_403|geo_block|network|outro`.
- `rodar_yt_dlp(args, timeout, video_id, op, log)`: tentativa 1 = direto (ou proxy se `always`); se modo=fallback e erro ∈ {bot_check, 429, 403, geo} → retenta com proxy de sessão nova; timeout NÃO dispara proxy (conservador). Retorna `CompletedProcess`; `TimeoutExpired` propagado (contrato idêntico ao `subprocess.run`).
- `_telemetria()`: append JSONL, nunca bloqueia fluxo. Caminho: `agent_data/v4_cafezinho_youtube/telemetria_proxy.jsonl`.
- CLI: `--status` (modo+credencial) e `--resumo` (contadores + veredito manter/desligar).

## 5. Patches (backups `.bak_pre_20260803_iproyal` em todos)

**`agentes_cafezinho/youtube_cafezinho.py`** (import duro — mesmo repo, fail-fast):
- L60 `_duracao_segundos` → `rodar_yt_dlp(..., op="duracao")`
- L181 `_estreia_futura` → `op="estreia_futura"`
- L693 `_live_status` → `op="live_status"`

**`agents_labs/youtube_v2/util_youtube_transcript.py`** (import **defensivo** `try/except ModuleNotFoundError` com `_rodar_yt_dlp=None` → fallback ao `subprocess.run` histórico; preserva consumidores antigos como GSN):
- `_baixar_audio_yt_dlp` (download MP3, timeout 600) → `op="download_audio"`
- `_duracao_segundos` (probe, timeout 20) → `op="duracao_transcritor"`

**`toggle_proxy.sh`**: reescrito para ler `IPROYAL_PROXY` do cofre canônico e extrair user/pass/host/port via sed; sem nenhum segredo no arquivo. Mantidos bypass `.gov`/`.gov.br` e modo off.

Não tocado (decisão de arquitetura): RSS (feedparser), thumbnails (requests) e chamadas à API Transkriptor seguem **diretos** — tráfego minúsculo e/ou destino não-YouTube.

## 6. Testes executados (03/08 15:45-15:47 BRT)

```
TESTE 1 (always→proxy):  rc=0 | duração=7344 | lat 8,0s | sessão fresca ...dYxlNlr0
TESTE 2 (fallback→direto ok): rc=0 | duração=7344 | lat 5,6s | via=direto
TESTE 3 (off→direto):    rc=0 | lat 4,6s | modo=off
py_compile nos 3 arquivos: ok · bash -n toggle_proxy.sh: ok
import youtube_cafezinho: ok · modo visto pelo agente: fallback
--resumo: contadores corretos (3 tentativas, 1 proxy, veredito coerente)
```

Vídeo de teste: `NshQJcHUXL8` (citado no docstring do próprio agente). Telemetria gravada e inspecionada linha a linha.

## 7. Moka Reader — investigação e veredito

`Outros/Aplicativos/Moka/Moka-Producao/apps/web/src/app/api/` contém apenas: `auth`, `proxy` (relay CORS para provedores de IA com allowlist), `proxy-stream`, `tts`. **Nenhuma ingestão server-side** (sem RSS, trafilatura ou yt-dlp). YouTube no Reader = link estático na página "Sobre". ⇒ Nada a ligar hoje.

O consumidor Moka é o **Moka Video** (`Outros/Aplicativos/MokaVideo`): `/api/ingest` roda yt-dlp+ffmpeg server-side; README prevê deploy em VPS (datacenter = alvo primário de bot-check). Quando o servidor de ingestão entrar em produção (fase 2), aplicar o mesmo padrão no route Node: ler `IPROYAL_PROXY` do ambiente, tentar direto, em erro de bloqueio retentar com `--proxy` e sessão nova. Variável já está no cofre; padrão documentado aqui e no Cofre.

## 8. Chave de desligamento + telemetria (pedido explícito do Miguel)

- **Desligar:** editar cofre → `YOUTUBE_PROXY_MODE="off"`. Zero código, zero deploy. Com `off`, bloqueios continuam sendo **logados** (telemetria marca o que TERIA acionado proxy) — dados para eventual religamento.
- **Decidir (~30 dias):** `python3 Projeto\ Cafezinho\ Agentes/agents_labs/youtube_v2/util_proxy_iproyal.py --resumo`. Veredito automático: "nunca necessário → candidato a desligar" / "salvou N → manter".

## 9. Rollback

1. Cofres: restaurar `.env.unificado.bak_pre_20260803_iproyal` (2 arquivos) ou apagar o bloco IPRoyal.
2. Código: restaurar os 4 `.bak_pre_20260803_iproyal`. O agente volta ao comportamento histórico (sem proxy) mesmo SEM rollback — basta `YOUTUBE_PROXY_MODE=off`.
3. Telemetria jsonl é append-only inócuo; pode ser arquivado.

## 10. Pendências registradas

- Espelhamento servidores (Tencent/NYC) caso yt-dlp rode lá — Constituição §2. Beijing: não.
- Bug de path: loader `chaves.py` não alcança `Outros/chaves/agentes_labs/.env.unificado` (canônico) — anexar à OPERAÇÃO COFRE ÚNICO.
- Nota: o `youtube_cafezinho.py` recebeu hoje mais cedo (15:25 BRT, outra sessão Kimi) o fix B+C `VERIFICAR_NOME`; meus patches foram aplicados sobre essa versão (backup pré-iproyal já a contém).


---

## ADENDO 2026-08-03 ~16:00 BRT — Moka VIDEO integrado (Miguel: "eu queria dizer Moka Video")

Miguel corrigiu o alvo: era Moka **Video**, não Reader. Implementado na mesma sessão:

- **`Outros/Aplicativos/MokaVideo/src/lib/iproyal.ts` (novo, ~150 linhas):** espelho TS do helper Python — `readVar` (env → espelho → canônico), `proxyMode` (`MOKA_PROXY_MODE` → herda `YOUTUBE_PROXY_MODE` → default fallback; sem credencial → off), `freshSessionUrl`, `classifyError` (mesmas classes), `telemetry` (mesmo jsonl, `fonte:"moka_video"`), `runYtDlp` (mesmo contrato do execFile promisificado: resolve {stdout,stderr} ou rejeita com erro da tentativa final; erro carrega `_classeIproyal` para a decisão de retentativa).
- **`src/app/api/ingest/route.ts`:** import `@/lib/iproyal`; call sites `ytDlpJson` (op `meta_json`) e `downloadAudioChunks` (op `download_audio`) migrados de `run("yt-dlp",...)` para `runYtDlp(...)`. Backup `.bak_pre_20260803_iproyal`. Chamadas `ffmpeg` e o probe `yt-dlp --version` (caminho serverless) NÃO migrados (não são tráfego YouTube de risco).
- **Helper Python atualizado:** telemetria agora grava `fonte` (default `agente_youtube`) e `--resumo` mostra breakdown por fonte — resumo único para a decisão de 02/09.
- **Testes:** `tsc --noEmit` exit 0; 3 modos ao vivo via `node --experimental-strip-types` (always→proxy 5,4s / fallback→direto 2,5s / off→direto 2,4s; duração 7344 nos 3); telemetria unificada confirmada (6 linhas: 3 `agente_youtube` + 3 `moka_video`).
- **Rollback Moka:** restaurar `route.ts.bak_pre_20260803_iproyal` e apagar `src/lib/iproyal.ts`; ou simplesmente `MOKA_PROXY_MODE=off` no cofre.


---

## ADENDO 2 — 2026-08-03 ~16:45 BRT — Cascata multi-provedor + pesquisa de alternativas

**Contexto:** após análise de compliance (ToS IPRoyal permite uso comercial próprio, cláusula 4.2; risco = só a conta IPRoyal, comunicado ao Miguel em linguagem simples), Miguel declarou a conta descartável e pediu sistema robusto multi-fallback.

**Pesquisa (subagente, 57 tool calls, fontes citadas no fórum):** tabela completa no fórum §Cascata. Destaques: NetNut apreendida pelo FBI (verificado por 2 fetches); PacketStream 11% Google (inviável); IPRoyal com queixas Trustpilot de IPs datacenter vendidos como residencial (reforça cascata); APIs de transcrição (ScrapeCreators/Supadata) como camada alternativa futura.

**Upgrade cascata (Python `util_proxy_iproyal.py` reescrito + TS `src/lib/iproyal.ts` reescrito):**
- `_VARS_PROVEDORES = (IPROYAL_PROXY, PROXY_RESIDENCIAL_2, PROXY_RESIDENCIAL_3)`; slots vazios pulados; nome do provedor derivado do host.
- `url_sessao_nova(url)`: regex ampliado `(session|sessid)[-_]` com preservação de prefixo/separador; URL sem token de sessão retorna intacta (rotação por requisição do provedor).
- `rodar_yt_dlp`: fallback = direto → prov1→2→3 (só em erro-gatilho); always = prov1→2→3 (qualquer falha); off = direto (bloqueios logados). Telemetria ganhou campo `provedor`; `--status` lista a cascata; `--resumo` mostra por fonte e por provedor.
- Slots dormentes documentados nos 2 cofres (com candidatos e instrução de ativação).

**Testes (8/8 ✅):** py_compile; enumeração [iproyal, dataimpulse, webshare]; rotação sessão 3 formatos; simulação cascata completa mockada (direto bot_check → iproyal falha → dataimpulse salva, 3 tentativas na ordem exata); modo off 1 tentativa; tsc --noEmit; Node enumeração + always ao vivo IPRoyal (7344s); import do agente.

**Ativação futura do slot 2 (runbook):** comprar provedor → colar URL completa em `PROXY_RESIDENCIAL_2` nos 2 cofres → pronto (zero código, próximo cron já usa).


---

## ADENDO 3 — 2026-08-03 ~17:15 BRT — Pesquisa APIs de transcrição + prova ao vivo SearchAPI

**Pedido Miguel:** "quero uma lista de apis de transcrição para usar no Moka Video".

**Prova ao vivo (17:05 BRT):** engine `youtube_transcripts` da SearchAPI com a chave existente em `Projeto Cafezinho Agentes/root/chaves_novas.env` (sha8:14c0c9e9) — vídeo NshQJcHUXL8 → **2.760 segmentos** `{text, start(s), duration(s)}`, `available_languages: ['pt']`. ⚠️ engine no singular (`youtube_transcript`) retorna HTTP 400 — usar plural. **Ressalva de governança:** essa chave é a reserva do gate fact-check (SearchAPI); uso no Moka divide cota (só visível no dashboard). NÃO integrada ao Moka sem OK do Miguel.

**Ranking + descartadas + tabela ASR:** ver fórum do dia §APIs. Fontes verificadas 03/08: supadata.ai/pricing, docs.scrapecreators.com/v1/youtube/video/transcript, scrapebadger.com/pricing, searchapi.io/docs/youtube-transcripts, socialkit.dev/pricing, apify.com (streamers/youtube-scraper $0,005/vídeo; pintostudio $0,01), assemblyai.com/pricing, deepgram.com/pricing, gladia.io/pricing, speechmatics.com, rev.ai.

**Detalhe de integração futura (para quem executar):** encaixar a camada API no `/api/ingest` entre "sem legendas" e "download de áudio" — função `transcricaoViaApi(videoId)` testando provedores na ordem configurada (`TRANSCRICAO_API_ORDEM`), cada um com sua chave no cofre (`SCRAPECREATORS_API_KEY`, `SUPADATA_API_KEY`, `SEARCHAPI_API_KEY` já existe) e telemetria `fonte:"moka_video", via:"api_transcricao", provedor:<nome>` no mesmo jsonl. Schemas: ScrapeCreators `transcript[]{text,startMs,endMs}`; Supadata `content[]{text,offset,duration}`; SearchAPI `transcripts[]{text,start,duration}`.
