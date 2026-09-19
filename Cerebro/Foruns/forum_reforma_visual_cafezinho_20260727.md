# Fórum — Reforma Visual do Cafezinho

**Criado:** 27 de julho de 2026, a pedido de Miguel
**Natureza:** fórum **guarda-chuva permanente** de todas as reformas visuais do Cafezinho (capa, tema, responsivo, componentes). Cada empreitada específica tem seu próprio fórum; este aqui é o ponto de entrada, o mapa de credenciais, o protocolo de segurança e o caderno de observações técnicas para facilitar as próximas.

**Fóruns filhos (cronológico):**
- `forum_lab_visual_cafezinho_news_20260720.md` — laboratório visual no espelho cafezinho.news (V1.0–V1.3)
- `forum_deploy_canonico_tablet_historico_20260727.md` — port da V1.3 ao canônico, em 4 passos homologados
- `forum_acesso_ssh_servidor_wp_cafezinho_20260720.md` — acesso SSH ao servidor do canônico

**Manifesto do deploy vigente:** `MANIFESTO_REFORMA_VISUAL_CAFEZINHO_20260727.md`

---

## 🎯 Fluxo de trabalho canônico (aprovado por Miguel)

```
ESPelho (cafezinho.news)  →  homologação visual de Miguel  →  CANÔNICO (ocafezinho.com)
     mexer à vontade              "ah, gostei"               1 passo por vez, com rollback
```

1. Toda mudança visual nasce no **espelho** (`cafezinho.news`), via **mu-plugin aditivo** (tema NUNCA é editado).
2. Miguel homologa visualmente (iPad/desktop/celular).
3. O port ao canônico segue o **Protocolo de Segurança** abaixo, **uma coisa por vez**.

## 🔐 Protocolo de Segurança do Canônico (definido por Miguel, 27/07)

1. **Diagnóstico antes** — estado do servidor, plugins de cache/CDN, markup afetado, baseline da página (curl salvo).
2. **Plano + plano de rollback escritos antes** — gravados em `/root/rollback_canonico_<AAAAMMDD>/PLANO_E_ROLLBACK.md` no servidor e no fórum filho correspondente.
3. **100% aditivo** — nenhum arquivo existente é editado; tudo via mu-plugins NOVOS. Se uma etapa exigir editar algo, backup versionado ANTES.
4. **Rollback de cada passo = apagar os arquivos novos + purgar cache** (comandos exatos no plano).
5. **Uma coisa por vez** — cada passo só avança após OK visual de Miguel.
6. **Purge obrigatório pós-deploy** — WP Rocket + object cache (ver receita em Observações Técnicas §4).
7. **Validação pós-deploy** — curl da capa (HTTP, tamanho vs baseline, marcadores intactos), smoke de CSS/JS/páginas.
8. **Nunca** colar valor de credencial em fórum/chat/código — só ponteiros (Artigo 1 da Constituição do Cafezinho; Dez Mandamentos de Segurança para Agentes, ver `CEREBRO_NODE_COFRE_CHAVES.md`).

## 🗝️ Mapa de credenciais para reforma visual (PONTEIROS — valores NUNCA aqui)

| Recurso | Onde está / como usar |
|---|---|
| **SSH canônico** (us65.serverdo.in) | alias `cafezinho-wp` no `~/.ssh/config` (chave `~/.ssh/id_rsa`); tutorial: `Cerebro/cartoes_bolso/CARTAO_BOLSO_SSH_SERVIDOR_WP_CAFEZINHO.md`; senha root SÓ em `Outros/chaves/ssh_servidor_wp_cafezinho.md` (gitignored) — rotação é dívida ativa desde 28/06 |
| **SSH espelho** (droplet DO) | `ssh root@159.65.177.60` (chave local já autorizada) |
| **Front do espelho** | `https://cafezinho.news` — Basic Auth documentada no fórum do lab |
| **wp-cli canônico** | `sudo -u www-data wp --path=/var/www/ocafezinho` |
| **wp-cli espelho** | `sudo -u www-data wp --path=/var/www/cafezinho-news` |
| **WP REST canônico** | usuário `redacao-nova` (ID 5786, administrator); Application Password no cofre `Outros/chaves/agentes_labs/.env.unificado` (`WP_USER_CAFEZINHO`/`WP_PASS_CAFEZINHO` — rotacionada por Codex em 27/07 04:40, ver `CEREBRO_NODE_ATUALIZACOES.md`); cartão `Outros/chaves/wp_cafezinho_chatbots.md` |
| **DB canônico** | credenciais em `/var/www/ocafezinho/wp-config.php` (ler via SSH) |
| **DB espelho** | senha em `/root/.cafezinho_news_db_pass` (no droplet) |
| **Versões/rollback canônico** | `/root/rollback_canonico_20260727/` (plano, baseline, script de purge) |
| **Versões espelho** | `/root/lab_visual_versoes/` |

## 🛠️ Observações técnicas (o que já quebrou a cabeça — não quebre de novo)

### 1. Método de reforma visual = mu-plugin aditivo
Tema `ocafezinho-portal` NUNCA é editado. CSS/JS/PHP experimental mora em `wp-content/mu-plugins/`. Rollback trivial = apagar os arquivos + purge. O espelho usa `cafezinho-lab-visual.*`; o canônico usa módulos por feature (`cafezinho-historico.*`, etc.).

