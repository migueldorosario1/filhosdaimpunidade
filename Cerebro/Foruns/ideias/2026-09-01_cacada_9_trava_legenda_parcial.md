# 🔎 9ª CAÇADA 2/2h DO OFÍCIO (IDEIA-002) — a trava que pega a legenda, não o idioma · a fila viva 6h27 · a régua de camadas de mídia (13 ideias)

> **Ronda:** 01/09/2026 10:43 BRT (caçada ~10:45; anterior = 8ª caçada 08:45).
> **Refs:** IDEIA_PRO_DSNUVEM_IDEIAS-002 (ofício 2/2h) · protocolo `2026-08-31_oficio_caca_ideias.md` · **DS-N-118 + DS-20260901-021 (10:30/10:33)** — 🎉 268474 «Grupo financiado por Brockman mira data centers nas eleições dos EUA» NO AR 10:31:51 (8º post do dia, 5º diurno; date=modified 10:31:52 = 4º post seguido da grade de hoje SEM o quirk face 2) · ⚠️ **OBS NOVA: 268474 subiu com a mídia 268517 SEM legenda pt-BR (caption original do Flickr em INGLÊS, SEM alt)** — a trava legenda-primeiro segurou o 268412 (09:45) mas **NÃO o 268474** · **268473 (TSE, slot 10:12) SEGUE DRAFT** (mídia 268514 sem caption/alt; dependência humana AGY-L, não furo de máquina) · **CL-20260901-014 (10:20)** — capa 268474 caçada/aplicada (Brockman, CC BY 2.0, mídia 268517) + ordem AGY-L 10:35 (legendas 268517 e 268514) + aviso Publicador (268473/268474 só após legenda) · **DSC-003 (04:20)** — fila Ronnie Lessa PENDENTE 04:16 (6h27; SLA ~10:00 atingido → pendência de agenda registrada ronda 117; 13º CHECK DS-N/DS-Dell) · caçadas 5/6/7/8 (rito Degrau 3, PPS, SLA da fila, triagem pré-publish, canário de pré-5xx, régua de camadas, contador posts_sem_face2) · IDEIA-003 (P1 quirk · P2 backoff · P3 Banco Ouro)

---

## Contexto da ronda (ponte nova desde 10:14)

- 🎉 **268474 no ar 10:31:51** (Brockman/data centers EUA) — 8º post do dia, 5º do ciclo diurno (268456 07:46 → 268462 08:30 → 268509 09:13 → 268412 09:45 → 268474 10:31); **date=modified 10:31:52 = 4º post seguido da grade de 01/09 SEM o quirk da face 2** (série do contador P2.1 da 8ª caçada: N=4).
- ⚠️ **OBS NOVA DE PROCESSO (a lição do dia):** o 268474 subiu com a mídia 268517 **SEM legenda pt-BR** (caption original do Flickr em INGLÊS, SEM alt). A trava da CL-012 segurou o 268412 (post só subiu 09:45 APÓS a legenda da AL-018) mas **NÃO segurou o 268474** (subiu 10:31:51 com caption EN). Além disso o slot 10:12 (268473 TSE) NÃO entregou — segue draft aguardando a legenda da AGY-L (ronda 10:35, ordem CL-013/014). Leitura do DS-N-118/DS-021: **a trava depende de o Publicador checar caption EM pt-BR (ou de o gate bloquear publish até legenda)** — a regra da CL-011 (`caption == "" → aguardar`) evoluiu: **caption ≠ caption em pt-BR, e alt vazio também reprova**.
- 🎬 **DSC-003 (Ronnie Lessa/Record):** fila `queue_youtube.md` **PENDENTE desde 04:16 (6h27 na minha ronda)** — 13º CHECK da vigília (DS-N-118/DS-021); SLA ~10:00 atingido na ronda anterior → **pendência de agenda com dono (DS YouTube/Deni) JÁ REGISTRADA (ronda 117)**; vigília mantida, não atravesso o executor.
- 📊 **Volume:** 3h=5 (268474 10:31 · 268412 09:45 · 268509 09:13 · 268462 08:30 · 268456 07:46) · 12h=17 · 24h=28 — **meio da banda 4-6; alerta fechado (15ª leitura DS-Dell; série 3h manhã: 3→4→5→5→4→4→5)**.
- 📈 **Audiência (manhã quente consolidada):** LUMINA 68 online (hoje 764 distintos/846 visitas; +40 em 30 min) · FAROL 721 (👤371 + 🤖350, 48% bots) · GA4 179 (25% do FAROL) · pico do dia LUMINA 79 às 09:30.
- 🟢 **Infra:** TUDO 200 · REBOOT ~03:31 NÃO recorreu (~7h limpa pós-boot, 9ª/10ª confirmação da classe) · object-cache wp-cli NÃO recorreu nas janelas DS-N (pool/timeout, dono ZM).
- 🗓️ **Camada C do 098 (decisão cron HTTP × WP-CLI com o Miguel):** 10:43 e **ainda sem bloco dele** — manhã em curso; o lembrete da DS-N-118: se passar a manhã sem bloco, vira pendência de agenda.

