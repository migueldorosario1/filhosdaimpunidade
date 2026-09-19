# Lição 02/09/2026 — Gestor da grade: verificação por EVIDÊNCIA quando o cron cru é inacessível

**O quê:** Ordem do Miguel ~12:0x (DSC-039): grade de controle única de TODOS os agentes
(`cerebro/Foruns/GRADE_DE_CONTROLE_AGENTES.md`) + revisores em cadência calma 1x/hora
(R1 :05 · R2 :20) + regra-de-ouro (mudança de cadência = anúncio na ponte + atualização da
grade no MESMO commit; violação = D9) + **DS-N Chefe nomeado GESTOR da grade** (conferir a
grade contra o real a cada ronda B, atualizar última-ronda-viva/status, RELATÓRIO curto na
ponte, alertar DSN silencioso 2+ rondas). Na 1ª execução descobri que o arquivo cru do cron
(spool `/var/spool/cron/crontabs/ubuntu`) NÃO abre na minha sessão (permission denied) —
mas o controle funciona e é verificável por outras vias.

**Por quê:** O Miguel quer saber se o controle "está funcionando" — e a resposta honesta não
é "sim" genérico nem "não consigo ver nada": é mostrar O QUE dá para ver e COMO. O cron é a
intenção; a execução é a prova. Quem tem o acesso cru é o DSC (us65/root); o gestor confere
o efeito.

**Como aplicar (verificação por evidência, nesta ordem):**
1. **Processos**: `ps aux | grep` — ronda B sobe :00/:30 (ronda_dsn.sh), escuta.py viva (Loop A).
2. **systemd**: `systemctl status ds-nuvem-chefe-escuta` — Loop A ativo.
3. **Logs de ciclo**: `tail cron.log` de cada robô (dsn_revisor1/dsn_revisor2/ds_youtube/...) —
   timestamps dos ciclos conferem a cadência (R1 12:06 ≈ :05; R2 11:52; YT 11:07 ≈ :07).
4. **Canais na ponte**: vereditos/checks de R1/R2/Ideias/YouTube com hora — última ronda viva.
5. **Grade**: atualizar a linha do DSN (última ronda viva + status) e o log de mudanças.
6. Ciclo com "0 revisados por timeout de leitura" NÃO é falha do robô (fail-safe ok) — anotar
   a causa (rajada de latência do site) na grade, sem alarme.
7. Limitação honesta declarada na ponte: arquivo cru do cron não abre na sessão do gestor —
   leitura/edição direta é do DSC; grade + evidência = verdade; cron = consequência.
