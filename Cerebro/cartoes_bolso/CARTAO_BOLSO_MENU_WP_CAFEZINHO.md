# Cartão de Bolso — MENU do WordPress O Cafezinho (editar / corrigir / travar)

> **Criado:** 2026-08-06 (ZCode/Kimi K3) · **Origem:** caso-escola `BUG-20260806-MENU-SPAM-CASSINO-AUTOADD` — publi autorizado ("O jogo do balão…", cassino) vazou pro menu porque a caixa "adicionar novas páginas automaticamente" estava ligada. Tema Duplo: `Foruns/forum_menu_spam_cassino_autodd_20260806.md` + `Memorias/memoria_menu_spam_cassino_autodd_20260806.md`.

---

## 🚨 REGRA DE OURO (permanente — ordem Miguel 06/08/2026)

**`auto_add` DESLIGADO para sempre.** Nenhuma página nova entra automaticamente em menu nenhum. Estado atual: `nav_menu_options = {"0":false,"auto_add":[]}`.

- Ao criar/recriar menu no wp-admin, a caixa **"Automatically add new top-level pages" vem MARCADA por padrão → DESMARCAR sempre.**
- Publis (Rian/rhyandemeira, autorizados) publicam normal — só não podem vazar pro menu. É exatamente o que o auto-add desligado garante.
- Se um dia alguém religar sem querer, sintoma = página de publi aparecendo no menu. Correção: seção "Emergência" abaixo.

---

## 🗺️ Qual menu é qual (mapa 06/08/2026)

| term_id | Nome | Onde aparece | Usar? |
|---|---|---|---|
| **21062** | **Menu** | **locations `menu`, `amp-menu`, `amp-footer-menu`, `amp-alternative-menu` = TOPO e RODAPÉ do site (são o MESMO menu)** | ✅ **ESTE** |
| 1279 | apptha | nenhuma (relíquia de plugin de app; 626 itens acumulados por auto-add histórico) | ❌ nunca |
| 1309 | Header Menu | nenhuma (legado, 29 itens) | ❌ |
| 1369 / 2880 / 2879 / 654 / 1678 / 2373 / 1340 / 1268 | footer, Menu Topo Direito/Esquerdo, Pages, Temas do blog, Colunistas, English, wiziapp_custom | nenhuma location ativa | ❌ (legados) |

**Estrutura atual do menu 21062 (10 itens — atualizado 12/08/2026 ~19:27):**
1. Quem somos? (página 158707)
2. Editorias (custom `#`) ▸
   - Política (22) ▸ **Regional (4986) ▸ Ceará (4968), Rio de Janeiro (1656)** *(Regional movido p/ submenu de Política 12/08 ~18:11; era filho direto de Editorias)*
   - Vídeos (28) · Economia (43) · Geopolítica (5003) · Tecnologia (30)  *(cat Youtube 20751 UNIFICADA em Vídeos e removida do menu 12/08 ~19:27)*
   - Ordem por `menu_order`: Política=60 · Regional=61 · Ceará=62 · RJ=63 · Vídeos=70 · Economia=80 · Geopolítica=90 · Tecnologia=100. (Vídeos db_id 265408 antes de Economia ~18:01.) **offcanvas mobile `depth`=3** (footer.php:67; era 2) — Regional (nível 3) visível no hambúrguer; Ceará/RJ (nível 4) só com depth 4 (sprint maior). **Youtube db_id 265406 removido 12/08 ~19:27 (unificado em Vídeos); cat 20751 mantida vazia (0 posts).**
   - ⚠️ Para reordenar, **setar `menu_order` direto via SQL** (`UPDATE wp_posts SET menu_order=N WHERE ID=...`) — o `wp menu item update --position=N` renumera de forma confusa neste servidor.
   - *(obs: "Ciência e Tecnologia" 19936 foi mergeada em Tecnologia 30 em 12/08 ~00:18 — port F8)*

**📋 PRÓXIMO SPRINT PLANEJADO (não executado, 12/08):** alinhar hambúrguer ao header + reestruturar Regional como submenu de Política ▸ 5 regiões ▸ 27 unidades (+ criar DF). Diagnóstico: header desktop dropdown é **HTML estático** (sem Vídeos/Youtube); offcanvas é `wp_nav_menu` dinâmico mas `depth=2` (precisa 4). Ver `Foruns/forum_menu_hamburguer_regional_estados_20260812.md` + `Foruns/plano_trabalho_menu_hamburguer_regional_estados_20260812.md`. Aguarda Miguel.

---

## 🔧 Acesso

