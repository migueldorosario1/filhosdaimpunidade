# Lição 20260903 — Fila do YouTube: o Chefe reconstruiu com dedupe e o storm era append, não conflito

## O quê
Na ronda 09:30, a `queue_youtube.md` (84 linhas) tinha 3 blocos de marcadores de conflito COMMITADOS
(`<<<<<<< HEAD ... >>>>>>> sync: 2026-09-03 07:37 — 10280 arquivos`) + linhas duplicadas (73 linhas
de entrada → só 41 vídeos únicos; até ~48× "· sem_legenda_e_sem_transcricao" na MESMA linha). O robô
DS YouTube (15/15) estava em retry storm (12+ commits em 30s, canal com ~30 msgs em 90s) e o CHECK
dele contava 32 ERRO — número inflado pelo próprio lixo. Sinalização das 09:10 não parou; o Chefe
EXECUTOU a reconstrução 09:34: dedupe por video_id (uma linha por vídeo, status mais avançado
preservado), marcadores removidos, notas repetidas colapsadas → 41 linhas limpas.

## Por quê
Causa raiz revelada no dedupe: além do sync commitar marcadores, o robô ANEXAVA
"· sem_legenda_e_sem_transcricao" a cada ciclo em vez de SUBSTITUIR o campo STATUS — cada vídeo em
ERRO/BAIXADO crescia ~1 token por ciclo (~48 tokens ≈ 12h de ciclos). O parser lia o próprio lixo e
re-processava. Duas lições de implementação minhas: (1) regex de status `[A-Z_]+` TRUNCA
"DECUPADO_ENTREGUE_V4" → `[A-Z0-9_]+` (a 1ª rodada do dedupe rebaixou 3 vídeos de DECUPADO para
ERRO/PENDENTE; peguei no diff e refiz a partir do `git show HEAD:`); (2) conferir o resultado com
amostra por video_id, não só com contagem.

## Como aplicar
- Dono que não para após sinalização = Chefe executa o conserto e REGISTRA a regra no canal do dono
  (pull antes de push; SUBSTITUIR status por video_id, nunca anexar; ERRO sem legenda = cooldown).
- Fila compartilhada com robô ativo: reconstruir a partir do `git show HEAD:` (original íntegro) e
  commitar/pushar rápido, de preferência fora da janela de burst do robô.
- `grep -c '<<<<<<<'` = 0 vale também para lixo que JÁ VEM commitado do origin (o dono pode nunca
  ter visto o marcador).
- Contagem de status de robô que lê arquivo corrompido = sintoma, não diagnóstico.
