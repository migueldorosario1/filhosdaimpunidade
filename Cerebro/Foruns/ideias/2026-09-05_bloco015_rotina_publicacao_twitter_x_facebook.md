# 🐦📘 BLOCO IDEIA_PRO_DSNUVEM_IDEIAS-015 — ROTINA DE PUBLICAÇÃO ESPELHO no TWITTER/X e FACEBOOK do Cafezinho (arquitetura + plano de implementação)

> **Ronda:** 05/09/2026 ~12:15-12:35 BRT (DS-N Ideias, Tencent). Pull ff-only OK na 1ª (12:13; fast-forward 893f7ef7b..8cf7b34e6).
> **Bloco:** `IDEIA_PRO_DSNUVEM_IDEIAS-015` — DSH-us65 (ordem do Miguel por voz ~09:1x), carimbo `20260905 09:20 BRT`, bloco em `cerebro/Foruns/ponte_laura_completa/de_dell.md` (~18440-18449; entrou no repo junto com o 016, visível 12:05). **Atenção a numeração:** a "IDEIA-015" processada às 09:43-09:46 desta manhã foi o boletim de custos (encomenda do Maestro, contagem interna da casa); o bloco OFICIAL 015 do DSC é ESTE (X/Facebook). Registro no estado com o identificador do bloco.
> **Fluxo da casa (do bloco):** Ideias entrega → DS-N Chefe aprova/travas → resumo ao MIGUEL pelo @Dsnchefe_bot. Prazo do plano: HOJE 05/09.
> **Refs:** SPRINT_REDES_SOCIAIS_20260831.md (31/08 15:44) · manual criativo IDEIA-001/001A (`2026-08-31_manual_criativo_redes.md`, aprovado 01/09 no tema2 DSC) · VAGA_DS_NUVEM_REDES_20260901.md · forum_video_diario_multirrede_20260723.md (teste Kakay: FB Reels ✅ via Graph API) · regra-mãe da casa: **robô NÃO posta em rede social; publish = mão do Miguel** · regra §82 (segredos no cofre, nunca na ponte/arquivo de ideia) · regra 409 (1 consumidor por token) · régua YouTube anti-rajada (≥2h, máx 6/dia — ordem Miguel 04/09 22:55) · legado `~/cing_sync/` + `~/root_copy/` (agente_twitter/facebook/tiktok, postador_twitter via tweepy, postador_facebook) SEM cron ativo.
> **Natureza:** ESTUDO/ARQUITETURA/PLANO — NADA executado em produção (Lei de Poderes). Nenhum valor de chave neste arquivo (§82).
> **Marcador:** `PRONTO_BLOCO015_ROTINA_TWITTER_FACEBOOK`

---

## 0. Resumo executivo (o veredito do arquiteto)

1. **A casa NÃO parte do zero:** desde 31/08 existe a Sprint Redes Sociais com manual criativo APROVADO pelo Miguel (X = 2 tweets · FB = longo + link no 1º comentário · autoria sempre "Miguel do Rosário") e a regra-mãe **"robô não posta; publish = mão do Miguel (ou rascunho que ELE aperta)"**. A DS Nuvem Redes foi desenhada (vaga 01/09) e **não nasceu** (aguarda ✓). Este bloco do maestro é o relançamento com viés de IMPLEMENTAÇÃO — então a entrega certa é: reconciliar a regra-mãe com a automação que ele pede, e desenhar a rotina em 2 estágios.
2. **Caminho principal recomendado: Facebook Graph API** (token de PÁGINA de longa duração, **gratuito e estável**, a casa JÁ tem `FB_PAGE_ID`/`FB_PAGE_ACCESS_TOKEN` no cofre e JÁ PUBLICOU por essa via — Reels do Kakay 23/07; o IG @ocafezinhooficial usa o mesmo token Meta) **+ X API v2 no tier gratuito (Free)** como 2º caminho (a casa JÁ tem o par de chaves completo no cofre; 2 tweets/dia ≈ 60/mês cabe folgado no Free de escrita; o Miguel tem X Premium para os tweets longos quando posta pela UI). **Fallbacks:** X sem API = pacote manual no Telegram (formato já desenhado no manual criativo §6) · FB sem API = Meta Business Suite na mão do Miguel. **Descartados na fase 1: Jetpack Social/Publicize e IFTTT/Zapier** — custo/plano/dependência e telemetria fora do controle da casa (detalhe no §3).
3. **A automação proposta é de RASCUNHO + AGENDAMENTO COM CONFIRMAÇÃO do Miguel, não robô postando livre.** A regra-mãe de 31/08 (reforçada 01/09 no tema2 DSC: "EU publico com minha mão, robô não posta") só cai por decisão explícita do dono — eu desenho os 2 estágios e a pergunta vai ao Miguel via Chefe.
4. **Formato do espelho com qualidade mínima anti-mecânico** (o Miguel já disse que "post mecânico no FB = visualização ruim"): título do post + 1 frase de lead (não só título+link pelado) + capa + 1 hashtag da casa + UTM. Encurtador: NÃO (domínio próprio é curto; encurtador esconde o domínio e adiciona camada de falha). UTM: SIM (medir no GA4).
5. **Régua espelhada da lição YouTube:** mín 2h entre posts na MESMA rede, máx 6/dia por rede, JAMAIS post duplicado na janela (dedupe por URL+rede), janela 07:30-21:30 BRT (noturno respeitado), falha de API = retry espaçado ≥60s (lição "sonda gentil" anti-rajada), no máximo 2-3 tentativas.

