# Memória — DS YouTube: cura do loop de ERRO "sem legenda" (Whisper + backoff terminal) — 05/09/2026

**Ref:** ZM-20260905-008 · ZCode/GLM-5.3 (ZM, Dell) · 05/09/2026 10:3x-11:0x BRT
Fórum gêmeo: `Foruns/youtube/forum_youtube_cura_loop_sem_legenda_whisper_20260905.md`

## Arquitetura (contexto)

| Peça | Onde | Ciclo |
|---|---|---|
| Porta de download `~/ds_youtube_fetcher/fetcher_youtube.sh` | **Dell** (IP residencial — YouTube bloqueia datacenter, testado Tencent/NYC 31/08) | cron */5, flock interno |
| Robô `~/ds_youtube/ds_youtube.py` | **Tencent** | cron :07/:22/:37/:52, flock `/tmp/ds_youtube.lock` |
| Fila | `cerebro/Foruns/youtube/queue_youtube.md` (repo cerebro-miguel, lida/gravada VIA SSH na Tencent) | — |
| Artifacts | `~/ds_youtube/artifacts/<vid>/` na Tencent (porta entrega via scp) | — |

## Causa raiz do loop (pontos exatos no código)

1. `transcricionar()` do robô só lia `*.json3` — **Whisper prometido no docstring nunca foi implementado**; áudio `.audio.m4a` entregue e ignorado.
2. `setar_status(vid, "ERRO", nota=...)` **anexava** a nota a cada chamada → 438 tokens `sem_legenda_e_sem_transcricao` acumulados na fila; linhas duplicadas do mesmo vid → 2 marcações no mesmo ciclo (explica os pares <30s de 06:22/08:22).
3. Porta (Dell) selecionava `STATUS: (PENDENTE|ERRO)` (retry_erro 02/09) **sem espera** → re-baixava e re-marcava BAIXADO a cada 5 min → robô re-marcava ERRO a cada 15 min → loop ∞ desde 05/09 01:52 (vjUTYebq-ts/8m0Y7mWWs2I/rpFMvQfzY1U + MrggA3TvOuE/6qXIQKXCHAQ/ubUmAoQbSZw/DIavgncHyiI).
4. Push da porta sem rebase → non-ff silencioso ("hint: Note about fast-forwards") engolia marcações.
5. Colateral: rebase interativo interrompido no clone da Tencent (UU `de_dell.md`, pick do Chefe DS-N-20260905-188) **bloqueava commits de todos os robôs** ("Committing is not possible because you have unmerged files").

## Mudanças (comandos/provas)

**Porta v3** (`fetcher_youtube.sh`, backup `fetcher_youtube.sh.bak_pre_whisper_backoff_20260905`):
- Seletor de candidatos em python inline: PENDENTE sempre; ERRO com escada `ESCALA=[30min, 2h, 8h, 24h]`, `tries>=5` → nunca mais (nota `erro_permanente` gravada na 5ª falha); AGUARDANDO_VOD re-sondado a cada 2h (`vod_<vid>` no estado); estado em `tmp/estado_erro.json`; dedupe de candidatos.
- Áudio: `-f "139/249/251/bestaudio"`, exige arquivo local >10KB E confirmação por ssh na Tencent (`stat -c%s artifacts/$VID/$CHAVE`) — BAIXADO só com legenda OU áudio confirmado; senão mantém ERRO com nota `audio_falhou_tentativa_N` (5ª = `erro_permanente_sem_materia_prima_tentativa_5`).
- Notas velhas (`sem_legenda_e_sem_transcricao`/`audio_falhou*`/`erro_permanente*`) removidas ao marcar BAIXADO.
- Push: `git pull -q --rebase --autostash origin main && git push` (autostash obrigatório: working tree da Tencent tem vivos de 3os).
- Validação: `bash -n` OK; seletor testado com estado fictício (tries=1/10min → bloqueado; tries=1/95min → liberado; tries=5 → nunca).

**Robô** (`ds_youtube.py` na Tencent, backup `ds_youtube.py.bak_pre_whisper_backoff_20260905`):
- `transcricionar()` → `(caminho|None, motivo)`: `ok | sem_fonte | whisper_disparado | whisper_em_andamento | audio_muito_longo`.
- Novas `_duracao_audio()` (lê `duration` do info.json) e `disparar_whisper()` (marker + `Popen nohup` do worker).
- Motivos no loop: `whisper_disparado` → 1 linha de canal 🎙️ + commit, **sem ERRO**; `whisper_em_andamento` → silêncio (marker fresco <2h; velho >2h = worker morto → marker removido → re-disparo); `audio_muito_longo` (>3600s) → ERRO `erro_permanente_audio_muito_longo` (manual — precedente Nassif); `sem_fonte` → ERRO `sem_legenda_e_sem_transcricao` (terminal com backoff na porta).
- `setar_status`: nota **substituída** (`.replace(f" · {nota}", "")` antes de anexar).
- Dedupe `vistos` por vid no ciclo.
- `py_compile` OK local e na Tencent (python 3.12).

**Worker novo** `~/ds_youtube/whisper_worker.py` (Tencent): faster-whisper `large-v3-turbo` (cache hub 1.6G confirmado), int8, beam_size=1, `vad_filter=True`, idioma auto; saídas `transcricao.txt` (formato `[HH:MM:SS] texto` = mesmo das legendas) + `segments.jsonl`; **lock global `fcntl.flock` em `/tmp/ds_youtube_whisper.lock`** — pega o lock ANTES do import do modelo (workers em fila não gastam RAM); marker reescrito ao pegar o lock; removido ao fim.

