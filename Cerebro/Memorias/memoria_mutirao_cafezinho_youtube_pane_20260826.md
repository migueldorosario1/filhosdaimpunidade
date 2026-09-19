# 🧠 Memória técnica — Mutirão Cafezinho YouTube Eleições: diagnóstico da pane tripla + correções (26/08/2026)

**Sessão:** ZCode/GLM-5.3 · 26/08 17:45→18:15 BRT
**Fórum irmão (Tema Duplo):** `Foruns/forum_mutirao_cafezinho_youtube_eleicoes_20260826.md`
**Gatilho:** ordem do Miguel 26/08 ~17:45 — mutirão Cafezinho (sabatinas Ponto Poder/O Povo/DN, todos os candidatos, pró-Lula/anti-imperialista), GSN 1/dia, Rio Carta 2/dia, outros 1/semana, por ~2 meses.

## 1. Comandos e provas do diagnóstico

### Pane Transkriptor (desde 25/08 15:29)
```bash
# Lista de jobs: últimos 25 ALL Failed (Cafezinho + GSN + temáticos)
curl -H "Authorization: Bearer $TRANSKRIPTOR_API_KEY" "https://api.tor.app/developer/files?page=1&size=25"
# Último Completed: 25/08 15:29 "JANGADEIRO_ELEIÇÕES_2026" (57min)
# Teste isolado não-YouTube (WAV de 10s, UIC):
POST /developer/transcription/url {"url":"https://www2.cs.uic.edu/~i101/SoundFiles/preamble10.wav",...}
# → 202 + order_id 1787777988293256950, mas job EVAPORA: 404 no /content, ausente de /files
# ⇒ pane de conta/backend (não é só YouTube×Transkriptor)
```
Jobs de hoje no histórico incluem tentativas de outros agentes já mirando sabatinas DN ("Elmano de Freitas (PT) candidato ao Governo do Ceará | SABATINA" 3×, todas Failed).

### YouTube bloqueando os 3 servidores
| Servidor | yt-dlp | Erro |
|---|---|---|
| Dell (local) | qualquer | `HTTP Error 403: Forbidden` |
| Tencent 43.156.151.165 | 2026.08.19 + deno 2.9.5 (instalados nesta sessão) | `Sign in to confirm you're not a bot` |
| NYC 198.199.121.136 | 2026.08.19 + deno (já existiam) | idem bot-check |

### iProyal sem crédito
```bash
curl --proxy "$IPROYAL_PROXY" https://ipinfo.io/json
# → curl: (56) Received HTTP code 402 from proxy after CONNECT
```
Renovado 03/08 (fórum `forum_iproyal_renovacao_fallback_youtube_20260803.md`); crédito de tráfego esgotado. Ledger AGY em `ponte_laura_completa/ledger/agy_miguel.md` registra o desligamento (`YOUTUBE_PROXY_MODE=off`) após ritual dos 30 dias.

### AssemblyAI (teste)
- Chave `ASSEMBLYAI_API_KEY` do cofre: **válida** (`GET /v2/transcript?limit=1` → 200).
- Submit com URL YouTube: aceito, mas falha — `Transcoding failed. File type text/html` (AssemblyAI NÃO baixa YouTube; precisa de arquivo/URL pública de mídia).
- No agente, AssemblyAI hoje só existe como **LLM-gateway coringa** (`youtube_cafezinho.py:1115-1134`, cascade DeepSeek→AssemblyAI→Kimi) — não como transcriber de áudio.

## 2. Correções aplicadas nesta sessão (todas com backup)

| # | Ação | Arquivo/backup |
|---|---|---|
| 1 | Canal DN corrigido: `UCi9JxJuwkMTW_5BzArzf6Ig` (entretenimento!) → `UCMf_wuiFqxdhZI1GVx02mmw` (canal principal DN, sabatinas) | `agent_data/canais_cafezinho_youtube.json` / `.bak_pre_pontopoder_20260826` |
| 2 | Canal "Ponto de Poder (programa — entrevistas)" adicionado: `UChHqX_jmsN3ddng9aCiBT9Q` | idem |
| 3 | `YOUTUBE_PROXY_MODE=off` → `fallback` nos **2 cofres** (canônico + espelho `Outros/chaves/agentes_labs`) | `.bak_pre_proxy_fallback_20260826` (ambos) |
| 4 | Tencent: yt-dlp 2026.03.17 → **2026.08.19** (binário oficial, pip bloqueado por PEP 668) | `/usr/local/bin/yt-dlp.bak_20260826` |
| 5 | Tencent: **deno 2.9.5** instalado em `/home/ubuntu/.deno/bin/deno` | — |

