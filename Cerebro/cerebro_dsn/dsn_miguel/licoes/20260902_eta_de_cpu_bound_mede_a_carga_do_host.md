# ETA de CPU-bound mede a carga do host no momento — 2026-09-02

## O quê
A transcrição whisper da TV GGN (trilha A, ZM-006) teve 3 ETAs diferentes na mesma noite:
DS-037 (22:15) prometeu ~22h35-40 ("base ~22-25min"); a medição real com o host ocupado
(carga 14,6/12 núcleos) deu 4% em 5min → ETA real ~00h15-00h30 (adendo DS-038-A, 22:43);
com a carga já caída para 3,7 (23:03, downloads da noite terminados), o relance deve fechar
em ~25-30min. O mesmo comando, o mesmo modelo, o mesmo áudio — três respostas diferentes
porque a fila do host mudou entre as medições. E o job morreu 2x com a sessão (DS-037 e
DS-038) — a 6ª confirmação do padrão job-morre-com-a-sessão (lição DS-032); só o relance com
`setsid nohup` (23:03) fica vivo.

## Por quê
Whisper/ffmpeg são CPU-bound: a velocidade real é (capacidade do host) − (carga dos outros
jobs). A calibração "base = ~25min p/ 54min de áudio" foi feita com a máquina livre; na
prática da casa, o Dell roda downloads, transcrições e a esteira ao mesmo tempo, e ETA
prometido sem medir `uptime`/loadavg é calendário de mentira: quem espera o SRT (o ZM, com
publish na agulha) planeja em cima do número, e o número errado corrói a confiança.

## Como aplicar
1. Antes de prometer ETA de CPU-bound, rodar `uptime` e comparar loadavg com nproc — se a
   carga ≥ núcleos, multiplicar o ETA calibrado por 3-5x (ou avisar que o host está ocupado).
2. Quando o ETA medido divergir do prometido, avisar o dono na ponte IMEDIATAMENTE (o
   adendo DS-038-A fez isso em ~20min) com as opções — nunca deixar o dono descobrir sozinho.
3. Lançar jobs longos com `setsid nohup … < /dev/null &` (padrão sobrevivente comprovado) e
   verificar por artefato (log crescendo), não por pgrep (o sandbox isola o namespace de PID).
4. Registrar o loadavg no mesmo log do job para a próxima calibração ter a régua de contexto.

Refs: DS-20260902-037/038/038-A/039 · lição 20260902_job_background_morre_com_a_sessao_relance_na_abertura.md
