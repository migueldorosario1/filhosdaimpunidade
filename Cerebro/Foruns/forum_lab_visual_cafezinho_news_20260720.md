# Fórum — Lab Visual do Espelho cafezinho.news

**Data:** 20 de julho de 2026
**Escopo:** experimentos de redesign visual **somente no espelho** `cafezinho.news` (droplet DO NYC3 `159.65.177.60`). O canônico `ocafezinho.com` (`us65.serverdo.in`) permanece **intocado**.
**Relacionado:** `forum_exercicio_copia_cafezinho_news_20260629.md` (criação do espelho), `forum_acesso_ssh_servidor_wp_cafezinho_20260720.md` (acesso SSH ao canônico).

## Premissa

Miguel decidiu usar o espelho como **laboratório visual**: testar mudanças de aparência antes de qualquer decisão sobre o canônico. Nada do que está aqui sobe para produção sem homologação explícita.

## Acessos do laboratório

| Recurso | Valor |
|---|---|
| SSH | `ssh root@159.65.177.60` (porta 22, chave local já autorizada) |
| Front-end | `https://cafezinho.news` — Basic Auth `cafezinho` / `000` |
| WP path | `/var/www/cafezinho-news/` |
| wp-cli | `sudo -u www-data wp --path=/var/www/cafezinho-news` |
| Banco | `cafezinho_news` (senha em `/root/.cafezinho_news_db_pass`) |
| Sync horário | ATIVO (cron `17 * * * *`) — **não toca** tema nem mu-plugins; posts/uploads/`wp_highlights` são sobrescritos |

## Implementação (mu-plugin, tema intacto)

- `wp-content/mu-plugins/cafezinho-lab-visual.php` — enfileira o CSS (prioridade 100)
- `wp-content/mu-plugins/cafezinho-lab-visual.css` — os estilos do lab
- **Rollback total:** apagar os 2 arquivos
- **Versionamento:** `/root/lab_visual_versoes/` no droplet (cópia local em `/tmp/cafezinho-lab/versoes/` na máquina de Miguel — volátil, droplet é a referência)
  - `cafezinho-lab-visual_v1.0_20260720.css`
  - `cafezinho-lab-visual_v1.1_20260720.css` ← ativa
  - `menu_backup_v1.0_20260720.json` (menu antes da reestruturação)

## Changelog

### V1.0 (20/07, ~14h BRT)

1. **Bug da logo no iPad corrigido:** o tema aplicava `position: absolute; height: 100px` à logo a partir de 768px (`style.css:146-152`), derrubando-a por cima do menu. Logo voltou ao fluxo (56px mobile / 72px desktop).
2. **Menu em pills:** links de texto viraram botõezinhos arredondados (fundo cinza-claro, hover vermelho com elevação).
3. **Tipografia fluida:** `clamp()` nos títulos (fim do salto seco em 768px) + correção da hierarquia invertida do tema (h3 era maior que h2) + `text-wrap: balance`.
4. **Footer moderno:** bloco escuro com faixa vermelha, logo em cartão branco, ícones sociais em fichas redondas, CTA "Apoie" em pill vermelho.

### V1.1 (20/07, ~17h BRT) — pedido de Miguel após ver V1.0 no iPad

1. **Cabeçalho reformulado (masthead de 2 linhas):** linha 1 = logo à esquerda + busca/Apoie/sociais à direita; linha 2 = pills centralizadas ocupando a largura toda. Faixa vermelha de marca no topo do header. Fim do vazamento/quebra no iPad.
2. **Menu reestruturado (via wp-cli):**
   - `Política` → renomeado para **Nacional** (item 154833)
   - **Eleições 2026** e **Economia** viraram submenus de Nacional
   - **Regional** agora tem os **26 estados + DF** em ordem alfabética (20 categorias novas criadas no espelho, IDs 20958–20977; itens de menu posteriormente reparados após B-SYNC-001)
   - Menu de topo ficou com 5 itens: Quem somos?, Nacional▾, Regional▾, Geopolítica, Tecnologia
3. **iPad (768–1199px):** resumo da manchete escondido — capa fica só com título + data + botão Leia mais.
4. **Dropdowns roláveis** (`max-height: 70vh`); dropdown do Regional em grade de 2 colunas em telas ≥992px.

### V1.2 (20/07, ~18h BRT) — pacote de modernização da página de post

