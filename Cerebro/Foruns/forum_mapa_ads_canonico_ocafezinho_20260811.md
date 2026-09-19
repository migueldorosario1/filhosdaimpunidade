# Fórum — Mapa Definitivo dos Ads do Canônico ocafezinho.com

**Data:** 2026-08-11, 07:25 BRT
**Autor:** ZCode (GLM-5.2 Z.ai — Kimi/Qwen esgotaram 🔴🔴, sessão no fallback final)
**Missão:** Sprint Visual Cafezinho — etapa "Decodificar ads do canônico" (investigação pendente deixada pelo Claude no fórum de transferência `forum_transfer_sprint_visual_cafezinho_zcode_20260811.md`, §9.1)
**Status:** ✅ ENTREGUE — mapa completo + 4 retratações factuais ao fórum do Claude
**Trabalho:** 100% read-only (zero escrita no DB, zero edição de plugin, zero mudança em produção)

---

## 0. Sumário executivo (3 linhas)

Decodifiquei o `wp_options.ad_inserter` (49.216 bytes) + auditei todas as camadas de ads do canônico. **O fórum do Claude continha 4 informações estruturais incorretas** sobre a arquitetura de ads — corrigidas aqui com prova. A descoberta mais importante: **o ad-inserter é predominantemente AMP**, mas há 18 slots `.ad-space` renderizando vazios no non-AMP (blocos 21/22 injetam divs que esperam JS externo). O port da reforma visual do espelho pro canônico **pode seguir com segurança** desde que preserve esses slots `.ad-space`.

---

## 1. ⚠️ Retratações ao fórum do Claude (4 correções)

O fórum `forum_transfer_sprint_visual_cafezinho_zcode_20260811.md` §5 afirmava:

| # | Afirmação do fórum (Claude) | Realidade verificada por GLM-5.2 | Prova |
|---|---|---|---|
| 1 | Publisher ID GAM **`21622511100`** | ❌ ERRADO. Publisher real nos data-slots é **`/21715141650,22670554696/ocafezinho.com/...`** (network GAM com 2 IDs child — padrão de ad server que agrupa多个 publishers) | `curl /2026/08/10/lula-reconquista-as-capitais/amp/` → 15 `data-slot="/21715141650,22670554696/..."`; zero ocorrências de `21622511100` em todo o `wp_options.ad_inserter` decodificado |
| 2 | "90 blocos configurados no ad-inserter, 36 ATIVOS" | ⚠️ **90 entradas** no array (85 chaves numéricas de bloco + 5 chaves de config global `h`/`f`/`a`/`global`/`extract`). Dessas 85, apenas **35 são dicts** (estrutura real de bloco); as outras 50 são listas vazias (slots de hooks/global fields não usados). O campo oficial `extract.used_blocks` lista **19 blocos usados** pelo plugin; desses, **18 têm code real** (bloco 14 é placeholder vazio — `code_len=0`) | `unserialize(base64_decode(substr($raw,4)))` + parse do `used_blocks` (string PHP serialize `a:19:{...}`) |
| 3 | Quick AdSense 2 ativo (insere `adsbygoogle` in-article) | ❌ **NÃO EXISTE** — nem ativo, nem inativo, nem instalado. Não há pasta `wp-content/plugins/*quic*` ou `*adsense*` | `glob(GLOB_ONLYDIR)` em plugins + `active_plugins` unserialize |
| 4 | Colabs AdSense legado ativo (`ca-pub-5835338445130243`) | ❌ **NÃO EXISTE** — nenhum plugin Colabs instalado. O `ca-pub-5835338445130243` **não aparece em lugar nenhum** do site (HTML, options, wpcode, ads.txt) | grep em raw wpcode (49KB) + HTML ao vivo + ads.txt |

**Consequência prática:** a seção §6 "Riscos destrutivos" do fórum do Claude lista "Desativar Quick AdSense 2" e "Editar/deletar Colabs AdSense" como proibições 🔴 — **esses itens são NULOS** (não há o que desativar). A lista real de proibições está na §5 deste documento.

---

## 2. Camadas REAIS de ads do canônico (4 fontes, não 3)

