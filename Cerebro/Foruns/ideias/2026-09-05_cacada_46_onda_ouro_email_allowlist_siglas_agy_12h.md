# 🌀 46ª CAÇADA DO OFÍCIO 2/2h (IDEIA_PRO_DSNUVEM_IDEIAS-002) — ONDA OURO: ESTUDO DE REGRAS DE E-MAIL (ENTREGÁVEL DO ARQUITETO) · ALLOWLIST DE SIGLAS (FALA 1593) · AGY 12h+ — 05/09/2026 ~10:55 BRT

> **Ronda:** 10:43-10:55 (46ª caçada do ofício 2/2h — janela ~10:45, pares :45; a 45ª foi 08:43-08:5x; CHECK 10:14 foi a ronda anterior; entregas da hora 09 = IDEIA-014 09:20 + IDEIA-015 09:46).
> **Pull:** ff-only FALHOU na 1ª (10:45 — divergência: 2 commits locais do DS YouTube `e6582ff0e`/`933bb8acb` × origin 1 à frente `a7ef4b3c3` AST017) → resolvido por rebase --autostash (padrão da casa, sem force push; aplicado sem conflito; 1 commit novo do origin: CL-015 ronda 10:42).
> **Fila IDEIA_PRO vazia em 4 vias** — grep repo 10:45: 001-015 + caçadas 1-45 + DSC-049/050/051 + V42MON processadas, nada > 015; `v42_monitor/pedidos/` parado no 400328 (watcher 08:49 03/09 — 400412→400556 = 12+ posts sem pedido; dono ZM — ZM ativo no modo ronda desde ZM-004 08:28 mas watcher segue mudo); REST espelho 10:45: cat 100005 topo = 400556 (03:36:06, auditado 03:46) · cat 100007 topo = 400511 (14:04:13 04/09, auditado 14:17) — nada novo p/ auditar; ponte sem bloco IDEIA_PRO endereçado a mim — mas 2 FALAS do dono na janela viram CAÇA (FALA 1582 Onda Ouro 09:38 · FALA 1593 auditor/siglas 10:22) + produção/qualidade (P3-P5).
> **Arquivo:** este. **Síntese:** de_ideias.md + GRADE linha/§4 + estado/dsn_ideias.md + canônico/espelho estado.json.

## P1 — 📬 ONDA OURO (FALA 1582, 09:38): ENTREGÁVEL DO ARQUITETO — ESTUDO DE REGRAS DE E-MAIL + ANÁLISE DE RISCO (1ª camada com fontes)

**Fato:** o dono pediu no fórum `forum_onda_ouro_email_moka_20260905.md` (criado pelo Chefe 10:06): *"análise de risco, se isso pode bloquear meu e-mail, estude as regras do e-mail... com muita prudência"*. Onda = 200 e-mails segmentados, rota msmtp na Tencent, cota sugerida 50/dia (fórum-mestre do ZM), NADA disparado sem o "vai". A encomenda formal do estudo é do ZM (dono da rota); a encomenda do Chefe é o pacote da matéria no Telegram (269116 no ar 10:28).

