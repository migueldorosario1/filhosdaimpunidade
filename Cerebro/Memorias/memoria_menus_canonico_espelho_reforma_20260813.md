# Memória técnica — Reforma dos Menus (hambúrguer + desktop) Canônico e Espelho

**Data:** 13/08/2026 ~12:20–13:10 BRT · **Executor:** ZCode (GLM-5.2, sessão ZCodeProject)
**Fórum irmão:** `Foruns/forum_menus_canonico_espelho_reforma_20260813.md`

## Inventário do estado ANTES (provas)

**Canônico (ocafezinho.com = cafezinho-wp 190.89.239.65:51439):**
- Menu WP `21062` ("Menu"): Quem somos? / Editorias → Política → Regional → (Ceará 263606, RJ 263607); Vídeos, Economia, Geopolítica, Tecnologia.
- `footer.php` offcanvas: `wp_nav_menu(['menu'=>'Menu','depth'=>3,'walker'=>bootstrap_5_wp_nav_menu_walker])`. Hierarquia antiga: Editorias(0)→Política(1)→Regional(2)→estados(3) → **estados cortados pelo depth=3** (WP conta 0,1,2).
- `header.php` desktop: dropdown hardcoded 1 nível (Regional, Política, Vídeos, Economia, Geopolítica, Tecnologia).
- HTML renderizado provado via curl (grep offcanvas-body): mostrava "Editorias > Política > Regional" sem estados.

**Espelho (cafezinho.news = 159.65.177.60):**
- **DOIS menus slug "Menu": 4967 (9 itens, legado/corrompido) e 21062 (10 itens, cópia do canônico).** `wp_get_nav_menu_object('Menu')` resolvia para o 4967 (menor term_id).
- Menu 4967: Política → Geopolítica, Eleições 2026, Regional → Ceará, RJ → **Economia (filha de RJ!)**; Tecnologia solto; **~15 itens órfãos sem título** (IDs 400000–400011, 262350...). Era o que o hambúrguer do espelho renderizava.
- `header.php` do espelho chamava `cafezinho_render_submenu_editorias()` — definida em `wp-content/mu-plugins/cafezinho-dropdown-editorias.php` (não existe no canônico).
- `footer.php` espelho: `depth=>4` (canônico: 3). style.css: quase idêntico.
- Espelho NÃO usa WP Rocket. Canônico usa (cache limpo via `wp eval 'rocket_clean_domain();'` SEM --skip-plugins — com skip a função não existe).

## Execução (ordem real)

**Backups:**
- Canônico `/root/backup_menus_20260813_1221/`: header_pre.php, footer_pre.php, style_pre.css, menu_21062_pre.csv.
- Espelho `/root/backup_menus_20260813_1536/`: idem + menu_4967_pre.csv.

**Canônico — menu 21062 (wp-cli como www-data, `--skip-themes --skip-plugins`):**
1. `menu item update 263596 --title="Nacional"` (só o label; categoria 22/politica-2 intacta).
2. `menu item update 263595 --parent-id=263602` (Regional: filho de Política → filho de Editorias).
3. `menu item add-term 21062 category <id> --parent-id=263595` ×10: Norte 21068, Nordeste 4984, Centro-Oeste 21069, Sudeste 21070, Sul 21071, SP 4988, Paraná 21082, RS 5004, MG 2549, Bahia 4994. (Ceará 263606 e RJ 263607 já eram filhos de Regional — mantidos.)
4. Eleições: `add-term ... 47 --parent-id=263602` → id 265517; `add-term ... 5088 --parent-id=265517` (Eleições 2026).
5. Novas verticais: `add-term ... --parent-id=263602` ×4: Cultura 79, Meio Ambiente 582, Esporte 1271, Saúde 258.
6. Reordenação DFS: `menu item update <id> --position=N` para 26 itens (1=Quem somos?, 2=Editorias, 3=Nacional, 4=Regional, 5-9 regiões, 10-11 Ceará/RJ, 12-16 SP/Paraná/RS/MG/Bahia, 17=Eleições, 18=Eleições 2026, 19=Economia, 20=Geopolítica, 21=Tecnologia, 22=Cultura, 23=Meio Ambiente, 24=Esporte, 25=Saúde, 26=Vídeos).