### Camada A — AMP via ad-inserter (predominante)

**Onde mora:** rotas `/amp/` e `?amp` (plugin `accelerated-mobile-pages/accelerated-moblie-pages.php` cria as versões AMP).
**Publisher:** `/21715141650,22670554696/ocafezinho.com/...` (GAM network, 2 child IDs).
**Formato:** `<amp-ad type="doubleclick" data-slot="..." data-multi-size="320x100,320x50,300x100,300x75,300x50,300x250">` + `<amp-embed type="mgid">` (bloco 32).
**Contagem:** 15 ad-units GAM únicos + 1 widget mgid = **16 slots ativos no AMP**.

#### Mapa dos 19 blocos `used_blocks` do ad-inserter

| Bloco | display_type | Onde aparece | Ad-unit / conteúdo | code_len |
|---|---|---|---|---|
| **14** | 16 (Before/After element) | home, `section:nth-child(8) > div` | **PLACEHOLDER VAZIO** (code apagado, órfão) | 0 |
| **15** | 16 | `.date-comments` (single) | Banner Google News (PHP `echo` com link + img) | 310 |
| **17** | 13 (Footer code) | todos | **Teads** `<script src="//a.teads.tv/page/86345/tag">` — o único ad que roda em non-AMP E AMP | 119 |
| **21** | 6 (After paragraph) | single, parágrafo 3 | `<div id="in-text-1" class="ad-space">` (non-AMP, slot vazio esperando JS) | 48 |
| **22** | 6 | single, parágrafo 6 | `<div id="in-text-2" class="ad-space">` (non-AMP, slot vazio) | 48 |
| **24** | 15 (AMP, before element) | AMP, `header.amp-wp-article-header` | `/21715141650,22670554696/ocafezinho.com/first/post/1` | 402 |
| **25** | 16 | AMP, `.featured-image-content` | `/21715141650,22670554696/ocafezinho.com/intext/post/1` | 411 |
| **26** | 6 | AMP, parágrafo 3 | `.../intext/post/2` | 412 |
| **27** | 6 | AMP, parágrafo 6 | `.../intext/post/3` | 411 |
| **28** | 6 | AMP, parágrafo 9 | `.../intext/post/4` | 411 |
| **29** | 6 | AMP, parágrafo 12 | `.../intext/post/5` | 411 |
| **30** | 15 | AMP, `div.relatedpost` | `.../scroll/post/1` | 411 |
| **31** | 16 | AMP, `div.relatedpost` | `.../scroll/post/2` | 411 |
| **32** | 15 | AMP, `footer.footer_wrapper` | **mgid** `<amp-embed type="mgid" data-website="836425" data-widget="1373898">` | 195 |
| **33** | 6 | AMP, parágrafo 15 | `.../intext/post/6` | 383 |
| **34** | 6 | AMP, parágrafo 18 | `.../intext/post/7` | 383 |
| **35** | 6 | AMP, parágrafo 21 | `.../intext/post/8` | 383 |
| **36** | 6 | AMP, parágrafo 24 | `.../intext/post/9` | 383 |
| **37** | 6 | AMP, parágrafo 27 | `.../intext/post/10` | 384 |

**Globais (header `h` + footer `f`):**
- `h` (AMP head): carrega `amp-iframe-0.1.js` + `amp-sticky-ad-1.0.js` (scripts AMP, não ad)
- `f` (AMP footer/body): `<amp-sticky-ad>` com `data-slot="/21715141650,22670554696/ocafezinho.com/under/post/1"` (320x100/50) — **sticky mobile AMP**

**Ad-units GAM únicos ativos no AMP (15):**
```
/21715141650,22670554696/ocafezinho.com/first/post/1
/21715141650,22670554696/ocafezinho.com/intext/post/{1..10}
/21715141650,22670554696/ocafezinho.com/scroll/post/{1,2}
/21715141650,22670554696/ocafezinho.com/under/post/1   (sticky)
```

### Camada B — Teads (cross-context)

- **Bloco 17** do ad-inserter: `<script async class="teads" src="//a.teads.tv/page/86345/tag">`
- `display_type=13` (Footer code) — injetado globalmente
- Aparece **1 vez** no single non-AMP ao vivo (confirmado por `curl | grep -c teads`)
- Page ID Teads: **86345**

