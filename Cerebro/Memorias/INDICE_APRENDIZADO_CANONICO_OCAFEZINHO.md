# 📚 Índice de Aprendizado — Canônico ocafezinho.com

**Criado:** 2026-08-11 07:40 BRT (ordem do Miguel: "anotando tudo com cuidado, indexando cada passo, pra ir aprendendo cada vez mais como funciona o cafezinho canônico e a publicidade")
**Custódia:** ZCode (GLM-5.2 / Kimi K3 / Qwen 3.8 — ambiente)
**Filosofia:** cada descoberta sobre o canônico vira uma entrada aqui. Conhecimento cumulativo, indexado, reusável por qualquer agente (Claude/ZCode/Codex) que herdar o sprint.
**Status:** VIVO — cresce a cada iteração do sprint visual

---

## Como usar este índice

1. **Antes de qualquer mudança no canônico**, consultar as seções relevantes aqui.
2. **Cada nova descoberta** (categoria, plugin, behavior, ad-unit, seletor) vira uma entrada nova datada na seção apropriada, com link pro fórum/memória de origem.
3. **Erros corrigidos** ficam marcados ✅ com data da correção + referência.
4. **Seções** organizadas por domínio: Ads · Categorias · Autores · Estrutura do tema · Plugins · DB · Comportamentos · APIs.

---

## 📊 Snapshot fundamental (números do canônico em 11/08/2026)

| Métrica | Valor | Fonte |
|---|---|---|
| Posts publicados | ~40.000+ | `wp_posts` (count publish) |
| Categorias ativas (count>0) | 40+ | `wp_term_taxonomy` |
| Plugins ativos | 43 | `wp_options.active_plugins` |
| mu-plugins | 17 arquivos | `/wp-content/mu-plugins/` |
| Ad-units GAM ativos (AMP) | 15 + 1 mgid | `wp_options.ad_inserter` + `/amp/` ao vivo |
| Vendors em ads.txt | 1822 | `https://ocafezinho.com/ads.txt` |
| Publisher GAM real | `/21715141650,22670554696/` | data-slots AMP (não `21622511100`) |
| WP Rocket + serverdoin-cdn | sim | cache em produção |

---

## 🎯 1. ADS — arquitetura completa

### 1.1 Camadas (4, não 3)

| Camada | Onde | Plugin/option | Detalhe |
|---|---|---|---|
| **A — GAM via AMP** | `/amp/` e `?amp` | `ad-inserter` (19 blocos, 18 com code) | 15 data-slots `/21715141650,22670554696/ocafezinho.com/{first,intext,scroll,under}/post/*` + 1 mgid widget |
| **B — Teads** | todos (AMP + non-AMP) | `ad-inserter` bloco 17, `display_type=13` (Footer code) | `<script src="//a.teads.tv/page/86345/tag">` — page ID 86345 |
| **C — 360yield header** | non-AMP header | option `wp_options.wpc_inner_header_wide_ad` (772 bytes, NÃO é ad-inserter) | `document.write` injeta `<script src="http://ad.360yield.com/adj?p=739943&w=728&h=90">`. ⚠️ **HTTP não-HTTPS = mixed content (LV-005)** |
| **D — ads.txt** | `/ads.txt` público | `ads-txt/ads-txt.php` | 1822 vendors: richaudience, rubicon 17210, appnexus 10264, pubmatic 156383, criteo B-060278, smartadserver 1743, indexexchange 192450, onetag, triplelift 12911, etc. |

### 1.2 Mapa dos 19 blocos `used_blocks` do ad-inserter

| Bloco | display_type | Onde | Conteúdo |
|---|---|---|---|
| 14 | 16 (Before/After element) | home `section:nth-child(8) > div` | **PLACEHOLDER VAZIO** (`code_len=0`) — órfão |
| 15 | 16 | single `.date-comments` | Banner Google News (PHP echo) |
| 17 | 13 (Footer code) | todos | **Teads** page 86345 |
| 21 | 6 (After paragraph) | single ¶3 | `<div id="in-text-1" class="ad-space">` (vazio non-AMP) |
| 22 | 6 | single ¶6 | `<div id="in-text-2" class="ad-space">` (vazio non-AMP) |
| 24 | 15 (AMP before element) | AMP `header.amp-wp-article-header` | GAM `first/post/1` |
| 25 | 16 | AMP `.featured-image-content` | GAM `intext/post/1` |
| 26-29 | 6 | AMP ¶3/6/9/12 | GAM `intext/post/2-5` |
| 30-31 | 15/16 | AMP `div.relatedpost` | GAM `scroll/post/1-2` |
| 32 | 15 | AMP `footer.footer_wrapper` | **mgid** widget 1373898 / website 836425 |
| 33-37 | 6 | AMP ¶15/18/21/24/27 | GAM `intext/post/6-10` |
| **h** (global head) | — | AMP `<head>` | Carrega `amp-iframe` + `amp-sticky-ad` scripts |
| **f** (global footer) | — | AMP `<body>` fim | `<amp-sticky-ad>` GAM `under/post/1` |