---

## 1. HISTÓRICO NO CÉREBRO — o que a casa já discutiu e decidiu (não reinventar)

| Data | O que foi decidido/registrado | Onde |
|---|---|---|
| 23/07 | Vídeo Diário Multirrede: teste Kakay ponta a ponta — **FB Reels PUBLICADO via Graph API** (upload binário 3 fases, sem URL pública) · IG Reels publicado · YouTube Shorts publicado (após re-auth OAuth) · TikTok: upload em RASCUNHOS funciona sem auditoria; publish direto bloqueado (app não auditado) | forum_video_diario_multirrede_20260723.md + memoria |
| 31/08 15:44 | **SPRINT REDES SOCIAIS** (ordem do Miguel): 2 posts/dia/rede (FB, X, TikTok) derivados de posts **de autoria Miguel do Rosário**; peças criativas (anti-mecânico); **PUBLISH = MÃO DO MIGUEL** ("posts saem do dispositivo/IP dele — autêntico pro algoritmo"); fase 2 com API só "com orçamento aprovado antes (regra transparência)" | SPRINT_REDES_SOCIAIS_20260831.md |
| 31/08 18:46 | **Manual criativo IDEIA-001/001A** (DS-N Ideias): X = 2 tweets (1 longo/gancho + 1 só link, intervalo 2-5 min) · FB = post longo 200-400 palavras + **link no 1º comentário** · TikTok = roteiro 30-60s · kit anti-mecânico · horários por rede · pacote one-click no Telegram · métrica = alcance por peça | 2026-08-31_manual_criativo_redes.md |
| 01/09 ~00:50 | Tema2 DSC: manual **APROVADO pelo Miguel**; **X Premium: Miguel TEM**; criar **DS Nuvem Redes** (fase 1 debate/teste de credenciais+formatos+rascunho-via-API × pacote Telegram; fase 2 lançamento só com ✓ explícito; "EU publico com minha mão, robô não posta"); inventário: FB ✅ token de página · IG ✅ token Meta (~25.976 seguidores @ocafezinhooficial) · X ✅ API completa no cofre · TikTok ❌ sem credencial de API | sessoes_dsc/2026-08-31_tema2_sprint_redes_sociais.md + VAGA_DS_NUVEM_REDES_20260901.md |
| 01/09+ | DS Nuvem Redes **NÃO nasceu** (vaga aguardando ✓ do Miguel; nenhum bloco da vaga nos dias seguintes) · Sprint Redes sem avanço registrado em 02-05/09 → **parada desde 01/09** | grep ponte 02-05/09 |
| Legado | `~/cing_sync/` e `~/root_copy/` têm `agente_twitter.py` (gerador_fios_x + postador_twitter/tweepy), `agente_facebook.py` + `postador_facebook.py`/`postador_meta.py`, `agente_tiktok.py` — **sem cron ativo** (crontab do ubuntu sem jobs sociais); baseados em .env (cofre) | máquina Tencent |

**Decisões que amarram (inegociáveis):** (1) autoria sempre "Miguel do Rosário", nunca voz de robô; (2) publish = mão do Miguel OU rascunho que ele aperta — robô não posta em rede social; (3) anti-mecânico: proibido colar título+link pelado (o espelho deste bloco é uma exceção a negociar — §4); (4) revisão antes de entregar; (5) métrica = alcance por peça, nunca volume; (6) sem segredos na ponte (§82); (7) 1 consumidor por token (regra 409).

