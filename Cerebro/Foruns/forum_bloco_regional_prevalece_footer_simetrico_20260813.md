# Fórum — Regional prevalece no bloco da home + Footer simétrico ao header (13/08/2026)

**Sprint:** ZCode (GLM-5.2) — ordem do Miguel via chat, 13/08 ~16:20–17:00 BRT.
**Escopo:** `front-page.php` + `footer.php` + `style.css` do tema `ocafezinho-portal`, **canônico + espelho**.
**Post-gatilho:** 265618 ("Pesquisas Atlas e Datafolha agitam o final da semana no Ceará" — cats Política 22 + Regional 4986 + Nordeste 4984 + Ceará 4968).

## Decisão 1 — REGRA EDITORIAL: categoria regional PREVALECE

> Miguel: *"se tiver regional, vai pro bloco regional, e nao pro nacional"* (post vai pro bloco Regional, que fica **depois** do Nacional na home).

- **Problema:** o bloco Nacional (`category__in=[22]`) "engolia" posts regionais (agentes V4 regionais marcam Política 22 **e** Regional/região/estado) e ainda os empurrava pro `$excludes` — o post **sumia do bloco Regional**. Prova: 265618 aparecia 2× no Nacional e 0× no Regional.
- **Fix:** as 2 queries do bloco Nacional agora excluem **todas as cats regionais** (4986 + 5 regiões + 27 estados + DF = 34 IDs) via `$nacional_not_in` (merge com os excludes existentes 28/20751/20699). Post regional flui pro bloco Regional sozinho.
- **Ordem dos blocos:** inalterada (Nacional primeiro; Regional depois — já estava correta; a 1ª leitura do Miguel era sobre O POST, não o bloco).
- **Lista canônica dos 34 IDs** (fonte: árvore do menu 21062, fonte da verdade da taxonomia): `4986, 21068, 4984, 21069, 21070, 21071` (regional+regiões) + `21072–21090, 21139` + legados `1656 (RJ), 2549 (MG), 4968 (CE), 4988 (SP), 4994 (BA), 5004 (RS), 5101 (PB)`.
- **Não mexido (escopo mínimo):** manchete, Coluna do Editor, blocos Geopolítica/Tecnologia/etc. e a query do bloco Regional.

## Decisão 2 — FOOTER SIMÉTRICO AO HEADER

> Miguel: *"aproveita e ajeita o menu do footer. deixa ele simétrico, dentro do possível, com o menu do header."*

- **Antes:** `wp_nav_menu('Menu', depth=1)` numa coluna — renderizava só "Quem somos? / Editorias / Regional" (3 itens soltos).
- **Depois:** 2 colunas estáticas hardcoded (mesmo padrão do header): **Editorias** (Nacional, Eleições, Economia, Geopolítica, Tecnologia, Cultura, Meio Ambiente, Esporte, Saúde, Vídeos — em 2 colunas internas via `two-columns`) + **Regional** (Norte, Nordeste, Centro-Oeste, Sudeste, Sul). Mesmos slugs do dropdown do header (`/politica-2/`, `/meio-ambiente-2/`, etc.).
- **Regrade do rodapé para 12 cols:** logo 1 + texto 3 + social 2 + Editorias 2 + Regional 2 + Apoie 2 (antes somava 13 → Apoie quebrava de linha). Botão Apoie (`nowrap`) ganhou media query md–lg encolhendo fonte/padding.
- **"Quem somos?"** continua de fora das colunas (o texto do footer já tem o link "Sobre nós").
- Mobile: colunas `d-none d-md-block` (hambúrguer/offcanvas continua sendo o menu do mobile).

## Estado (o que aconteceu / o que falta / o que preciso do Miguel)

- ✅ Canônico `ocafezinho.com` no ar: 265618 **2× no Regional, 0× no Nacional** (validado curl c/ `?nocache=`); footer novo renderizado; `php -l` verde; cache WP Rocket purgado (página+min+busting).
- ✅ Espelho `cafezinho.news` no ar: mesmos 3 arquivos (md5 pré-mudança batia 3/3 com o canônico → aplicação limpa); footer validado; sem cache no espelho.
- ⚠️ **Miguel homologar visualmente** (hard refresh): footer simétrico no desktop + post regional fora do Nacional.
- 📋 Pendência futura (não executado, escopo mínimo): se surgir post com **só o estado** (sem região/4986), ele hoje não entra em bloco nenhum — se acontecer, adicionar os 27+DF ao `category__in` do bloco Regional.

