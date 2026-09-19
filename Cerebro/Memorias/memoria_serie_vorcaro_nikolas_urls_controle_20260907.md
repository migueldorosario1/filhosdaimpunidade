# Memória — Correção urgente URLs `controle.ocafezinho.com` posts 269245/269246/269247 (07/09/2026, ZCode Dell Kimi K3)

Log técnico completo. Fórum irmão: `Cerebro/Foruns/forum_serie_vorcaro_nikolas_urls_controle_20260907.md`.

## Contexto

- Pedido do Miguel 07/09 ~16:1x (urgente): 3 posts da série Vorcaro/Nikolas (269245 parte 1, 269246 parte 2 "A mina do áudio", 269247 parte 3 "Horta, Teixeira") com 4 URLs de imagem cada apontando para `controle.ocafezinho.com` (domínio admin, proibido em público).
- Trava conhecida: REST POST → `HTTP 423 editorial_post_intocavel / post_publicado_por_humano` (mu-plugin `cafezinho-protecao-editorial.php`; autor 2018 = humano, fora da lista de autores automáticos {5470, 5786, 5787}).
- Monitor checado antes (regra Nº 2): nenhuma sessão nos 3 posts; linha própria aberta 16:14.

## Estado inicial (levantamento)

```
wp post get 269245/46/47: publish, post_author 2018
mídia 269289: attachment inherit "nikolas-ferreira-plenario-camara-julho-2024"
term get category 22 = Política · 21141 = Nacional (slug: nacional)
terms iniciais: 269245 [22, 21141] ✓ · 269246 [22] · 269247 [22]
_thumbnail_id 269245 antes: 269290
db query "SELECT ID FROM wp_posts WHERE post_content LIKE '%controle.ocafezinho.com%'":
  → CENTENAS de posts (94268 … 269304) — search-replace global inviável; escopo = 3 IDs
```

## Backups (antes de tocar)

`Cerebro/Backups/posts_editados/`:
- `269245_pre_fix_20260907.md` (13.598 bytes, 4 ocorrências)
- `269246_pre_fix_20260907.md` (10.761 bytes, 4 ocorrências)
- `269247_pre_fix_20260907.md` (8.514 bytes, 4 ocorrências)
- `269245_thumbnail_pre_fix_20260907.txt` (= 269290)

Rollback do conteúdo = `wp post update <id> <arquivo_backup>` com o override; rollback do thumb = `wp post meta update 269245 _thumbnail_id 269290` com override.

## Execução

1. **Conteúdo** (por post, via arquivo — receita do caso 268553):
```bash
sudo -u www-data wp --path=/var/www/ocafezinho post get $id --field=post_content > /tmp/fix_$id.html
sed -i "s/controle\.ocafezinho\.com/www.ocafezinho.com/g" /tmp/fix_$id.html
sudo -u www-data env CAFEZINHO_EDITORIAL_HUMAN_OVERRIDE=1 wp --path=/var/www/ocafezinho post update $id /tmp/fix_$id.html
```
→ `Success: Updated post` ×3; 0 ocorrências no arquivo antes do update; 0 no banco depois.

2. **Categorias — ERRO E CURA (armadilha nova):**
```bash
wp post term add 269246 category 21141   # ❌ cria termo NOVO nome "21141" (term_id 21230)!
```
`post term add` resolve o termo **por slug**; "21141" não existia como slug → `wp_set_post_terms` criou categoria nova. Cura:
```bash
wp post term remove <id> category 21141   # remove a espúria (slug "21141") dos 2 posts
wp term delete category 21230             # apaga a espúria
wp post term add <id> category nacional   # ✅ pelo slug real
```
Terms finais conferidos: os 3 posts com [21141 Nacional, 22 Política].

3. **Thumbnail:**
```bash
sudo -u www-data env CAFEZINHO_EDITORIAL_HUMAN_OVERRIDE=1 wp post meta update 269245 _thumbnail_id 269289
```
→ `Success: Updated custom field` (sem o env, o guard bloqueia meta de post de humano — caso 267802/30-08).

4. **Purge em camadas (receita 27/08):**
```bash
wp eval 'rocket_clean_post(269245/46/47); rocket_clean_domain(); wp_cache_flush();'
redis-cli FLUSHALL   # → OK
```

## Verificação

- **Banco (wp-cli):** 0 ocorrências `controle.ocafezinho.com` no post_content dos 3; terms [22, 21141] ×3; `_thumbnail_id` 269245 = 269289.
- **REST público** (`/wp-json/wp/v2/posts/<id>?_fields=id,categories,featured_media,status`):
  - 269245: `featured_media: 269289`, `categories: [21141, 22]` ✓
  - 269246: `categories: [21141, 22]` ✓ · 269247: idem ✓
- **Páginas públicas** (curl UA navegador + `?nocache=<ts>`): imagens do conteúdo servidas de `www.ocafezinho.com/wp-content/uploads/...`; as 12 URLs únicas de imagem testadas com HEAD → **HTTP 200** (ex.: `mapa-topazio-vorcaro-lages-kallas-ouro-preto.png`, `cronologia-topazio-nikolas-vorcaro.png`, `diagrama-nikolas-faria-vorcaro-v3-scaled.png`).
- URLs públicas:
  - https://www.ocafezinho.com/2026/09/06/exclusivo-o-amigo-de-nikolas-e-as-minas-do-rei-vorcaro/
  - https://www.ocafezinho.com/2026/09/06/a-mina-do-audio-o-que-ha-no-subsolo-de-rodrigo-silva-e-por-que-ela-esta-travada/
  - https://www.ocafezinho.com/2026/09/06/horta-teixeira-e-a-empresa-de-fachada-que-contratou-o-advogado-de-nikolas-para-vender-a-mina/

## Achado estrutural (registrado, NÃO mexido — aguarda Miguel)

Nas páginas públicas restam 2 ocorrências de `controle.ocafezinho.com` vindas do **WP Statistics**: `WP_Statistics_Tracker_Object = {"ajaxUrl":"https://controle.ocafezinho.com/wp-admin/admin-ajax.php",...}` — site-wide, todo post/página. Diagnóstico: `wp option get siteurl|home` = `https://www.ocafezinho.com` e `WP_SITEURL` não definido, **mas `admin_url('admin-ajax.php')` devolve `https://controle.ocafezinho.com/...`** → há filtro/mu-plugin roteando admin para o vhost controle (arquitetura da casa). O JS do plugin apenas expõe isso no frontend. Opções futuras: filtro no plugin p/ usar `home_url`/REST próprio, ou aceitar (admin-ajax via controle pode ser desenho).

## Lições

1. **Desbloqueio da trava editorial** (registrado também como ATUALIZAÇÃO na OBS-035 do CEREBRO_NODE_BUGS_ATIVOS, a pedido do Miguel): `sudo -u www-data env CAFEZINHO_EDITORIAL_HUMAN_OVERRIDE=1 wp --path=/var/www/ocafezinho <cmd>` — cobre `post update`, `post meta update`, `post term add/remove`. Só com ordem explícita do Miguel.
2. 🔴 **`wp post term add` é por SLUG**: passar ID numérico de categoria cria termo novo com esse número como nome. Conferir `post term list` depois de qualquer add.
3. 🔴 **Search-replace de domínio no Cafezinho NUNCA global sem dry-run de IDs**: `controle.ocafezinho.com` está no post_content de centenas de posts antigos (legado). Sempre restringir por ID.
4. Prova = readback do servidor (REGRA DE PROVA da CL-035): grep no banco + REST público + curl `?nocache` — nunca o eco do comando de escrita.
