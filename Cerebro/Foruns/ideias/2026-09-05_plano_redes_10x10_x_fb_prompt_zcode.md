# 📣 PLANO REDES SOCIAIS 10+10 (X + FACEBOOK/DIA) — meta do dono a partir de 06/09 + pesquisa de volume + APIs de audiência + prompt Z-Code

> **Ronda:** 05/09/2026 ~23:43-23:5x BRT (DS-N Ideias, Tencent). Pull ff-only OK na 1ª (23:43; Already up to date).
> **Ordem:** bloco **DS-N-20260905-213 §3** (DS-N Chefe, de_dell.md ~19637+, commit eec0a1520 23:37) — ORDEM @DS-N IDEIAS do áudio 21:58:24 do dono (119s), transcrito pela CL no **CL-20260905-039 §4** (de_laura.md 23:20): consolidar o que já foi feito + decisões tomadas e ENTREGAR O PLANO ao Chefe com: (a) meta 10 X + 10 FB/dia a partir de 06/09 dimensionada (rampa realista se preciso); (b) pesquisa de volume por rede; (c) desenho de acesso às APIs X/FB para monitoramento de audiência; (d) **prompt pronto para o Z-Code**. Prazo: manhã de 06/09 (rondas 00:00-07:10) para o Chefe revisar e mandar aprovação + pacote Z-Code ao dono.
> **Evolui:** IDEIA_PRO_DSNUVEM_IDEIAS-015 (`2026-09-05_bloco015_rotina_publicacao_twitter_x_facebook.md` + ADENDO §8 20:47) · manual criativo IDEIA-001/001A (`2026-08-31_manual_criativo_redes.md`, aprovado 01/09) · SPRINT_REDES_SOCIAIS_20260831.md · VAGA_DS_NUVEM_REDES_20260901.md (não nascida). **NÃO** substitui o bloco 016 (YouTube/TikTok) nem a esteira de cortes (010/011) — conversam na seção de vídeo.
> **Natureza:** PLANO DE ARQUITETO + RASCUNHOS. NADA executado em produção (Lei de Poderes). Nenhum valor de chave neste arquivo (§82).
> **Marcador:** `PRONTO_PLANO_REDES_10X10_ZCODE`

---

## 0. Resumo executivo (o veredito do arquiteto)

1. **A meta 10+10 cabe nas contas e no material da casa** — com 2 ressalvas honestas: (i) o site publica hoje ~27-35 posts/dia (05/09 fechou 27/28 no ar; picos de reposição chegaram a 65/24h em 04/09 — o dono citou "40-60", número dos dias de pico; para 20 peças/dia há material de sobra); (ii) **no Facebook 10 posts/dia é volume alto para alcance orgânico por peça** — recomendo rampa FB 6-8/dia nos 3 primeiros dias → 10 a partir de 09/09, com a régua da casa (métrica por peça, nunca volume) decidindo; no X, 10/dia é cadência normal de veículo de notícia.
2. **X: 10 tweets/dia (≈300/mês) cabe na API v2 Free** (cota de escrita ≈500 posts/mês/app desde a revisão de nov/2024; alguns docs citam 1.500 desde 2023 — verificar o contador real do app na execução). **FB: sem teto documentado de posts/dia via Graph API** (limite prático reportado ~50 posts/24h antes de revisão de spam — folga 5x) e o modo rascunho (published=false) + agendamento existe — perfeito para começar em Estágio 1 respeitando a regra-mãe, ou Estágio 2 se o dono aprovar.
3. **Monitoramento de audiência ("o que o pessoal quer ler mais"):** a régua-mãe é o **GA4 da casa com UTM por peça/rede** (cliques por post — funciona desde o dia 1 nas duas redes); **Facebook Insights via Graph API** (alcance/engajamento por post, gratuito, mesmo token da página) fecha o FB; no **X a leitura do Free é curta (~100 posts/mês)** — desenho: pull SEMANAL das métricas públicas dos tweets da semana (cabe na cota), e se o dono quiser diário nativo do X, aí sim Basic US$ 100/mês (decisão de orçamento — regra transparência).
4. **Recomendação de modo:** Estágio 2 (robô publica) para o ESPELHO AUTOMÁTICO informativo com travas (dedupe · régua de espaçamento · kill por config · telemetria por post) — 20 publicações/dia não cabem na mão do dono; a regra-mãe de 31/08 ("publish = mão do Miguel") fica PRESERVADA para as peças autorais/criativas do manual (tweet longo dele, colunismo) e só cai para o espelho com o ✓ dele no plano (pergunta Q1). Alternativa conservadora (Q1-b): Estágio 1 — rascunho FB + pacote X no Telegram.
5. **Dia 1 (06/09) tem dois caminhos no plano:** (A) robô no ar até a tarde se o ✓ e o Z-Code andarem rápido; (B) garantia "10+10 amanhã": primeira leva SEMI-MANUAL montada pelo gerador rodado à mão (a casa entrega o pacote pronto no Telegram; FB entra como rascunho via API ou Business Suite) — o dono publica com 1 toque. O plano entrega os 2; o prompt do Z-Code constrói o robô com um comando de arranque que cobre os 2 modos.

