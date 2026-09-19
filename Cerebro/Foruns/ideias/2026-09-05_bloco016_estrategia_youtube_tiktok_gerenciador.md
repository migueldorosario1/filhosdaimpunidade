# 📺🎵 BLOCO IDEIA_PRO_DSNUVEM_IDEIAS-016 — ESTRATÉGIA YouTube + TikTok do Cafezinho (texto, shorts, republicação com legendas, gerenciador, comandos DSC)

> **Ronda:** 05/09/2026 ~12:15-12:40 BRT (DS-N Ideias, Tencent). Pull ff-only OK na 1ª (12:13).
> **Bloco:** `IDEIA_PRO_DSNUVEM_IDEIAS-016` — DSH-us65 (ordem do maestro ~09:2x), carimbo `20260905 12:05 BRT`, bloco em `cerebro/Foruns/ponte_laura_completa/de_dell.md` (~18451-18460). "Na fila após a IDEIA-015" (bloco X/Facebook, processado na mesma ronda).
> **Fluxo da casa (do bloco):** Ideias desenvolve → DS-N Chefe aprova → resumo ao MIGUEL pelo @Dsnchefe_bot.
> **Refs:** DS YouTube (`Foruns/youtube/canal_ds_youtube.md` + `queue_youtube.md`: loop 15/15 Tencent, porta Dell residencial p/ download, rascunho-only draft 5801, gate CL, quem publica é o Publicador — ordens 01/09) · régua anti-rajada do canal: **≥2h entre vídeos, máx 6/dia** (ordem Miguel 04/09 22:55; confirmada na grade; freno 60min/6dia do Chefe 04/09 18:40 superado pela ordem do dono) · IDEIA-009 carrossel reels (`2026-09-02_video_vertical_espelho_reels.md` + forum_carrossel_videos_miguel_captacao_automatica_20260902.md: cortes 9:16 fundo blur + legenda assada, cat 28, thumbnail_oficial_video) · IDEIA-010/011 (esteira cortes da live do Miguel, TV Fórum @forumrevista, relógio 23h/08h) · forum_video_diario_multirrede_20260723.md (YouTube Shorts publicado após re-auth; TikTok inbox/rascunhos OK sem auditoria; publish direto exige app auditado — "Rota de Sangue Azul") · IDEIA-013 (padrão Bertrand/Norton: voz externa com crédito — citar autor, link, falar dele; NUNCA apropriar) · regra-mãe: robô não posta em rede social; publish = mão do Miguel ou rascunho que ele aperta · §82 segredos · regra 409 (1 consumidor por token) · porta-download residencial do Dell com yt-dlp instalado pela CL (05/12, CL-006; prova do dia: 6qXIQKXCHAQ baixado) · manual do publicador (cerebro/Estilo/manual_do_publicador.md, 05/09): só o publicador ou o Miguel publica; robô e agente YouTube entregam rascunho.
> **Natureza:** ESTUDO/ARQUITETURA/PLANO — NADA executado em produção (Lei de Poderes). Nenhum valor de chave neste arquivo (§82).
> **Marcador:** `PRONTO_BLOCO016_ESTRATEGIA_YOUTUBE_TIKTOK`

---

## 0. Resumo executivo (o veredito do arquiteto)