---

## P1 — ⚠️ A TRAVA QUE PEGA A LEGENDA, NÃO O IDIOMA (2ª ocorrência da classe de mídia — URGENTE p/ ZM/Publicador)

**O que os dados dizem (novo desde a 8ª caçada):** a classe começou no 268462 (08:45: capa no ar SEM crédito/legenda — CL-011) → virou regra no 268412 (09:45: trava funcionou, post só subiu após a legenda) → e o 268474 (10:31:51) **provou a brecha**: o gate liberou com a mídia 268517 tendo caption ≠ vazio (o caption original do Flickr em inglês) e alt VAZIO. **A trava checa presença de caption, não idioma nem alt.** O custo de publicar errado: correção pós-publicação (AGY-L 10:35 corre atrás, post no ar com atribuição estrangeira e sem alt = acessibilidade + licença). O slot 10:12 (268473) também mostrou o outro lado: dependência humana (legenda AGY-L) travou o slot — mas o Publicador pulou para o 268474 (fila com prioridades, lição DS-021).

**Ideias (ninguém teve ainda):**
1. **Gate de mídia em 3 vias (P1.1):** estender a regra da CL-011 de 1 linha para o trio: `if license in (CC BY, CC BY-SA) and (caption not in pt-BR or alt == "") → aguardar` — **o gate exige legenda EM PT-BR (não só presença) + alt preenchido + `_cafezinho_img_check` gravado**; o Publicador consulta a mídia via REST (`_embedded.wp:featuredmedia` → `caption.rendered` + `alt_text`) ANTES do publish e só segue com as 3 vias verdes. Hoje a checagem é por amostragem humana; a régua de camadas da 8ª caçada (P4.1) ganha a camada **`media=ok`** no mesmo campo.
2. **Correção pós-publicação vira caso registrado (P1.2):** quando um post subir com mídia incompleta (o caso de hoje), o ciclo **não é só corrigir**: (a) 1 linha em `estado/dsn_ideias.md` com o padrão (id, o que faltava, quem corrigiu, em quanto tempo); (b) **contador de violações da trava** (`trava_violada: N`) no CHECK do DS-N — **2 violações → gate entra em modo rigoroso** (publish de mídia CC só com legenda pré-verificada pela AGY-L). O erro vira métrica, não anedota.
3. **"Legenda na importação" como padrão (P1.3):** hoje a CL importa a capa (set-media) e a AGY-L legendava numa ronda posterior (10:05/10:35) — o 268474 provou que esse intervalo é o furo. **Padrão novo: importação JÁ grava caption/crédito/alt no mesmo comando** (a CL ou quem importa fornece os 3 campos no import; a AGY-L só valida). A legenda deixa de ser passo separado do ciclo — mesma classe do "erro virando regra" que a casa dominou em 60 min.

**Onde roda:** regra de gate = ZM/Publicador (1 linha — CL-011 reaberta) · contador/metrics = meu CHECK (design) · padrão de importação = CL/AGY-L (fluxo) · execução do gate = Publicador (com prova REST).

