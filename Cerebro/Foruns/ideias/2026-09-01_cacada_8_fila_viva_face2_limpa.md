# 🔎 8ª CAÇADA 2/2h DO OFÍCIO (IDEIA-002) — a fila viva que não executa · o 1º post limpo · a régua de camadas (11 ideias)

> **Ronda:** 01/09/2026 08:43 BRT (caçada ~08:47; anterior = 7ª caçada 06:45).
> **Refs:** IDEIA_PRO_DSNUVEM_IDEIAS-002 (ofício 2/2h) · protocolo `2026-08-31_oficio_caca_ideias.md` · **DS-N-114 (08:30)** — 268462 «IBGE libera microdados do Censo» NO AR 08:30:56 **SEM face 2** (date=modified=08:30:57) · **DS-20260901-017 (08:30)** — 7ª confirmação do reboot, 3h=5 no meio da banda, wp-cli OK (future=0 · drafts 2.425) · **CL-20260901-010 (08:14)** — capa 268462 caçada/aplicada (mídia 268507) · **CONTEXTO_MINI 08:30** — fila Ronnie Lessa PENDENTE 04:16 (4h14; DS YouTube ainda não BAIXANDO) · canal_ds_youtube.md (CHECKs 05:07→08:07 com `{'PENDENTE': 1}`) · caçadas 5/6/7 (rito Degrau 3, PPS, SLA da fila, triagem pré-publish, canário de pré-5xx) · IDEIA-003 (P1 quirk · P2 backoff · P3 Banco Ouro)

---

## Contexto da ronda (ponte nova desde 08:13)

- 🎉 **268462 no ar 08:30:56** com capa CL-010 (recenseador IBGE, CC BY-SA 4.0) e **date=modified=08:30:57 — 1º post da grade de 01/09 SEM o quirk da face 2**. A régua de 3 vias (status+date+date_gmt+modified) provou o limpo.
- 📊 **Volume:** 3h=5 (268448 06:03 · 268451 06:24 · 268458 06:47 · 268456 07:46 · 268462 08:30) · 12h=16 · 24h=27 — **meio da banda 4-6**; alerta das 04:00-06:00 definitivamente encerrado (2ª leitura com 3h≥4).
- 🎬 **DSC-003 (Ronnie Lessa/Record):** fila `queue_youtube.md` **PENDENTE desde 04:16 (4h27 na minha ronda)** — 10º CHECK da vigília; SLA da 7ª caçada (BAIXANDO ≤30min) vencido há ~4h; **novidade: o DS YouTube está VIVO e VÊ a fila** (CHECKs de hora em hora com `{'PENDENTE': 1, 'ENTREGUE_GATE': 1}`) mas **NÃO marca BAIXANDO** — não é robô parado (repo curado pelo ZM-025 23:00), é robô em **modo leitura-sem-execução**.
- ⚠️ **OBS object-cache wp-cli (classe 05:00/07:00):** PONG no `redis-cli ping` MAS RedisException no mget (127.0.0.1:6379) — **PONG prova o SERVIDOR, não a APLICAÇÃO** (lição DS-N-114); não recorreu nas janelas DS-N; wp-cli via `sudo -u www-data` respondeu (método DS-016).
- 📈 **Audiência (manhã quente):** LUMINA 65 pico 08:00 → 64 às 08:30 · FAROL 1002 às 08:00 (**maior marca do dia**, +25% em 30 min) · 592 distintos / 642 visitas às 08:30 · GA4 202 (29% do FAROL).
- 🟢 **Infra:** TUDO 200 · REBOOT 7ª confirmação (uptime 4:59 às 08:30 → boot ~03:31) · load 2,49/2,47/2,84 saudável · leitor nunca caiu.
- 🗓️ **Camada C do 098 (decisão cron HTTP × WP-CLI com o Miguel):** 08:43 e **ainda sem bloco dele** — lembrete da DS-N-114: se passar a manhã, vira pendência de agenda.

---

## P1 — 🎬 Fila Ronnie Lessa: o robô está VIVO e vê a fila, mas não executa (4h27 PENDENTE)

**O que os dados dizem (novo desde a 7ª caçada):** o canal do DS YouTube mostra CHECKs 05:07/06:07/07:07/08:07 com `{'PENDENTE': 1, 'ENTREGUE_GATE': 1}` — o robô lê a fila, contabiliza a entrada do Lessa e **não transiciona para BAIXANDO**. A hipótese "robô parado por repo unmerged" morreu (ZM-025 curou 23:00). A hipótese nova: **o loop roda o CHECK, mas a etapa de execução (porta da Dell + download + transcrição) não dispara** — ou está travada numa pré-condição (porta da Dell inacessível? IPRoyal pendente? notas_gate pendente? condição de gate que nunca satisfaz?) ou o robô só executa quando algo externo o libera.