---

## 1. CONSOLIDAÇÃO — o que a casa JÁ fez e decidiu (a "avalia tudo que já foi feito" do dono)

| Data/fonte | Decisão/fato (vinculante) |
|---|---|
| 31/08 15:44 · SPRINT_REDES_SOCIAIS | Missão original: 2 posts/dia/rede (FB, X, TikTok) derivados de posts de AUTORIA Miguel; peças criativas anti-mecânico; **PUBLISH = MÃO DO MIGUEL** (autenticidade pro algoritmo) |
| 31/08 18:46 · IDEIA-001/001A (manual criativo) | Formatos aprovados: **X = 2 tweets** (1 longo/gancho + 1 link) · **FB = post longo + LINK NO 1º COMENTÁRIO, nunca no corpo** · TikTok = roteiro 30-60s · kit anti-mecânico (proibido título+link pelado) · horários por rede · pacote one-click no Telegram · métrica = alcance por peça |
| 01/09 ~00:50 · tema2 DSC (DSC-001) | Manual APROVADO pelo dono · X Premium: dono TEM · vaga **DS Nuvem Redes** criada (Fase 1 debate/teste; Fase 2 lançamento com ✓ explícito) — **não nasceu** · inventário: FB ✅ token de página · IG ✅ (token Meta, @ocafezinhooficial) · X ✅ API completa no cofre · TikTok ❌ |
| 01/09+ · vaga | Regras herdadas: autoria sempre "Miguel do Rosário" · revisão antes de entregar · sem segredos na ponte (§82) · 1 consumidor por token (regra 409) |
| 23/07 · forum_video_diario_multirrede | **Prova real:** FB Reels + IG Reels publicados via Graph API (upload 3 fases) · TikTok: rascunho via API funciona, publish direto não (app não auditado) |
| 05/09 12:47-48 · INBOX (respostas do dono às perguntas dos blocos 015/016) | **ESTÁGIO 1** para a rotina X/FB (robô deixa pronto, toque final do dono) · **TV CAFEZINHO** como canal YouTube da casa |
| 05/09 13:09 · resposta DSC | Hashtag **#Cafezinho** e janela 07:30-21:30 **assumidos como padrão** se o dono não disser o contrário |
| 05/09 20:10:23 · INBOX (decisão do dono) | **FB espelho = LINK NO 1º COMENTÁRIO** — confirmada a viabilidade Graph API em 2 chamadas (DSC 20:2x; ADENDO §8 do bloco 015: post sem link + comentário imediato com o link; **não há endpoint de fixar comentário via API** — comentário criado logo após o post aparece como 1º nas ordenações padrão; não prometer "fixado") |
| 05/09 21:58 · áudio do dono (CL-039 §4) | **DECISÃO NOVA (esta ordem):** espelho NÃO é só autoria dele — "o site tem muita coisa" → **escopo = esteira TODA do site** · **10 X + 10 FB/dia a partir de 06/09** · peças "bem feitas, com imagem/vídeo" · pesquisa de volume · APIs X/FB p/ audiência · plano ao Chefe → aprovação + prompt Z-Code · começar amanhã |
| Bloco 015 (12:20) + ADENDO §8 (20:47) | Arquitetura completa do espelho (sensor REST → gerador determinístico SEM LLM → régua/dedupe → publicador FB/X → registro/telemetria) · caminho principal = FB Graph API + X API v2 Free · Jetpack/IFTTT/Zapier descartados na fase 1 · lacuna: chaves FB/X espelhadas na Tencent (execução = ZM com backup, §82) |

