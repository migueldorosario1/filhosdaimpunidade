# MEMÓRIA TÉCNICA — Regra da manchete nacional por jornada (08–22h) — 15/09/2026

**Fórum-irmão:** `Foruns/forum_regra_manchete_nacional_jornada_20260915.md` (decisões resumidas). Este arquivo é o log técnico completo.

## O que aconteceu / o que falta / o que preciso do Miguel

- **O que aconteceu:** ordem do Miguel 15/09 ~14:3x cumprida em ~40min — regra "manchete só Nacional/Política/Eleições 2026 das 08h às 22h" implantada no gate da home (mu-plugin) e a manchete do ar trocada na hora (Irã/Omuz → Ciro Gomes), com provas de banco, gate e HTML público.
- **O que falta:** nada de ação. Espelho cafezinho.news fechado (aplicar lá quando reabrir); patch antigo "só cat 22" do agente_manchete NYC segue opcional (gate já protege).
- **O que preciso do Miguel:** nada; ajustes de janela/slugs são 1 linha.

## Arquivos tocados

1. `ocafezinho:/var/www/ocafezinho/wp-content/mu-plugins/cafezinho-real-image-gate.php` — v1.0.0→**v1.1.0** (edição completa regravada via `cat >` preservando dono/perms; `php -l` 2×).
2. Backup: `/var/www/ocafezinho/wp-content/mu-plugins-baks/cafezinho-real-image-gate.php.bak_pre_regra_manchete_nacional_20260915` (10.621 bytes, fora da raiz mu-plugins para o WP não carregar).
3. Cérebro: fórum + esta memória + NODO_MANCHETE + ATUALIZACOES + MONITORAMENTO + bloc na ponte de_dell (ZM-20260915-005).

## Diferença exata no código

- **Novas funções:** `cafezinho_manchete_janela_nacional_ativa()` (`current_time('H')` ∈ [8,22); WP tz America/Sao_Paulo confirmada via `wp option get timezone_string`), `cafezinho_post_is_nacional_politica_eleicoes($id)` (slug match em category+post_tag), `cafezinho_manchete_nacional_tax_query()` (relation AND: sub-OR de slugs + NOT IN cat 20699).
- **`cafezinho_get_real_highlight()`**: `$janela_nacional` só para `$name==='Manchete'`; manual ganhou 3ª cláusula `( ! $janela || is_nacional(...) )`; fallback ganha `tax_query` + `unset(category__not_in)` na janela; degrau extra: se a query de janela vier vazia após filtro verified, re-usa as MESMAS args (com tax_query) sem o filtro de selo e retorna o 1º com capa qualquer; fluxo noturno intocado.

## Slugs/termos mapeados (decisão)

Lista única aplicada às 2 taxonomias: `nacional` (cat 21141), `politica` (tag 16), `politica-2` (cat 22 «Política» 13.290 posts), `eleicoes-2026` (cat 5088 «Eleições 2026» 1.178 + tag 5602 498), `eleicoes2026` (cat 21186), `eleicoes` (cat 47 + tag 4597). Não existe tag «nacional» — o Miguel falou "tags" mas no site Nacional é categoria; casar por slug nas 2 taxonomias cobre a intenção.

## Bug caçado: tax_query + category__not_in (core WP)

- Sintoma: pós-fix#1 o gate elegeu **271117 (IA «Golpistas clonam voz», cat Inteligência Artificial)** com a janela ativa — a tax_query não restringia.
- Causa (SQL provada): com `tax_query` E `category__not_in` juntos, o core mescla o NOT IN 20699 como **cláusula OR** no grupo: `(... IN termos) OR (... IN termos) OR (ID NOT IN 20699)` → aprova quase tudo.
- Cura: 20699 entra como `array('taxonomy'=>'category','field'=>'term_id','terms'=>array(20699),'operator'=>'NOT IN')` dentro de tax_query com `relation=>'AND'` no topo + `unset($fallback_args['category__not_in'])`.
- Prova: query bruta 60/60 com tema certo; 271117 ausente; SQL mostra `AND` entre grupos.
- **Lição da casa:** misturar params de categoria simples com tax_query = armadilha silenciosa; sempre conferir `$query->request`, nunca confiar só no resultado quando o 1º já "parece" certo (271129 apareceu por coincidência de horário e quase mascara o bug).

## Comandos de prova (reprodutíveis)

```bash
# janela + gate
ssh cafezinho-wp 'wp --path=/var/www/ocafezinho --allow-root eval "\$h=cafezinho_get_real_highlight(\"Manchete\"); echo \$h->posts[0]->ID.\" | \".\$h->posts[0]->post_title; echo var_export(cafezinho_post_is_nacional_politica_eleicoes(\$h->posts[0]->ID),true);"'
# query bruta do filtro (271117 tem que estar AUSENTE de dia)
# curl público
curl -sL https://www.ocafezinho.com/ | grep -A2 'manchete-titulo'
```

## Testes

1. `php -l` antes do install + no arquivo final: sem erros (2×).
2. Janela ativa às 14:5x: true.
3. Gate elege 271129 (Política, capa verified) ✓; manual 270489 rejeitado ✓.
4. Query bruta de 60: zero posts fora da regra; IA 271117 ausente ✓.
5. HTML público www.ocafezinho.com 200: h1 manchete-titulo = Ciro Gomes + link do post ✓ (após `rocket_clean_home()`; CF é DYNAMIC p/ HTML).

— **ZCode/GLM-5.3**, 15/09/2026 ~15:0x BRT
