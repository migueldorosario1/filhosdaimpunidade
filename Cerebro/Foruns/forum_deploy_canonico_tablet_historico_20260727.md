# Fórum — Deploy canônico V1.3 (tablet + Histórico) no ocafezinho.com

**Data:** 27 de julho de 2026
**Executor:** ZCode · **Autorizador:** Miguel (homologou no espelho e pediu o port "com muito cuidado, plano de rollback e backups")
**Escopo:** portar do espelho `cafezinho.news` para o canônico `ocafezinho.com` as 4 mudanças da V1.3, **uma por vez**, nesta ordem combinada com Miguel:
1. **Histórico** vermelho no fim do bloco Recentes (arquivo por ano/mês)
2. Colunas — card mostra só a última coluna no tablet (768–1199.98px)
3. Menu sanfona (hambúrguer) no tablet
4. Tirar o resumo da manchete no tablet

**Relacionado:** `forum_lab_visual_cafezinho_news_20260720.md` (V1.0–V1.3 do espelho, onde tudo foi homologado).

## Protocolo de segurança (definido por Miguel)

- **100% aditivo:** nenhum arquivo existente é editado; tudo via mu-plugins NOVOS.
- **Rollback de cada passo = apagar os arquivos novos + purgar cache.**
- Plano completo + rollback + log no servidor: `/root/rollback_canonico_20260727/PLANO_E_ROLLBACK.md`
- Baseline da capa antes de mexer: `/root/rollback_canonico_20260727/baseline_capa_antes.html.gz`
- Cada passo só avança após OK visual de Miguel.

## Diagnóstico do canônico (27/07 ~08h50 BRT)

- WP Rocket 3.12.3.2 ativo; CLI `wp rocket` indisponível → purge via `rocket_clean_domain()` (wp eval-file a partir de /tmp — **www-data não lê /root**) + `wp cache flush`.
- `serverdoin-cdn` 1.4 ativo (rewrite de URL de assets; arquivos novos = URLs novas, sem purge necessário; filemtime cache-busta edições).
- Markup da capa idêntico ao espelho nos pontos usados (hamburger `a[href="#menu"]`, `ul#menu-menu`, 21 cards `.col.columnists`, 37 linhas de anteriores, `h4.text-red` Recentes).
- `--red: #CD152B` existe no `:root` do style.css do tema.
- Arquivo real: 2011–2026 (~70k posts; 2023=10.656, 2026=15.898+).

## PASSO 1 — Histórico ✅ (27/07 ~09h00 BRT)

**Arquivos novos (mu-plugins/):** `cafezinho-historico.php` + `.css` + `.js`
- Diferença do espelho: HTML do painel cacheado em **transient de 1h** (`cafezinho_historico_html`), invalidado em `save_post`/`deleted_post`/`trashed_post` — protege o MySQL do GROUP BY em ~70k posts a cada view da capa.
- `php -l` antes de instalar; rollback documentado no servidor.

**Validação pós-deploy:**
- Capa HTTP 200, 284.962 → 318.145 bytes (+33KB do painel)
- Painel com **16 anos (2011–2026)**, **179 links mensais**, contagens reais (soma de 2023 = 10.656, confere com o banco)
- 21 cards de colunistas e 37 anteriores intactos; manchete intacta
- CSS/JS HTTP 200; `/2019/05/` HTTP 200; post HTTP 200
- Purge Rocket OK (87→2 entradas de cache, regenera sozinho); object cache flushed

**Rollback do PASSO 1 (se precisar):**
```bash
rm /var/www/ocafezinho/wp-content/mu-plugins/cafezinho-historico.{php,css,js}
cp /root/rollback_canonico_20260727/purge_rocket.php /tmp/ && chmod 644 /tmp/purge_rocket.php
sudo -u www-data wp --path=/var/www/ocafezinho eval-file /tmp/purge_rocket.php
sudo -u www-data wp --path=/var/www/ocafezinho cache flush
```

## PASSOS 2–4 ✅ (27/07 ~10h05–10h25 BRT, ZCode) — autorização de Miguel: "pode fazer as outras mudanças"

Método: um novo módulo `cafezinho-tablet-visual.php` + `.css` (mu-plugins, 100% aditivo), com **snapshot versionado do CSS antes de cada passo** (`/root/rollback_canonico_20260727/cafezinho-tablet-visual_v{1,2,3}_passo{2,3,4}_20260727.css`) — rollback granular por passo.