### 1.3 Ad-units GAM únicos (15) — todos AMP

```
/21715141650,22670554696/ocafezinho.com/first/post/1      (header AMP)
/21715141650,22670554696/ocafezinho.com/intext/post/{1..10} (¶3-27 AMP)
/21715141650,22670554696/ocafezinho.com/scroll/post/{1,2}  (related AMP)
/21715141650,22670554696/ocafezinho.com/under/post/1       (sticky mobile AMP)
```

### 1.4 Descobertas críticas

- **Non-AMP não tem GAM** — sem `gpt.js`, sem `googletag.defineSlot`, sem `adsbygoogle`. Só Teads + 360yield.
- **18 slots `.ad-space` vazios no non-AMP** (incl. `in-text-1/2`) — possível inventário não monetizado ou quebra latente (LV-006, investigar com browser headless).
- **Quick AdSense e Colabs NÃO existem** — o fórum do Claude estava errado (retratado em 11/08 07:30).
- **Não há `defineOutOfPageSlot`** no ad-inserter — interstitials (se houver) vêm de outro lugar (provavelmente GAM dashboard config, não blocos).

📖 **Referências:** `Foruns/forum_mapa_ads_canonico_ocafezinho_20260811.md` (fórum), `Memorias/memoria_mapa_ads_canonico_ocafezinho_20260811.md` (log técnico)

---

## 🏷️ 2. CATEGORIAS — IDs e estrutura

### 2.1 Top categorias (count > 0, ordenadas por volume)

| ID | Nome | Slug | Posts | Parent |
|---|---|---|---|---|
| 2403 | Redação | redacao | 37.374 | 0 |
| **22** | **Política** | politica-2 | 12.844 | 0 |
| 15 | Internacional | politica-internacional | 8.360 | 0 |
| **43** | **Economia** | economia | 6.285 | 0 |
| **5003** | **Geopolítica** | geopolitica | 5.905 | 0 |
| 4949 | Rhyan de Meira | rhyan-de-meira | 4.211 | 0 |
| **19936** | **Ciência e Tecnologia** | ciencia-e-tecnologia | 2.816 | 0 |
| **30** | **Tecnologia** | tecnologia | 2.203 | 0 |
| 5062 | Guerra | guerra | 2.032 | 0 |
| 3 | Conteúdo Livre | conteudolivre | 1.956 | 0 |
| 4996 | China | china | 1.838 | 0 |
| 1308 | Golpe | golpe | 1.795 | 0 |
| 5061 | EUA | eua | 1.722 | 0 |
| 1335 | Justiça | justica | 1.544 | 0 |
| 23 | Mídia | midia | 1.234 | 0 |
| 735 | Ciência | ciencia | 1.149 | 0 |
| 5088 | Eleições 2026 | eleicoes-2026 | 1.109 | 0 |
| 3019 | Geonoticias | geonoticias | 1.054 | 0 |
| 358 | Direitos Humanos | direitos-humanos | 887 | 0 |
| 1100 | STF | stf-2 | 886 | 0 |

### 2.2 Categorias usadas nos blocos temáticos do espelho (front-page.php)

| Bloco | category__in | Observação |
|---|---|---|
| **NACIONAL** | `[22, 43]` | Política + Economia (1 destaque + 4 laterais) |
| **GEOPOLÍTICA** | `[5003]` | 1 foto hero + 5 títulos |
| **CIÊNCIA E TECNOLOGIA** | `[30, 19936]` | Tecnologia + Ciência e Tecnologia **combinadas** (pendência §9.1 fórum Claude: unificar oficialmente depois) |
| **LINHA DO TEMPO** | sem filtro | `posts_per_page=7`, cronológico geral |
| **RECENTES** | sem filtro, `post__not_in=$excludes` | `posts_per_page=20` (grid 4×5) |
| **COLUNA DO EDITOR** | autor 2018 (Miguel) | `posts_per_page=4`, 3 breakpoints |

