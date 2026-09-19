# 📣 Fórum — Plano de Mídias Sociais do Cafezinho (Etapa 1: Top 1 das 24h) + Conselheiro de Audiência

> **Quem:** ZCode/Kimi K3 · **Quando:** 19/08/2026 ~14:40→15:20 BRT · **Ordem do Miguel** (voz)
> **Tema Duplo:** este fórum + `Memorias/memoria_plano_social_top1_conselheiro_20260819.md`
> **Compromisso assumido:** NENHUM post de teste ("teste maluco") — só investigação + desenho + dry-run quando aprovado.

---

## §1. Investigação da infra social (feita, sem nenhum post)

| Rede | Conta | Credenciais | Estado técnico | Agente legado |
|---|---|---|---|---|
| **X/Twitter** | @ocafezinho | 4 chaves OAuth1 + Bearer em `/root/.env` (NYC) e nos 2 cofres Dell (hash conferido ✅) | **OK** — `verify_credentials` passou (read-only) | `agente_twitter.py` pausado 19/05 (em reforma); `postador_twitter.py` (Tweepy v1+v2, limite/dia) + `postador_twitter_fio.py` (contrato dry-run de fios) |
| **Facebook** | Página "O Cafezinho" | `FB_PAGE_ACCESS_TOKEN` + `FB_PAGE_ID` ✅ (read-only 200) | **OK** | `agente_facebook.py` ATIVO (modo foto, cooldown 4h, sem LLM; manifesto: texto 4-5 parágrafos quando no modo texto) |
| **Instagram** | @ocafezinhooficial | `IG_USER_ID` + token da página ✅ (read-only 200) | **OK** | `agente_instagram.py` pausado 20/07 (NYC); agente noturno local DESLIGADO 17/08 por ordem do Miguel (cards 22h, pipeline `scratch/card_v2/`) |
| **Visual/cards** | — | `CREATOMATE_API_KEY` + templates (INSTAGRAM/FACEBOOK/VERTICAL…) ✅ | OK | `agente_creatomate_bridge.py` (render de cards/reels) + card v2.7 legado (logo vazada + chapéu) |
| **Aprovação humana** | — | Telegram | OK | padrão `pendentes_social.json` + aprovação via Telegram (já existe no fluxo Creatomate) |

**Por que estava parado:** Twitter pausado pelo Miguel 19/05 (em reforma); Instagram pausado 20/07 (NYC) e o noturno local desligado 17/08 (publicou tema errado — "eua e vila euclides"). **Nada está quebrado: faltava decisão editorial + formato.**

## §2. ETAPA 1 (começar de leve) — "Top 1 das últimas 24h" todo dia, nas 3 redes

**Fonte única de dados:** o mesmo motor do box Top 10 (`/root/top_tendencias_push.py`, NYC, GA4 canônico, score hoje+ontem×0,3). O **Top 1** da rodada alimenta os 3 formatos. Publicação diária às **09:30 BRT** (sugestão; ajustável).

**Formatos por rede:**
- **Instagram — carrossel "Texto de capa do Cafezinho" (2 cards):** card 1 = capa do post (foto) com selo "🔥 TOP 1 DAS ÚLTIMAS 24H" + data/hora do selo + endereço `ocafezinho.com` na imagem; card 2 = card de texto (título + primeiro parágrafo grande, estilo editorial v2.7). Legenda com link encurtado e "link na bio". (IG não tem link clicável na imagem — por isso a URL vai escrita NA imagem + legenda.)
- **Facebook — bela postagem de texto grande + link:** 4–5 parágrafos de análise (estilo do manifesto FB: sério, sem hashtags), selo "Top 1 das últimas 24h" no 1º parágrafo + link para a matéria.
- **X/Twitter — fio de 2:** tweet 1 = "texto maiorzinho" (tese do post em até ~270 chars, sem pergunta-bait); tweet 2 = "continua aqui → link ocafezinho.com/…". (Antigravity já provou que fio é viável com essas chaves.)

