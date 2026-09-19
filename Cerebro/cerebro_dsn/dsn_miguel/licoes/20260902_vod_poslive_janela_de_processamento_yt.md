# 2026-09-02 — VOD pós-live do YouTube tem janela de processamento (retry em loop vence)

## O quê
Depois que uma live do YouTube encerra, o VOD não fica disponível para download na hora:
por ~10-20 minutos os fragmentos do vídeo voltam **HTTP 403** (o processamento do lado do
YouTube ainda não abriu o arquivo). Na noite de 02/09 (Jornal da Fórum bkrMslEN5Co, live
encerrada ~22h2x): tentativas 22:09 (f137, 629KB), 22:16 e o retry até ~22:25 — todos 403 no
mesmo fragmento (856/857); o relance das 22:34 pegou o processamento ABERTO na 1ª tentativa e
baixou o VOD inteiro (253,6MiB, 2h00:50) em ~1 min (client android, `bv*+ba`).

## Por quê
O 403 aqui NÃO é bug do yt-dlp nem do script nem estrangulamento de rota (o mesmo client que
dava 403 às 22:25 baixou liso às 22:34): é o estado do VOD no YouTube — o arquivo pós-live só
fica íntegro depois que o processamento termina. Detalhe útil: o **áudio** do VOD costuma
liberar antes do vídeo (vod_audio 7,3MB às 22:09 vs f137 629KB na mesma hora) — para
transcrição, o áudio basta.

## Como aplicar
1. Download de VOD pós-live = retry em loop com sleep (script `retry_vod_forum.sh`: 20
   tentativas × 2min, clientes android→default, `bv*+ba` → fallback `fmt18`), log por
   tentativa; não declarar falha antes de ~20-30min pós-live.
2. Se a missão é transcrição, tentar o áudio isolado primeiro (libera antes).
3. Registrar "processamento do YT ainda fechado" como WATCH com retry, não como bug.
4. O download em `.part` retoma: o mesmo `-o` + URL continua de onde parou quando o 403 cessa.