### 2.3 Padrões importantes

- **Slug "política" é `politica-2`** (não `politica`) — provável conflito histórico. URL pública é `/politica-2/`.
- **Geopolítica (5003) é category filha** do site pós-2022 (quando o Cafezinho virou portal de análise).
- **Ciência (735) ≠ Ciência e Tecnologia (19936)** — categorias irmãs, sobreposição conceitual. A `19936` é mais nova (2025?).
- **Redação (2403, 37k posts)** é a categoria-coringa — 93% de tudo.

---

## 👤 3. AUTORES — IDs relevantes

| ID | Nome | Posts | Uso |
|---|---|---|---|
| 5470 | Redação | 40.524 | Default |
| **2018** | **Miguel do Rosário** | 10.352 | **Coluna do Editor** (autor alvo do bloco) |
| 5728 | Cláudia Beatriz | 7.545 | Colunista |
| 1005 | Redação | 2.290 | Variante Redação |
| 5727 | Redação | 2.077 | Variante Redação |
| 5749 | Rhyan de Meira | 1.614 | Colunista (cat 4949) |
| 5735 | Gabriel Barbosa | 1.559 | Colunista (cat 4942) |
| 5734 | Redação | 1.251 | Variante |
| 5745 | Cleber Lourenço | 968 | Colunista (cat 4944) |

---

## 🏗️ 4. ESTRUTURA DO TEMA — `ocafezinho-portal`

### 4.1 Comparação espelho vs canônico (front-page.php)

| Arquivo | Espelho (cafezinho.news) | Canônico (ocafezinho.com) |
|---|---|---|
| `front-page.php` linhas | 433 | **258** |
| Blocos na home | Manchete + Coluna Editor + Nacional + Geopolítica + Ciência + Linha do Tempo + Recentes (7) | **Só Manchete + Coluna Editor (2)** |

**Conclusão:** o canônico tem home ENXUTA. Os blocos temáticos (Nacional/Geopolítica/Ciência/Linha do Tempo) são **inovação da reforma visual** — só existem no espelho. O port pro canônico vai **adicionar** blocos que não existem lá.

### 4.2 Templates do tema

| Template | Função | Linhas (espelho) |
|---|---|---|
| `front-page.php` | Home | 433 |
| `single.php` | Post individual | 11.271 (ajustado iPad 1 col) |
| `header.php` | Cabeçalho | 4.099 |
| `footer.php` | Rodapé | 5.014 |
| `sidebar.php` | Sidebar (`d-none d-lg-block`) | 375 |
| `index.php` | Fallback (categorias/arquivo/tags) | 1.696 |

### 4.3 Padrão `$excludes` (anti-repetição entre blocos)

Cada bloco do front-page faz `array_push($excludes, get_the_ID())` em cada iteração do loop, e o próximo bloco passa `'post__not_in' => $excludes`. Isso garante que **um post nunca aparece em 2 blocos**. **Qualquer bloco novo precisa respeitar esse padrão** ou vai duplicar posts.

### 4.4 Separadores visuais

Cada bloco tem um separador HTML consistente:
```php
<div class="container-xxl my-4">
  <div class="d-flex align-items-center">
    <img src="<?php bloginfo('template_url'); ?>/img/icon-start.svg" width="20" height="20" class="me-2" alt="...">
    <h4 class="m-0 text-red">NOME DO BLOCO</h4>
    <div class="flex-grow-1 border-top border-secondary opacity-25 ms-3"></div>
  </div>
</div>
```
Usa Bootstrap 5 (container-xxl, d-flex), ícone `icon-start.svg`, classe `text-red` (cor primária do tema).

### 4.5 Manchete (post de destaque da home) — aprendizado 11/08 07:55