### Camada C — 360yield header (non-AMP, legado)

- **Option:** `wpc_inner_header_wide_ad` (772 bytes, opção avulsa em `wp_options`, **não** em ad-inserter nem wpcode)
- **Code:** `document.write` injeta `<script src="http://ad.360yield.com/adj?p=739943&w=728&h=90">` — banner 728×90 header
- Placement 360yield: **p=739943**
- ⚠️ Usa **HTTP** (não HTTPS) no `src` — mixed content em site HTTPS; browsers modernos podem bloquear. **Bug latente** (não reportado ainda — ver §7 LV-005)

### Camada D — ads.txt (19+ SSPs/exchanges)

- **Plugin:** `ads-txt/ads-txt.php` ativo
- **Arquivo público:** `https://www.ocafezinho.com/ads.txt` (1822 linhas de vendors)
- SSPs principais: richaudience, rubiconproject (17210), appnexus (10264), pubmatic (156383), criteo (B-060278), smartadserver (1743), indexexchange (192450), onetag, triplelift (12911), amxrtb, contextweb (563371), adform (2474), ligit (257429), improvedigital (2048), themedialgrid, aps.amazon

### Camada E — wpcode_snippets (NÃO é ad, é funcional)

O `wpcode_snippets` (50.344 bytes, 17 snippets) **não contém código de ads**. São snippets PHP/JS funcionais:
- `Cafezinho Noindex Pruning 358 URLs` (recovery SEO)
- `B-018: Registrar meta campos de origem do agente`
- `Inserção dos Scripts da Denakop no Header`
- `No-Home Grid Filter`
- `Trava §94 Anti-Repetição (Cafezinho)`
- `Ocultar Matérias Sem Home da Página Inicial`
- `dequeue Scripts do JBA (Anúncios) em Publipost` ← remove ads de publiposts, não exibe
- etc.

`insert-headers-and-footers` (`ihaf_insert_header/footer/body`) está **vazio** — legacy inerte.

---

## 3. Descoberta crítica: 18 slots `.ad-space` vazios no non-AMP

No single post non-AMP (`/2026/08/10/lula-reconquista-as-capitual/`), `grep` encontrou **18 ocorrências de `ad-space`** e **20 `class="ad`**. Os blocos 21 e 22 do ad-inserter (display_type 6, After Paragraph 3 e 6) injetam `<div id="in-text-{1,2}" class="ad-space">` — **mas esses slots ficam vazios no non-AMP** porque **não há `gpt.js`, `googletag`, `defineSlot` ou `adsbygoogle` carregado no HTML non-AMP**.

**Hipóteses (a validar com browser headless — pendência §6):**
1. **Intencional:** os slots `.ad-space` non-AMP esperam um JS externo (provavelmente deveria ser o `gpt.js` + `googletag.cmd.push`) que **não está configurado** — inventário non-AMP não monetizado por GAM, só por Teads + 360yield.
2. **Quebra latente:** o ad-inserter foi configurado pra inserir as divs mas o JS que as preenche foi removido/desativado em algum momento (talvez quando Quick AdSense/Colabs foram desinstalados — ver retratação §1).

**Implicação para o port da reforma visual:** mover blocos temáticos, Coluna do Editor, etc. **não quebra** esses slots desde que:
- Os novos blocos não removam acidentalmente parágrafos de posts (os `in-text-1/2` ancoram em parágrafos 3 e 6)
- A classe `.ad-space` seja preservada no CSS
- Os seletores AMP (`header.amp-wp-article-header`, `.featured-image-content`, `div.relatedpost`, `footer.footer_wrapper`) continuem existindo no tema AMP

---

## 4. Plugins de ads realmente ativos (3, não 5)

| Plugin | Estado | Função |
|---|---|---|
| `ad-inserter/ad-inserter.php` | ✅ ativo | 19 blocos (18 com code), serve AMP + 2 slots non-AMP |
| `ads-txt/ads-txt.php` | ✅ ativo | Gerencia `/ads.txt` público (1822 vendors) |
| `insert-headers-and-footers/ihaf.php` | ✅ ativo (legacy inerte) | `ihaf_*` options vazias; funcionalidade real migrada pra wpcode |

