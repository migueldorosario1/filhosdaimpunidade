# Fórum — Publicação dos banners animados do Moka Reader no Cafezinho + temáticos

- **Data:** 16/08/2026 (~23:20–23:40 BRT)
- **Autor:** ZCode (Qwen 3.8 Max)
- **Status:** 📋 ESTUDO CONCLUÍDO — plano pronto, **aguarda decisões do Miguel + "vai"** para executar
- **Memória técnica:** `Memorias/memoria_banners_moka_reader_publicacao_cafezinho_tematicos_20260816.md`

---

## 1. O que são os banners

4 arquivos HTML **animados, únicos e autossuficientes** (fonte Archivo embutida em base64, animações em JS puro, funcionam offline, ~135 KB cada). O banner inteiro é clicável e abre **https://mokareader.com** em nova aba — link já embutido, **não alterar**. Formato "bundler": o arquivo descompacta o payload via JS ao carregar (placeholder SVG + "Unpacking..." por uma fração de segundo — comportamento normal).

| Arquivo | Formato | Idioma |
|---|---|---|
| `Moka Reader 300x250.html` | retângulo médio | PT |
| `Moka Reader 728x90.html` | leaderboard | PT |
| `Moka Reader 300x250 EN.html` | retângulo médio | EN |
| `Moka Reader 728x90 EN.html` | leaderboard | EN |

Local: `~/Downloads/Antigravity Google/Outros/mokareader/banners/` (design "Modernist"; substituem como peça de campanha o lote anterior de `moka/marketing/banners/`).

**Regra de idioma (Miguel):** PT só em sites/páginas PT; EN só em sites/páginas EN. Nunca misturar.

## 2. Paisagem de anúncios descoberta (recon 16/08, read-only)

### Cafezinho (canônico ocafezinho.com + espelho cafezinho.news)
- **Google Ad Manager** (rede `/21622511100`: slots `cafe_mobile_1..6`, half-page, interstitial) + **Taboola** + **Teads** + **MGID**, todos entregues via **Ad Inserter 2.8.17** (85 blocos canônico / 96 espelho).
- **Ad Inserter está DESLIGADO na home** (todos os blocos `display_on_homepage=0` — correção da rodada 6 de 14/08 contra empilhamento).
- Tema `ocafezinho-portal` tem **slots vazios `<div id="banner-*">`** preenchidos client-side pelo GAM:
  - `single.php`: before-content · before-comments · after-comments · after-related · after-recents (variantes -desktop/-mobile).
  - `front-page.php`: after-manchete · after-colunistas · after-latest · after-recents (variantes -desktop/-mobile, alternativos por dispositivo).
- **Regra Miguel (14/08):** nunca anúncio empilhado; no máx. 1 bloco de anúncio entre blocos de conteúdo; "um antes e um depois".
- **AMP ativo nos posts** (plugin Accelerated Mobile Pages): URLs `/amp/` com ~21 elementos `amp-ad`. AMP ≈ **64% das views** (análise 1.125 posts, 15/08).
- Espelho: mesmo stack; o **sync de hora em hora NÃO copia tema nem wp-content** — qualquer alteração precisa ser feita nos 2 servidores.

### Temáticos (8 sites, Astro + Vercel, repos `Projeto Cafezinho Agentes/sites-v4/`)
- **Todos os 8 carregam AdSense `ca-pub-8991943608456423` no modo AUTO ADS** (só o script + meta; nenhuma unidade `<ins>` fixa — o Google insere os anúncios automaticamente). GA4 próprio por site; `ads.txt` no `public/`.
- Idiomas (missão SEO 13/08): **PT** = Ceará (`ceara.digital`), Rio Carta (`riocarta.com`), Mapa Rio (`mapario.com.br`), Mundo Trilhos (`mundotrilhos.com`); **EN** = GSN (`globalsouth.news`), Rail Post (`railpost.news`), Discover Brazil (`discoverbrazil.news`); **Aiatolah (`aiatolah.com`) = bilíngue** (EN raiz + seção `/pt/`).
- `public/` do Astro é servido direto pela Vercel → lugar natural para hospedar os HTMLs.

