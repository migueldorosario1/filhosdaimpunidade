# Plano de Trabalho — Menu hambúrguer = header + Regional▸Regiões▸Estados

**Data:** 2026-08-12 ~18:10 · **Autor:** ZCode/GLM-5.2 · **Status:** 📋 PRONTO PRA EXECUTAR (aguarda autorização Miguel + decisões do §4 do fórum)
**Fórum pareado:** `Foruns/forum_menu_hamburguer_regional_estados_20260812.md`
**Ambiente:** canônico `ocafezinho.com` (190.89.239.65:51439) + espelho `cafezinho.news` (159.65.177.60) · tema `ocafezinho-portal` · menu WP **21062** ("Menu").

---

## Pré-requisitos (decisões do Miguel — ver fórum §4)
- [ ] **Regiões = 5 oficiais** (Norte, Nordeste, Sudeste, Sul, Centro‑Oeste)? (Miguel disse "4")
- [ ] Hierarquia de **taxonomia** (category parent) além da de menu? (recomendado: sim, p/ consistência)
- [ ] Header desktop: **dinâmico** (wp_nav_menu) ou **estático** atualizado? (recomendado: dinâmico)
- [ ] Estados **vazios (count=0)** aparecem? (recomendado: sim, criar a estrutura completa)
- [ ] **Espelho primeiro** p/ homologar? (recomendado: sim)

## Mapa de Categorias (já existem — confirmado 12/08)

| Região (parent) | term_id | Estados (term_id) |
|---|---|---|
| **Norte** (21068) | — | Acre 21072 · Amapá 21074 · Amazonas 21075 · Pará 21081 · Rondônia 21086 · Roraima 21087 · Tocantins 21090 |
| **Nordeste** (4984) | — | Alagoas 21073 · Bahia 4994 · Ceará 4968 · Maranhão 21078 · Paraíba 5101 · Pernambuco 21083 · Piauí 21084 · RN 21085 · Sergipe 21089 |
| **Sudeste** (21070) | — | Espírito Santo 21076 · Minas Gerais 2549 · Rio de Janeiro 1656 · São Paulo 4988 |
| **Sul** (21071) | — | Paraná 21082 · Rio Grande do Sul 5004 · Santa Catarina 21088 |
| **Centro‑Oeste** (21069) | — | Goiás 21077 · Mato Grosso 21079 · Mato Grosso do Sul 21080 · **Distrito Federal = CRIAR** |

Regional = 4986 (hoje parent de ninguém na taxonomia).

---

## FASE 0 — Backup + baseline (obrigatório, ~5 min)
```bash
WP='sudo -u www-data wp --path=/var/www/cafezinho-news'   # espelho primeiro
BK=/root/backup_menu_regional_$(date +%Y%m%d_%H%M%S); mkdir -p $BK
$WP menu item list 21062 --fields=db_id,title,object_id,menu_item_parent,position > $BK/menu_items_pre.txt 2>/dev/null
$WP option get nav_menu_options --format=json > $BK/nav_menu_options_pre.json 2>/dev/null
cp /var/www/cafezinho-news/wp-content/themes/ocafezinho-portal/{header,footer}.php $BK/
# snapshot menu_order de todos os itens do menu 21062
$WP db query "SELECT ID, post_title, menu_order FROM wp_posts p JOIN wp_term_relationships tr ON p.ID=tr.object_id JOIN wp_term_taxonomy tt ON tr.term_taxonomy_id=tt.term_taxonomy_id WHERE tt.taxonomy='nav_menu' AND tt.term_id=21062 ORDER BY menu_order;" > $BK/menu_order_pre.txt 2>/dev/null
```
**Conclusão F0:** backups em `$BK`. Smoke: site no ar (HTTP 200 home).

## FASE 1 — Categorias faltantes (~5 min)
```bash
# Criar Distrito Federal (Centro-Oeste). Confirmar slug único.
$WP term create category "Distrito Federal" --slug="distrito-federal" --porcelain   # → novo term_id
# (Opcional, se decisão §4.2 = sim) hierarquia de taxonomia:
$WP term update 21068 category --parent=4986   # Norte  → filha de Regional
$WP term update 4984  category --parent=4986   # Nordeste
$WP term update 21070 category --parent=4986   # Sudeste
$WP term update 21071 category --parent=4986   # Sul
$WP term update 21069 category --parent=4986   # Centro-Oeste
# estados → filhos da região correta (27 UPDATEs; ver mapa acima)
#   ex.: $WP term update 21072 category --parent=21068   # Acre → Norte
```
**Validação F1:** `wp term get <id> category --field=parent` retorna o term_id pai correto. Distrito Federal criada.

## FASE 2 — Reestruturar o MENU 21062 (~30 min, a fase mais longa)
Objetivo: montar a árvore do §3 do fórum. Estratégia: **criar itens via `menu item add-term` e encadear `menu_item_parent` por `menu_order` direto (SQL)** — `wp menu item update --position` é não-determinístico aqui (lição 18:01).

**Passo 2.1 — Regional vira submenu de Política:**
- Regional (item existente, db_id 263595) muda `menu_item_parent` de 263602 (Editorias) → 263596 (Política). Via SQL:
```sql
UPDATE wp_postmeta SET meta_value='263596' WHERE meta_key='_menu_item_menu_item_parent' AND post_id=263595;
```