- **Função que define qual post é a manchete:** espelho usa `get_highlight('Manchete')`, canônico usa `cafezinho_get_real_highlight('Manchete')`. ⚠️ **A função `get_highlight` NÃO está no tema do espelho nem em mu-plugins** — provavelmente vem de plugin/parent theme. **Pendência:** mapear origem.
- **Layout ORIGINAL (canônico + espelho, pré-11/08):** `row` > `col-md-8` (imagem) + `col-md-4` (título/data/excerpt/botão). Mobile = empilhado (OK); iPad/desktop = lado a lado 8/12+4/12 (Miguel considerou feio).
- **Layout NOVO (espelho pós-11/08 07:55, REFORM V2.0):** empilhado vertical em TODOS os breakpoints — `h1.manchete-titulo` → `img 100%` → `figcaption.manchete-caption` (condicional) → excerpt → botão. Usa `wp_get_attachment_caption(get_post_thumbnail_id())` pra mostrar a legenda WP se preenchida.
- **Caption é campo nativo WP:** `wp_posts.post_excerpt` do attachment. Redação JÁ usa (ex: manchete "Lula reconquista as capitais" 11/08 tem caption Ricardo Stuckert/MTST). Feature tem valor real.
- **`no_lazyload` class:** imagem da manchete usa `'class' => '... no_lazyload'` — é pra não ter lazy-load (above the fold, carrega imediato). Preservar em qualquer mudança.
- **Backup + rollback:** `front-page.php.bak_pre_manchete_titulo_cima_20260811_<ts>` + `/root/manchete_titulo_cima_20260811/rollback.sh`
- **Iteração pendente:** Miguel quer testar "sem excerpt" depois (só comentar a linha `<p class="text-gray manchete-excerpt">`)

### 4.6 Coluna do Editor — setas de carrossel (aprendizado 11/08 08:25)

- **Layout (3 breakpoints):**
  - Mobile (<768px): scroll horizontal, 1 card (85%) por vez — swipe natural
  - iPad (768-991px): grid 2×2 fixo, mostra os 4 cards
  - Desktop (≥992px): scroll horizontal, 2 cards visíveis por vez — **adicionado setas ← → em 11/08**
- **Setas (REFORM V2.1, 11/08 08:25):** overlay flutuante nas laterais (estilo Netflix), `position:absolute`, `top:50%`, `width/height 44px`, círculo vermelho (`rgba(220,53,69,0.92)`), hover 100% opacidade, `disabled` cinza no início/fim. **Só aparecem em ≥992px** (`display:none` base, `display:inline-flex` no media query).
- **JS vanilla** (sem jQuery): IIFE, `cardWidth()` calcula card+gap, `step()` retorna 2 (desktop) ou 1, `grid.scrollBy({behavior:'smooth'})`, listeners em scroll/resize atualizam estado disabled. Truque: `document.currentScript.previousElementSibling` referencia o carousel (script inserido logo após o wrapper).
- **Acessibilidade:** `aria-label` nos botões, `tabindex=-1` default, `focus-visible` com outline vermelho, SVG `aria-hidden`.
- **Backup + rollback:** `front-page.php.bak_pre_setas_coluna_editor_20260811_<ts>` + `/root/setas_coluna_editor_20260811/rollback.sh`
- **Iteração pendente:** validação visual real do Miguel no desktop (confirmar se setas aparecem e fluem).

> **ATUALIZAÇÃO V2.3 (11/08 08:45):** Coluna do Editor agora tem **8 posts** (antes 4) e **iPad virou swipe** (antes era grid 2×2 fixo). Configuração atual:
> - Mobile (<768px): swipe, 1 card por vez, 8 posts no total
> - iPad (768-991px): swipe, **2 cards por vez** (NOVO — deixou de ser grid fixo)
> - Desktop (≥992px): swipe + setinhas, 2 cards por vez, step 2 por clique
>
> `posts_per_page: 8`. Miguel (autor 2018) tem 161 posts publicados — preenche os 8 slots folgado. Backup `/root/coluna_editor_8_swipe_20260811/`.

### 4.7 Balão de comentários "pegando fogo" 🔥 (aprendizado 11/08 08:40)