### 2. `show_on_front` — a pegadinha do espelho
O espelho estava com `show_on_front = posts` e por isso **não renderizava o bloco Colunas** (o `get_field('columnists')` do `front-page.php` ficava sem contexto). Canônico usa `page` (Home estática **ID 156483**, meta `columnists` = 21 IDs de autores, `_columnists` = `field_647d7be8db4c5`). Corrigido no espelho em 27/07.

### 3. www-data NÃO lê /root
Scripts para `wp eval-file` (purge etc.) devem ser copiados para `/tmp` antes — o wp-cli roda como www-data e reporta o erro enganoso `'...' does not exist` quando o arquivo está em /root.

### 4. Cache (canônico): WP Rocket sem CLI
- `wp rocket` **não existe** nesta instalação → purge via `rocket_clean_domain()` em eval-file (script pronto: `/root/rollback_canonico_20260727/purge_rocket.php`, copiar pra /tmp) + `wp cache flush`.
- minify_css=1 e cache mobile separado → purge é **obrigatório** após qualquer deploy de CSS/HTML.
- O cache regenera sozinho (preload); 87 → 2 entradas após purge é normal.

### 5. CDN (serverdoin-cdn 1.4)
Reescreve URLs de assets na saída. Arquivos **novos** dispensam purge (CDN puxa da origem). Edições em arquivo existente cache-bustam sozinhas se o enqueue usar `filemtime()` na query string (sempre usar).

### 6. Sync do espelho (cron `17 * * * *`)
Só faz **upsert** de posts com `post_modified` recente. **Não apaga** posts antigos, **não toca** tema, mu-plugins nem options. Por isso foi possível semear 171 posts reais de 2011–2025 no espelho (Histórico multi-ano) sem risco de sumirem.

### 7. Mapa de seletores da capa (`front-page.php`, canônico = espelho)
| Bloco | Seletor |
|---|---|
| Manchete | `section.pb-4` → `h1` + `p.date` + **`p.text-gray` (o resumo)** + botão `Leia mais` |
| Colunas | `.col.columnists` → card `bg-white rounded p-4` (última coluna) + **2 anteriores** em `div.d-flex.border-bottom.py-4` |
| Matérias | 1ª `section.pb-5` |
| Recentes | 2ª `section.pb-5` → `h4.m-0.text-red` "Recentes" + grade `row-cols-md-4` de 20 posts |
| Menu desktop | `ul#menu-menu.nav.ms-5.d-none.d-md-flex` |
| Hambúrguer | `a[href="#menu"].d-md-none` (**img interna tem `d-lg-none`** — escondida ≥992px!) + offcanvas `#menu.mobile_menu` |
| Variáveis | `--red: #CD152B`, `--black`, `--light-gray` no `:root` do style.css |

### 8. A faixa "tablet/espremido" = 768–1199.98px
O tema usa Bootstrap `md` (768px): iPad retrato cai no layout **desktop espremido** (manchete lado a lado, menu completo quebrado, 4 colunas de cards). Todas as correções de tablet usam `@media (min-width: 768px) and (max-width: 1199.98px)`.

### 9. Transient para consultas pesadas
O Histórico faz `GROUP BY` em ~70k posts — no canônico roda **1x/hora** via transient `cafezinho_historico_html`, invalidado em `save_post`/`deleted_post`/`trashed_post`. Replicar o padrão em qualquer widget derivado de agregação.

### 10. Ruído pré-existente do wp-cli (os DOIS servidores)
O wp-cli imprime o fonte de `wp_bs_pagination()` no stdout em qualquer comando (algum include do tema sem `<?php` que só ecoa em CLI). **Não afeta o site** (HTML sai limpo). Filtrar a saída ao automatizar. Fica registrado como dívida técnica a investigar.

### 11. Baselines (comparar antes/depois)
- **Canônico 27/07:** capa 285KB, 21 cards de colunistas, 37 linhas de anteriores, arquivo 2011–2026 (~70k posts; 2023=10.656, 2026=15.898+), `/root/rollback_canonico_20260727/baseline_capa_antes.html.gz`.
- **Espelho:** só posts de mai–jul/2026 + 171 posts-semente (1/mês de 2011–2025) para testar o Histórico; só 2 dos 21 colunistas têm posts (2018, 5749).

## 📋 Status das reformas

| Reforma | Espelho | Canônico |
|---|---|---|
| Histórico no fim do Recentes | ✅ V1.3 (27/07) | ✅ PASSO 1 (27/07) |
| Colunas só última | ✅ V1.3 (tablet) | ✅ PASSO 2 (tablet) + **PASSO 5: TODAS as larguras** (27/07, "tira de tudo") |
| Menu sanfona (tablet) | ✅ V1.3 | ✅ PASSO 3 (27/07) |
| Manchete sem resumo (tablet) | ✅ desde V1.1 | ✅ PASSO 4 (27/07) |
| Header masthead + pills (V1.1) | ✅ | ❌ sem previsão (Miguel não pediu port) |
| Próximas reformas (Miguel anunciou "várias") | — | — |
| Reordenar capa (Colunas colada acima do Recentes) | ✅ V1.4 (27/07, front-page em buffer) | ✅ PASSO 6 (27/07) — única edição de arquivo existente do projeto (front-page.php, com backup duplo) |

> **Lição de cache (27/07):** purge do Rocket no canônico exige `rocket_clean_domain()` + `rocket_clean_minify()` + `rocket_clean_cache_busting()` — só o primeiro deixa o CSS minificado velho no ar. Script pronto: `/root/rollback_canonico_20260727/purge_rocket.php`.

— Criado por ZCode a pedido de Miguel, 2026-07-27