---

## 2. CHECKLIST DO MAESTRO, PONTO A PONTO

### 2.1 Histórico — §1 acima (resumo: sprint aprovado e parado; infra de credenciais existe; regra-mãe vigente).

### 2.2 Caminhos comparados — O QUE DEU CERTO / melhor autorização

| Caminho | Custo | Limites/condições | O que a casa já tem | Veredito |
|---|---|---|---|---|
| **(a) X API v2** | Free: escrita limitada (app único, ~1.500 posts/mês — suficiente p/ 2-6/dia ≈ 60-180/mês); Basic US$ 200/mês para mais apps/leitura | OAuth 1.0a user-context (a conta do dono); regras de automação do X (conteúdo automatizado de baixa qualidade é contra as regras; espelho do próprio site é uso legítimo de social media); agendamento via API a confirmar na execução (senão: texto pronto + Miguel agenda pela UI) | `X_API_KEY/SECRET`, `X_ACCESS_TOKEN/SECRET`, `X_BEARER_TOKEN` no cofre (mai/26: conta era plano básico p/ vídeo >140s; Miguel declara Premium hoje) | **Recomendado (Free)** — só para a conta do Cafezinho; subir de tier só com orçamento aprovado (regra transparência do sprint) |
| **(b) Facebook Graph API** | **Gratuito** (token de página; longa duração 60d renovável; sem custo por post) | Post na Página do Cafezinho; criar post como **rascunho (published=false)** e/ou **agendar (scheduled_publish_time)** — perfeito para a regra-mãe (o Miguel revisa e publica/confirma); sem "rascunho" para Stories; taxa de post por página bem acima do uso | `FB_PAGE_ID` + `FB_PAGE_ACCESS_TOKEN` no cofre; **prova real de funcionamento**: FB Reels Kakay 23/07 + IG via token Meta | **CAMINHO PRINCIPAL** |
| **(c) Jetpack Social/Publicize (WP)** | Plano Jetpack (free: 1 conta conectada e agendamento básico; mais contas = pago) | Publica do wp-admin no push do post; exige instalar/configurar plugin no WordPress de produção (mão de quem tem WP: ZM/CL) e conectar as contas sociais lá; telemetria/provas ficam dentro do Jetpack, fora do padrão de registro da casa (Relatorios/redes_sociais) | O site É WordPress (canônico www.ocafezinho.com); **não há registro de Jetpack ativo/avaliado no repo** (menções antigas em memórias de 06/08) | **Descartado na fase 1** (dependência de plano + instalação em produção + telemetria fora da casa); revisitar só se o Miguel quiser gestão dentro do WP |
| **(d) IFTTT/Zapier** | Zapier free ~100 tarefas/mês; IFTTT free ~2-3 applets; pagos para mais | Cola rápida, mas depende das MESMAS APIs (X/FB) e adiciona camada externa: fila, erros e provas fora do controle da casa; difícil aplicar dedupe/régua 2h/máx6 e registro | Nada | **Descartado na fase 1** (bom só p/ protótipo de 1-2 feeds, não p/ operação diária com régua e telemetria) |

**Recomendação:** um caminho principal = **Facebook Graph API** (gratuito, estável, provado, rascunho/agendamento = regra-mãe respeitada) e o 2º = **X API v2 Free**; fallback operacional dos dois = pacote manual no Telegram (estado atual do sprint, já desenhado). Jetpack/IFTTT/Zapier ficam documentados como não-recomendados agora.

### 2.3 Formato (espelho do publicado)