- **Estado ORIGINAL:** tema tinha `<span class="icon-comments">` no `single.php` L19 (página do post, com bg svg `img/icon-comments.svg`), mas **NUNCA na home/capa**. Espelho e canônico idênticos nisso.
- **"Pegando fogo" NÃO existia** — foi criado nesta iteração (REFORM V2.2).
- **Regra (Miguel 11/08 08:35):** balão aparece **sempre que o post tem ≥1 comentário** aprovado, **com fogo sempre** (sem threshold alto — Miguel rejeitou ≥3 e ≥5; "deixa o balao com fogo sempre").
- **Implementação:** `<div class="manchete-titulo-linha">` (flex, `flex-wrap:wrap`) envolve `<h1>` + `<a class="manchete-balao-comentarios" href="...#comments">` com `<span class="manchete-balao-fogo">🔥</span>` + `<span class="icon-comments manchete-balao-numero">N</span>`. CSS: pill gradient vermelho→laranja, animação `manchete-fogo-piscar` (scale+rotate+opacity, 1.6s infinite), `prefers-reduced-motion` desativa.
- **Contexto:** Miguel vai **religar o agente comentarista** (`agente_comentarista_v4.py` no `.codex_work/`) — expectativa de aumento de comentários na manchete. Threshold do fogo pode ser revisto futuramente quando volume real for conhecido.
- **Acessibilidade:** `title` informativo, `aria-hidden` no emoji decorativo, `focus-visible` outline, `prefers-reduced-motion` respeitado.
- **⚠️ Cache do navegador:** CSS animation fica no `style.css` — pra ver a animação, usuário precisa fazer hard refresh (Ctrl+Shift+R) na 1ª visita após a mudança.
- **Backup + rollback:** `front-page.php.bak_pre_balao_fogo_manchete_20260811_<ts>` + `/root/balao_fogo_manchete_20260811/rollback.sh`
- **Funções WP úteis:** `get_comments_number($post_id)` retorna int; `wp_countComments()` alternativo. `#comments` é âncora padrão WP pra seção de comentários.

### 4.8 Logo do header — troca e otimização (aprendizado 11/08 08:55)

- **Logo antiga (header):** `/img/logo-ocafezinho-outline.png` — 138×95 HORIZONTAL, 6,8KB. Usada em `header.php` L16 com `width=138 height=95 class="logo mx-auto"`.
- **Logo nova (Miguel, 11/08):** `Logo O Cafezinho-selection.png` — 1840×1816 **QUADRADA**, 205KB (source: `~/Downloads/Antigravity Google/Outros/logo cafezinho/logo nova 3/`).
- **⚠️ Não dá pra subir direto:** quebra o header. Solução em 4 camadas:
  1. **PIL redimensiona** 1840→200 (LANCZOS, optimize): 205KB→15,9KB (-92%)
  2. **HTML** `<img width="60" height="60">` (atributos fixos anti-layout-shift)
  3. **CSS** `.logo { width:60px; height:60px; max-width:60px; max-height:60px; object-fit:contain }`
  4. **CSS desktop** `@media 768px { .logo { width:100px; height:100px; max-width:100px } }`
- **Arquivo novo:** `/img/logo-nova-cafezinho.png` (200×200, SHA `45e7c38d...`) — **não substitui** a original `logo-ocafezinho-outline.png` (preservada, ainda usada no footer).
- **Footer (footer.php L5):** ainda tem a logo horizontal antiga numa `col-md-1`. Pendência decidir se troca também pra consistência.
- **Logos no tema:** `logo-ocafezinho-outline.png` (138×95), `logo-ocafezinho.png` (276×190), `cafezinho.svg` (ícone pequeno), `logo-nova-cafezinho.png` (200×200 NOVA).
- **Padrão aprendido:** sempre que trocar imagem por uma de proporção diferente, redimensionar antes de subir + travar dimensões no HTML e CSS. Não confiar em `width:auto` pra imagens quadradas novas.
- **Backup + rollback:** `header.php.bak_pre_logo_nova_header_20260811_<ts>` + `style.css.bak_pre_logo_nova_header_20260811_<ts>` + `/root/logo_nova_header_20260811/rollback.sh` (restaura header + css + remove logo nova).

---

## 🔌 5. PLUGINS — 43 ativos

### 5.1 Ads-related (3)
- `ad-inserter/ad-inserter.php` — 19 blocos (18 com code), AMP-focused
- `ads-txt/ads-txt.php` — gerencia `/ads.txt`
- `insert-headers-and-footers/ihaf.php` — **LEGACY INERTE** (`ihaf_*` options vazias; wpcode é o sucessor)

### 5.2 AMP
- `accelerated-mobile-pages/accelerated-moblie-pages.php` (sim, "moblie" com typo) — cria rotas `/amp/` e `?amp`

### 5.3 Críticos (não mexer sem plano)
- `wp-rocket` — cache (não purgar sem autorização Miguel)
- `serverdoin-cdn/index.php` — CDN
- `wordpress-seo-premium` + `wordpress-seo` + `wpseo-news` + `wpseo-local` — Yoast SEO (5 plugins)
- `wordfence` — firewall
- `really-simple-ssl` — HTTPS
- `redis-cache` — object cache
- `updraftplus` — backup
- `jwt-authentication-for-wp-rest-api` — auth REST API

