# MEMÓRIA — Selo Cafezinho Media Group na rede + Aplicativos no site do grupo (05/08/2026)

**Data:** 2026-08-05 10:50→11:20 BRT · **Agente:** ZCode/Kimi K3
**Fórum irmão:** `Foruns/forum_selo_cafezinho_media_group_20260805.md`

## 1. Endereços e acessos (mapa usado)

- **Espelho cafezinho.news:** droplet DO `159.65.177.60` (SSH root:22, chave local), WP em `/var/www/cafezinho-news/`, Basic Auth front `cafezinho/000`.
- **Canônico ocafezinho.com:** SSH alias `cafezinho-wp` (us65.serverdo.in, 190.89.239.65:51439), WP em `/var/www/ocafezinho/`, WP Super Cache ATIVO (`advanced-cache.php` + `wp-content/cache/`).
- **Media Group:** repo `migueldorosario1/cafezinhomediagroup` (Astro 1 página) → Vercel `cafezinhomediagroup.vercel.app`. Identidade git do repo: `Miguel do Rosario <migueldorosario1@gmail.com>` (clone novo não herda — configurar local).
- **Moka Reader:** `ZCodeProject/igot`, branch local `mokavideo` → upstream `moka/main` (repo `migueldorosario1/moka`); remote `origin`=igot (espelho). Push nos DOIS: `git push moka mokavideo:main` + `git push origin mokavideo:main` (rebase antes se o outro agente adiantar a main).
- **8 temáticos:** `Projeto Cafezinho Agentes/sites-v4/<site>` (Footer.astro; aiatolah = `layouts/Layout.astro`).

## 2. Implementações

### 2.1 Selo nos 8 temáticos
Script idempotente: div `.group-tag` antes do `</footer>` + CSS antes do `</style>`; texto PT ("Um portal do") ou EN ("Part of the") conforme `language` do config. Validação: `astro build` local em ceara e aiatolah antes dos 8 pushes.

### 2.2 Espelho WP (cafezinho.news)
`wp-content/mu-plugins/cafezinho-media-group-selo.php` — hook `wp_footer` pri 99, echo de div inline-styled (11px, cinza #8a8a8a, borda pontilhada no link, safe-area-inset-bottom). 100% aditivo; rollback = apagar. Cópia local: `/tmp/cafezinho-media-group-selo.php`.

### 2.3 Moka Reader
- `apps/web/src/lib/ui-strings.ts`: nova chave `footer_group` na união de tipos + 12 traduções (PT "Um portal do" · EN "Part of the" · ES "Parte del" · FR "Un portail du" · DE "Ein Portal der" · IT "Un portale del" · RU "Входит в" · ZH "所属集团：" · JA "運営グループ：" · KO "운영 그룹:" · AR "ضمن" · HI "समूह:") — inseridas após `footer_feedback` em cada bloco (script por marcador de idioma).
- `SiteFooter.tsx`: `<p className="site-footer-group">` após o link de feedback + CSS (11px, muted, dotted). `tsc --noEmit` 0 erros + `next build` OK.

### 2.4 Media Group — seção Aplicativos
`index.astro`: `<section class="apps-section">` entre o grid de portais e o `</main>`, card do Moka Reader (https://www.mokareader.com) com badge "App · Grátis · 12 idiomas", ícone livro SVG, slogan e descrição BYOK. CSS próprio em `global.css` (`.app-card` espelha `.portal-card`; NÃO usar portal-card — o JS de filtros varre essa classe globalmente e esconderia o card sem data-lang). Build OK, no ar.

## 3. Verificação ao vivo (11:15-11:20)

selo=1 em: ceara.digital, riocarta.com, mundotrilhos.com, mapario.com.br, globalsouth.news, discoverbrazil.news, railpost.news, aiatolah.com, cafezinho.news, mokareader.com. Apps section no cafezinhomediagroup.vercel.app. (Domínios canônicos vêm do `site_url` de cada config — .com.br/.news variam; não chutar.)

## 4. Plano canônico (pendente ordem do Miguel)

Registrado em `CEREBRO_NODE_AGENDA_LEMBRETES.md` (05/08 tarde): copiar mu-plugin → flush Super Cache → verificar → rollback documentado.
