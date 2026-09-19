# Fórum — Menu hambúrguer = header + Regional▸Regiões▸Estados (PLANO, 12/08/2026)

**Data:** 2026-08-12 ~18:10 · **Autor:** ZCode/GLM-5.2 (Kimi/Qwen 🔴🔴, fallback final) · **Status:** 📋 **PLANO (não executado)** — ordem Miguel: *"isso é sprint grande demais para agora. apenas anote, faça forum, e crie um plano de trabalho."*
**Plano de trabalho pareado:** `Foruns/plano_trabalho_menu_hamburguer_regional_estados_20260812.md`

---

## 0b. ATUALIZAÇÃO (12/08 ~22:40) — ESPELHO RESOLVIDO (submenus regionais visíveis desktop + mobile)

Ordem Miguel: *"vamos trabalhar primeiro no espelho. não está aparecendo os submenus regionais... nem no desktop, nem no hamburguer"*. **Resolvido no espelho (`cafezinho.news`):**
1. **`footer.php:67` `depth` 2→4** no offcanvas → hambúrguer mostra **Editorias▸Política▸Regional▸(Ceará, RJ)** (raiz do problema: depth=2 cortava o nível 3+).
2. **mu-plugin `cafezinho-dropdown-editorias.php`** (novo): função recursiva `cafezinho_render_submenu_editorias()` renderiza filhos de "Editorias" do menu 21062 com submenus aninhados (`dropdown-submenu` BS5 + CSS no `wp_head`).
3. **`header.php`:** `<ul>` estático (5 itens flat) substituído por `<?php cafezinho_render_submenu_editorias(); ?>` → dropdown desktop **dinâmico** com a árvore completa.
- **Validação:** PHP lint verde; HTTP 200; HTML confirma dropdown-submenu(6×), Política/Regional como toggle, Ceará/RJ no submenu. Backup `/root/backup_submenus_espelho_20260813_013624/`.
- **Pendência:** replicar no **canônico** (depth + mu-plugin + header) após Miguel homologar o espelho.

## 0. ATUALIZAÇÃO (12/08 ~18:11) — 1ª parte EXECUTADA

✅ **Regional movida para submenu de Política** (ordem Miguel *"bota Regional sob Política"*), executada isoladamente (antes do sprint completo):
- Menu 21062: Regional (263595) `parent` 263602 (Editorias) → **263596 (Política)**; `menu_order` 61 (Ceará 62, RJ 63).
- Offcanvas mobile: `depth` **2→3** (footer.php:67) — Regional (nível 3) agora visível no hambúrguer; Ceará/RJ (nível 4) só com depth 4 (resto do sprint).
- Header desktop **estático** não reflete (pendente Fase 4). Backup `/root/backup_menu_regional_politica_20260812_180910/`.
- **Restante do sprint NÃO executado:** regiões▸estados, header dinâmico, depth 4, AMP — aguardam autorização.

## 1. Contexto (ordem Miguel)

> *"No menu do hamburguer, tem que ter as mesmas categorias que no menu visível no canonico, no header. E tem que ter regional como submenu de política, e as 4 regiões do país como submenu, os 27 estados mais DF como submenus respectivos de cada região. Mas isso é sprint grande demais para agora. Apenas anote, faça forum, e crie um plano de trabalho."*

## 2. Diagnóstico (investigado, read-only, 12/08 ~18:05)

### 2.1 Header desktop × Hambúrguer — a discrepância
| Elemento | Origem | Conteúdo |
|---|---|---|
| **Dropdown "Editorias" do header DESKTOP** | **HTML estático** em `header.php` (linhas 30‑35, port visual F5) | Regional, Política, Economia, Geopolítica, Tecnologia — **SEM Vídeos, SEM Youtube** |
| **Hambúrguer / offcanvas MOBILE** | **`wp_nav_menu('menu'=>'Menu')` dinâmico** em `footer.php:65` (menu 21062) | Tudo do menu 21062 (hoje: Regional▸Ceará/RJ, Política, **Vídeos**, Economia, Geopolítica, Tecnologia, Youtube) |
| Locations do menu 21062 | `menu, amp-menu, amp-footer-menu, amp-alternative-menu` | Topo + rodapé + AMP usam o MESMO menu — mudar aqui afeta tudo |

**Raiz da queixa:** o dropdown desktop é estático e dessincronizado do menu WP (faltam Vídeos/Youtube); o hambúrguer já é dinâmico. **Alinhar = tornar o header desktop também dinâmico (`wp_nav_menu`) ou manter estático atualizado à mão.**

### 2.2 Profundidade do offcanvas
- Hoje: `'depth' => 2` no `wp_nav_menu` do offcanvas (`footer.php:67`) — mostra só **2 níveis**.
- Estrutura desejada tem **4 níveis** (Política ▸ Regional ▸ Região ▸ Estado). **Precisa mudar depth para 4.**

### 2.3 Categorias regionais — o que JÁ EXISTE
Investigação `wp db query` no canônico (taxonomy category):

