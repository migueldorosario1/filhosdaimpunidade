# Fórum — Cura estrutural do loop de ERRO "sem legenda" do DS YouTube (fallback Whisper + backoff terminal)

**Ref:** ZM-20260905-008 · **Quem:** ZCode/GLM-5.3 (ZM, Dell) · **Quando:** 05/09/2026 ~10:5x BRT
**Ordem do Miguel** (manhã 05/09, via diagnóstico do DS-N Chefe): investigar e corrigir estruturalmente o loop de erro nos vídeos sem legenda; quando não houver legenda, baixar o áudio e transcrever com Whisper; erro terminal com espera (backoff), nunca repetição imediata; testar com vídeo sem legenda mostrando prova; nada publicado.

---

## O que aconteceu (diagnóstico confirmado no código)

O loop tinha **3 engrenagens** (a caçada 43 do DS-N Ideias e o Chefe apontaram o sintoma; o ponto exato no código):

1. **Robô sem Whisper** (`~/ds_youtube/ds_youtube.py` na Tencent): `transcricionar()` só converte legendas `json3`. O docstring prometia "sem legendas e com áudio → Whisper" desde o batismo 31/08, mas a etapa **nunca existiu no código**. A porta entregava o áudio `.audio.m4a` na Tencent (provado: os 7 vídeos em loop tinham áudio de 100-800KB em `artifacts/`) e o robô ignorava.
2. **Nota de ERRO anexada, nunca substituída** (`setar_status`): cada ciclo grudava mais um `· sem_legenda_e_sem_transcricao` na linha da fila — 438 tokens duplicados acumulados; linhas duplicadas do mesmo vídeo geravam marcação dupla no mesmo ciclo (<30s).
3. **Porta com retry cego de ERRO** (`~/ds_youtube_fetcher/fetcher_youtube.sh` no Dell, linha do grep `PENDENTE|ERRO` adicionada 02/09): re-processava itens ERRO **a cada ciclo de 5 min**, sem espera — marcava BAIXADO de novo (áudio já baixado) e o robô marcava ERRO de novo 15 min depois. **Loop ∞** = os mesmos vídeos marcados a cada :07/:22/:37/:52 desde 01:52. E o `git push` da porta falhava por non-ff (sem rebase), engolindo marcações.

O Nassif (`-szqKhIY-3A`) travou horas nesse loop até a contingência do Chefe (CL baixou áudio pela máquina residencial → faster-whisper manual). O caso do Chefe virou a receita oficial do Whisper do robô.

## O que mudou no código (2 arquivos + 1 novo; backups em cadeia)

**Porta (Dell) `fetcher_youtube.sh` v3** (backup `.bak_pre_whisper_backoff_20260905`):
- Retry de ERRO só com **backoff terminal**: escada 30min → 2h → 8h → 24h; 5ª falha = nota `erro_permanente` (nunca mais pega). Estado em `tmp/estado_erro.json`.
- **BAIXADO só com matéria-prima comprovada NA TENCENT** (ssh pós-scp): legenda json3 OU áudio >10KB. Sem as duas → mantém ERRO com nota `audio_falhou_tentativa_N` (substituída, não acumulada).
- Live em AGUARDANDO_VOD re-sondada a cada 2h (VOD sai → fluxo normal — sub-bug das lives presas).
- Push com `pull --rebase --autostash` antes (fim do non-ff engolindo marcação).
- Candidatos deduplicados (linhas duplicadas = 1).

**Robô (Tencent) `ds_youtube.py`** (backup `.bak_pre_whisper_backoff_20260905`):
- `transcricionar()` agora devolve `(caminho, motivo)`: sem legenda e com áudio → **dispara Whisper em background** (worker novo) e o item AGUARDA sem ERRO; áudio >60min → ERRO terminal `erro_permanente_audio_muito_longo` (manual, precedente Nassif — não prende a CPU); sem legenda E sem áudio → ERRO `sem_legenda_e_sem_transcricao` (a porta só re-oferece com backoff).
- `setar_status` **substitui** a nota (fim do acúmulo).
- Dedupe por vídeo no ciclo (fim da marcação dupla por linha duplicada).

**Worker novo (Tencent) `~/ds_youtube/whisper_worker.py`**: faster-whisper `large-v3-turbo`, int8, beam_size=1, auto-idioma (fila tem pt e en), gera `transcricao.txt` no MESMO formato `[HH:MM:SS]` das legendas + `segments.jsonl` (o decupador lê igual). **Lock global** (`/tmp/ds_youtube_whisper.lock`): 1 transcrição por vez (RAM/2 núcleos). Marker `whisper.marker` com timeout 2h (worker morto → re-disparo automático).

**Saneamento da fila**: 438 tokens duplicados colapsados (30 restantes = 1 por vídeo). Rebase interrompido no clone da Tencent (conflito `de_dell.md`, travava commits de TODOS os robôs) resolvido por união com conteúdo do Chefe preservado — backup `/tmp/de_dell_conflito_*`.

## Prova do teste E2E (vídeo sem legenda, 05/09 10:3x-10:47)

- `vjUTYebq-ts` (CNN, 133s, sem legenda): porta nova → **BAIXADO** com áudio confirmado → robô disparou Whisper → `whisper.log`: "worker start 10:43:39" → "worker fim 10:46:21: 20 segmentos, lang=en" → `transcricao.txt` com timestamps → 2ª corrida do robô → **DECUPADO_ENTREGUE_V4** (ficha `Foruns/youtube/decupagens/vjUTYebq-ts.md` para o redator V4.1) às 10:47. Vídeo em `estado.json processados` = nunca mais reprocessa. **Prova de que o caminho legenda→matéria nunca foi tocado e o caminho áudio→Whisper→matéria agora existe.**
- Backoff provado ao vivo no 1º ciclo: `DvFe9bR2eHA` (vídeo indicado pelo próprio Miguel 09:59) tomou 429/403 do YouTube → porta manteve **ERRO · audio_falhou_tentativa_1** + tries=1 no backoff (re-tentativa só ≥30 min; antes disso o comportamento era marcar BAIXADO às cegas).
- Os outros 6 do loop entraram na fila do Whisper (lock serializa; cada um decupa na corrida seguinte do robô :07/:22/:37/:52).

## Estado / o que falta / preciso do Miguel

- **Pronto:** cura nos 2 lados + worker + saneamento + rebase desatravado; E2E provado. Rollback = restaurar os 2 `.bak_pre_whisper_backoff_20260905` + apagar `whisper_worker.py` (fila saneada não precisa voltar).
- **Falta:** os 6 vídeos restantes decupando nos próximos ciclos (~30-40 min de fila de Whisper); `DvFe9bR2eHA` depende do rate-limit do YouTube passar (backoff cobre). Vigiar 1-2 ciclos do cron real (:52/:07) para confirmar o fluxo automático (teste E2E foi manual).
- **Preciso do Miguel:** nada obrigatório. Opcional: se quiser áudios >60min automáticos também (hoje viram manual, para não prender a CPU — o Nassif ficaria manual), é 1 linha.
- **Publicação:** nada foi publicado; rascunho/gate seguem o fluxo da casa (redator V4.1 → CL publica).

— ZCode/GLM-5.3 (ZM) · 20260905 10:5x BRT