## 3. Plano proposto

### Fase A — Cafezinho (espelho primeiro, depois canônico)
1. **Hospedagem:** criar `wp-content/moka-banners/` nos 2 servidores com os 2 arquivos PT renomeados sem espaço: `moka-300x250-pt.html`, `moka-728x90-pt.html` (chown www-data; teste HTTP 200). Nginx serve estático direto; WP Rocket não interfere.
2. **Inserção via slot novo no tema** (NÃO usar Ad Inserter — histórico de injeção posicional quebrando a home):
   - **Home:** 1 slot novo, desktop (728x90) + mobile (300x250) alternativos, no mesmo padrão `desktop-ad-space/mobile-ad-space`. **Posição recomendada: depois da Linha do Tempo / antes do rodapé** — região sem nenhum anúncio hoje, risco zero de empilhamento. (Miguel pode escolher outra.)
   - **Posts (opcional):** os posts já têm 5 slots GAM; se Miguel quiser Moka também no post, posição segura = 1 slot 300x250 no meio do conteúdo com matéria dos 2 lados. **Recomendação: começar só na home** e decidir depois.
3. **Iframe** no tamanho exato, `scrolling="no"`, `style="border:0;overflow:hidden"`, `title="Moka Reader"`; `loading="lazy"` por ser abaixo da dobra.
4. **AMP:** banner animado NÃO cabe em AMP (AMP proíbe JS externo; `amp-iframe` tem restrições pesadas de viewport). **Recomendação: começar sem banner no AMP** (aparece nos ~36% de views não-AMP) e medir; decidir depois se vale o esforço do `amp-iframe`.
5. Procedimento padrão: backup `.bak_pre_banners_moka_20260816` + `php -l` + purge Rocket (`wp-content/cache/wp-rocket/` + `cache/busting/` + `wp cache flush`) + prova curl/browser nos 3 viewports. Espelho primeiro.

### Fase B — Temáticos (8 sites)
1. Copiar para `public/banners/` de cada repo (PT nos 4 sites PT, EN nos 3 EN, **Aiatolah recebe os 2** — EN na raiz, PT na seção `/pt/`).
2. Criar componente `MokaBanner.astro` (iframe tamanho exato, lazy) e inserir **1 por home** (posição sugerida: entre as seções de conteúdo ou no fim, antes do footer — como os ads são AUTO, não há slot fixo para conflitar; só manter respiro visual).
3. Deploy por site: GSN publica sozinho no push (<1 min); **Aiatolah precisa `vercel --prod` manual** (webhook GitHub→Vercel inativo); demais: conferir remoto no ato. Validação: `astro build` verde + `/banners/*.html` HTTP 200 + iframe visível na home.

### Por que NÃO prejudica os anúncios (resposta direta ao Miguel)
1. **Nenhum slot de receita é tocado** — os `banner-*` do GAM ficam intactos; o Moka entra em slot NOVO dedicado.
2. **Políticas Google:** house ad (autopromoção) é permitida no AdSense/GAM; não mexe em ads.txt/leilão (não é inventário programático). Regras respeitadas: não imitar visual de anúncio do Google, não colocar dentro de unidade de anúncio, separação visível.
3. **Regra anti-empilhamento do Miguel respeitada** — posição recomendada da home fica em zona sem anúncio adjacente (auditada no fluxo da rodada 6).
4. **Zero CLS** (iframe com dimensões fixas) — CWV continua limpo (desktop 100% Bom).
5. **Performance:** 135 KB por banner, cacheados em browser/CDN; lazy loading; máx. 1 por dispositivo por página (desktop/mobile alternativos).
6. **Rollback trivial:** backups nomeados nos 2 servidores + `git revert` nos 8 temáticos.