1. **Botões de compartilhar** (AddToAny): redondos, dessaturados em repouso, cor e elevação no hover.
2. **Thumbs da sidebar** (Recentes): cantos arredondados (12px) + sombra leve.
3. **"Siga-nos no Google News"**: de bloco cinza para pill com borda, hover vermelho.
4. **Corpo do artigo**: medida de leitura confortável (`max-width: 70ch`, `line-height: 1.75`).

### V1.3 (27/07, ~08h15 BRT, ZCode) — pedido de Miguel: formato "espremido" (iPad) + Histórico

1. **Correção de ambiente (não-visual):** o espelho estava com `show_on_front = posts` e por isso **nunca renderizou o bloco Colunas** (o `get_field('columnists')` do `front-page.php` não achava contexto). Ajustado para `page` (página estática "Home" ID 156483), igualando o canônico. Bloco Colunas passou a renderizar no espelho (2 cards — só os autores 2018 e 5749 têm posts sincronizados no espelho; no canônico são 21 colunistas).
2. **iPad/tablet (768–1199.98px): menu vira hambúrguer.** As pills do menu (`ul#menu-menu`) somem nessa faixa e aparece o botão de três linhas (offcanvas), igual ao celular. Menu completo só em ≥1200px. (O resumo da manchete já sumia nessa faixa desde a V1.1 — mantido.)
3. **iPad/tablet: card de colunista mostra SÓ a última coluna.** As 2 colunas anteriores (`div.d-flex.border-bottom` dentro de `.col.columnists`) ficam `display: none` na faixa 768–1199.98px — eram elas que estouravam o quadradinho. Desktop e celular inalterados.
4. **NOVO — "Histórico" no fim do bloco Recentes:** link vermelho que expande painel com o **arquivo do site por ano → mês** (links `/AAAA/MM/` com contagem de posts). Implementado no mu-plugin: PHP imprime o painel no `wp_footer` (só na capa, `is_front_page()`), JS (`cafezinho-lab-visual.js`, novo 3º arquivo) move o painel para o fim da seção Recentes e liga os toggles. Ano corrente abre expandido. No espelho aparece só 2026 (mai–jul, retenção do sync); no canônico listará todos os anos.
5. **Arquivos/rollback:** `cafezinho-lab-visual.php` + `.css` atualizados, `.js` criado. Backups pré-V1.3 e cópias V1.3 em `/root/lab_visual_versoes/` (`*_v1.3_20260727.*`, `*_v1.2_20260720.php`, `*_v1.2_20260720_ativa_pre_v13.css`). Rollback continua: apagar os 3 arquivos de mu-plugins.
6. **Pendente homologação de Miguel no iPad** antes de qualquer port para o canônico.
7. **Complemento (27/07, ~08h40 BRT):** a pedido de Miguel ("o histórico tem que ter de outros anos"), semeados **171 posts reais do canônico no espelho** — 1 post por mês de 2011–2025 (`mysqldump` do `wp_posts` com IDs originais, zero colisão; o sync horário só faz upsert de `post_modified` recente, não apaga esses posts). Motivo: o espelho só tinha posts de mai–jul/2026 e o painel mostrava só 2026. Agora o Histórico do espelho lista **2011–2026** (16 anos). Contagens no espelho são de amostra (1–12/ano); no canônico serão as reais (arquivo real: 2011=226 … 2023=10.656 … 2026=15.898+).

### V1.4 (27/07, ~16h50 BRT, ZCode) — REORDENAÇÃO DA CAPA + colunas global

1. **Bloco Colunas desce para imediatamente antes do Recentes** (pedido de Miguel). Nova ordem da capa: Manchete → Notícias → **Colunas** → Recentes. Implementado no `front-page.php` do espelho: o bloco inteiro (queries + HTML) roda em **output buffer na posição original** — assim a coleta de `$excludes` continua acontecendo antes do bloco de Notícias (zero posts duplicados entre os blocos, validado) — e o HTML capturado é impresso logo antes da seção Recentes. **Primeira edição de tema do espelho** (até aqui só mu-plugin); backups: `front-page.php.bak_pre_reorder_20260727` (ao lado do tema) + `/root/lab_visual_versoes/front-page_pre_reorder_20260727.php` e `front-page_reorder_v1.4_20260727.php`.
2. **Colunas sem anteriores vira GLOBAL no espelho** (regra 3d perdeu o @media) — espelha o PASSO 5 já homologado e no ar no canônico ("tira de tudo, celular e desktop"). Versão: `cafezinho-lab-visual_v1.4_20260727.css`.
3. **Validação:** ordem Manchete → Notícias → Colunas → Recentes confirmada no HTML; 1 só seção Colunas (sem dupla renderização do buffer); 0 posts duplicados entre Notícias e Colunas; Histórico intacto.
4. **Pendente homologação de Miguel** — se aprovado, o port ao canônico será uma edição do `front-page.php` DE LÁ com backup prévio (não dá para fazer reorder 100% aditivo sem JS com flash de reposicionamento).

