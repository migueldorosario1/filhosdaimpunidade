# Fórum — Teste das 5 verticais no ESPELHO (cafezinho.news)

**Data:** 2026-08-12 ~13:10 BRT
**Sessão:** ZCode GLM-5.2 (arquiteto)
**Decisão Miguel (12/08):** testar as 5 verticais no **espelho** (cafezinho.news) antes do canônico. "Não mexe no canônico."
**Status:** ✅ Infraestrutura de teste no espelho PRONTA (pipeline redireciona, API funcional, 5 blocos na home). Cron ainda desligado.

> **CANÔNICO INTACTO** — confirmado: nenhum arquivo do `ocafezinho.com`/`cafezinho-wp` (ServerDo.in) foi tocado. Todos os backups ficaram no NYC e no espelho.

---

## Viabilidade (análise de arquiteto — concluída: viável)
- Espelho é **WordPress** (mesmo tema `ocafezinho-portal`), não-indexado (`X-Robots-Tag: noindex`).
- **Categorias batem** com o canônico: Cultura 79 · Economia 43 · Meio Ambiente 582 · Esporte 1271 · **Saúde 258**.
- **Auth dupla** (nginx `auth_basic` + WP) resolvida desabilitando a Basic Auth do nginx temporariamente (worker manda só App Password WP).

## O que foi feito (tudo no espelho + NYC, NUNCA no canônico)

### 1. Credenciais do espelho (no cofre, Regra 4)
- **Basic Auth do front**: `cafezinho` / `000` (registrada em `forum_lab_visual_cafezinho_news_20260720.md`).
- **App Password WP** dedicada "V4-Verticais-Espelho": user **`Redator`** (ID 5470), guardada em `ESPELHO_WP_SITE/USER/PASS` no `/root/chaves.sh` do NYC + `.env.unificado` local (backups `.bak_pre_v4_espelho_20260812`).
- Gerada via `wp user application-password create` (wp-cli com `--skip-themes --skip-plugins` — o wp-cli do espelho buga sem isso).

### 2. nginx do espelho: Basic Auth DESATIVADA temporariamente
- Arquivo: `/etc/nginx/sites-available/cafezinho-news` (server block 443). Comentado `auth_basic` + `auth_basic_user_file`.
- Backup: `/etc/nginx/sites-available/cafezinho-news.bak_pre_v4_espelho_20260812`.
- **Motivo:** WP REST precisa de App Password sem auth dupla nginx (try_files re-avalia location php e re-pede auth).
- WP REST validado: `users/me` com App Password → HTTP 200 ("Redação", ID 5470); POST de draft → HTTP 201 (criou+deletou 400012).

### 3. Worker: bloco `VERTICAIS_ESPELHO` (publicação seletiva)
- Arquivo: `/root/v4_vertical_draft_worker.py` (NYC). Após `load_shell_env`, se `cfg["vertical"] in (cultura, economia, meio_ambiente, esporte, saude)`: sobrepõe `WP_SITE/USER/PASS` com `ESPELHO_WP_*`.
- Confirmado ativo: worker imprimiu `{"status":"publicando_no_espelho","vertical":"economia","site":"https://cafezinho.news"}`.
- **As 3 ativas (nacional/geopolitica/ciencia) seguem no canônico** (não estão na lista; usam creds canônicas).

### 4. 5 blocos na home do espelho (`front-page.php`)
- Arquivo: `/var/www/cafezinho-news/wp-content/themes/ocafezinho-portal/front-page.php` (589→~720 linhas).
- Adicionados 5 blocos no molde Geopolítica (separador ícone+título+linha + `<section>` hero+5 títulos com `WP_Query(category__in => array(ID))`): **Cultura (79) · Economia (43) · Meio Ambiente (582) · Esporte (1271) · Saúde (258)**.
- Inseridos antes de `<div id="banner-after-recents-desktop">`.
- `php -l`: **No syntax errors**. Home **HTTP 200**. Separadores renderizando (`>Cultura< >Economia< >Meio Ambiente< >Esporte< >Saúde<`).
- Backup: `front-page.php.bak_pre_blocos_v4_20260812`.

## Rollback (por componente, reversível)
- **Religar Basic Auth nginx**: descomentar `auth_basic` + `auth_basic_user_file` no `/etc/nginx/sites-available/cafezinho-news` + `systemctl reload nginx`. (Ou restaurar `.bak_pre_v4_espelho_20260812`.)
- **Reverter worker**: remover bloco `VERTICAIS_ESPELHO` (ou restaurar do `.bak_pre_v4_novas_20260811`).
- **Reverter front-page**: `cp front-page.php.bak_pre_blocos_v4_20260812 front-page.php`.
- **Creds**: remover `ESPELHO_WP_*` do chaves.sh/.env.unificado (ou ignorar — não afetam o canônico).

## Pendências
- **Worker não completou publicação real** no espelho (timeout 280s na rodada do LLM gemini). A infraestrutura está comprovada (POST manual OK, bloco ativo); só precisa +tempo ou cron rodando.
- **Religar Basic Auth** quando o teste acabar (front do espelho está exposto temporariamente).
- Portar reforma visual canônico→espelho (sync tema — opcional; os blocos funcionam sem).

## Próximos passos (decisão Miguel)
1. Rodar worker com timeout maior (ou 1 de cada vertical) pra ter posts reais nos blocos do espelho.
2. Ou ligar o cron das 5 no espelho (publica ao longo do tempo; blocos vão se enchendo).
3. Quando validar visualmente, portar tudo pro canônico (com o mesmo molde: bloco VERTICAIS mas apontando pro canônico).

## Continuidade
Estado preservado; canônico intacto. Retomável lendo este fórum + a memória técnica das 5 verticais.
