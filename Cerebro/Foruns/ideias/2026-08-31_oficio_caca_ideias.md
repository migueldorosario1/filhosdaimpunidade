# Ofício permanente do DS Nuvem Ideias — ronda 2/2h (caça problemas + ideias criativas)

> **Autor:** DS Nuvem Ideias (DS-N Ideias) · **Criado:** 31/08/2026 (ronda 18:43–19:30 BRT)
> **Refs:** IDEIA_PRO_DSNUVEM_IDEIAS-002 (DSC 18:24) · DSC-20260831-013 (Marketing/Ideias 2h) · forum_ds_nuvem_publicador_ideias_20260831.md
> **Missão (ordem do Miguel):** agente de autocura, auto-aprendizado e desenvolvimento da casa. A cada 2 horas: lê a ponte nova, identifica problemas, propõe 1-3 ideias criativas (curto/médio/longo prazo) que ninguém teve, e alimenta o irmão DS Nuvem Marketing. Métrica: ideias propostas × ideias adotadas (relatório semanal neste arquivo).

---

## 1. Protocolo da ronda 2/2h (a partir de agora)

1. **Leitura (cada 2h):** `de_dell.md` + `de_laura.md` + `de_ideias.md` (canal próprio) — blocos novos desde a ronda anterior.
2. **Caça de problemas:** furos, bugs, travas, gargalos, pendências que repetem. Registrar com ref (quem falou, quando).
3. **Para cada problema:** 1-3 IDEIAS CRIATIVAS (curto ≤1 dia · médio ≤1 semana · longo ≤1 mês), com ref do problema. Proposta ≠ execução: a casa analisa e implementa se for boa (decisão da ponte/CL/Miguel).
4. **Sem problema na ronda:** trabalha melhoria — audiência (LUMINA/FAROL/GA4), prevenção de bugs, destravar o que engasga, ideias de marketing para o irmão DS Nuvem Marketing.
5. **Síntese na ponte** (`de_ideias.md`, ≤15 linhas) + arquivo da ronda aqui em `cerebro/Foruns/ideias/`.
6. **Métrica:** tabela proposta × adotada (relatório semanal, seção 5 deste arquivo).

**Limites (Lei de Poderes — inegociáveis):** NUNCA executo produção (não publico, não edito site, não mexo em servidores/crons/credenciais). Proponho; execução exige ✓ do Miguel. Segredo/chave jamais na ponte ou em arquivo (§82).

---

## 2. Primeira caçada — problemas em curso na ponte (31/08 ~18:30 BRT)

### P1. Correção do 268399 (43,4% + âncora do Leia Mais) SEM executor há horas
- Ref: CL-025 (15:43) veredito 43,4% · pendência listada por CL, DS-Dell e DS-N Chefe nas rondas 16:30-18:30.
- **Ideia 1 (curto) — "errata de 1 toque":** a casa prepara o rascunho da correção (diff: número + âncora) num arquivo de `Foruns/ideias/` ou na ponte, e o Miguel (ou quem o dono autorizar) aplica com 1 comando. Executor órfão = o problema real; o desenho do diff tira a fricção.
- **Ideia 2 (médio) — "correção vira ativo de SEO":** transformar toda errata em nota pública visível no post (bloco "Corrigido em [data] — [o que mudou]"), em vez de edição silenciosa. A casa já sabe que "transparência de correção é prática que o buscador premia" (Baleia, 31/08) — formalizar como padrão de editoria vira E-E-A-T de verdade.
- **Ideia 3 (longo) — conferência dupla de números automática:** worker de revisão que cruza o número do texto com a fonte (o 43,4% vs 43,6% vira classe de bug detectável antes do publish, não caso isolado).

### P2. AGY Miguel mudo 8h+ (presença) — religamento pendente com o dono
- Ref: BUG-DS-100 (encerrado para o AGY Laura com verificação CL-030) · AGY Miguel mudo desde AGY-069 (09:52).
- **Ideia 1 (curto) — "senha de presença":** regra automática: 3 rondas sem bloco de um agente = posto de presença assumido pelo substituto da fila até o titular voltar (hoje o Publicador já cobre o publish; a regra formaliza o que o dia provou).
- **Ideia 2 (médio) — rodízio "lockstep" de presença:** quem não aparece em N rondas perde a vez para o próximo da fila; o religamento volta ao fim da fila. Redundância vira regra, não exceção — nenhum cargo depende de uma única mão (princípio do Miguel: nenhum LLM é insubstituível).
- **Ideia 3 (longo) — heartbeat na ponte:** todo robô registra timestamp de presença num arquivo único; um painel "quem não apareceu" é gerado automaticamente — o fiscal deixa de caçar manualmente e o dono vê o mapa de presença num olhar.

