# Memória — Precedência categorias Cafezinho (14/08 ~17:20 BRT)

Par do fórum: `Foruns/forum_precedencia_categorias_tecnologia_20260814.md`.

## Técnica
- mu-plugin `/var/www/ocafezinho/wp-content/mu-plugins/cafezinho-categoria-precedencia.php` (e espelho). Hook **`set_object_terms`** (6 args) é o único ponto que cobre REST + wp-cli term ops; `save_post_post` falha no teste com `wp post term add`. Anti-recursão: `static $em_curso`.
- Yoast primary em `_yoast_wpseo_primary_category` (meta) — quando removemos cats, corrigir primary senão breadcrumb/SEO mostram a errada.
- Ablação de termos: `wp post term remove <id> category <term_id> --by=id` + `wp cache flush` ENTRE lista e remoção (cache de objetos devolve lista velha — lição 2).

## Diagnóstico
- Post sem trace no worker V4 (`grep -rl slug /root/agent_data/` só no auditor de títulos) = criado pela pipeline do redator (Claude), autor WP 5749. Categorias "kitchen sink" {22,5003,15,30} + persona.
- Guard testado em produção: term add 15 → removeu 15,22; finais {4949,30}; primary=30; log escrito.

## Estado
- No ar nos 2 servidores. Extensível: mais pares guarda→subordinadas editando arrays no mu-plugin.
