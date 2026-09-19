# 🎬 BLOCO IDEIA_PRO_DSNUVEM_IDEIAS-017 — PADRÃO EDITORIAL DAS MATÉRIAS DE VÍDEO do YouTube no Cafezinho (template fixo + auditoria + segurança do fluxo)

> **Ronda:** 05/09/2026 ~13:0x-13:3x BRT (DS-N Ideias, Tencent). Pull ff-only OK na 1ª (12:43).
> **Bloco:** `IDEIA_PRO_DSNUVEM_IDEIAS-017` — DSH-us65 (ordem do Miguel ~13:0x), carimbo `20260905 13:15 BRT` e reenvio `13:35 BRT` (2ª versão com o estado atualizado do DS YouTube), blocos em `cerebro/Foruns/ponte_laura_completa/de_dell.md` (~18460-18474).
> **Fluxo da casa (do bloco):** Ideias entrega → DS-N Chefe aprova → resumo ao MIGUEL pelo @Dsnchefe_bot. Aplicar em TODO vídeo novo e retroajustar os recentes.
> **Encaminhamento do Miguel (relay 14:05):** a IDEIA-017 pronta → Chefe CHANCELA → execução termina na mão do ZM. **Piloto imediato do padrão: vídeo Peter H. Diamandis EP285 (`https://youtu.be/JywXvB8PpTs`)**, já na queue_youtube.md.
> **Refs:** manual_do_publicador.md (CL, 05/09 — entregue 12:10) · MANUAL_DE_ESCRITA/ESCRITA_PORTAL (v2.1.1) · MANUAL_DE_ESTILO_UNIFICADO (fonte única de estilo) · MANUAL_DE_COMUNICACAO_INTERNA (texto limpo) · fluxo DS YouTube (canal_ds_youtube.md + queue_youtube.md) · lições do Nassif de hoje (269113: timecodes na FONTE, não no corpo; nota interna nunca no corpo; dia da semana no calendário) · INCIDENTE-1740 (runtime publicou direto 04/09) · ordem 04/09 22:55 (YouTube draft-only, régua ≥2h/máx6, gate CL) · **Emenda 10 (24-25/08: cat 28 exclusiva do Agente YouTube — reportagem baseada em vídeo NÃO ganha 28)** · IDEIA-009/010/011/016 (carrossel/cortes/estratégia YT) · manual de operação dos agentes YouTube (16/08) · memória vertical YouTube V4.1 (02/09) · regra §82 (sem segredos) · regra da casa: **robô entrega rascunho; quem publica é a CL (gate)**.
> **Natureza:** ESTUDO/ARQUITETURA/PLANO + TEMPLATE DOCUMENTADO (exemplo preenchido) — NADA executado em produção (Lei de Poderes). Nenhum valor de chave neste arquivo (§82).
> **Marcador:** `PRONTO_BLOCO017_PADRAO_EDITORIAL_VIDEO`

---

## 0. Resumo executivo (o veredito do arquiteto)

1. **A dor do Miguel é real e tem nome: cada matéria de vídeo sai de um jeito.** Auditoria de hoje (269113 Nassif + os precedentes 268553 Ronnie Lessa e 268440 Sabatinas) mostra que o formato varia em 6 pontos: posição do embed (às vezes nem tem), crédito do canal (fraco ou ausente), quem fala (nomes sem qualificação), timecodes (no corpo × na FONTE), nota interna de produção (vazou no Nassif pré-gate), e categoria/tags. O que falta não é mais um "jeito certo" solto — é **UM molde único + UM fluxo com gates que obriga o molde**.
2. **A casa já tem 80% do molde nas regras** — o Nassif de hoje (269113) foi o primeiro a passar pela régua completa da CL (timecodes na FONTE, nota interna removida, dia da semana conferido no calendário, capa = thumbnail oficial carimbada) e o resultado é o melhor exemplo de matéria de vídeo da casa. A IDEIA-017 **congela esse padrão em template documentado** e fecha as lacunas restantes (embed no topo, crédito canônico, título do molde, resumo editado, citações com timestamp na FONTE).
3. **Fluxo seguro (a "maneira mais segura" que o Miguel pediu) já é o fluxo de hoje pós-1740:** link → porta-download (Dell residencial, IP não-datacenter) → Whisper/legenda (inglês → legenda + resumo pt) → matéria no TEMPLATE → **RASCUNHO WP (nunca publicar direto)** → revisão do DS-N Chefe (pessoal) → **GATE CL (publica com prova REST)**. O que falta documentar/automatizar: o checklist de personagens (nomes com qualificação — DB de 248 personagens existe), a transcrição COMPLETA antes de escrever (regra de ouro), e o rascunho já nascer no molde (para a CL não precisar remendar).
4. **Piloto Diamandis EP285 JÁ ESTÁ NA FILA (12:37) e em ERRO** (`audio_falhou_tentativa_1` às 12:37; JywXvB8PpTs) — a entrega deste bloco destrava o molde; a execução (porta→whisper→rascunho no template→gate) é do ZM/DS YouTube/CL com a chancela do Chefe.
5. **Auditoria entregue neste arquivo (§2): antes/depois do padrão com 4 matérias reais** — o que variava, o que o molde padroniza e o ganho por caso. Retroajuste dos recentes: 269113 já está no padrão; 268440/268553 publicados em 01/09 permanecem como estão (publicado não se despublica; a régua vale do padrão em diante, com correção só se houver erro factual).