**Segurança (compromisso):** as 2 primeiras semanas em **modo aprovação** — o agente monta tudo, manda preview no Telegram do Miguel e **só publica após OK** (aprovação em 1 toque; silêncio = não publica). Nada de post automático direto nesta etapa.

## §3. Histórico dos Tops ("guarda esse dado")

- **Arquivo diário:** toda rodada do Top 10 também grava `/root/agent_data/top10_historico/AAAA-MM-DD.json` (ts, metodologia, os 10 com posição/score) no NYC + cópia semanal no Cérebro (`Cerebro/Dados/top10_historico/`).
- **Baleia Azul:** passa a ler esse histórico (bloco "Top da semana/mês" quando existirem janelas suficientes).
- **Deriváveis (Etapa 2+):** top da semana (sexta/domingo), 15 dias, 30 dias, 3 meses, 6 meses, 1 ano — todos computáveis do histórico diário sem custo extra de API.

## §4. Agente CONSELHEIRO DE AUDIÊNCIA (o "estuda o analytics") — desenho

**Missão:** todo dia (07:30 BRT) produzir a **Análise do Dia** com janelas crescentes (dia/semana/mês/3m/6m/1ano), eleger o melhor post e dar **conselho editorial acionável** — ex.: "hoje apostaria mais em geopolítica", "eleição brasileira esquentando", "Ceará segue forte".

**Cérebro que cresce (auto-aprendizado conservador):**
1. Lê: GA4 (por post/editoria/hora), histórico Top 10 (§3), as próprias análises anteriores.
2. Escreve a análise do dia (LLM, roteador padrão) → arquivada em `Cerebro/Dados/conselheiro_analises/` (cada análise entra no histórico → o agente fica mais inteligente a cada dia).
3. **Saída operacional (a parte que muda o jogo):** o conselho vira `diretriz_conselheiro.json` (editorias quentes/frias + temas sugeridos) que os **intakes dos V4 leem todo dia** (fail-soft: se o arquivo não existir ou estiver velho, o V4 segue com a diretriz padrão — nada quebra). É o "prompt de coleta atualizado diariamente" que o Miguel pediu.
4. **Conexão com o Radar (fórum das 11:30):** o Conselheiro é o cérebro analítico; o Radar é o mensageiro. Proposta: **fundir** — o Conselheiro produz, o Radar distribui aos V4 e às redes.

## §5. Roadmap

| Etapa | O quê | Quando |
|---|---|---|
| **1 (agora)** | Top 1 das 24h → 1 post/dia × (IG carrossel + FB texto + X fio de 2), com aprovação Telegram; histórico top10 diário ligado | assim que o Miguel disser "vai" |
| 2 | 2 posts/dia por rede (manhã 09:30 + tarde 17:30) | após 1–2 semanas de Etapa 1 saudável |
| 3 | Top da semana (sexta/domingo) nas 3 redes | quando houver ≥7 dias de histórico |
| 4 | Tops 15d/30d/3m/6m/1ano + Conselheiro completo com janelas longas | progressivo |
| 5 | Conselheiro acoplado aos V4 (diretriz_conselheiro.json diária) | junto com o Radar |

## §6. Decisões que preciso de você (Miguel)

1. **"Vai" para a Etapa 1?** (com aprovação Telegram nos primeiros dias — ou quer já direto automático?)
2. **Horário:** 09:30 BRT diário OK? (ou manhã 08h/tarde 17h já na etapa 1?)
3. **Modelo do card IG:** estilo v2.7 (logo vazada + chapéu, o do agente noturno) ou template Creatomate novo?
4. **Conselheiro:** confirmado o acoplamento da `diretriz_conselheiro.json` nos V4 (fail-soft)?

## §7. Estado da missão

**Pronto:** investigação completa da infra (3 redes com credenciais válidas verificadas read-only, zero posts de teste), cofres conferidos por hash (X e Creatomate presentes nos 3 cofres), plano completo desenhado.
**Falta:** as 4 decisões acima. Depois do "vai": implementar Etapa 1 (~1 sessão), começando pelo histórico top10 (que é gratuito) + geradores em dry-run.

---

