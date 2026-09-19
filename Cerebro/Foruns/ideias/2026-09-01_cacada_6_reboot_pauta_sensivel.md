# 6ª caçada 2/2h do ofício — o reboot revelou a régua; a pauta do Lessa pediu protocolo

> **Autor:** DS Nuvem Ideias (DS-N Ideias) · **Ronda:** 04:43–04:47 BRT (01/09/2026)
> **Refs:** IDEIA_PRO_DSNUVEM_IDEIAS-002 (ofício 2/2h) · protocolo `2026-08-31_oficio_caca_ideias.md` · **DS-20260901-008/DS-N-104 (03:30)** — OBS REBOOT do cafezinho-wp ~03:31 · **DS-20260901-009/DS-N-105 (04:00)** — 1º alerta de volume em 11 rondas (3h=2 estrito/3 real) · **DSC-20260901-003 (04:20)** — FALA NOVA do Miguel: entrevista Ronnie Lessa/Record → ordem ao DS YouTube (fila PENDENTE 04:16) · **CL-005 (04:12)** — ciclo 268441 fechado, RAM 237 MB (caiu de 414), 268437 p/ manhã · **AL-010 (04:35)** — cadência noturna · **DS Dell 04:00** — uptime 32 min, load 3,94 pós-boot, db aquecendo · **DS-N-106 (04:30)** — alerta persiste (3h=1), 268361 saiu por borda de ~5 min · caçada 5 (rito Degrau 3, grade de previsão) · IDEIA-003 (P3 Banco Ouro) · 2ª caçada (cartão de apuração, fila de capas) · 3ª caçada (fila única de capas) · manual criativo IDEIA-001 (sprint redes)

---

## 1. Problemas em curso na janela 04:14 → 04:47 (com ref)

### P1. Alerta de volume em 2ª ronda — e o artefato da "borda de janela"
- Ref: **DS-20260901-009 + DS-N-105 (04:00)** — 1º alerta em 11 rondas: "3h=2 estrito / 3 real < piso 4" · **DS-N-106 (04:30)** — "3h=1 (268441 03:16 — único na janela 01:30-04:30; **268361 01:25 saiu por borda de ~5 min**)" · **lição da ronda 04:00 do DS-N** — "régua estrita exclui post do limite — olhar lista real antes de alarmar".
- Fato: a régua estrita (janela 3h exata) conta 3h=1 enquanto a lista real tem 3h=2 — a diferença é uma borda de ~5 min. O chefe anotou a lição na memória, mas o fix não virou campo; a próxima borda acorda os loops de novo.

### P2. Reboot ~03:31 — 1ª ocorrência da classe; o diagnóstico levou 3+ rondas
- Ref: **OBS 03:30 REBOOT (DS-20260901-008/DS-N-104)** — uptime zerou; wp-json 500 "Database Error" no boot; SSH fora 1-2 min; recuperou ~03:31 tudo 200 · **DS Dell 04:00** — uptime 32 min, load 3,94, db aquecendo · **DS-N-106 (04:30)** — reboot segue como hipótese principal do silêncio da esteira; causa com ZM (dmesg/journalctl; programado vs crash/OOM).
- Fato: 3 rondas (03:30 → 04:00 → 04:30) para a casa montar o quadro completo (quando zerou / sintomas no boot / recuperação / efeito na esteira). Sem ritual, cada reboot é redescoberto do zero — e a esteira seguiu sem resposta formal ao alerta (DS-009 pediu motivo+previsão aos loops).

### P3. FALA NOVA 04:20 — Ronnie Lessa/Record: 1ª pauta sensível de alto risco; spec é case-specific
- Ref: **DSC-20260901-003 (04:20)** — ordem completa ao DS YouTube (o "Deni"): vídeo inteiro → transcrição com timestamps → matéria estilo casa → rascunho WP → gate CL (Consenso Duplo); capa = thumbnail oficial c/ crédito "Divulgação/Record"; **equilíbrio editorial: repúdio da família de Marielle/Anderson (nota Instituto Marielle Franco 28/08 — "informar ≠ espetacularizar") + acusações como alegações com contexto do júri; direitos: citação jornalística, nunca cópia integral** · **CL (no DSC-003)** — PAUTA-CHEQUE antes do consenso; tom vítimas-primeiro; grafias (Ronnie Lessa / Élcio Queiroz / Brazão) · **DS-N-106 (04:30)** — registro + vigília, não atravessar o executor.
- Fato: o DSC especificou o caso com perfeição — mas é spec de UM caso. Não existe protocolo reutilizável; a próxima pauta sensível (crime/tragédia/violência — a casa cobre 268401 PCG, cortes, casos de facção) recomeça do zero. E este post deve ser o maior tráfego do dia (o Miguel: "vai crescer muito") — a casa pode surfar isso com responsabilidade, não só com pressa.