**Canônico — arquivos:**
- `header.php`: bloco `<div class="dropdown">` reescrito — Nacional, Regional (`.dropdown-submenu` + `<ul>` aninhado com 5 regiões + hr + 7 estados), Eleições (submenu: Eleições 2026), Economia, Geopolítica, Tecnologia, Cultura, Meio Ambiente (/meio-ambiente-2/), Esporte, Saúde, Vídeos. URLs limpas (testadas: `/categoria/X` = 301 → `/X` = 200). `php -l` OK antes do mv.
- `style.css` (append): `.header-desktop-nav .dropdown-submenu { position:relative }` + `> .dropdown-menu { top:0; right:100%; left:auto; margin-top:-1px }` (abre à ESQUERDA — dropdown é menu-end no canto direito) + `:hover/:focus-within > .dropdown-menu { display:block }` + override do `::after` (seta ▸: border-left solid, top/bottom transparent).
- Cache: `rocket_clean_domain()` + validação curl com cache-buster — desktop e offcanvas renderizam a estrutura nova completa. CSS servido com `?ver=<filemtime>` (bust automático).

**Espelho:**
1. `term update nav_menu 4967 --name="Menu Legado (nao usar)" --slug="menu-legado-nao-usar"` (⚠️ `wp menu update` NÃO existe — menus são terms de nav_menu).
2. `menu item update 263602 --url="https://cafezinho.news/"` (item custom Editorias apontava para ocafezinho.com — herança do espelhamento do banco).
3. `menu item delete 400018` (Ciência, filha de Tecnologia — só existia no espelho), `delete 265406` (Youtube), `delete 400019` (órfão sem título).
4. Mesma reestruturação do canônico (mesmos db_ids para itens originais; novos = 400020–400035). Todas as 24 categorias verificadas existirem no espelho ANTES (mesmos term_ids — banco espelhado).
5. Arquivos: header.php, footer.php, style.css copiados do canônico (`php -l` OK; chown www-data). footer depth=3 agora (suficiente: Editorias=0, editoria=1, região/estado=2).
6. Validação curl: offcanvas e desktop idênticos ao canônico. ✓

## Estrutura final (ambos)

```
Quem somos?
Editorias
├─ Nacional (/politica-2/)
├─ Regional (/regional/)
│  ├─ Norte, Nordeste, Centro-Oeste, Sudeste, Sul
│  └─ Ceará, Rio de Janeiro, São Paulo, Paraná, Rio Grande do Sul, Minas Gerais, Bahia
├─ Eleições (/eleicoes/)
│  └─ Eleições 2026 (/eleicoes-2026/)
├─ Economia, Geopolítica, Tecnologia
├─ Cultura, Meio Ambiente, Esporte, Saúde
└─ Vídeos
```

## Lições / armadilhas registradas

- `wp menu update` não existe → `wp term update nav_menu <id>`.
- Dois menus com mesmo slug: `wp_get_nav_menu_object` pega o de menor term_id (espelho puxava o legado corrompido). Ao espelhar banco, verificar duplicatas de slug em nav_menu.
- WP Rocket: `rocket_clean_domain()` só existe SEM `--skip-plugins`. HTML cacheado fez o desktop parecer "não deployado" no 1º curl (o offcanvas, do menu WP, veio novo — falso negativo clássico).
- IAB do ZCode não dispara `data-bs-toggle="dropdown"` do Bootstrap (clique segue href, página recarrega) — prova visual de dropdown/hover fica limitada; estrutura validar por curl.
- Categorias-chave: Meio Ambiente = 582 slug **meio-ambiente-2**; Eleições 2026 = 5088 (1112 posts, ciclo ativo); Nacional = categoria 22 (politica-2) com LABEL de menu "Nacional" (categoria não renomeada — URLs preservadas).

## Estado da missão

- **Feito:** menus canônico + espelho reestruturados, deployados e validados via HTML renderizado nos dois servidores.
- **Falta:** confirmação visual do Miguel no desktop (hover Editorias → Regional). Se o submenu não abrir no navegador dele, verificar computed style do `.dropdown-submenu` (CSS foi servido — `grep dropdown-submenu` = 6 ocorrências nos dois).
- **Preciso do Miguel:** OK visual. Depois: municípios via tags (fase futura).