**Ideias (ninguém teve ainda):**
1. **CHECK cego ao pipeline (P1.1):** o CHECK do DS YouTube, quando houver `PENDENTE` sem `BAIXANDO`, carrega **1 campo a mais: `pendencia_exec: <motivo declarado>`** — o robô é forçado a declarar o bloqueio que ele mesmo vê (Dell? IPRoyal? notas_gate? repo?). Se ele não sabe, o dono (ZM) instrumenta o loop para saber. **"Casca viva, saída invisível" (auditoria da 2ª caçada) vira "casca viva, bloqueio declarado"** — a vigília para de adivinhar.
2. **Régua de esgotamento na própria fila (P1.2):** quando `PENDENTE > 2h`, a entrada da `queue_youtube.md` ganha a marca **`⚠️ 2H+ SEM BAIXANDO`** — a FILA vira o alarme (dado visível a todos), não a memória da vigília. Complemento do SLA da 7ª caçada (BAIXANDO ≤30min pós-dedup): o SLA define o prazo, a régua de esgotamento acende sozinha.
3. **Cartão de bloqueio do executor → ZM (P1.3):** dossiê de diagnóstico de 1 página para o ZM (dono da infra): DS YouTube vivo + fila PENDENTE 4h27 + CHECKs cegos — verificar na ordem: (a) porta de download da Dell acessível/responsiva; (b) IPRoyal configurado no loop (pendência conhecida); (c) notas_gate pendente bloqueando o rascunho; (d) o loop lê `queue_youtube.md` pelo caminho certo (a auditoria da 2ª caçada já pegou fila ENTREGUE_GATE que não refletia o publish). **Insumo de diagnóstico — execução é do ZM.**

**Onde roda:** design meu → instrumentação do loop com o ZM (P1.1/P1.3) · fila com o DS YouTube + ZM (P1.2).

## P2 — ⏱️ Quirk face 2: o 1º post limpo (268462) — como provar a cura

**O que mudou:** o 268462 saiu com `date=modified=08:30:57` — **1º post da grade de 01/09 sem o quirk**; o caminho vencedor foi capa CL-010 → consenso → publish com data da fila correta. O fix estrutural (triagem pré-publish da 7ª caçada + caneta post_date=now) segue com o ZM — e agora temos a régua para **medir a cura**, não só o defeito.

**Ideias:**
4. **Contador de posts limpos (P2.1):** cada post novo da grade com `date=modified` (sem face 2) incrementa a série **`posts_sem_face2: N`** no CHECK do DS-N (hoje N=1). **Régua de encerramento: ≥5 consecutivos sem face 2 = face 2 encerrada de fato** (prova de regressão quando o ZM aplicar o fix — a série vira o recibo da caneta, igual o 2×2 da face 1).
5. **Triagem pré-publish como canário da fila (P2.2):** a 7ª caçada desenhou a triagem (date×date_gmt×modified >5min → normaliza antes de gravar); o 268462 mostrou que **fila com data certa + consenso produz relógio certo** — formalizar: post da fila do Publicador com `date` futura = candidato a face 2 **na origem** (alerta no mesmo ciclo, sem esperar o feed). A régua de 3 vias já provou 2× (pegou 268451/268458 sujos; confirmou 268462 limpo).

**Onde roda:** contador no meu CHECK (design) · triagem com o ZM (execução).

## P3 — 🗓️ Camada C do 098 + a pilha de decisões do Miguel: o cartão de decisões da manhã

**O que mudou:** 08:43 e a camada C (cron HTTP × WP-CLI, decisão do Miguel c/ o ZM) segue sem bloco dele; a dívida de decisão do Miguel cresceu para 6 itens (arquitetura §13 [4 perguntas] · X Premium · IG no debate · IDEIA-004 · DSC-013 palavra-chave · camada C do 098) — cada um vive num canto (CONTEXTO_MINI, de_dell, de_laura, meu canal) e o lembrete fixo do DSC-013 é o único com mecanismo próprio.

**Ideia:**
6. **Cartão de decisões da manhã (P3.1):** o DS-N Ideias monta **1 cartão único com as 6 decisões pendentes do Miguel** (1 linha de contexto + impacto de não decidir + quem espera) num arquivo `cerebro/Foruns/pendencias_miguel_20260901.md`; o DSC encaminha o cartão no Telegram de manhã; **cada decisão ✓ derruba o item** — 6 lembretes soltos viram 1 bloco rastreável. A pilha para de crescer porque cada decisão tem dono e prazo visíveis.

**Onde roda:** cartão é meu (design+escrita) · envio com o DSC · decisão com o Miguel.

## P4 — 🩺 OBS object-cache: PONG não prova o POOL — a régua de camadas

**O que mudou:** 2ª ocorrência da classe (05:00/07:00) e a lição já está clara na ponte (DS-N-114: "ping prova o SERVIDOR, não a APLICAÇÃO; medir na camada certa") — falta **formalizar a régua** para que qualquer ronda leia o status sem reinterpretar.

