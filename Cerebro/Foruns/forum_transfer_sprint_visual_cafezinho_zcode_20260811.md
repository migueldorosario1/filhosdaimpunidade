# Fórum de Transferência — Sprint Visual Cafezinho para ZCode

**Data de abertura:** 2026-08-11, 07:15 BRT
**Autor:** Claude Code (Anthropic, `claude-opus-4-7`)
**Destinatário principal:** ZCode (Kimi K3 / GLM 5.2 / Qwen 3.8)
**Motivo:** Miguel decidiu 11/08/2026 07:12 BRT transferir a condução do sprint de reforma visual (espelho `cafezinho.news` + canônico `ocafezinho.com`) pro ZCode.
**Status:** ATIVO — documento vivo, atualizar conforme sprint avança

---

## 1. Objetivo do sprint

Reforma visual completa do site O Cafezinho — testando primeiro no espelho `cafezinho.news` (ambiente lab, atrás de HTTP Basic Auth) e portando decisões validadas pro canônico `ocafezinho.com` (produção, milhares de leitores diários, monetizado via Google Ad Manager).

Miguel escolhe o design final visualmente no espelho; ZCode implementa e depois porta. Trabalho iniciado 10/08/2026 pela madrugada, contínuo desde então. Já tem 15+ iterações aplicadas ao espelho e nenhum port ainda pro canônico.

---

## 2. Acessos e credenciais

### 2.1 SSH

**Alias `~/.ssh/config` já configurados na máquina do Miguel:**

- **`cafezinho-wp`** — canônico ocafezinho.com
  - Host: `us65.serverdo.in` (IP variável, resolvido pelo DNS ServerDo.in)
  - User: root
  - Chave: `~/.ssh/id_ed25519` (padrão)
  - Web root: `/var/www/ocafezinho/`
  - Tema: `/var/www/ocafezinho/wp-content/themes/ocafezinho-portal/`
  - mu-plugins: `/var/www/ocafezinho/wp-content/mu-plugins/` (17 arquivos ativos)
  - Cache: WP Rocket + serverdoin-cdn (não purgar sem autorização Miguel)

- **`root@159.65.177.60`** — espelho cafezinho.news
  - Host direto por IP: `159.65.177.60` (Digital Ocean)
  - User: root
  - Chave: `~/.ssh/id_ed25519` (mesma padrão)
  - Hostname interno: `cafezinho-news-espelho`
  - Web root: `/var/www/cafezinho-news/`
  - Tema: `/var/www/cafezinho-news/wp-content/themes/ocafezinho-portal/` (mesmo nome do tema do canônico, arquivos SIMILARES mas com iterações do lab visual aplicadas)
  - mu-plugins: `/var/www/cafezinho-news/wp-content/mu-plugins/` (inclui `cafezinho-lab-visual.*` legado + `cafezinho-lab-ad-calhau.php` v1.1 criado no sprint)
  - Não tem cache aparente (nginx + PHP-FPM direto)

**Não há alias configurado pro espelho** — usar `root@159.65.177.60` explicitamente. Se ZCode quer criar alias `cafezinho-news`, adicionar em `~/.ssh/config`.

### 2.2 HTTP Basic Auth do espelho

Espelho está protegido:
- Arquivo htpasswd: `/etc/nginx/.htpasswd_cafezinho`
- User em produção: `cafezinho` (senha só Miguel sabe — hash APR1 `$apr1$I7x1qCTI$...`)
- **Método pra ZCode testar HTTP sem pedir senha ao Miguel:** adicionar user temporário via `htpasswd`/`openssl passwd -apr1`, testar, remover. Padrão usado por Claude no sprint:

```bash
ssh root@159.65.177.60 '
HASH=$(openssl passwd -apr1 "senha_temp_apagar")
echo "claudetest_temp:$HASH" >> /etc/nginx/.htpasswd_cafezinho
# ... testes curl ...
sed -i "/^claudetest_temp:/d" /etc/nginx/.htpasswd_cafezinho
'
```

### 2.3 WordPress / DB (via wp-load ou mysql)

Tanto canônico quanto espelho usam MySQL. Credenciais em `wp-config.php` de cada instalação:
- Canônico: `/var/www/ocafezinho/wp-config.php`
- Espelho: `/var/www/cafezinho-news/wp-config.php`

