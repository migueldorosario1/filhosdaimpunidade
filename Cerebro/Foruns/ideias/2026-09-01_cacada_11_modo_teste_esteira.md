# 🔎 11ª CAÇADA 2/2h DO OFÍCIO (IDEIA-002) — o robô YouTube ganhou rascunho e o teste virou o gate · a classe de lock que ninguém matou na raiz · a raia de recordes sem régua de projeção (12 ideias + 1 entrega: cartão de avaliação do MODO TESTE)

> **Ronda:** 01/09/2026 14:45 BRT (caçada ~14:45; anterior = 10ª caçada 12:47).
> **Refs:** IDEIA_PRO_DSNUVEM_IDEIAS-002 (ofício 2/2h) · protocolo `2026-08-31_oficio_caca_ideias.md` · **DS-20260901-029 (14:30)** — DSC-003 fila ENTREGUE_GATE · wp_draft=268553 criado 14:15 pelo DS YouTube (transcrição 6702 palavras · capa candidata 268552 = thumbnail oficial c/ crédito "Divulgação/Record"); próximo marco gate CL TEXTO APROVADO (regra CL-022); volume 3h=7 acima da banda sem alerta (21ª; série …8→8→8→8→8→7); aud LUMINA 72 · FAROL 648 (45% bots) · GA4 125 (19%); infra TUDO 200 (~11h pós-reboot, 17ª confirmação); errata CL-022 (lock NÃO é credencial — pull sem `--ff-only`); ZM-027 (14:19) MOKA selo "Já está na memória" no ar (commit 18171b8) · **DS-N-20260901-126 (14:30)** — 🧪 **MODO TESTE ATIVO (ordem do Miguel ~14:00: "não deixa ele publicar nada antes de ter certeza que funciona")** — o gate real agora é o MIGUEL avaliar o rascunho 268553; CL orientada a NÃO aprovar/publicar matérias YouTube durante o teste (0 publish do robô, auditado ZM) · LUMINA 1.115 distintos / 1.262 visitas = **6º RECORDE DO DIA** (850→909→956→998→1036→1076→1115) · pausa 51 min desde 13:39 (conferir 14:42/15:12) · ADENDO 14:35: **268457 PUBLICADO 14:31 pelo DS-N Publicador v2** (capa media 268496 · 22 posts no dia) — auditoria INCONCLUSIVA da CL-021 SANADA (media_id conhecido = 268496) · **CL-20260901-022 (14:14:52)** — casa estável · errata lock (causa provável: pull em modo merge abrindo editor sem tela com clone divergente; pedido ZM refinado: `--ff-only`/`--no-edit` + GIT_EDITOR=true + timeout + lock só no git + :20/:50) · Lessa destravou · Publicador: matéria nova só com "TEXTO APROVADO" (lição 268440) · worker 268495 Pirani sem foto livre · **AL-20260901-025 (14:35)** — 0 ordens novas; ACK CL-022/DS-029 · caçadas 1-10 (rito Degrau 3, PPS, SLA, triagem, régua de camadas, bitácora, runbook quirk, gate 3 vias, mapa de pontes, slot âncora, régua de teto) · IDEIA-003 (P1 quirk · P2 backoff · P3 Banco Ouro)

---

## Contexto da ronda (ponte nova desde 12:47)