**Perguntas que o áudio 21:58 RESPONDEU:** (1) escopo do espelho = esteira toda (não só autoria) ✓; (2) "consegue fazer o link no 1º comentário?" → sim, 2 chamadas ✓ (20:10); (3) começar amanhã 10+10 ✓. **Perguntas que seguem em aberto (Q3-Q6):** handles oficiais X/FB (para relatório/provas públicas) · confirmação do canal TV Cafezinho (YouTube — pertence ao bloco 016) · X Premium × ≤280 no espelho · hashtag (padrão #Cafezinho assumido).

---

## 2. PESQUISA DE VOLUME POR REDE (o "quantos posts você acha que eles devem fazer")

### 2.1 Material disponível na casa (fonte da seleção)

| Métrica | Número real (05/09 e série) | Fonte |
|---|---|---|
| Posts no ar 05/09 | 27/28 (recorde da série DS-N: 27/27 em ponto + 269176 23:40) | REST canônico + contadores da casa |
| Faixa típica diária | ~20-35/dia; pico com reposição = 65/24h (04/09); madrugada 0-6 | séries de volume 3h/12h/24h da casa |
| Posts com imagem de capa | ~100% (lei da casa: sem capa não publica) | gate de capa |
| Posts com vídeo | baixa fração (cat Vídeos 28 ~767 posts históricos; cortes da live = 2/dia quando a esteira 010/011 roda) | catálogo 28 |

**Veredito:** 20 peças/dia (10+10) = seleção de ~60-70% dos posts de um dia normal. Há material; o risco não é falta de conteúdo, é a QUALIDADE da seleção (equilíbrio de verticais + frescor + não-repetição) — por isso o selecionador entra como componente (§5) e a CL/Chefe revisam a seleção na 1ª semana.

### 2.2 Capacidade técnica das APIs (limites duros)

| Rede | Limite de escrita | 10/dia cabe? | Leitura p/ métricas | Fonte |
|---|---|---|---|---|
| **X (Twitter) API v2 Free** | ~**500 posts/mês/app** (revisão nov/2024; docs originais 2023 citavam 1.500) | 10/dia = 300/mês → **SIM, ~60% da cota** (folga p/ retries) | curta: ~100 posts/mês → métrica diária NÃO cabe; semanal SIM | [X API tiers (xpoz.ai)](https://www.xpoz.ai/blog/guides/understanding-twitter-api-pricing-tiers-and-alternatives/) · [revisão nov/2024 (mynavi)](https://news.mynavi.jp/article/20241101-3057347/) |
| **X API v2 Basic** (US$ 100/mês) | ~3.000 posts/mês | sobra | ~10.000 posts/mês → diário SIM | idem |
| **Facebook Graph API** | **sem teto documentado** de posts/dia por página; limite prático reportado ~50 posts/24h antes de revisão de spam | 10/dia → **SIM, folga 5x** | **Page Insights completo** (alcance/engajamento por post) com o token da página, gratuito | [FB post limit (AdaptlyPost)](https://adaptlypost.com/pt/blog/facebook-post-limit-per-day) |
| **Jetpack Social / IFTTT / Zapier** | — | descartados na fase 1 (bloco 015 §2.2: plano/dependência/telemetria fora da casa) | — | bloco 015 |

⚠️ **Verificação na execução (passo do executor):** conferir no painel do desenvolvedor (X) o contador real de escrita do mês do app da casa e a janela de agendamento do Graph API (FB) antes de ligar o cron — 2 chamadas de prova, nada destrutivo.

### 2.3 Benchmark de cadência por rede (o que os dados de mercado dizem)

- **X/Twitter:** veículos de notícia operam 10-20+ posts/dia; 10/dia espaçados é cadência normal e não dispara shadowban quando o conteúdo é original (espelho do próprio site é uso legítimo; conteúdo automatizado de baixa qualidade é o que as regras do X proíbem — peça com imagem + lead próprio + link não é spam). Referências: [Buffer — frequência por rede](https://buffer.com/resources/social-media-frequency-guide/) · [Hootsuite — how often to post](https://blog.hootsuite.com/how-often-to-post-on-social-media/).
- **Facebook:** para páginas de notícia 5-15/dia é comum, MAS alcance orgânico por peça tende a cair conforme sobe o volume diário (o algoritmo prioriza recência × engajamento; página com volume alto compete com ela mesma). **Recomendação do arquiteto: FB 6-8/dia nos dias 06-08/09 → 10/dia a partir de 09/09**, com a régua "alcance por peça" (resposta do dono, 1 número por peça) validando a subida. Se o dono preferir 10 desde o dia 1, é decisão dele — o plano funciona, com o aviso de que a calibração da 1ª semana dirá se o número segura.
- **Métrica de sucesso (regra da casa):** alcance/visualização POR PEÇA e cliques (GA4/UTM) — nunca volume de postagem.

---

## 3. META DIMENSIONADA — 10 X + 10 FB/dia (o desenho operacional)

### 3.1 O que são as 20 peças do dia (espelho da esteira toda)

Cada peça = 1 post do Cafezinho (canônico) transformado em 1 post nativo por rede, com:
- **Imagem obrigatória:** a capa do post (URL via REST; já licenciada e com `_cafezinho_img_check` ok por construção). **Vídeo:** quando o post tiver vídeo (cat 28/cortes da esteira 010/011) a peça usa o vídeo no lugar da imagem — X e FB aceitam vídeo nativo; sem vídeo disponível, imagem (o "imagem/vídeo" do dono é satisfeito por peça: sempre imagem, vídeo quando houver).
- **Texto anti-mecânico (determinístico, SEM LLM na fase 1):** 1) título do post (linkado) · 2) 1 frase de lead real (a 1ª frase do post — nunca só o título) · 3) variação de abertura por template rotativo (5+ templates, escolha por hash do post_id — evita o "cara de robô" de repetir o mesmo molde) · 4) 1 hashtag `#Cafezinho` (FB: 1-3; X: 1) · 5) link com UTM `utm_source=x|facebook&utm_medium=social&utm_campaign=rotina_10x10&utm_content=<post_id>`.
- **FB:** post SEM link no corpo + **1º comentário com o link** (decisão 20:10; 2 chamadas Graph API; ver ressalva do pin no §1).
- **X:** texto ≤280 (Free) com o link no corpo + imagem. (Se o dono aprovar tweet longo Premium no espelho, é só config — Q5.)