1. **YouTube do Cafezinho = 2 realidades que não se misturam:** (a) o **canal TV Fórum (@forumrevista, ~982 mil inscritos)** — do programa do Miguel, administrado por ele; a casa usa como FONTE (download → matéria no site) e destino dos cortes é o SITE (cat 28), não o canal; (b) a **operação DS YouTube** (Tencent 15/15) que produz matérias-rascunho no site a partir de vídeos públicos — draft-only, gate da CL, régua ≥2h/máx6. **Community posts e upload de shorts no YouTube pressupõem um canal que a casa GERENCIA** — não há registro de canal próprio do Cafezinho no YouTube (o upload do Short em 23/07 foi num canal cujo dono não está documentado). **Pergunta nº 1 ao Miguel: qual canal é "o do Cafezinho" para a casa operar (community posts + shorts)?** Sem essa resposta, os itens 1a/1b do bloco ficam em desenho condicional.
2. **Community posts (texto no YouTube):** viável SÓ em canal elegível (a aba Comunidade exige ~500+ inscritos e canal sem restrições; canal recém-criado não tem). Formato recomendado: 1-2/dia, texto curto + imagem (capa/arte da casa), anúncio da matéria do dia com link — **link no comentário fixado** (community post com link externo no corpo perde alcance; e o YouTube é ecossistema fechado). Régua: mesma anti-rajada (≥2h, máx 6/dia — para community posts recomendo máx 2-3/dia).
3. **Shorts:** o ativo JÁ EXISTE — os cortes verticais 9:16 do carrossel IDEIA-009 (cortes da live do Miguel: hook 3s + beats + CTA, legenda amarela assada, ffmpeg provado no teste Kakay). **1 gravação serve a 4 destinos:** site (carrossel) + YouTube Shorts + TikTok + IG Reels. Upload via YouTube Data API (escopo youtube.upload; o token `token_youtube.json` já existiu no /root da Tencent — **revalidar**; lição 23/07: client secret revogado derruba upload). Cadência: 1-2 shorts/dia, ≥2h entre eles, contando na régua do canal.
4. **Republicação com legendas (pipeline):** o DS YouTube JÁ faz a versão "site" (baixar → transcrever → matéria com citação). A novidade do bloco = **escala + licenças**: usar a porta residencial do Dell (yt-dlp instalado 05/12) com **filtro de licença Creative Commons** (`--match-filter "license=creativecommons"`) + watchlist de canais que autorizam (padrão Bertrand/Norton da IDEIA-013: citar autor, link, falar dele — NUNCA canal que proíba). Veredito: republicar VÍDEO baixado de terceiro no canal da casa exige licença CC ou autorização escrita; sem isso, o caminho é o atual (matéria no site com embed/citação), não upload.
5. **TikTok — abrir a frente SEM quebrar a regra-mãe:** o fluxo de 23/07 provou que o endpoint de **rascunhos (inbox) funciona sem app auditado** — ou seja, dá para o robô subir o vídeo como RASCUNHO e o Miguel finalizar com 1 toque (regra-mãe intacta). Publicação 100% automática exige submeter o app à auditoria do TikTok ("Rota de Sangue Azul"). Conta do Cafezinho no TikTok: **não há credencial de API na casa** (VAGA 01/09) e o dono da conta usada em 23/07 não está documentado — **pergunta nº 2 ao Miguel**.
6. **Gerenciador:** NÃO construir GUI na fase 1. A casa já gerencia em markdown + fila (padrão `queue_youtube.md`) — estender para um **painel único multi-rede em `Foruns/redes_sociais/`** + **comandos DSC no Telegram** (item 5 do bloco) + relatório diário. GUI web fica como fase 2 documentada (escopo read-mostly), com a mão de quem constrói painéis na casa (ZM/Moka) só se o Miguel pedir.
7. **Comandos DSC (o Miguel manda pelo @dscelular_bot; o DSH-us65 executa com facilidade):** desenho no §7.3 — `dsc status youtube|tiktok`, `dsc fila youtube|tiktok`, `dsc agenda`, `dsc metricas youtube|tiktok`, `dsc pausa|retoma <recurso>`, `dsc proximo corte`. Saída em texto limpo (regra permanente: sem asterisco/jogo da velha) e sempre com a hora real.

---

## 1. ESTADO DA ARTE (o que a casa JÁ tem — nada se constrói do zero)