## 4. Limitações conhecidas
- **AMP sem banner** (ver §3.4) — maior limitação de alcance no Cafezinho.
- **728x90 não cabe em mobile** (375px) — por isso o par alternativo desktop/mobile.
- O bundler mostra placeholder por ~1s no primeiro carregamento (sem cache).

## 5. Estado da missão
- **O que aconteceu:** estudo completo read-only (4 banners inspecionados; recon Ad Inserter/slots/AMP/Nginx no canônico+espelho; registry dos 8 temáticos; AdSense auto ads confirmado; idiomas mapeados). Zero escrita nos sites.
- **O que falta:** decisões abaixo + execução (estimativa: ~1h Cafezinho 2 servidores + ~1h30 temáticos 8 sites).
- **O que preciso de você (Miguel):**
  1. **Posição na home do Cafezinho** — aprova "depois da Linha do Tempo / antes do rodapé"?
  2. **Posts do Cafezinho** — só home (recomendado) ou quer nos posts também?
  3. **AMP** — ok começar sem banner no AMP?
  4. **Temáticos** — 1 banner por home basta? Qual posição prefere (fim da home vs. meio)?
  5. **"vai"** para executar (espelho primeiro, como sempre).

---
## §adendo — 16/08 ~23:59: banners AMP recebidos e VALIDADOS

**1ª leva (23:52) REPROVADA para AMP:** os 4 arquivos "... AMP.html" embutiam o conteúdo estático dentro do MESMO bundler JS dos animados — dentro de `amp-iframe` com sandbox sem `allow-scripts` ficariam congelados no placeholder "Unpacking..." para sempre. (Derivados que gerei foram descartados quando o Miguel avisou do zip.)

**2ª leva (23:58) APROVADA:** `Moka Reader Ad Banners.zip` → extraído em `banners/_zip_extraido/AMP estatico/` com os nomes de produção: `moka-300x250-pt.html`, `moka-728x90-pt.html`, `moka-300x250-en.html`, `moka-728x90-en.html`. Validação dos 4: **0 `<script>`** (~3,3 KB cada), dimensões fixas no body, frase principal fixa, `<a href="https://mokareader.com" target="_blank" rel="noopener">` cobrindo o banner, `lang` correto, visual idêntico aos animados.

**Duas ressalvas (resolvidas no plano):**
1. **Fonte externa:** carregam Archivo via `fonts.googleapis.com/css2` (não embutida). Se a requisição falhar, cai no fallback sans-serif — aceitável, não editar.
2. **Snippet do amp-iframe precisa de `allow-popups`:** o link usa `target="_blank"`; com só `allow-top-navigation` o clique é bloqueado pelo sandbox. Snippet correto:
```html
<amp-iframe width="300" height="250" layout="fixed" frameborder="0"
  sandbox="allow-popups allow-top-navigation"
  src="https://<origem-diferente>/moka-300x250-pt.html"></amp-iframe>
```

**Hospedagem (obrigação do amp-iframe):** HTTPS + **origem diferente** da página AMP (www.ocafezinho.com). **Recomendação: projetinho estático na Vercel** (`moka-banners`) com os 4 estáticos (e opcionalmente os 4 animados, virando fonte única p/ tudo). Alternativas descartadas: espelho cafezinho.news (gambiarra usar o mirror como CDN do canônico) e Tencent (sem domínio/cert público). **Decisão do Miguel.**

**Inserção nas páginas AMP do Cafezinho:** criar bloco `[ADINSERTER AMP]` novo no Ad Inserter (mesmo mecanismo dos amp-ad existentes, blocos 13/18-37), posição no meio do artigo (regra do amp-iframe: ≥600px do topo / fora do 1º viewport — no corpo do artigo cumpre; se não cumprir, o elemento fica vazio sem quebrar a página).

**Mapa final de arquivos p/ execução (8):**
- Não-AMP (animados): `Moka Reader 300x250.html` (PT), `728x90.html` (PT) no Cafezinho; versões EN nos 3 temáticos EN; Aiatolah usa PT e EN conforme a seção.
- AMP (estáticos): os 4 do zip, hospedados na origem diferente.

