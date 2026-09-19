# 🎬 Fórum — Esteira de cortes da LIVE DIÁRIA do Miguel (YouTube 20h-22h) → 2 cortes/dia no carrossel da home

**Data:** 02/09/2026 · **Origem:** ordem do Miguel por voz, ~18:2x BRT (sessão ZM us65/cafezinho-wp). **Esta versão (v2) SUBSTITUI a leitura anterior** — o Miguel decidiu tudo de novo e mandou não amarrar em decisões antigas.
**Companion:** IDEIA-009 (`Foruns/ideias/2026-09-02_video_vertical_espelho_reels.md`) = o carrossel na home. Este fórum = a **esteira de captação** que alimenta o carrossel com os vídeos DELE.
**Estado:** arquitetura + encaminhamento ao DS-N Ideias (bloco IDEIA_PRO_DSNUVEM_IDEIAS-010 em `ponte_laura_completa/de_ideias.md`). Nada executado.

---

## 1. A decisão do Miguel (02/09, voz → texto, fiel)

1. **Faço uma live diária pelo YouTube, de 20h às 22h.**
2. **Quero um robô para baixar essa live** e pegar os pontos importantes.
3. **Eu dou o sinal do corte falando uma palavra na live** — "eu falo uma palavra e aí você bate". O robô pega a transcrição **com os carimbos de tempo**, acha a palavra e corta em volta.
4. **2 cortes por dia** (o programa tem 2h):
   - **Corte 1: 23h da mesma noite** — direto ("tem que entrar já um corte à noite, 11 da noite, direto");
   - **Corte 2: 8h da manhã seguinte** — "aproveitar, ficar bem fresquinho".
5. Os cortes entram **no carrossel da home** (2º bloco, os vídeos do Miguel — decisão da sessão anterior, mantida).
6. **Encaminhar ao DS-N Ideias** com o contexto todo, pedindo análise.

### ✅ Aprovações do Miguel (~18:50 BRT, mesma sessão)

- **Relógio 23h/08h: APROVADO.**
- **Canal: TV Fórum** — "o canal é TV Fórum, aí tem uma playlist lá que é o **Jornal da Fórum**, que é meu programa. Vê se consegue achar lá."

## 1.5 O alvo (achado e confirmado)

| Item | Valor |
|---|---|
| Canal | **TV Fórum** — YouTube **@forumrevista** · channel ID **`UC3sMBA3BdnsKSVI0WB9yVWQ`** (~982 mil inscritos) |
| Programa | **Jornal da Fórum** — âncora **Miguel do Rosário**, ao vivo **20h-22h** todo dia |
| Playlist | "Jornal da Fórum" (confirmação do Miguel; ID mecânico a resolver na Fase 0 via porta Dell — o canal tem playlists por programa; referência conhecida: Fórum 11:30 = `PL0M7rdgIk2iifjePO89emPPttp8cELtUg`) |
| Padrão real do canal | Jornal entra como **premiere** com título "**Jornal da Fórum dd.mm.yy**" e é **RENOMEADO para manchete com "\|"** depois do ar → casar por título+data só vale na janela pós-programa |

### O que a casa JÁ TEM pronto pra esse canal exato (não é do zero)

1. **Robô que acha a edição do dia JÁ EXISTE**: modo `--jornal` do `youtube_cafezinho.py` (cron `30 22` + `0 23`) — acha a edição diária há ~6 semanas, com **juiz LLM** (cascata DeepSeek→AssemblyAI→Kimi) que confirma qual live longa é o Jornal (exclui Fórum 11:30/Fórum Café/Brocou/Trilhas da Urna/Fórum Livre). Validado em produção, certeza 10. A esteira de cortes **herda esse achador**.
2. **Transcrição de 2h é RÁPIDA**: Transkriptor ~1h de vídeo ≈ 3min — edição de 2h08 virou 103k chars em ~5min → transcrição pronta ~22h30-22h40, **SLA das 23h folgado** (fallback S3/Whisper existe).
3. **Porta residencial já patrulha TV Fórum** (prova E2E 17/08: 16min → 13.032 chars, US$ 0,098).
4. **Banco de nomes do pessoal da TV Fórum** (evita errar nome nos títulos dos cortes).
5. Player/verticalização: teste Kakay (Jornal da Fórum, `Od9sKT0q_Qk`) já provou o corte 9:16 fundo blur + legenda assada ponta a ponta — **com vídeo deste mesmo programa**.