---

## 1. A DOR (do bloco, verbatim resumido)

> "Dor real dele: assiste muito vídeo, quando gosta manda publicar no Cafezinho — mas as matérias de vídeo tão saindo DESCONFIGURADAS, cada uma de um jeito. Criar UM PADRÃO para TODAS as matérias de vídeo do YouTube:
> 1. TEMPLATE FIXO (o Miguel manda o link → o sistema FAZ o padrão): [título forte estilo casa] → [embed do vídeo no topo] → [crédito do canal + link + quem fala (personagens com nome/qualificação)] → [resumo editado com o melhor do vídeo] → [citações com timestamp] → [categoria 28 Vídeos + tags + thumbnail oficial]. Nada de formato livre: TODO post de vídeo segue o molde.
> 2. AUDITORIA: amostrar posts de vídeo recentes (269113 Nassif de hoje incluído) e listar o que varia (posição do embed, crédito, título, tamanho) — mostrar o antes/depois do padrão.
> 3. SEGURANÇA DO FLUXO: transcrição completa antes de publicar, checagem de nomes dos personagens, revisão dupla Chefe→CL permanente p/ vídeo, réguas já aprovadas (2h/máx6/dedupe), e CONFIRMAR o que o DS YouTube já resolveu (porta-download residencial OK hoje: 6qXIQKXCHAQ, DIavgncHyiI, MrggA3TvOuE baixados; Whispers disparados) e o que falta.
> 4. ENTREGA: ideia desenvolvida + template documentado (exemplo preenchido) → Chefe aprova → aplicar em TODO vídeo novo e retroajustar os recentes."

Nota de leitura do arquiteto: a 2ª postagem do bloco (13:35) corrige o estado do DS YouTube — 6qXIQKXCHAQ baixado; DIavgncHyiI e MrggA3TvOuE "em tratamento/erro a acompanhar". Incorporei a versão atualizada.

---

## 2. AUDITORIA — o que varia hoje (antes/depois do padrão)

Base: as 4 matérias de vídeo-referência da casa + o que a CL registrou nos gates.

| Matéria | Título | Embed | Crédito do canal | Personagens | Timecodes | Nota interna | Cat | Tamanho aprox. |
|---|---|---|---|---|---|---|---|---|
| **268440** (Sabatinas das Cunhãs, 31/08, robô YouTube) | forte estilo casa (furo Elmano×Ciro) | não documentado no arquivo | citado no rodapé do arquivo (canal As Cunhãs) | Elmano + jornalistas — grafia a conferir (PAUTA-CHEQUE: "Elumano", "Ébel Rebolsas", "Luizane Lins") | **NO CORPO** (cada citação [mm:ss]) + lista na FONTE | não | Vídeos | longo (~2.500 palavras) |
| **268553** (Ronnie Lessa/Record, 01/09, robô YouTube) | forte estilo casa | não documentado | canal Record citado | Lessa, Élcio, promotor — grafia conferida pela CL no gate | **NO CORPO** (cada citação [mm:ss]) | não | Vídeos | longo |
| **269113** (Nassif/TV GGN, 05/09, texto do Chefe) | forte estilo casa (EMU-2 do ZM mantido) | **embed no topo do WP** (não documentado no arquivo .md) | crédito na FONTE (TV GGN 20 Horas + link + timestamps) | Nassif + bancada (Ícaro, Camila) nomeados com papel | **SÓ NA FONTE** (13 removidos do corpo pela CL) | **REMOVIDA pela CL** ("aguarda gate da Claude Laura" não pode ficar) | **Política** (pelo assunto — live de política) | médio (~5.300 chars) |
| **269091** (Advogado defensor de Moraes, texto DO MIGUEL, 05/09) | do dono | **embed do vídeo de 14 min (X) no corpo** | perfil do criminalista conferido pela CL | Bruno Salles Pereira Ribeiro (perfil completo verificado) | não se aplica (texto do dono) | não | a definir | longo (11,8 mil chars) |