### 5.4 Funcionais
- `ai-engine` — IA (Jorge?)
- `wpcode` (snippet runner, 17 snippets funcionais)
- `wp-ajaxify-comments` — comentários AJAX
- `wp-post-signature` — assinatura do autor nos posts
- `wptelegram` — Telegram
- `zapier` — Zapier
- `ga-google-analytics` — GA (GTM G-4E5DKNTYET)
- `gtranslate` — tradução

### 5.5 NÃO existem (retratação)
- `quick-adsense` / `quick-adsense-2` — ❌ não instalado
- `colabs-adsense` — ❌ não instalado
- Qualquer plugin com "adsense" no nome — ❌ nenhum

---

## 💾 6. BANCO DE DADOS — padrões

### 6.1 Acesso (credenciais em `wp-config.php`)
```bash
DBN=$(awk -F"'" "/DB_NAME/{print \$4; exit}" /var/www/ocafezinho/wp-config.php)
DBU=$(awk -F"'" "/DB_USER/{print \$4; exit}" /var/www/ocafezinho/wp-config.php)
DBP=$(awk -F"'" "/DB_PASSWORD/{print \$4; exit}" /var/www/ocafezinho/wp-config.php)
mysql -u"$DBU" -p"$DBP" "$DBN" -e "..."
```

### 6.2 Options relevantes de ads
| Option | Tamanho | Conteúdo |
|---|---|---|
| `ad_inserter` | 49.216 bytes | `:AI:` + base64 + PHP serialize → 90 entradas (85 blocos + 5 config) |
| `wpc_inner_header_wide_ad` | 772 bytes | Banner 360yield (HTTP mixed content) |
| `wpcode_snippets` | 50.344 bytes | 17 snippets funcionais PHP (NÃO ads) |
| `ihaf_insert_header/footer/body` | 0/2/0 | Legacy vazio |

### 6.3 Padrão de query de bloco temático (exemplo)
```php
$args = array(
    'posts_per_page' => 1,           // ou 4, 5, 20 dependendo do bloco
    'order'          => 'desc',
    'orderby'        => 'date',
    'post_status'    => 'publish',
    'post_type'      => 'post',
    'category__in'   => array(5003), // categoria(s)
    'post__not_in'   => $excludes    // array acumulado anti-repetição
);
$latest = new WP_Query( $args );
while( $latest->have_posts() ) : $latest->the_post();
    array_push( $excludes, get_the_ID() );  // ADD ao excludes
    // renderiza card
endwhile; wp_reset_query();
```

---

## ⚡ 6.5 PERFORMANCE / PESO DO PAINEL — diagnóstico completo (11/08 08:50)

> **Fonte:** `Foruns/forum_diagnostico_peso_painel_cafezinho_canonico_20260811.md` (decisões) + `Memorias/memoria_diagnostico_peso_painel_cafezinho_canonico_20260811.md` (log técnico)

### 6.5.1 Snapshot de infraestrutura (11/08 08:45 BRT — VPS QEMU 8 cores / 8 GB)

| Métrica | Valor | Estado |
|---|---|---|
| Load average (1/5/15min) | 4,31 / 3,79 / 3,78 | 🔴 saturado |
| RAM usada / livre | 4,2 GB / 663 MB | 🟡 apertado |
| **Swap em uso** | **2,5 GB** | 🔴 swap ativo = lentidão |
| MySQL CPU% | 203% (647 min CPU em 5h uptime) | 🔴 vilão CPU |
| PHP-FPM workers ativos | 65 × 97 MB = 6,3 GB | 🔴 causa raiz swap |
| DB total | 3,2 GB | 🟡 inflado |
| `/uploads` | 62 GB / 823.337 arquivos | 🟡 pesado |
| Latência home non-AMP | TTFB 5,7s (+ 2 timeouts/3) | 🔴 crítico |
| Latência home AMP | TTFB 0,9s | 🟢 OK |
| Latência wp-admin login | TTFB 1,8-2,9s | 🟡 alto |

### 6.5.2 Stack