### 3.2 Seleção das 20 peças do dia (o selecionador)

Regras (determinísticas, na ordem):
1. **Fonte:** posts `status=publish` do canônico nas últimas 24h (esteira toda, não só autoria — decisão do áudio).
2. **Dedupe 48h:** URL/post já espelhado em qualquer rede na janela de 48h não entra de novo (registro local).
3. **Equilíbrio de verticais:** máximo 3 peças da mesma vertical/dia em cada rede (anti-cara-de-um-tema-só).
4. **Frescor:** prioriza o mais novo, mas garante cobertura do dia (manhã/tarde/noite) e não espelha "velharia".
5. **Imagem/vídeo:** descarta post sem capa acessível (não deve existir — lei da casa; se aparecer, registra exceção).
6. **Teto por rede:** 10/dia (X) e 10/dia (FB) — a seleção das 2 redes pode divergir (o que é forte no X nem sempre é no FB; idealmente ~70% de interseção).

### 3.3 Espaçamento e janela (régua — calibrada para 10/dia, NÃO a régua 2h do YouTube)

- Janela: **07:30-21:30 BRT** (padrão assumido, sem espelho noturno automático).
- **X:** 10 posts em 14h → espaçamento mínimo **≥60 min** (o dono pode ver rajada se for menos; 60 min = cara de veículo de notícia, não de bot). Slots sugeridos fixos: 07:30, 09:00, 10:30, 12:00, 13:30, 15:00, 16:30, 18:00, 19:30, 21:00.
- **FB:** 10 posts → espaçamento mínimo **≥80 min** (9 intervalos × 80 = 12h); na rampa de 6-8/dia, ≥2h (régua conservadora do bloco 015) — na subida para 10, relaxa para ≥80 min mantendo os horários de pico (12h-13h, 18h-20h) para as peças mais fortes.
- **Anti-sincronia entre redes:** nunca X e FB no mesmo minuto (≥5 min de diferença entre as redes).
- **Retry de API:** 1 retry ≥60s, máx 2-3 tentativas, depois ERRO registrado + alerta (lição "sonda gentil").

### 3.4 Rampa realista (honestidade de arquiteto — o dono pediu "bem feita", não "muita")