```bash
ssh cafezinho-wp                      # us65.serverdo.in (190.89.239.65:51439) — ver CARTAO_BOLSO_SSH_SERVIDOR_WP_CAFEZINHO.md
WP='sudo -u www-data wp --path=/var/www/ocafezinho'
```

⚠️ wp-cli nesse servidor cospe um PHP Notice + dump da função `wp_bs_pagination` (bootstrap do tema faz eval sem HTTP_HOST). Ruído cosmético — pipe `2>/dev/null | tail -N` resolve.

---

## ✅ Operações do dia a dia (wp-cli)

**Listar menus e itens:**
```bash
$WP menu list                                              # todos os menus + locations + contagem
$WP menu item list 21062 --fields=db_id,title,type,object,object_id,menu_item_parent,position
```

**Renomear um item:**
```bash
$WP menu item update <db_id> --title="Novo nome"
```

**Reordenar (position começa em 1):**
```bash
$WP menu item update <db_id> --position=2
```

**Adicionar itens:**
```bash
$WP menu item add-post   21062 <page_id> [--title="..."]          # página
$WP menu item add-term   21062 category <cat_id> [--title="..."]  # categoria
$WP menu item add-custom 21062 "Rótulo" "https://url"             # link livre
$WP menu item add-term   21062 category <cat_id> --parent-id=<db_id_do_pai>   # SUBMENU
```

**Remover item:**
```bash
$WP menu item delete <db_id>
```

**Backup ANTES de mexer (padrão obrigatório):**
```bash
mkdir -p /root/backup_menu_$(date +%Y%m%d)
$WP menu item list 21062 --fields=db_id,title,type,object,object_id,menu_item_parent,position > /root/backup_menu_$(date +%Y%m%d)/menu_21062_items.txt
$WP option get nav_menu_options --format=json > /root/backup_menu_$(date +%Y%m%d)/nav_menu_options.json
```

**DEPOIS de qualquer mudança — purgar cache (Rocket não tem CLI neste servidor):**
```bash
# padrão usado em 06/08: php em /tmp + eval-file
printf '%s\n' '<?php if(function_exists("rocket_clean_domain")){rocket_clean_domain();} wp_cache_flush(); echo "CACHE_OK\n";' > /tmp/purge.php
$WP eval-file /tmp/purge.php
# alternativa: wp-admin → barra superior WP Rocket → "Limpar cache"
```

**Verificar no ar:**
```bash
curl -sL https://www.ocafezinho.com/ | grep -c "nome-do-item"   # homepage reflete o menu
```

---

## 🖱️ Pelo wp-admin (para o Miguel)

`controle.ocafezinho.com/wp-admin` → **Aparência → Menus** → selecionar "Menu" (21062) → arrastar/soltar, renomear, adicionar à esquerda. **Só NÃO marcar** "Automatically add new top-level pages". Salvar. Se a mudança não aparecer no site: barra do WP Rocket → Limpar cache.

---

## 🚑 Emergência — "entrou página estranha no menu de novo"

```bash
# 1) achar o item (ex.: procurar por título/objeto)
$WP db query "SELECT p.ID, p.post_title FROM wp_posts p JOIN wp_term_relationships tr ON p.ID=tr.object_id JOIN wp_term_taxonomy tt ON tr.term_taxonomy_id=tt.term_taxonomy_id AND tt.taxonomy='nav_menu' AND tt.term_id=21062 WHERE p.post_type='nav_menu_item' AND p.post_status='publish' AND p.post_title LIKE '%trecho%';"
# 2) apagar o item
$WP menu item delete <ID>
# 3) conferir a trava (tem que ser auto_add vazio!)
$WP option get nav_menu_options
# 4) se voltou ligado, desligar de novo:
printf '%s\n' '<?php $o=get_option("nav_menu_options"); $o["auto_add"]=array(); update_option("nav_menu_options",$o); echo "TRAVADO\n";' > /tmp/trava.php
$WP eval-file /tmp/trava.php
# 5) purgar cache (bloco acima) e verificar o site
```

---

## ↩️ Rollback

- Estado pré-fix de 06/08: `/root/backup_menu_fix_20260806/` no servidor (itens + opção originais, script usado).
- Item apagado por engano: re-criar com `add-post`/`add-term` na posição certa (a lista de backup tem todos os IDs).
- NUNCA restaurar `auto_add` com valor não-vazio — a trava vazia é o estado canônico.

---

## Lição permanente

> Menu do Cafezinho: topo e rodapé são **um objeto só** (21062) — mexer num mexe nos dois (+ AMP). A porta dos fundos é o `auto_add`: em site com publis/editores múltiplos, ele **sempre** desligado. Qualquer agente que criar menu novo no wp-admin deve desmarcar a caixa na hora.
