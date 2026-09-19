---
name: reference-ads-canonico-ocafezinho-arquitetura-real
description: "Arquitetura REAL de ads no canônico ocafezinho.com — DFP/GAM Publisher ID 21622511100, 90 blocos ad-inserter (36 ativos), Quick AdSense + Colabs legado + AutoAds. Descoberto 11/08/2026 07:15 BRT."
metadata: 
  node_type: memory
  type: reference
  originSessionId: ab72ecc4-9deb-4729-9735-80bcceefd907
---

**Motor principal de ads no Cafezinho canônico é o Google Ad Manager (DFP), servido via plugin ad-inserter.** Contradiz meu diagnóstico anterior (que era baseado em busca com chave errada: `ad-inserter` com hífen em vez de `ad_inserter` com underscore).

## Fatos verificados

**Publisher ID Google Ad Manager (DFP):** `21622511100`
**Formato de ad path:** `/21622511100/cafezinho_post/<slot_name>`

**Plugin ad-inserter:**
- Total de blocos configurados: **90**
- Blocos ATIVOS (com código não-vazio): **36**
- Storage: `wp_options.ad_inserter` (49KB), formato `:AI:<base64>(serialize PHP)`
- Precisa `base64_decode(substr($raw, 4))` + `unserialize()` pra ler config

**Slots GAM identificados (dos primeiros 6):**
- Block 1: `/21622511100/cafezinho_post/cafe_mobile_1`
- Block 2: `/21622511100/cafezinho_post/cafe_mobile_2`
- Block 3: `/21622511100/cafezinho_post/cafe_mobile_3`
- Block 4: `/21622511100/cafezinho_post/cafe_mobile_4`
- Block 5: `/21622511100/cafezinho_post/cafe_mobile_5`
- Block 6: `/21622511100/cafezinho_post/cafe_mobile_6`
- Block 11: **Interstitial GAM** (o modal fullscreen "ACESSE MEU SUS DIGITAL" que Miguel viu no screenshot)
- Block 12: `/21622511100/cafezinho_post/cafe_mobile_3` (duplicata?)
- Block 32: **consent** (fundingchoices — Google Funding Choices, CMP LGPD/GDPR)
- Outros blocos GAM ativos (30+) com paths não capturados pelo regex inicial — reinvestigar

**Div IDs dos slots GAM:**
- `CafeMobile-1` até `CafeMobile-6` (mobile)
- **NÃO são os `banner-*` do tema** — os slots GAM têm IDs customizados criados pelo ad-inserter

**Plugins de ads secundários:**
- **Quick AdSense 2** (`quick_adsense_2_options`, 5KB) — insere ads dentro dos POSTS (Beginning/Middle/End) usando `(adsbygoogle = window.adsbygoogle || []).push({})`
- **Colabs AdSense** (`colabs_adsensecode_1` e `_3`) — legado, banners 728x90 e 468x60 com publisher `ca-pub-5835338445130243`
- **widget_colabs_ads** — widget AdSense
- **insert-headers-and-footers** — `ihaf_insert_footer` só 2 bytes (essencialmente vazio)

## Por que meu `curl` inicial mostrou HTML vazio

Ads GAM são injetados **dinamicamente via JavaScript** DEPOIS que a página carrega. `curl` puro pega o HTML antes do JS rodar — os `<div id="CafeMobile-1">` estão vazios no HTML puro, mas populam quando o browser executa `googletag.display('CafeMobile-1')`.

**Isso significa:** auditoria de ads em Cafezinho SEMPRE precisa de browser headless (Puppeteer, Playwright) ou análise dos SCRIPTS injetados — nunca só `curl` do HTML.

## Formatos de ad identificados via screenshots

Miguel mandou 10 screenshots (11/08 06:17) que mostram formatos ativos no canônico:

1. **In-article banners** (dentro do texto do post, entre parágrafos) — Quick AdSense + AdSense standard
2. **Header banners** (logo abaixo do header, antes do título do post) — ad-inserter → GAM
3. **Home meio** (entre blocos de posts) — ad-inserter → GAM
4. **Anchor sticky mobile** (banner fixo no rodapé com ✕) — GAM AutoAds ou ad-inserter formato especial
5. **Interstitial fullscreen** (modal grande centralizado com "Fechar") — Block 11 GAM Interstitial
6. **Native "Conteúdo Promovido"** (card de Discovery ads) — GAM Native/Discovery
7. **Sticky bottom sponsored** ("O SUS PODE TE AJUDAR!") — GAM formato especial

Neste momento (11/08 06:17), 95%+ dos ads visíveis eram **campanhas institucionais governo** (SUS/Ministério da Saúde sobre vício em apostas). Alguns comerciais (Verisure câmera, Betnacional Fortune Tiger regulamentado SPA/MF 2.092/24) apareceram no Discovery Native.

