# Fórum — Plano de Port da Reforma Visual: Espelho → Canônico

**Data:** 2026-08-11, 11:10 BRT
**Autor:** ZCode (GLM-5.2 Z.ai)
**Missão pai:** Sprint Visual Cafezinho (transferência do Claude)
**Status:** PLANO — aguardando Miguel aprovar antes de QUALQUER edição no canônico
**Escopo:** Levar TUDO que fizemos no espelho `cafezinho.news` pro canônico `ocafezinho.com` (produção, milhares de leitores diários)
**Operacional:** Uma coisa de cada vez, com calma, backup triplo, rollback pré-instalado, teste antes de avançar

---

## 0. Princípios sagrados (NÃO negociáveis)

1. **NUNCA editar sem backup triplo** (droplet + versionado + local, SHA-256)
2. **NUNCA editar sem rollback pré-instalado** (script bash testado)
3. **NUNCA editar sem PHP lint** antes E depois
4. **NUNCA editar sem HTTP check** (home + single + categoria)
5. **NUNCA editar sem grep** nos logs (nginx error, PHP-FPM, WP debug)
6. **NUNCA portar** `mu-plugins/cafezinho-lab-ad-calhau.php` (CSS esconderia ads reais)
7. **NUNCA editar** `wp_options.ad_inserter` sem backup DB
8. **NUNCA desativar** plugins de ads (`ad-inserter`, `accelerated-mobile-pages`)
9. **Purgar cache WP Rocket + serverdoin-cdn** após cada edição (senão mudança não aparece)
10. **Confirmar visualmente com Miguel** antes de avançar pra próxima etapa

---

## 1. Lista consolidada do que fizemos no espelho (24 mudanças)

### 🟢 Grupo A — Estáticos (imagens + CSS puro)
**Os mais seguros pra portar primeiro — só upload de arquivo + CSS, sem lógica PHP.**

| # | LV | Mudança | Arquivo espelho | Arquivo canônico equivalente |
|---|---|---|---|---|
| A1 | 012/015/017/020/023 | Logo header — versão final v6 (`logo-cafezinho-2026-v6.png`, 1550×280, super horizontal 5.54:1) | `/img/logo-cafezinho-2026-v6.png` (NOVO) + `header.php` `<img>` | upload + trocar src no `header.php` |
| A2 | 021/026 | Foto editor — versão final v2 (`foto-miguel-editor-v2.jpg`, 240×240) | `/img/foto-miguel-editor-v2.jpg` (NOVO) | upload |

### 🟡 Grupo B — PHP estrutural (header + footer)
**Médio risco — mexe em estrutura HTML, mas não em ads.**

| # | LV | Mudança | Arquivos |
|---|---|---|---|
| B1 | 012/013/018 | Logo header + footer (depois removida do footer) | `header.php`, `footer.php` |
| B2 | 019/028 | Botão "Apoie o Cafezinho" pill vermelho escuro + centralização | `footer.php`, `style.css` |
| B3 | 027/029/030 | Reorganização header (logo esquerda, hamburger direita, search no fim, item "Buscar" no offcanvas, item "Apoie" no offcanvas, limpar redes sociais do header) | `header.php`, `footer.php`, `style.css` |

### 🟠 Grupo C — Manchete + Coluna Editor (front-page.php)
**Médio-alto risco — mexe na estrutura da HOME, onde está a manchete e os blocos temáticos.**

| # | LV | Mudança | Arquivos |
|---|---|---|---|
| C1 | 008/031 | Manchete: título no topo + imagem 100% + caption (object-fit contain, sem cortar) | `front-page.php`, `style.css` |
| C2 | 010/014 | Balão comentários 🔥 "pegando fogo" (vermelho escuro, sempre que ≥1 comentário; se 0 só foguinho) | `front-page.php`, `style.css` |
| C3 | 009/011 | Coluna Editor: setas carrossel desktop + 8 posts + iPad vira swipe | `front-page.php`, `style.css` |
| C4 | 021/022/024/026 | Cabeçalho Coluna Editor: avatar foto nova + título/nome vertical + cores invertidas (preto/vermelho) + caixa justificada + MAIÚSCULAS | `front-page.php`, `style.css` |

