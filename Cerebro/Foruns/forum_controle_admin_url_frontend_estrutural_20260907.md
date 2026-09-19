# 🔗 FÓRUM — Cura estrutural do "controle.ocafezinho.com" no HTML público (07/09/2026)

**Ordem do Miguel (07/09 ~17:2x):** "Não pode ter link controle na frente. Consertou também estruturalmente."
**Autor:** ZCode Dell (ZM, Qwen3.8-Max) · **Status:** ✅ CONCLUÍDO E PROVADO — home com 0 ocorrências de `controle.ocafezinho.com`, ajaxUrl público, HTTP 200.
**Tema Duplo:** memória `controle-admin-url-frontend-cura-estrutural-20260907.md`.

## 1. Estado anterior (o que o Miguel viu)

- **3 posts da série Vorcaro/Nikolas (269245/269246/269247):** URLs de imagem apontando para `controle.ocafezinho.com` no post_content — **corrigidos pela sessão Kimi K3** (16:1x–16:3x, wp-cli + override da trava editorial; readback 0 ocorrências — **re-verificado pelo ZM às 17:1x: 0 nos 3**).
- **HTML PÚBLICO ainda vazava controle:** a home renderizava `var WP_Statistics_Tracker_Object = {... "ajaxUrl":"https://controle.ocafezinho.com/wp-admin/admin-ajax.php" ...}` — para TODO visitante anônimo.

## 2. Causa raiz (prova em runtime)

`admin_url()` devolvia controle enquanto `site_url()` devolvia www. Reflection apontou: **plugin `serverdoin-cdn/rewrite.php`** registrava `add_filter('admin_url', 'new_admin_url')` **incondicionalmente** — a função reescreve toda URL de admin do domínio principal (www) para o domínio publicador (controle), sem distinguir contexto. Efeito colateral: o ajaxUrl do WP Statistics (que usa `admin_url('admin-ajax.php')`) saía controle em TODA página pública. O plugin é da arquitetura do CDN ServerDoIn (publicador=controle p/ operações admin) — o filtro só faz sentido em contexto admin, não no front público.

## 3. Cura (mínima, com backup)

1. **Backup:** `rewrite.php.bak_pre_adminurl_front_20260907`.
2. **Patch (1 bloco):** o filtro agora só é registrado em contexto admin/preview/host-publicador ou usuário logado (barra de admin preservada para editores). Página pública anônima = `admin_url` 100% www. ⚠️ Incidente intermediário registrado com honestidade: a 1ª versão do guard chamava `is_user_logged_in()` na carga do plugin — fatal (pluggable ainda não carregado) por ~2 min; curado na hora com `function_exists('is_user_logged_in') &&`. `php -l` OK.
3. **Prova:** `admin_url('admin-ajax.php')` em contexto público = `https://www.ocafezinho.com/wp-admin/admin-ajax.php`; purga Redis + WP Rocket (rocket_clean_domain/clean_home); **home com 0 `controle`**, ajaxUrl público, HTTP 200.
4. **Endurecimento de banco:** options `siteurl`/`home` no DB ainda apontavam `http://controle.ocafezinho.com` (bomba-relógio — as constantes `WP_SITEURL`/`WP_HOME` do wp-config as mascaravam em runtime). Corrigidas via SQL p/ `https://www.ocafezinho.com` + flush do object cache (as constantes seguem valendo; agora o fallback do DB é consistente).
5. **Não mexido (by design, não vaza):** `cafezinho-force-rest-url-controle-v2.php` (mu-plugin do fix Yoast — só reescreve REST em contexto admin/controle) e a opção `serverdoin-cdn-setup` (config do CDN).

## 4. Estado

- **Aconteceu:** links dos 3 posts ✓ (Kimi + re-verificação ZM), vazamento estrutural do admin_url ✓ (ZM), siteurl/home do DB ✓, caches purgados ✓, home provada limpa ✓.
- **Falta:** nada pendente deste tema. Vigilância natural da ronda (o sweeper da Kimi varre datas; a ronda VIGIA-BG segue de 2/2h).
- **Preciso de você:** nada — só o seu OK quando conferir a home.