---
## §adendo 2 — 17/08 ~01:10: APLICADO NO CAFEZINHO (home + single posts), nos 2 servidores

**Ordem do Miguel:** "bota nos single posts também. encontra um lugar vazio para esses banners."

**Recon dos lugares vazios (provas no log técnico da memória):**
- Todos os divs `banner-*` do tema `ocafezinho-portal` são **placeholders MORTOS** — o HTML renderizado (espelho e canônico) vem com eles vazios; nenhum bloco Ad Inserter os preenche.
- Os anúncios VIVOS do single entram via Ad Inserter **client-side** em posições próprias: GAM `CafeMobile-1` no header; `CafeMobile-2..5` depois do 6º/12º/16º/18º parágrafos; `CafeMobile-6` after-post; **Taboola + half-page dentro da seção de comentários** (`#comentario`); Teads no footer; MGID com seletor de tema antigo = morto; interstitial = overlay.
- CSS do tema (bloco F1 de 11/08): `.desktop-ad-space` só aparece ≥992px, `.mobile-ad-space` <992px — 1 por vez, sem empilhar.

**Posições escolhidas (regra do Miguel respeitada — 1 anúncio por intervalo, nada adjacente a anúncio vivo):**
1. **Single posts:** iframes dentro dos divs mortos `banner-before-content-desktop` (728x90) e `banner-before-content-mobile` (300x250) — entre a foto destacada e o corpo do texto. Anúncio vivo mais próximo acima = CafeMobile-1 no header (separado por título/excerpt/foto); abaixo = só depois do 6º parágrafo.
2. **Home:** div NOVO `#moka-banner-home` (container centralizado) **depois da Linha do Tempo, antes do Histórico/footer** — posição recomendada no estudo; home não tem nenhum anúncio vivo (todos os blocos Ad Inserter com `display_on_homepage=0`).

**Execução (espelho primeiro, como sempre):**
- Arquivos PT estáticos do zip em `wp-content/moka-banners/` nos 2 servidores: `moka-728x90-pt.html` + `moka-300x250-pt.html` (HTTP 200 nos dois domínios). Versões EN ficam reservadas p/ AMP e temáticos.
- `single.php`: iframes com `content_url()` nos 2 divs `banner-before-content-*` (idêntico nos 2 servidores; md5 original 312c69f4…).
- `front-page.php`: bloco `#moka-banner-home` inserido após o `<!-- LINHA DO TEMPO -->` (arquivos DIFEREM entre servidores — editados separadamente).
- `php -l` verde em tudo; backups `.bak_pre_banners_moka_20260817` ao lado de cada arquivo; Rocket purgado no canônico.
- **Gotcha do canônico:** WP Smush Pro converte os iframes em lazyload (`data-src` + placeholder) — carrega quando entra no viewport, comportamento correto; no espelho sai `src` direto.

**Validação ao vivo (espelho + canônico):** home com Moka entre Linha do Tempo e footer ✓; single com iframes no lugar certo ✓; iframe-arquivo 200 nos dois domínios ✓.

**O que falta / preciso do Miguel:**
1. **AMP (~64% das views):** segue precisando de hospedagem dos estáticos em origem HTTPS diferente (recomendação: projeto Vercel `moka-banners`) + bloco `[ADINSERTER AMP]` — aguarda OK.
2. **Temáticos (8 sites):** plano pronto no estudo (`public/banners/` + `MokaBanner.astro`, idioma casado) — aguarda ordem.

---
## §adendo 3 — 17/08 ~08:05: RESPIRO entre anúncio comercial e banner Moka (fix NO AR nos 2 servidores)

**Ordem do Miguel (print mobile 07:44):** no celular o banner Moka (300x250) apareceu **colado** no anúncio comercial GAM — *"não pode. deixa um espaço de respiração entre esses dois banners. um pequeno espaço de respiração para não ficarem colados."*