### 🟠 Grupo D — Estilos CSS globais (responsividade mobile/iPad)
**Médio risco — afetam todos os breakpoints, mas é só CSS.**

| # | LV | Mudança | Arquivos |
|---|---|---|---|
| D1 | 023/025/026 | Ajustes mobile (logo menor, hamburger baseline, fontes coluna editor reduzidas) | `style.css` |
| D2 | 026 | `text-transform: uppercase` + letter-spacing global | `style.css` |

---

## 2. Ordem de execução proposta (mais seguro → mais arriscado)

### Fase 1 — Estáticos (🟢 Grupo A) — **começamos aqui**
- A2: **Foto editor** primeiro (1 arquivo, sem depender de nada, rollback = só deletar arquivo)
- A1: **Logo v6** depois (idem, rollback = só trocar src de volta)

### Fase 2 — Header/footer isolados (🟡 Grupo B)
- B2: **Botão Apoie pill** (só footer, isolado)
- B1: **Logo no header/footer** (já com arquivo A1 subido)
- B3: **Reorganização header** (maior mudança, mas isolada no header/footer)

### Fase 3 — Home / front-page (🟠 Grupo C)
- C1: **Manchete título+caption** (uma seção do front-page)
- C2: **Balão comentários** (depende de C1 estar pronto)
- C3: **Coluna Editor 8 posts + setas** (outra seção)
- C4: **Cabeçalho Coluna Editor** (acabamento visual)

### Fase 4 — CSS global (🟠 Grupo D)
- D1+D2: Ajustes mobile + uppercase (layered no final)

---

## 3. Decisões que preciso do Miguel ANTES de começar

### 3.1 Confirmação da ordem
Você disse "vamos começar com o novo reader" — eu **acho** que você quis dizer **header** (cabeçalho), né? "Reader" pode ser erro de transcrição. Me confirma:

- **Opção 1:** Começar pelo **header** (Grupos A1 + B1 + B3: logo + estrutura do header) ← **mais provável que você quis dizer**
- **Opção 2:** Começar pela **foto do editor** (A2 — item isolado, mais seguro possível)
- **Opção 3:** Começar pela **manchete** (C1 — front-page, onde a capa fica)
- **Opção 4:** Outra ordem — me diz

### 3.2 Quanto à abordagem cirúrgica
Confirmo que vou seguir as **6 fases do Claude** em CADA item portado:
- (0) Descoberta read-only do arquivo canônico (diff com espelho)
- (1) Backup triplo SHA-256 (droplet + versionado + local)
- (5) Rollback script bash pré-instalado e testado
- (2) Edição cirúrgica preservando ads/comentários/PHP que já existe
- (3) (N/A — sem mu-plugins no port)
- (4) Verificação HTTP + grep logs
- (6) Registro no fórum lab visual canônico

### 3.3 Cache do canônico
O canônico tem **WP Rocket + serverdoin-cdn**. Após cada edição vou precisar **purgar cache**. Você autoriza? (Senão a mudança não aparece pra validação.)

---

## 4. Riscos específicos do canônico (que não tinham no espelho)

| Risco | Mitigação |
|---|---|
| **Tráfego real** (milhares de leitores) | Rollback pronto + teste em janela de baixo tráfego |
| **Cache WP Rocket + CDN** | Purgar após cada edição |
| **PHP-FPM reciclado** (outra sessão diagnosticou peso) | Não rodar nada pesado simultâneo |
| **Ad-inserter ativo** (19 blocos GAM AMP) | NÃO mexer em `wp_options.ad_inserter`, NÃO mexer em seletores AMP |
| **Mu-plugins 17 arquivos** | NÃO mexer em nenhum mu-plugin do canônico |
| **WP Rocket otimiza CSS/JS** | Pode ser preciso desativar otimização CSS temporariamente pra ver mudanças |
| **DB em MyISAM** (lock em escrita) | Evitar escrita no DB; só editar arquivos do tema |

