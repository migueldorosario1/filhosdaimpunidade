# Memória — Deploy canônico V1.3 (tablet + Histórico) — 2026-07-27

**Fórum par:** `Foruns/forum_deploy_canonico_tablet_historico_20260727.md` (decisões e validações completas)
**Fórum relacionado:** `Foruns/forum_lab_visual_cafezinho_news_20260720.md` (homologação no espelho)

## Log técnico

### Contexto
Miguel homologou no espelho cafezinho.news (V1.3) e autorizou o port ao canônico com protocolo rígido: diagnóstico → plano → rollback → backups → 1 passo por vez (Histórico → Colunas → menu sanfona → resumo manchete), cada um só após OK visual dele.

### PASSO 1 executado (27/07 ~09h00 BRT) — Histórico no canônico

**Servidor:** us65.serverdo.in (`ssh cafezinho-wp`) · WP path `/var/www/ocafezinho`

**Arquivos criados (nenhum existente tocado):**
- `wp-content/mu-plugins/cafezinho-historico.php` — enqueue CSS/JS (só `is_front_page()`), painel impresso no `wp_footer`, **transient 1h** `cafezinho_historico_html` invalidado em save_post/deleted_post/trashed_post
- `wp-content/mu-plugins/cafezinho-historico.css` — estilos `.cz-hist*` (var(--red) do tema)
- `wp-content/mu-plugins/cafezinho-historico.js` — move painel pro fim da seção Recentes (`h4.text-red` "Recentes" → closest section → .container-xxl; fallback última section.pb-5) + toggles ano/mês

**Plano/rollback/backups no servidor:** `/root/rollback_canonico_20260727/`
- `PLANO_E_ROLLBACK.md` (plano completo dos 4 passos + log)
- `baseline_capa_antes.html.gz` (capa antes: 284.962 bytes)
- `purge_rocket.php` (script de purge — **copiar pra /tmp antes de rodar**: www-data não lê /root e wp-cli roda como www-data; erro enganoso do wp-cli: "does not exist")

**Cache:** WP Rocket ativo sem CLI → `rocket_clean_domain()` via wp eval-file + `wp cache flush`. CDN serverdoin reescreve URLs na saída (sem purge necessário pra arquivos novos).

**Validação:** capa 318.145 bytes (+33KB); 16 anos / 179 links mensais / contagens reais (2023=10.656 ✓); colunistas e manchete intactos; CSS/JS/arquivo/post 200.

### PASSO 6 (27/07 ~17h10 BRT) — Reordenação da capa no canônico

Homologado no espelho (V1.4) e autorizado por Miguel ("agora faz o mesmo no canônico"). **Única edição de arquivo existente do projeto:** `front-page.php` do tema. Bloco Colunas roda em `ob_start()` na posição original (preserva a coleta de `$excludes` ANTES do bloco de Notícias — sem duplicados) e o HTML é ecoado imediatamente antes da seção Recentes (`$cafezinho_colunas_html`). Nova ordem: Manchete → Notícias → Colunas → Recentes. Os 8 divs `banner-after-*` ficaram nas posições originais. Backups: `.bak_pre_reorder_20260727` ao lado do tema + 2 cópias em `/root/rollback_canonico_20260727/` + baseline da capa. Validação: 1 seção Colunas, 21 cards, 0 duplicados Notícias×Colunas, Histórico/menu/banners intactos, HTTP 200.

### PASSO 5 (27/07 ~11h45 BRT) — Colunas sem anteriores em TODAS as larguras

Pedido de Miguel ("tira de tudo, celular e desktop"): a regra `.col.columnists > div.d-flex.border-bottom { display:none !important }` perdeu o `@media (min-width:768px) and (max-width:1199.98px)` e virou **global**. Snapshot `cafezinho-tablet-visual_v4_passo5_20260727.css`; desfazer só o PASSO 5 = restaurar `_v3_passo4`. Menu sanfona e manchete sem resumo seguem **tablet-only** (Miguel não pediu para estendê-los).

### PASSOS 2–4 executados (27/07 ~10h05–10h25 BRT) — autorização Miguel: "pode fazer as outras mudanças"

**Módulo novo (mu-plugins, 100% aditivo):** `cafezinho-tablet-visual.php` (loader global, filemtime) + `cafezinho-tablet-visual.css`. Snapshot versionado do CSS antes de cada passo em `/root/rollback_canonico_20260727/cafezinho-tablet-visual_v{1,2,3}_passo{2,3,4}_20260727.css`.

1. **PASSO 2:** `.col.columnists > div.d-flex.border-bottom { display:none !important }` @ 768–1199.98px — anteriores ficam no HTML, escondem no CSS.
2. **PASSO 3:** `ul#menu-menu.nav { display:none }` + `header .container-xxl > a[href="#menu"] { display:block !important; margin-right:1rem }` + override da img `d-lg-none` @ 768–1199.98px. Tema: logo absoluto em ≥768 (style.css:133-139) desliza sem sobrepor.
3. **PASSO 4:** `body.home section.pb-4 .col-md-4.px-md-4 > p.text-gray { display:none }` @ 768–1199.98px (body class="home" confirmado no canônico, page-id-156483).

**⚠️ Incidente de cache (resolvido):** após o PASSO 3, a homepage servida seguia referenciando o CSS minificado velho (`?ver=` antigo): `rocket_clean_domain()` **não** limpa `cache/min/1/`. Purge correto = `rocket_clean_domain()` + `rocket_clean_minify()` + `rocket_clean_cache_busting()`. Script atualizado em `/root/rollback_canonico_20260727/purge_rocket.php`. Também observado: timeout transitório na 1ª requisição pós-purge (regeneração geral) — não é queda (site respondeu 200 em 2,2s em seguida).

**Validação final:** capa 317.880 bytes; 21 cards/37 anteriores/Histórico/menu/sanfona/resumo intactos no HTML; 3 regras vivas no CSS minificado servido (`col.columnists`, `menu-menu`, `section.pb-4`).

### PASSOS 2–4 (pendentes, aguardando OK de Miguel)

### Lições
1. **www-data não lê /root** — scripts de manutenção pro wp-cli devem ir pra /tmp (ou /var/www) antes de rodar.
2. Espelho estava com `show_on_front=posts` (nunca renderizou Colunas até 27/07); canônico é `page` (Home ID 156483, meta `columnists` com 21 autores).
3. Sync do espelho (cron :17) só faz upsert de `post_modified` recente — não apaga posts antigos (permitiu semear 171 posts de 2011–2025 no espelho pro Histórico mostrar todos os anos).
4. Baseline do canônico: 21 cards de colunistas, 37 linhas de colunas anteriores, arquivo 2011–2026 (~70k posts).

— ZCode, 2026-07-27