## Backups / rollback

- Canônico: `/root/backup_nacional_prevalece_footer_20260813_20260813_175955/` (front-page.php, footer.php, style.css).
- Espelho: `/root/backup_nacional_prevalece_footer_espelho_20260813_210222/` (idem).
- Rollback = copiar os 3 de volta pro tema e purgar cache (canônico).

## ✅ ADENDO ~18:15 — 2ª RODADA (ordem Miguel): footer HIERÁRQUICO

> Miguel: *"deixa apenas 3 links do menu no footer, Quem Somos, Editorias e Regional. O resto é submenu."*

- **Mudança:** as 2 colunas hardcoded (Editorias + Regional) deram lugar a **UMA coluna** com `wp_nav_menu('Menu', depth=2)` → renderiza exatamente **Quem somos? · Editorias▸(10 editorias) · Regional▸(5 regiões)**, subitens indentados (CSS `footer ul.footer-tree`). **Vantagem:** footer agora vem do menu WP 21062 (fonte da verdade) — editar o menu atualiza o footer sozinho. Grid: 1+3+2+3+3=12 (texto 3, menu 3, Apoie volta a 3).
- **CSS:** bloco `footer-menu-title` substituído por `footer-tree` (topo bold .8rem, sub-menu .75rem cinza indentado, break-inside avoid); media query do botão Apoie removida (voltou pra col-md-3).
- **Fix colateral:** item custom "Editorias" (db_id 263602) tinha URL absoluta do canônico — no espelho o link do footer/hambúrguer levava pra `www.ocafezinho.com`. Trocado por **link relativo `/`** nos 2 menus (resolve no host atual; à prova de sync).
- **⚠️ Incidente (auto-infligido, ~90s):** comentário PHP de rollback continha `..._20260813_*/` → o `*/` fechou o comentário no meio → `footer.php` com parse error no ar (cp rodou antes do lint; set -e abortou depois). Recuperado em seguida; lição gravada: **nunca `*/` dentro de comentário de bloco PHP; lint ANTES do cp**.
- **Prova (curl, 2 servidores):** footer-tree com Quem somos? + sub-menus ✓; `href="/"` no Editorias ✓; 265618 segue 2× Regional / 0× Nacional ✓.
- **Backups 2ª rodada:** `/root/backup_footer_hierarquico_20260813_20260813_181218/` (canônico) + `/root/backup_footer_hierarquico_20260813_20260813_181324/` (espelho).

**Memória técnica:** `Memorias/memoria_bloco_regional_prevalece_footer_simetrico_20260813.md` (com adendos das rodadas 2 e 3).

## ✅ ADENDO ~18:31 — 3ª RODADA (ordem Miguel, c/ screenshot): submenu só no HOVER + fim da faixa cinza

> Miguel: *"os submenus não eram para ficar visíveis. e agora tem uma faixa cinza embaixo que está feio"* (screenshot 18:27).

- **Submenus ocultos:** `footer-tree` virou **flex horizontal** (3 topos lado a lado); `.sub-menu` agora `display:none` e abre **só no hover/focus-within**, **pra cima** (`bottom: calc(100%+10px)`, card branco com borda/shadow/z-index 1050) — padrão dropdown de footer. Tirado o `two-columns`.
- **Faixa cinza:** causa = regra antiga `#banner-video-sticky-desktop { background:#ccc }` + F1 `.desktop-ad-space { min-height:90px }` — slot de anúncio sticky de vídeo **vazio** pintando 90px de #ccc no fim da página (existe desde o port 11/08). Fix: override no fim do style.css (`background:none; min-height:0 !important`) — mantém o hook caso o anúncio volte.
- **Deploy:** protocolo pós-incidente (lint no /tmp ANTES do cp) nos 2 servidores; provas: HTML c/ `class="footer-tree"` ✓, CSS servido c/ hover+focus-within ✓ e regra nova após a antiga (cascade vence) ✓. Backups: `/root/backup_footer_hover_20260813_20260813_183030/` (canônico) + `_183042/` (espelho).
- **Pendência:** homologação visual do hover no desktop (IAB não dispara hover — precisa olho humano).