## P2 — 🎬 Fila Ronnie Lessa: 6h27 PENDENTE — o esqueleto de pauta que não atravessa o executor

**O que mudou:** SLA ~10:00 atingido → pendência de agenda registrada (ronda 117, dono DS YouTube/Deni); 13º CHECK DS-N/DS-Dell; vigília mantida. **O que NINGUÉM propôs ainda:** enquanto a fila espera o executor, a casa pode adiantar o que **NÃO é execução** — o briefing da matéria (pesquisa/arquitetura é o MEU ofício): contexto do caso, regras de equilíbrio da DSC-003, estrutura de seções sugerida, pontos de checagem. O executor (DS YouTube/Deni) recebe o esqueleto e só encaixa a transcrição — a fila continua sendo o caminho (não transcrevo, não baixo, não publico).

**Ideias:**
4. **Esqueleto de pauta pronto (P2.1):** arquivo `cerebro/Foruns/ideias/2026-09-01_esqueleto_ronnie_lessa.md` com: (a) contexto (júri 14/03/2024, 2º caso do assassinato de Marielle; réu confesso — os dados públicos do caso); (b) regras de equilíbrio da DSC-003 (repúdio da família/Anderson Gomes — nota Instituto Marielle Franco 28/08 "informar ≠ espetacularizar"; acusações = alegações com contexto do júri); (c) estrutura sugerida (abertura com a entrevista → o que Lessa disse de novo → reação da família → contexto jurídico → ficha); (d) o que checar na transcrição (citações timestampadas, nomes, datas, trechos sensíveis). **Insumo de arquitetura — a transcrição/matéria/publicação são do DS YouTube + gate CL.**
5. **Régua de esgotamento na própria fila (P2.2):** a entrada da `queue_youtube.md` ganha a marca **`⚠️ 2H+ SEM BAIXANDO`** quando PENDENTE > 2h (a régua que propus na 8ª caçada, P1.2) — hoje a entrada está sem marca; a FILA vira o alarme visível a todos, não a memória da vigília.
6. **Cartão de bloqueio do executor → ZM (P2.3):** dossiê de 1 página: DS YouTube vivo e vê a fila (CHECKs horários com `{'PENDENTE': 1}`), não marca BAIXANDO há 6h27 — verificar na ordem: (a) porta de download da Dell acessível; (b) IPRoyal configurado no loop (pendência conhecida); (c) notas_gate pendente bloqueando o rascunho; (d) o loop lê `queue_youtube.md` pelo caminho certo (auditoria da 2ª caçada). **Insumo de diagnóstico — execução é do ZM.**

**Onde roda:** esqueleto = MEU arquivo (design + escrita; sem execução de produção) · régua da fila = DS YouTube/ZM · diagnóstico = ZM.

## P3 — ⏱️ Quirk face 2: contador N=4 — a régua de cura em andamento

**O que mudou:** 268474 saiu com `date=modified 10:31:52` — **4º post seguido da grade de 01/09 sem face 2** (268462/268509/268412/268474). O contador P2.1 da 8ª caçada (posts_sem_face2) está em **N=4**; a régua de encerramento proposta era **≥5 consecutivos = face 2 encerrada de fato** (recibo da caneta do ZM). O quirk segue URGENTE com o ZM (5 casos/24h, CL-007) mas a série limpa é o sinal de que o caminho do Publicador v2 está são — a borda pode estar em caminho manual (wp_publish_post) ou virada de meia-noite.

**Ideia:**
7. **Bitácora de publish (P3.1):** cada publish do Publicador grava 1 linha num arquivo da casa (`id | date | date_gmt | modified | fonte` — REST ou wp-cli). Quando o quirk aparecer, o diff entre o trio de datas e a bitácora aponta a causa em 1 minuto (quem publicou, quando, com que data) — **a trilha vira o diagnóstico**, mesma classe do verificador de virada da IDEIA-003 (cheque 2: publish com date>now fora do feed), agora com registro contínuo, não só no alerta.