**O que varia (diagnóstico):**
1. **Posição do embed:** nos arquivos .md da casa o embed não é documentado (o WP decide); no 269091 o embed veio no corpo porque o dono colou. O markup canônico histórico (53 posts com `youtube.com/embed` desde 21/07, template YT V2) é `<figure class="wp-block-embed is-type-video is-provider-youtube…">` como **PRIMEIRO elemento** do conteúdo, antes do 1º parágrafo — o padrão do bloco 017 (embed no topo) já era o padrão histórico do agente. Padrão: **embed no TOPO, logo abaixo do título**.
2. **Crédito do canal:** forte no 269113 (FONTE canônica), fraco nos do robô (só menção). Padrão: **bloco de crédito obrigatório logo após o embed** (canal + link + licença/uso jornalístico).
3. **Timecodes:** no CORPO nos 2 do robô (01/09 e antes — o estilo foi proibido em 01/09 17:5x e a CL aplicou no 269113); o Nassif é o 1º no padrão novo. Padrão: **citações no corpo SEM timecode; timecodes das falas-chave SÓ na FONTE**.
4. **Nota interna de produção:** vazou no rascunho do Nassif ("aguarda gate da Claude Laura" — removida pela CL). Padrão: **nota interna/estado de produção NUNCA no corpo** (fica no arquivo de produção, não no post).
5. **Categoria:** 269113 foi para Política (pelo assunto); a regra da casa (CL-015/feedback 108) é **categoria pelo assunto, não pela vertical**; o bloco pede "categoria 28 Vídeos + tags". **TENSÃO REGISTRADA: a Emenda 10 (24-25/08) reserva a cat 28 para o post do Agente YouTube com vídeo ABRINDO o post e o plugin endurecido REMOVE a 28 de reportagem baseada em vídeo** — o 269113 (live) saiu Política porque é reportagem, não produção do agente. Resolução proposta do molde: **cat de ASSUNTO como primária (sempre)** + cat 28 automática (pelo mu-plugin `cafezinho-auto-cat-videos.php`, que já cobre qualquer embed) quando o post for produção do agente YouTube com o vídeo abrindo; reportagem baseada em vídeo (Nassif) fica na regra da Emenda 10 (sem 28, só assunto). **Decisão pedida ao Miguel no §6** (revogar ou manter a Emenda 10 para o molde 017).
6. **Tamanho:** robô escrevia ~2.500 palavras (decupagem longa); o padrão da casa (Nassif) é **matéria editada ~2.000-5.500 chars** com o melhor do vídeo, não a transcrição inteira. Regra transversal: NUNCA cópia integral das legendas (uso jornalístico com citação).

**Antes/depois (o ganho do molde):**
- **ANTES (268440/268553):** timecodes no corpo (leitura quebrada), grafia de personagens com PAUTA-CHEQUE para conferir depois, sem crédito em bloco próprio, categoria única.
- **DEPOIS (molde 017):** embed no topo → crédito canônico → lead com personagens qualificados → corpo editado sem timecode → FONTE com timestamps → cat de assunto + 28 automática → capa thumbnail oficial. O leitor sabe onde está o vídeo, quem fala, o que ele disse e onde conferir — em TODO post de vídeo, sempre igual.

---

## 3. ARQUITETURA — o molde (template fixo) + o fluxo com gates

### 3.1 O TEMPLATE (estrutura canônica de TODO post de vídeo)

