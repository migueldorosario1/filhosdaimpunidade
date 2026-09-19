# Fórum — Precedência de categorias: TECNOLOGIA SOBREPÕE (14/08 ~17:20 BRT)

**Regra Miguel (14/08, palavra):** "Quando tiver tecnologia, tem que sobrepor. Tecnologia também se sobrepõe a geopolítica. De qq forma, não é política."

**Caso-escola:** post 265822 "IA chinesa mais barata pressiona gigantes americanas" com cats {22 Política, 5003 Geopolítica, 15 Internacional, 30 Tecnologia, 4949 persona} + Yoast primary=4949 (pessoa!) → aparecia no bloco NACIONAL da home. Post NÃO veio do worker V4 (não há trace; criado pela pipeline do redator/Claude, autor 5749).

**Correção pontual:** removidas 22/5003/15 (canônico; espelho não tinha o post) + `_yoast_wpseo_primary_category` → 30. Home: post só no bloco Tecnologia.

**Correção ESTRUTURAL (pedida pelo Miguel):** mu-plugin `cafezinho-categoria-precedencia.php` v1.1 **nos 2 servidores** — hook `set_object_terms` (dispara em REST, wp-cli, humano; `save_post` NÃO cobre `wp post term add` — lição do teste). Se Tecnologia(30) presente → remove 22/5003/15 e corrige Yoast primary se apontava para removida. Anti-recursão via static flag. Log: `wp-content/uploads/categoria_precedencia.log`. **Testado em produção:** re-adicionei 22+15 e o guard expulsou na hora (log 18:14:36).

**Falta / próximos:** se Miguel quiser mais precedências (ex.: Esporte sobre Política?), é 1 linha no array $SUBORDINADAS por categoria-guarda. Atribuição "kitchen sink" do redator (5 cats de uma vez) continua acontecendo na origem — o guard neutraliza no WP; se quiser, cartinha ao Claude para parar de enviar 22/5008 junto.