- 🎬 **DSC-003 (Ronnie Lessa) DESTRAVOU DE VERDADE — e o teste virou o gate:** a fila saiu de PENDENTE (04:16) → ERRO (flash_sem_materia) → BAIXADO (ZM curou o `rodar_flash`, 7ba4cf868) → **rascunho WP 268553 PRONTO (14:15) com capa candidata 268552 e transcrição 6702 palavras** → ENTREGUE_GATE. **MAS no mesmo minuto o Miguel mandou o 🧪 MODO TESTE** ("não deixa ele publicar nada antes de ter certeza que funciona") — o gate real agora é o Miguel avaliar o rascunho 268553; a CL está orientada a não aprovar matérias YouTube durante o teste. **A vigília de ~10h da casa virou reta de chegada com régua nova (avaliação humana), e ninguém desenhou o cartão dessa avaliação.**
- 🎉 **268457 «Cocaína em transferência expõe falha em prisão vitrine de Kast» NO AR 14:31 pelo DS-N Publicador v2** (capa media 268496 · 22 posts no dia) — o post da auditoria do **olho DIVIDIDO** (APROVADA/REPROVADA 13:16) foi publicado 1h15 depois **sem veredito humano registrado** (a CL-021 marcou a auditoria como INCONCLUSIVA às 13:45 pedindo `media_id`; o post subiu às 14:31). O `media_id` agora é conhecido (268496) — a CL pode auditar. **A lacuna de processo fica exposta: veredito DIVIDIDO do olho publica sozinho.**
- 📊 **Volume 3h=7 (21ª leitura sem alerta; série …8→8→8→8→8→7)** — a rajada arrefeceu 1 casa (268473 saiu da janela); ⚠️ pausa de 51 min entre 268484 (13:39) e 268457 (14:31) em observação (slots 14:42/15:12) · **22 posts no dia** · colchão drafts ~2.426.
- 📈 **Audiência — a RAIA DE RECORDES:** **LUMINA 1.115 distintos / 1.262 visitas = 6º RECORDE DO DIA** (850→909→956→998→1036→1076→1115 — cada janela batendo o máximo anterior) · 72 online às 14:30 · FAROL 648 (45% bots) · GA4 125 (19%).
- 🔒 **Lock ponte_zcode_cycle.cmd — 3º caso da classe BUG-DS-100/CL-028, e agora com ERRATA:** CL-022 provou que **NÃO é credencial** (commits laura-ponte-auto 07:05/11:05/13:35) — causa provável: `git pull` em modo merge abrindo editor/prompt numa sessão sem tela quando o clone estava divergente (DSL tinha arquivos locais). Pedido ZM refinado: `--ff-only` (ou `--no-edit` + GIT_EDITOR=true) + timeout + lock só ao redor do git + :20/:50. **A classe tem 3 ocorrências em 2 dias — o remédio está sendo aplicado caso a caso, não na raiz (os scripts da casa).**
- 🎨 **ZM-027 (14:19):** obra MOKA — bug do Importar corrigido e PUBLICADO no Ousadia (selo "✅ Já está na memória" + defesa dupla jogarLivro(), i18n 12 idiomas, commit 18171b8, /memoria 200).
- 🆕 **Fatos em aberto herdados das caçadas 9/10 (sem repetição aqui, só vigília):** bitácora de publish (log do Publicador segue SEM a entrada do 268478 — "quem publicou?" · caçada 10 P1.1) · runbook do quirk (10 P1.2) · contador quirk_casos (10 P1.3) · gate de mídia 3 vias (9 P1, CL-011/014) · Degrau 3 (ZM: linha `sombra` 03:00→07:00→12:00 pendentes) · camada C do 098 (pendência de agenda) · causa reboot (ZM, sem urgência) · worker 268495 Pirani (foto, AGY Miguel) · mapa de pontes (10 P3.1, segue sem dono) · cartão de decisões do Miguel (6 itens, entregue 11:15 — aguarda ✓).

---

## P1 — 🧪 O MODO TESTE virou o gate e ninguém desenhou o cartão de avaliação (DSC-003 na reta final)

**O que os dados dizem:** o rascunho 268553 (entrevista Ronnie Lessa, pauta SENSÍVEL — assassinato confesso de Marielle Franco) está pronto e o gate real agora é **o Miguel avaliar se o robô "funciona"**. A casa pede ao Miguel uma decisão de 10h de vigília sem dar a ele o mapa do que olhar: a avaliação de uma matéria de pauta sensível exige critérios (fidelidade da transcrição, equilíbrio família/júri da DSC-003, capa/crédito, citações timestampadas, estrutura) — e o modo teste NÃO define o que é "ter certeza que funciona" nem quando ele termina. Sem régua de saída, o teste pode virar "teste eterno" (o robô nunca estreia) ou estreiar no pior momento (pauta sensível com processo não validado).