**Causa (recon):** o anúncio que gruda no Moka no mobile é o bloco **25** do Ad Inserter (GAM, `html_selector=.featured-image-content`, dt=16) — injetado logo DEPOIS da foto destacada, exatamente em cima do div `#banner-before-content-mobile` onde mora o Moka. A margem padrão do tema (20px, regra `#banner-before-content-*` do bloco "Definições de Banners Anúncio") existia mas era curta demais. Nota: blocos 1-19 do Ad Inserter estão com `disable_insertion=1` (desativados); os vivos são 24-37.

**Fix aplicado (espelho primeiro, como sempre):** bloco CSS no FIM do `style.css` (depois de todas as regras do tema; mesma especificidade → vence o 20px):
```css
#banner-before-content-mobile { margin-top: 28px; }
#banner-before-content-desktop { margin-top: 28px; }
```
- Nos 2 servidores (canônico + espelho), comentário datado + backup `style.css.bak_pre_respiro_moka_20260817` ao lado; rollback documentado no próprio comentário (remover o bloco).
- `functions.php` enfileira o CSS com `filemtime` → `?ver` auto-bump para `1786963715`; Rocket purgado (cache/busting/min) + `wp cache flush` no canônico.
- **Prova servidor:** CSS entregue ao vivo contém a regra 28px DEPOIS da regra 20px do tema (linhas 1462-1463 × 655).
- **Prova navegador (IAB, post China×Índia 17/08):** `link#main-styles-css` = `style.css?ver=1786963715` e margem computada do div = **28px** (leitura anterior de 20px era cache velho do cliente; resolvida com reload).

**Estado:** pronto. Miguel deve dar refresh no celular para ver o respiro. Pendências anteriores seguem: AMP (Vercel `moka-banners` + bloco `[ADINSERTER AMP]`) e temáticos (8) — aguardam decisão/ordem do Miguel.

---
## §adendo 4 — 17/08 ~08:45: RESPIRO v2 — Moka fora dos slots do Denakop (fix NO AR nos 2 servidores)

**Ordem do Miguel (chat 08:2x, após print + "ainda está grudado"):** *"cuidado com o anúncio do denakop, que é comercial e deve ser respeitado. se achar necessário, bota o moka em outro lugar, mais para baixo do post."*

**Diagnóstico correto desta vez (o do §adendo 3 estava incompleto):** os divs `banner-before-content-*` NÃO estavam vazios de verdade — o script **Denakop** (`tags.denakop.com/10819/ocafezinho.com.js` via `servg1.net/o.js`, anúncio comercial do Miguel) injeta client-side o slot `denakop-scroll-1` DENTRO deles. O Moka estava dividindo o MESMO container com o anúncio — por isso nenhuma margem externa separava (e o "respiro" de margin-top do §3 empurrava o slot inteiro, não o espaço entre os dois). Sequência vista no celular bate: 1º o Moka (iframe leve), depois o anúncio Denakop preenche o slot no mesmo div → colados.

**Fix (respeita o Denakop — anúncio intacto no slot dele):**
- `single.php`: os 2 divs `banner-before-content-desktop/mobile` voltaram a ser slots VAZIOS (para o Denakop) e o Moka ganhou div PRÓPRIO `#moka-banner-before-content` logo abaixo, com os 2 iframes (desktop 728x90 / mobile 300x250) nas classes responsive do tema.
- `style.css` (fim): `#moka-banner-before-content { margin-top: 28px; margin-bottom: 28px; }` — respiro entre o anúncio Denakop e o Moka, e entre o Moka e o texto.
- Backups `single.php.bak_pre_moka_div_proprio_20260817` + `style.css.bak_pre_moka_div_proprio_20260817` nos 2 servidores; `php -l` verde; Rocket purgado; `?ver=1786966610`.
- **Provas:** DOM mobile headless = `banner-before-content-mobile` contém só o div do Denakop; `#moka-banner-before-content` separado com 2 iframes. Navegador real (IAB): margem computada 28px/28px, slot desktop com o anúncio Denakop dentro. curl desktop+mobile = estrutura nova no canônico E no espelho (post do espelho validado: 16/08 bancos-endurecem-credito).