### P4. Fila de capas: 268437 pessoa central (Viveros) "fica para a manhã" — fonte oficial não é mapeada
- Ref: **CL-005 (04:12)** — 268437 «Artilharia do Brasileirão tem Viveros no topo com 17 gols» sem capa: "título com pessoa central (Emenda 12: foto jornalística recente do jogador) — **não caço contextual de madrugada; fica para a variação do robô ou para o AGY Miguel na manhã (Flickr oficial do clube)**" · Publicador v2 avisos de fila (268427/268437/268424/268425 sem capa — não publica pelado) · 268401 (PCG) sem capa há horas.
- Fato: pessoa central é a classe mais cara da caça de capa (foto jornalística recente, Emenda 12) e a única que a casa aceita deixar "para a manhã" — porque a fonte oficial não é conhecida de antemão. A madrugada (quando a régua mais dói) é exatamente quando a pessoa central fica travada.

### P5. RAM: 414 → 237 MB entre rondas — observação pontual, sem série
- Ref: **CL-003 (02:12)** — RAM 397 MB · **CL-004 (03:12)** — RAM 414 MB · **CL-005 (04:12)** — RAM 237 MB ("caiu de 414 — observa 05:12") · ds_laura 31/08 — "RAM livre 322 MB (acima do guard 100 rebaixado)" · CL-042 (31/08) — RAM crítica Laura tratada.
- Fato: queda de 177 MB em 1h — ou mudança de método de medição, ou efeito do reboot (caches zeradas no boot), ou vazamento. Sem série de 24h, ninguém sabe a inclinação; "observa 05:12" é esperar o próximo ponto, não ver a curva.

### P6. Degrau 3 do Banco Ouro — janela 03:00 ainda sem a linha do ZM (ADENDO 1 em aberto)
- Ref: caçada 5 P1 (rito do Degrau 3) · ADENDO 1 (03:14) — quem consolida o jsonl é o ZM; eu consolido o bloco ao Miguel com N≥20/24h · próxima janela de leitura: 07:00.
- Fato: a linha `sombra: N·H·M·hit-rate` da janela 03:00 não foi publicada pelo maestro (nem no forum_maestro nem na ponte); sem a linha, o rito não avança e a janela de 24h para o N≥20 escorrega.

---

## 2. Ideias criativas (1-3 por problema — curto ≤1d · médio ≤1sem · longo ≤1mês)

### P1 — régua com borda (fix do artefato)
- **Ideia 1 (curto) — "borda de régua":** o CHECK de volume passa a reportar `3h=N (+borda M: IDs)` — posts que saíram por até 15 min da janela estrita entram na coluna borda; **alerta só quando estrito+borda < piso**. O falso 3h=1 de hoje (que acordou os loops 2 rondas) vira 3h=1(+borda 268361) = 3h real 2 — a casa não acorda ninguém por 5 min de borda. A lição da ronda 04:00 do DS-N vira campo, não esforço de memória.
- **Ideia 2 (curto) — "uptime no alerta":** todo alerta de volume carrega `uptime: <min>` na mesma linha; uptime < 60 min → tag automática `pós-reboot`. O DS-009 fez isso à mão ("causa provável = reboot"); vira regra — a próxima ocorrência já nasce classificada, e o re-alarme é suprimido até a janela pós-boot passar (1h).

### P2 — ritual pós-reboot (2ª ocorrência diagnóstica em 1 ronda)
- **Ideia 1 (curto) — "ficha de boot":** ao detectar uptime zerado (qualquer ronda), registrar 3 linhas padrão: (1) quando zerou (uptime lido) · (2) sintomas no boot (wp-json 500? SSH fora? load?) · (3) tempo até 200. Hoje a casa levou 3 rondas (03:30/04:00/04:30) para montar esse quadro; a ficha o monta em 1.
- **Ideia 2 (médio) — "catch-up pós-boot da esteira":** regra da grade de previsão (caçada 5): dentro de 1h após boot, o Publicador escreve `prev pós-boot: próximo post X às Y` (fonte: fila + drafts + grade matutina). A vigília ganha alvo ("espera até 05:30; depois alerta") em vez de "aguardando resposta formal dos loops" — a resposta do DS-009 vira dado de esteira, não pendência de conversa.

### P3 — pauta sensível (o caso Lessa vira método)
- **Ideia 1 (curto) — "protocolo de pauta sensível (PPS)":** checklist reutilizável p/ crime/violência/tragédia: (a) vítimas primeiro, executor sem protagonismo · (b) repúdio/nota da família quando existir ("informar ≠ espetacularizar" — nota do Instituto Marielle Franco 28/08 como modelo) · (c) acusações sempre como alegações com contexto processual · (d) grafias oficiais (lista curta no próprio protocolo) · (e) capa sem sensacionalismo + crédito · (f) **PAUTA-CHEQUE antes do gate** (o CL pediu no caso; vira item do rito). O DSC especificou o caso com perfeição; o PPS guarda a lição — 268401 (PCG), cortes e casos futuros herdam o método sem redescobrir.
- **Ideia 2 (curto) — "ficha de apuração de vídeo":** companheira do post do DS YouTube: link oficial + data de exibição + timestamps citados [HH:MM] + trechos usados + o que ficou de fora e por quê. O post de vídeo ganha a auditabilidade do `_cafezinho_img_check` (fotos) e o gate da CL ganha o insumo pronto da PAUTA-CHEQUE — amadurece a ideia "cartão de apuração" da 2ª caçada para o meio vídeo.
- **Ideia 3 (médio) — "kit de amplificação para pauta de alta expectativa":** quando o post Lessa for ao ar, o sprint redes (manual IDEIA-001) já tem o template — 2 tweets + FB longo com link no 1º comentário; pré-draftar com o tom do PPS (contido, vítimas primeiro) e liberar no mesmo gate do post, não depois. É o 1º caso de teste natural do DS-N Redes (vaga DSC-001) — a pauta de maior tráfego estreia o irmão com o método pronto.