## Riscos destrutivos — atualizado

**🔴 CRÍTICO — evitar:**
- Alterar `wp_options.ad_inserter` sem backup completo — pode zerar 36 blocos ativos
- Desativar plugin `ad-inserter` — para todos os 36 blocos GAM
- Editar/desativar `Quick AdSense 2` — para ads in-article (grande parte da receita)
- Renomear IDs dos divs GAM (`CafeMobile-1..6`) — perde targeting
- Deletar ou editar Colabs AdSense — legado mas potencialmente ativo

**🟡 MÉDIO:**
- Mudar `<div id="banner-*">` do tema (aqueles do inventário anterior) — provavelmente NÃO servem GAM hoje, mas ad-inserter pode ter blocos mapeados via seletor CSS que apontem pra essas classes
- Mexer no functions.php do tema
- Mudar `<head>` (onde carrega `gpt.js` do GAM)

**🟢 BAIXO:**
- Mudanças visuais em arquivos do tema que não afetem os divs de ad
- Adicionar novos slots com IDs próprios (ex: `CafeCustom-Foo`)
- CSS puro que não altere `display` dos divs de ad

## Como se defender ao portar reforma visual pro canônico

Antes de qualquer edição no canônico:

1. **Backup completo do banco `wp_options`** (não só do tema)
2. **Backup do plugin ad-inserter config** — export via `wp option get ad_inserter --allow-root > backup.txt` OU dump SQL direto
3. **Snapshot dos scripts populados** — abrir home no browser, salvar HTML pós-JS, guardar
4. **Testar TUDO no espelho primeiro** — se algo quebrar visualmente no espelho relacionado a ads, é provável que quebre no canônico também
5. **Se precisar tocar em qualquer arquivo relacionado a `<div id="banner-*">` ou `<div id="CafeMobile-*">` ou `<div class="ad-space">`** — inspecionar ad-inserter primeiro pra ver se aquele slot tem block mapeado

## Investigação pendente

- [ ] Decodificar blocos ad-inserter 7-90 (nem todos GAM foram capturados pelo regex — muitos aparecem como "?")
- [ ] Mapear cada bloco ATIVO a: (a) tipo (GAM/AdSense/HTML/consent), (b) ad path completo, (c) automatic_insertion (paragrafo N, seletor CSS, etc.), (d) div ID gerado
- [x] ~~Ver se algum bloco ad-inserter usa seletor `#banner-*`~~ **CONFIRMADO 11/08 07:30 BRT: ZERO blocos usam custom_css_selector, ZERO usam automatic_insertion baseada em paragraph, ZERO mencionam IDs `banner-*` do tema. Ad-inserter é totalmente independente da estrutura visual do tema.**
- [ ] Auditar ihaf_insert_header / ihaf_insert_body (podem ter script GAM inicial — mas ihaf_insert_footer é vazio)
- [ ] Testar renderização real do canônico via browser headless pra ver quais divs são populados
- [x] ~~Ver se posts têm shortcode [adinserter]~~ **CONFIRMADO 0 posts com shortcode. Sem shortcodes no tema. CafeMobile-* deve ser via filter the_content ou hook wp_head/wp_footer.**

## ✅ CONCLUSÃO PRÁTICA (11/08 07:30 BRT)

**Mudanças VISUAIS na estrutura da home/single (mover Coluna do Editor, adicionar blocos temáticos, esconder sidebar em iPad, remover bloco canônico, etc.) NÃO AFETAM os anúncios ativos do canônico** — porque:

1. Ad-inserter não referencia IDs `banner-*` do tema
2. Ad-inserter não usa seletor CSS baseado em estrutura da home
3. Ad-inserter não usa `automatic_insertion` dependente de paragraph number
4. Divs `CafeMobile-1..6` são criados pelo próprio código HTML dos blocks (via `googletag.display()`) — não são elementos do tema

**O que continua exigindo cuidado (não fazer):**
- Desativar/deletar plugin ad-inserter
- Editar `wp_options.ad_inserter` sem backup DB
- Portar mu-plugin `cafezinho-lab-ad-calhau.php` pro canônico (CSS `.desktop-ad-space{display:none!important}` esconderia ads reais)
- Desativar Quick AdSense 2 (serve `adsbygoogle` in-article dos posts)
- Deletar mu-plugins do canônico (17 arquivos, todos features editoriais — não são ad-serving mas podem afetar features do worker)

Regras irmãs: [[project-lab-visual-cafezinho-news-20260811]] · [[feedback-lab-visual-anotar-bugs-seguranca-port-canonico]] · [[feedback-canonico-port-do-espelho-cirurgico]]