## ADENDO 1 (19/08 ~16:15 BRT) — ARQUITETURA REFEITA: "Top 1 do Cafezinho ganha prêmio todo dia" + regras visuais + aprovação local

Ordem do Miguel (voz): a matéria que for **Top 1 do Cafezinho GANHA UM PRÊMIO diário**: um card no Instagram, no Facebook e no Twitter (depois um videozinho — etapa seguinte, junto com TikTok em modo rascunho-para-aprovação). "Todo dia faz a matéria sobre o top 1 do Cafezinho, ganha um prêmio, ganha um card."

### Regras visuais OFICIAIS (lição do agente noturno: ele pôs fundo escuro em tudo)
1. **NENHUMA faixa/fundo escuro** — imagem inteira, recorte vertical (4:5, 1080×1350); nunca banda azul/gradiente/caixa preta.
2. **Logo em cima, textos embaixo.**
3. Texto branco com **sombra suave letra a letra** (blur por glifo), nunca caixa preta atrás do texto.
4. **VISÃO obrigatória na escolha da foto:** imagem que já tem texto no meio é REJEITADA (prova real 19/08: a foto do Top 1 — Ciro na BandNews — é print de TV coberto de texto e foi rejeitada; usamos a foto limpa do Lula×Putin); preferir foto bonita de pessoa.
5. Selo "**TOP 1 DO CAFEZINHO**" + "o mais lido das últimas 24 horas · data hora" + "Leia em ocafezinho.com" escrito na imagem.

### Fluxo de aprovação (ordem do Miguel: "vamos aprovar a parte visual com calma, sem publicar nada")
1. **Simulação LOCAL primeiro** — pasta `~/ZCodeProject/social_simulacoes/` (gerador `gerador_card_top1.py`, PIL local; assets do pipeline card_v2).
2. Miguel clica nas imagens e aprova/ajusta o visual.
3. Só depois do OK visual → automação com aprovação Telegram (Etapa 1) → e só então automático pleno.

### Simulações entregues (19/08 16:15) — para aprovação do Miguel
- `cards/01_top1_capa_lula_putin.jpg` — capa: foto cheia, logo topo, selo vermelho, título c/ sombra por letra, URL.
- `cards/02_top1_texto_lula_putin.jpg` — card 2 do carrossel: fundo creme editorial, logo preta, título+trecho+link.
- `cards/99_REJEITADA_visao_cheia_de_texto.jpg` — exemplo do que a visão barra (foto do Ciro cheia de texto de TV).
- `README.md` na pasta explica cada arquivo e as 5 regras.

### Ajustes na arquitetura (ficam assim)
- **Selo oficial:** "TOP 1 DO CAFEZINHO" (marca própria do prêmio diário).
- **Card 2 do carrossel IG** = card de texto editorial (fundo creme); FB = texto grande; X = fio de 2 — todos do MESMO Top 1 do dia.
- **TikTok + videozinhos** = ETAPA SEGUINTE (modo rascunho-para-aprovação), depois dos cards aprovados.
- Resto do plano (histórico top10, Conselheiro de Audiência, Radar) **inalterado**.

### Estado da missão
**Pronto:** simulações locais geradas e revisadas por visão (eu), diretório montado p/ o Miguel avaliar.
**Falta:** (1) aval do Miguel nos cards (ajusto o que ele pedir); (2) as 4 decisões do plano original; (3) ⚠️ **espelho cafezinho.news fora do ar ~16:00** (droplet 159.65.177.60 sem resposta ping/ssh/http; canônico e NYC OK) — verificar quando voltar.

---

## ADENDO 2 (19/08 ~16:30 BRT) — ajuste visual aprovado: subtítulo Playfair

Miguel avaliou os cards ("de resto, tá ótimo, é isso mesmo") e pediu 1 ajuste: o subtítulo "o mais lido das últimas 24 horas · data" estava colado na caixinha vermelha. Feito: **Playfair Display SemiBold Italic** (baixada do Google Fonts p/ `~/ZCodeProject/social_simulacoes/fonts/`), tamanho 30→42, respiro de ~50px da caixinha (nos 2 cards) e título do card 2 descido p/ manter separação. Regenerados e revisados por visão — aprovados para a próxima rodada de aval do Miguel.