| Peça | Estado (05/09) | Ref |
|---|---|---|
| Download YouTube por IP residencial | ✅ porta do Dell em produção (cron; yt-dlp instalado pela CL 05:12 05/09; prova do dia 6qXIQKXCHAQ) | canal_ds_youtube.md · CL-006 |
| Transcrição (legendas YT / Whisper) | ✅ prática da casa (decupagens; faster-whisper na Tencent) | Foruns/youtube/decupagens/ |
| Matéria no site a partir de vídeo (cat 28) | ✅ DS YouTube 15/15 — **rascunho-only** (conta cafezinhodsn1/5801), gate CL, publicação pelo Publicador | canal_ds_youtube.md (ordens 01/09) |
| Régua anti-rajada do canal de vídeo | ✅ **≥2h entre vídeos, máx 6/dia** (grade; ordem do Miguel 04/09 22:55) | de_dell.md DS-N 173º |
| Cortes verticais 9:16 (carrossel IDEIA-009) | 🔧 arquitetura + esteira de cortes da live (23h/08h) desenhada (IDEIA-010/011); produção do corte testada (Kakay) | ideias/2026-09-02_* |
| Upload Shorts no YouTube | ✅ PROVADO 23/07 (após re-auth; token em /root/token_youtube.json; **revalidar**) | forum_video_diario_multirrede (adendo 3) |
| TikTok inbox/rascunhos | ✅ PROVADO 23/07 (upload 201, publish_id; app não auditado → rascunho + 1 toque) | idem (adendo 3) |
| TikTok publish direto | ❌ bloqueado (app dev não auditado) — caminho: auditoria ("Rota de Sangue Azul") | idem |
| TikTok credencial de API na casa | ❌ NÃO (VAGA 01/09: "TikTok sem credencial"; token antigo existiu em /root/.env.unificado) | VAGA_DS_NUVEM_REDES |
| Padrão de crédito p/ voz externa | ✅ IDEIA-013 (Bertrand/Norton: citar, linkar, falar dele; nunca apropriar) | ideias/2026-09-05_ideia013 |
| Gerenciamento de fila | ✅ padrão markdown `queue_youtube.md` (status: PENDENTE/BAIXADO/ENTREGUE_GATE/ERRO) | Foruns/youtube/ |
| Regra-mãe publicação em rede social | ✅ robô não posta; publish = mão do Miguel/rascunho que ele aperta | sprint 31/08 + tema2 DSC 01/09 |

---

## 2. OS 5 PONTOS DO BLOCO, DESENVOLVIDOS

### 2.1 YouTube completo

**(a) Postar TEXTO (community posts):**
- **Pré-requisito:** aba "Comunidade" só em canal elegível (~500+ inscritos, sem restrições). O TV Fórum (982 mil) é elegível, mas é o canal do programa do Miguel — a casa não administra. Canal próprio do Cafezinho: criar + elegibilidade leva tempo (500 inscritos).
- **Se o canal for o TV Fórum (operação pelo Miguel):** a casa entrega o TEXTO pronto do community post no pacote (como o manual criativo faz para X/FB) e ele cola — cadência 1-2/dia, texto curto + imagem (capa da matéria), link no comentário fixado.
- **Se for canal próprio da casa:** o robô (com o token OAuth youtube.upload + escopo de community post — a API de community posts é a mesma Data API, endpoint `liveChat`? não: community posts via API têm suporte limitado/oficialmente não há endpoint público estável para criar community posts — **verificar na execução**; historicamente o YouTube não expõe criação de community posts na Data API v3; apps fazem via interface). → Recomendação honesta: **community post é operação semi-manual** (texto pronto no pacote) até o YouTube expor API; não prometer automação que a plataforma não dá.
- Régua proposta: 1-2/dia, sempre com imagem, sem título+link pelado (gancho de 1 frase), horário 11:00-13:00 / 18:00-20:00 (janelas do manual).

**(b) SHORTS:**
- **Formato:** os MESMOS cortes verticais da esteira IDEIA-009/010/011 (9:16 1080×1920, ≤60s, legenda amarela assada, hook 3s, CTA "segue o Cafezinho" ou "link na descrição"; regra de Margem ≤100 — bug PlayResY=288 documentado). Um corte = 4 destinos (site carrossel, YT Shorts, TikTok, IG Reels).
- **Cadência:** 1-2/dia na fase 1; **compatível com a régua anti-rajada** (≥2h entre shorts; shorts contam no teto diário do canal — máx 6/dia somando tudo; recomendo máx 2 shorts + 1 longo/dia).
- **Upload:** YouTube Data API v3 `videos.insert` com `snippet.categoryId` apropriado; token OAuth do canal operado (revalidar `token_youtube.json` — lição 23/07 do `invalid_client`).
- **Título/descrição:** título = gancho do corte (não o título do site); descrição com link do post completo + crédito do programa (padrão da casa: citação + link + timestamps no PAUTA-CHEQUE interno, sem timecode no corpo — ordem 01/09).
- **Gate:** shorts que vão ao AR no canal passam pelo mesmo rito de revisão dupla Chefe→CL (regra da grade) ANTES de qualquer publicação — e publicação no canal do Cafezinho segue a regra-mãe (mão do Miguel ou rascunho que ele aperta) enquanto ele não liberar o estágio 2.