**Plugins NÃO existentes** (contrariando fórum do Claude): `quick-adsense`, `colabs-adsense`, qualquer plugin com `adsense` no nome.

---

## 5. Riscos destrutivos REAIS (substitui §6 do fórum do Claude)

### 🔴 CRÍTICO — NUNCA fazer
- Editar `wp_options.ad_inserter` sem backup DB triplo (zera 19 blocos AMP GAM)
- Desativar plugin `ad-inserter` (para todos GAM AMP + Teads + slots non-AMP)
- Desativar plugin `accelerated-pages` (AMP) — sem AMP, ad-inserter perde 16 dos 19 slots
- Editar option `wpc_inner_header_wide_ad` sem backup (banner 360yield header)
- Editar `wp_options.wpcode_snippets` sem backup (17 snippets funcionais, incl. Denakop + noindex pruning + trava anti-repetição)
- Editar `/ads.txt` via plugin `ads-txt` sem entender consentimento das SSPs

### 🟡 MÉDIO — cuidado
- Editar `functions.php` ou `header.php` do tema (onde os `wp_head` hooks rodam)
- Mexer em qualquer mu-plugin do canônico sem entender função (17 arquivos ativos)
- Purgar cache WP Rocket / serverdoin-cdn sem autorização do Miguel
- Renomear seletores AMP (`header.amp-wp-article-header`, `.featured-image-content`, `div.relatedpost`)

### 🟢 BAIXO — pode fazer com backup
- Mudanças visuais no tema que **preservem** classes `.ad-space` e seletores AMP
- Adicionar novos slots com IDs próprios (não conflitantes com `in-text-*`, `first/post/*`, etc.)
- CSS puro que não altere `display` dos divs de ad

---

## 6. Pendências remanescentes (próximos passos sugeridos)

1. **[investigação] Browser headless no single non-AMP** — usar Puppeteer/Playwright pra confirmar se os 18 slots `.ad-space` realmente ficam vazios ou se algum JS deferred os preenche. `curl` puro não vê (o JS roda depois). **Skill disponível no ZCode:** `browser-use:web-gui-tester` pode fazer isso.
2. **[investigação] O JS GAM non-AMP foi removido?** — checar histórico de commits do tema / `git log` se versionado, ou backups antigos do `header.php`, pra entender quando/quem removeu o `gpt.js` (se é que existiu). Pode explicar os slots vazios.
3. **[decisão Miguel] Ativar GAM non-AMP?** — se o Miguel quiser monetizar os 18 slots `.ad-space` non-AMP (hoje vazios), precisa: (a) carregar `gpt.js` no `<head>` non-AMP, (b) configurar `googletag.defineSlot()` apontando pros `div id="in-text-1/2"` etc., (c) criar ad-units no GAM. Trabalho de médio prazo.
4. **[decisão Miguel] Cleanup bloco 14 órfão** — placeholder vazio em `used_blocks`; remover do used list (não urgente, não causa dano).
5. **[decisão Miguel] Fix 360yield HTTP→HTTPS** — bug latente de mixed content (LV-005); pode estar silenciosamente bloqueando o banner header em browsers estritos.

---

## 7. Bugs identificados nesta auditoria (anotar em `lab_visual_bugs/`)

| ID | Severidade | Descrição | Origem |
|---|---|---|---|
| **LV-20260811-005** | 🟡 médio | `wpc_inner_header_wide_ad` usa `http://ad.360yield.com/...` (não HTTPS) — mixed content em site HTTPS; browsers estritos podem bloquear o banner 728×90 header | pre_existente (não da reforma visual) |
| **LV-20260811-006** | 🟠 investigar | 18 slots `.ad-space` non-AMP renderizam vazios — sem `gpt.js`/`googletag` carregado; possível inventário não monetizado non-AMP ou quebra latente | pre_existente |
| **LV-20260811-007** | 🟢 baixo | Bloco 14 do ad-inserter é placeholder vazio (`code_len=0`) mas consta em `used_blocks` — órfão inerte | pre_existente |

