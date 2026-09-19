# Memória — Regional prevalece na home + Footer simétrico (13/08/2026, ZCode GLM-5.2)

Log técnico completo do sprint. Fórum de decisões: `Foruns/forum_bloco_regional_prevalece_footer_simetrico_20260813.md`.

## Contexto

- Miguel reportou pelo post **265618** (`controle.ocafezinho.com/wp-admin/post.php?post=265618&action=edit`): post com cats Política(22)+Regional(4986)+Nordeste(4984)+Ceará(4968) aparecia no bloco **Nacional** da home.
- 1ª mensagem sugeria mexer ordem de blocos; correção do Miguel: a regra é sobre **o POST** — *"se tiver regional, vai pro bloco regional, e nao pro nacional"* — + tarefa extra: footer simétrico ao header.

## Diagnóstico (provas)

- `wp post term list 265618 category` → 4968 Ceará, 4984 Nordeste, 22 Política, 4986 Regional (todas parent=0; hierarquia região▸estado existe SÓ no menu, não na taxonomia).
- Post `publish` ("Pesquisas Atlas e Datafolha agitam o final da semana no Ceará").
- HTML home (curl `?nocache=`): 265618 **2× no bloco Nacional, 0× no Regional**. Mecânica do bug: Nacional pegava o post (cat 22, mais recente) → `array_push($excludes)` → bloco Regional (`post__not_in=$excludes`) o pulava. Ou seja, o regional não só poluía o Nacional como **sumia do Regional**.
- Ordem dos blocos na home (já correta, não mexida): Nacional → Geopolítica → Tecnologia → Economia → Vídeos → Cultura → Meio Ambiente → Saúde → Esporte → **Regional** → Linha do Tempo → 10 mais vistos → Recentes.
- Menu footer antigo: `wp_nav_menu('Menu', depth=1)` → resolvia o menu 21062 mas só topo (Quem somos?/Editorias/Regional). Grid do footer somava 13 cols (Apoie quebrava linha).
- Confere `term_id == term_taxonomy_id` nas cats antigas (22/1656/4968/4986) → `category__not_in` por term_id seguro.

## Mudanças (3 arquivos do tema `ocafezinho-portal`)

### 1. `front-page.php` (canônico + espelho, idênticos)

Bloco Nacional (2 queries: destaque `posts_per_page=1` + laterais `=4`), era:
```php
'category__not_in' => array(28, 20751, 20699), 'category__in' => array(22),
```
agora (var definida no cabeçalho do bloco):
```php
$regional_cats = array(4986, 21068, 4984, 21069, 21070, 21071, 21072, 21073, 21074, 21075, 21076, 21077, 21078, 21079, 21080, 21081, 21082, 21083, 21084, 21085, 21086, 21087, 21088, 21089, 21090, 21139, 1656, 2549, 4968, 4988, 4994, 5004, 5101);
$nacional_not_in = array_merge( array(28, 20751, 20699), $regional_cats );
// queries: 'category__not_in' => $nacional_not_in, 'category__in' => array(22),
```
34 IDs = Regional 4986 + 5 regiões + 27 unidades (21072–21090 contíguos = AC,AL,AP,AM,ES,GO,MA,MT,MS,PA,PB,PE,PI,RN,RO,RR,SC,SE,SP?,TO — atenção: 21082=PR, 21083=PE... lista exata extraída da árvore do menu 21062) + legados 1656 RJ, 2549 MG, 4968 CE, 4988 SP, 4994 BA, 5004 RS, 5101 PB + DF 21139.

### 2. `footer.php` (canônico + espelho, idênticos)

- Coluna do `wp_nav_menu` (col-md-3, d-none d-md-flex) → **2 colunas** (col-md-2 cada, d-none d-md-block): **Editorias** (`ul.two-columns.footer-menu-cols`, 10 links, slugs do header) + **Regional** (5 regiões).
- Regrade: texto col-md-4→**3**; Apoie col-md-3→**2** (total 12; antes 13).
- Links idênticos ao dropdown do header: `/politica-2/ /eleicoes/ /economia/ /geopolitica/ /tecnologia/ /cultura/ /meio-ambiente-2/ /esporte/ /saude/ /videos/` + `/norte/ /nordeste/ /centro-oeste/ /sudeste/ /sul/`.

### 3. `style.css` (append no fim, canônico + espelho)

`footer .footer-menu-title` (uppercase, vermelho `--red`, .75rem) + `footer .footer-menu-cols li` (break-inside avoid) + media query md–lg encolhendo `.btn-apoie-footer` (nowrap).

## Deploy e validação