| Dia | X | FB | Condição |
|---|---|---|---|
| 06/09 (Dia 1) | 10 | 6-8 (ou 10 se o dono mandar) | 1ª leva do dia montada pelo caminho B (§0.5) se o robô não estiver pronto; o robô entra em teste no mesmo dia |
| 07-08/09 | 10 | 8 | calibração: CL/Chefe revisam a seleção; resposta de alcance do dono calibra |
| 09/09+ | 10 | 10 | meta cheia, se a régua por peça segurar (senão, trava em 8 e sobe o caso ao dono) |

---

## 4. ACESSO ÀS APIs X/FB PARA MONITORAMENTO DE AUDIÊNCIA (o desenho)

Objetivo do dono (áudio): "monitoramento da audiência, entender o que o pessoal quer ler mais". Desenho em 3 camadas:

1. **GA4/UTM (régua-mãe — liga já no dia 1):** todo link do espelho leva UTM (§3.1); o GA4 da casa (property já instalada) reporta **cliques por peça/rede/campanha** — é a resposta direta a "o que o pessoal quer ler mais", idêntica nas 2 redes, sem depender de cota de API. Relatório diário: `Relatorios/redes_sociais/AAAA-MM-DD.md` (regra DSC-006) com cliques (GA4) + status por peça.
2. **Facebook Insights (Graph API — gratuito, token da página):** pull diário (cron ~22:00) de `page_impressions`, `post_reach` e `engaged_users` por post do dia via `GET /{page-id}/insights` + `GET /{post-id}/insights` — fecha o alcance/engajamento nativo do FB sem custo.
3. **X — métricas nativas com cota do Free:** pull SEMANAL (ex.: domingo 22:00) das `public_metrics` (like/retweet/reply/impressions) dos tweets da semana via `GET /2/tweets?ids=…` — ~70 IDs/semana cabe na cota de leitura do Free (~100 posts/mês). **Se o dono quiser diário nativo do X:** subir para Basic US$ 100/mês (decisão de orçamento — regra transparência do sprint; o prompt do Z-Code já lê a config `x_tier: free|basic`).

**Relatório semanal ao dono (1 mensagem):** top 5 peças por cliques (GA4) + top por alcance nativo (FB) — "o que o pessoal quer ler mais" vira dado de pauta para a esteira (retroalimenta a curadoria, conversa com a IDEIA-014).

---

## 5. ARQUITETURA (componentes · dados · fluxo · onde roda — refinamento do bloco 015 para 10+10)

```
[WP canônico www.ocafezinho.com] → [SENSOR Tencent: REST wp-json a cada 15 min]
      → [SELECIONADOR (novo): regras §3.2 — 20 peças/dia (10 X + 10 FB) c/ dedupe 48h + equilíbrio de verticais]
      → [GERADOR DE PEÇAS (determinístico SEM LLM): título + lead(1ª frase) + template rotativo + capa + hashtag + UTM]
      → [RÉGUA/AGENDA: slots §3.3 · dedupe local JSON em ~/dsn_redes/estado.json]
      → [PUBLICADOR]
          FB: Graph API — 1) POST /{page}/feed published=false|scheduled_publish_time (rascunho/agenda)
              2) POST /{post-id}/comments (link com UTM) — decisão 20:10
          X:  API v2 (OAuth1a user-context) — POST /2/tweets (media opcional)  | modo pacote Telegram p/ mão do dono
      → [REGISTRO: Relatorios/redes_sociais/AAAA-MM-DD.md — regra DSC-006]
      → [TELEMETRIA: comando DSC (dsc status x|facebook) + relatório diário + semanal de audiência §4]
```

- **Componentes:** 5 novos (selecionador, gerador, régua/agenda, publicador FB, publicador X) + sensor reusado do desenho do sprint — ~300-400 linhas Python + requests/tweepy; sem dependência pesada. Esqueleto referência: bloco 015 §7 + legado `~/cing_sync/` (referência de chamadas, não base).
- **Dados:** `~/dsn_redes/estado.json` (peças do dia, ids de API, status, dedupe) — valores NUNCA no arquivo de dados (§82; só nomes de env).
- **Onde roda:** **Tencent** (cron 15/15 do sensor + cron de slots do publicador). Dell: nada (X/FB não bloqueiam datacenter). NYC: intocada. **Lacuna registrada (bloco 015 §2.6):** espelhar as chaves FB/X do cofre (Dell `/root/.env.unificado` + cofres) na Tencent — passo do executor (ZM) com backup e sem expor valor em log.
- **Regra 409:** 1 consumidor por token — o robô do espelho é o ÚNICO consumidor das chaves FB/X; app único "cafezinho-social" (Meta + X) criado na execução.