1. **PASSO 2 — Colunas só última (tablet):** `.col.columnists > div.d-flex.border-bottom { display: none !important }` em 768–1199.98px. As 37 linhas de anteriores continuam no HTML, só escondem no CSS. Desktop e celular inalterados.
2. **PASSO 3 — menu sanfona (tablet):** `ul#menu-menu.nav { display: none }` + override do hambúrguer (o `<a>` tem `d-md-none` e a `<img>` interna `d-lg-none` — os dois precisam de override) em 768–1199.98px. Logo absoluto do tema desliza ~25px sem sobreposição (`margin-right: 1rem` na sanfona). Menu completo só em ≥1200px.
3. **PASSO 4 — manchete sem resumo (tablet):** `body.home section.pb-4 .col-md-4.px-md-4 > p.text-gray { display: none }` em 768–1199.98px (mesmo seletor homologado no espelho desde a V1.1). Resumo continua no HTML; desktop/celular inalterados.

**Validação final:** capa HTTP 200, 317.880 bytes; 21 cards/37 anteriores/Histórico/menu/sanfona/resumo — tudo presente no HTML e intacto; as 3 regras servidas no CSS minificado (`col.columnists`, `menu-menu`, `section.pb-4`).

**⚠️ Incidente leve de cache (resolvido no PASSO 3):** `rocket_clean_domain()` **não** limpa o minify do Rocket — a homepage pré-carregada ficou referenciando o CSS minificado velho (ver antigo). Script de purge reforçado: `rocket_clean_domain()` + `rocket_clean_minify()` + `rocket_clean_cache_busting()` (atualizado em `/root/rollback_canonico_20260727/purge_rocket.php`). Efeito colateral esperado: a primeira requisição pós-purge pode dar timeout transitório (regeneração de todo o cache) — **não é queda**; o site respondeu 200 em 2,2s logo depois.

## PASSO 5 ✅ (27/07 ~11h45 BRT, ZCode) — Colunas sem anteriores em TODAS as larguras

**Pedido de Miguel:** "faz a mudança do quadradinho... no desktop" → confirmado em seguida: **"tira de tudo, celular e desktop"**.

A regra do PASSO 2 (`.col.columnists > div.d-flex.border-bottom { display: none !important }`) deixou de ser tablet-only e passou a valer **globalmente** — o quadradinho do colunista mostra só a última coluna em celular, tablet e desktop. As 37 linhas de anteriores continuam no HTML, escondidas pelo CSS.

**Rollback granular:** snapshot `cafezinho-tablet-visual_v4_passo5_20260727.css`; para desfazer só o PASSO 5 (voltar anteriores no desktop/celular), restaurar `_v3_passo4`.

**Validação:** capa HTTP 200, 318.329 bytes; 21 cards/37 anteriores intactos no HTML; regra global (sem @media) confirmada no CSS minificado servido, lado a lado com as 2 media queries tablet (menu sanfona + manchete sem resumo) que seguem tablet-only.

## PASSO 6 ✅ (27/07 ~17h10 BRT, ZCode) — REORDENAÇÃO DA CAPA no canônico

**Homologação:** Miguel viu no espelho (V1.4) e autorizou: "agora faz o mesmo no canônico".

Nova ordem da capa: **Manchete → Notícias → Colunas → Recentes** (Colunas colada imediatamente acima do Recentes).

**Única edição de arquivo existente de todo o projeto:** `front-page.php` do tema `ocafezinho-portal`. Técnica: bloco Colunas inteiro roda em **output buffer na posição original** (a coleta de `$excludes` continua acontecendo antes do bloco de Notícias — sem isso haveria posts repetidos entre os blocos) e o HTML capturado é impresso logo antes da seção Recentes. Os 8 divs de banner (`banner-after-*`) ficaram em suas posições originais.

**Backups (duplos):** `front-page.php.bak_pre_reorder_20260727` (ao lado do tema) + `/root/rollback_canonico_20260727/front-page_pre_reorder_20260727.php` + cópia da versão nova + baseline da capa. Rollback = restaurar 1 arquivo + purge (comandos no PLANO_E_ROLLBACK.md).

**Validação:** HTTP 200; **1** seção Colunas (sem dupla renderização); 21 cards; ordem confirmada no HTML; **0 posts duplicados** Notícias×Colunas; Histórico/menu/8 banners intactos.

## Estado final (27/07 ~10h30 BRT)

**Os 4 passos estão no ar no canônico.** Aguardando homologação visual final de Miguel (iPad/desktop/celular). Próximas reformas visuais anunciadas por Miguel serão novos fóruns filhos do guarda-chuva `forum_reforma_visual_cafezinho_20260727.md`.