- **PHP 7.4.33** (EOL nov/2022) — **PHP 8.3 já instalado** mas site roda no 7.4
- **MySQL 5.7.44** (EOL out/2023)
- **nginx 1.28.0**
- Redis object cache ✅ (PONG, 256 MB), WP Rocket ✅, OPcache ✅
- `slow_query_log=OFF` (impede diagnóstico fino)

### 6.5.3 Vilões do banco (top 10 por tamanho)

| Tabela | Engine | MB | Observação |
|---|---|---|---|
| `wp_wffilemods` | InnoDB | 855 | Wordfence (modificações arquivo) |
| `wp_posts` | **MyISAM** | 545 | ⚠️ lock de tabela |
| `wp_wfknownfilelist` | InnoDB | 393 | Wordfence (hashes plugins) |
| `wp_postmeta` | **MyISAM** | 325 | ⚠️ lock de tabela |
| `wp_comments` | **MyISAM** | 305 | ⚠️ lock de tabela (625K linhas) |
| `wp_evermonitor_event_queue` | InnoDB | 234 | plugin sem rotação |
| `wp_commentmeta` | **MyISAM** | 153 | ⚠️ lock de tabela |
| `wp_wpr_rocket_cache` | InnoDB | 117 | cache no banco (anormal) |
| `wp_yoast_indexable` | InnoDB | 104 | Yoast SEO |
| `wp_yoast_seo_links` | InnoDB | 75 | Yoast SEO |

**Wordfence come 1,2 GB sozinho** (`wffilemods` + `wfknownfilelist`). **4 tabelas críticas ainda em MyISAM** (lock de tabela em escrita trava leitura em site com 625K comentários).

### 6.5.4 Causas-raiz (em ordem de impacto)

1. **PHP-FPM `pm.max_children=110`** → pode consumir 16 GB numa VPS de 8 GB → swap 2,5 GB → lentidão geral
2. **Wordfence 1,2 GB** inflando MySQL (CPU 203%)
3. **4 tabelas MyISAM** com lock de tabela em escrita
4. **`wp_evermonitor_event_queue` 234 MB** sem rotação
5. **PHP 7.4 EOL** (20-30% mais lento que 8.x)
6. **`wp_wpr_rocket_cache` 228K linhas no banco** (anormal)
7. **15 plugins inativos** no disco
8. **823K arquivos em `/uploads`** (62 GB)

### 6.5.5 Plano de leveza (12 itens em 3 tiers — AGUARDA Miguel)

**🟢 TIER 1 (baixo risco):** reduzir `pm.max_children` 110→40 · ligar slow_query_log · limpar Wordfence (TRUNCATE `wffilemods`) · limpar `evermonitor_event_queue` · deletar 15 plugins inativos · otimizar wp_options autoload (`colabs_template` etc.)
**🟡 TIER 2 (médio risco, com backup):** converter 4 tabelas MyISAM→InnoDB · migrar PHP 7.4→8.3 (com staging) · reindexar Yoast · configurar WP Rocket p/ não usar DB
**🟠 TIER 3 (alto risco/infra):** migrar MySQL 5.7→8.x · upgrade VPS 8→16 GB · `/uploads` p/ object storage (B2/S3) · CDN p/ imagens

### 6.5.6 Pontos saudáveis (NÃO mexer)

- ✅ Redis object cache funcionando
- ✅ WP Rocket + OPcache ativos
- ✅ Home non-AMP sem `gpt.js`/`adsbygoogle` (ads quase só AMP)
- ✅ Disco com espaço (47%)

### 6.5.7 Anomalias de segurança (bônus, fora do escopo)

- 🟠 IP `176.65.132.53` tentando exploit `device.rsp` (malware `data_arm7`) — várias tentativas, Wordfence não bloqueia
- 🟡 Requests a `timthumb.php` (theme `arthemia` antigo, vulnerabilidade RCE histórica)
- 🟢 Warning PHP `wp-smush-pro` (undefined array key)

---

## 🐛 7. BUGS CONHECIDOS (pre-existentes, não da reforma visual)

| ID | Severidade | Descrição | Status |
|---|---|---|---|
| LV-005 | 🟡 médio | 360yield header usa HTTP (mixed content) | DOCUMENTADO, aguarda Miguel |
| LV-006 | 🟠 investigar | 18 slots `.ad-space` vazios no non-AMP (sem gpt.js) | INVESTIGACAO_PENDENTE (browser headless) |
| LV-007 | 🟢 cosmético | Bloco 14 ad-inserter placeholder vazio órfão | DOCUMENTADO |

---