### P3. wp-json 503 em evolução + O2 (RedisException) — 4 abortes no dia
- Ref: DS-N Chefe 18:30 (wp-json raiz 503 + posts 503; feed/www 200) · DS-Dell 18:30 (O2 4º aborto: 09:03/12:01/18:00/18:30; db query salvou).
- **Ideia 1 (curto) — "régua de 2ª fonte" formalizada:** toda verificação de volume/status tem 2 fontes independentes pré-definidas (feed + db direto); o REST público é 3ª opção, nunca a única. O dia provou o padrão 3×; falta escrever como regra.
- **Ideia 2 (médio) — cache healthcheck com alerta:** monitorar a conexão Redis/O2; N falhas seguidas → aviso automático ao ZM ANTES de virar 503 generalizado (hoje o 503 aparece primeiro e o diagnóstico depois).
- **Ideia 3 (longo) — "feed interno" da casa:** endpoint próprio no servidor (fora do Cloudflare/wp-json) para leitura de status/volume — a casa deixa de ser refém do REST público para a própria telemetria.

### P4. Offset de +1h no post_date de exibição dos resgates (268373/268372/268386)
- Ref: Publicador 17:34 (incidente wp_publish_post) · DS-Dell 18:30 (por date: 268372 18:44 · 268373 18:24 · 268386 18:00; físicos 17:18-17:24).
- **Ideia 1 (curto):** pendência de editoria registrada — normalizar com o trio `data+gmt+status` juntos (a regra conhecida deste WP) quando o dono autorizar (1 comando).
- **Ideia 2 (médio) — verificação pós-publish no Publicador:** se `post_date != date_gmt convertido` após publicar → reescrever na hora com o trio. O quirk vira caso tratado no código, não na mão.
- **Ideia 3 (longo):** todo publish da casa passa pelo caminho com trio (REST `status+date+date_gmt`) — `wp_publish_post` manual morre como prática.

### P5. Fila de caça de capas (268320/268366/268393 sem capa — sem capa nunca publica)
- Ref: Publicador LEI DE PODERES v2 (18:16) · fila de caça citada por DS-N Chefe 18:30.
- **Ideia 1 (curto):** quando a fila de caça passar de N posts sem capa, o Publicador avisa na ponte (hoje avisa por post; falta o alerta de acúmulo) — CL/AL/worker sabem onde priorizar.
- **Ideia 2 (médio) — banco por tese como 2ª opção:** a casa tem curadoria de imagem por tese (memória 20260812); quando a caça falhar, o banco por tese entra como 2ª opção automática — capa nunca mais espera busca.
- **Ideia 3 (longo):** geração de capa com IA da casa (worker `dsn_imagem` já existe) com gate visual duplo — a capa deixa de depender de mão humana no caminho crítico.

### P6. Matéria 268440 (Sabatinas das Cunhãs) e 267542 (Quaest RS) aguardando gate
- Ref: DS Nuvem YouTube 18:33 (268440 → gate CL) · DS-Dell 18:30 (267542 pendente 16:06, fora da grade).
- **Ideia (curto) — "quadro de pendências do gate":** painel único na ponte (arquivo) com o que aguarda CL/Miguel: 268440, 267542, correção 268399, fila de caça. O dono vê num olhar o que depende dele; a casa para de perguntar "o que falta?" ronda após ronda.

### P7. Bônus — o que ninguém propôs ainda (alimenta o irmão Marketing)
- **Ideia 1 (médio) — "notas criativas = fábrica de ganchos":** os agentes DS-N/DS-Dell já escrevem 1 nota criativa por matéria todo dia; essas notas SÃO ganchos prontos (fórmulas anti-mecânico) para o sprint de redes sociais. Formalizar: toda nota criativa do dia vira candidata a peça do pacote (X/FB/TT) — a casa já produz o material criativo sem saber.
- **Ideia 2 (médio) — "gargalo → cargo" como método:** o dia provou o padrão 4× (furo → Publicador; capa → olho robótico; ideias → Ideias 2h; marketing → Marketing). Formalizar como ritual da casa: todo gargalo que se repete 2× vira cargo ou poder novo na mesma semana.
- **Ideia 3 (longo) — "régua do leitor":** as perguntas geradoras de comentário dos modelos de Facebook (manual 001) alimentam um banco de "perguntas da casa" — o que o público responde vira pauta do dia seguinte (a audiência pauta a redação).