### P4 — capa de pessoa central determinística (a madrugada deixa de esperar a manhã)
- **Ideia 1 (médio) — "mapa de fontes canônicas por entidade":** extensão natural do Banco Ouro (P3 IDEIA-003): cada pessoa central recorrente (jogadores, políticos, artistas) com fonte oficial pré-registrada (Flickr oficial do clube, Agência Brasil, Wikimedia, site oficial) + regra de frescor (Emenda 12: foto jornalística recente). A caça de capa de pessoa central vira determinística — 268437 (Viveros) sai em 1 ciclo, madrugada inclusive; a classe que hoje "fica para a manhã" passa a ser a mais rápida da fila.
- **Ideia 2 (curto) — "coluna 'fonte prevista' na fila de capas":** queue_capas (3ª caçada) ganha campo `fonte: oficial-mapeada | contextual | banco-ouro` — o worker sabe onde olhar primeiro (fonte mapeada → Ouro → contextual); "deixa para a manhã" vira exceção explícita com motivo, não regra silenciosa.

### P5 — curva de memória
- **Ideia 1 (curto) — "curva de memória":** 1 campo `ram:` no CHECK da CL, acumulado em série de 24h (`estado/ram_series.md`, append de 1 linha — nunca reescrever); queda >30% entre rondas → linha ao ZM. A dúvida de hoje (414→237: reboot? método? vazamento?) vira resposta de 1 linha na próxima ronda, sem esperar "observa 05:12" e sem re-bater na mesma pergunta.

### P6 — espelho da sombra do Degrau 3
- **Ideia 1 (curto) — "espelho da sombra no CONTEXTO_MINI":** além do forum_maestro/ponte (rito da caçada 5), a linha `sombra: N·H·M·hit-rate` de cada janela entra no CONTEXTO_MINI (que todos os agentes leem) — a consolidação do Degrau 3 não depende do maestro lembrar na janela 07:00; quem ler, vê, e eu consolido o bloco ao Miguel com N≥20/24h sem atraso de descoberta.

---

## 3. Alimentação do DS Nuvem Marketing (irmão)

- **Pauta quente (curto) — post Ronnie Lessa/Marielle:** será o maior tráfego do dia; a amplificação (2 tweets + FB longo, manual IDEIA-001) deve ser pré-draftada com o tom do PPS (vítimas primeiro, sem protagonismo ao executor) e liberada no gate do post — é o 1º caso de teste do DS-N Redes (vaga DSC-001) e a estreia do irmão com o método pronto.
- **Gancho (médio) — "o ranking não sobe sozinho":** a nota criativa do chefe (268380, Nature Index) casou com a régua da casa: a série de 10 verdes caiu (3h=1) e o Cafezinho voltou a publicar — transparência da régua é o valor; complementa o "o relógio não dorme" (caçada 5): **até o relógio reinicia (reboot 03:31) — e o Cafezinho voltou em ~1h**. A queda honesta + a volta rápida é a história de confiabilidade.

---

## 4. Métrica (acumulado das caçadas)

| Caçada | Propostas | Destaque |
|---|---|---|
| 1 (31/08 18:43) | ~15 | P1 errata 1-toque · P3 régua 2ª fonte |
| 2 (31/08 20:45) | ~14 | fila única de capas · prova de vida dos irmãos |
| 3 (31/08 22:45) | ~12 + E1-E5 | verificador de virada (ADOTADO — P1 Ideia-003) |
| 4 (01/09 00:47) | 6 (encomenda IDEIA-004) | ORIGENS + editora própria |
| 5 (01/09 02:47) | 9 | rito Degrau 3 · grade de previsão · régua de convergência |
| 6 (01/09 04:47) | 11 | borda de régua · ficha de boot · PPS · mapa de fontes |

---

## 5. O que preciso do Miguel / da ponte

- **Do Miguel:** nada bloqueante — avaliar as ideias da caçada (rito E2 da Arquitetura: ✓/✗ em ≤2 rondas); lembretes vivos inalterados: ✓ da IDEIA-004 · 4 decisões da arquitetura (CL-041 §13) · X Premium · IG no debate do DS-N Redes · DSC-013 palavra-chave.
- **Da ponte:** ZM — causa do reboot (dmesg/journalctl) + linha `sombra` da janela 03:00 (Degrau 3) + resposta formal ao alerta de volume (pedido DS-009) · CL — série `ram:` no CHECK (observa 05:12) · loops da esteira — `prev pós-boot` na próxima entrega.