**5 regiões (todas existem):**
| Região | term_id | slug | count |
|---|---|---|---|
| Norte | 21068 | norte | 2 |
| Nordeste | 4984 | nordeste | 19 |
| Sudeste | 21070 | sudeste | 9 |
| Sul | 21071 | sul | 200 |
| Centro‑Oeste | 21069 | centro-oeste | 0 |

**27 unidades federativas — 26 existem, FALTA 1:**
- ✅ Existem (term_ids 21072‑21090 + antigas): Acre, Alagoas, Amapá, Amazonas, Bahia, Ceará, Espírito Santo, Goiás, Maranhão, Mato Grosso, Mato Grosso do Sul, Minas Gerais, Pará, Paraíba, Paraná, Pernambuco, Piauí, Rio de Janeiro, Rio Grande do Norte, Rio Grande do Sul, Rondônia, Roraima, Santa Catarina, São Paulo, Sergipe, Tocantins.
- ❌ **Falta criar: Distrito Federal** (Centro‑Oeste).
- ⚠️ Muitas com **count=0** (vazias) — apareceriam no menu sem conteúdo. Decidir se mostram mesmo vazias.

**Regional (4986):** 53 posts, mas **não é parent de nenhuma categoria** na taxonomia (`tt.parent=4986` retorna vazio). Hoje Ceará/RJ são subitens de Regional só na **hierarquia do menu** (nav_menu_item.menu_item_parent), não na taxonomia.

## 3. Estrutura desejada (árvore do menu)

```
Quem somos?
Editorias ▸
  Política ▸
    Regional ▸
      Norte ▸        (Acre, Amapá, Amazonas, Pará, Rondônia, Roraima, Tocantins)
      Nordeste ▸     (Alagoas, Bahia, Ceará, Maranhão, Paraíba, Pernambuco, Piauí, RN, Sergipe)
      Sudeste ▸      (Espírito Santo, Minas Gerais, Rio de Janeiro, São Paulo)
      Sul ▸          (Paraná, Rio Grande do Sul, Santa Catarina)
      Centro-Oeste ▸ (Distrito Federal [criar], Goiás, Mato Grosso, Mato Grosso do Sul)
  Vídeos
  Economia
  Geopolítica
  Tecnologia
  Youtube
```

(Regional sai de "Editorias" e vira submenu de "Política"; Vídeos/Economia/Geopolítica/Tecnologia/Youtube permanecem subitens diretos de Editorias.)

## 4. Decisões a confirmar com o Miguel (pendências do plano)

1. **Regiões: 5 oficiais do IBGE** (Norte, Nordeste, Sudeste, Sul, Centro‑Oeste). Miguel falou *"4 regiões"* — **confirmar se são 5** (oficial) ou se quer excluir alguma.
2. **Hierarquia de taxonomia** (category parent) além da de menu? Hoje Regional não é parent categoria. Fazer `Região.parent = Regional` e `Estado.parent = Região` (consistência taxonômica) ou só montar a árvore no menu nav_menu?
3. **Header desktop:** tornar dinâmico (`wp_nav_menu` com walker, igual ao offcanvas) **ou** manter estático e só atualizar o HTML (Vídeos/Youtube)? Dinâmico = sempre sincronizado; estático = mais controle visual mas desseca.
4. **Estados vazios (count=0):** aparecer no menu mesmo sem posts? (Hoje 19 das 27 unidades têm count=0.)
5. **Onde aplicar primeiro:** espelho (homologação) ou canônico direto? Dado o tamanho, **espelho primeiro** é mais seguro.
6. **Depth do offcanvas 2→4:** validar que o walker `bootstrap_5_wp_nav_menu_walker` renderiza 4 níveis bem no mobile (UX: offcanvas muito profundo pode ficar cansativo).

## 5. Riscos / atenção

- **AMP:** o menu 21062 também alimenta `amp-menu/amp-footer/amp-alternative`. Uma árvore de 4 níveis afeta o AMP (pode ficar pesado/feio no mobile AMP). Validar.
- **auto_add:** tem que permanecer **vazio** (`{"0":false,"auto_add":[]}`) — regra de ouro §BUG-20260806-MENU-SPAM-CASSINO-AUTOADD. Conferir depois de cada mudança.
- **Menu item por `menu_order` direto (SQL):** neste servidor o `wp menu item update --position` é não-determinístico (lição 18:01); usar `UPDATE wp_posts SET menu_order=N`.
- **Volume:** criar ~33 itens de menu (1 Regional já existe + 5 regiões + 27 unidades + mover Regional pra dentro de Política). Operação demorada, fazer com backup e validação incremental.

## 6. Pendência Miguel

Aprovar as decisões do §4 (especialmente nº 1 — 4 ou 5 regiões? — e nº 5 — espelho primeiro?) para iniciar a execução pelo `plano_trabalho_menu_hamburguer_regional_estados_20260812.md`.