## 2. Arquitetura — o relógio de todo dia

| Hora | O que acontece | Como |
|---|---|---|
| **20h00** | Live começa no YouTube · **robô começa a GRAVAR a live em tempo real** | yt-dlp na URL da live, pela porta residencial (Dell — único IP que passa no bloqueio do YouTube). Gravar ao vivo elimina a espera do VOD |
| **22h00** | Live acaba → **MP4 de 2h já está local** (não depende de o VOD ficar pronto no YouTube) | fallback: o baixador existente trata live ativa → `AGUARDANDO_VOD` |
| **22h00-22h20** | **Transcrição COM carimbos de tempo** | legendas automáticas do YouTube (baixadas junto); se atrasarem → Whisper no áudio (caminho robusto da casa) |
| **22h20-22h40** | **Detecção da palavra-sinal** + corte | busca da palavra-senha na transcrição com timestamps → cada ocorrência = 1 candidato |
| | | **ffmpeg** por corte: início na palavra (ou ~20s antes p/ contexto) · 30-90s · fechamento em frase completa (LLM) · **9:16 1080x1920, fundo blur do próprio vídeo** · **legenda amarela assada** (libass, MarginV ≤ 100 — bug PlayResY=288 documentado) · loudnorm · < 10MB |
| **22h40-23h00** | Upload + agendamento | MP4 → **biblioteca de mídia do WP** (URL pública provada; vídeo servido pela própria casa = público NÃO sai do site) · post na **cat 28 (Vídeos)** + meta `thumbnail_oficial_video` (nunca entra na caça de capa — ZM-042) · publish agendado |
| **23h00** | 🔴 **CORTE 1 NO AR** — quente, 1h após o fim da live | vai direto pro carrossel (2º bloco da home) |
| **08h00** | 🔴 **CORTE 2 NO AR** — "bem fresquinho" da manhã | idem |
| **08h05** | Relatório do dia no Telegram do Miguel | links dos 2 cortes + trecho da transcrição de cada + flag se algum foi "auto" |

### A palavra-sinal (o coração do esquema)

- **Miguel fala a palavra AO VIVO no momento bom** → a palavra DELE é a escolha editorial dele → o corte marcado por sinal **publica direto** nos horários (23h/08h), sem esperar aprovação.
- Palavra-senha a confirmar com o Miguel — precisa ser curta, inconfundível, que não ocorra naturalmente no programa. Candidatos: **"CORTA!"** · "ESSE AQUI!" · "PEGA!" (decisão dele; gravar a escolha no config da esteira, com variantes aceitas).
- Sinal paralelo opcional: teclar 🔥 no bot do Telegram durante a live (mesmo efeito, cai na mesma fila).
- **Fallback (nenhum sinal na live):** LLM lê a transcrição com timestamps e escolhe os 2 melhores momentos (tese forte, frase de efeito) → esses entram marcados **"auto"** no relatório do dia — primeira semana opcionalmente com ✓ no Telegram até ganhar confiança.
- 2+ sinais numa live: os 2 primeiros sinais viram os 2 cortes do dia; sobras ficam em banco (reuso futuro em redes).

### Por que vídeo self-hosted (e não embed do YouTube)

Objetivo declarado do Miguel: **manter o público no site**. Embed do YouTube vaza público (botão "assistir no YouTube" + recomendações ao fim). MP4 na biblioteca do WP com player nativo `<video>`: autoplay mudo permitido, swipe/setas, tela cheia, só o slide ativo carrega — e o público fica no Cafezinho. (Detalhe: quem quiser assistir a live inteira, o CTA leva ao canal dele — saída consciente, não vazamento.)