```
[TÍTULO] — frase única forte estilo casa (EMU-2/EMU-6: agente + ação; sem sigla desconhecida;
          sem "vídeo", "assista", "live de"; o título vende o FATO, não o formato)

[EMBED] — bloco do YouTube no TOPO (logo abaixo do título; nunca no fim)

[CRÉDITO] — 1-2 linhas: "O vídeo é do canal <NOME DO CANAL> (<link>). <Quem fala: nome +
            qualificação>. Reprodução autorizada para uso jornalístico com citação."
            (padrão Bertrand/Norton da IDEIA-013: citar, linkar, falar dele)

[LIDE] — 1º parágrafo: o fato central que o vídeo traz (o que o Miguel achou digno de
         publicar), com o contexto de data/canal/ocasião (ex.: "Na live da TV GGN 20 Horas
         desta quinta-feira (03/09)…")

[CORPO] — 2-4 blocos editados com o melhor do vídeo (cada um com subtítulo <h3>):
          o argumento/fala principal, os personagens com nome+qualificação na 1ª menção,
          aspas literais SEM timecode no corpo. Sem nota interna, sem "a redação".

[FONTE] — bloco final (negrito FONTE:):
          - O vídeo: <título do vídeo>, do canal <canal>, publicado em <data>.
          - Link: <URL completa do YouTube>
          - Timestamps das falas-chave (só aqui):
            [mm:ss] <o que é dito e por quem>
          (regra CL: timecodes vão para a FONTE, nunca no corpo)

[METADADOS WP] — categoria PRIMÁRIA pelo assunto (Política/Economia/… por ID, regra "categoria
          pelo assunto"; reportagem baseada em vídeo NÃO ganha 28 — Emenda 10; produção do agente
          YouTube com vídeo abrindo = 28 automática pelo mu-plugin) · tags do tema
          · capa = thumbnail oficial do vídeo com crédito na legenda (regra thumbnail_oficial_video;
          Vídeos(28) com essa meta NUNCA entram na caçada de capa) · autor = conta da casa (5801) ·
          status = RASCUNHO (nunca publicar direto)
```

### 3.2 O FLUXO SEGURO (quem faz o quê — da ordem à publicação)

```
[1] MIGUEL manda o LINK (bloco VIDEO_PRO_DSYOUTUBE / fila queue_youtube.md)
       ↓
[2] PORTA-DOWNLOAD (Dell residencial — YouTube bloqueia IP de datacenter; provado hoje:
    6qXIQKXCHAQ, DIavgncHyiI, MrggA3TvOuE) — dono: ZM/DS YouTube
       ↓
[3] TRANSCRIÇÃO COMPLETA (Whisper local / legendas) — REGRA DE OURO: nada de escrever
    sem o texto integral; inglês → legenda + resumo pt (tradução nossa, citada como tal)
    — dono: DS YouTube (cron :07/:22/:37/:52)
       ↓
[4] MATÉRIA NO TEMPLATE (o molde §3.1) — escrita por humano/Chefe ou robô; se robô,
    com personagens do DB (248 nomes canônicos) e checagem de grafia
    — dono: DS-N Chefe (revisão PESSOAL) / DS YouTube (rascunho)
       ↓
[5] RASCUNHO WP (status: draft; conta 5801; JAMAIS publicar direto — INCIDENTE-1740)
    — dono: DS YouTube/executor com credencial
       ↓
[6] REVISÃO DUPLA permanente p/ vídeo: DS-N Chefe (revisão pessoal do texto)
    → GATE CL (a Claude Laura lê inteiro, confere os 9 passos do manual do publicador,
    aplica correções, agenda e publica COM PROVA REST) — regra da casa pós-22:55 04/09
       ↓
[7] NO AR + PROVA (HTTP 200, permalink, meta _cafezinho_img_check/_txt_check)
```

### 3.3 O que o DS YouTube JÁ resolveu (confirmado nesta ronda) e o que falta

**Já resolveu (05/09):**
- Porta-download residencial OPERANDO (provas de hoje na queue: 6qXIQKXCHAQ e DIavgncHyiI BAIXADOS ~12:25-12:30; MrggA3TvOuE em ERRO com backoff; **JywXvB8PpTs = ERRO audio_falhou_tentativa_1 às 12:37 — piloto do molde aguarda retry da porta**).
- Transcrição por Whisper/legendas pt (provado no batismo 31/08 e no Nassif 05/09 — transcrição integral 4.177s via setsid; worker Whisper large-v3-turbo serial com backoff 30min→2h→8h→24h).
- Flash/redator escreve matéria estilo casa (268440/268553 — formato antigo; desde 02/09 o texto sai do redator V4.1 no NYC a partir da decupagem) — MAS no formato antigo (timecodes no corpo).
- Rascunho WP draft-only + pedido de gate (pós-01/09; travado no código GATE-TEXTO: 5801 nunca sai automático).
- DB de 248 personagens canônicos + correção de grafia (vertical V4.1, 02/09); regra da casa: nenhum nome é gravado/corrigido sem busca na fonte.
- Markup histórico do embed no topo (53 posts com `youtube.com/embed` desde 21/07) — o molde 017 devolve o padrão que o template YT V2 já usava.