**Estado:** pronto nos 2 servidores. Miguel deve dar refresh no celular. Denakop intocado. Pendências anteriores seguem: AMP (Vercel `moka-banners` + `[ADINSERTER AMP]`) e temáticos (8) — aguardam Miguel.

---
## §adendo 5 — 17/08 ~10:30: banner Moka CORTADO no espelho — fix height no iframe (NO AR, 2 servidores)

**Ordem do Miguel (print mobile, post Vila Clara no espelho):** banner Moka aparece cortado no espelho (`cafezinho.news/2026/08/17/a-voz-de-vila-clara-capitulo-1-o-herdeiro-do-contrato/`); no canônico está correto.

**Causa (medida por CDP, não chute):** o espelho carrega o mu-plugin `cafezinho-lab-visual.css` com a regra global `img, iframe, video { max-width: 100%; height: auto; }` — o `height: auto` sobrescreve o atributo `height="250"` do iframe e o navegador usa a altura default de 150px (iframe sem razão intrínseca) → o banner 300x250 renderizava 300x150 = cortado. O canônico NÃO tem esse mu-plugin (por isso estava correto). Medida: iframe 300x150 no espelho × 300x250 no canônico.

**Fix (inofensivo no canônico):** altura explícita no style inline dos 4 iframes Moka (single + front-page/home, 2 servidores): `height:90px` no 728x90 e `height:250px` no 300x250. Style inline vence o `height:auto` do lab-visual. Backups `.bak_pre_moka_height_20260817` ao lado de single.php e front-page.php nos 2 servidores; `php -l` verde; Rocket purgado no canônico.
- **Provas (CDP):** espelho single mobile iframe 300x250 ✓ (antes 300x150); espelho single desktop div 90px ✓; espelho home mobile iframe 300x250 ✓; canônico mobile h=250 sem regressão ✓.

**Estado:** pronto. Pendências anteriores seguem: AMP (Vercel `moka-banners` + `[ADINSERTER AMP]`) e temáticos (8) — aguardam Miguel.

---

## ADENDO 19/08 ~12:50 BRT — BANNER MOKA DO SINGLE DESCE (ordem Miguel ~12:35)

**Queixa do Miguel:** no single post, depois da foto principal apareciam DOIS anúncios empilhados (slot Denakop + banner Moka) — "a gente até criou um espaço de respiração, mas não ficou legal". **Ordem:** tirar o Moka dali e colocar lá embaixo — depois do "Leia também" e antes do bloco "Inscreva-se na Newsletter".

**Mapeamento (canônico):** o single.php tinha o Moka hardcoded logo após a foto (`#moka-banner-before-content`, linhas 45-56). Os blocos "Leia também" e "Newsletter" são injetados no `the_content` pelo snippet WPCode **255106** ("Blocos externos ao post_content", prio 20; só em posts com `_cafezinho_external_blocks_v1=true`).

**Implementado (backups + php -l nos 2 sites):**
1. **single.php** (canônico + espelho, `.bak_pre_moka_desce_20260819`): div do Moka REMOVIDA do topo (904 chars) — o slot Denakop fica sozinho (fim dos dois anúncios empilhados).
2. **Mu-plugin novo `cafezinho-moka-single.php`** (nos 2 sites): filtro `the_content` prio 25 (depois do WPCode) insere o banner ANTES do `<aside class="cafezinho-newsletter">` — ou seja, depois do "Leia também"; sem os blocos externos, cai no fim do conteúdo. Rollback: apagar o arquivo.
3. **Verificado ao vivo:** post real do canônico com a ordem exata Leia também → Moka → Newsletter; topo sem o Moka; espelho igual (lá sem os blocos externos → fim do conteúdo). Sites 200.
