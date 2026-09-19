# Agulha perdida em silêncio: pacote dado a executor que parou (269085/cl153 — 05/09 00:00)

## O quê
O 269085 («"Ciro não está comigo", diz Lula em Juazeiro do Norte», texto humano §132, prioridade) foi agendado pelo pacote cl153 (ordem CL-20260904-039: AGY roda 23:35, `entra 23:48:00`). Na ronda 00:00/167º, o post seguia RASCUNHO (prova wp-cli no us65: post_status draft, post_date 22:41, sem evento cron). A causa não foi o WP nem o cron: o EXECUTOR (AGY-LAURA) tinha parado — último registro AL-628 (22:38); as rondas 23:05 e 23:35 dele nunca rodaram, o `/tmp/cl153.sh` nunca foi executado e nenhum commit dele existe entre 22:38 e 00:00. O dia 04/09 fechou em 60 posts (topo 269077 bosque 23:08) — a agulha das 23:48 foi perdida SEM barulho: o future nunca chegou a existir no WP, então nenhuma sonda de "evento due/cron" teria disparado.

## Por quê
A vigília clássica (BUG-DS-098) sonda o WP: post em `future` + evento na fila → espera o disparo. Esse padrão cobre falha do CRON, não falha do EXECUTOR QUE AGENDA. Quando o robô que recebe a ordem (AGY, ronda :05/:35) cai entre a ordem da CL (23:14) e a execução (23:35), o pacote morre ANTES de virar `future` — o WP nunca soube da agulha. A fila de produção da casa depende da cadeia CL → AGY → WP; um elo mudo = furo silencioso de agulha (o leitor só percebe se reparar no horário).

## Como aplicar
1. Vigia de agulhas: não conferir só o estado WP — conferir a SAÚDE DO EXECUTOR: ledger/estado do AGY (ou do robô dono da ronda) deve avançar a cada ciclo; 2 rondas seguidas sem registro (AL-629/630 ausentes) = executor provavelmente parado, alertar a CL ANTES da agulha.
2. Quando um pacote com slot (cl1XX "entra HH:MM") for dado a um executor e o executor não registrar a execução, subir o alerta na ponte no mesmo ciclo — o dono do pacote (CL) re-emite ou deputiza (padrão cl147 do 157º).
3. Executor substituto: o Chefe cobre contenção SÓ com o pacote já revisado pela CL e SÓ agendando (nunca publicando direto — regra do dono 23:00/23:27: quem publica é a CL ou o Miguel). Script do pacote mora na máquina do dono (/tmp); reconstruir do DESCRITIVO (CL-039 seção 3) quando não houver deputização explícita — e registrar a reconstrução com md5 + stdout, como no cl147.
4. Fecho de dia: a ronda 00:12 da CL é o ponto de verificação do "fechou tudo?" — o Chefe deve deixar o achado no bloco da ponte com prova (wp-cli) para ela agir em segundos.

## Verificação
269085 draft confirmado 00:02 (wp-cli us65) e 401 no REST público (não publicado). AGY: ledger termina AL-628 22:38; estado/agy_laura.md parado na ronda 22:35; zero commits 22:38→00:00 (git log --all). Sem evento `publish_future_post` na fila do cron (wp cron event list 00:02). Acompanhamento: CL ronda 00:12 → re-emissão do cl153 (ela tem o script) ou Chefe contém ~00:30.