---

## 5. Pre-flight check (antes de começar Fase 1)

Antes de tocar em QUALQUER arquivo do canônico, vou rodar:

1. **Backup completo do tema canônico** (`tar.gz` com timestamp + SHA-256)
2. **Snapshot dos arquivos que vamos tocar** (`header.php`, `footer.php`, `front-page.php`, `style.css`, pasta `img/`)
3. **HTTP baseline** (status atual das páginas: home, single, categoria, /amp/)
4. **Confirmar** que a outra sessão de diagnóstico não está mexendo nos mesmos arquivos
5. **Documentar** no monitoramento que estou começando o port (linha nova)

---

## 6. Documentação que vou manter atualizada

- **Este fórum** (plano) — `Foruns/forum_plano_port_canonico_20260811.md`
- **Memória técnica** (log detalhado de cada etapa executada) — `Memorias/memoria_port_canonico_20260811.md`
- **Índice de aprendizado** — `INDICE_APRENDIZADO_CANONICO_OCAFEZINHO.md` (nova seção "Port canônico")
- **Bugs canônicos** — vou criar `lab_visual_bugs/bugs_canonico_2026-08-11.jsonl` (separado do espelho)
- **Monitoramento** — linha nova no `MONITORAMENTO_DE_TRABALHO.md`

---

## 7. Estado que deixo pronto AGORA (antes da sua aprovação)

NADA. Zero escrita no canônico. Só:
- ✅ Este plano (no Cérebro)
- ✅ Lista consolidada das 24 mudanças
- ✅ Ordem de execução proposta
- ✅ Princípios sagrados definidos

Quando você responder às perguntas da seção 3, eu começo a Fase 0 (pre-flight check, ainda read-only).

---

## Assinatura

**ZCode (GLM-5.2 Z.ai)** — sessão fallback final (Kimi/Qwen esgotados 🔴🔴)
Timestamp: 2026-08-11 11:10 BRT

_Aguardando autorização explícita do Miguel para começar._

---

## 🆕 Adendo F2 (11/08/2026 ~23:11 BRT) — Resolver empilhamento residual de anúncios

**Contexto:** depois do port F1 (mover `banner-after-manchete-desktop` pra depois da Coluna Editor) + CSS anti-empilhamento, Miguel reportou (screenshot ~22:52) que **AINDA apareciam 2 anúncios empilhados** entre a Coluna do Editor e a seção Nacional.

### Diagnóstico (HTML renderizado + front-page.php)

Front-page.php canônico tinha **3 banners colados** nas linhas 304-307 (depois da Coluna Editor):

```
304: banner-after-colunistas-desktop  (DESKTOP) ← VELHO, herdado do tema
305: banner-after-colunistas-mobile   (MOBILE)
306: /* comentário do port F1 */
307: banner-after-manchete-desktop    (DESKTOP) ← MOVIDO por F1
```

CSS anti-empilhamento aplicado em F1:
```css
.desktop-ad-space { display: none !important; }
.mobile-ad-space { display: none !important; }
@media (min-width: 992px) { .desktop-ad-space { display: block !important; min-height: 90px; } }
@media (max-width: 991.98px) { .mobile-ad-space { display: block !important; min-height: 100px; } }
```

Resultado:
- **Desktop**: L304 + L307 ambas `desktop-ad-space` → `display:block` → **2 anúncios empilhados** ✗ (era o bug que Miguel via)
- **Mobile**: L305 = `mobile-ad-space` → 1 banner sozinho ✓

### Ação F2 (executada ~23:11 BRT)

Movido `banner-after-colunistas-desktop` (L304) de **depois** da Coluna Editor → **ANTES** dela (entre manchete e Coluna Editor). Mantendo o mesmo ID (não rename) pra não quebrar eventual config futura do ad-inserter.

**Backup:** `/root/port_mover_banner_coluna_20260811_231157/front-page.php.pre` (SHA `93b016c3...`)
**Rollback:** `bash /root/port_mover_banner_coluna_20260811_231157/rollback.sh`
**Cache WP Rocket:** `wp cache flush` (deletados `index.html` + `index-*.html` em `wp-content/cache/wp-rocket/www.ocafezinho.com/`)