### 🐛 B-SYNC-001 — Colisão de IDs entre criação local e sync horário (20/07, corrigido)

**Sintoma:** 4 "pills fantasmas" (itens vazios) no menu e 12 estados sumiram do submenu Regional horas após a V1.1.

**Causa raiz:** menu items são posts (`nav_menu_item`). O `AUTO_INCREMENT` do `wp_posts` do espelho (262365) anda **na mesma faixa** dos IDs dos posts novos do prod. O sync horário importa posts do prod com `REPLACE INTO` — posts vindos do prod **sobrescreveram 8 itens de menu** criados localmente e corromperam 4. Confirmado: IDs 262342–262345 viraram posts/attachments do prod ("Brasil terá 158,7 milhões de eleitores...", `ig-cropped-image-179`).

**Cura estrutural (impede repetição):**
```sql
ALTER TABLE wp_posts AUTO_INCREMENT = 400000;        -- prod em ~262k, margem de anos
ALTER TABLE wp_terms AUTO_INCREMENT = 100000;        -- prod em ~21k
ALTER TABLE wp_term_taxonomy AUTO_INCREMENT = 100000;
```
**Reparo do menu:** fantasmas 262341/262347/262348/262349 apagados; 12 estados re-adicionados com `--title` explícito (novos IDs ≥400001); posições normalizadas 100–126 em ordem alfabética. Validação: 0 itens vazios no nav, 27 estados renderizados.

**Lição para o port da madrugada:** no canônico não existe esse risco (é a origem dos IDs). A correção de AUTO_INCREMENT é exclusiva do espelho. **Qualquer criação futura de conteúdo local no espelho (menus, páginas de teste) herda automaticamente IDs seguros a partir de agora.**

## Validação

- Screenshots headless (Chrome CDP) em 820×1180 (iPad) e 390×844 (mobile): header integrado, pills OK, título da manchete completo e balanceado, sem estouro horizontal (`scrollWidth` = viewport; únicos elementos fora da tela são o offcanvas do menu mobile, comportamento padrão do Bootstrap).
- 29 `dropdown-item` no HTML (27 UFs + Eleições 2026 + Economia).
- Home 200, CSS servido com versionamento por `filemtime`.

## Riscos / pendências conhecidas

- **Categorias de estados criadas só no espelho** estão vazias (0 posts) até o prod criar categorias homônimas — o sync importa `wp_terms` com `REPLACE INTO`, então as locais sobrevivem; colisão de ID só se o prod criar termo com o mesmo ID (remoto, registrado).
- **Sync horário não leva o menu nem as categorias novas para lugar nenhum** — mudanças são 100% locais do espelho.
- O canônico continua com o visual antigo: nada foi propagado (de propósito).
- wp-cli no espelho cospe lixo PHP de um plugin (função `wp_bs_pagination` impressa em toda saída) — usar `| tail -n1` ao capturar IDs. Candidato a investigação futura.

## Próximos passos possíveis

1. Miguel avalia V1.1 no iPad físico → ajustes finos (V1.2).
2. Se homologado: portar mudanças para o canônico (processo separado, com backup e janela de manutenção).
3. Dívida ativa de sempre: rotação da senha do ServerDo.in (28/06).

---

— Registrado por Kimi (ZCode), 2026-07-20.

---

# 📎 ANEXO — Análise de viabilidade do port para o canônico (20/07 ~18h BRT)

**Pedido de Miguel: SOMENTE ANÁLISE, nada foi alterado no canônico.** Reconhecimento feito por SSH read-only (`ssh cafezinho-wp`).