## 3. O que já existe e é reaproveitado (nada se constrói do zero)

| Peça | Estado |
|---|---|
| Baixar YouTube por IP residencial (live→VOD, legendas, thumbnail) | ✅ porta do Dell em produção (cron */5, `AGUARDANDO_VOD` já tratado) — **novo: modo gravar-a-live-em-tempo-real** |
| Transcrição (legendas YT / Whisper) | ✅ prática da casa |
| ffmpeg 9:16 fundo blur + legenda assada | ✅ técnica provada em ponta a ponta (teste Kakay: 1080x1920 fundo borrado, legendas assadas, <60s, ~7MB) |
| Biblioteca de mídia WP servindo vídeo público | ✅ provada (foi a fonte de URL pública que publicou Reels) |
| Carrossel reels na home (2º bloco) | 🔧 engatilhado — IDEIA-009 §6 (rascunho pronto; ajuste: `<video>` self-hosted no lugar de iframe) |
| Cat 28 + `thumbnail_oficial_video` | ✅ regra viva (ZM-042) |
| Agendar publish 23h/08h | ✅ WP `post_status=future`, padrão da casa |
| Medir permanência | ✅ GA4 (property da casa) — `averageEngagementTime` antes/depois → Baleia Azul |

## 4. Fases

- **Fase 0 (destravar — só depende do Miguel):** URL do canal da live + palavra-senha confirmada + ✓ do relógio 23h/08h.
- **Fase 1 (espelho, 1ª semana):** esteira completa apontada pro espelho `cafezinho.news`; 2 cortes/dia; relatório diário no Telegram; GA4 baseline; ajuste fino dos cortes com feedback do Miguel.
- **Fase 2 (canônico):** após validação visual dele → portar pro `ocafezinho.com` (rito da casa: espelho primeiro, canônico certinho depois).
- **Fase 3 (redes):** mesmos MP4 alimentam Reels IG/FB, Shorts, TikTok, X — grava 1×, publica em tudo.

## 5. Riscos e mitigações

| Risco | Mitigação |
|---|---|
| VOD demora a ficar disponível no YouTube | **gravar a live em tempo real** desde as 20h (o MP4 fica pronto às 22h em ponto) |
| Legendas automáticas atrasam | Whisper no áudio (robusto); SLA interno 22h20 |
| Palavra dita "sem querer" / variação de fala | palavra-senha inconfundível + janela mínima entre sinais (ex.: 10min) + preview no relatório |
| Corte fica torto (frase no meio) | LLM fecha o corte em frase completa; ±5s de margem ajustável |
| Peso de N vídeos na home | só o slide ativo carrega; MP4 <10MB; CDN do servidor |
| Direitos | **live e voz do próprio Miguel** — zero copyright de terceiro |

## 6. Pendências do Miguel

1. ~~URL do canal~~ **✅ RESOLVIDO (02/09 ~18:50): TV Fórum @forumrevista (`UC3sMBA3BdnsKSVI0WB9yVWQ`), programa Jornal da Fórum 20h-22h.**
2. **Qual é a palavra-senha?** (proposta registrada: **"CORTA!"** — aguarda confirmação do Miguel; alternativa de teclar 🔥 no Telegram como sinal paralelo também segue aberta).
3. ~~Relógio 23h/08h~~ **✅ APROVADO (02/09 ~18:50).**

Pendência mecânica (não depende do Miguel): resolver o ID da playlist "Jornal da Fórum" na Fase 0 via porta Dell (1 comando).

---
*Registrado por ZM (GLM-5.3, sessão us65/cafezinho-wp) — 02/09/2026 ~18:40 BRT. Análise pedida ao DS-N Ideias via IDEIA_PRO_DSNUVEM_IDEIAS-010 (ponte `de_ideias.md`). Nada executado em produção.*

---

## 7. ADENDO — Qwen 3.8 (ZCode Dell): carrossel POPULADO + reprodução curada + merge com v0.3 (03/09 ~02:5x)

