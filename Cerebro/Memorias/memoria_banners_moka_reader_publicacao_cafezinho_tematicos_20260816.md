# Memória técnica — Estudo de publicação dos banners Moka Reader (Cafezinho + temáticos)

- **Data:** 16/08/2026 ~23:20–23:40 BRT · **Autor:** ZCode (Qwen 3.8 Max)
- **Fórum-irmão:** `Foruns/forum_banners_moka_reader_publicacao_cafezinho_tematicos_20260816.md`
- **Natureza:** SÓ LEITURA/ESTUDO. Nenhuma escrita em servidor/repo nesta fase.

## 1. Inventário dos banners

Diretório: `~/Downloads/Antigravity Google/Outros/mokareader/banners/`

| Arquivo | Bytes |
|---|---|
| `Moka Reader 300x250.html` (PT) | 135.312 |
| `Moka Reader 728x90.html` (PT) | 135.163 |
| `Moka Reader 300x250 EN.html` | 135.301 |
| `Moka Reader 728x90 EN.html` | 135.152 |

Estrutura (inspeção do PT 300x250): HTML único formato **bundler** — `<body>` com `#__bundler_thumbnail` (placeholder SVG) + `#__bundler_loading` ("Unpacking...") + script que decodifica payload base64 (fonts inclusive, MIME font/*) e faz `replaceWith` do documento no `DOMContentLoaded`. Payload contém: `<a href="https://mokareader.com">` cobrindo o banner (abre nova aba), frases rotativas PT `['Qualquer livro ou vídeo, resumido em 2 minutos. ☕', 'Aprenda mais, lendo menos.', 'Resumos inteligentes, direto ao ponto.']` trocando a cada 4 s c/ fade; EN: `['Any book or video summarized in 2 minutes', 'Learn more by reading less', 'Smart summaries, straight to the point']`. `<noscript>` avisa que precisa JS. Sem dependências externas → funciona em iframe same-origin sem CORS.
Renomear ao subir (sem espaços): `moka-300x250-pt.html`, `moka-728x90-pt.html`, `moka-300x250-en.html`, `moka-728x90-en.html`.

## 2. Cafezinho — recon nos 2 servidores (ssh `cafezinho-wp` / `root@159.65.177.60`)

**Plugins ativos relevantes (canônico):** ad-inserter (2.8.17), ads-txt, accelerated-mobile-pages, insert-headers-and-footers (vazio p/ ads — grep não achou googletag lá), ga-google-analytics, wp-rocket, wp-smush-pro, serverdoin-cdn. Espelho: idem menos AMP/wordfence/smush/rocket.

**Ad Inserter (option `ad_inserter` = `:AI:` + base64(serialize) — NÃO é JSON):** blocos 1-6 = GAM `/21622511100/cafezinho_post/cafe_mobile_1..6`; 7 = amp-ima-video; 8 = Ads Footer; 9 = Taboola `taboola-below-article-thumbnails`; 10 = half-page DFP; 11 = Interstitial googletag; 13 = flying-carpet AMP; 16 = MGID `M836425ScriptRootC1373897`; 17 = Teads; 18-19 e 24-37 = blocos `[ADINSERTER AMP]` amp-ad 300x250/320x*. **TODOS com `display_on_homepage=0`** (home livre de Ad Inserter desde 14/08).

**Slots do tema `ocafezinho-portal`** (divs vazias preenchidas client-side; gpt.js não está no tema — vem nos blocos AI):
- `single.php` L43/45 banner-before-content, L110/112 before-comments, L117/119 after-comments, L163/165 after-related, L199/201 after-recents (sempre par -desktop/-mobile).
- `front-page.php` L49 after-manchete-mobile, L69 after-colunistas-desktop, L302 after-manchete-desktop, L488 after-colunistas-mobile, L720/721 after-latest, L757/758 after-recents.

**AMP:** posts têm `<link rel="amphtml" .../amp/>`; `/amp/` HTTP 200 com ~21 `amp-ad`/`amp-fx-flying-carpet`. AMP ≈ 64% das views (análise 15/08).
**Nginx:** `root /var/www/ocafezinho`; estáticos de wp-content servidos direto (sem location especial bloqueando html).
**ads.txt canônico:** resellers programáticos (richaudience, themediagrid, contextweb, onetag, indexexchange...) — house ad não interfere.

## 3. Temáticos — registry e ads

Registry canônico: `Projeto Cafezinho Agentes/root/ferramentas/sentinela_tematicos/site_registry.json` (base_dir = Antigravity Google):

| id | url | repo | idioma |
|---|---|---|---|
| rio_carta | https://www.riocarta.com | sites-v4/riocarta | PT |
| mapa_rio | https://mapario.com.br | sites-v4/mapario | PT |
| aiatolah | https://www.aiatolah.com | sites-v4/aiatolah | **bilíngue** (EN raiz + `/pt/`) |
| global_south_news | https://www.globalsouth.news | sites-v4/globalsouth | EN |
| mundo_trilhos | https://www.mundotrilhos.com | sites-v4/mundotrilhos | PT |
| rail_post | https://www.railpost.news | sites-v4/railpost | EN |
| discover_brazil | https://www.discoverbrazil.news | sites-v4/discoverbrazil | EN |
| ceara_digital | https://ceara.digital | sites-v4/ceara | PT |

**Ads:** os 8 só carregam o loader AdSense `ca-pub-8991943608456423` (`BaseHead.astro` / `Layout.astro` do aiatolah) + meta `google-adsense-account` = **AUTO ADS**; grep `<ins` nas `src/` = 0 unidades fixas. GA4 por site (ex.: ceara G-V69T3YC32N, GSN G-E6NLZ31Y21, aiatolah G-3D6BW79H8F). `public/` tem ads.txt (ceara/gsn), hero/, images/, robots.txt.
**Deploy:** GSN push→Vercel sozinho (<1 min); **Aiatolah: webhook morto, precisa `vercel --prod` manual** (lição 09/08); demais conferir remoto. Astro: `public/banners/` → URL `/banners/...`.

## 4. Decisões técnicas do plano (do fórum)
- Hospedagem Cafezinho: `wp-content/moka-banners/` nos 2 servidores (sync horário NÃO copia tema/wp-content → subir nos 2). Nomes sem espaço, chown www-data.
- Inserção: slot novo no tema (front-page.php; single.php opcional) — NUNCA Ad Inserter na home (histórico de empilhamento, blocos posicionais frágeis).
- Iframe: `<iframe src="/wp-content/moka-banners/moka-728x90-pt.html" width="728" height="90" scrolling="no" style="border:0;overflow:hidden" title="Moka Reader" loading="lazy"></iframe>` (idem 300x250). Par alternativo -desktop/-mobile como os slots GAM.
- AMP: fora na fase 1 (JS externo proibido; amp-iframe exige sandbox+fora do 1º viewport).
- Temáticos: componente `MokaBanner.astro` + arquivos em `public/banners/`; 1 por home; idioma casado (Aiatolah: EN raiz, PT `/pt/`).
- Validação: backup `.bak_pre_banners_moka_20260816` · `php -l` · purge Rocket (`wp-content/cache/wp-rocket/` + `cache/busting/` + `wp cache flush`) · curl HTTP 200 no html + iframe renderizado · browser 375/768/1440.
- Rollback: .bak nos 2 servidores; git revert nos temáticos.

## 5. Comandos de recon usados (reprodução)
- Scripts: `/tmp/estudo_banner_recon{,2,3,4}.sh` locais → scp → bash no servidor (read-only).
- Ad Inserter unserialize: `wp eval '$o=unserialize(base64_decode(substr(get_option("ad_inserter"),4))); ...'` (JSON falha — formato antigo).
- AMP: `curl https://ocafezinho.com/<slug>/amp/` → 200; grep `amp-ad`.
- Gotcha: monitor foi editado por outra sessão durante meu edit (reler de novo antes de escrever — incidente clássico do §112).

## 6. Adendo 16/08 ~23:59 — banners AMP

- 1ª leva "... AMP.html" (23:52, 134 KB): bundler JS igual aos animados; payload interno estático (extraí p/ prova: 0 scripts no payload, âncora `href=https://mokareader.com target=_blank rel=noopener`), mas fontes ficam no manifest (uuid→woff2 base64, 108 KB) — sem o loader nada renderiza. INUTILIZÁVEL em amp-iframe sem allow-scripts. Descartei os derivados que tinha gerado.
- 2ª leva (zip 23:58, 6.316 B): `banners/_zip_extraido/AMP estatico/moka-{300x250,728x90}-{pt,en}.html`, 3.252–3.379 B, **0 `<script>`**, fonte Archivo via Google Fonts css2 (externa, fallback sans-serif), link `target="_blank"`, body com dimensão exata. APROVADOS.
- Sandbox correto p/ clique: `sandbox="allow-popups allow-top-navigation"` (allow-scripts dispensável; allow-popups obrigatório p/ o target=_blank).
- amp-iframe: HTTPS + origem diferente + fora do 1º viewport/≥600px do topo; falha → elemento vazio (fail-safe).
- Hospedagem recomendada: projeto estático Vercel `moka-banners` (decisão Miguel). Inserção AMP: bloco `[ADINSERTER AMP]` novo (padrão dos blocos 13/18-37 existentes).

## 7. Adendo 17/08 ~01:10 — execução home + single posts (2 servidores)

**Ordem Miguel:** "bota nos single posts também. encontra um lugar vazio para esses banners."

### 7.1 Recon decisivo — quem preenche o quê no single post
- Dump completo da option `ad_inserter` (`unserialize(base64_decode(substr($raw,4)))`): blocos 1-19 ativos; **todos os GAM/Taboola inserem divs próprios via client-side** (`html_selector`/`display_type`), NENHUM preenche os divs `banner-*` do tema.
- Mapa dos blocos: B1 CafeMobile-1 (`body > header`), B2-B5 after paragraph 6/12/16/18, B6 after-post, B9 Taboola (`body > section:eq(2) > div > div` = seção `#comentario`), B10 half-page (dt=16, dentro de `#comentario`), B11 interstitial, B15 Google News (`.date-comments`), B16 MGID (seletor `col-lg-8 col-md-8 col-sm-12` = tema antigo = MORTO), B17 Teads (footer), B13/18/19 AMP (`[ADINSERTER AMP]`).
- `curl` do single renderizado (espelho e canônico): **0 googletag/adv-dfp/taboola/mgid no HTML** (inserção client-side) e TODOS os `banner-*` vazios; `data-ai` markers presentes.
- Seções body-level do single: `[0] #search`, `[1] .pb-5 (artigo)`, `[2] #comentario`, `[3] leia-mais`, `[4] recentes` → Taboola/half-page caem na seção de comentários, não no Leia Mais.
- CSS `style.css` bloco F1 (11/08): `.desktop-ad-space`/`.mobile-ad-space` = display none global + block por breakpoint (≥992px / <992px) — anti-empilhamento.

### 7.2 Escolha dos lugares vazios
- **Single:** `banner-before-content-desktop/mobile` (single.php L43-46, entre foto destacada e corpo). Adjacências verificadas: acima = header (CafeMobile-1 separado por título/excerpt/foto); abaixo = 1º anúncio só após 6º parágrafo.
- **Home:** div novo `#moka-banner-home` após `<!-- LINHA DO TEMPO -->` (front-page.php fim, antes de `get_footer()`; Histórico fica no footer). Home = 0 anúncios vivos (`display_on_homepage=0` em todos os blocos).

### 7.3 Arquivos tocados (backup `.bak_pre_banners_moka_20260817` ao lado de cada um)
- `wp-content/moka-banners/` (NOVO, nos 2 servidores): `moka-728x90-pt.html` (3257 B) + `moka-300x250-pt.html` (3379 B), chown www-data, 644. Origem: `_zip_extraido/AMP estatico/` do zip do Miguel.
- `wp-content/themes/ocafezinho-portal/single.php` — idêntico nos 2 servidores (md5 pré-edição `312c69f4…`); iframes via `content_url('/moka-banners/…')` dentro dos 2 divs.
- `wp-content/themes/ocafezinho-portal/front-page.php` — **DIFERE entre servidores** (espelho a6ec017a… × canônico cb8d0554…, bloco legenda V2.9); bloco `#moka-banner-home` inserido separadamente em cada um (âncora `</section>\n<!-- LINHA DO TEMPO -->`, única nos dois).
- Iframe markup: `width/height` fixos, `style="border:0;display:block;margin:0 auto;max-width:100%;"`, `scrolling="no"`, `title="Moka Reader"`, sem `loading=lazy` manual (está acima da dobra).

### 7.4 Validação
- `php -l` verde nos 3 arquivos novos (espelho e canônico).
- Espelho: `https://cafezinho.news/wp-content/moka-banners/*.html` → 200; single e home com iframes no lugar (ordem Linha do Tempo < moka < footer confirmada por posição no HTML).
- Canônico: iframes → 200; home OK de primeira; single saiu STALE nos primeiros minutos após o deploy (opcache/janela curta de edge) — retestado ~10 min depois = novo nos 2 posts testados. **Gotcha:** WP Smush Pro reescreve os iframes para lazyload (`data-src` + placeholder SVG + `class="lazyload"`); grep de validação tem que casar `data-src`, não só `src`.
- Purge canônico: `rm -rf wp-content/cache/wp-rocket/ wp-content/cache/busting/` + `wp cache flush`. (advanced-cache.php do Rocket segue ativo mas com diretório de cache ausente → bypass; ServerDo reboota o canônico 03:30 diário.)

### 7.5 Estado da missão
- **Pronto:** Cafezinho não-AMP (home + single) nos 2 servidores, PT, sem tocar em nenhum anúncio de receita.
- **Falta:** (1) AMP = hospedagem Vercel `moka-banners` (origem diferente HTTPS) + bloco `[ADINSERTER AMP]` no meio do artigo — decisão do Miguel; (2) temáticos — aguarda ordem.

### 8. RESPIRO entre anúncio comercial e banner Moka (17/08 ~08:05)
- Ordem Miguel (print mobile 07:44): Moka colado no GAM comercial — pedir respiro ("um pequeno espaço de respiração para não ficarem colados").
- Raiz: bloco 25 do Ad Inserter (GAM, `html_selector=.featured-image-content`, dt=16) injeta logo ACIMA do div do Moka; margem padrão 20px do tema (style.css L653-656, bloco "Definições de Banners Anúncio") não bastava. Dump atual da option: blocos 1-19 = `disable_insertion=1` (desativados); vivos = 24-37.
- Fix: 2 regras no FIM do style.css — `#banner-before-content-desktop { margin-top: 28px; }` e `#banner-before-content-mobile { margin-top: 28px; }` — nos 2 servidores; backup `style.css.bak_pre_respiro_moka_20260817`; `?ver=1786963715` (filemtime via functions.php L8); purge Rocket (cache/busting/min) + `wp cache flush` no canônico.
- Provas: (1) curl do CSS entregue = regra 28px após a de 20px; (2) navegador IAB no post China×Índia de 17/08: `link#main-styles-css` aponta `?ver=1786963715` e margem computada do `#banner-before-content-desktop` = 28px; 20px anterior era cache do cliente (reload resolveu).
- Rollback: remover o bloco CSS do fim do arquivo.

### 9. RESPIRO v2 — Moka fora dos slots do Denakop (17/08 ~08:45)
- Ordem Miguel: "cuidado com o anúncio do denakop, que é comercial e deve ser respeitado; se necessário, bota o moka em outro lugar, mais para baixo do post".
- **Achado central:** os slots `banner-before-content-*` são preenchidos client-side pelo **Denakop** (script `tags.denakop.com/10819/ocafezinho.com.js`, carregado por `servg1.net/o.js?uid=a6a9ff0d0f1e980b3cea04fa` — injeção fora do WP, não há código servg1/denakop em plugins/temas; script no `<head>` da página). O Denakop insere `denakop-scroll-1` DENTRO do slot; o Moka estava no mesmo container → colagem inevitável; margem externa não separa filhos do mesmo div. §3 diagnosticou errado (culpou bloco 25 do Ad Inserter, que nem existe no single).
- Mapa Denakop nos slots mobile do single: banner-top-mobile=first-1, banner-before-content-mobile=scroll-1, advertisement-after-support-mobile=scroll-2, banner-before-comments-mobile=scroll-3, banner-after-comments-mobile=scroll-4, banner-after-related-mobile=scroll-5; desktop: banner-before-content-desktop=scroll-1.
- Fix: Moka em div próprio `#moka-banner-before-content` (single.php, depois dos slots) + CSS `margin: 28px 0`; slots voltaram vazios p/ o Denakop. Backups `.bak_pre_moka_div_proprio_20260817` nos 2 servidores; `?ver=1786966610`; Rocket purge; Redis do canônico falhou no `wp cache flush` (drop-in object-cache.php presente, conexão recusada — anotado, não bloqueou: purge por rm funcionou).
- Provas: headless mobile DOM (slot só com div Denakop; div Moka separado); IAB real (margem computada 28px, slot desktop com Denakop); curl nos 2 servidores (estrutura nova; espelho validado em post 16/08).
- Lição: div "vazio" no HTML servido não prova nada — script de ad client-side pode injetar depois; recon tem que incluir renderização com JS (headless chrome) antes de ocupar um slot.

### 10. Banner Moka CORTADO no espelho (17/08 ~10:30)
- Sintoma: banner 300x250 cortado (~60% da altura visível) no espelho; canônico ok. Post: a-voz-de-vila-clara-capitulo-1.
- Causa: `cafezinho-lab-visual.css` (mu-plugin SÓ do espelho, linha 316-318) tem `img, iframe, video { max-width:100%; height:auto; }` — `height:auto` vence o atributo height=250 → iframe fica 150px (default de elemento substituído sem razão intrínseca) → conteúdo interno 250px cortado. Canônico não tem esse mu-plugin.
- Diagnóstico por medição CDP (não dá p/ ver screenshot na sessão): script /tmp/cdp_measure.mjs (Chrome headless + remote-debugging, Emulation.setDeviceMetricsOverride) → mediu 300x150 espelho vs 300x250 canônico; cdp_cssmatch.mjs confirmou matches=[] (nenhuma regra normal) e pai flex — a causa era o stylesheet global.
- Fix: `height:90px`/`height:250px` no style inline dos 4 iframes Moka (single.php + front-page.php) nos 2 servidores — inline vence o stylesheet. Backups `.bak_pre_moka_height_20260817`; php -l; purge canônico.
- Provas finais (CDP): espelho single 300x250, desktop div 90px, home 300x250; canônico sem regressão (h=250).
- Lições: (1) mu-plugins do espelho podem afetar markup novo que o canônico não testa — sempre validar os 2; (2) `height:auto` em iframes é armadilha clássica — pôr altura explícita no inline de todo iframe de banner.