---

## 6. PLANO DE EXECUÇÃO (protocolo da casa: backup → prova → registro → rollback escrito)

| # | Passo | Quem (proposta) | Risco | Reversível? |
|---|---|---|---|---|
| P0 | ✓ do dono no plano (Q1-Q6) — via Chefe (@Dsnchefe_bot) | Miguel / Chefe | modo errado (estágio) | sim (config) |
| P1 | Backup `.env.unificado` (Dell) + `/root/.env.unificado` (Tencent) com data; espelhar FB/X na Tencent | ZM | chave exposta em log | sim (backup; rotaciona) |
| P2 | App único Meta + X "cafezinho-social"; conferir contador X Free + janela de agendamento FB (prova de 2 chamadas em modo rascunho) | ZM | token novo quebra IG (mesmo token Meta!) | sim (token antigo no backup) |
| P3 | Robô MODO TESTE (Tencent): 3 posts reais → rascunho FB + 3 tweets X em modo pacote/rascunho, NADA público; provas REST | executor (ZM/DS-N Redes se nascer) | peça feia/errada | sim (rascunho não publicado se apaga) |
| P4 | Dia 1 (06/09): primeira leva 10+10 — caminho B (gerador rodado à mão + pacote Telegram + rascunho FB) se o robô não estiver pronto; caminho A se P3 passou cedo | DS-N Ideias monta/Chefe+CL revisam/executor entrega | dia 1 sem as 20 peças | sim (nada público sem o toque do dono no estágio 1; no estágio 2, kill por config) |
| P5 | Robô em produção (estágio aprovado) com régua §3.3 + dedupe + telemetria | executor | rajada/duplicata | sim (kill por config: pausa o cron; FB rascunho não sai) |
| P6 | Revisão da seleção pela CL/Chefe na 1ª semana (antes do 1º disparo do dia) | CL/Chefe | seleção torta | sim |
| P7 | Registro do padrão em `Relatorios/redes_sociais/` + linha na grade + relatório semanal de audiência | DS-N Ideias | — | — |
| P8 | (Se Q1 = estágio 2) — ROBÔ PUBLICA; regra-mãe vale só para autorais/criativas; monitorar resposta do dono (1 número por peça) | executor | regra-mãe revogada no espelho | sim (volta ao estágio 1 por config) |

**Rollback escrito:** qualquer erro de peça → rascunho FB apagado/ignorado (nunca foi público) e pacote X não colado; se algo PUBLICAR errado (estágio 2), o dono apaga/edita na plataforma (1 toque) + lição no relatório do dia; kill total = `dsc pausa redes` (remove o cron; estado preservado em `~/dsn_redes/`).

---

## 7. DECISÕES QUE PRECISO DO MIGUEL (via Chefe — curtas, p/ o resumo de aprovação)

1. **Q1 — Modo:** (a) Estágio 2 p/ o espelho automático (robô publica as 20/dia com travas; recomendado — 20 publicações/dia não cabem na mão dele) ou (b) Estágio 1 (rascunho FB + pacote X no Telegram, ele aperta)? A regra-mãe de 31/08 permanece para peças autorais/criativas nos 2 modos.
2. **Q2 — Rampa FB:** 6-8/dia nos 3 primeiros dias → 10 a partir de 09/09 (recomendado) ou 10 já no dia 1?
3. **Q3 — Handles oficiais** do X e da página do FB (para relatório/provas públicas; não estão registrados no repo).
4. **Q4 — Hashtag:** padrão `#Cafezinho` + janela 07:30-21:30 assumidos (confirmar se mantém).
5. **Q5 — X Premium:** espelho em tweet ≤280 com imagem (padrão Free, recomendado) ou tweet longo Premium?
6. **Q6 — X Basic (US$ 100/mês):** autoriza se quiser métrica nativa DIÁRIA do X via API (senão, semanal na cota Free + GA4 cobre o diário)?

---

## 8. RISCOS (top 6) e mitigação

