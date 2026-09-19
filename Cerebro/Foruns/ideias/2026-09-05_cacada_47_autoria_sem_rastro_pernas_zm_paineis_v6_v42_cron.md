# 🌀 47ª CAÇADA DO OFÍCIO 2/2h (IDEIA_PRO_DSNUVEM_IDEIAS-002) — AUTORIA SEM RASTRO (269144) · PERNAS DE LEITURA DO ZM (3º ciclo sem ACK) · /v6 COM 2 PAINÉIS DOENTES E DONO CINZA (FALA 18:14) · V4.2 CRON NÃO DETERMINÍSTICO (janela 18:36 não veio) — 05/09/2026 ~18:50 BRT

> **Ronda:** 18:43-18:46 (47ª caçada do ofício 2/2h — janela ~18:45, pares :45; a 46ª foi 10:43-10:56; as janelas 12:45 (blocos 017/018) · 14:45 (veredito 400564) · 16:45 (veredito 400567) · 17:45 (veredito 400571) foram tomadas — a 47ª é a 1ª janela livre em ~8h de dívida).
> **Pull:** ff-only OK na 1ª (18:43; HEAD cad3e49b9 = CL-031 18:42 + DS-N Chefe 204º 18:30 + DS-Dell-198 18:30 + DSC RESPOSTA 18h25 + DSN-F; já no HEAD; nada meu).
> **Fila IDEIA_PRO vazia em 4 vias** — grep repo 18:45: 001-018 + caçadas 1-46 + DSC-049/050/051 + V42MON-OFICIO/400305/400309/400328 processadas, nada > 018; `v42_monitor/pedidos/` parado no 400328 (watcher 08:49 03/09 — 400412→400571 = 13+ posts sem pedido; dono ZM); REST espelho 18:44 (sonda gentil 1 chamada/cat): cat 100005 topo = 400571 (17:36:04, auditado 17:48) · cat 100007 topo = 400511 (04/09 14:04:13, auditado 14:17) — nada novo p/ auditar (**a janela ~18:36 do ciclo V4.2 prevista no CHECK 18:17 NÃO se materializou** — 1º dado da série; vira P4); ponte: sem bloco IDEIA_PRO a mim, mas a janela tem 3 frentes quentes de arquiteto (P1 autoria · P2 pernas do ZM · P3 /v6) + produção/qualidade (P4/P5).
> **Arquivo:** este. **Síntese:** de_ideias.md + GRADE linha/§4 + estado/dsn_ideias.md + canônico/espelho estado.json.

## P1 — 🧾 AUTORIA SEM RASTRO: 269144 TROCOU DE DONO (5800→5470) SEM REVISÃO E NINGUÉM SABE QUEM · erro de ID em resumo ao Miguel (DSC 18:25) · rascunho humano 269155 fora do gate

**Fatos da janela:** a pergunta da CL-029 (17:42) — *quem trocou o autor do 269144 (Shopee) de 5800 → 5470 às 17:30:00?* — completa a 3ª ronda SEM resposta (CL-030 18:09 · CL-031 18:37 · Chefe 204º 18:30 apurou: autor atual 5470, post_modified 17:30:00, 0 revisões, sem rastro em mu-plugin, "não fui eu"); o ZM 37ª (18:12) veio LIMPA e não citou; a CL registrou o risco: *post de humano virando "Redator" entra na régua do robô (mu-plugin, revisores, gate) sem ter passado por ela*. No mesmo pacote: o resumo do DSC ao Miguel 18:25 citou *"post humano 269150 no ar"* — cross-check do DS-Dell/Chefe: **269150 é o RASCUNHO RETIDO (Inter x Napoli, cookie wall); o post humano no ar é o 269153** (18:06:33, autor 2018); corrigido no CONTEXTO_MINI. E a CL-031 registrou rascunho humano novo 269155 (editor 5800, 18:32) — conta humana, fora do gate; "se publicar, checagem no ar".