**(c) Vídeo longo:** já opera no SITE (DS YouTube cat 28, draft-only + gate + régua). Upload de vídeo longo NO CANAL do YouTube (ex.: a live de 2h ou o programa) é operação do Miguel no TV Fórum — a casa pode ajudar com título/descrição/meta, mas não é abertura nova de robô.

### 2.2 Pipeline de republicação (canais públicos → baixar → legendar → republicar)

- **O que é possível:** o fluxo baixar→transcrever→legendar JÁ roda (DS YouTube + porta Dell + Whisper). A régua de DIREITO é o ponto novo:
  - **Canais/vídeos com licença Creative Commons** (o YouTube permite filtrar: `yt-dlp --match-filter "license=creativecommons"`): republicação permitida com atribuição — crédito visível (canal/autor, link, "falar dele" — padrão Bertrand/Norton da IDEIA-013).
  - **Licença padrão do YouTube:** republicar o VÍDEO baixado no canal da casa NÃO é permitido sem autorização; o que a casa faz (e segue fazendo) é matéria no site com citação curta + embed + crédito (uso jornalístico, nunca cópia integral — regra do canal DS YouTube).
  - **Watchlist de canais autorizadores:** montar lista curta (começar com canais institucionais/acadêmicos/gov que usam CC — verificar licença vídeo a vídeo na execução; a casa já tem allowlists de fontes geo/tec nos coletores, mesmo espírito). NUNCA canal que proíba (termos do canal prevalecem).
- **Fluxo proposto (fase 1, escala controlada):** watchlist (10-20 canais CC) → porta Dell baixa com filtro CC → Whisper legenda → validação de licença (2ª checagem manual/LLM: license=creativecommons + termos do canal) → matéria rascunho cat 28 (padrão atual) OU upload com atribuição se for canal operado pela casa → dedupe por ID do YouTube (banco de IDs usados — anti-repetição) → gate CL → publicação pelo Publicador.
- **Cadência:** respeitar a régua da grade (≥2h, máx 6/dia no total de vídeos publicados no site). A fila do DS YouTube (queue_youtube.md) ganha a coluna "licença" (CC/padrão/autorizado).

### 2.3 TikTok — abrir a frente

- **Conta:** pergunta ao Miguel (nº 2): qual conta? (a) criar conta oficial do Cafezinho (recomendado — o espelho precisa de conta da casa; IG @ocafezinhooficial já é da casa; padrão de naming a confirmar) ou (b) usar conta existente (a de 23/07?).
- **API:** **Content Posting API** — o fluxo de 23/07 é a base: (1) `POST /v2/post/publish/inbox/video/init` (rascunho) → upload 201 → publish_id → o Miguel finaliza no app (1 toque) — **funciona sem auditoria e respeita a regra-mãe**; (2) publicação direta (`/v2/post/publish/video/init` com app auditado) — só depois de submeter o app à revisão do TikTok ("Rota de Sangue Azul", fórum forum_adesao_tiktok.md da memória) + ✓ do Miguel (estágio 2).
- **Formato:** os MESMOS clips verticais do carrossel (IDEIA-009) — 1 gravação serve TikTok + Shorts + Reels + site. Legenda automática sempre (80% vê sem som); hashtags 3-5 (manual §5.3); CTA "segue o Cafezinho".
- **Régua própria:** 1-2/dia, ≥2h entre posts, janela 12:00-13:30 / 19:30-21:30 (manual §5.4), dedupe de vídeo (ID do YouTube de origem), noturno respeitado. **Anti-rajada igual ao YouTube** (a régua da casa é transversal).
- **Métricas:** views/plays por vídeo — o Miguel lê no app e responde 1 número (regra do manual §7); se o app for auditado, Insights da API entram no relatório.

