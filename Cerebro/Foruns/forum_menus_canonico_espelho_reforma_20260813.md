# Fórum — Reforma dos Menus (hambúrguer + desktop) Canônico e Espelho

**Data:** 13/08/2026 ~12:20–13:10 BRT · **Executor:** ZCode (GLM-5.2) · **Ordem:** Miguel (voz, 13/08 manhã)
**Memória técnica irmã:** `Memorias/memoria_menus_canonico_espelho_reforma_20260813.md`

## A ordem do Miguel

"O menu hambúrguer em todos os formatos tá errado. O menu visível do desktop também tá faltando o submenu de Regional — tem que ter regiões e estados (municípios depois, com tags). Não tem nem o Nacional — o Política podia trocar o nome pra Nacional. Tem que ter Eleições. Tem que consertar esses menus."

## Diagnóstico (as 3 raízes)

1. **Menu WP 21062 (canônico) com hierarquia errada:** Regional era filho de Política; estados (Ceará, RJ) no nível 4 eram cortados pelo `depth=3` do `wp_nav_menu` — nunca apareciam.
2. **Desktop = dropdown HARDCODED de 1 nível** no `header.php` (6 links flat, sem Nacional, sem Eleições, sem submenu).
3. **ESPELHO pior:** dois menus com slug "Menu" (4967 legado/corrompido + 21062). O hambúrguer resolvia para o **4967** — estrutura bizarra (Economia filha de Rio de Janeiro!) + ~15 itens órfãos sem título. Era isso que o Miguel via de errado "em todos os formatos".

## O que foi feito (decisões)

- **Estrutura final (os DOIS servidores, idêntica):** Quem somos? · Editorias → **Nacional** (label novo sobre a categoria politica-2 — categoria NÃO renomeada, URLs intactas) · **Regional** → 5 regiões (Norte, Nordeste, Centro-Oeste, Sudeste, Sul) + 7 estados (Ceará, RJ, SP, Paraná, RS, MG, Bahia — os com tradição de pauta) · **Eleições** → Eleições 2026 · Economia · Geopolítica · Tecnologia · **Cultura · Meio Ambiente · Esporte · Saúde** (4 novas verticais V4 entram no menu) · Vídeos.
- **Hambúrguer:** corrigido pela reestruturação do menu WP (via wp-cli). `depth=3` comporta os 3 níveis novos (Editorias=0, editoria=1, região/estado=2).
- **Desktop:** dropdown reescrito com submenu multinível (`.dropdown-submenu` em CSS puro, hover/focus; Bootstrap 5.2 não tem nativo). Submenu abre **à esquerda** (o dropdown é menu-end no canto direito — abrir à direita sairia da tela). Seta ▸ nos itens com submenu.
- **Espelho:** menu 4967 renomeado para "Menu Legado (nao usar)" (slug `menu-legado-nao-usar`) — mata a ambiguidade; menu 21062 reestruturado igual ao canônico; itens extras Ciência/Youtube e 1 órfão removidos; URL do item custom "Editorias" corrigida (apontava para ocafezinho.com → agora cafezinho.news); header.php/footer.php/style.css copiados do canônico (eram quase idênticos — diff era o dropdown + depth).
- **URLs:** usadas as limpas (`/regional/`, `/norte/`...) — `/categoria/X` existe mas é 301.
- **Municípios:** ficam para depois, via **tags** (combinado anterior).

## Estado: o que está pronto / o que falta / o que preciso do Miguel

- ✅ Canônico: menu 21062 reestruturado + header.php + style.css no ar, validado via HTML renderizado (hambúrguer e desktop) após limpar cache WP Rocket.
- ✅ Espelho: idem, validado via HTML renderizado. Backups nos dois servidores (`/root/backup_menus_20260813_1221` canônico, `/root/backup_menus_20260813_1536` espelho).
- ⚠️ **Prova visual do hover ficou limitada:** o navegador embutido do ZCode (IAB) não dispara o toggle do Bootstrap (o clique segue o href e recarrega). Estrutura+CSS validadas; o padrão do dropdown é o mesmo de antes (não foi alterado o mecanismo, só o conteúdo). **Preciso do Miguel:** passar o mouse em Editorias → Regional no desktop e confirmar o submenu abrindo (1 segundo de teste).
- 📋 Pendente conhecido (não desta missão): municípios via tags; `cafezinho_render_submenu_editorias` (mu-plugin do espelho) ficou órfã — inofensiva, candidata a remoção na próxima faxina.