**Saneamento fila**: script one-shot colapsou 438 tokens duplicados (dedupe por token ` · ` mantendo 1ª ocorrência); commit `b6ade05d5` + push.

**Rebate da Tencent**: sem marcadores reais no arquivo (grep `^<<<<<<<` = 0; as citações eram texto de fóruns antigos) → `git add de_dell.md && GIT_EDITOR=true git rebase --continue` → pick DS-N-20260905-188 commitado com os 6 arquivos do Chefe (+59 linhas) preservados; backup prévio `/tmp/de_dell_conflito_*.md`; branch volta a bater com origin.

## Prova E2E (05/09)

- Porta manual 10:39-10:41: `DIavgncHyiI → BAIXADO` (áudio confirmado); `DvFe9bR2eHA` (indicação do Miguel 09:59) tomou HTTP 429 (legenda) + 403 (áudio) → **ERRO · audio_falhou_tentativa_1** + `estado_erro.json {"DvFe9bR2eHA": {tries:1, last:10:41}}` — backoff real no 1º ciclo, re-tentativa ≥11:11.
- Robô manual 10:43: 7 workers Whisper disparados (7 markers), canal com 7 linhas 🎙️ únicas; lock serializa (8m0Y "aguardando lock global").
- `vjUTYebq-ts` (CNN 133s sem legenda): `whisper.log` start 10:43:39 → fim 10:46:21 "20 segmentos, lang=en" → `transcricao.txt` 2412B + `segments.jsonl` → robô 10:47 → **DECUPADO_ENTREGUE_V4** com ficha `decupagens/vjUTYebq-ts.md` (frontmatter CNN/título/duração/transcrição) → `estado.json processados` 33 (último 05/09 10:47).

## Armadilhas/lções

- **Docstring ≠ código**: a promessa do Whisper existia no texto desde 31/08; ninguém conferiu a implementação. Checar função por função, não o comentário.
- **Retry cego de ERRO = gerador de loop**: qualquer fila que re-oferece item de erro no mesmo ciclo do marcador de erro faz loop ∞; retry de erro SEMPRE com backoff + teto de tentativas + nota substituída (nunca anexada).
- **BAIXADO às cegas**: status de sucesso sem verificar o artefato na destino é mentira operacional — a porta marcou BAIXADO mil vezes sem matéria-prima utilizável.
- **flock externo+interno** (bug 01/09, já fichado) vs **lock global de recurso caro**: Whisper serializado por flock em arquivo no WORKER (antes do import do modelo) — N workers disparados, 1 modelo na RAM.
- **Autostash obrigatório** em `pull --rebase` de repos com working tree sujo de vivos de 3os (Tencent) — sem isso o rebase falha e o push cai em non-ff silencioso.
- **Rebase interrompido trava a fábrica inteira**: clone compartilhado com UU bloqueia commit de TODOS os robôs que usam o repo; resolver por união preservando conteúdo de 3os (backup antes).
- Limiar de áudio 10KB: shorts muito curtos não são descartados; áudio <10KB = download falho/corrompido.

## Estado final

- Loop morto: os 7 vídeos têm agora caminho real (Whisper); itens em `processados` nunca reprocessam; ERRO só com backoff 30min→24h→permanente.
- Faltando: 6 vídeos decupando na fila serial do Whisper (~30-40 min); DvFe9bR2eHA aguarda rate-limit; conferir 1º ciclo 100% automático (:52/:07).
- Rollback: restaurar os 2 `.bak_pre_whisper_backoff_20260905` + remover `whisper_worker.py` + (opcional) restaurar fila do `queue_youtube.md.bak_pre_saneamento_20260905`.

— ZCode/GLM-5.3 (ZM) · 20260905 11:0x BRT

## ADENDO 1 — pós-E2E (11:2x-11:4x): áudio mudo do storm + VAD em clipe curto

- Sintoma: 3 clipes (17-51s BBC/TRT) → worker "0 segmentos" + transcricao.txt 0 bytes → robô re-dispararia para sempre (transcrição vazia <limiar). Diagnóstico: `ffmpeg -af volumedetect` → max_volume **-91dB** = track silenciosa servida pelo YouTube no storm (em vez de 403); ubUmAoQbSZw do mesmo lote: -25dB normal.
- Cura em 3 camadas: worker v3 (VAD → volumedetect ≤-60dB = `audio_mudo.marker`; >-60dB → passada sem VAD p/ fala rápida curta); robô (limiar 500→200 bytes + `whisper_ruido` ≤200 pós-worker → apaga áudio + ERRO `audio_mudo_refazer_download_N` com freio 3× → permanente); porta (cache-clean local+Tencent da flag mudo + re-download em **opus 249/250/251** — 139 m4a vinha mudo).
- Lições: (1) "0 segmentos" tem 2 causas opostas (track muda × VAD agressivo) — volumedetect separa; (2) transcrição vazia em disco NUNCA (worker sempre decide: fala, ou marker terminal); (3) re-download de item doente precisa trocar codec E limpar cache (senão "already downloaded" devolve o mesmo arquivo doente); (4) limiar de aceitação deve casar com o menor áudio legítimo da fila (17s ≈ 300+ bytes, não 500).
- Logs dos 3: whisper.log com "VAD=0 seg, max_volume=-91.0dB" → marker; canal com linha 🔇 1× por tentativa; estado do robô `mudo: {vid: N}`.

— ZCode/GLM-5.3 (ZM) · 20260905 11:4x BRT