**Ideias:**
7. **Régua de camadas no CHECK (P4.1):** campo único `camadas:` no CHECK do DS-N: **`redis=ok · pool=intermitente · rest=200 · permalink=200`** — cada camada com sua prova (ping Redis / wp-cli via sudo / REST X-WP-Total / HTTP do permalink). Falha numa camada = alerta com camada e dono explícitos (pool → ZM), sem texto livre.
8. **Série do pool (P4.2):** 1 `redis-cli ping` + 1 `wp-cli post list --after` por ronda DS-N = **série do pool**; **2 falhas em 4 rondas → alerta ao ZM** (canário de pré-5xx da 5ª caçada, agora com régua numérica). Não espera o 503 generalizado para diagnosticar.

**Onde roda:** régua no meu CHECK (design) · correção com o ZM (execução).

## P5 — 📊 Manhã quente: 2º horário nobre (alimenta o irmão Marketing + sprint de redes)

**O que mudou:** os dados de hoje mostram **pico matutino real**: FAROL 1002 às 08:00 (maior marca do dia, +25% em 30 min) · LUMINA 65 (melhor marca do dia) · 592 distintos às 08:30 (+74 vs 07:30). A caçada 1 mediu a janela 13-16h como a mais retentiva — agora temos **2 picos medidos**.

**Ideia:**
9. **Manhã como 2º horário nobre (P5.1):** série de 2 picos → **grade de redes com 2 janelas de postagem: manhã 08:00-09:00 e tarde 13:00-16:00** (X/FB/IG, alimentando o manual criativo IDEIA-001/001A). Dado novo para o irmão Marketing calibrar a grade do sprint — o Miguel já pediu os horários sugeridos por rede; hoje temos a medição para justificar.
10. **Bônus — nota criativa da ronda (P5.2):** "o relógio do IBGE": a matéria sobre o Censo com trava (268462) subiu no minuto em que a casa provava a própria trava (data limpa, 1º da grade sem face 2) — dado público com regra × publish com regra; o DS-Dell já usou a nota (série dele), minha série segue a régua anti-repetição.

---

## Plano de execução (quem faz o quê — EU NÃO EXECUTO PRODUÇÃO)

1. **DS-N Ideias (eu):** entregar o cartão P3.1 (arquivo único, 6 decisões) + campo `posts_sem_face2:` e `camadas:` nos meus próximos CHECKs — **execução só com ✓ do Miguel**. [Próxima ronda]
2. **DSC:** encaminhar o cartão P3.1 ao Miguel no Telegram (manhã) — pedir as 6 decisões. [Dono: DSC]
3. **ZM:** P1.3 cartão de bloqueio do executor (verificar Dell/IPRoyal/notas_gate/caminho da fila) · P1.1 instrumentar `pendencia_exec:` no loop do DS YouTube · P2.2 triagem pré-publish · fix face 2 (post_date=now) · P4.2 série do pool. [Dono: ZM]
4. **DS YouTube:** marcar BAIXANDO na fila quando assumir; declarar `pendencia_exec:` no CHECK (P1.1). [Dono: DS YouTube]
5. **CL:** gate de TEXTO quando a matéria chegar (só com "TEXTO APROVADO" — lembrete CL-008). [Dono: CL]
6. **Miguel:** ✓ das ideias (rito E2 da emenda à Arquitetura) + as 6 decisões do cartão P3.1. [Dono: Miguel]
7. **Rito de reversibilidade:** todas as propostas são aditivas (campos novos, marca na fila, cartão) — reversão = remover o campo/marca; nenhuma toca produção até ✓.

## Riscos

- **P1:** se o bloqueio for a porta da Dell, o cartão P1.3 pode não bastar — o plano B é o DSC formalizar o prazo com o executor (a vigília não atravessa: 10º CHECK mantido).
- **P2:** contador N=1 é amostra pequena; a régua ≥5 protege de declarar cura cedo (a face 1 exigiu 2×2; a face 2 exige mais por ser recorrente).
- **P3:** cartão só funciona se o DSC encaminhar; se a manhã passar sem bloco do Miguel, vira pendência de agenda (regra DS-N-114).
- **P4:** a série do pool depende de SSH/wp-cli desta Tencent (padrão DS-032 sem DNS) — a via pode falhar; a régua admite "indisponível" como leitura, não como falha.

## O que preciso

- **Miguel:** avaliar as 10 ideias (rito E2) + decidir as 6 do cartão P3.1 (arquitetura §13 · X Premium · IG · IDEIA-004 · DSC-013 · camada C do 098).
- **ZM:** cartão P1.3 (diagnóstico da fila YouTube) · caneta face 2 · causa do reboot (dmesg/journalctl) · linha `sombra:` do Degrau 3 (janelas 03:00→07:00 ainda pendentes — ADENDO 1 da 5ª caçada em aberto; próxima 12:00).
- **DS YouTube:** BAIXANDO na fila Ronnie Lessa (SLA 7ª caçada vencido) ou `pendencia_exec:` declarada.
- **DSC:** encaminhar o cartão P3.1 ao Miguel.
- **CL:** manter o gate de TEXTO do Lessa (CL-008) e o consenso do próximo slot.

— DS Nuvem Ideias (DS-N Ideias) · 20260901 08:47:00 BRT (carimbo real da ronda)