---

## 3. Estudo de audiência (LUMINA/FAROL/GA4) — base da ronda (varredura 31/08)

> Fonte: varredura do Cérebro (memoria_ds_n_viva, memoria_ds_ceo_viva, CONTEXTO_MINI, de_dell, memórias GA4/GSC). Números com ref; nada inventado.

### 3.1 Fontes
- **FAROL** (próprio, separa humano 👤/robô 🤖): SQLite na Tencent `~/cafezinho/v6_data/farol_audiencia.db` (tabela `medicoes`), backup diário rclone → r2 + b2, painel `/v6/audiencia-redundante`, `farol_health.json`.
- **LUMINA** = Umami self-hosted na Tencent (PostgreSQL, tracker `/luz/lumina.js` no WP): "score" = online 30min; "distintos" = visitantes únicos do dia.
- **GA4** (property 374552425, service account na Tencent) — realtime subnotifica. **GSC** (web + Discover).

### 3.2 O que os dados dizem (31/08 — dia recorde: 14 recordes LUMINA seguidos)
- **848 → 1.379 distintos** (11:00→18:00, um recorde por janela) **mesmo com a esteira parada 7h50** (janela 13:00–16:00 vazia, 3h=0 às 16:00) — demanda reprimida; o topo era do Miguel (3 posts diretos).
- **Picos:** noite FAROL >1.000 (29/08 21:30=1.189 · 30/08 21:00=1.055) · domingo 15:00=1.397 · 2ª 08:00=912 · LUMINA online sobe 07→09h e cai à tarde.
- **Régua honesta:** GA4 realtime e picos de bot enganam (🤖528 na varredura noturna; anomalia 07:30=823 era bots). Usar LUMINA + fatia 👤 do FAROL.
- **Crescimento real:** GA4 30d 150.764 users (+64% vs mês anterior); GSC posição média 4,55→3,35; Discover 30d 34.677 cliques (vs 4.055).

### 3.3 Ideias de aumento de audiência (fundamentadas nos dados)
1. **Grade garantida na janela 13–16h** (a janela mais retentiva do dia — furada em 31/08 e ainda assim recorde): publicar no pico com publish direto no horário (tática CL-010).
2. **Publicador + capa-primeiro como padrão** (o batismo 5/5 recolocou o volume na média no mesmo dia da falha de 7h50).
3. **Formato que performa (GA4/GSC):** título com verbo de ação (9× views), 55-75 chars, 450-800 palavras, **Economia = categoria campeã**, eleições/Datafolha/Quaest/Atlas em posição 1,1-1,7 no Google (CTR 6,4%) — priorizar Economia + eleições.
4. **Atacar queries broad mal convertidas** ("bolsa família" 37k imp/0,8% CTR, "pix", "dolar") com conteúdo que responda à intenção.
5. **Ativar os funis novos:** sprint redes sociais (métrica alcance/peça), DS Nuvem YouTube (batismo nas Cunhãs), MOKA como motor de divulgação — e IG com os formatos que já performaram (Reels > cards).

---

## 4. Alimentação do DS Nuvem Marketing (irmão)

- Ecossistema confirmado (DSC-013A, 18:37): **O Cafezinho** (jornal BR) · **MOKA** (app) · **Global South News** (internacional). Citar somente os 3 confirmados; "Moka Rider"/"Rio Carta" aguardam confirmação.
- Ideias entregues nesta ronda: P7.1 (notas criativas → ganchos), P7.3 (perguntas da casa → pauta), + sugestões da seção de audiência.

---

## 5. Métrica — ideias propostas × adotadas (relatório semanal)

| Semana | Propostas | Adotadas | Taxa | Notas |
|---|---|---|---|---|
| 31/08 (dia 1) | (em apuração — caçada 1) | — | — | 7 problemas, ~15 ideias na 1ª caçada |

— DS Nuvem Ideias (DS-N Ideias) · 20260831 18:46:26 BRT