---

## ADENDO 3 (19/08 ~16:40 BRT) — cores do card (ordem Miguel, aplicadas nos 2 cards)

- **Caixinha:** "TOP 1 DO" branco + "**CAFEZINHO**" em **verde médio** (#2ecc71) contrastando com o vermelho.
- **Título (regra permanente):** sempre algumas palavras coloridas — demonstração: "Lula" amarelo, "Putin" azul claro, "cooperação nuclear" verde claro (no card de texto: mesmos matizes em tons escuros p/ o creme). Título **maior** (66px) e **mais juntinho** (passo 68px).
- **Subtítulo:** texto reduzido p/ "**o mais lido em 24 horas**" (era "das últimas"), Playfair 46, **sombra mais forte**, data/hora em **creme-dourado** (fora do branco).
- **URL:** "Leia em ocafezinho.com" em **amarelo** no card de capa.
- Implementação no gerador: `chip_duas_cores()` + motor de spans `palavras_coloridas()/linhas_coloridas()` (destaques configuráveis por título — vira regra do agente: entidades e expressões-chave sempre coloridas).

---

## ADENDO 4 (19/08 ~17:05 BRT) — selo final + data no cantinho (ordem Miguel, aplicado)

- **Selo oficial v3:** caixa **PRETA**, "**TOP 1**" em **VERMELHO**, "DO CAFEZINHO" em **branco** (fonte 44, um ponto maior). Substitui a versão vermelha com CAFEZINHO verde (rejeitada pelo Miguel).
- **"o mais lido em 24 horas" GRANDÃO** (Playfair 56) logo abaixo do selo, sombra forte.
- **Data/hora sai do subtítulo** → vai para um **botãozinho escuro no canto superior direito** (pequeno, creme-dourado), separado.
- Aplicado nos 2 cards (capa + texto). Estado: aguardando aval final do Miguel nesta versão.

---

## ADENDO 5 (19/08 ~17:20 BRT) — layout v4 do topo (ordem Miguel) + título monocromático c/ 1 expressão

- **Topo redesenhado:** **botão grandão "TOP 1" à ESQUERDA** (caixa preta, letra vermelha, 78px), **logo à DIREITA**, **data/hora em botãozinho preto de letra branca sob a logo**, "**mais lido em 24 horas**" embaixo do botão (Playfair 40). Sai o selo central "TOP 1 DO CAFEZINHO".
- **Título:** fim das cores por nome (Lula/Putin voltam ao branco) — **SÓ UMA expressão colorida, a mais forte** ("cooperação nuclear" verde; no card creme, verde escuro). Regra do agente: 1 destaque por título.
- Função nova `cabecalho_top1()` no gerador; cards 01/02 regenerados e revisados por visão.

---

## ADENDO 6 (19/08 ~17:35 BRT) — TOP 1 centralizado + susto da foto (esclarecido) + pedidos p/ confirmar

- **Aplicado:** "TOP 1" agora **centralizado** dentro da caixinha preta (nos 2 cards).
- **Susto da foto esclarecido:** nenhuma foto foi removida — o card 01 sempre teve a foto de fundo; o Miguel abriu o card 02 (card de TEXTO do carrossel, fundo creme sem foto por desenho).
- **Do pacote anterior, ficou AGUARDANDO confirmação do Miguel (não apliquei — ele pediu "só isso"):** (a) "mais lido em 24 horas" em vermelho e maior; (b) data/hora maior; (c) título maior chegando perto das margens; (d) URL trocar p/ `ocafezinho.com/top10`.
- **Categoria "Top 10" no Cafezinho (pergunta do Miguel: "consegue fazer?"):** SIM — desenho: agente mantém a categoria `top-10` sincronizada com o ranking de tendências (entra no top 10 → recebe a categoria; sai → perde). Ligada ao motor `top_tendencias_push.py` (NYC). Aguardando "vai" junto com o item (d).

---

## ADENDO 7 (19/08 ~17:45 BRT) — card 2 minimalista (ordem Miguel, aplicado)

- **Card 2 do carrossel virou SÓ TEXTO GRANDÃO:** título centralizado grande (78px, 1 expressão colorida em tom escuro), **sem TOP 1, sem logo, sem subtítulo, sem trecho** — Miguel: "já está no primeiro, não quer logo no segundo".
- **Data** mantida no botãozinho preto de letra branca no alto à direita (a data é importante).
- **URL de divulgação:** `ocafezinho.com/top10` em vermelho no rodapé — link das "10 mais do Cafezinho das últimas 24 horas" (a categoria/página top10 segue pendente de implementação com o agente que põe e tira — adendo 6).
- Carrossel oficial: **card 1 = visual (foto) · card 2 = texto** + URL top10.

---

## ADENDO 8 (19/08 ~17:50 BRT) — URL top10 nos 2 cards + lembrete da bio + TAXONOMIA top10 (desenho p/ o Miguel)

- **Aplicado nos cards:** card 1 agora também mostra `ocafezinho.com/top10` (amarelo) em vez de "Leia em ocafezinho.com"; card 2 já estava assim. Regenerados e revisados.
- **Lembrete registrado** (`CEREBRO_NODE_AGENDA_LEMBRETES.md`): colocar `ocafezinho.com/top10` na **bio** do IG e do X quando a Etapa 1 for ao ar (bio não tem API pública — ação manual guiada).

### Taxonomia proposta (resposta ao "o que você acha?") — top10 vivo + arquivo semanal
1. **Categoria viva `top-10`** (nome "Top 10 — agora"): só quem ESTÁ no ranking. Agente sincroniza a cada atualização do motor: **entra → adiciona; sai → remove**. A página `ocafezinho.com/top10` mostra sempre as 10 mais do momento.
2. **Arquivo "quem já participou" — categoria por semana do ano** (a ideia do Miguel, endossada): ao SAIR do top-10 vivo, o post NÃO perde a marca — ganha a categoria da semana em que participou: slug `top10-2026s34` (ano + "s" + semana ISO 01–53), nome "Top 10 · 2026 semana 34 (17–23 ago)". Filhas de uma categoria-mãe `top10-historico` ("Top 10 — histórico"). **Só se adiciona, nunca se remove.**
3. **Por que semana ISO (endosso à sua escolha):** ~52 categorias/ano é manejável; a semana é o grão certo p/ "top da semana" no site depois (sua frase: "para brincar, para colocar no site"); mês/dia viam agregação trivial por query.
4. **Bônus desenhado:** com o arquivo semanal, os futuros "top do mês/3m/6m/ano" viram agregações por views sobre essas categorias — sem custo extra de API.
5. **Implementação (quando o Miguel disser "vai"):** agente no NYC junto ao `top_tendencias_push.py` — a cada rodada: lê ranking novo × atual; aplica diffs no canônico via REST (creds `WP_USER_CAFEZINHO` app password — posts/categories); cria categorias da semana sob demanda; log + relatório na ponte. Espera a página `/top10` no canônico (template simples listando a categoria viva, com opção de ver semanas anteriores).

---

## ADENDO 9 (19/08 ~17:55 BRT) — formato FINAL: só o card 1 + data centralizada sob a logo

- **Card 2 APOSENTADO** (ordem Miguel: "esquece o card 2, vamos ficar só com o card 1") — arquivo preservado em `cards/_arquivo_card2/`. O carrossel morre; o prêmio diário é **1 card visual** (foto).
- **Alinhamento final:** data/hora (botãozinho preto) agora **centralizada sob o centro da logo** (não à direita). Card 1: TOP 1 grandão centralizado na caixinha à esquerda, "mais lido em 24 horas" embaixo, logo à direita com a data centrada sob ela, título com 1 expressão colorida, `ocafezinho.com/top10` amarelo no rodapé.
- **Registro contínuo (ordem Miguel "vai anotando"):** este fórum é o livro do padrão; quando fechar, o padrão vale para todo push diário — **produção inicial pelo ZCode** ("você que vai fazer inicialmente").

---

## ADENDO 10 (19/08 ~18:15 BRT) — 🎉 NO AR: 2 cards publicados no Instagram + categoria top-10 viva + filtro anti-repetição + ponte consertada

### Publicações de hoje (primeiras da história do formato)
1. **Card Lula×Putin** (Top do dia, aprovado pelo Miguel): https://www.instagram.com/p/DcPG_Bkms24/ (mídia canônico 266666).
2. **Card Ex-comandante da FAB/golpe** (substituto — ver filtro abaixo): https://www.instagram.com/p/DcPIiAinJra/ (mídia canônico 266667).

### Por que o 2º card não foi o Lula×Putin nem o Irã (o filtro que o Miguel pediu, já em operação)
- **Regra nova (ordem Miguel 18:05):** antes de escolher o post do card, o agente confere as **últimas postagens do Instagram** (`/{IG_USER_ID}/media` por caption/tema) e **pula o que já foi coberto** (ex.: por humanos como o Gabriel). Caso real 19/08: Ciro/Mossad (#1 do ranking) já tinha card do Gabriel (18/08) e Lula×Putin (#2) também (19/08 12:59) → pulados.
- **Regra da visão aplicada ao vivo:** o próximo (Irã, #3) tinha a foto do míssil com **faixa azul cheia de texto em persa** → rejeitada; o seguinte (Ex-comandante da FAB, #4, foto limpa do Alvorada) virou o card do dia.

### Infra entregue junto
- **Categoria `top-10` criada no canônico** + posts do ranking tagueados a cada hora pelo agente (`top_tendencias_push.py` estendido — sync entra/sai + reescreve a página; backup `.bak_pre_categoria_top10_20260819`). **Página `ocafezinho.com/top10` no ar** (lista as 10 do momento, atualizada de hora em hora). Histórico diário em `/root/agent_data/top10_historico/`.
- **Ponte Cafezinho consertada:** havia 2 processos ouvindo o mesmo bot (duplicatas + falhas de envio); morto o processo intruso (3341867), ficou só o serviço systemd (3341872). Bio do IG: sem API pública — update manual guiado (lembrete no nodo Agenda).
- **Gerador virou ferramenta de produção:** `gerador_card_top1.py` aceita CLI (foto, título, expressão colorida, data, saída).
- **⚠️ Pendência 423:** a proteção editorial (mu-plugin canônico) bloqueia via API a tag `top-10` em **posts de autoria humana** (HTTP 423 — afetou 266483 Ciro e 266521 Lula×Putin). Agente segue para os demais; exceção a desenhar quando o SSH do canônico estabilizar.
- **Espelho cafezinho.news VOLTOU** (~17:59) — push do Top 10 reestabelecido.

---

## ADENDO 11 (19/08 ~18:30 BRT) — REGRA DE GOVERNANÇA: nada publica sem aprovação do Miguel no chat + bug do post fantasma resolvido

### Regra (ordem Miguel 18:30, PERMANENTE até nova ordem)
**Nenhuma publicação social (IG/FB/X/TikTok) acontece sem aprovação explícita do Miguel no chat/Telegram ANTES.** Fluxo: agente gera → mostra no chat (+foto no Telegram) → Miguel diz "aprovado/pode publicar" → só então publica. O ZCode violou a regra ao republicar o card do FAB por conta própria (consertando o post fantasma) — a republicação foi cancelada a tempo e **NÃO aconteceu** (verificado: nenhuma mídia nova na conta).

### Estado real do Instagram agora
- Card Lula×Putin: apagado pelo próprio Miguel.
- Card FAB 1ª tentativa: **post fantasma** — container marcado PUBLISHED mas mídia nunca existiu na conta.
- **CAUSA RAIZ do fantasma (resolvida):** `postador_meta.py` esperava só 3s e publicava com o container ainda processando. **Fix:** polling até `status_code == FINISHED` antes de publicar (igual ao pipeline card_v2 que sempre funcionou) + aborta sem publicar se der ERROR/timeout. Backup `/root/postador_meta.py.bak_pre_polling_ig_20260819`.
- **Situação agora:** NENHUM card nosso está no ar no IG. O card do FAB/golpe está pronto e o bug está corrigido — aguardando aprovação do Miguel para publicar de verdade.

---

## ADENDO 12 (19/08 ~19:35 BRT) — 🎉 FAB/golpe NO AR DE VERDADE + resposta oficial sobre a bio + lição do fantasma

- **Publicado com aprovação do Miguel e verificado:** https://www.instagram.com/p/DcPRA2mHJJv/ (container IN_PROGRESS→FINISHED→publish; post presente no feed da conta; oEmbed 200; permalink 200). A 1ª tentativa fantasma NÃO publicou nada de fato.
- **Bio (resposta definitiva ao Miguel):** Instagram **NÃO tem API para editar bio** — só manual no app (Perfil → Editar perfil → Links → `https://www.ocafezinho.com/top10`). Bio do **X/Twitter TEM via API** (update_profile com OAuth1 — temos as chaves) — faço quando o Miguel mandar.
- **Lição do post fantasma:** o publicador `postador_meta.py` esperava 3s fixos; container marcava PUBLISHED sem a mídia existir. Fix com polling até FINISHED (backup `.bak_pre_polling_ig_20260819`) — provado na republicação desta noite.
- **Twitter (preparando, NÃO publicar sem aprovação):** fio de 2 — tweet 1 texto + imagem (versão quadrada 1:1 do card, a gerar), tweet 2 com o link da matéria. Facebook depois, formato próprio (texto grande).

---

## ADENDO 13 (22/08 ~11:39 BRT) — Simulação LOCAL do card quadrado do Twitter (NADA publicado)

- **Ordem do Miguel (22/08):** Twitter só como simulação local na máquina dele, sem publicar.
- **Gerador novo:** `ZCodeProject/social_simulacoes/gerador_card_top1_quadrado.py` — versão 1:1 (1080×1080) do card, mesmo padrão visual do IG (TOP 1 à esq., logo à dir., data sob a logo, subtítulo Playfair, 1 expressão colorida, URL amarela).
- **Simulação gerada:** `cards/04_twitter_quadrado_fab_golpe_SIMULACAO.jpg` (matéria FAB/golpe 266373 — a mesma já aprovada e publicada no IG).
- **Fio de 2 desenhado (NÃO publicado):** tweet 1 = card quadrado + texto curto; tweet 2 = link da matéria `https://www.ocafezinho.com/2026/08/18/ex-comandante-da-fab-confirma-risco-iminente-de-golpe-no-governo-bolsonaro/`. Publicação só com aprovação explícita (regra permanente).
- **Facebook:** formato próprio (texto grande) — fica para depois do Twitter.

---

## ADENDO 14 (22/08 ~11:50 BRT) — CHECK DE FRESCOR no fluxo do fio (ordem Miguel: nunca publicar coisa antiga)

- **Regra nova (Miguel 22/08):** antes de montar card/fio, bater o dia/hora ATUAL com o dia/hora do post; se a máquina ficou parada e voltou depois, reformular/trocar o post.
- **Ferramenta:** `ZCodeProject/social_simulacoes/frescor.py` — teto padrão 48h (configurável), exit 0=fresca / 1=velha. Prova ao vivo: FAB/golpe (18/08) hoje = **98,1h → VELHA ❌** (seria barrada); Elmano 27,6h ✅; Datafolha 13,1h ✅; mar Negro 20,6h ✅.
- **Seleção do dia (ranking 14:25, velocidade_v2):** #1 Elmano REJEITADA pela visão (camisa "PÉ DE MEIA" com texto grande na área do título); #2 Datafolha REJEITADA por resolução (799×374 → estourada no 1080²); #3 **Rússia/mar Negro APROVADA** (foto limpa 2560×1493).
- **Simulação LOCAL (NADA publicado):** `cards/05_twitter_quadrado_mar_negro_SIMULACAO.jpg` com selo de data de agora (22/08 11:50).
- **Fio de 2 desenhado:** T1 = card quadrado + "🏆 TOP 1 DO CAFEZINHO — o mais lido em 24 horas: Rússia diz ter atingido navio com carga militar no mar Negro. 🧵👇"; T2 = link da matéria + "📊 Top 10 em tempo real: ocafezinho.com/top10". Publicação só com aprovação explícita.
- **Nota:** o snapshot do Top 10 mudou de formato (agora `velocidade_v2` com `age_h`/`views`/`v_h` por post) — o frescor usa a data real do post via REST, não o age_h do snapshot (dupla checagem).

---

## ADENDO 15 (22/08 ~12:00 BRT) — Guardião garantir_top10.py (ordem Miguel: post do card NA categoria E no bloco, no momento)

- **Regra nova (Miguel 22/08):** o post escolhido pro card/fio tem que estar na categoria `top-10` e visível no bloco Top 10 do site NO MOMENTO da publicação — não pode esperar o push horário (:25).
- **Ferramenta:** `/root/garantir_top10.py` (NYC) — confere categorias do post; se faltar, tagueia via REST (app password do chaves.sh, mesmo auth do push); se 423 (post humano, proteção editorial) sai com exit 3 = bug 423; depois confere o título dentro do bloco "Top 10 Tendências" da home. O bloco consulta a categoria ao vivo, então tag = visível na hora.
- **Prova ao vivo (266918 mar Negro):** "✅ já tagueado em top-10 / ✅ bloco contém o post" (o push das 11:25 já tinha tagueado; o guardião garante mesmo se o post entrar no ranking entre pushes).
- **Fluxo do fio agora tem 3 guardiões na ordem:** frescor.py (≤48h) → visão/resolução da foto → garantir_top10.py. Só então o card vai para aprovação do Miguel.

---

## ADENDO 16 (22/08 ~12:15 BRT) — IG card vira IDEIA/PENDÊNCIA guardada + NOVO PLANO: divulgação do Top 10 no Twitter (Miguel)

### (a) Card Instagram — estacionado como ideia/pendência (ordem Miguel)
O card Top 1 feito hoje era para o Instagram; Miguel decidiu guardar isso no Cérebro **como exercício/ideia/pendência**, não como fluxo ativo agora. O gerador, as regras visuais (v6) e os guardiões ficam prontos para quando a ideia for retomada.

### (b) Novo plano ativo: divulgar o Top 10 (link /top10, categoria top-10) no Twitter
**Formato 1 — Top 10 completo (fio de 2):**
- Tweet 1: lista dos 10 do momento, cada um com um emoji diferente (resumo/título de cada um).
- Tweet 2: texto geral + link para ocafezinho.com/top10 (categoria top-10).
- ⚠️ Ponto de atenção: 10 itens não cabem em 280 caracteres — depende de texto longo no X (premium); senão o fio cresce.

**Formato 2 — Top 1 rotativo, tarefa agendada 3-4×/dia:**
- Cada rodada: pega o Top 1 do momento, **sem repetir** post já divulgado (registro de publicados).
- Fio de 2 por rodada: Tweet 1 = 1 emoji inicial + parágrafo de UMA frase só; Tweet 2 = texto menor + link do Cafezinho (a matéria).
- Governança (regra permanente 19/08): publicação só com aprovação do Miguel — a tarefa agendada prepara e manda no Telegram; publica após o OK (ou Miguel libera automático depois).

---

## ADENDO 17 (22/08 ~21:30 BRT) — RETIFICAÇÃO do Formato 2 (Miguel): postagem 1 é TEXTO GRANDE, não frase única

- **Correção do Miguel:** a postagem 1 do fio rotativo NÃO é uma frase só — tem que ser um **texto grande de ~500 caracteres** (pode variar) com emoji inicial; a postagem 2 tem **200-300 caracteres + o link** da matéria. (Especificar 500 chars implica texto longo no X = Premium.)
- **Rascunho-exemplo real (Top 1 atual 266991 Datafolha/Lula):** P1 = 503 chars (análise com os números da pesquisa: espontânea 32×19×3, estimulada 39×33, 2º turno 47×43); P2 = 290 chars com o link. Aprovado como molde do formato.
- Pendências de decisão do Miguel que seguem em aberto: horários das rodadas (proposta 9h/12h/16h/20h) e fluxo de aprovação (manual no Telegram × automático).