## 📝 8. CONTRATOS / REGRAS aprendidas

1. **6 fases do port cirúrgico** (do Claude): (0) descoberta read-only → (1) backup triplo SHA-256 → (5) rollback pré-instalado → (2) edição cirúrgica preservando ads/comentários → (3) mu-plugin isolado com nome DIFERENTE → (4) verificação HTTP + grep → (6) registro no fórum
2. **Nunca** editar `wp_options.ad_inserter` sem backup DB triplo
3. **Nunca** desativar `ad-inserter` / `accelerated-mobile-pages` (perde 16 slots GAM AMP)
4. **Nunca** portar mu-plugin `cafezinho-lab-ad-calhau.php` pro canônico
5. **Sempre** anotar bug em `lab_visual_bugs/bugs_YYYY-MM-DD.jsonl`
6. **URLs de categoria** são `/slug/` direto (não `/category/slug/`) — Yoast `stripcategorybase=true`
7. **wp-cli no canônico polui stdout** com `wp_bs_pagination()` — usar `php` + `wp-load.php` + `grep -v`, ou MySQL direto

---

## 🔗 9. LOG de descobertas (cronológico)

| Data/Hora | Agente | Descoberta | Documento |
|---|---|---|---|
| 2026-08-11 ~07:25 | ZCode (GLM-5.2) | Mapa ads completo + 4 retratações ao fórum do Claude (publisher real, contagem blocos, Quick AdSense/Colabs não existem) | `Foruns/forum_mapa_ads_canonico_ocafezinho_20260811.md` |
| 2026-08-11 ~07:40 | ZCode (GLM-5.2) | Comparação estrutura espelho vs canônico (front-page: 433 vs 258 linhas; 7 blocos vs 2) + top 40 categorias + autores | **ESTE ÍNDICE** (seção 4.1, 2.1, 3) |

---

## 🎯 10. PRÓXIMAS descobertas planejadas (backlog de aprendizado)

- [ ] Validar slots `.ad-space` vazios via browser headless (LV-006)
- [ ] Mapear `header.php` do canônico (quais hooks rodam, scripts carregados)
- [ ] Mapear `functions.php` do tema (loops, hooks, shortcodes)
- [ ] Listar 17 mu-plugins e o que cada um faz
- [ ] Entender `wpcode_snippets` (17 snippets funcionais — Denakop, noindex pruning, trava §94, etc.)
- [ ] Decodificar `wpseo` config (sitemaps, breadcrumbs, schema)
- [ ] Mapear rotas REST API expostas (`jwt-auth` + custom endpoints)
- [ ] Entender o fluxo editorial (quando o post é publicado, qual mu-plugin roda)
- [ ] Mapear `wp_post_signature` (assinatura do autor)
- [ ] Histórico de quando Quick AdSense/Colabs existiram (se existiram) — relevante pra LV-006

---

### 4.9 Balão comentários — reestilização (V2.5, aprendizado 11/08 09:05)

- **Antes (V2.2):** gradiente vermelho→laranja (#dc3545→#ff6b35), balão só aparecia se ≥1 comentário.
- **Miguel achou feio** o gradiente. Mudanças V2.5:
  1. **Fundo:** vermelho **ESCURO** sólido `#8b0000` (hover `#6b0000` — ainda mais escuro)
  2. **Letra:** branca **forçada** com `!important` (incluindo `.manchete-balao-numero`)
  3. **Lógica zero:** balão aparece **SEMPRE** (até 0 comentários). Se 0 → mostra **só 🔥** (sem número), title "Sem comentários ainda — seja o primeiro!". Se ≥1 → 🔥 + número.
- **Padrão aprendido:** `.icon-comments` do tema tem `background-image: url(...svg)` que vazava pro número dentro do balão. Solução: `background-image: none !important` na regra filha. Sempre que reusar classe do tema dentro de componente novo, verificar heranças de background.
- **Cores que combinam com "fogo":** vermelho escuro sólido (#8b0000) + emoji 🔥 nativo + outline laranja (#ff6b35) no focus. Laranja só no detalhe, vermelho escuro no fundo.
- **Backup + rollback:** `/root/balao_reestilizado_20260811/rollback.sh`

---

## Assinatura

**Custódia:** ZCode (ambiente)
**Criado por:** GLM-5.2 Z.ai (11/08/2026 07:40 BRT) — sessão fallback final
**Próxima revisão:** a cada descoberta significativa
