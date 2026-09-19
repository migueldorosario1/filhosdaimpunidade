# 401 na sonda ≠ prova de falha — a agulha subiu no slot (Gracindo 268740, ronda 06:00)

**O quê:** na ronda 05:30, a agulha GRACINDO 268740 (slot 05:37:51) foi dada como "NÃO SUBIU" porque o GET anônimo às 05:45 devolveu 401 — e a cadeia entrou em alerta de "possível 3ª cara do BUG-DS-098" (contenção = rodar o evento). Na ronda 06:00, o post estava PUBLISH com `date=2026-09-03T05:37:51` — exatamente o slot. O 401 era janela de propagação/leitura do REST (cache do proxy/CDN ou indexação do status ainda não refletida), não ausência de publicação.

**Por quê:** o GET anônimo prova "público PARA MIM agora" — e o "agora" tem latência própria quando o post acaba de mudar de status. Falha real do cron tem outras assinaturas (evento ainda na fila, status segue `future` horas depois, sem data de publish); 401 minutos após o slot é ambíguo: pode ser falha OU propagação. Na 05:30 eu tratei a ambiguidade como falha e alertei a cadeia — gastou atenção de CL/AGY/DS-Dell à toa.

**Como aplicar:**
1. Sonda de agulha com janela: para slot HH:MM, a 1ª sonda de confirmação não antes de HH+10~15min; se 401, re-sondar 2-3× com intervalo antes de declarar falha.
2. Prova de falha = estado persistente (status `future` + evento na fila + sem data de publish após 2 janelas), não um 401 isolado.
3. Se o alerta já foi dado e o post depois sobe no slot, registrar a RESOLUÇÃO na ronda seguinte (feito nesta 84ª: "401 era janela de propagação") — fecha o ciclo e evita que o falso alarme vire "recorrência fantasma" do bug.
4. Complementa a lição 20260903_restauro_nao_e_publish: sonda o POST (status real), mas respeita a latência de leitura do próprio status.

**Bônus da ronda (régua EMU-6):** ordem do Miguel (via ZCode/DSC, commit a84eed718) determinou que o bolo pronto da régua de título (EMU-1+2+6, `cerebro/Estilo/BLOCO_PRONTO_REGRA_TITULO_EMU6.md`) chega aos revisores DSN pelo CHEFE, colado VERBATIM — executado no canal_dsn_revisores.md + INDEC R1/R2. Lição de processo: retificação explícita com endereçamento (quem injeta onde) elimina paráfrase e ruído; Codex/Grok fora da corrente porque não participam da ponte.

— DS Nuvem Chefe (DS-N Chefe) · 20260903 06:0x BRT
