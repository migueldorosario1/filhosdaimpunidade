# Memória técnica — Banner KUBET revezando com MOKA (Cafezinho) — 14/09/2026

**Autor:** ZCode/GLM-5.3 · **Fórum gêmeo:** `Foruns/forum_banner_kubet_revezamento_moka_20260914.md`

## 1. Origem do pedido

Miguel (chat CLI 14/09 ~18:0x, áudio + pasta `Outros/pautas editoriais o cafezinho/Dia a dia/bet/` com `image (1).png` 351×141, logo KUBET, fundo azul-marinho opaco rgb≈(5,25,57)): achar lugar vazio no Cafezinho pro anúncio sem trepar em outro. Segundo pedido (~18:1x): "no mesmo lugar do MOKA, mas revezando com ele".

## 2. Inventário de anúncios do site (investigação)

- **Home (front-page.php):** slots `banner-top` (desktop/mobile), `after-manchete`, `middle`, `after-colunistas`, `after-latest`, `after-recents`, `video-sticky`, `bottom` — TODOS vazios no HTML servido (os que "têm IMG" são só placeholder `icon-start.svg`/logo outline ou conteúdo editorial vizinho detectado pelo parser). Único anúncio real: `#moka-banner-home` (728×90 + 300×250 iframe).
- **Single (single.php):** mesma malha + `before-content`, `advertisement-after-support`, `article-bottom`, `before/after-sidebar`, `sidebar` (sticky), `before-comments`, `after-comments` (ambos VAZIOS — o "embaixo dos comentários"), `after-related`. Único anúncio real: `.cafezinho-moka-single` (mu-plugin).
- **Zero AdSense/GAM/taboola** no HTML público non-AMP. CSS do tema: `.desktop-ad-space`/`.mobile-ad-space` alternam por media query (desktop ≥992px, min-height 90/100px). Comentário do style.css: slots são placeholders vazios no non-AMP; "ads reais usam divs GAM via ad-inserter em /amp/".
- **Mecanismo MOKA:** HTML autocontido em `wp-content/moka-banners/moka-{728x90,300x250}-pt.html` + iframe apontando direto. Origem dos iframes: front-page.php (src direto) e mu-plugin `cafezinho-moka-single.php` (filtro the_content prio 25, entra antes do aside da newsletter).
- **Plugins relevantes ativos:** wp-rocket, redis-cache, ad-inserter (só AMP), serverdoin-cdn, wordfence. Gate da casa: `cafezinho-gate-apostas-emenda11.php` (posts com padrão de funil de afiliado viram page — banner estático não passa por save_post).

## 3. Implementação

### 3.1 Arquivos criados (`/var/www/ocafezinho/wp-content/banners-cafezinho/`, www-data 755/644)

- `kubet-logo.png` — image (1).png do Miguel (scp + mv).
- `kubet-728x90.html` / `kubet-300x250.html` — criativo: fundo `#051939` (cor média das bordas da logo, emenda invisível), `<img>` centrada (82px de altura no 728×90; 300px de largura no 300×250), link `https://thbku.bet/` `target=_blank rel="nofollow sponsored noopener"`, selo `+18` 9px canto inferior direito. SEM frase de funil (coerência Emenda 11).
- `rotator-728x90.html` / `rotator-300x250.html` — `<script>var P_KUBET=0.5; location.replace(Math.random()<P_KUBET ? kubet : moka)</script>` + `<noscript><meta refresh → moka>`. Sorteio no CLIENTE: imune ao cache de página (cada pageview sorteia). Proporção ajustável num único lugar.

### 3.2 Edições (backup `.bak_pre_kubet_revezamento_20260914` antes; `php -l` OK)

- `wp-content/themes/ocafezinho-portal/front-page.php` (iframes do `#moka-banner-home`): `content_url('/moka-banners/moka-728x90-pt.html')` → `content_url('/banners-cafezinho/rotator-728x90.html')` (idem 300×250); `title="Moka Reader"` → `title="Publicidade"`.
- `wp-content/mu-plugins/cafezinho-moka-single.php`: mesmas 2 trocas.
- Cache: `rm -rf wp-content/cache/wp-rocket/*` (948MB; `wp rocket purge` não registrado no wp-cli deste servidor — Registrar? menor).
- Cloudflare: HTML é `cf-cache-status: DYNAMIC` (não cacheia) — nada a purgar.

## 4. Provas (todas em 14/09 ~18:2x-18:4x)

1. curl 200: 5/5 arquivos em `https://www.ocafezinho.com/wp-content/banners-cafezinho/`.
2. HTML público: home e single com `rotator-728x90/300x250` nos iframes.
3. Browser real (IAB): home — leitura `iframe.contentWindow.location.href` pós-lazyload: 24 sortes válidos → KUBET 13 × MOKA 11 (≈50/50; 1 leitura "rotator ainda" = replace em andamento, imperceptível).
4. Screenshots auditados por visão: MESMO slot com KUBET (azul-marinho, coroa dourada + KUBET, +18) e com MOKA (laranja, "Qualquer livro ou vídeo resumido em 2 minutos", CTA mokareader.com) — alternância comprovada visualmente, sem sobreposição/empilhamento.
5. Single: 5 cargas → MOKA, KUBET, MOKA, MOKA, MOKA.
6. Artefatos locais: `~/.zcode/cli/artifacts/sess_eb4d1417.../call_0d4dc785...png` (KUBET home), `call_3cd2ee34...png` (MOKA home).

## 5. Aprendizados / receitas

- **Rotator client-side é o padrão ouro para revezamento em site com cache de página** (WP Rocket): rotação por pageview no servidor morre no cache; no cliente sobrevive.
- Pegadinha de captura no IAB: `screenshot({clip})` não bate com `getBoundingClientRect()` medido antes (layout shift do lazyload + escala do pane); para prova visual, capturar viewport INTEIRA e localizar o banner na imagem.
- `wp rocket purge` não registrado neste WP (wp-cli) — limpar `wp-content/cache/wp-rocket/*` direto é o fallback instantâneo.
- curl de prova SEM `-L` no ocafezinho.com pega só o redirect 301 (corpo quase vazio) — sempre `-sL`.
- Slots vazios do tema NÃO são "espaço desperdiçado a ocupar às cegas": a regra viva do front-page é 1 anúncio por intervalo — o revezamento no slot MOKA cumpre sem tocar na regra.

## 6. Pendências

- Nenhuma técnica. Opcionais: `P_KUBET` ≠ 0,5; criativo KUBET nativo 728×90 (logo atual fica pequena no leaderboard); revezo no AMP (fora de escopo — lá usam GAM/ad-inserter).
- Aviso regulatório dado ao Miguel (offshore não licenciado × Resolução SPA 1.315/2025) — decisão editorial é dele.
- Rollback: restaurar os 2 `.bak` + (opcional) `rm -rf banners-cafezinho/`.