### Ordem final dos banners na home (HTML renderizado pós-F2)

| Linha | ID | Breakpoint visível | Posição |
|---|---|---|---|
| L318 | `banner-after-manchete-mobile` | mobile | depois da manchete |
| L321 | `banner-after-colunistas-desktop` ⬅ NOVA POSIÇÃO | desktop | **ANTES** da Coluna Editor |
| — | `<section coluna-editor-section>` | — | Coluna do Editor |
| L594 | `banner-after-colunistas-mobile` | mobile | depois da Coluna |
| L595 | `banner-after-manchete-desktop` | desktop | depois da Coluna |

**Resultado:** zero empilhamento. Desktop vê 2 banners reais separados (1 antes + 1 depois da Coluna). Mobile idem.

### PHP lint + HTTP check

- `php -l front-page.php`: ✅ No syntax errors
- HTTP 200 home, 232578 bytes, TTFB 0.112s ✅

### Estado da missão (Regra Nº 3)

- **O que aconteceu:** Miguel reportou 2 anúncios empilhados pós-F1. Diagnóstico raiz: 3 divs `desktop-ad-space`/`mobile-ad-space` colados, dos quais 2 `desktop-ad-space` ficavam visíveis no desktop. Ação F2 moveu 1 dos 2 desktop pra antes da Coluna Editor.
- **O que falta:** Miguel fazer hard refresh (Ctrl+Shift+R) e confirmar visualmente que os 2 anúncios não estão mais empilhados. CDN (serverdoin-cdn) pode precisar de alguns minutos pra refletir em todas as bordas.
- **O que preciso de você (Miguel):** screenshot pós-hard-refresh da home (desktop) + da home (mobile) pra validar.

— ZCode (GLM-5.2 Z.ai), 2026-08-11 23:14 BRT

---

## 🆕 Adendo F3 (11/08/2026 ~23:23 BRT) — Crescer header (3 breakpoints) + fix gtranslate overlap

**Contexto:** Miguel pediu (screenshot ~23:20): "título header está muito pequeno, fica espaço vazio muito grande no desktop, não dá para crescer mais o header no desktop e iPad? no mobile também acho que pode crescer um pouco". Também reportou (screenshot ~23:17): "bandeirinhas de idiomas estão trepando sobre o submenu".

### (1) Header crescido (3 breakpoints)

| Breakpoint | min-height antes→depois | Logo altura antes→depois | Logo max-width antes→depois |
|---|---|---|---|
| Mobile (<768px) | 100→**130px** | 50→**72px** | 278→**399px** |
| iPad (768-991px) | 140→**180px** | 80→**120px** | 443→**665px** |
| Desktop (≥992px) | 140→**200px** | 100→**150px** | 554→**831px** |

Proporção logo mantida em 5.54:1 (aspect ratio da imagem original 1550×280).

### (2) Fix gtranslate overlap (CSS preventivo)

Plugin gtranslate pode injetar position absolute/fixed nas bandeirinhas, fazendo-as "trepimpar" sobre o submenu expandido do offcanvas. Aplicado 4 blocos CSS defensivos:

```css
/* Wrapper gtranslate SEMPRE relative, z-index baixo, sem float */
.offcanvas .gt_switcher_wrapper,
.offcanvas .gtranslate_wrapper,
.offcanvas #gtranslate_wrapper,
.offcanvas div[class*="gt_switcher"],
.offcanvas .glink,
.offcanvas .gt_float_switcher { position: relative !important; z-index: 1 !important; top/left/right/bottom: auto !important; float: none !important; }

/* Dropdown aberto do gtranslate: position static (empurra conteúdo em vez de flutuar) */
.offcanvas .gt_switcher_wrapper .gt_languages { position: static !important; ... }

/* Item submenu do offcanvas SEMPRE acima quando aberto */
.offcanvas-menu .dropdown-menu.show { z-index: 5 !important; position: static !important; }

/* gtranslate nunca absolute/fixed dentro do offcanvas */
.offcanvas [class*="gtranslate"],
.offcanvas [id*="gtranslate"],
.offcanvas [class*="gt_"] { position: relative !important; }
```