**O que FALTA (lacunas que este bloco aponta):**
1. **O rascunho do robô nascer NO MOLDE 017** (embed no topo + crédito + sem timecode no corpo + cat de assunto) — hoje nasce no formato antigo e a CL remenda. Mudança: atualizar o template do `ds_youtube.py`/prompt do redator V4.1 para o molde §3.1 (dono ZM/DS YouTube, com a chancela do Chefe).
2. **Categoria de assunto automática** para o rascunho de vídeo (regra "pelo assunto" + Emenda 10 — o robô hoje não decide; a CL/Chefe decide no gate).
3. **Checklist de personagens no gate** (nome + qualificação conferidos ANTES do rascunho — o DB existe; falta o passo explícito no fluxo do vídeo).
4. **Transcrição completa como pré-condição** (regra de ouro) — o Nassif provou o caminho; falta virar trava do fluxo (sem transcrição integral, não escreve).
5. **Estado do piloto Diamandis**: JywXvB8PpTs em ERRO de áudio (1ª tentativa 12:37) + o 2º vídeo do dono DvFe9bR2eHA também em ERRO (audio_falhou_tentativa_2, 10:05) — a porta baixou outros; falta o retry com backoff do ZM para o piloto sair no molde. Nenhum dos 2 tem download OK/Whisper/decupagem/rascunho até 12:45.

### 3.4 Onde roda
- **Desenho/template:** este arquivo (Cérebro) — referência canônica do molde.
- **Execução:** Tencent (DS YouTube/robô) + Dell residencial (porta-download) + NYC (se o pipeline V4.1 pegar) + WP canônico (rascunho/gate CL). Nada muda de máquina: o molde é um CONTRATO DE TEXTO que todos os produtores de vídeo passam a seguir.

---

## 4. PLANO DE EXECUÇÃO (rito da casa: proposta → ponte → ✓ → execução → prova → rollback escrito)

| Passo | O quê | Dono | Prova de saída | Rollback |
|---|---|---|---|---|
| **P0** | Chancela do Chefe no molde 017 + resumo ao Miguel (via @Dsnchefe_bot) com as decisões §6 | DS-N Chefe | linha na ponte + RESPOSTAS | — (papel) |
| **P1** | Aplicar o molde no piloto Diamandis EP285 (porta→whisper→matéria no TEMPLATE→rascunho) | ZM + DS YouTube (execução) | rascunho WP no molde + gate CL | rascunho permanece draft |
| **P2** | GATE CL do piloto + publicação com prova REST | CL | HTTP 200 + permalink | publicado não sai (regra da casa) |
| **P3** | Atualizar o template do produtor automático (ds_youtube.py/prompt) para nascer no molde | ZM/DS YouTube | 1 vídeo novo nascendo no molde sem remendo da CL | backup do .py antes |
| **P4** | Registrar o molde como capítulo/padrão (referência no manual do publicador ou manual de estilo) | CL/Chefe | arquivo referenciado | — |
| **P5** | Retroajuste dos recentes: conferir 269113 (já no padrão) e os demais posts de vídeo do dia; correção só de erro factual (publicado não se despublica) | CL | lista conferida | — |

**Riscos e mitigação:**
- **R1 — piloto travado no download** (JywXvB8PpTs ERRO): backoff do ZM; se persistir, o molde vale no próximo vídeo (o padrão não depende de 1 vídeo).
- **R2 — robô volta a publicar direto** (família INCIDENTE-1740): travas já existem (draft-only no código + gate CL + whitelist de publish); o molde não muda a autorização — reforça o rascunho.
- **R3 — molde engessa demais:** o molde padroniza ESTRUTURA; a redação continua livre dentro dela (manual de escrita: "diretrizes, não regras ditatoriais"). Texto humano do dono (269091) NÃO passa pelo molde (regra: texto do dono não passa pela régua).
- **R4 — categoria errada:** regra "pelo assunto" + revisão dupla pega antes do ar.
- **R5 — capa:** thumbnail oficial com crédito é a regra; Vídeos(28) com `thumbnail_oficial_video` nunca entram na caçada.

---

## 5. EXEMPLO PREENCHIDO — o molde aplicado ao piloto Diamandis EP285 (rascunho de demonstração, NÃO publicado)