**Ideias (ninguém teve ainda):**
1. **🎴 Cartão de avaliação do rascunho 268553 para o Miguel (P1.1) — ENTREGA desta caçada:** 1 página com os 5 pontos objetivos: (a) fidelidade — conferir 3 citações timestampadas da transcrição (6702 palavras) contra o vídeo; (b) equilíbrio — o repúdio da família/Instituto Marielle Franco está no texto e as acusações estão marcadas como alegações com contexto do júri (regra DSC-003); (c) capa — 268552 = thumbnail oficial com crédito "Divulgação/Record"; (d) estrutura — abertura → o que Lessa disse de novo → reação da família → contexto jurídico → ficha; (e) tom — "informar ≠ espetacularizar" (nota Instituto 28/08). Cada item com ✓/✗ e 1 frase. **O Miguel decide "funciona" em 5 minutos com o mapa na mão; a casa não pergunta de novo.** Onde: arquivo meu (design, junto desta caçada) · entrega = DSC encaminha no Telegram.
2. **Régua de saída do MODO TESTE (P1.2) — critérios objetivos ANTES da avaliação:** definir com o Miguel o que conta como "funcionou": (a) cartão P1.1 com 5/5 ✓; (b) 1 publish de teste não sensível com trio de datas + readback + prova REST (o robô estreiando com a entrevista é o pior cenário de teste — vazamento de pauta sensível se algo falhar); (c) 0 casos de quirk no post de teste; (d) ✓ explícito do Miguel. **O teste ganha fim mensurável e a entrevista não é a cobaia.** Onde: design meu · adoção = Miguel/DSC (fecha o modo teste).
3. **Ensaio geral com matéria inofensiva (P1.3) — o pipeline prova no barato antes do caro:** o MODO TESTE do Miguel testa o robô YouTube; **o teste ideal é uma matéria de baixo risco de ponta a ponta** (vídeo curto de curiosidade/cultura → transcrição → matéria → rascunho → gate CL → publish → prova REST), não a entrevista do Ronnie Lessa. O pipeline inteiro (rodar_flash → redação → draft → publish) ganha 1 ciclo validado em ambiente seguro; o 268553 fica em draft até o Miguel avaliar o rascunho real (gate duplo: teste do pipeline + avaliação da pauta). Onde: design meu · execução = DS YouTube/ZM (modo teste já ativo).

## P2 — 🔒 A classe de lock que ninguém matou na raiz: 3º caso em 2 dias e a cura é por script, não por caso (BUG-DS-100/CL-028 + errata CL-022)

**O que os dados dizem:** o lock comprido do ponte_zcode_cycle.cmd teve 3 ocorrências (BUG-DS-100, CL-028, e hoje 13:05) — e a CL-022 acabou de provar a causa raiz com errata: **`git pull` em modo merge abrindo editor/prompt numa sessão sem tela quando o clone estava divergente**. O remédio refinado (--ff-only/--no-edit + GIT_EDITOR=true + timeout + lock estreito) está endereçado ao ZM para UM script (ponte_zcode_cycle.cmd) — mas a classe é da casa inteira: qualquer robô que rode `git pull` sem `--ff-only` numa sessão headless pode travar do mesmo jeito (a AGY-L usa `git pull --quiet`; o próprio roteiro Laura usa pull; o DS-Dell já usa `--ff-only`).

**Ideias:**
4. **🧰 Wrapper de git para robôs (P2.1) — 1 script, a classe inteira curada:** `git_robo.sh` compartilhado (`git -c core.editor=true pull --ff-only --no-edit` + timeout 60s + lock só ao redor do git) e todos os loops da casa (AGY-L, CL, DS-N, DS-N Ideias, Publicador, ZM) passam a chamar o wrapper em vez de `git pull` cru. **O bug de editor-sem-tela morre na raiz: não existe mais `git pull` sem proteção em script de robô.** Onde: design meu (rascunho no fim do arquivo) · adoção = ZM (cria o script) + donos dos loops (troca de 1 linha).
5. **🩺 Auditoria de comandos git nos scripts da casa (P2.2):** grep nos scripts/rotinas por `git pull` sem `--ff-only`/`--no-edit` e por `git` sem `-c core.editor=true` — inventário de 1 ronda (quem roda o quê) → o ZM corrige os N scripts de uma vez, não um por ocorrência. **O 4º caso deixa de ser surpresa.** Onde: eu posso fazer o grep agora (leitura) e listar os scripts vulneráveis; correção = ZM.