Extrair credenciais programaticamente (padrão que uso — evita bugs de escape de quotes):
```bash
DBU=$(awk -F"'" "/DB_USER/{print \$4; exit}" wp-config.php)
DBP=$(awk -F"'" "/DB_PASSWORD/{print \$4; exit}" wp-config.php)
DBN=$(awk -F"'" "/DB_NAME/{print \$4; exit}" wp-config.php)
```

**Cuidado:** `wp-cli` no canônico tende a poluir stdout com o conteúdo do `wp_bs_pagination()` (arquivo pagination.php do tema). Uso `php` chamando `wp-load.php` diretamente + `grep -v` pra filtrar, OU MySQL direto. Deixei código pronto em vários exemplos nos arquivos `/tmp/adiag*.php` do canônico.

### 2.4 Publisher IDs de ads

- **Google Ad Manager (DFP) canônico:** `21622511100`
- **Google AdSense legado (Colabs):** `ca-pub-5835338445130243`

Detalhes completos: [[reference-ads-canonico-ocafezinho-arquitetura-real]] na memória Claude.

---

## 3. Estado atual do espelho (11/08/2026 08:00 BRT)

### 3.1 Home (`front-page.php`)

```
1. MANCHETE (post 0 destaque)
2. banner-after-manchete-desktop/mobile (calhau, se reveza por breakpoint)
3. COLUNA DO EDITOR (4 posts do autor 2018 Miguel, 3 breakpoints:
   - mobile <768px: scroll horizontal 1 card por vez
   - iPad vertical 768-991px: grid 2×2 fixo
   - desktop ≥992px: scroll horizontal 2 cards por vez)
4. banner-after-colunistas-desktop/mobile (calhau)
5. NACIONAL (destaque + 4 laterais, category__in=[22, 43])
6. GEOPOLÍTICA (foto hero + 5 títulos, category__in=[5003])
7. CIÊNCIA E TECNOLOGIA (foto hero + 5 títulos, category__in=[30, 19936])
8. LINHA DO TEMPO (timeline vertical hora a hora, sem filtro categoria)
9. banner-after-latest-desktop/mobile (calhau)
10. RECENTES (grid 4×5, offset dinâmico via post__not_in $excludes)
11. banner-after-recents-desktop/mobile (calhau)
```

Cada bloco temático faz `array_push($excludes, get_the_ID())` em cada loop pra evitar post repetir entre blocos.

### 3.2 Single post (`single.php`)

- Post ocupa `col-12 col-lg-8` (100% no iPad vertical/mobile; 8/12 no desktop)
- Sidebar tem `d-none d-lg-block` (some no iPad vertical e mobile, aparece só desktop)
- `banner-lateral-tablet` (slot novo criado no sprint, só visível 768-991px, placeholder no espelho)
- Todos slots `banner-*` do canônico reproduzidos como calhau: before-content, article-bottom, before-comments, after-comments, after-related, after-recents

### 3.3 Includes ad/*

**Fiel ao canônico** (11/08 07:53 BRT): `ad/_top.php` e `ad/_middle.php` estão comentados (`<!--<section>...-->`) — igual canônico. Espelho NÃO renderiza mais `banner-top` (extra) nem `banner-middle`. Só os pares `-desktop`/`-mobile` que revezam.

### 3.4 Mu-plugin `cafezinho-lab-ad-calhau.php` v1.1

- CSS `<style>` injetado em `wp_head` que aplica visual calhau a todos `.ad-space` e `[id^="banner-"]`
- v1.1 (11/08 05:34 BRT) tem RESET explícito: por padrão TODOS escondidos, cada `@media` reativa só o correspondente ao breakpoint. Evita empilhamento de placeholders.
- **NUNCA portar pro canônico** — CSS `.desktop-ad-space {display:none!important}` esconderia ads reais.

### 3.5 Total de slots de ad reproduzidos como calhau no espelho

**21 IDs únicos**, fiéis ao canônico:
- Header: banner-top-desktop, banner-top-mobile (+ include _top.php comentado)
- Front-page: after-manchete, after-colunistas, after-latest, after-recents (todos com -desktop/-mobile)
- Sidebar: before-sidebar-desktop, after-sidebar-desktop, banner-sidebar (sticky)
- Single: before-content, article-bottom, before-comments, after-comments, after-related, after-recents (com sufixos) + banner-lateral-tablet (novo)
- Footer: video-sticky-desktop, bottom-desktop, bottom-mobile
- Index (categorias/arquivo/tags): after-category-desktop, after-category-mobile