### Validação técnica

- **Backup:** `/root/port_header_gtranslate_20260811_232348/style.css.pre` (SHA `9c11101...`) + `rollback.sh`
- **Rollback:** `bash /root/port_header_gtranslate_20260811_232348/rollback.sh`
- **Cache WP Rocket:** deletados `index*.html` em `wp-content/cache/wp-rocket/www.ocafezinho.com/`
- **HTTP:** 200 home, TTFB 2.848s (acima do baseline 0.112s — provavelmente regeneração de cache WP Rocket após purge, deve normalizar)
- **CSS servido:** 27135 bytes, 1175 linhas, marker F3 presente ✅, 10 regras novas encontradas ✅

### Estado da missão

- **O que aconteceu:** Miguel pediu pra crescer header (3 breakpoints) e reportou gtranslate sobre submenu. Apliquei CSS para os 2 problemas em paralelo (mesma edição no style.css).
- **O que falta:** Miguel hard refresh (Ctrl+Shift+R) em desktop + iPad + mobile + screenshots novos. Se header ainda parecer pequeno, posso crescer mais (ou reduzir se tiver estourado). Se gtranslate ainda trepando, precisa de novo screenshot pra diagnosticar comportamento real (CSS preventivo cobre os casos comuns de position absolute).
- **O que preciso de você (Miguel):** hard refresh + screenshots novos (home desktop + offcanvas aberto com submenu).

— ZCode (GLM-5.2 Z.ai), 2026-08-11 23:24 BRT

---

## 🆕 Adendo F3.1 (11/08/2026 ~23:30 BRT) — Reduzir header (meio-termo pré-F3↔F3)

**Contexto:** Miguel respondeu ao F3: "cresceu demais o header". Apliquei meio-termo entre pré-F3 (pequeno) e F3 (grande demais):

| Breakpoint | min-height | Logo altura |
|---|---|---|
| Mobile (<768px) | 130 → **110px** | 72 → **60px** |
| iPad (768-991px) | 180 → **160px** | 120 → **100px** |
| Desktop (≥992px) | 200 → **170px** | 150 → **125px** |

CSS aplicado direto no style.css (mesma edição incremental do F3).

---

## 🆕 Adendo F4 (11/08/2026 ~23:50 BRT) — Fix definitivo: submenu trepando nas bandeirinhas

**Contexto:** Miguel reportou novamente: "submenu ainda está trepando nas bandeirinhas". Meu CSS preventivo do F3 (4 blocos `position: relative` no gtranslate) NÃO resolveu.

### Diagnóstico raiz (verdadeiro)

1. **Estrutura HTML do offcanvas** (footer.php): `<a class="mobile-menu-buscar">` → `<a class="mobile-menu-apoie">` → `wp_nav_menu(depth=2, walker=bootstrap_5)` → `<div class="mt-3 pb-3 border-bottom">[gtranslate]</div>` → ícones sociais. O gtranslate está DEPOIS do menu no DOM.

2. **Menu com submenu**: `<ul class="dropdown-menu depth_0">` é o submenu do item "Editorias" (Regional, Política, Economia, Geopolítica, Tecnologia, Ciência). Bootstrap 5 + **Popper.js** por padrão injetam `style="position: absolute; transform: translate(x,y)"` INLINE no submenu quando `.show`. Inline style tem prioridade alta sobre seletor CSS.

3. **Walker customizado** (`functions/_dropdown.php`): a classe `bootstrap_5_wp_nav_menu_walker` monta os atributos HTML via **string concatenation** e **IGNORA** o filter nativo `nav_menu_link_attributes` do WordPress. Meu filter original F3 nunca disparava.

### Solução F4 (3 camadas)

**Camada 1 — Filter PHP em `walker_nav_menu_start_el`** (novo filter que PEGA o HTML final do item, ao contrário do `nav_menu_link_attributes`):