1. **Cara de robô a 20 peças/dia** → templates rotativos + lead real + revisão CL/Chefe na 1ª semana; se o dono achar mecânico, desce o volume (kill por config).
2. **FB: alcance orgânico por peça cai com volume** → rampa Q2 + régua por peça; se cair < patamar aceitável, trava em 6-8 e sobe o caso.
3. **Cota X Free (500/mês) estourada por retries/erros** → contador verificado em P2; 300/mês previstos; folga 200 p/ retries; se apertar, Basic (Q6).
4. **Token FB de longa duração expira (60d)** → renovação documentada com gatilho <10 dias (lembrete no relatório 4/4h do Chefe; lição do `invalid_client` do YouTube 23/07).
5. **Conteúdo repetido entre redes (X e FB espelhando o mesmo)** → interseção ~70% é desejada (públicos diferentes); dedupe é por rede; anti-sincronia ≥5 min.
6. **Publicar duplicata do dia anterior** → dedupe 48h por URL/rede em `~/dsn_redes/estado.json` (registro local, nunca em produção).

---

## 9. FONTES (pesquisa de volume — §2)

[X API tiers comparados](https://www.xpoz.ai/blog/guides/understanding-twitter-api-pricing-tiers-and-alternatives/) · [Revisão da cota do Free em nov/2024 (mynavi)](https://news.mynavi.jp/article/20241101-3057347/) · [Limite de posts/dia no Facebook (AdaptlyPost)](https://adaptlypost.com/pt/blog/facebook-post-limit-per-day) · [Frequência por rede (Buffer 2026)](https://buffer.com/resources/social-media-frequency-guide/) · [How often to post (Hootsuite 2025)](https://blog.hootsuite.com/how-often-to-post-on-social-media/) · [Limites diários de publicação (Metricool)](https://help.metricool.com/fr/article/limites-de-publication-quotidiennes-sur-les-reseaux-sociaux-9f6vn3/)

---

## ANEXO A — PROMPT PRONTO PARA O Z-CODE (colar no Z-Code; texto limpo, sem segredos)

```
PROMPT Z-CODE — ROTINA ESPELHO REDES SOCIAIS 10+10 (X + FACEBOOK) DO CAFEZINHO

1. CONTEXTO
O dono do Cafezinho decidiu (áudio 21:58 de 05/09, transcrito no CL-039): 10 posts por dia no X e 10 por dia no Facebook, a partir de 06/09, peças bem feitas com imagem (vídeo quando houver), espelhando a esteira TODA do site (www.ocafezinho.com), não só posts do Miguel. Fluxo aprovado: Ideias desenhou (arquivo cerebro/Foruns/ideias/2026-09-05_plano_redes_10x10_x_fb_prompt_zcode.md no repo cerebro-miguel) e o dono aprovou. Tua missão: construir e ligar a rotina descrita abaixo. Leia primeiro: o arquivo do plano (seções 3, 4, 5 e 6) + cerebro/Foruns/ideias/2026-09-05_bloco015_rotina_publicacao_twitter_x_facebook.md (arquitetura e esqueleto §7) + cerebro/Foruns/ideias/2026-08-31_manual_criativo_redes.md (formato das peças e pacote Telegram §6) + cerebro/Foruns/SPRINT_REDES_SOCIAIS_20260831.md.

2. ONDE CONSTRUIR
Servidor Tencent (o mesmo que roda o coletor DSN). Pasta ~/dsn_redes/. Scripts: espelho_social.py (sensor+selecionador+gerador+régua) e publicador_fb.py / publicador_x.py (ou um único CLI com subcomandos: sensor, seleciona, gera, publica_fb, publica_x, status, pausa, retoma). Estado em ~/dsn_redes/estado.json (dedupe 48h por URL/rede, peças do dia, ids de API, status). Registro diário em cerebro/Relatorios/redes_sociais/AAAA-MM-DD.md (padrão DSC-006: post do site, rede, texto, id da API, hora BRT, status). Use o cron do usuário ubuntu (backup do crontab antes, com data).

3. CREDENCIAIS — REGRA §82 (NUNCA valores no código, nos logs ou na ponte)
Leia do ambiente: FB_PAGE_ID, FB_PAGE_ACCESS_TOKEN, X_API_KEY, X_API_KEY_SECRET, X_ACCESS_TOKEN, X_ACCESS_TOKEN_SECRET (cofre .env.unificado — Dell e Tencent /root/.env.unificado; se faltar na Tencent, espelhe a partir do cofre com backup e sem imprimir valor). App único "cafezinho-social" (1 consumidor por token, regra 409). Se o contador de escrita do X Free estiver abaixo do necessário (10/dia = 300/mês; cota ≈500/mês), avise no registro — não mude de tier sem ordem.

4. O QUE CONSTRUIR (resumo do plano; detalhes no arquivo)
- Sensor: REST wp-json a cada 15 min, posts status=publish das últimas 24h, com capa.
- Selecionador: 20 peças/dia (10 X + 10 FB) com dedupe 48h, máx 3 por vertical/dia/rede, prioridade por frescor, nunca título+link pelado.
- Gerador determinístico SEM LLM: título + 1ª frase do post como lead + abertura por template rotativo (5+ variações) + 1 imagem (URL da capa do post via REST) + hashtag #Cafezinho + link com UTM (utm_source=x|facebook, utm_medium=social, utm_campaign=rotina_10x10, utm_content=post_id).
- Facebook: post SEM link no corpo + 1º comentário com o link (2 chamadas Graph API: POST /{page}/feed → POST /{post-id}/comments). Modo conforme config: rascunho (published=false) OU agendado (scheduled_publish_time) OU publicado (estágio 2 aprovado).
- X: POST /2/tweets com o link no corpo + imagem (OAuth 1.0a user-context). Modo conforme config: pacote Telegram (texto pronto no canal do dono, ele cola) OU publicado (estágio 2 aprovado).
- Régua: janela 07:30-21:30 BRT; X espaçamento ≥60 min (slots 07:30, 09:00, 10:30, 12:00, 13:30, 15:00, 16:30, 18:00, 19:30, 21:00); FB espaçamento ≥80 min na meta 10, ≥2h na rampa 6-8; nunca X e FB no mesmo minuto (≥5 min); retry 1× ≥60s, máx 3 tentativas, depois ERRO + alerta.
- Config em ~/dsn_redes/config.json: {"modo_fb": "rascunho|agendado|publicado", "modo_x": "pacote|publicado", "meta_fb": 8, "meta_x": 10, "x_tier": "free"} — o DONO aprova o modo; default seguro = rascunho FB + pacote X (estágio 1).
- Comandos para o DSC: espelho_social.py status|pausa|retoma|seleciona|publica_fb|publica_x (pausa = remove o cron; retoma = recria; estado preservado).
- Telemetria de audiência: (1) GA4/UTM já cobre cliques (relatório diário manual a partir do GA4); (2) FB Insights via Graph API (pull diário ~22:00: page_impressions/post_reach/engaged_users por post do dia); (3) X: pull semanal (domingo 22:00) de public_metrics dos tweets da semana via GET /2/tweets?ids= (cabe na cota Free; se x_tier=basic, diário).

5. PROTOCOLO DA CASA (obrigatório)
- Backup → prova → registro → rollback escrito. Antes de tocar crontab/env: backup com data (cp -a e crontab -l > backup). Prova de cada etapa no registro (resposta da API, id criado, hora BRT real). Nada em produção sem passar pelo modo teste (P3 do plano: 3 posts reais em rascunho FB + 3 pacotes X, nada público — mostre as provas).
- MODO TESTE primeiro (config modo_fb=rascunho, modo_x=pacote) por pelo menos 1 dia; a troca para publicado SÓ com ordem explícita do dono (estágio 2 aprovado no plano Q1).
- Rollback: dsc pausa redes remove o cron; estado preservado; rascunho FB nunca vira público sozinho.

6. ENTREGA (o que reportar)
Relatório final com: (a) o que foi construído (arquivos, crons, linhas); (b) provas do modo teste (3 rascunhos FB + 3 pacotes X com ids/horas); (c) confirmação do contador X Free e da janela de agendamento FB; (d) como ligar/desligar (comandos); (e) pendências (ex.: chaves espelhadas na Tencent, handles oficiais, canal TV Cafezinho). Registre tudo em cerebro/Relatorios/redes_sociais/ e avise na ponte (canal de_ideias.md) com a assinatura do agente.
```

---

— DS Nuvem Ideias (DS-N Ideias) · 20260905 23:50:07 BRT