---

## 4. Rollbacks empilhados (14 níveis, todos com script pronto no droplet)

Cada mudança tem seu rollback em `/root/<slug>_20260811/rollback.sh` no droplet do espelho:

1. `blocos_variantes_20260811/rollback_blocos_variantes.sh` — remove os 4 blocos originais (base do sprint)
2. `reorder_blocos_scroll_editor_20260811/rollback.sh`
3. `coluna_apos_manchete_20260811/rollback.sh`
4. `coluna_8_quadrados_20260811/rollback.sh`
5. `coluna_6_3x2_20260811/rollback.sh`
6. `coluna_4_2x2_20260811/rollback.sh`
7. `coluna_swipe_desktop_20260811/rollback.sh` — 3 breakpoints coluna editor
8. `remove_bloco_canonico_20260811/rollback.sh`
9. `blocos_categorias_20260811/rollback.sh`
10. `single_1col_ipad_20260811/rollback.sh`
11. `banner_realocado_tablet_20260811/rollback.sh`
12. `ads_calhau_20260811/rollback.sh` — **restaura tema INTEIRO via tar.gz** (SHA `dc99994981...`)
13. `ads_manchete_e_css_robusto_20260811/rollback.sh` — banner-after-manchete + CSS v1.1
14. `comentar_ad_includes_20260811/rollback.sh` — comenta _top e _middle igual canônico

**Rollback máximo (volta ao estado 100% pré-sprint):** `bash /root/ads_calhau_20260811/rollback.sh`

---

## 5. Arquitetura de ads do canônico (crítica pra port seguro)

**Motor principal:** Google Ad Manager (DFP) via plugin `ad-inserter`.

- Publisher ID: `21622511100`
- Ad paths tipo `/21622511100/cafezinho_post/cafe_mobile_1..6`
- **90 blocos configurados no ad-inserter, 36 ATIVOS**
- Storage: `wp_options.ad_inserter`, formato `:AI:<base64>(serialize PHP)` (49KB)
- Decodificação: `$data = @unserialize(base64_decode(substr($raw, 4)));`

**Descoberta CRÍTICA (11/08 07:30 BRT):** os 36 blocos ativos do ad-inserter:
- ❌ Zero usam `custom_css_selector`
- ❌ Zero usam `automatic_insertion` com paragraph_number
- ❌ Zero referenciam IDs `banner-*` do tema

**Consequência:** mudanças visuais no tema (mover Coluna do Editor, adicionar blocos temáticos, esconder sidebar em iPad, remover bloco canônico) **NÃO afetam** os ads ativos, porque ad-inserter não tem dependência da estrutura HTML do tema.

**Divs GAM** (`CafeMobile-1..6`) são criados pelo próprio HTML dos blocks (via `googletag.display()`), não são elementos do tema.

**Outros plugins de ads:**
- Quick AdSense 2 — insere `adsbygoogle` DENTRO dos posts (Beg/Midd/End)
- Colabs AdSense — legado, 2 slots (`ca-pub-5835338445130243`, 728x90 e 468x60)

**Formatos ativos observados** (screenshots Miguel 11/08 06:17):
1. In-article banners (Quick AdSense)
2. Header banners (GAM)
3. Home meio (GAM)
4. Anchor sticky mobile (com ✕)
5. Interstitial fullscreen (Block 11 GAM Interstitial — "ACESSE MEU SUS DIGITAL")
6. Discovery Native ("Conteúdo Promovido")
7. Google Funding Choices (Block 32 — CMP LGPD)

Neste momento (11/08), majoria dos ads = campanhas institucionais SUS/Ministério da Saúde sobre vício em apostas online. Comerciais reais (Verisure, Betnacional Fortune Tiger regulamentado) apareceram no Discovery.

**Auditoria: NUNCA usar `curl` puro pra checar ads.** Ad-inserter injeta via JS depois do HTML carregar. Usar browser headless (Puppeteer, Playwright) ou análise dos scripts injetados.

---

## 6. Riscos destrutivos identificados

### 🔴 CRÍTICO — NUNCA fazer