## Achados do reconhecimento (read-only)

| Item | Estado no canônico |
|---|---|
| WP path | `/var/www/ocafezinho` (WP 7.0.2, tema `ocafezinho-portal` ativo) |
| Tema vs espelho | drift **mínimo**: prod só tem divs extras de ads (`banner-top-*`, `banner-bottom-*`, `banner-video-sticky-desktop`) e ~15 linhas de CSS de ads. **Todos os seletores do lab V1.1 existem idênticos no prod** |
| Menu | **IDs idênticos** ao estado pré-V1.1 do espelho (Política=154833, Eleições=229818, Regional=161555, Economia=154834 etc.) — os mesmos comandos wp-cli funcionam |
| Categorias de estados | prod tem as mesmas 9 que o espelho tinha; as 20 novas precisariam ser criadas lá também (mesmo script) |
| REST API | pública 200; credencial `Redator` + Application Password existe (`Outros/chaves/wp_cafezinho_chatbots.md`) |
| JWT plugin | ativo mas **mal configurado** (`jwt_auth_bad_config`) — irrelevante, App Passwords funcionam |
| WP Rocket | **minify_css=1**, cache mobile separado → `wp rocket clean` **obrigatório** após deploy de CSS |
| CDN | plugin `serverdoin-cdn` ativo → avaliar purge de CDN |
| Segurança | Wordfence ativo (não interfere com deploy via SSH); UpdraftPlus ativo (ponto de restauração trivial) |

## Veredito

**Viável e de risco baixo via SSH + wp-cli** — mesma receita do espelho (mu-plugin aditivo, sem editar tema). A REST API cobriria só ~30% (cria categorias, mas não gerencia menu clássico nem instala mu-plugin) → não serve sozinha.

Bônus: se o menu/categorias forem mudados no prod, o sync horário propaga para o espelho sozinho (nav_menu_items entram no delta; terms vão com REPLACE) — os dois convergem.

## Plano de port (quando Miguel homologar — NÃO executar antes)

1. Ponto de restauração (UpdraftPlus ou tar+mysqldump)
2. scp dos 2 arquivos do mu-plugin para `/var/www/ocafezinho/wp-content/mu-plugins/`
3. Script de menu (mesmos IDs) + criação das 20 categorias
4. `wp rocket clean` (+ purge CDN ServerDo se aplicável)
5. Validar iPad/mobile/desktop
6. Rollback = `rm` dos 2 arquivos + restaurar menu do backup JSON (< 5 min)

Estimativa: 30–40 min com validação. Janela de baixo tráfego recomendada.

---

## Port ao canônico V2.0 (09/08/2026, Claude a pedido de Miguel) — **APENAS "Coluna do Editor"**

**Escopo:** port cirúrgico de UMA feature do lab do espelho (V1.5 "Coluna do Editor", feita ~14:30 BRT hoje) para o canônico `ocafezinho.com`. Miguel viu o resultado no espelho, aprovou ("ficou perfeito"), autorizou aplicar no canônico ("mas faz com muito cuidado, pelo amor de Deus"). Plano gravado em `plano_coluna_editor_canonico_20260809.md` antes da execução.

**Escopo NÃO feito hoje:** o pacote V1.1 inteiro (menu pills + iPad hambúrguer + histórico + tablet visual + tipografia fluida etc.) permanece como plano acima, aguardando homologação separada.

### O que mudou (2 arquivos)

**1. `wp-content/themes/ocafezinho-portal/front-page.php`**

- Substituição CIRÚRGICA do bloco Colunas dentro do `ob_start()` (mesmo padrão do REFORMA VISUAL PASSO 6 de 27/07):
  - Query antiga (`get_field('columnists')` → 21 colunistas) trocada por `WP_Query` com `author=2018 posts_per_page=4 post_status=publish`
  - HTML antigo (2 col mobile / 4 col desktop + scroll horizontal + 3 posts por card com avatar/nome/2 extras) trocado pelo layout novo (1 col mobile visível + 4 col md+ empilhadas via `d-none d-md-block` nos cards 2/3/4, cada card com só thumb+título+data)
  - Cabeçalho novo: xicrinha (`img/cafezinho.svg`) + `get_avatar(2018, 48)` + "Coluna do Editor" em vermelho + "Miguel do Rosário" logo abaixo
