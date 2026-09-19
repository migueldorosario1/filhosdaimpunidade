# Memória — Investigação GSC noindex 49.356 no canônico ocafezinho.com (ZM, 06/09/2026)

Log técnico completo do fórum `Foruns/forum_gsc_noindex_49mil_canonico_20260906.md`. LEITURA-ONLY: nada foi alterado em produção.

## Insumos

- Export GSC do Miguel (baixado ~18:43–18:48 de 06/09): Coverage, Performance-on-Search (3 meses), AMP, HTTPS, CWV ×2 — em `Outros/google search/google search/google search 6 set 2026/` (descompactado em `exports/`).
- SSH canônico: `ssh cafezinho-wp` (190.89.239.65:51439, root, WP em /var/www/ocafezinho; domínio real = **https://www.ocafezinho.com** — NÃO .com.br).
- SSH Tencent: `ssh tencent`.

## Fatos medidos no WP canônico

- Contagens: **78.981 posts** publicados, **116.381 anexos**, 577 pages, **18.542 tags**, 310 categorias.
- Plugins SEO: wordpress-seo 28.4 (+premium, +news, +local). Config `wpseo_titles`: `noindex-tax-post_tag=False`, `noindex-tax-category=False`, `noindex-tax-post_format=True`, `noindex-ptarchive-produto=true`, `disable-attachment=True` (anexo → 301 pro arquivo).
- Mu-plugins da casa com noindex (4): `cafezinho-noindex-pruning.php` (358 IDs, 27/06, sprint Trindade, autorizado pelo Miguel; monitora o próprio GSC), `cafezinho-noindex-pages.php` (06/07 GLM; pages pré-10/08 11:08 noindex, whitelist 156483/84052/158707/263412 + override Yoast meta=2), `cafezinho-seo-pruning.php` (01/07 GLM; listas via REST `cafezinho/v1/noindex-list` sincronizadas da Tencent; **option `cafezinho_seo_pruning_list`: updated_at 2026-07-20 00:07:12, strategy_410=1.317, strategy_noindex=1** → CONGELADO), `cafezinho-gone-pending-review.php` (10 URLs 410).
- Banco: `_yoast_wpseo_meta-robots-noindex` → 550 posts com valor 1 (auditoria categorias 28/06 tinha 2.368 candidatos: Ciência e Tecnologia 2.267, Sobrenatural 97, Fantástico 4 — ver `Outros/google search/auditoria_noindex_categorias_20260628/`).
- Tencent: **nenhum** cron (ubuntu/root) com noindex/pruning/saneamento/seo → nada alimenta o endpoint desde 20/07.

## Provas ao vivo (curl, 06/09 ~18:4x–18:5x BRT)

| URL | Resultado |
|---|---|
| Post pruning `/2026/04/14/nasa-anuncia-sr-1-freedom.../` (ID 234468) | HTTP 200 + `<meta name='robots' content='noindex, follow'/>` ✓ |
| Page antiga `/logout/` (77275) | `noindex` ✓ (regra do mu-plugin pages) |
| Post comum 2025 `/2025/07/31/tesouro-dos-eua.../` | `index, follow, max-image-preview...` ✓ saudável |
| Post set/2026 `/2026/09/06/a-psicopatia-de-bessent/` | indexável + canonical próprio + amphtml ✓ |
| `?attachment_id=269261` | **301 → arquivo PNG** (não é noindex) |
| `/2026/09/06/.../embed/` e `/amp/` e `?amp` | 200 + canonical → post (viram "alternativa canônica" no GSC) |
| `/tag/lula/`, `/2026/09/`, `/page/2/` | 200 sem noindex (indexáveis) |
| `/es/` (GTranslate) | 404 (não usa path de idioma) |
| Espelho `cafezinho.news` | `X-Robots-Tag: noindex, nofollow, noarchive` (sandbox de propósito, alheio a esta conta) |

## Leitura dos exports GSC

- Coverage (03/09): não-indexadas 205.458 estáveis desde 28/08; noindex 49.356; alternativa canônica 68.554; rastreada-não-indexada 70.872; detectada 7.867; 404 3.860; robots.txt 3.090.
- Gráfico histórico: salto de **+11.041 não-indexadas em 24/07** ← eco dos últimos lotes do saneamento (última sync 20/07 00:07). Baseline de 07/06 já era ~209k não-indexadas (site de ~10 anos, ~280k URLs conhecidas).
- Performance 3 meses: ~180k cliques / 6,3M impressões; mobile posição 3,65 CTR 3,25%; **AMP 101.448 cliques posição 2,51**; HTTPS 0; CWV só melhorias.

## Conclusão

Robô algum está contaminando o canônico: noindex = saneamento deliberado (358+550+~570+1) + estado congelado de lotes históricos de junho/julho + acumulação do GSC (URL noindex quase não é re-rastreada). Posts novos nascem indexáveis. Recomendação: NÃO mexer (tirar do índice era o objetivo); vigiar só "Rastreada, mas não indexada" (qualidade editorial).

## Armadilhas anotadas (para próximas investigações)

1. **IP do Dell é bloqueado/limitado pela CDN do canônico** em rajada (45 curls seguidos → todos HTTP 000). Testar em rajada via SSH no próprio servidor (curl -sk localhost/externo de lá) ou poucas URLs.
2. **wp-cli do canônico imprime uma linha extra** (permalink do post mais recente) em vários comandos — provável mu-plugin (suspeito: `cafezinho-purge-on-manchete.php`). Sempre `| tail -1` ao capturar URL de `wp post url`.
3. `wp post list --date_query=[...]` por ssh com as duplas quebra silenciosamente (ignora o filtro) — usar `wp db query "ORDER BY RAND() LIMIT n"` direto.
4. `wp eval` com `\$` por ssh dá parse error — usar `wp option get --format=json | python3 -c ...` no servidor.
5. Exports do GSC descompactam com **nomes UTF-8 quebrados** (`Gr├бfico.csv`) — acessar por glob (`P*ginas.csv`), não por nome literal.
6. O ZIP "Coverage" do GSC traz só resumo; a lista de URLs por motivo é outro botão (exportar dentro do motivo).