- **Estrutura mínima por post espelho:** 1) título do post (linkado); 2) 1 frase de lead extraída do post (não repetir só o título — mínimo anti-mecânico); 3) link com **UTM** (`utm_source=x|facebook`, `utm_medium=social`, `utm_campaign=rotina_espelho`, `utm_content=<post_id>`); 4) 1 imagem de capa (a mídia destacada do post — via REST a casa pega a URL da capa já licenciada, `_cafezinho_img_check` ok por construção); 5) 1 hashtag da casa (proposta: `#Cafezinho` — decidir com o Miguel; 0-2 no X, 3-5 no FB segundo o manual §5.3).
- **Encurtador:** NÃO usar (ocafezinho.com é curto; encurtador esconde o domínio e adiciona ponto de falha/rastreio de terceiro). Se o X contar caracteres e o título for longo, o próprio link já é o encurtador natural; o tweet 2 do manual criativo continua sendo o padrão quando a peça for criativa.
- **UTM:** SIM, nos links de TODOS os posts do espelho — é o que permite medir no GA4 (property da casa) e fechar o loop com a métrica do sprint (alcance por peça + cliques).
- **No Facebook:** no ESPELHO AUTOMÁTICO o link vai no CORPO (a tática "link no 1º comentário" é do pacote criativo manual, postado pela mão do Miguel; via API o rascunho/agendamento sai mais simples com link no corpo). **Pergunta ao Miguel** se ele quer a tática do 1º comentário também no espelho automático (dá para fazer: post sem link + comentário fixado com link — 2 chamadas).

### 2.4 Régua (espelhando a lição do YouTube)

Proposta de régua única para X e FB (calibrada na lição YouTube ≥2h/máx6 — ordem 04/09 22:55 e freno do Chefe):

| Régua | Valor | Origem/porquê |
|---|---|---|
| Cadência mínima entre posts da MESMA rede | **≥2h** | anti-rajada (lição YouTube; rajada = cara de robô + risco de shadowban) |
| Máximo por dia por rede | **6** (X: 2-4 sugerido; FB: 2-4 sugerido) | teto da régua YouTube; qualidade > volume |
| JAMAIS mesmo minuto entre redes | sim (espalhar ≥5 min) | não parecer síncrono de bot |
| Dedupe | **bloquear URL já postada na rede na janela de 48h** | não repetir; guardar (post_id, url, rede, ts) em registro local |
| Horário noturno | **07:30-21:30 BRT** (sem espelho automático fora da janela) | respeito ao leitor + janelas do manual §5.4 |
| Falha de API | retry único ≥60s, máx 2-3 tentativas, depois ERRO registrado + alerta | lição "sonda gentil" anti-rajada (caçada 16) |
| Autores | **só posts de autoria "Miguel do Rosário"** (decisão do sprint 31/08) — perguntar se o espelho cobre a esteira toda | sprint redes |

### 2.5 Fluxo de controle — quem aperta o botão

**Dois estágios (a decisão do estágio é do Miguel via Chefe):**

- **ESTÁGIO 1 (lançamento recomendado — respeita a regra-mãe na íntegra):** o robô (Tencent) detecta o post novo de autoria do Miguel, monta a peça-espelho (determinística, SEM LLM — custo zero e zero alucinação; o lead é a 1ª frase do post), e:
  - **Facebook:** cria **rascunho na Página via Graph API** (published=false) → o Miguel recebe aviso no Telegram (com DSC/Chefe) e **publica com 1 toque** (app Meta Business Suite) ou manda "vai" e o robô agenda/publica (se ele liberar esse modo no debate);
  - **X:** sem rascunho nativo na API → entrega o **texto pronto no pacote do Telegram** (formato manual §6) para o Miguel colar (tweets longos via Premium) OU, se ele liberar, agenda via API (a confirmar) / posta na hora.
  - Travas: allowlist de autores · dedupe · régua §2.4 · revisão leve do Chefe/CL antes do 1º disparo de cada dia (opcional, só na 1ª semana).
- **ESTÁGIO 2 (só com ✓ explícito do Miguel):** robô publica sozinho com a régua + travas + telemetria por post (id, hora, código/resposta da API) em `Relatorios/redes_sociais/AAAA-MM-DD.md`; o Miguel acompanha por comando DSC (`dsc status x`, `dsc status facebook` — no desenho do bloco 016) e recebe relatório diário. **Isto REVOGA parcialmente a regra-mãe de 31/08** — precisa da palavra do dono, não minha.

**Telemetria/provas (como o Miguel acompanha):** registro em `Relatorios/redes_sociais/AAAA-MM-DD.md` (regra DSC-006: nada se perde) com: post do site (id/URL) → rede → texto enviado (ou pacote) → id da API (se houver) → hora BRT real → resposta/serviço → status (rascunho_criado / publicado / erro). Relatório semanal de alcance (o Miguel responde 1 número por peça quando posta pela mão — regra do manual §7).

### 2.6 Contas/segredos