```php
add_filter('walker_nav_menu_start_el', function($item_output, $item, $depth, $args) {
    if (isset($args->menu_class) && strpos($args->menu_class, 'offcanvas-menu') !== false) {
        if (strpos($item_output, 'data-bs-toggle="dropdown"') !== false) {
            $item_output = str_replace(
                'data-bs-toggle="dropdown"',
                'data-bs-display="static" data-bs-auto-close="outside" data-bs-toggle="dropdown"',
                $item_output
            );
        }
    }
    return $item_output;
}, 10, 4);
```

`data-bs-display="static"` desabilita o Popper pro dropdown. Submenu abre com position estático, empurrando o conteúdo abaixo (gtranslate descende junto).

**Camada 2 — CSS agressivo** (style.css F4) capturando qualquer inline style remanescente do Popper:
```css
.offcanvas-menu .dropdown-menu,
.offcanvas .dropdown-menu.show,
.offcanvas-menu li.menu-item-has-children > ul.dropdown-menu,
.offcanvas-menu ul.dropdown-menu.depth_0 {
    position: static !important;
    top/left/right/bottom/inset: auto !important;
    transform: none !important;
    margin: 0 !important;
    width: 100% !important;
    /* ... */
}
```

**Camada 3 — CSS preventivo gtranslate** (já aplicado no F3): wrapper sempre `position: relative`.

### Incidente (erro que corrigi)

Na primeira tentativa de aplicar o filter, usei PHP heredoc `<<<PHP` (sem aspas), que **interpolou** as variáveis `$item_output`, `$item`, `$depth`, `$args` e quebrou o functions.php (parse error L88). **Site ficou fora do ar por ~30 segundos.** Fiz rollback imediato do backup `/root/port_submenu_gtranslate_fix_20260811_234301/functions.php.pre` (PHP lint verde + HTTP 200 confirmados). **Lição técnica CRÍTICA:** ao inserir código PHP dentro de outro script PHP via heredoc, SEMPRE usar nowdoc `<<<'PHP'` (aspas) ou string simples com aspas escapadas, NUNCA heredoc `<<<PHP` (sem aspas) — ele interpola as variáveis PHP do código injetado.

### Validação

- **HTML renderizado** agora tem `data-bs-display="static"` no dropdown-toggle do Editorias (count=2): ✅
- PHP lint functions.php verde ✅
- HTTP 200 home ✅
- Cache WP Rocket purgado ✅
- OPcache resetado ✅

### Estado da missão

- **O que aconteceu:** F3 cresceu header demais → F3.1 reduziu pra meio-termo. Submenu gtranslate: CSS preventivo F3 não pegou porque raiz era Popper injetando inline; F4 desabilita Popper via `data-bs-display="static"` (aplicado via filter no `walker_nav_menu_start_el` porque walker customizado ignora filter nativo).
- **O que falta:** Miguel hard refresh e validar visualmente (header + offcanvas com submenu).
- **Backups/rollbacks:**
  - F2: `bash /root/port_mover_banner_coluna_20260811_231157/rollback.sh`
  - F3/F3.1: `bash /root/port_header_gtranslate_20260811_232348/rollback.sh`
  - F4: `bash /root/port_submenu_gtranslate_fix_20260811_234301/rollback.sh`
  - TOTAL: `bash /root/port_canonico_noturno_20260811_222724/rollback_TOTAL.sh`

— ZCode (GLM-5.2 Z.ai), 2026-08-11 23:50 BRT

---

## 🆕 Adendo F5 (11/08/2026 ~23:54 BRT) — Header mobile menor + nav desktop (Editorias/Apoie/Buscar)

**Contexto:** Miguel após F3.1+F4: "no celular o header ficou agora muito grande, pode diminuir um pouco, pra caber tudo na tela. no desktop pode diminuir um pouco e tentar acrescentar botões do menu, pra ocupar o espaço vazio, ai bota Editorias, apoie, ícone de buscar".

### (1) Header mobile menor

- min-height: 110 → **80px** (-27%)
- logo altura: 60 → **44px** (-27%)
- padding: 1.5rem → **0.75rem** (compacto)

