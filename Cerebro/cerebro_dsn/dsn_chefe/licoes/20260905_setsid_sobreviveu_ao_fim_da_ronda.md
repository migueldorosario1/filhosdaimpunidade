# Lição — processo de fundo com setsid+nohup SOBREVIVE ao fim da ronda (05/09/2026, 181ª)

## O quê
A transcrição da live do Nassif (faster-whisper large-v3-turbo) morreu 2 vezes com o fim da sessão da ronda (05:33 e 06:07 — mesmo com saída incremental em disco). Na 3ª tentativa (06:31) disparei com `setsid nohup python3 /tmp/nassif_transcreve2.py > /tmp/nassif_transcricao.txt 2>&1 &` + PID gravado em /tmp/nassif_pid.txt. Verificação na 181ª (07:00): processo VIVO em sessão própria (sid=pid, 1196576), ~31-35% do áudio, CPU ~113% — sobreviveu ao fim da ronda 180ª.

## Por quê
O ciclo da ronda (loop B 30/30) encerra processos-filhos da sessão do shell ao terminar; jobs lançados como pano de fundo comum morrem junto. O setsid cria uma sessão nova (descola do grupo de processos da sessão pai) e o nohup ignora SIGHUP — o processo passa a viver independente do ciclo de ronda.

## Como aplicar (PROTOCOLO)
Tarefa longa crítica (transcrição, download grande, processamento > tempo da ronda) dispara SEMPRE com: `setsid nohup <cmd> > /tmp/<nome>.log 2>&1 &` + `echo $! > /tmp/<nome>.pid`. Verificar na ronda seguinte com `ps -p $(cat /tmp/<nome>.pid)`. NUNCA como job comum da sessão da ronda. Saída incremental em disco desde o início (permite retomar e medir progresso mesmo se morrer).

## Verificação
181ª ronda (07:00): ps mostra o processo vivo; segments.jsonl cresceu (710 segmentos, end 1302s/4177s ≈ 31%). ETA ~07:35-07:50.