## Rollback

Canônico: `cp /root/backup_menus_20260813_1221/{header_pre.php→header.php, style_pre.css→style.css}` + reimportar `menu_21062_pre.csv` se necessário. Espelho: idem em `/root/backup_menus_20260813_1536/`.

---

## Adendo — Sincronização canônico→espelho (header + front-page) — 13/08 ~14:25 BRT

**Executor:** ZCode (GLM-5.2, fallback final) · **Ordem:** Miguel (chat direto) — "faz a sincronia do canonico com o espelho, sem mexer no canonico, transferindo header, menu, blocos, o que não vem no sync normal, pro espelho cafezinho.news".

**Por que:** o sync normal (cron `:17`/h, delta `post_modified`) copia só **posts** canônico→espelho — **NÃO** copia tema nem menu. O canônico evoluiu depois da reforma de 12:21 (sessão de Auditoria V4 às ~13:55–14:05 adicionou bloco Regional no `front-page.php` + árvore 27 estados no `header.php`); o espelho ficou defasado.

**Diagnóstico (checksums sha256+tamanho de TODOS os arquivos do tema):** só **2 arquivos** divergiam — `header.php` (canônico 11981 B/144 L vs espelho 8093 B/105 L) e `front-page.php` (canônico 53747 B/803 L vs espelho 47496 B/736 L). Todo o resto idêntico: `style.css`, `footer.php`, `functions.php`, `functions/*`, `includes/*`, `js/*`, `single.php`, `page.php`, `404.php`, `comments.php`, `ad/*`.

**O que o canônico tinha a mais:**
- `header.php`: dropdown desktop de Regional em **árvore completa** (5 regiões como `dropdown-submenu`, cada uma abrindo seus estados — **27 estados + DF**). Espelho tinha só 5 regiões + 7 estados flat.
- `front-page.php`: bloco **Regional** (cat 4986 + 5 regiões, "adicionado 13/08/2026"); blocos **Nacional** (22) e **Economia** (43) **separados** (no espelho eram `array(22,43)` juntos); `category__not_in` p/ excluir vídeos (28, 20751, 20699); blocos Meio Ambiente (582)/Saúde (258)/Esporte (1271)/Cultura (79).
- **Sem dependência perigosa:** única ref. a lazyload é a classe `no_lazyload` na manchete (desativa); sem `data-src`/Smush/WP-Rocket hardcoded. Copiar é seguro.

**Pré-checks (tudo OK):** 28 categorias de estado (27 estados + DF) existem no espelho (banco espelhado, **0 faltando**); imgs do tema (`icon-start.svg`, `foto-miguel-editor-v2.jpg`) presentes; categorias de posts mesmos IDs nos dois.

**Execução (ZERO escrita no canônico):**
1. Backup espelho: `/root/backup_sync_canon_espelho_20260813_142104/` (`header_pre.php` + `front-page_pre.php`).
2. `scp` header.php + front-page.php do canônico → /tmp do espelho (sha confirmado: header `79afa974363e`, front `ee293ad5581c`).
3. `php -l` verde nos dois → `mv` → `chown www-data:www-data` → `chmod 644`.
4. Espelho **sem plugin de cache** e **sem `fastcgi_cache`** nginx → nada a purgar.

**Validação (curl home visitante real, `?nocache=`):** HTTP 200 (276 KB); bloco **Regional** presente; **11 `dropdown-submenu`** no header; estados antes ausentes agora linkados (`/acre/ /amapa/ /amazonas/ /roraima/ /tocantins/ /alagoas/ /piaui/ /sergipe/`); todos os 9 separadores de bloco (Nacional, Geopolítica, Tecnologia, Economia, Vídeos, Cultura, Meio Ambiente, Saúde, Esporte) presentes.

**Menu WP 21062:** verificado **alinhado** — 46 itens idênticos, mesmos `menu_item_parent` (hierarquia idêntica) e **ordem de renderização idêntica** (ordenando por parent+position, a sequência de títulos bate nos dois). Os números de `position` absolutos divergem, mas como a ordem relativa é a mesma o menu **renderiza igual**. Nenhum toque necessário.

**Estado:** ✅ sincronização concluída e validada. Espelho agora reflete o canônico em header, blocos e menu. **Falta:** confirmação visual do Miguel (hard refresh desktop + mobile).

**Rollback (deste adendo):** `cp /root/backup_sync_canon_espelho_20260813_142104/{header_pre.php→header.php, front-page_pre.php→front-page.php}` no espelho.