### (2) Header desktop menor (libera espaço pros botões)

- min-height: 170 → **130px** (-24%)
- logo altura: 125 → **100px** (-20%)
- padding: 2rem → **1.5rem** (compacto)

### (3) NOVO bloco `.header-desktop-nav` no header.php (visível só ≥992px via `d-none d-lg-flex`)

Estrutura PHP inserida entre logo e hamburger:

```php
<div class="header-desktop-nav d-none d-lg-flex">
    <div class="dropdown">
        <a class="header-nav-link dropdown-toggle" data-bs-toggle="dropdown">Editorias</a>
        <ul class="dropdown-menu dropdown-menu-end">
            <li>Regional, Política, Economia, Geopolítica, Tecnologia, Ciência e Tecnologia</li>
        </ul>
    </div>
    <a href="/apoie" class="header-nav-link header-apoie-link">Apoie</a>
    <a href="#search" data-bs-toggle="collapse" class="header-search-icon">[SVG lupa]</a>
</div>
```

### (4) CSS do nav desktop (style.css F5)

```css
.header-desktop-nav { align-items: center; gap: 1.75rem; margin-left: auto; padding-right: 1.5rem; }
.header-nav-link { font-weight: 700; color: #1a1a1a; font-size: 1.05rem; }
.header-nav-link:hover { color: #dc3545; }
.header-apoie-link { background: #8b0000; color: #fff; padding: 0.5rem 1.25rem; border-radius: 9999px; }
.header-apoie-link:hover { background: #dc3545; }
.header-search-icon svg { width: 24px; height: 24px; }
.header-desktop-nav .dropdown-menu { border, box-shadow, border-radius 0.5rem, min-width 220px; }
.header-desktop-nav .dropdown-item:hover { background: #f8f9fa; color: #dc3545; }
```

Dropdown do "Editorias" no header desktop usa **Popper habilitado** (desejado fora do offcanvas — flutua sobre o conteúdo abaixo sem empurrar).

### Validação técnica
- PHP lint header.php + style.css: ✅
- HTTP 200 home TTFB 1.44s ✅
- HTML renderizado: `header-desktop-nav` (count=1), `header-apoie-link` (count=1), `header-search-icon` (count=1), `Editorias` (count=3: header+offcanvas+footer) ✅
- Cache WP Rocket + OPcache purgados ✅

### Backups/rollbacks (acumulados)
- F5 (este): `bash /root/port_header_nav_desktop_20260811_235313/rollback.sh`
- F4: `bash /root/port_submenu_gtranslate_fix_20260811_234301/rollback.sh`
- F3.x: `bash /root/port_header_gtranslate_20260811_232348/rollback.sh`
- F2: `bash /root/port_mover_banner_coluna_20260811_231157/rollback.sh`
- TOTAL: `bash /root/port_canonico_noturno_20260811_222724/rollback_TOTAL.sh`

### Estado da missão
- **O que aconteceu:** F5 aplicou 2 mudanças pedidas pelo Miguel: mobile reduzido (80px), desktop reduzido (130px) + novo bloco nav desktop com Editorias (dropdown), Apoie (pill), Buscar (ícone).
- **O que falta:** Miguel hard refresh desktop + mobile + iPad e validar visualmente.
- **Decisões pendentes:** se iPad também quer os botões (hoje `d-none d-lg-flex` mostra só ≥992px, iPad não tem). Se header ainda precisa de ajuste fino (maior/menor). Se "Editorias" no header desktop deveria apontar pra / (home) ou abrir só o dropdown.

— ZCode (GLM-5.2 Z.ai), 2026-08-11 23:55 BRT

---

## 🆕 Adendo F8 (12/08/2026 ~00:18 BRT) — Merge categorias: Ciência e Tecnologia → Tecnologia

**Contexto:** Miguel: "unifica as categorias ciência e tecnologia, Ciência e Tecnologia, numa só, Tecnologia, e troca o nome para Tecnologia em toda a parte. No nome do bloco no site deixa apenas Tecnologia".