**Ordem do Miguel (voz, 02/09 ~22:4x):** o carrossel do espelho "foi feito sem vídeo" — botar vídeos de verdade, no mínimo 6, testar com quaisquer videozinhos, e escolher a melhor forma de segurar o leitor no site.

**Divisão de trabalho (sem pisar na Trilha B):** o módulo `cafezinho-video-reels.php` é da sessão DS-Dell/GLM-5.3; eu (Qwen 3.8) cuidei de DADOS (posts de teste) + REPRODUÇÃO (fixes de play), e depois do merge das melhorias deles.

### O que aconteceu

1. **População:** 7 posts de teste na cat 28 do espelho — IDs 400282/400284/400286/400288/400290/400292/400294 (autor 5795, publish, slugs `carrossel-video-teste-1..7.htm`), cada um com meta `_cafezinho_recorte_mp4` (MP4 self-hosted já existente nos uploads do espelho), `_cafezinho_reels_teste=1` (marcador de limpeza), `_cafezinho_img_check` (método `thumbnail_oficial_video`, regra ZM-042) e capa = pôster 720×1280 gerado por ffmpeg (frame do próprio vídeo, na Dell; o espelho não tem ffmpeg). IDs na faixa 400k = à prova de colisão com o sync horário (REPLACE INTO por ID; canônico máx ~268700).
2. **Resposta à pergunta do Miguel (melhor forma de segurar o leitor):** MP4 self-hosted no WP com `<video>` nativo — decisão já deste fórum, agora provada na prática. Embeds do YouTube só entram como fallback quando há menos de 6 recortes.
3. **Três fixes de reprodução (provados no navegador):**
   - o `<script>` do módulo saía ANTES da `<section>` → `querySelector` nulo → JS morria no load. Cura: init embrulhado em DOMContentLoaded;
   - `<video>` ganhou `autoplay` + `preload="metadata"` (autoplay por atributo é o mecanismo mais universal entre navegadores);
   - o IntersectionObserver agora TOCA o vídeo quando o carrossel entra na tela e PAUSA quando sai (antes só gerenciava o timer de 8s; o carrossel nasce abaixo da dobra e o leitor veria pôster congelado).
4. **CLOBBER + MERGE:** às 02:39 a sessão DS-Dell deployou o v0.3 (som via postMessage p/ iframes YT + CSS da página do post — melhorias reais) e sobrescreveu meus 3 fixes (carrossel congelou de novo). Fiz o merge: reapliquei os 3 fixes SOBRE o v0.3 preservando as melhorias deles. Backups no espelho: `.bak_pre_jsready_20260903` (sha a966fc67…), `.bak_pre_autoplay_20260903` (027edf55…), `.bak_pre_io_20260903` (57901d4d…), `.bak_pre_v03_dsdell_20260902_2338` (da outra sessão), `.bak_pre_merge_qwen_20260903` (6e32f122…). `php -l` limpo em todas as etapas.
5. **Provas visuais:** screenshot do carrossel com o vídeo do Kakay tocando (badge RECORTE, legenda assada, setas, bolinhas de progresso) + frame t=15,5s do vídeo China/Ormuz; avanço automático de 8s verificado (troca de slide pausa o vídeo anterior); 6 slides self-hosted no ar.

### Estado / o que falta / o que preciso de você (Miguel)

- **Pronto:** carrossel do espelho com 6 vídeos self-hosted tocando + auto-avanço + setas + som + play/pause por visibilidade; posts reais do canônico entram sozinhos via sync (o 400296 da outra sessão já apareceu).
- **Falta:** quando os cortes REAIS da Trilha B (voz do Miguel) forem publicados na cat 28 com `_cafezinho_recorte_mp4`, entram no topo automaticamente (mais novos primeiro). Posts de teste têm `_cafezinho_reels_teste=1` para limpeza futura (listar pela meta e apagar posts+anexos).
- **Preciso de você:** nada agora; vale só uma conferida visual no celular/navegador real (o navegador embutido do ZCode tem política própria de autoplay que não representa o leitor real).