## Adendo técnico — Sincronização canônico→espelho (header + front-page) — 13/08 ~14:25 BRT

**Executor:** ZCode (GLM-5.2). Ordem Miguel: sincronizar canônico→espelho **sem mexer no canônico**, transferindo header/menu/blocos (o que o sync normal de posts não traz).

**Método de diagnóstico (reproduzível):** checksum sha256 + `wc -c` de todos os arquivos `.php/.css/.js` do tema (`find . -maxdepth 2`) nos dois servidores via SSH BatchMode. Cruzamento pinpointou exatamente **quais** divergiam.

**Divergências encontradas (apenas 2 arquivos):**
| arquivo | canônico | espelho | sha canônico |
|---|---|---|---|
| `header.php` | 11981 B / 144 L | 8093 B / 105 L | `79afa974363e` |
| `front-page.php` | 53747 B / 803 L | 47496 B / 736 L | `ee293ad5581c` |
(style.css `e0c6a59f1988` 32104 B, footer.php `cec0aa53b8e9` 7145 B, functions.php `2ea9f8dcc0f2` 3953 B — **idênticos** nos dois; functions/, includes/, js/ idênticos.)

**Causa da defasagem:** o canônico foi alterado DEPOIS da reforma de 12:21 (que copiou header/footer/style do canônico→espelho). A sessão de Auditoria V4 (linha 15 do monitor, ~13:55–14:05) adicionou o bloco Regional no `front-page.php` e expandiu o dropdown do `header.php` para a árvore 27 estados — só no canônico.

**Comandos executados (espelho, servidor `root@159.65.177.60`, tema `/var/www/cafezinho-news/wp-content/themes/ocafezinho-portal`):**
```bash
# backup
BK=/root/backup_sync_canon_espelho_20260813_142104
mkdir -p $BK
cp -a header.php $BK/header_pre.php && cp -a front-page.php $BK/front-page_pre.php
# arquivos vieram do canônico via scp local (/tmp/canon_header.php, /tmp/canon_frontpage.php) — shas já conferidos
mv /tmp/canon_header.php header.php && mv /tmp/canon_frontpage.php front-page.php
chown www-data:www-data header.php front-page.php && chmod 644 header.php front-page.php
# php -l verde nos dois antes do mv
```

**Menu WP 21062 — comprovação de alinhamento:**
```bash
wp menu item list 21062 --fields=title,menu_item_parent,position --format=csv  # 46 itens em cada
# diff ordenado por (parent,position): sequência de TÍTULOS idêntica → renderiza igual
sort -t, -k2,2n -k3,3n menu_canon.txt  | cut -d, -f1 > canon_ord.txt
sort -t, -k2,2n -k3,3n menu_espelho.txt | cut -d, -f1 > espelho_ord.txt
diff espelho_ord.txt canon_ord.txt   # vazio = ordem de renderização idêntica
```
Note: campo válido é `menu_item_parent` (NÃO `parent_id`, que faz o comando falhar silenciosamente). Sem `--skip-themes` o WP-CLI ecoa o `_pagination.php` (short-tag `<?` mal-formada) — filtro com `grep -E '^[^,]+,[0-9]+,[0-9]+$'`.

**Armadilhas aprendidas:**
- O sync normal de posts (cron `:17`) **não** toca no tema nem no menu — esses ficam por conta de sincronização manual (este adendo).
- Espelho **sem cache** (nem plugin WP Rocket/Outro, nem fastcgi_cache nginx) — validação via curl `?nocache=` é definitiva. (Canônico usa WP Rocket, que requer `wp eval 'rocket_clean_domain();'` SEM `--skip-plugins`.)
- `wp menu item list --fields=parent_id` = vazio (campo inválido). Campo certo: `menu_item_parent`.
- Ordem absoluta de `position` pode divergir entre servidores sem afetar o renderizado — o que importa é a **ordem relativa por parent** (comprovar ordenando por parent+position e diffando títulos).

**Estado:** ✅ sincronizado e validado. Espelho = canônico em header/blocos/menu. Aguarda hard refresh do Miguel.