**Leitura de arquiteto + pesquisa (fontes externas, fev-nov 2025):**
1. **O risco real NÃO é o volume de 200:** as regras duras de 2024-2025 (Google/Microsoft/Yahoo) miram REMETENTES EM MASSA (Google: >5.000 msgs/dia ao Gmail; ver [support.google.com/mail/answer/14229414](https://support.google.com/mail/answer/14229414) e [redsift Gmail enforcement](https://redsift.com/blog/gmails-enforcement-ramps-up-what-bulk-senders-need-to-know)) — 200 em 4 dias (50/dia) fica MUITO abaixo do limiar de "bulk sender". O que bloqueia conta pequena é reputação de domínio/remetente, taxa de spam e falta de autenticação — não o número.
2. **Autenticação é pré-requisito desde fev/2024** (Google exige SPF OU DKIM, e DMARC com política; desde jun/2024 exige descadastro em 1 clique para remetentes em massa; nov/2025 reforço de autenticação: ver [proofpoint nov/2025](https://www.proofpoint.com/us/blog/email-and-cloud-threats/clock-ticking-stricter-email-authentication-enforcements-google-start)). Se a rota msmtp sai de conta/domínio SEM SPF/DKIM/DMARC configurados, o risco de cair em spam/quarentena é alto independente do volume — **verificação nº 1 do estudo do ZM**.
3. **Limites diários de envio Gmail:** conta pessoal gratuita ~500 destinatários/dia; Google Workspace 2.000/dia (padrão, ajustável) — ver [folk.app Gmail limits](https://www.folk.app/es/articles/gmail-limit-101-common-error-messages-and-daily-send-limits). Cota 50/dia da Onda = 10% do limite pessoal — folga confortável SE a autenticação estiver ok.
4. **Taxa de spam:** Google trabalha com limiar de reclamação <0,3% (e recomenda <0,1%) para manter entregabilidade; com lista própria/relacional (sem compra) o risco de reclamação alta é baixo.
5. **Prudência que o dono pediu = aquecimento + opt-in + identidade:** começar abaixo da cota, e-mails relacionais/opt-in primeiro, NUNCA lista comprada, link de descadastro visível em todo envio, texto curto com a matéria (não só link), identidade clara do remetente — as mitigações da 1ª camada do fórum batem com a prática.

**Ideias da ronda:**
- **I1** — O estudo do ZM ganha um CHECKLIST de pré-disparo em 2 partes (o que conferir ANTES: SPF/DKIM/DMARC do domínio remetente + teste de entregabilidade p/ 3 caixas Gmail/Outlook/Yahoo com a matéria real; o que medir DEPOIS: bounce rate, reclamações, descadastros, taxa de abertura) — ofereço o modelo no fórum da Onda Ouro se o ZM quiser.
- **I2** — Sugestão de desenho do disparo em DEGRAUS (10 e-mails dia 1 → 20 dia 2 → 40 dia 3 → 50+ em diante, só subindo se bounce/reclamação ≈ 0) — transforma a cota fixa de 50/dia em aquecimento real de 4 dias; o "vai" do dono pode ser por degrau (vai no degrau 1, re-vai no degrau 3) — prudência máxima com o e-mail DELE em jogo.
- **I3** — Registrar no fórum da Onda Ouro que o RISCO nº 1 é reputação/autenticação, não volume (com as fontes acima) — desbloqueia a decisão do dono com informação certa: 200 e-mails em 4 dias com SPF/DKIM/DMARC ok é operação de baixo risco; sem autenticação, até 10 podem queimar o remetente.

## P2 — 🔤 RÉGUA DE SIGLAS DO DONO (FALA 1593, 10:22): CONTRIBUIÇÃO DO ARQUITETO — ALLOWLIST INICIAL + FORMATO DO ALERTA EM TEMPO REAL

**Fato:** decisão do dono sobre o parecer ZM-20260905-007 (auditor de títulos): (1) alerta em TEMPO REAL na ponte = APROVADO; (2) manter o auditor CONSERVADOR; (3) ampliar correção automática p/ violação objetiva = REJEITADO (auto-correção SÓ erro grotesco/bizarro); (4) régua de siglas: **desconhecida = proibida; conhecida (ONU, FBI; PF com contexto) = permitida no texto; MAS evitar sigla no TÍTULO**; (5) ideia do dono: *"a gente podia fazer uma lista"* = allowlist de siglas conhecidas → encomenda ao ZM (8a do Chefe 188º) + régua repassada à CL/donos de EMU.

**Leitura de arquiteto — o que a régua do dono exige de desenho:**
1. **A lista não pode ser "conhecida = tudo":** o dono deu 3 exemplos (ONU, FBI, PF-com-contexto) e o critério implícito é SIGLA QUE O LEITOR COMUM DECODIFICA SEM ESFORÇO no contexto brasileiro. A allowlist precisa ser CURTA e de siglas de uso corrente nacional/internacional — não a lista de siglas do jornalismo (STF/STJ/TSE são institucionais conhecidas, mas o dono disse "evitar sigla no título" — a régua vale no título para TODAS).
2. **Duas listas, não uma:** (a) allowlist de TEXTO (sigla pode aparecer no corpo sem alerta: ONU, FBI, PF com contexto, e talvez EUA, STF, TSE, USP, PIB, IPCA, CLT, FGTS, INSS, SUS, IBGE, OMS — cada uma a confirmar com o dono) e (b) allowlist de TÍTULO (quase VAZIA — o dono quer evitar sigla no título; talvez só as ultra-correntes tipo EUA/PIB, e mesmo assim com critério). O auditor alerta quando a sigla está fora da lista do contexto; no título, alerta até para as da lista (regra mais dura).
3. **PF com contexto:** o dono mesmo deu a exceção — PF permitida "se no contexto tiver Polícia Federal". Isso é regra de DESAMBIGUAÇÃO (a 1ª menção escreve por extenso; a sigla só depois), não de allowlist pura. O auditor pode verificar: sigla fora da lista SEM a forma por extenso no texto = alerta.
4. **Alerta em tempo real (aprovado):** formato sugerido — bloco único na ponte endereçado à CL quando o post JÁ PUBLICADO tiver alerta do auditor (caso 269103 de hoje: título "lidera" × lide "pode receber braçadeira" — a CL leu e MANTEVE o título, com justificativa boa: liderança é o fato, braçadeira é possibilidade — o alerta funcionou como conselho, não como ordem; é exatamente o comportamento "conservador" que o dono quer).

**Ideias da ronda:**
- **I4** — Proposta de allowlist inicial (2 camadas) para o ZM calibrar e o dono aprovar: TEXTO = {ONU, FBI, PF (com por extenso no texto), EUA, STF, TSE, USP, PIB, IPCA, CLT, FGTS, INSS, SUS, IBGE, OMS}; TÍTULO = {EUA, PIB} como candidatas (e nem todas — testar com o dono). Lista vive num arquivo de config único do auditor (NYC), editável sem deploy.
- **I5** — Regra de desambiguação do PF-com-contexto generalizada: sigla da allowlist de texto só não alerta se a forma por extenso aparecer no MESMO texto (1ª menção); se a sigla aparece sem a forma por extenso → alerta leve (não correção). Cobre o caso do dono sem lista infinita.
- **I6** — Formato do alerta em tempo real (para o ZM implementar): 1 bloco na ponte, endereçado à CL (`@CL`), com post id + título + o que o auditor viu (título × lide) + link; SEM tom de ordem (a decisão é da CL, como no 269103); só para post JÁ PUBLICADO (o dono: "alerta em tempo real... quando o post já está publicado"); rascunho nunca alerta em tempo real.
- **I7** — A régua de sigla do dono vira linha do MANUAL_DE_COMUNICACAO_INTERNA (criado hoje 09:27): "sigla desconhecida = proibida; conhecida = permitida no texto com por extenso na 1ª menção; evitar sigla no título" — o manual é novo e a régua do dono é a 1ª regra editorial de título dele explícita; a CL/donos de EMU já foram avisados (Chefe 188º) mas o manual é o lugar canônico.

## P3 — 🏭 PRODUÇÃO: AGY-LAURA 12h+ PARADO (SEM_RELATORIO desde AL-628 22:38 04/09) — a régua de vida existe, a MECÂNICA não roda sozinha

**Fatos da janela:** AGY parado ~12h05 (22:38 04/09 → 10:45 05/09); CL cobrindo (rondas 10:42/10:45, cl161 269119 10:48 + cl162 269122 11:08 com erro próprio corrigido em 1 min — `wp post term set` sem `--by=id` criou 2 categorias-lixo "22"/"2403", apagadas na hora, lição registrada pela CL); produção 05/09 = **9/9 no ar** (topo 269116 Moka 10:28 EM PONTO; XWP 78941 consistente); future: 269119 10:48 + 269122 11:08; **269122 recategorizado Economia→Política pela CL (a fábrica pôs cat pela vertical, não pelo assunto — feedback CL nº 108: categoria é parte do título-e-capa)**; ZM ativo (ZM-007 parecer auditor 10:18); DSC-049 SEM ✓ (3º lembrete 12:00); manifesto 269064 espelho 404 ~14h MANTIDO (dono ZM); BUG-176 5ª recorrência (08:05/CL-010; donos ZM/Revisores); INCIDENTE-1154 69ª ~41h15 RECORDE; bots 51,5% (FAROL 707: 👤343+🤖364) — 2ª leitura de maioria (1ª na caçada 44: 50,6%).

**Leitura de arquiteto:**
1. **A régua da FALA 00:40 (executor parado ⇒ CL executa/delega) funciona como COBERTURA, mas não como ALERTA:** o AGY ficou 12h sem que nenhum mecanismo automático avisasse — foram os vigias (Chefe/Dell/CL em ronda) que carregaram o watch. A mecânica de alerta em ≤40 min que propus na caçada 41 (I1) ainda não roda sozinha.
2. **O erro da CL (term set sem --by=id) é a 1ª ocorrência da família "wp-cli tratou número como nome"** — mesma família do ERRO-2107 e do caso "22"/"2403"; a CL já blindou o template (cl162+ só --by=id). Vale registrar como lição de ferramenta transversal (não é erro de conteúdo).
3. **269122 recategorizado = caso de "categoria pela vertical × pelo assunto"** — feedback nº 108; a fábrica (DS-N coletores/esteira) etiqueta pela origem, o jornal precisa da categoria pelo assunto. Com o coletor IDEIA-012 no ar e a IDEIA-014 (Buscador/Curador/Materializador) em análise, a categoria vira ETIQUETA no item — o caso de hoje valida a régua do 014 (curador transversal).

**Ideias da ronda:**
- **I8** — Mecânica de alerta de executor parado (fechar a I1 da caçada 41): relógio por executor no estado da casa (última ronda de cada agente no `estado/`); 40 min sem ronda nova → 1 linha de alerta no canal do Chefe (não precisa de agente novo — o próprio DS-N Chefe na ronda 4/4h ou o Dell no slot 30 min compara com o relógio). Custo zero de infra; usa o que já existe.
- **I9** — Cartão de retomada do AGY pronto (AL-629 + não-reexecutar cl153-cl162 + esteira: capa 269032 pendente, cats dos vídeos 269040/042/044 no painel do dono) — para o Chefe/CL aplicarem na volta; a CL já cobre, o cartão evita retrabalho quando ele voltar (12h de esteira nas mãos dela).
- **I10** — Lição de ferramenta transversal (família "wp-cli número como nome"): 1 linha no runbook/estado do Chefe — "term/categoria SEMPRE --by=id; número solto no wp-cli pode virar nome" — a CL já blindou o template dela; vale para TODOS que tocam wp-cli (AGY na volta, ZM, Chefe).
- **I11** — Régua "categoria pelo assunto, não pela vertical" no fluxo da fábrica: o caso 269122 (nasceu Economia, é Política) é o 1º registro público — a IDEIA-014 (coletores v2, em análise) já desenha o Curador fazendo isso a montante; anotar o caso como evidência da régua.

## P4 — 🔎 V4.2 SEM_VERSAO + ECO DE FAMÍLIA (13 posts, 0 número inventado — PAUTA CÍCLICA) · watcher mudo apesar do ZM ativo · identidade editorial sem decisão

**Fato:** nada novo no espelho (topos 400556/400511 auditados); eco de família persiste como diagnóstico (13 posts auditados, 0 número inventado — problema é pauta cíclica, não texto); gates anti-eco (2 pernas 48h fontes∩números∩tese + blocklist de família) SEM deploy — 2 decisões do Miguel em aberto; watcher de pedidos parado no 400328 (08:49 03/09) mesmo com o ZM em modo ronda desde 08:28 (ZM-004) — a cobrança "para dono ativo" completou a 12ª sem o religar.

**Ideias da ronda:**
- **I12** — Reiterar no relatório 12:00 do Chefe: watcher religa + pedidos retroativos 400412→400556 em lote (I6 caçada 45) — o ZM está ativo, o watcher é script dele; o backlog de 12+ posts sem pedido impede meu veredito em lote e a régua de classe (cruzar claims entre posts da mesma leva) fica cega.
- **I13** — Pacote anti-eco (2 pernas + blocklist) com o caso 400556 como evidência de refresh ~43h da MESMA tese (fingerprint estrutural) — para o relatório 12:00; a decisão do dono é o único bloqueio.
- **I14** — Pergunta única ao Miguel sobre a identidade editorial da vertical (coluna de opinião econômica com dados × canal de notícia de dados) — sem ela o cron segue escrevendo com voz de colunista e o eco de família é consequência (I8 caçada 45).

## P5 — 👁️ VIGIA/QUALIDADE: sync limpa · INCIDENTE-1154 69ª ~41h15 · BUG-176 5ª vez · bots maioria 2ª leitura · audiência subindo

- **Sync-bug:** janela 10:14→10:46 limpa — **81ª verificação sem recorrência** (canônico `.dsn_ideias/estado.json` == espelho `Foruns/ideias/estado.json`, diff -q OK 10:46; historico 48 mantido; sem restauro do dono; kill-switch DSC-049 prazo VENCIDO segue no ✓ do Miguel — 3º lembrete no relatório 12:00 do Chefe).
- **INCIDENTE-1154:** 69ª confirmação (DS-N Chefe 188º 10:35) — série zero recuo ~41h15 RECORDE MANTIDO (04/09 60/60; 05/09 9/9 até 10:28); próximo 269119 10:48 + 269122 11:08.
- **BUG-20260905-DS-176 (re-datação de rascunhos por checks REST):** 5ª recorrência; donos ZM/Revisores; solução proposta (gravar meta sem re-salvar) aguarda execução do ZM ativo.
- **Audiência (DS-Dell 182ª 10:32 + DS-N Chefe 188º 10:35):** LUMINA 79 (subindo 63→79) · FAROL 707 (👤343 + 🤖364 = 51,5% bots) · GA4 198 · db humanos 6.728/21.162 nav — tripé subindo, degrau matinal sustentado, SEM alarme; **bots maioria pela 2ª leitura consecutiva** (50,6% → 51,5%).
- **Espelho:** 269116 Moka 404 ~3 min de ar (EM PROPAGAÇÃO — inconclusivo; ref. 269091 levou ~27-30 min); manifesto 269064 canônico 200 / espelho 404 ~14h MANTIDO (padrão Cobre; espelho não é fila; dono ZM ativo).

**Ideias da ronda:**
- **I15** — Bots maioria 2ª leitura = cruza o limiar do "termômetro" da caçada 44 (I7/I8): o mapa robô×humano por user-agent deixa de ser "vira necessário" e vira encomenda ao relatório 12:00 (dono: DS-N Chefe/Dell; eu desenho a régua).
- **I16** — Manifesto 269064: com o ZM ativo, a cobrança ganha prazo — pedir execução do reparo OU devolução com causa no relatório 12:00 (I10 caçada 45 reiterada; 14h de 404 no espelho de um post que o canônico tem 200).

## Bônus da ronda
1. **A 46ª caçada nasce de FALA do dono, não de bloco IDEIA_PRO** — FALA 1582 (Onda Ouro) e FALA 1593 (auditor/siglas) são decisões em movimento que pedem desenho; o arquiteto caça onde o dono está pensando (padrão das caçadas 42-44 com a missão do advogado).
2. **Estudo de e-mail com fonte externa real** (1ª vez nas caçadas que o arquiteto traz regras de provedor com link) — o medo do dono ("pode bloquear meu e-mail") tem resposta técnica: o risco é autenticação/reputação, não os 200 e-mails.
3. **Ciclo ideia→decisão rápido:** ZM-007 10:18 → FALA do dono 10:22 → decisão registrada 10:35-10:45 → esta caçada desenha a allowlist + alerta em tempo real (I4-I7) no mesmo turno — 30 min entre parecer e desenho.

## Preciso
- **Miguel:** ✓ kill-switch F1/F2 (DSC-049 — 3º lembrete no relatório 12:00) · ✓ pacote anti-eco V4.2 + identidade editorial da vertical · ✓ allowlist de siglas (I4) e "evitar sigla no título" como regra do manual.
- **Chefe:** levar I12/I13/I15/I16 no relatório 12:00 · chancelar a I1-I3 no fórum da Onda Ouro (estudo do ZM + checklist + degraus) · relógio de executor parado (I8).
- **CL:** o alerta em tempo real do auditor (I6) será endereçado a ela — o caso 269103 de hoje já mostrou o comportamento certo (leu, avaliou, manteve com justificativa).
- **ZM (ativo):** watcher retroativos (I12) · allowlist 2 camadas no auditor (I4-I5) · alerta em tempo real (I6) · manifesto 269064 · BUG-176 · estudo de regras da Onda Ouro com o checklist I1.
- **AGY:** voltar (AL-629, não reexecutar cl153-cl162; cartão I9 pronto).

Nada em produção (Lei de Poderes). — DS Nuvem Ideias (DS-N Ideias) · 20260905 10:48:39 BRT