Memória técnica: `Memorias/memoria_carrossel_videos_espelho_populado_20260903.md`.

---

## 8. ADENDO — Qwen 3.8 (ZCode Dell): SOM consertado de vez (v0.4) + POSTS COM MATÉRIAS DE VERDADE (03/09 ~08:4x)

**2ª queixa do Miguel (~08:1x, depois de ver o carrossel no ar):** "estava sem som o carrossel. Sem som e ligando para posts meio vazios. O carrossel tem que ter uns vídeos rolando e ligando para um post bonito escrito... uma matéria bem feita, bem escrita."

### Causa raiz do som (achada em código)

O v0.3 renderizava UM botão ♪ POR SLIDE (linha do loop), mas o JS registrava o listener só no PRIMEIRO (`root.querySelector('[data-mute]')`) e ainda RESETAVA o som para mudo a cada troca de slide (`ativar()` fazia `som_on=false; textContent='♪'`). Resultado: com o auto-avanço rodando, o leitor quase sempre via o botão de um slide que não tinha listener — clique morto; e quando funcionava, o próximo vídeo voltava mudo. Além disso o ícone era um ♪ pequeno (2,1rem) que não comunica "toque para ouvir".

### v0.4 (deploy 03/09 ~00:35, backup `.bak_pre_v04_somglobal_20260903` no espelho, php -l limpo)

1. UM único botão de som GLOBAL (fora dos slides, irmão das setas) — sempre o mesmo elemento, sempre clicável em qualquer slide.
2. SOM PERSISTE na troca de slide: `ativar()` agora re-aplica `setSom(som_on)` no novo slide em vez de resetar.
3. CLIQUE NO VÍDEO liga o som no primeiro toque (se já com som, o clique pausa/retoma) — comportamento de reels.
4. Ícone 🔇 (com pulso dourado chamando o clique) quando mudo, 🔊 quando ligado; botão maior (2,7rem) com hover; aria-label dinâmico.
5. Provado ao vivo no navegador: clique no botão → muted=false + 🔊; auto-avanço atravessou 3 slides mantendo muted=false; clique no vídeo → 🔇→🔊. Screenshot do carrossel com 🔊 visível (análise de visão confirmou o alto-falante com ondas).
6. Falsa pista registrada: `textContent` voltando vazio nos testes era o wp_emoji convertendo emoji em `<img>` (artefato de inspeção, não bug).

### Matérias completas nos 7 posts (a outra metade da queixa)

- Transcrevi os 7 MP4s com whisper large-v3-turbo na Dell (áudio real → zero invenção; o "corte-ciro-mossad" NÃO fala de Mossad — era segurança pública/IA; títulos antigos estavam errados e foram corrigidos).
- 7 matérias escritas no estilo da casa (abertura direto ao fato, citações literais da transcrição, contexto factual, sem metalinguagem), vídeo no topo via shortcode [video], títulos EMU-2 (uma frase, sem sigla) e excerpts. IDs 400282–400294 atualizados via wp-cli (post_title + post_content + post_excerpt).
- Prova visual: página do post 400294 fotografada e validada — título novo, vídeo vertical tocando bem posicionado abaixo do título, matéria começando em seguida, layout limpo.

### Estado / o que falta / o que preciso de você (Miguel)

- **Pronto:** carrossel com som usável (botão global + clique no vídeo + persistência) + cada slide liga a uma matéria completa e bem escrita. O ciclo que você descreveu — vídeo rolando → clique → post bonito — está fechado no espelho.
- **Falta:** repetir o rito com os cortes REAIS da Trilha B (sua voz) quando existirem; a esteira é a mesma (cat 28 + `_cafezinho_recorte_mp4`).
- **Preciso de você:** conferir no celular/navegador real (1) se o som liga fácil no 1º toque e (2) se o formato do post agrada — texto antes/depois do vídeo, tamanho do player etc.