**Passo 2.2 — Adicionar 5 regiões como submenu de Regional (parent=263595):**
```bash
for CAT in 21068:21068 4984:4984 21070:21070 21071:21071 21069:21069; do
  TID=${CAT%%:*}
  $WP menu item add-term 21062 category $TID --parent-id=263595   # db_id novo a cada um
done
```

**Passo 2.3 — Adicionar 27 unidades como submenu da região correta (parent=db_id da região):**
Script: para cada estado, `menu item add-term 21062 category <estado_term_id> --parent-id=<regiao_db_id>`. Mapear estado→região (ver mapa). 27 comandos.

**Passo 2.4 — Reordenar tudo por `menu_order` direto (SQL):**
Atribuir `menu_order` em faixas largas por nível, de forma determinística:
- Quem somos = 10, Editorias = 20
- Política = 60 (submenu de Editorias)
  - Regional = 6010 (submenu de Política)
    - Norte = 601010, Nordeste = 601020, Sudeste = 601030, Sul = 601040, Centro-Oeste = 601050
      - estados:submenu-item (60101010, 60101020, ... — faixa de 10 por estado dentro de cada região)
- Vídeos = 70, Economia = 80, Geopolítica = 90, Tecnologia = 100, Youtube = 110
```sql
UPDATE wp_posts SET menu_order=<N> WHERE ID=<db_id>;   -- um por item
```

**Validação F2:** `wp menu list` + renderizar home mobile (offcanvas) e desktop. Conferir árvore com `wp menu item list 21062 --fields=db_id,title,menu_item_parent` ordenado por menu_order.

## FASE 3 — Offcanvas mobile: depth 2 → 4 (~3 min)
`footer.php` (canônico e espelho), bloco `wp_nav_menu` do offcanvas (~linha 65):
```php
wp_nav_menu( array(
    'menu'   => 'Menu',
    'depth'  => 4,          // era 2  ← MUDAR
    ...
) );
```
**Validação F3:** abrir offcanvas no mobile → Política ▸ Regional ▸ Norte ▸ Acre abre em 4 níveis. PHP lint.

## FASE 4 — Header desktop alinhado (~10 min, depende da decisão §4.3)
- **Opção A (recomendada — dinâmico):** substituir o `<ul class="dropdown-menu">` estático (header.php linhas 30‑35) por `wp_nav_menu` com o mesmo walker do offcanvas. Vantagem: sempre sincronizado com o menu 21062.
- **Opção B (estático):** adicionar Vídeos + Youtube ao `<ul>` estático e (opcional) recriar a árvore Regional em HTML. Dessincroniza novamente no futuro.
**Validação F4:** dropdown desktop mostra as mesmas categorias do hambúrguer.

## FASE 5 — AMP + cache + homologação (~10 min)
- Conferir **AMP** (locations amp-menu/amp-footer/amp-alternative): árvore de 4 níveis não pode quebrar o mobile AMP.
- `auto_add` conferir vazio: `$WP option get nav_menu_options` → `{"0":false,"auto_add":[]}`.
- Purge WP Rocket (`rocket_clean_domain()` + `wp_cache_flush()` via `wp eval-file`).
- **Hard refresh mobile + desktop + AMP** e validar visualmente com o Miguel.

## FASE 6 — Port espelho → canônico (após Miguel homologar no espelho)
Repetir F0‑F5 no canônico (`/var/www/ocafezinho`). Mesma sequência, mesmos backups.

## FASE 7 — Documentação (Tema Duplo)
Adendo/memória: comandos exatos, db_ids criados, diffs header/footer.php, SHAs, screenshots. Indexar em `CARTAO_BOLSO_MENU_WP_CAFEZINHO.md` (estrutura do menu) + `CEREBRO_NODE_PUBLICACAO_WP_CAFEZINHO.md` + `ATUALIZACOES` + monitor.

---

## Rollback (por fase)
- **F1 (categorias):** `wp term delete <id> category` (Distrito Federal) + reverter `--parent` (setar `--parent=0`).
- **F2 (menu):** restaurar `menu_item_parent` e `menu_order` do `$BK/menu_order_pre.txt`; remover itens novos via `wp menu item delete <db_id>`.
- **F3/F4 (tema):** restaurar `header.php`/`footer.php` de `$BK/`.
- **auto_add:** se mudou, reverter pra `{"0":false,"auto_add":[]}` (script no `CARTAO_BOLSO_MENU_WP_CAFEZINHO.md`).

## Estimativa
~60‑90 min no espelho + homologação Miguel + ~45 min port canônico. Sprint de média duração — justificada a separação (ordem Miguel).

## Riscos
- Walker `bootstrap_5_wp_nav_menu_walker` renderiza 4 níveis? Testar no F3 (se não, patch no walker).
- UX mobile: offcanvas com 4 níveis pode ficar cansativo — avaliar com o Miguel (talvez collapse/accordion).
- Estados count=0: cliques levam a páginas vazias — decidir se maquia (ex: "em breve") ou se popula depois.
- Performance: menu 21062 passa de 11 → ~45 itens; impacto no tempo de render do menu (medir).
