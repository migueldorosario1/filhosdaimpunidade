# Lição — 2026-09-02 · Relance áudio-only: 4ª confirmação do padrão "job morre com a sessão"

## O quê
O 3º relance do gravador da ZM-RECORD-001 (job 21:03, formato `bv*[height<=720]+ba/b`) morreu com o fim da sessão ~21:07 — partes congeladas 21:03 (vídeo f136 3,7MB travado nos 403 do YT, áudio f140 50MB ok). 4ª confirmação do padrão já documentado (lição 20260902_job_background_morre_com_a_sessao_relance_na_abertura.md). O 4º relance (21:30) aplicou a cura da DS-035: download SOMENTE do áudio (`-f ba`), script dedicado `gravador_relance_2130.sh`, log próprio, retries até 22:30, ffmpeg → m4a AAC 96k.

## Por quê
A missão da janela das 22h é a TRANSCRIÇÃO — que precisa só do áudio. O formato combinado `bv+ba` gastava minutos nos retries do vídeo (403s do YT na rota desta live) e arriscava o relance inteiro; separando o `ba`, o download do que importa para a transcrição anda liso (frag ~762 em 1 min). O vídeo para o CORTE (9:16) virá do VOD pós-live (~22h+), que é a fonte confiável (plano B do ZM no CORTE_TONIGHT).

## Como aplicar
1. Missão com janela futura (gravação/transcrição/entrega): verificar o job na ABERTURA da sessão — se morreu (4ª confirmação: morre SEMPRE com a sessão), relance na hora.
2. Antes de relance, perguntar: o que a próxima etapa precisa? Transcrição → só `ba` (áudio); corte → VOD pós-live, não DVR de vídeo 720p com 403.
3. Script dedicado por relance (número no nome + log próprio) com retries até o fim da janela e conversão final embutida.
4. Registrar no bloco da ponte: formato escolhido, prova de vida (log progredindo) e o que cada fonte garante (áudio = transcrição; VOD = corte).

Refs: DS-20260902-036 · ZM-RECORD-001 (assumida DS-032) · lição 20260902_job_background_morre_com_a_sessao_relance_na_abertura.md · lição 20260902_live_dvr_audio_desce_video_403_corte_do_vod.md.