- **Onde cofrar tokens (§82):** valores NUNCA na ponte nem em arquivo de ideia. Os nomes já existem: `FB_PAGE_ID`, `FB_PAGE_ACCESS_TOKEN`, `X_API_KEY`, `X_API_KEY_SECRET`, `X_ACCESS_TOKEN`, `X_ACCESS_TOKEN_SECRET`, `X_BEARER_TOKEN` — cofre `.env.unificado` (Dell) + `/root/.env.unificado` (Tencent). **Lacuna registrada (23/07, Constituição §2):** chaves FB/X precisam estar espelhadas na Tencent onde o robô vai rodar — executar o espelho SÓ na fase de execução, por quem tem mão (ZM), com backup e sem expor valor em log.
- **Quem cria o app:** app único da casa nas plataformas (Meta Developers + X Developer) — **1 consumidor por token (regra 409)**: o robô do espelho é o ÚNICO consumidor das chaves FB/X da casa; se a DS Nuvem Redes nascer, ela herda o app — nunca 2 processos com o mesmo token (lição 409 de 02/09 nos bots Telegram). App X no tier Free = 1 app; se precisar de 2º app (ex.: separar leitura), aí sim avaliar Basic US$ 200/mês com orçamento aprovado.
- **Token FB de longa duração:** validade 60 dias; renovação documentada (quem: ZM; gatilho: lembrete no relatório 4/4h do Chefe quando faltarem <10 dias — evitar o erro do token YouTube `invalid_client` de 23/07).
- Handles oficiais (X/FB) a confirmar com o Miguel (não estão registrados no repo; só @ocafezinhooficial no IG).

---

## 3. ARQUITETURA (componentes · dados · fluxo · onde roda)

```
[WP canônico www.ocafezinho.com]  →  [SENSOR Tencent: REST wp-json, a cada 15 min]
        | detecta post novo (autor Miguel do Rosário + status publish)
        v
[GERADOR DE PEÇAS (Tencent, determinístico, SEM LLM na fase 1)]
        | monta: título + lead (1ª frase do post) + link c/ UTM + capa (URL da mídia) + hashtag
        | por rede: X (≤280 ou longo p/ pacote) · FB (texto + link no corpo ou 1º comentário)
        v
[REGRA (Tencent): dedupe 48h · cadência ≥2h · máx 6/dia · janela 07:30-21:30 · retry ≥60s]
        v
[PUBLICADOR (Tencent, estágio 1 = rascunho/agendamento; estágio 2 = posta)]
        | FB: Graph API (rascunho published=false OU scheduled_publish_time)
        | X: pacote Telegram p/ mão do Miguel (estágio 1) OU API v2 (estágio 2)
        v
[REGISTRO: Relatorios/redes_sociais/AAAA-MM-DD.md  ← regra DSC-006]
        v
[TELEMETRIA: status por comando DSC + relatório diário no Telegram do Miguel]
```

- **Componentes:** sensor (reusa o desenho do sprint: DS-Dell/DS-N flag AUTORIA_MIGUEL; ou cron REST simples) · gerador (novo, ~100 linhas Python + requests; sem dependência pesada) · régua/dedupe (banco local JSON/estado em `~/dsn_redes/` ou no repo `Foruns/redes_sociais/`) · publicador FB (Graph API) e X (tweepy v2 ou requests OAuth1) · registro (markdown).
- **Dados:** fila de pendências (post_id, url, autor, ts_detectado) → peças geradas (rede, texto, imagem_url, utm) → estado de postagem (rede, post_id_api, status, ts) → relatório do dia. Nenhum valor de chave em arquivo de dados/registro (§82).
- **Onde roda:** **Tencent** (cron 15/15 ou ronda 30/30 do DS-N Redes quando nascer; a Tencent já roda o coletor e tem os .env). **Dell**: nada (X/FB não bloqueiam datacenter — diferente do YouTube; a porta residencial do Dell fica só para YouTube). **NYC**: intocada (contrato do adapter).
- **Reuso do legado:** os scripts `~/cing_sync/agente_facebook.py`/`postador_twitter.py` são a PROVA de que o caminho de código existe — mas são de abril/2026, sem régua/dedupe/telemetria; o novo robô nasce enxuto (esqueleto no §7), e o legado vira referência de chamadas, não base.

---

## 4. PLANO DE EXECUÇÃO (passos numerados, riscos, reversibilidade — protocolo da casa: backup → prova → registro → rollback escrito)

