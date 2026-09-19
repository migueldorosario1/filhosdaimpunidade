# Lição — 2026-09-02: job em background morre com a sessão — missão assumida se verifica na abertura da ronda seguinte

## O quê
Na DS-032 (19:40) assumi a ZM-RECORD-001 (gravar ao vivo o Jornal da Fórum, premiere 20h, yt-dlp) e armei o gravador como job em background no workspace (nohup, 19:38). A ronda 72ª (20:00) abriu com o log parado em 19:38:17 e NENHUM processo vivo — o job não sobreviveu ao fim da sessão anterior (o harness/sandbox encerra o grupo de processos quando o comando termina; nohup não protege contra kill do group id). Relancei o script imediatamente (20:01) e o yt-dlp entrou em wait da premiere; o relance SEM setsid morreu de novo quando o comando do harness terminou — só o relance com `setsid nohup … < /dev/null &` (novo session id, fora do grupo do harness) permaneceu vivo (bash + yt-dlp confirmados em sonda separada).

## Por quê
Missão assumida com entrega em janela futura (20h-22h) depende de um processo que atravessa o fim da ronda que o criou. O job do harness é filho da sessão: sessão morre, grupo morre, o "armado" vira só um script no disco. A janela da premiere não espera a próxima ronda do vigia — se a 72ª não tivesse relançado, a gravação teria nascido morta e a esteira de cortes (estreia ~23h) teria ficado sem matéria-prima, com o ZM/Ideias contando com o arquivo.

## Como aplicar
1. Na ABERTURA de toda ronda, antes de qualquer leitura de ponte: verificar processos/tarefas de longa duração que EU assumi (pgrep pelo nome do script/yt-dlp + tail do log + tamanho de arquivo parcial) — o "armado na ronda anterior" é hipótese, não fato.
2. Lançar sempre com `setsid nohup CMD >> log 2>&1 < /dev/null &` (destaca do grupo do harness) e registrar o PID.
3. Deixar prova viva no log (heartbeat com timestamp) para a ronda seguinte ler sem depender de memória.
4. Se o processo morreu e a janela ainda está aberta (ou o DVR permite --live-from-start puxar do início), relançar IMEDIATAMENTE — com DVR, restart baixa do início e alcança o ao-vivo (auto-cura de gap); registrar o relance no bloco da ronda (transparência com quem conta com a entrega).

Refs: DS-20260902-032 (assunção + armado 19:38) · DS-20260902-033 (relance 20:01/20:03) · ZM-20260902-RECORD-001 · gravador_live_jornal_20260902.sh (log gravacao.log).
