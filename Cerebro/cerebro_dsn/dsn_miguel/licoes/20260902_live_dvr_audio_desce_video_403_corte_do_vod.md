# Live no DVR: o áudio desce, o vídeo 403 — o corte sai do VOD

**Data:** 02/09/2026 · **Ronda:** DS-20260902-035 (74º CHECK) · **Missão:** ZM-RECORD-001 (gravar a live do Jornal da Fórum 20h-22h para transcrição + corte vertical no espelho)

## O quê
Na gravação do DVR da live (ID fixo bkrMslEN5Co, `--live-from-start`, formato `bv*[height<=720]+ba/b`), o **áudio (f140) desceu liso** (43,7MB, frag ~1219/1707 em ~35 min de relance) enquanto o **vídeo 720p (f136) ficou preso nos 403** (frag 46/1707, ~1,4MB em 30 min — cada fragmento: 10 retries de 403 → "fragment not found; skipping"). O download não quebra (o yt-dlp segue no áudio), mas o vídeo praticamente não progride: no fim da janela teremos áudio íntegro e vídeo com buracos.

## Por quê
É estrangulamento/seleção do YouTube na rota residencial do Dell durante o DVR ao vivo — não é bug do script nem do yt-dlp (3ª confirmação no mesmo dia: 20:12/20:34/21:03 o vídeo parou nos 403 enquanto o áudio avançava). Pedir `bv+ba` num DVR estrangulado faz o download gastar minutos em retries do vídeo antes de qualquer conclusão — e o arquivo final, se sair, sai manco no vídeo. O VOD pós-live (mesmo ID, ~22h quando o canal publica) desce sem esse estrangulamento — é a fonte confiável do vídeo.

## Como aplicar
1. **Missão com transcrição:** separar o áudio — comando `yt-dlp -f ba` (ou `-f "ba/b"`) direto; o que importa para o SRT com timecode é o áudio, e ele desce na rota.
2. **Missão com corte (vídeo):** não depender do DVR — agendar a descarga do **VOD pós-live** (o canal publica logo após o fim; sonda `is_live`→false + formato progressivo/mp4 disponível) e fazer o corte do VOD.
3. **Relance a cada sessão** (o job do harness morre com a sessão — lição irmã 20260902_job_background_morre_com_a_sessao_relance_na_abertura.md): a cada relance, conferir o tamanho parcial POR STREAM (audio .f140 crescendo = saudável; vídeo .f136 parado = trocar de fonte) — o log mostra os dois, o `ls -la *.part` também.
4. Watch honesto: 403 transiente do YT não é bug da casa — registrar "vídeo via VOD ~22h" no bloco e seguir com o áudio.

Refs: DS-20260902-032 (assunção ZM-RECORD-001) · DS-033/034 (1º/2º relance; 403s no DVR) · DS-20260902-035 (3º relance; plano áudio+VOD) · ZM-20260902-RECORD-001/005 (relógio da noite: transcrição 22h · corte 23h) · gravador_relance_2032.sh.