- Editar `wp_options.ad_inserter` sem backup DB (zera 36 blocks GAM)
- Desativar plugin ad-inserter (para todos GAM)
- Desativar Quick AdSense 2 (para ads in-article)
- Editar/deletar Colabs AdSense (legado ativo)
- Portar mu-plugin `cafezinho-lab-ad-calhau.php` pro canônico (CSS esconderia ads reais)
- Renomear divs `CafeMobile-1..6` no canônico

### 🟡 MÉDIO — cuidado

- Editar functions.php do tema
- Mudar `<head>` (onde carrega gpt.js)
- Mexer em qualquer mu-plugin do canônico sem entender função
- Purgar cache WP Rocket / serverdoin-cdn sem autorização Miguel

### 🟢 BAIXO — pode fazer com backup

- Mudanças visuais no tema (front-page.php, single.php, sidebar.php, header.php, footer.php, index.php, page.php)
- Adicionar novos slots com IDs próprios
- CSS puro que não altere `display` dos divs de ad

---

## 7. Bugs conhecidos anotados

Arquivo: `Cerebro/monitoramento_horario/lab_visual_bugs/bugs_2026-08-11.jsonl`

- **LV-20260811-001** — FALSO POSITIVO: URLs `/category/*/` são 404 em ambos (correto: Yoast SEO `stripcategorybase=true` — URL real é `/slug/` direto)
- **LV-20260811-002** — banner-after-manchete faltando no espelho — CORRIGIDO
- **LV-20260811-003** — CSS calhau empilhando 2 ads — CORRIGIDO (v1.1)
- **LV-20260811-004** — ad/_top.php e _middle.php descomentados no espelho vs comentados no canônico — CORRIGIDO (comentados no espelho pra ficar fiel)

---

## 8. Regras editoriais / contratos vigentes

Miguel opera com Claude em modo cirúrgico, disciplinado por várias regras cristalizadas em memory files:

- **`feedback_modo_enxuto_preservar_worker_v4.md`** — Contrato editorial assinado 11/08 05:29 BRT: worker V4 traz texto bom, Claude só corrige bugs objetivos e ajusta título; PROIBIDO reescrever prosa, empilhar `<strong>`, `;`, parágrafos longos, H2 novos, aspas literais adicionadas. Contrato formal em `Cerebro/Foruns/contrato_claude_modo_enxuto_vigilia_v5_20260811.md`.
- **`feedback_canonico_port_do_espelho_cirurgico.md`** — 6 fases pra portar do espelho ao canônico: (0) descoberta read-only, (1) backup triplo SHA-256, (5) rollback pré-instalado, (2) edição cirúrgica preservando ads/comentários, (3) mu-plugin isolado com nome DIFERENTE do lab do espelho, (4) verificação HTTP + grep, (6) registro no fórum lab visual.
- **`feedback_lab_visual_anotar_bugs_seguranca_port_canonico.md`** — todo bug do lab visual anota em `Cerebro/monitoramento_horario/lab_visual_bugs/bugs_YYYY-MM-DD.jsonl`.
- **`feedback_url_categoria_cafezinho_e_slug_direto_sem_prefixo.md`** — URLs de categoria são `/slug/` direto, não `/category/`.
- **`reference_ads_canonico_ocafezinho_arquitetura_real.md`** — arquitetura completa dos ads.
- **`project_lab_visual_cafezinho_news_20260811.md`** — memory-índice com os 14 rollbacks empilhados.

---

## 9. Pendências pro ZCode (o que precisa ser decidido/feito)

### 9.1 Curto prazo

- **[decisão Miguel] Portar reforma visual pro canônico** — em ETAPAS incrementais ou tudo de uma vez? Recomendação minha: etapas (Coluna Editor primeiro, blocos temáticos depois, single 1 col por último). Cada etapa com 6 fases cirúrgicas.
- **[decisão Miguel] Unificar categorias `Tecnologia (30)` com `Ciência e Tecnologia (19936)` no DB** — Miguel disse "podemos juntar bota um bloco com as duas, depois a gente junta oficialmente". Bloco já usa `category__in=[30, 19936]`. Unificação oficial via `wp term merge` ou UPDATE `wp_term_relationships` fica pra depois.
- **[investigação pendente]** Decodificar blocos ad-inserter 7-90 (36 ativos, meu regex só pegou os 6 primeiros mais o Interstitial 11 e consent 32). Ver ad-inserter blocks 8, 9, 10, 12, 13-31, 33-96 pra mapear cada slot GAM completo.
- **[investigação pendente]** Testar renderização do canônico via browser headless (Puppeteer/Playwright) pra ver quais divs GAM realmente populam. `curl` puro não vê ads.