| Passo | Canônico `ocafezinho.com` | Espelho `cafezinho.news` |
|---|---|---|
| Backup | `/root/backup_nacional_prevalece_footer_20260813_20260813_175955/` | `/root/backup_nacional_prevalece_footer_espelho_20260813_210222/` |
| Pré-check | — | md5 dos 3 = backup pré-mudança canônico (3/3 ✓) |
| Install | scp→cp→chown www-data + `cat >>` CSS | idem |
| Lint | `php -l` verde ×2 | `php -l` verde ×2 |
| Cache | Rocket purge manual (`wp rocket purge` NÃO existe neste WP: limpo `wp-rocket/{www,controle}/*` + `min/*` + `busting/*`) | nenhum (espelho sem cache) |
| Prova curl | 265618: **2× Regional, 0× Nacional**; footer Editorias+Regional ✓; menu antigo sumiu | footer ✓ (todas as probes); blocos na ordem |

## Gotchas aprendidos

1. `wp rocket purge` não é comando registrado neste WP — purge confiável = limpar dirs de cache como www-data/root (`wp-rocket/<host>/*`, `min/*`, `busting/*`).
2. Pipe `wp ... | tail` mascara exit-code → fallback `||` não dispara (usar `set -o pipefail` ou checar saída).
3. Bug clássico de "post some de bloco": `$excludes` é compartilhado entre blocos em ordem — bloco ganancioso upstream mata bloco downstream (mesma mecânica de outros bugs de home já vistos).
4. `curl ocafezinho.com` → 301 nginx; usar `www.ocafezinho.com`.
5. Espelho e canônico estavam 100% alinhados no tema (sync 14:25 de hoje) → qualquer diff futuro entre os dois é sinal de sessão que mexeu só num lado.

## Pendências

- Miguel homologar (hard refresh): footer hierárquico desktop + 265618 fora do Nacional.
- Futuro: post com SÓ estado (sem região/4986) não entra em bloco nenhum → se aparecer, adicionar 27+DF ao `category__in` do bloco Regional.

## ADENDO 2ª RODADA (~18:15, ordem Miguel "apenas 3 links, o resto é submenu")

- `footer.php`: 2 colunas hardcoded → 1 coluna `wp_nav_menu('Menu', depth=2, menu_class='two-columns footer-tree')` = **Quem somos? · Editorias▸10 · Regional▸5**; grid 1+3+2+3+3=12; Apoie volta col-md-3.
- `style.css`: bloco `footer-menu-title`/media-query → `footer ul.footer-tree` (topo bold, `.sub-menu` .75rem var(--gray) indent .8rem, `> li { break-inside: avoid }`).
- Menu WP (2 servidores): item custom Editorias db_id 263602 `--link=/` (era absoluto do canônico; quebrou o espelho) — `wp menu item update 263602 --link=/`.
- **Incidente ~90s:** comentário `Rollback: ..._20260813_*/` fechou o comentário PHP (`*/`) → parse error no footer.php em produção (cp antes do lint). Recuperação: fix local + scp + `php -l` + purge. **Lições: (1) NUNCA `*/` em caminho dentro de comentário `/* */`; (2) SEMPRE `php -l` no /tmp ANTES do `cp` pro tema; (3) pipe `| tail` mascara exit code.**
- Provas: canônico `href="/"` ✓ 2×Regional ✓; espelho footer-tree ✓ `href="/"` ✓ (regex de validação precisa tolerar atributos extras tipo `aria-current`).
- Backups: `/root/backup_footer_hierarquico_20260813_20260813_181218/` (canônico) + `_20260813_181324/` (espelho).

## ADENDO 3ª RODADA (~18:31, ordem Miguel c/ screenshot: "submenus não eram pra ficar visíveis" + "faixa cinza embaixo feia")

- `footer.php`: `menu_class` `'two-columns footer-tree'` → `'footer-tree'`.
- `style.css`: bloco `footer-tree` reescrito — **flex horizontal** de 3 topos; `.sub-menu { display:none; position:absolute; bottom:calc(100%+10px); card branco }` abre só em `:hover`/`:focus-within`; li:hover sub a → vermelho.
- **Faixa cinza raiz:** `#banner-video-sticky-desktop { background:#ccc }` (regra antiga ~L703) + F1 `.desktop-ad-space` (≥992px `min-height:90px`) = slot de anúncio sticky VAZIO pintando 90px #ccc no fim do footer (desde o port 11/08). Fix: bloco novo no fim (`background:none; min-height:0 !important`) — mesma especificidade, última vence; hook do anúncio preservado.
- Deploy c/ protocolo novo: `php -l` no `/tmp` ANTES do `cp` (2 servidores ✓). Provas: HTML `class="footer-tree"` ✓; CSS servido: 2× `focus-within` ✓; regra nova DEPOIS da antiga ✓.
- Backups: `/root/backup_footer_hover_20260813_20260813_183030/` (canônico) + `_20260813_183042/` (espelho).