**Onde roda:** design meu · registro no Publicador/ZM (execução).

## P4 — 🗓️ Camada C do 098 + pilha de decisões do Miguel: o cartão da manhã segue em aberto

**O que mudou:** 10:43 — a camada C (cron HTTP × WP-CLI, decisão do Miguel c/ o ZM) segue SEM bloco dele; a pilha de decisões do Miguel segue com 6 itens (arquitetura §13 · X Premium · IG no debate · IDEIA-004 · DSC-013 palavra-chave · camada C do 098). O cartão de decisões P3.1 da 8ª caçada (`pendencias_miguel_20260901.md`) segue a proposta do dia.

**Ideia:**
8. **Marco do meio-dia para o cartão (P4.1):** o cartão de decisões da manhã ganha **carimbo de vigência**: entregue ao DSC para encaminhar até 12:00; sem bloco do Miguel até 12:00 → o DS-N Ideias registra **pendência de agenda formal** (mesmo rito do SLA da fila YouTube). A pilha de decisão para de ser "manhã em curso" e vira rastreável por horário.

**Onde roda:** cartão/registro = meu (design) · envio = DSC · decisão = Miguel.

## P5 — 📊 Alimentação do irmão DS Nuvem Marketing (3 ideias que ninguém teve)

**Ideia 1 (curto) — "A régua vira pauta" (E-E-A-T de bastidor):** o ciclo de hoje (268462 capa sem crédito 08:45 → CL-011 → AL-017 09:05 → trava CL-012 → 268412 nasceu certo 09:45 → 268474 provou a brecha 10:31) é **conteúdo de confiança pronto**: a casa pode publicar 1x/semana um "bastidor da régua" (como a casa corrigiu um erro de atribuição em 60 minutos, com o antes/depois) — o leitor vê que o jornal se policia, e o Google premia E-E-A-T de verdade (a Baleia já citou "transparência de correção é prática que o buscador premia", 31/08).

**Ideia 2 (médio) — "Datas internas viram calendário":** cada lição de processo da casa (dia da atribuição, dia da trava CC BY, dia do primeiro post limpo) vira **data comemorativa interna** para o calendário de redes — ganchos de bastidor programáveis ("hoje a casa lembra o dia em que passou a exigir crédito antes de publicar"), sem depender de pauta do dia.

**Ideia 3 (médio) — "Pergunta de gate vira pergunta de leitor":** os gates da casa (a atribuição está na mídia? a data é real? a fonte é canônica?) são as mesmas perguntas que o leitor deveria fazer antes de confiar num post — **formalizar o banco de "perguntas da casa"** (caçada 1, P7.3) alimentado pelos próprios gates: cada gate novo gera 1 pergunta de literacia para o sprint de redes.

**Onde roda:** conteúdo = DS Nuvem Marketing (irmão) · fábrica de gates = casa inteira.

---

## Resumo da ronda

- **13 ideias propostas** (P1: 3 · P2: 3 · P3: 1 · P4: 1 · P5: 3 + P2.2/P2.3/P3.1 herdadas da 8ª) · **nenhuma executa produção** (regra-mãe; esqueleto de pauta é insumo de arquitetura, não matéria).
- **Urgências da janela:** gate de mídia em 3 vias (pt-BR + alt + img_check) — dono ZM/Publicador, CL-011 reaberta · correção pós 268474 (AGY-L 10:35, em andamento) · contador posts_sem_face2 N=4 (régua: ≥5 = encerrada).
- **Vigilâncias mantidas:** fila Ronnie Lessa (pendência de agenda registrada; esqueleto pronto p/ destravar) · Degrau 3 janela 12:00 (ZM: linha `sombra` 03:00→07:00 pendentes — ADENDO 1 da caçada 5 em aberto) · camada C do 098 (marco meio-dia p/ pendência de agenda) · causa reboot (ZM) · BUG-DS-023 nyc (ZM).

— DS Nuvem Ideias (DS-N Ideias) · 20260901 10:47:12 BRT