- **Preservados**:
  - `ob_start()` (linha 35) e `ob_get_clean()` (linha 135)
  - 2 divs `banner-after-manchete-*` dentro do buffer (linhas 59-60)
  - 2 divs `banner-after-colunistas-*` depois do buffer (linhas 137-138)
  - `array_push($excludes, get_the_ID())` — os 4 posts do Miguel continuam sendo excluídos da seção Recentes (sem duplicata)
  - Comentário histórico "REFORMA VISUAL — PASSO 6" (não apaguei — deixa a linhagem visível)

**2. `wp-content/mu-plugins/cafezinho-avatar-openid.php` (novo, 40 linhas)**

- Filter `get_avatar_url` que substitui o mystery man do Gravatar pela meta `moopenid_user_avatar` (foto do Google Photos herdada do login OpenID). Genérico — vale para qualquer autor que tenha essa meta preenchida.
- **Não** traz o `cafezinho-lab-visual.{php,css,js}` inteiro do espelho. Só o filter de avatar isolado, sem CSS/JS.

### Backups (redundância tripla)

STAMP: `20260809_164909` · hash pré-mudança: `c839c1109dbde74213d49786c42fc54d43e3f27bd5986eab80a8be6e2c6f0c9b`

1. `/var/www/ocafezinho/wp-content/themes/ocafezinho-portal/front-page.php.bak_pre_coluna_editor_20260809_164909` (droplet, ao lado do arquivo)
2. `/root/coluna_editor_canonico_versoes/front-page_pre_coluna_editor_20260809_164909.php` (droplet, versionado)
3. `/tmp/cafezinho_canonico_20260809/front-page.php.bak_TRIPLE` (máquina local Miguel)

Cópia da versão nova em `/root/coluna_editor_canonico_versoes/front-page_coluna_editor_v1.0_canonico_20260809_164909.php` + `cafezinho-avatar-openid_v1.0_canonico_20260809.php`.

### Rollback pré-instalado (antes da mudança)

- Script `/root/coluna_editor_canonico_versoes/rollback_coluna_editor_canonico.sh` (uma linha `bash` restaura tudo)
- Doc manual `/root/coluna_editor_canonico_versoes/rollback_MANUAL.md`
- Script já testado no espelho (mesmo padrão da casa)

### Verificação (Fase 4)

- HTTP 200 · 191830 bytes · 1,65s
- `grep "Coluna do Editor"` = 2 · `grep "coluna-editor-item"` = 4 · `grep "coluna-editor-section"` = 1
- Avatar: `https://lh6.googleusercontent.com/-Rug7ADZIEqY/…/photo.jpg?sz=48` (foto real do Miguel, não mystery man) ✅
- 4 cards renderizados com os 4 posts mais recentes do Miguel:
  1. Milei volta a atacar Lula nas redes (MOBILE-VISIVEL)
  2. Líder do governo Milei culpa Lula pela crise mas implora por volta de embaixador
  3. Quaest mostra Lula firme do primeiro ao segundo turno e aprovação estável
  4. Bolsonaristas ressuscitam, com fúria, a campanha antivacina
- Miguel confirmou visualmente: "eu vi aqui. ficou bom."

### O que NÃO precisou (nesta rodada)

- **WP Rocket cache flush:** mudei PHP do tema, não CSS — WP Rocket não minifica PHP. Home apareceu corretamente sem purge (Miguel confirmou "ficou bom" ~5 min após o deploy).
- **serverdoin-cdn purge:** mesma razão. Se aparecer versão stale pra algum leitor, avisar Miguel pra purge manual.
- **Restauração UpdraftPlus:** backup triplo do arquivo é suficiente; nenhuma alteração de DB/plugin ativo.

### Timeline

- 17:20 BRT plano gravado
- 17:48-17:50 Fase 0 descoberta read-only via alias `cafezinho-wp`
- 17:49 Fase 1 backup triplo com hash-check
- 17:50 Fase 5 rollback script pré-instalado
- 17:55 Fase 2 edição bloco Colunas + upload + PHP lint OK
- 17:56 Fase 3 mu-plugin avatar OpenID + upload + PHP lint OK
- 17:58 Fase 4 verificação curl + confirmação visual Miguel
- 18:20 Fase 6 registro neste fórum

**Total: ~30 min ponta a ponta, zero incidente, zero rollback necessário.**