| # | Passo | Quem (proposta) | Risco | Reversível? |
|---|---|---|---|---|
| 0 | ✓ do Miguel no desenho (estágio 1 ou 2 · handles · link no corpo ou 1º comentário no FB · escopo: só autoria Miguel ou esteira toda · hashtag) | Miguel via Chefe | decisão errada de escopo | sim (reconfigura) |
| 1 | Backup do `.env.unificado` (Dell) e do `/root/.env.unificado` (Tencent) com data; espelhar FB/X na Tencent (ZM; sem expor valor em log) | ZM | token exposto em log | sim (rotaciona; backup restaura) |
| 2 | App único Meta + X ("cafezinho-social", 1 consumidor por token — regra 409); token FB de longa duração renovado com data de expiração registrada | ZM + Miguel (login) | token novo quebra fluxo antigo (IG usa o mesmo token Meta!) | sim (token antigo no backup até o IG migrar) |
| 3 | Robô espelho fase 1 em MODO TESTE (Tencent): 3 posts-reais em rascunho FB + 3 pacotes X, SEM publicar nada | DS-N Ideias desenha + executor (ZM/DS-N Redes) | texto feio/errado | sim (rascunho não publicado se apaga; pacote não sai) |
| 4 | Prova: o Miguel vê os 3 rascunhos no app e os 3 pacotes no Telegram e dá "vai" (ou ajusta) | Miguel | — | — |
| 5 | Registro do padrão em `Relatorios/redes_sociais/` + regras na grade (linha redes) + aviso na ponte | DS-N Ideias/Chefe | — | — |
| 6 | Estágio 1 em produção (rascunho FB automático + pacote X automático) com régua §2.4 e dedupe | executor | rajada/duplicata | sim (kill por config: pausa o cron; nada publicado fica rascunho) |
| 7 | (Opcional, só com ✓) Estágio 2: robô publica; telemetria por post; comando DSC de status | executor | regra-mãe revogada | sim (volta ao estágio 1 por config) |

**Rollback escrito:** qualquer erro de peça → rascunho FB é apagado/ignorado (nunca foi público) e pacote X não é colado; se algo PUBLICAR errado (só no estágio 2), o Miguel apaga/edita na plataforma (1 toque) e a casa registra a lição no relatório do dia. Nada em produção é tocado por robô sem o ✓ do estágio.

---

## 5. RASCUNHOS (dentro do arquivo da ideia — nunca em produção)

### 5.1 Config (esqueleto — valores de exemplo, sem chaves)

```json
{
  "rede": ["facebook", "x"],
  "janela": {"inicio": "07:30", "fim": "21:30", "tz": "America/Sao_Paulo"},
  "regua": {"min_intervalo_min": 120, "max_por_dia": 6, "dedupe_janela_h": 48, "retry_max": 2, "retry_espera_s": 60},
  "utm": {"source": {"facebook": "facebook", "x": "x"}, "medium": "social", "campaign": "rotina_espelho"},
  "autores_allowlist": ["Miguel do Rosário"],
  "hashtags": {"facebook": ["#Cafezinho"], "x": []},
  "facebook": {"link_no_corpo": true, "modo": "rascunho"},
  "x": {"modo": "pacote_telegram"}
}
```

### 5.2 Esqueleto do robô (lógica, ~pseudo-código — sem valores)

```python
# espelho_social.py (Tencent) — fase 1: rascunho FB + pacote X. NUNCA posta sem o modo.
def detectar_novos():  # REST wp-json: posts status=publish, author=Miguel, sem utm_campaign=rotina_espelho
    ...
def montar_peca(post):  # determinístico: titulo + lead(1a frase) + url_utm + capa(post.media) + hashtag
    ...
def regra_ok(peca, estado):  # dedupe 48h · intervalo >=120min na rede · max 6/dia · janela 07:30-21:30
    ...
def facebook_rascunho(peca):  # POST /{FB_PAGE_ID}/feed published=false
    ...
def x_pacote(peca):  # grava texto no canal Telegram do Miguel (formato manual §6)
    ...
def registrar(peca, resultado):  # append em Relatorios/redes_sociais/AAAA-MM-DD.md
    ...
```

### 5.3 Linha do relatório diário (regra DSC-006)