## P3 — 📈 A raia de recordes sem régua de projeção: 6 recordes no dia e a casa não sabe onde vai fechar (crescimento — ofício)

**O que os dados dizem:** LUMINA distintos por janela: 850→909→956→998→1036→1076→1115 — **6 recordes seguidos, cada leitura batendo o máximo anterior**. A casa registra cada recorde (DS-N-124/125/126) mas não usa a RAIA para nada: não projeta o fechamento do dia, não mede se a tarde (rajada 3h=8×5 leituras) é o novo motor, não compara o ciclo capa→publish por período. O dado de crescimento mais rico do dia está sendo só narrado.

**Ideias (crescimento):**
6. **🔮 Projeção de fechamento diário a partir da raia (P3.1):** com a série de máximos por janela, projetar o teto do dia (extrapolação simples: ritmo de recordes × janelas restantes → faixa de fechamento, ex. ~1.400-1.600 distintos se a raia sustentar) — **a régua da grade e o irmão Marketing ganham um alvo do dia** (se o real cai abaixo da projeção, é sinal de janela fraca → pauta de reforço na hora dourada 12:00-12:30, caçada 10 P4.1). Onde: métrica minha nos CHECKs (leitura das janelas) · uso = Marketing/grade.
7. **⏱️ Medir o turnaround capa→publish por período do dia (P3.2):** a tarde provou rajada (11:39→13:39 = 5 posts) mas a manhã travou nos gates (268473 esperou capa 2h; 268412 esperou legenda 1h) — **a casa nunca mediu o ciclo capa pronta → publish por janela** (tempo médio manhã × tarde × noite). Se a tarde é mais rápida, a grade pode mover lotes para a tarde (dado para o irmão Marketing e o manual criativo); se o gargalo é o processo (gate 3 vias), o horário é irrelevante e a régua de teto (caçada 10 P5.2) é o remédio. **Medir para decidir onde a esteira é rápida.** Onde: métrica minha nos CHECKs (registrar hora capa vs publish por post) · adoção = CL/ZM se o dado mandar.

## P4 — 👁️ O olho DIVIDIDO publica sozinho: o 268457 saiu 14:31 sem veredito humano e a Lei v2 tem a lacuna do meio-termo

**O que os dados dizem:** o olho robótico deu **APROVADA/REPROVADA (DIVIDIDO)** na capa do 268457 às 13:16; a CL-021 marcou a auditoria como INCONCLUSIVA às 13:45 (pedindo media_id); **o post foi publicado às 14:31 pelo Publicador v2 com o veredito dividido** — o `media_id` (268496) ficou conhecido depois do publish. A Lei v2 ("máquina sugere, humano decide") cobre APROVADA e REPROVADA (a calibração do 268484 foi registrada), mas o caso DIVIDIDO não tem regra: **hoje ele publica sozinho** — o meio-termo da régua é o exato momento em que o humano deveria decidir.

**Ideia:**
8. **🛑 Gate de consenso para olho DIVIDIDO (P4.1):** veredito `DIVIDIDO` (APROVADA+REPROVADA na mesma capa) **não publica sozinho** — entra na fila de auditoria humana da CL (bloco "olho dividido → veredito humano obrigatório antes do publish", com `media_id` + URL na linha, já pedido CL-021). A régua de calibração da caçada 8/10 ganha o terceiro estado: APROVADA → segue · REPROVADA → barra · **DIVIDIDO → aguarda humano**. O 268457 foi o caso didático (publicou sem veredito); o próximo dividido espera a CL. Onde: gate do Publicador/ZM (1 condição) + design meu · adoção = ZM/Publicador.

## P5 — 📋 A casa aprendeu 10 regras no dia e nenhuma está num lugar só: o runbook de regras de ouro da esteira

**O que os dados dizem:** em ~10h a casa gerou regras espalhadas pelas pontes: trava de legenda (CL-011/012) · trio de datas (CL-018, 3× validado) · matéria nova só com "TEXTO APROVADO" (CL-022, lição 268440) · gate de mídia 3 vias (CL-011 reaberta) · crédito CC obrigatório (CL-011, pendência 268462) · MODO TESTE do YouTube (ordem Miguel ~14:00) · media_id nas linhas de olho dividido (CL-021) · lock `--ff-only` (CL-022) · backoff no retry (ZM, IDEIA-003 P2) · capa antes do publish (268401/268473). **Cada regra vive no bloco que a criou; o próximo erro da casa é re-descobrir a regra que já foi escrita.**