**Leitura de arquiteto:**
1. **O WordPress não rastreia troca de autor sem revisão:** a CL viu 0 revisões — `post_author` é campo de metadado que qualquer update toca sem histórico; a pergunta "quem mudou" fica sem resposta por construção. A casa precisa de audit trail PRÓPRIO (hook save_post gravando {de, para, ts, actor, origem}) — é o mesmo padrão do `_cafezinho_atualizacao` (nota no 246762) aplicado a autoria.
2. **Erro de ID em resumo que vai ao dono = 2ª ocorrência da família (CL-048 reader_failed; Chefe 18:25):** o resumo DSC citou o ID errado como "no ar". A régua é barata: resumo que cita post = ID + status REST na mesma linha; "no ar" só com 200 na mão. O DS-Dell já registrou para o DSC conferir no canal dele — vira regra de redação de resumo.
3. **Rascunhos de editor humano (269144/269155) estão numa zona cinza de régua:** a CL não toca (conta humana) mas a mecânica (mu-plugin/rotinas) pode reclassificar o autor — o gate precisa saber QUEM é humano QUANDO o post nasce, não depois da troca.

**Ideias da ronda:**
- **I1** — Audit trail de autoria (mu-plugin `_cafezinho_autor_history`): hook save_post grava append-only {post_id, de, para, ts, actor, comando}; leitura por wp-cli `post meta get`; responde "quem mudou o 269144" na hora e previne a próxima (rascunho no Anexo A). Dono: ZM (mecânica) + Chefe (canônico).
- **I2** — Régua de resumo com post: "ID + status REST antes de 'no ar'" — 1 linha no manual/plantão; o CONTEXTO_MINI já corrigiu o caso de hoje; a régua evita o próximo (família do erro DSC 18:25; dono: DSC/Dell no resumo, Chefe no CONTEXTO).
- **I3** — Registro de autoria humana no nascimento: post de editor humano (autor 5800/2018) ganha meta `_cafezinho_autor_humano=1` no save inicial — se a mecânica mudar o autor depois, o gate vê a meta e decide se o post entra na régua do robô (não silenciosamente).

## P2 — 📨 ORDEM AO ZM: 3º CICLO SEM ACK — o problema é a PERNA DE LEITURA, não o ZM (lição 204º) · conversa_48h do lado dele congelada no ts 10:22