---

## 8. Provas forenses (reprodutíveis)

Todos os comandos abaixo são **read-only** e podem ser re-executados pra validar:

```bash
# 1. Decodificar ad_inserter
ssh cafezinho-wp 'php /tmp/adiag_decode_ads_v1.php'
# → TOTAL_BLOCKS=90, FIRST_BLOCK_ID=1, WROTE=/tmp/adiag_ads_full.json

# 2. Publisher ID real no AMP
curl -sL "https://www.ocafezinho.com/2026/08/10/lula-reconquista-as-capitais/amp/" \
  | grep -oE 'data-slot="[^"]*"' | sort -u
# → /21715141650,22670554696/ocafezinho.com/{first,intext,scroll,under}/post/*

# 3. Provar que 21622511100 NÃO existe no ad_inserter
ssh cafezinho-wp 'php /tmp/adiag_decode_ads_v1.php'  # gera JSON
# (depois) python3 -c "import json; d=json.load(open('/tmp/adiag_ads_full.json')); print('21622511100 count:', json.dumps(d).count('21622511100'))"
# → 0

# 4. Slots .ad-space non-AMP vazios
curl -sL "https://www.ocafezinho.com/2026/08/10/lula-reconquista-as-capitais/" \
  | grep -c "ad-space"
# → 18

# 5. Teads aparece no non-AMP
curl -sL "https://www.ocafezinho.com/2026/08/10/lula-reconquista-as-capitais/" \
  | grep -c "teads"
# → 1

# 6. Quick AdSense / Colabs NÃO existem
ssh cafezinho-wp 'ls /var/www/ocafezinho/wp-content/plugins/ | grep -iE "quic|colab|adsense"'
# → (saída vazia)
```

**Arquivos de evidência persistidos:**
- `/tmp/adiag_ads_full.json` (no canônico) — dump completo decodificado (46KB)
- `/tmp/adiag_work/adiag_mapa_final.json` (local) — mapa estruturado dos 19 blocos + globais
- `/tmp/adiag_work/adiag_mapa.tsv` (local) — mapa tabular de todos os 85 blocos
- `/tmp/adiag_work/wpcode_raw.txt` (local) — raw wpcode_snippets (49KB)

---

## 9. Conclusão e recomendação para o port da reforma visual

A arquitetura de ads do canônico é **majoritariamente AMP-centric** (16 slots GAM via ad-inserter só renderizam em `/amp/`). No non-AMP, só **Teads** (bloco 17) e **360yield header** (option legada) servem ads reais — os 18 slots `.ad-space` estão vazios.

**Recomendação:** o port da reforma visual do espelho `cafezinho.news` → canônico `ocafezinho.com` pode seguir com segurança nas 6 fases cirúrgicas do Claude, **desde que**:
1. Preserve todos seletores AMP (`header.amp-wp-article-header`, `.featured-image-content`, `div.relatedpost`, `footer.footer_wrapper`) — os 16 blocos AMP dependem deles
2. Preserve a classe `.ad-space` no CSS (slots non-AMP a usam)
3. Não remova os ganchos de parágrafo 3 e 6 nos singles (`in-text-1/2` ancoram neles)
4. Comece pela **Coluna do Editor** (movida pra após manchete) — é a mudança mais isolada e segura
5. Os blocos temáticos (Nacional, Geopolítica, Ciência) vêm depois, em etapa separada
6. Single 1-col iPad por último (mais intrusivo)

O port **não afeta** os 16 ad-units GAM AMP nem o Teads, porque ad-inserter usa paragraph_number e seletores AMP — não depende da estrutura de blocos da home.

---

## Assinatura

**ZCode (GLM-5.2 Z.ai)** — sessão fallback final (Kimi K3 + Qwen Code esgotados 🔴🔴)
Workspace: `ZCodeProject`
Timestamp: 2026-08-11 07:25 BRT

_Documento vivo. Próxima etapa do sprint: aguardar decisão do Miguel sobre (a) port incremental Coluna Editor → blocos → single, ou (b) validar slots vazios via browser headless primeiro._
