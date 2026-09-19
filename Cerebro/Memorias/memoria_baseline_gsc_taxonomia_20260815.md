# 📊 Memória técnica — Baseline GSC da taxonomia + plano SEO rigoroso (15/08/2026)

> Tema Duplo do fórum `Foruns/forum_plano_seo_organizacao_categorias_tags_20260815.md`. Log técnico completo pra retomar em qualquer conversa.

## Como o baseline foi extraído (15/08 ~11:35 BRT)

1. **Creds:** service account Google no Tencent (`/root/google_api_client.py`, classe `GoogleAPIClient`, propriedade `sc-domain:ocafezinho.com`, método `get_search_analytics`). SSH `tencent` = usuário **ubuntu** → executar com `sudo -n` (gotcha: `/root/.env.unificado` é root-only).
2. **Script:** `/tmp/gsc_baseline2.py` no Tencent — 4 janelas de ~23d (15/05→13/08/2026), `dimensions=["page"]`, `rowLimit=1000` por request (API limita), agregação por página. Nota: cada janela bateu o teto de 1000 linhas → long-tail abaixo do top-1000/janela não está no CSV (páginas com ~0 cliques de qualquer forma — margem aceitável).
3. **Saída:** `/root/gsc_baseline_paginas_90d.csv` (Tencent; cópia `/tmp/gsc_baseline.csv` local): 3.652 páginas, 214.463 cliques, 90d.
4. **Cruzamento local (python):** WP `wp term list category` (298) + `post_tag` (18.487) → slugs × paths-raiz do GSC (categorias são URL na raiz: `ocafezinho.com/<slug>/`; tags em `/tag/<slug>/`). CSVs em `/tmp/wp_categorias.csv` + `/tmp/wp_tags.csv`. **Gotcha:** o CSV do WP vem SEM cabeçalho (grep removeu) e nomes com vírgula vêm entre aspas → usar `csv.reader` por posição, não DictReader.

## Resultados-chave (90d: 15/05–13/08/2026)

- **Categorias com tráfego: 4/298** — `/politica-2/` 951 cliques · `/politica-internacional/` 108 · `/economia/` 41 · `/pt/` 20 (total 1.120 = 0,52%).
- **Tags com tráfego: 5/18.477** — `/tag/brasil/` 53 cliques (20.742 impressões!) · `/tag/ira/` 44 · `/tag/russia/`, `/tag/rollo/`, `/tag/marica-2/` 2 cada (total 103 = 0,05%).
- **294 categorias com ZERO cliques.** Tráfego real = posts individuais + Discover (confirma memória da auditoria de 14/08: Discover +755%).

## Implicações (viraram a matriz §3 do fórum)

1. Risco real de mexer em categorias/tags sem tráfego = **baixo** (o medo era maior que o dado). As 9 URLs vivas são **patrimônio intocável**.
2. Pipeline prudente adotado: **noindex→14d observação→merge (≤500/sprint)→redirect 301 ANTES→excluir→medir 7d** (§4 do fórum). Reaproveita esqueleto `/root/seo_pruning/seo_progressive_noindex.py` (GLM 01/07) — consultar `ids_adicionais_noindex_candidatos_20260628.csv` p/ histórico de noindex.
3. Ondas revisadas: 2 dedup slugs → 3 fundir cats sem tráfego (2–4/semana) → 4 autores→tag → 5 cidades/países→tag + hierarquia → 6 "Redação" → 7 singletons c/ filtro GSC (100–200/sem).
4. Monitoramento: baseline mensal (dia 15), alerta se queda >15% semana pós-onda, health-check dos redirects.

## Categorias re-rastreadas (298, pós-reforma do menu — parents ainda =0 exceto poucos; hierarquia real vive no MENU, não nos termos)

Mudanças vs rastreamento 12/08: Tecnologia 4.897→4.903 (sessão-irmã migrou Ciência-Tecnologia), São Paulo 302→304, Ceará 274→280, Sul 200→201, Paraná 200, Esporte 210→214, Eleições 240→242, Redação 37.385→37.386, IA 623→627, Saúde 663→671, Ciência 1.150→1.153, Cultura 353→359. **DF (21139) agora existe** (count 0, no menu). "A guerra dos algoritmos" 31→31. Authors cats seguem lá (Rhyan 4.212...).

## Estado / próximos passos

- ✅ Investigação + baseline + fórum do plano entregues (15/08 ~11:50).
- ⏭️ Aguarda Miguel: "vai na Onda 2" (dedup de slugs — risco mínimo; eu preparo a tabela de pares) e/ou priorização diferente das ondas.