> **Aviso:** exemplo de FORMATO construído a partir do título/descrição públicos do vídeo (fila DS YouTube 12:37). Os fatos do corpo precisam da transcrição completa (regra de ouro §3.2 passo 3) antes de qualquer uso — nada aqui é matéria pronta. O vídeo está em inglês; a tradução das citações é nossa e deve ser citada como tal.

```
[TÍTULO — exemplo de formato] OpenAI corta o acesso de Elon Musk ao Cursor, sonda estelar
vira 1º voo de teste e Trump quer nave nuclear em Marte: o resumo da semana de Peter Diamandis

[EMBED — bloco do YouTube no topo]

[CRÉDITO] O vídeo é do canal Peter H. Diamandis (link: https://www.youtube.com/@pdiamandis),
episódio 285 do programa semanal do engenheiro e empreendedor americano, criador da XPRIZE
e da Singularity University. Reprodução para uso jornalístico com citação; tradução das falas
é da redação do Cafezinho.

[LIDE — a preencher após transcrição] No episódio 285 do programa de Peter Diamandis,
publicado em 05/09/2026, o engenheiro americano comentou três frentes da semana de
tecnologia e exploração espacial: a decisão da OpenAI de cortar o acesso de Elon Musk
à ferramenta de programação Cursor, o lançamento da primeira sonda interestelar da
história e o plano da Nasa/administração Trump de enviar uma nave movida a energia
nuclear a Marte. [fatos a conferir na transcrição]

[CORPO — 2-4 blocos editados, sem timecode; personagens com nome+qualificação]
...

[FONTE]
- O vídeo: «OpenAI Cuts Off Elon's Cursor, Humanity's First Star Probe, and Trump's Nuclear
  Mars Ship | EP #285», do canal Peter H. Diamandis.
- Link: https://youtu.be/JywXvB8PpTs
- Timestamps das falas-chave (a preencher com a transcrição):
  [mm:ss] OpenAI corta acesso de Elon Musk ao Cursor
  [mm:ss] 1ª sonda estelar da humanidade
  [mm:ss] nave nuclear de Trump para Marte

[METADADOS] categoria primária: Tecnologia (pelo assunto — IA/exploração espacial) + cat 28
Vídeos automática · tags: OpenAI, Cursor, Elon Musk, Peter Diamandis, exploração espacial,
Marte · capa: thumbnail oficial do vídeo com crédito · status: rascunho
```

---

## 6. O QUE PRECISO (decisões do Miguel via Chefe)

1. **Chancela do molde** (estrutura §3.1) para TODO post de vídeo novo — ou ajustes que ele quiser no formato (posição do crédito, tamanho, título).
2. **Cat primária dos vídeos — decisão sobre a Emenda 10:** o bloco pedia "cat 28 Vídeos + tags", mas a Emenda 10 vigente (24-25/08) reserva a 28 para o post do Agente YouTube com vídeo abrindo e REMOVE a 28 de reportagem baseada em vídeo (por isso o Nassif saiu Política). Proposta do arquiteto: **assunto como primária sempre + 28 automática quando for produção do agente com vídeo abrindo; reportagem (Nassif) sem 28**. Confirmar se revoga/ajusta a Emenda 10 ou mantém.
3. **Timestamps:** o bloco pede "citações com timestamp"; a regra interna (01/09, reforçada pela CL no 269113) é **timecode fora do corpo, na FONTE ao pé** (ou no PAUTA-CHEQUE interno, nunca no post). Proposta: manter a regra interna (timestamps na FONTE) — o leitor da matéria não lê [mm:ss] no meio da frase; quem quer conferir acha na FONTE. Confirmar.
4. **Piloto Diamandis EP285:** confirmar que ele quer esse vídeo como o 1º no molde (já está na fila por ordem dele — só o registro aqui; está em ERRO de áudio, retry do ZM).
5. **Retroajuste dos recentes:** ok manter 268440/268553 como publicados e aplicar o molde só nos novos? (publicado não se despublica).
6. **Texto do dono (269091) fora do molde** — confirmar que a régua "texto do Miguel não passa pelo molde" segue valendo.

---

*LI O MANUAL DE COMUNICAÇÃO INTERNA (cerebro/Estilo/MANUAL_DE_COMUNICACAO_INTERNA.md) — CHECK registrado (rondas anteriores; texto limpo sem asterisco nas sínteses da ponte).*

— DS Nuvem Ideias (DS-N Ideias) · arquivo de ronda 05/09/2026 (carimbo real na síntese da ponte)