### 2.4 Gerenciador do Cafezinho (YouTube/TikTok)

- **Fase 1 (recomendada — markdown + bot, a casa aprende a gerenciar antes de construir painel):**
  1. **Painel multi-rede em `cerebro/Foruns/redes_sociais/`**: `PAINEL_REDES.md` (status de cada rede: canal/conta, fila, últimos posts, régua ativa, token health sem valores, pendências) — espelho do `queue_youtube.md`, uma seção por rede (site-vídeo, YouTube, TikTok, X, FB). Atualizado a cada postagem/erro.
  2. **Fila única por rede** (formato do queue_youtube: PENDENTE/BAIXADO/PRONTO/RASCUNHO_CRIADO/PUBLICADO/ERRO + próxima ação/dono/prazo).
  3. **Relatório diário** no Telegram do Miguel (links, status, métricas de 1 número por peça) + relatório semanal de calibração (manual §7).
  4. **Registro em `Relatorios/redes_sociais/AAAA-MM-DD.md`** (regra DSC-006).
- **Fase 2 (GUI — só se o Miguel pedir):** painel web read-mostly (fila, status, métricas dos canais, agenda; ações = aprovar/agendar com login do dono). Onde: aplicação simples na Tencent (a casa tem gateway/portas; quem constrói painel: ZM/Moka com a régua de segurança da casa); escopo e custo aprovados antes. Não é pré-requisito para a operação.

### 2.5 Comandos DSC (o Miguel atualiza pelo @dscelular_bot; DSH-us65 executa)

Desenho no §7.3. Princípios: resposta em **texto limpo** (regra permanente: sem asterisco/jogo da velha), sempre com hora real BRT, nunca segredo, sempre o estado lido do painel/registros (o DSH-us65 consulta os arquivos, não inventa).

---

## 3. ARQUITETURA (componentes · dados · fluxo · onde roda)

```
[Fontes: live/canais públicos (watchlist CC)]  →  [PORTA DE DOWNLOAD — Dell residencial, yt-dlp]
        | filtro license=creativecommons · grava live em tempo real (esteira IDEIA-010)
        v
[DS YouTube — Tencent 15/15]  transcrição (legendas YT/Whisper) → decupagem → matéria cat 28 (rascunho 5801)
        | corte 9:16 (ffmpeg blur+legenda) p/ carrossel do site  ←  MESMO MP4 p/ shorts/tiktok/reels
        v
[REGRA transversal: ≥2h · máx 6/dia · dedupe por ID do YouTube · janela diurna · retry ≥60s]
        v
[PUBLICADOR por destino]
   site (cat 28): rascunho → gate CL → Publicador (prova REST)   [JÁ OPERA]
   YouTube (shorts/community): pacote p/ mão do Miguel (fase 1) → upload API (fase 2 c/ ✓)
   TikTok: inbox/rascunho via Content Posting API (fase 1, 1 toque do Miguel) → direto (fase 2, app auditado)
        v
[GERENCIADOR: PAINEL_REDES.md + filas + Relatorios/redes_sociais/ + comandos DSC + relatório diário]
```

- **Componentes:** porta Dell (existe) · DS YouTube (existe) · cortador 9:16 (existe, esteira IDEIA-010) · uploader YT shorts (reusar `agente_youtube_v2_publicador.py` legado + token revalidado) · uploader TikTok inbox (reusar fluxo `pipeline_cafezinho_to_tiktok.py` de 23/07) · painel/filas (markdown novo) · comandos DSC (leitura do painel pelo DSH-us65).
- **Dados:** fila por rede (id_origem YouTube, título, licença, status, id_api, ts) · registro diário · métricas (1 número/peça). Nenhum valor de chave em arquivo (§82).
- **Onde roda:** Tencent (DS YouTube, uploaders, painel, relatório) · Dell (porta de download — único IP que passa no bloqueio do YouTube) · NYC intocada · o app/cliente OAuth do YouTube/TikTok: **1 consumidor por token (regra 409)** — um único robô por credencial.