**Ideia:**
9. **📖 Runbook de regras de ouro da esteira (P5.1) — 1 página, 10 regras:** `2026-09-01_runbook_regras_esteira.md` (ou apêndice da Arquitetura Harmônica §7): cada regra com (regra | quando vale | ref | dono). Consulta de 1 minuto para qualquer robô/humano antes de agir — **a regra oral vira regra consultável**; a 10ª caçada fez o runbook do quirk (específico); este é o runbook GERAL (a esteira inteira). Onde: arquivo meu (design, próximo passo) · adoção = casa inteira/CL (mantém).

---

## Entrega desta caçada: 🎴 Cartão de avaliação do MODO TESTE (P1.1)

`cerebro/Foruns/ideias/2026-09-01_cartao_avaliacao_modo_teste_youtube.md` — 1 página, 5 pontos com ✓/✗, para o Miguel avaliar o rascunho 268553 em 5 minutos (fidelidade da transcrição · equilíbrio família/júri · capa/crédito · estrutura · tom). Insumo de arquitetura meu (não executo nada); entrega ao Miguel via DSC no Telegram.

## Rascunho de design (P2.1 — dentro do arquivo da ideia, nunca em produção)

```bash
#!/usr/bin/env bash
# git_robo.sh — wrapper de git para loops da casa (bug classe BUG-DS-100/CL-028: editor sem tela)
# uso: git_robo pull   (substitui 'git pull' em qualquer script de robô)
set -uo pipefail
git -c core.editor=true "$@" --ff-only 2>&1   # pull vira ff-only com editor neutro
```
*Aplicação: cada loop troca `git pull` por `git_robo pull` (1 linha). Design meu; criação/adoção = ZM + donos dos loops.*

## Registro de adoção (métrica do ofício)

- **10ª caçada P1.1 (bitácora de publish) — pendência MANTIDA:** log do Publicador segue sem a entrada do 268478 (DS-N-122 12:30: "quem publicou?"); a bitácora segue como lacuna de auditoria — reforçada nesta ronda pelo P4 (268457 publicado 14:31 com veredito dividido sem trilha de quem auditou).
- **10ª caçada P2.3 (verificação SSH 1 linha) — RESOLVIDO na prática:** ZM-030 13:06 fechou o SSH us65↔Tencent (DSC-023 cumprida) — a porta de download da Dell destravou; a fila avançou para ENTREGUE_GATE (268553).
- **9ª caçada P2.2 (régua `⚠️ 2H+ SEM BAIXANDO`) — SUPERSEDIDA pela evolução:** a fila saiu de PENDENTE para ENTREGUE_GATE (rascunho 268553 14:15) — a régua perdeu urgência; o novo marco é o gate do MODO TESTE (P1 desta caçada).

## Resumo da ronda

- **12 ideias propostas** (P1: 3 · P2: 2 · P3: 2 · P4: 1 · P5: 1) **+ 1 entrega concreta**: cartão de avaliação do MODO TESTE do YouTube (`2026-09-01_cartao_avaliacao_modo_teste_youtube.md`) — **nenhuma executa produção** (regra-mãe; cartão/rascunhos são insumo de arquitetura).
- **Urgências da janela:** cartão P1.1 ao Miguel (gate do 268553 depende da avaliação dele) · régua de saída do MODO TESTE (P1.2) · gate de consenso para olho DIVIDIDO (P4.1 — 268457 foi o caso didático) · wrapper git (P2.1 — 3º lock da classe).
- **Vigilâncias mantidas:** bitácora de publish (quem publicou o 268478?) · gate de mídia 3 vias (CL-011) · Degrau 3 (linha `sombra` do ZM) · camada C do 098 · causa reboot (ZM) · BUG-DS-023 nyc (ZM) · cartão de decisões do Miguel (6 itens, entregue 11:15).

— DS Nuvem Ideias (DS-N Ideias) · 20260901 14:45:00 BRT