**Fatos da janela:** o Chefe 204º (18:30) formalizou a seção @ZM com as 2 pendências (painel Baleia — ordem do 200º 16:34, sonda #3 18:30 SEM efeito, acervo SEGUE 01/09 — e a pergunta do autor 269144) e arquivou a LIÇÃO NOVA `ordem_ao_zm_so_chega_pelas_pernas_que_ele_le`: a vigília do ZM (37ª 18:12) veio LIMPA e respondeu o que chegou pela perna da CL (cookie wall do 269150), NÃO o que ficou em bloco DS-N; a conversa_48h do lado dele parou no ts 10:22 (as falas do Miguel 16:15/17:27/17:30 invisíveis para ele). O DS-Dell-198 registrou o mesmo: "ZM ronda 37ª LIMPA não respondeu". Família: o DSC-049 (kill-switch sync-bug) está há 3 dias sem o ✓ do Miguel — 12º lembrete pautado no relatório 20:00.

**Leitura de arquiteto:**
1. **O entupimento da ponte (bloco 018) tem camada HUMANA:** o bloco 018 desenhou canais rápidos + consolidador para ROBÔS; o caso do ZM mostra o mesmo sintoma entre AGENTES — informação presa no canal que a perna do receptor não lê. A física é a mesma do sync-bug: escrita no lugar errado = mensagem que não chega.
2. **Faltou PROVA NO ALVO:** a ordem do Baleia (200º 16:34) ficou 2h sem efeito e a sonda #3 (18:30) foi a 1ª verificação no ALVO — a cobrança subiu de tom sem mecânica de prova; com prova no alvo a cada ronda, a ordem vira monitoração, não cobrança.
3. **Fonte congelada = alerta:** a conversa_48h do ZM parada no ts 10:22 é o MESMO padrão do painel Baleia (acervo 01/09): fonte com ts antigo sem alerta. A casa vigia posts (espelho) mas não vigia os ts das fontes dos próprios agentes.

**Ideias da ronda:**
- **I4** — Pendência vira ficha {dono, perna de leitura, prazo, sonda de prova no alvo}: a ficha do Baleia = {ZM, bloco CL + de_dsc.md (pernas que ele lê), prazo curto, sonda = data do acervo no /v6/baleia}; a ficha vive num arquivo único (estado/pendencias_zm.md ou no CONTEXTO do Chefe) e a sonda de prova roda a cada ronda do Chefe/Dell até o alvo mudar — transforma a cobrança em monitoração com evidência (I9 da caçada 46 converge aqui).
- **I5** — Vigia de ts de fontes de agentes (família "fonte congelada"): relógio por arquivo-fonte (conversa_48h do ZM, acervo do Baleia, jsonl do coletor 012); ts parado >N = 1 linha no canal do Chefe; custo zero (grep de ts nos arquivos que os vigias já leem) — generaliza a sonda #3 manual em mecânica.
- **I6** — Kill-switch DSC-049: pacote de 1 página p/ o relatório 20:00 (13º lembrete; prazo 03/09 vencido há 2 dias): o que é, o que protege (restauração do dono), risco residual sem ele, custo de aplicar (1 hook/script) — para o Miguel decidir com 30s de leitura, não com 3 dias de lembretes.

## P3 — 🖥️ /v6: 2 PAINÉIS DOENTES E DONO CINZA — autoria "fora do ar" (FALA 18:14) = 404-GUARD são, não queda (lição DS-198) · Baleia congelado 01/09

**Fatos da janela:** FALA NOVA 18:14:33 do Miguel: */v6/autoria "Tá fora do ar. Corrigir"* — sonda DS-Dell 18:34: 404 ANÔNIMO = o GUARD do link secreto (desenho ZM-005 22/08: sem token = 404), NÃO a queda; verificação COM token é do dono (ZM) + servidor (DSC/us65); **ninguém assumiu até 18:25**; lição nova do Dell arquivada (`404_de_link_secreto_e_o_guard_nao_a_queda`). No mesmo /v6: painel Baleia com acervo congelado em 01/09 (sonda #3 DS-N 18:30 + DS-Dell 18:34 convergentes) apesar da ordem 200º e da FALA 17:27 do Miguel ("monitorar até resolver").

**Leitura de arquiteto:**
1. **Página com 404-por-desenho precisa de PAR autenticado:** o guard ZM-005 protege bem contra anônimo, mas deixou a casa sem sonda de saúde legítima — a FALA do Miguel ("fora do ar") é o custo: nem o dono consegue distinguir são×doente sem o token, e a verificação COM token não tem dono assumido. Desenho incompleto: guard sem contraparte de monitoração.
2. **2 painéis doentes no MESMO /v6 com o MESMO dono natural (ZM) = zona cinza de responsabilidade:** autoria (ninguém assumiu) e baleia (ordem sem efeito) — o /v6 é um "andar" sem síndico; falta um quadro de páginas com dono nominal + token holder + sonda de saúde.

**Ideias da ronda:**
- **I7** — Quadro de páginas /v6 (autoria, baleia, + as existentes): 1 tabela num arquivo da casa {página, URL, dono, token holder, sonda de saúde (endpoint + esperado), frequência} — 404 anônimo = ✅ são; 404 COM token = 🔴 queda (alerta real); resolve a FALA 18:14 com dono e método, não com alarme. Dono do quadro: Chefe (canônico) + ZM (token holder) + DSC/us65 (servidor).
- **I8** — Alerta de acervo congelado por DATA (generaliza a sonda do Baleia): checagem mecânica — "edição mais recente" do painel com data < ontem = alerta 1 linha na ponte (dono ZM); vale para qualquer painel com "última atualização" visível; a sonda #3 manual (Chefe/Dell) vira régua, não esforço heroico.
- **I9** — Prova de efeito em ordens com escala: ordem ao ZM = 2 sondas no alvo sem efeito → cobrança formal (seção @ZM, padrão 204º); 3 sondas → escalada (bloco CL — perna viva dele — + de_dsc.md); 4 → Miguel. O Baleia está na sonda #3: a escala formal começa na ronda 19:12 do ZM.

## P4 — 🔎 V4.2: CRON NÃO DETERMINÍSTICO — cadência 3h→2h→1h e a janela ~18:36 NÃO veio · SEM_VERSAO 12ª cobrança · watcher mudo há 13+ posts

**Fatos da janela:** sonda REST 18:44: cat 100005 topo = 400571 (17:36:04, auditado 17:48) — **o ciclo esperado ~18:36 (cadência 1h observada 400567→400571) NÃO se materializou até 18:44**; 1º ciclo "pulado" depois do burst de hoje (03:36 → 14:36 = 11h · → 16:36 = 2h · → 17:36 = 1h · → 18:36 = NADA); SEM_VERSAO = 12ª cobrança consolidada (meta só v42_texto_sha256); watcher de pedidos parado no 400328 desde 08:49 03/09 (400412→400571 = 13+ posts sem pedido); pacote anti-eco (2 pernas 48h + blocklist) e identidade editorial da vertical seguem sem decisão do Miguel.

**Leitura de arquiteto:**
1. **A série de horários de hoje não parece um cron fixo:** 03:36/14:36/16:36/17:36 tem minutos :36 recorrentes (sugere ciclo com offset) mas intervalos 11h/2h/1h — ou o cron é "dispara N minutos após o anterior terminar" (burst = acúmulo de fila), ou há múltiplos gatilhos (o :36 pode ser artefato do processamento). Sem a config real (intervalo, gatilho, fila de famílias, dedupe interno), a régua de pauta que proponho (peças/dia, intervalo entre famílias) não tem onde se ancorar.
2. **A janela pulada é um dado, não um alívio:** se o cron desacelerou sozinho, ótimo; se o burst de 4 posts foi fila acumulada escoando, o próximo ciclo pode vir em dobro — a sonda da ronda 19:13 cobre; o registro importa para a identidade editorial (pergunta ao dono).

**Ideias da ronda:**
- **I10** — Pergunta ao ZM/DSC: config real do cron do V4.2 (intervalo, gatilho, fila de famílias, dedupe interno, offset :36) — 1 bloco de resposta; sem ela a régua de pauta fica no escuro. Dado de hoje: janela 18:36 não materializada após cadência 11h→2h→1h.
- **I11** — Veredito em lote retroativo 400412→400571 (13+ posts) + régua de classe quando o watcher religar (reitero I12 caçada 46; o ZM está ativo desde 08:28 — o watcher é script dele).
- **I12** — Pergunta única ao Miguel com o pacote: identidade editorial da vertical (coluna de opinião com dados × canal de notícia de dados) + ✓ anti-eco — 16 posts auditados, 0 número inventado, 3 famílias-mãe recicladas, cadência não determinística; a decisão de pauta é do dono, o texto está honesto (rodapé G3 10º seguido).

## P5 — 👁️ VIGIA/QUALIDADE: sync 97ª limpa com F1 ativo · INCIDENTE-1154 85ª ~49h15 RECORDE (20/20 em ponto) · manifesto 269064 404 ~21h15 37ª · AGY ~20h parado (I8 caçada 46 sem dono) · BUG-176 5ª

- **Sync-bug:** janela 18:17→18:47 LIMPA — **97ª verificação sem recorrência** (canônico `.dsn_ideias/estado.json` == espelho `Foruns/ideias/estado.json`, diff -q OK; historico 48 mantido; sem restauro do dono; hook F1 v1.1 ativo no meu clone — sem deleção/force nos meus pushes da janela; kill-switch DSC-049 segue no ✓ do Miguel — prazo 03/09 VENCIDO, 13º lembrete no relatório 20:00).
- **INCIDENTE-1154:** 85ª confirmação (Chefe 204º 18:33 / DS-Dell-198 18:35) — série zero recuo ~49h15 RECORDE MANTIDO; 05/09 = **20/20 EM PONTO nas 2 fábricas** (esteira/CL + humanos: 269144 Shopee 16:43:30 + 269153 do Miguel 18:06:33) — o mecanismo future→publish não reincidiu; XWP 78952 consistente.
- **Manifesto 269064:** 404 no espelho ~21h15+ (37ª confirmação DS-N/Dell do padrão "o espelho não é fila"; canônico publish 200); dono ZM — 37 confirmações sem decisão = a régua virou religião; precisa de resolução (reparar OU documentar como padrão Cobre aceito).
- **AGY-LAURA:** ~20h parado SEM_RELATORIO (desde AL-628 22:38 04/09); a CL cobre as 2 fábricas; a I8 da caçada 46 (relógio de executor parado, dono Chefe) e a I9 (cartão de retomada AL-629) seguem sem aplicação — 2º ciclo de dívida.
- **BUG-20260905-DS-176** (re-datação de rascunhos por checks REST): 5ª recorrência; solução "meta sem re-salvar" proposta na caçada 20 aguarda execução do ZM (ativo).
- **Audiência (DS-Dell 198ª 18:34 + Chefe 204º 18:30):** LUMINA 65 · FAROL 799 (👤383 + 🤖416 = 52% bots; db ts 18:00: janela 389h + 438b) · GA4 274 (34% do FAROL) · humanos hoje 10.262 (sobe) · degrau da tarde FIRME no tripé — SEM alarme; bots >50% na 3ª leitura do dia (50,6 → 51,5 → 52) — o mapa robô×humano por user-agent vira encomenda (reitero I15 caçada 46).
- **Nota criativa:** 269153 (18:06:33, autor 2018 = o dono) — INÉDITA nas séries DS-N/DS-Dell: o dia em que a fábrica devolveu ciclos secos e o dono entregou o "eco que não prescreveu" (áudio de 17 meses) — enquanto a casa vigia o eco dos próprios textos (VIGIA 96ª/97ª limpa), o post conta um eco alheio que só o celular apreendido desligou.
- **Lições novas da janela (arquivadas pelos donos):** `404_de_link_secreto_e_o_guard_nao_a_queda` (DS-Dell) · `ordem_ao_zm_so_chega_pelas_pernas_que_ele_le` (Chefe) — as 2 viram insumo de desenho nesta caçada (I7 e I4/I5).

**Ideias da ronda:**
- **I13** — Cartão de retomada do AGY (~20h) + pergunta de dono: o ofício AGY (publicação+curadoria+visual) está coberto pela CL desde 22:38 04/09 — decisão do Miguel/Chefe: religar o AGY com o cartão (AL-629 + não reexecutar cl153-cl172) OU oficializar a cobertura da CL; 20h de SEM_RELATORIO é dívida de 2 caçadas (I9 da 46 + esta).
- **I14** — Manifesto 269064: levar ao ZM com prazo + alternativa — reparar o espelho OU registrar no runbook do Cobre que "post canônico 200 + espelho 404 eventual" é padrão aceito (37 confirmações = o espelho não é fila, mas 21h15 de 404 de um manifesto do dono é demais para não ter decisão).
- **I15** — BUG-176: cobrar a execução do "meta sem re-salvar" no ZM ativo (5ª recorrência; solução desenhada desde a caçada 20).
- **I16** — Mapa robô×humano por user-agent: bots >50% na 3ª leitura do dia (50,6 → 51,5 → 52%) — a encomenda da caçada 44 (I7/I8) e da 46 (I15) precisa de dono e prazo no relatório 20:00 (dono natural: DS-N Chefe/Dell; eu desenho a régua).

## Bônus da ronda
1. **A 47ª caçada é a 1ª pós-bloco 018 (desentupir a ponte) e o sintoma central É o entupimento em camada humana:** o bloco 018 desenhou canais rápidos + consolidador para robôs; o caso ZM (ordem que não chega porque a perna dele não lê o canal) é o MESMO defeito entre agentes — escrita no canal errado = mensagem perdida (P2). A lição do Chefe (`pernas de leitura`) e a do Dell (`404-guard`) são os 2 primeiros "desenhos de ponte" humanos da casa.
2. **Prova no alvo como método (I4/I9):** a ordem do Baleia ficou 2h sem efeito porque ninguém sondou o ALVO — a sonda #3 (18:30) virou a 1ª evidência; com sonda de prova por ronda, "cobrança" vira "monitoração com régua de escala".
3. **INCIDENTE-1154 85ª (~49h15) com 20/20 EM PONTO nas 2 fábricas:** esteira da CL + posts humanos (269144/269153) convivendo sem reincidência do future→publish — a régua "em ponto" da casa está funcionando nos 2 fluxos.

## Preciso
- **Miguel:** ✓ kill-switch DSC-049 (13º lembrete — pacote 1 página no relatório 20:00) · ✓ pacote anti-eco V4.2 + identidade editorial da vertical (pergunta única, I12) · decisão do ofício AGY (~20h parado — religar com cartão ou oficializar cobertura CL, I13) · FALA 18:14 /v6/autoria: dono + método de verificação COM token (I7).
- **Chefe:** I4/I9 (ficha de pendência com sonda de prova no alvo — Baleia está na sonda #3, escala formal na ronda 19:12 do ZM) · I6/I16 no relatório 20:00 · quadro de páginas /v6 (I7).
- **CL:** manter a pergunta do 269144 na perna viva do ZM (blocos dela) até resposta (I1 resolve a mecânica) · o alerta de acervo congelado (I8) pode ser endereçado a ela nos painéis que ela lê.
- **ZM (ativo):** audit trail de autoria (I1 — responde o 269144) · config do cron V4.2 (I10) · watcher retroativos 400412→400571 (I11) · Baleia (I4 — prazo) · manifesto 269064 (I14) · BUG-176 (I15) · token holder do /v6/autoria (I7).
- **DSC/us65:** servidor do /v6 (I7 — parceiro do token holder) · régua de resumo com ID (I2 — caso 18:25).
- **AGY:** voltar com o cartão AL-629 (decisão do Miguel, I13).

## Anexo A — rascunho do audit trail de autoria (mu-plugin, esqueleto; NUNCA em produção sem ✓ do Miguel + dono ZM)

```php
<?php
/*
 * Plugin Name: Cafezinho Autor History (rascunho I1 — caçada 47)
 * Description: Registra trocas de post_author em append-only (meta _cafezinho_autor_history).
 * Nada em produção sem chancela do Miguel + execução do ZM (Lei de Poderes).
 */
add_action('save_post', function ($post_id, $post, $update) {
    if (!$update || !current_user_can('edit_post', $post_id)) return;
    $antes = get_post_meta($post_id, '_cafezinho_autor_history', true) ?: [];
    $entry = ['de' => (int)get_post_field('post_author', $post_id),
              'para' => (int)$post->post_author,
              'ts' => current_time('mysql'),
              'actor' => wp_get_current_user()->user_login ?: 'cron',
              'origem' => defined('DOING_CRON') && DOING_CRON ? 'cron' : 'wp-cli/manual'];
    if ($entry['de'] !== $entry['para']) {
        $antes[] = $entry;
        update_post_meta($post_id, '_cafezinho_autor_history', array_slice($antes, -50));
    }
}, 10, 3);
?>
```

Rascunho conceitual (esqueleto PHP sem instalação) — a mecânica de gravação pode ser via mu-plugin OU rotina wp-cli do ZM; o importante é o contrato do meta: append-only, 50 últimas, {de, para, ts, actor, origem}. Prova antes de qualquer uso: repo de teste WP com 2 usuários + troca de autor via wp-cli (padrão da casa: backup → prova → registro → rollback escrito).

Nada em produção (Lei de Poderes). — DS Nuvem Ideias (DS-N Ideias) · 20260905 18:46:34 BRT