---

## 4. PLANO DE EXECUÇÃO (passos numerados, riscos, reversibilidade)

| # | Passo | Quem (proposta) | Risco | Reversível? |
|---|---|---|---|---|
| 0 | Miguel decide: (1) qual canal a casa opera no YouTube; (2) conta do TikTok; (3) fase 1 (rascunho/pacote) ou fase 2 (automático c/ ✓) | Miguel via Chefe | decisão de conta errada | sim (reconfigura) |
| 1 | Revalidar `token_youtube.json` (OAuth youtube.upload) com backup do client antigo; registrar expiração | ZM + Miguel (login 1×) | token quebrado (lição 23/07) | sim (backup; re-auth documentado) |
| 2 | App TikTok: re-registrar/validar credencial de inbox (rascunhos) — sem auditoria na fase 1 | ZM + Miguel (login) | token antigo perdido (lição 23/07) | sim |
| 3 | Watchlist de canais CC (10-20) + checagem de licença vídeo a vídeo (prova em 2 leituras) | DS-N Ideias/DS YouTube | canal "CC" com termos restritivos | sim (lista é config) |
| 4 | Uploader de shorts: 1º teste REAL em rascunho/privado no canal operado (nunca público sem gate) | executor (DS YouTube/ZM) | vídeo errado no ar | sim (privado/rascunho não é público) |
| 5 | Uploader TikTok inbox: 1º teste real em rascunho (o Miguel finaliza com 1 toque) | executor | app não auditado limita | sim (rascunho não publicado) |
| 6 | Painel multi-rede + comandos DSC + relatório diário (fase 1) | DS-N Ideias desenha; DSH-us65/Chefe operam | painel desatualizado | sim (markdown versionado) |
| 7 | (Só com ✓) Fase 2: publicar automático (shorts/community/TikTok direto) com régua + telemetria | executor | regra-mãe revogada | sim (volta à fase 1 por config) |

**Rollback escrito:** rascunho/privado nunca é público → apaga/ignora sem dano; se algo publicar errado (fase 2), o Miguel remove na plataforma (1 toque) e a casa registra a lição. Protocolo casa: backup (tokens/lista) → prova (teste rascunho) → registro (relatório) → rollback escrito (config de pausa por rede).

---

## 5. RISCOS ESPECÍFICOS (além da tabela)

1. **YouTube não tem API pública estável p/ community posts** → o item 2.1a é semi-manual por natureza; não prometer automação que a plataforma não dá (verificar na execução se surgiu endpoint).
2. **Token YouTube `invalid_client`** recorrente (23/07) → rotina de revalidação com lembrete (lição: client secret antigo deletado derruba upload).
3. **App TikTok não auditado** → só rascunhos; publish direto depende da auditoria (processo externo, prazo não controlável).
4. **Canal errado (qual é "o do Cafezinho")** → perguntas 1-2 do §6 são pré-requisito; operar canal alheio = risco de ban/ruído.
5. **Rajada** (lição YouTube: 4 vídeos em 1 min = "fora do controle") → régua ≥2h/máx6 é inegociável e vale para TODAS as redes novas.
6. **Custo de LLM** no pipeline (legendar/decupar) → reusar o caminho barato da casa (legendas YT primeiro, Whisper local, flash p/ texto — nunca modelo caro em esteira de vídeo).

---

## 6. DECISÕES QUE PRECISO DO MIGUEL (via DS-N Chefe — resumo ao @Dsnchefe_bot)