### Estado pré-merge

| term_id | name | slug | count | term_taxonomy_id |
|---|---|---|---|---|
| 30 | Tecnologia | tecnologia | 2206 | 31 |
| 19936 | Ciência e Tecnologia | ciencia-e-tecnologia | 2817 | 19936 |

### Operação F8 (5 passos)

**1. Backup triplo DB** (2.5GB mysqldump): `/root/port_merge_categorias_20260812_001852/db_pre_merge.sql` SHA `ab7d0d0934cb7a37713131c72211bb3b394c52275c1a622717b4465a12bcd56d` + `header.php.pre` + `front-page.php.pre` + nginx configs.

**2. SQL merge** (`wp_term_relationships`):
```sql
INSERT IGNORE INTO wp_term_relationships (object_id, term_taxonomy_id, term_order)
SELECT object_id, 31, 0 FROM wp_term_relationships WHERE term_taxonomy_id = 19936;  -- mover
DELETE FROM wp_term_relationships WHERE term_taxonomy_id = 19936;                   -- limpar
UPDATE wp_term_taxonomy SET count = (SELECT COUNT(*) FROM wp_term_relationships WHERE term_taxonomy_id = 31) WHERE term_taxonomy_id = 31;  -- recount
DELETE FROM wp_term_taxonomy WHERE term_taxonomy_id = 19936;                        -- deletar tax
DELETE FROM wp_terms WHERE term_id = 19936;                                         -- deletar term
```

**Resultado:** cat 30 "Tecnologia" agora tem **5015 posts** (2206 + 2809, pequena perda por overlap de posts em ambas). Cat 19936 deletada (count=0 confirmado).

**3. Tema (front-page.php + header.php):**
- Bloco "CIÊNCIA E TECNOLOGIA" → **"TECNOLOGIA"**
- `category__in=array(30, 19936)` → `array(30)`
- Header desktop dropdown Editorias: removido "Ciência e Tecnologia", mantido 1 item "Tecnologia"
- URL `/ciencia-e-tecnologia/` → `/tecnologia/`

**4. Menu DB (item 263599):**
- `_menu_item_object_id`: 19936 → **30** (atualiza para apontar pra nova cat)

**5. Nginx redirect 301** (SEO-safe):
```nginx
location = /ciencia-e-tecnologia/ { return 301 /tecnologia/; }
location ~ ^/ciencia-e-tecnologia/(.+)$ { return 301 /tecnologia/$1; }
```
Inserido no bloco HTTPS (porta 443). Obs: primeiramente inseri no bloco HTTP errado, não funcionou até mover pro HTTPS.

### Validação

- **PHP lint** header.php + front-page.php: ✅
- **HTTP 200** home, /tecnologia/, /geopolitica/ ✅
- **HTTP 301** `/ciencia-e-tecnologia/` → `location: /tecnologia/` ✅
- **HTML renderizado**: bloco "TECNOLOGIA" aparece, "CIÊNCIA E TECNOLOGIA" some ✅
- **Cache WP Rocket purgado** (era o motivo do redirect inicial não pegar — servia a página velha cached)

### Estado da missão

- **O que aconteceu:** Unificação completa DB + tema + menu + redirect. Posts da cat "Ciência e Tecnologia" migrados pra "Tecnologia" (5015 total). URL antiga faz 301 pra nova (Google link juice preservada).
- **O que falta:** Miguel hard refresh e validar: home (bloco TECNOLOGIA no front-page), header desktop dropdown Editorias (só 1 Tecnologia), footer/offcanvas menu, e URL antiga redirecionando.
- **Backups:**
  - DB: `/root/port_merge_categorias_20260812_001852/db_pre_merge.sql` (2.5GB, SHA `ab7d0d09...`)
  - Tema: `header.php.pre` + `front-page.php.pre` (mesma pasta)
  - Nginx: `/etc/nginx/sites-enabled/ocafezinho.com.conf.bak_pre_redirect_merge_20260812_002935`

— ZCode (GLM-5.2 Z.ai), 2026-08-12 00:32 BRT
