# Lição 20260910 — a memória de estado do plantão não recebe o que a ronda escreve

- **Data/hora:** 10/09/2026 23:03 BRT · ronda 440a DS-N Chefe
- **O quê:** ao atualizar o estado da casa, medi que o arquivo lido pelo plantão do Loop A
  (`~/ds_nuvem_chefe/estado_casa.md`) estava com **mtime 04/09/2026 01:36** e conteúdo **"Hoje, 30/08"** —
  seis dias parado — enquanto a versão viva vivia no **SEED do repo** (`.tencent_v6_oficina/estado_casa_SEED.md`),
  que a ronda atualiza a cada 30 min. A escrita no arquivo do plantão é **negada** pelo sandbox da sessão
  (só escrevo em `~/cerebro-miguel`), e **não existe sincronizador** entre os dois.
- **Por quê:** `escuta.py` L19 (`ESTADO = f'{BASE}/estado_casa.md'`) e L96 (`_ler(ESTADO, 2500)`) — o consumidor
  lê um arquivo que nenhum processo escreve; o produtor (eu) escreve outro (o SEED). A barra da obra tem sync
  (`~/bin/sync_reforma_status.py`, SEED -> `v6_data`, */5); o estado da casa **não tem equivalente**.
- **Como aplicar:** (a) **todo artefato que eu escrevo tem de nomear quem o lê** e onde esse leitor o busca —
  escrever no lugar errado é o mesmo que não escrever; (b) quando a escrita na física do leitor for negada,
  registrar o **BUG com as duas opções de conserto** (cron espelhador SEED->vivo, no padrão do
  `sync_reforma_status.py`, ou o leitor aceitar o SEED com fallback) e **parar de reportar "atualizado" como se
  entregue**; (c) régua de aceite do conserto: mtime do arquivo do leitor **da ronda atual** e conteúdo citando
  o dia corrente.
- **Família:** "mecanismo que responde sem ter feito" (182 · 184 · 187 · 190 · 191 · 198 · 200 · 201 · 203 · 204 · 205)
  — aqui a variante é **do meu próprio rito**: eu cumpria a etapa (escrevia o SEED) e o resultado da etapa
  (o plantão saber o estado) não acontecia, e o registro dizia que sim.
- **Ref:** bloco DS-N-20260910-042 + ADENDO; `BUG-20260910-DSN-001` em `cerebro/CEREBRO_NODE_BUGS_ATIVOS.md`.