1. **Qual canal a casa opera no YouTube** para community posts e shorts? (TV Fórum do programa dele? canal próprio do Cafezinho a criar? outro?)
2. **Conta do TikTok do Cafezinho:** criar oficial ou usar existente? (a casa não tem credencial de API de TikTok hoje)
3. **Fase 1 (rascunho/pacote + 1 toque dele — regra-mãe intacta) ou já fase 2 (robô publica, com app auditado e ✓)?**
4. **Cadência:** 1-2 shorts/dia + 1-2 community posts/dia + 1-2 TikToks/dia está bom como teto inicial? (régua ≥2h transversal)
5. **Watchlist de canais CC:** ele indica canais que autorizam republicação (ou aprova a lista que a casa montar)?
6. **Painel:** markdown + comandos DSC primeiro (recomendado) ou ele quer GUI já?

## 7. RASCUNHOS (dentro do arquivo da ideia — nunca em produção)

### 7.1 Config multi-rede (esqueleto — sem chaves)

```json
{
  "youtube": {"canal": "A DEFINIR (pergunta 1)", "shorts_dia_max": 2, "community_dia_max": 2, "token_arquivo": "token_youtube.json"},
  "tiktok": {"conta": "A DEFINIR (pergunta 2)", "dia_max": 2, "modo": "inbox_rascunho"},
  "regua_global": {"min_intervalo_min": 120, "max_videos_dia_site": 6, "dedupe_por_id_youtube": true, "janela": "07:30-21:30 BRT"},
  "watchlist_cc": ["<canais com license=creativecommons — montar na execução>"],
  "yt_dlp_filtro": "--match-filter \"license=creativecommons\""
}
```

### 7.2 Painel de redes (formato da fase 1 — `Foruns/redes_sociais/PAINEL_REDES.md`)

```
# Painel de Redes do Cafezinho — 05/09/2026
## YouTube (canal: A DEFINIR)
- fila: 2 PENDENTE (IDs ...) · 1 RASCUNHO cat 28 (268xxx) no gate CL · 0 ERRO
- último shorts: -- | último vídeo-site: 268xxx (hora) | régua ok
## TikTok (conta: A DEFINIR)
- fila: 0 | rascunhos inbox: 0 | publish direto: bloqueado (app não auditado)
## X / Facebook — ver bloco 015 (rotina espelho)
```

### 7.3 Comandos DSC (respostas em texto limpo, sem asterisco — regra permanente)

| Comando do Miguel | O que o DSH-us65 responde (lendo o painel/registros) |
|---|---|
| dsc status youtube | canal, fila (pendentes/prontos/gate), último publicado + hora, régua ok/suspensa |
| dsc status tiktok | conta, rascunhos no app, publish direto liberado? (auditoria), último + hora |
| dsc fila youtube | lista da fila: título curto, status, próxima ação, dono |
| dsc fila tiktok | idem |
| dsc agenda | próximos agendados do dia (site/shorts/tiktok) com horas BRT |
| dsc metricas youtube | views do último shorts/vídeo (1 número que o dono passar ou API) |
| dsc metricas tiktok | idem |
| dsc pausa youtube | marca pausa na config + avisa a régua (nada programa enquanto pausado) |
| dsc retoma youtube | desmarca |
| dsc proximo corte | o próximo corte da esteira IDEIA-010 (23h/08h) com status |

### 7.4 Linha de registro diário (regra DSC-006)

```
05/09 — REDES (YOUTUBE/TIKTOK)
- video 6qXIQKXCHAQ baixado (porta Dell) -> rascunho cat 28 268xxx no gate CL (hora)
- shorts 9:16 do corte 23h gerado (mp4 ...) -> rascunho YT/TikTok (hora)
- licença checada: canal CC ok (link) | views (resposta do Miguel): ...
```

---

## 8. NOTA DE MÉTODO

Este bloco (016) e o bloco 015 (X/FB) chegaram juntos ao repo às 12:05 (o 015 com carimbo 09:20) e foram processados na MESMA ronda 12:15-12:40. As duas ideias compartilham a régua anti-rajada, a regra-mãe de publicação e o desenho de comandos DSC — recomendo ao Chefe apresentá-las ao Miguel no MESMO resumo (rotina de presença das redes da casa é um único programa com 2 frentes: espelho X/FB + YouTube/TikTok).

— DS Nuvem Ideias (DS-N Ideias) · 20260905 12:19:33 BRT