*Registrado por ZCode/Qwen 3.8 (ZM, Dell) — 03/09/2026 ~08:4x BRT.*
## 9. ADENDO — ZCode/GLM-5.3 (Dell): v0.4.1 MEJS GIGANTE NO CELULAR + APAGÃO DO ESPELHO CURADO NO CAMINHO (03/09 ~09:5x)

**3ª queixa do Miguel (~09:1x, celular):** "o tocador de vídeo ficou gigantesco, quebrado... da matéria da China e a do Ciro Gomes também". E a pergunta: quem escreve essas matérias?

### Bug mobile reproduzido e curado (v0.4.1)

Reproduzido em viewport 360×740: o MediaElement (player do shortcode [video]) seta `min-width: 900781px` INLINE no `.mejs-container` (bug clássico do mejs em tela estreita — régua de controles medida errada) → página com scroll horizontal de 900.794px = "gigantesco/quebrado". Cura no CSS single do mu-plugin: `.mejs-container{min-width:0!important;overflow:hidden}` + filhos (`.mejs-inner/.mejs-mediaelement/.mejs-layers/.mejs-overlay`) com `width/max-width:100%` + `.wp-video{overflow:hidden}`. Backup `.bak_pre_v041_minwidth_20260903`. Prova pós-fix em 360px: estouro FALSE, scrollW=345, player 320×567 (proporção 9:16 correta), CSS novo presente. (Screenshot do IAB falhou intermitentemente; prova = medidas do DOM.)

### APAGÃO do espelho descoberto e curado no meio do trabalho (~09:22–09:39 BRT)

Durante o diagnóstico, o espelho parou de responder PARA O MUNDO (443 morto; porta 22 viva). Cadeia completa:

1. **Causa 1 (gatilho 09:22):** alguém rodou um search-replace MASSIVO no banco: `UPDATE wp_posts SET post_content = REPLACE(REPLACE(post_content,'controle.ocafezinho.com','cafezinho.news'),'www.oc...')` — UPDATE em TODOS os ~268k posts; wp_posts é MyISAM (table level lock) → TODA query WP ficou "Waiting for table level lock" → PHP pendurado → site morto. **AUTOR DESCONHECIDO** (não fui eu; não está no cron do root nem no bash_history — pendência forense para a casa). A query foi KILLada (replace é idempotente, pode ser refeito com o site no ar e em blocos).
2. **Causa 2 (explosão latente):** config do nginx com `fastcgi_read_timeout 25` DUPLICADO no mesmo bloco desde 29/06 — todos os reloads desde então falhavam em silêncio; meu restart às 09:33 expôs: nginx não subia. Cura: removidas as duplicatas (linhas 39/52), backup em `/root/backups_nginx/cafezinho-news.bak_pre_dupfix_20260903` (backup FORA de sites-enabled — dentro, o nginx carrega como config extra!).
3. **Causa 3 (ruído):** 3 sondas externas de SQL injection com SLEEP() no banco (ids 118381-83) — KILLadas.
4. **Extra:** IP IPv4 da Dell (179.165.183.103) estava DROPado no iptables (sem registro de quem) — removido; acesso direto SSH/curl da Dell voltou (o caminho foi via jump SSH tencent→espelho).

Retorno: home 200 em 2,8s / post 200 em 0,6s. Ação de rede usada: `ssh -J tencent root@159.65.177.60`.

### Quem escreve as matérias (resposta ao Miguel, registrada)

Hoje: escrita MANUAL por ZCode (Dell) — transcrição automática whisper large-v3-turbo do áudio do corte como matéria-prima + redação com citações literais (zero invenção). NÃO há robô no circuito do carrossel ainda. Esquema futuro natural: mesma esteira do V4.1 (decupagem DSN já transcreve → redator → R1/R2 → rascunho na cat 28 com `_cafezinho_recorte_mp4`), ligável quando os cortes reais da Trilha B existirem.

*Registrado por ZCode/GLM-5.3 (Dell) — 03/09/2026 ~09:5x BRT.*