```
05/09 — ESPELHO SOCIAL
- post 2691xx (autor: Miguel) -> FB rascunho criado (id_api ...) 11:32 BRT | X pacote enviado 11:33 BRT
- alcance (resposta do Miguel, 1 número por peça): FB ... | X ...
```

---

## 6. DECISÕES QUE PRECISO DO MIGUEL (via DS-N Chefe — resumo ao @Dsnchefe_bot)

1. **Estágio 1 (rascunho/agendamento + pacote, regra-mãe intacta) ou já Estágio 2 (robô publica)?** — recomendação do arquiteto: Estágio 1 primeiro (2 semanas), depois decidir.
2. **Handles oficiais** do X e da página do Facebook do Cafezinho (para os links/provas; não estão registrados no repo).
3. **Link no corpo ou no 1º comentário** nos posts automáticos do Facebook (o manual criativo manda 1º comentário para as peças da mão dele; no automático recomendo corpo).
4. **Escopo do espelho:** só posts de autoria dele (decisão do sprint) ou todos os posts do site? (o espelho do maestro parece ser da esteira toda — se for, muda o allowlist).
5. **Hashtag da casa** (proposta #Cafezinho) e horário noturno (proposta 07:30-21:30).
6. **X Premium:** confirmar se o espelho no X deve sair em tweet longo (Premium) ou ≤280 (Free) — afeta o gerador.

## 7. NOTA DE MÉTODO (para o relatório do Chefe)

A numeração interna da casa ("IDEIA-015" = boletim de custos, 09:46) colidiu com o bloco oficial `IDEIA_PRO_DSNUVEM_IDEIAS-015` (X/Facebook, carimbo 09:20, visível no repo só às 12:05). Recomendo ao Chefe registrar no relatório: **blocos IDEIA_PRO numerados pelo DSC passam a ser referidos pelo número do bloco** (ex.: "bloco 015 X/FB", "bloco 016 YouTube/TikTok") para não confundir com a contagem interna de arquivos da casa.

— DS Nuvem Ideias (DS-N Ideias) · 20260905 12:19:33 BRT

---

## 8. ADENDO 05/09 20:47 (48ª caçada) — DECISÃO DO DONO 20:10:23 RESPONDE A PERGUNTA DO PASSO 0: FB ESPELHO = LINK NO 1º COMENTÁRIO

**Fato:** INBOX do Miguel 20:10:23 — "acho que é preferível link no 1º comentário, mas a gente consegue fazer isso?" — responde a pergunta aberta do §2.3/linha 57 e o item 3 do §6. O DSC-us65 registrou a DECISÃO (20:2x) e confirmou a viabilidade Graph API em 2 chamadas (bloco 20:29 + DS-N Chefe 208º 20:36 + DS-Dell 202ª 20:35). Ciclo fechado na mesa.

**Impacto no desenho (substitui o §2.3 FB "link no CORPO no espelho automático"):**
- FB espelho automático passa a: **post SEM link no corpo + 1º comentário com o link** — 2 chamadas Graph API: `POST /{page-id}/feed` (texto da peça) → `POST /{post-id}/comments` (mensagem = link com UTM). A peça (título + lead + capa + hashtag) segue determinística SEM LLM (§2.5).
- **Ressalva técnica de arquiteto (registrar para o executor):** o Graph API NÃO tem endpoint público de fixar/pinar comentário (pin é recurso da UI/Meta Business Suite). O equivalente via API = criar o comentário IMEDIATAMENTE após o post: com poucos comentários, ele é exibido como o 1º da conversa nas ordenações padrão (relevância/mais recentes). Não prometer "fixado" literal no desenho/telemetria.
- **Fluxo/arquitetura (§3) inalterado** exceto o passo FB do gerador: monta a peça em 2 partes (post + comentário-link) e o publicador faz 2 chamadas com o post_id da 1ª resposta. Registro em `Relatorios/redes_sociais/` com os 2 ids (post + comentário).

**Passo 0 do §4 — PARCIALMENTE respondido:** decidido = link no 1º comentário no FB ✓. Ainda pendentes: estágio 1 ou 2 · handles oficiais · escopo (só autoria Miguel × esteira toda) · hashtag · X Premium (longo × ≤280). Nenhum pendente bloqueia o início do ESTÁGIO 1 em modo teste (3 rascunhos FB + 3 pacotes X, SEM publicar — passo 3 do plano).

— DS Nuvem Ideias (DS-N Ideias) · 20260905 20:47:5x BRT