### 9.2 Médio prazo (se Miguel quiser)

- **Ativar slots `<div id="banner-*">` do tema no canônico** — hoje ficam vazios. Se Miguel quiser começar a monetizar essas posições (banner-top-desktop, banner-after-manchete, etc.), configurar ad-inserter apontando pra esses IDs + criar ad units no Google Ad Manager.
- **Corrigir URLs `/category/*/`** — hoje quebradas em ambos (bug herdado do WP + Yoast). Se ativar, fazer no espelho primeiro.
- **Registro cronológico completo** — Miguel sugeriu ao Claude criar um fórum detalhado das 12+ iterações com screenshots ASCII antes/depois de cada uma. Claude ofereceu 3 formatos (fórum cronológico, manifesto final, guia de estilo) — Miguel ainda não escolheu.

---

## 10. Como o ZCode deve continuar o sprint

1. **Leia este fórum inteiro primeiro.** Se algo faltar, perguntar a Miguel via `inbox_trindade/claude.md` (deixa Claude ver a pergunta) OU direto pra Miguel via chat.
2. **Não portar nada pro canônico sem plano MD antes.** Mostrar plano a Miguel pra aprovação, aplicar as 6 fases cirúrgicas.
3. **Toda mudança no espelho — mesmo pequena — vai pra `lab_visual_bugs/bugs_YYYY-MM-DD.jsonl`.** Padrão de anotação já usado por Claude nesse arquivo. Se identificar bug pré-existente que não seja da reforma visual, marcar `origem: pre_existente`.
4. **Auditoria mínima após cada mudança:** PHP lint em todos arquivos do tema + mu-plugins, HTTP status home + single + página categoria, grep em logs (nginx error, PHP-FPM error, WP debug).
5. **Manter contrato modo enxuto** se ZCode também opera Vigília V5 editorial (mas Miguel pode ter comunicado outra coisa ao ZCode diretamente).
6. **Rollback pré-instalado antes de tocar em produção.** Padrão: bash script no droplet + doc MD + backup triplo (droplet + versionado + local).

---

## 11. Referências e links úteis

- **Memory Claude MEMORY.md (índice):** `~/.claude/projects/-home-migueldorosario-Downloads-Antigravity-Google/memory/MEMORY.md`
- **Contrato editorial:** `Cerebro/Foruns/contrato_claude_modo_enxuto_vigilia_v5_20260811.md`
- **Bugs lab visual JSONL:** `Cerebro/monitoramento_horario/lab_visual_bugs/bugs_2026-08-11.jsonl`
- **Fóruns relacionados:**
  - `forum_lab_visual_cafezinho_news_20260720.md` (lab anterior)
  - `forum_reforma_visual_cafezinho_20260727.md`
  - `forum_deploy_canonico_tablet_historico_20260727.md`
  - `MANIFESTO_REFORMA_VISUAL_CAFEZINHO_20260727.md`
  - `forum_exercicio_copia_cafezinho_news_20260629.md` (histórico do espelho)

---

## 12. Cabeçalho de resposta esperado do ZCode

Quando ZCode assumir o sprint, favor responder em `inbox_trindade/claude.md` com tag `[ZCODE-ACEITE-SPRINT-VISUAL-CAFEZINHO-<slug>]` contendo:

- (a) Modelo que pegou a cartinha (GLM 5.2 / Kimi K3 / Qwen 3.8 — proveniência)
- (b) Aceite ou dúvidas antes de aceitar
- (c) Primeiro passo planejado (proposta ao Miguel)

---

## Assinatura

**Claude Code** (Anthropic, `claude-opus-4-7`)
Sessão: `-home-migueldorosario-Downloads-Antigravity-Google`
Timestamp: 2026-08-11 08:15 BRT

_Transferência de sprint aberta. Continuo disponível pra dúvidas via chat direto do Miguel ou via cartinha em `inbox_trindade/claude.md`._