Como achar channel_id de canal YouTube sem API: `curl -sL "https://www.youtube.com/@HANDLE" -H "User-Agent: Mozilla/5.0..." | grep -oE 'UC[a-zA-Z0-9_-]{22}' | sort | uniq -c | sort -rn` — o dominante é o canal. Validar com `feeds/videos.xml?channel_id=`.

## 3. Feeds das sabatinas (frescor verificado 26/08 ~18h)

- **O Povo** (`UCj-RTZE-V3Q6jleatRR9k2A`): sabatinas AO VIVO governo CE — Danilo Soares (Democratas), Vera Lúcia (Novo) hoje; Debates do POVO (Caiado/anistia); Lula×Flávio. ~10 vídeos/dia.
- **Diário do Nordeste** (`UCMf_wuiFqxdhZI1GVx02mmw`): sabatina Roberto Cláudio (vice, 12min + 6 cortes) hoje; live PONTOPODER Camilo Santana ontem. ~10 vídeos/dia.
- **Ponto de Poder** (`UChHqX_jmsN3ddng9aCiBT9Q`): canal do programa, feed parco (1 vídeo 24/08 — Renan×Lula/Augusto Cury).
- **Haddad** (`UCpwjvP7rGvgIXoJIcdGjC3g`) e **Lula** (`UCvO2BExvkAbGMsTGnEnI_Ng`) já estavam na config.

## 4. Estado do pipeline

- Fila revisão WP: **1 draft** (267352) — breaker livre.
- Último draft do agente: **267639** (antes da pane).
- Cron Dell: `0 8,14,20` rodada + `30 14/15` forum11 + `30 22, 0 23, 30 23` jornal — intactos.
- Rodada de prova 17:53 com `--video eyPHXqVNGEU --publicar` (sabatina Roberto Cláudio): Transkriptor Failed 105s → yt-dlp 403 → iProyal 402 → abortada (comportamento correto do fail-safe; nada cacheado pois nada foi transcrito).

## 5. Próximos passos (ao receber o "vai" do Miguel)

1. Recarga iProyal (Miguel) → smoke `curl --proxy $IPROYAL_PROXY ipinfo.io`.
2. Patch `util_youtube_transcript.py`: rota **AssemblyAI** (yt-dlp→S3→AssemblyAI, diarização pt) como transcriber principal enquanto Transkriptor estiver em pane; manter Transkriptor como fallback (pane pode ser temporária — já foi em 16/08, ProxyError 504 que voltou).
3. Reprocessar sabatinas frescas: Roberto Cláudio (eyPHXqVNGEU), Danilo Soares (0A1yRuV0K64), Vera Lúcia (Xdv0d6Slqu8), Elmano de Freitas (achar video_id), live Camilo (TItHTY6zRWw — longa, avaliar janela de duração do agente).
4. Ritmos: reforçar rodadas Cafezinho; GSN 1/dia; Rio Carta 2/dia (já é); temáticos 1/semana — ajustar crons após destrave.
5. Registrar custo novo (AssemblyAI) na telemetria — a página /v6/transkriptor e filtros de gastos foram feitos para Transkriptor; AssemblyAI entra na mesma lógica de "transcrição paga" com campo provedor.

## 6. Lembretes operacionais

- Endpoints Transkriptor de saldo (`/balance` `/credits` `/account` `/me` `/subscription` `/usage`) → todos 403 (a chave não expõe; pane confirmada pelo comportamento do job).
- yt-dlp em servidor: atualização via **binário oficial** (pip = PEP 668); deno via `deno.land/install.sh` (JSR 403 no shell-setup é benigno).
- `YOUTUBE_PROXY_MODE`: `off` | `fallback` (padrão) | `always` — hoje = `fallback` (religado nesta sessão).
