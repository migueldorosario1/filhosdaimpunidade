# Fórum — INCIDENTE: hack do cafezinho.news (espelho 159.65.177.60) — 13/09/2026

**Ref:** ZM-20260913-HACK · **Autor:** ZCode/GLM-5.3 · **Status:** CONTENÇÃO CONCLUÍDA ~16h1x BRT (19h1x UTC), site recuperado e no ar. Reconstrução limpa do espelho recomendada (pendente Miguel).

## 1. Resumo executivo

- O domínio **cafezinho.news** (espelho, droplet DO `159.65.177.60`, hostname `cafezinho-news-espelho`) foi desfigurado por "**Ind3xZer0 and Anarchy Security Brazillian Team**".
- **O canônico (us65, ocafezinho.com) NÃO foi tocado** — auditado ao vivo: blogname correto, zero contas novas 10-13/09, zero plugins suspeitos, PHP modificados são todos da casa.
- Intrusão inicial: **14/08/2026 12:33 UTC** (webshells plantados). Dano visível só em 12-13/09 (contas + deface). O atacante teve **1 mês de acesso** como www-data.

## 2. O que foi encontrado (tudo backupado antes de remover)

| Artefato | Detalhe |
|---|---|
| Webshell ×2 | `wp-content/plugins/ps_2b31ca/` e `ps_26929a/` — POST com senha sha256 `27c23fcb…99591` → `shell_exec` arbitrário como www-data. Criados 14/08 12:33. Funcionam por URL direta mesmo "inactive". |
| Miner ×2 | `/var/tmp/.xd/.x` e `/tmp/sv` — MESMO binário ELF estático 32MB stripped (cryptominer). Desde 14/08 e 21/08. |
| Watchdog | `/var/tmp/.xd/.watch` + crontab do www-data com `@reboot` + `*/5min` (4 linhas). |
| Proxy aberto | `gost -L socks5://fleet:F1eetPass!@:38081` — porta escutando no mundo desde 09/09 (relay de terceiros). |
| Contas atacantes (13/09) | `kacak`, `steven27`, `wp_service_708090`, `Hoxxymexs`, `wp_admin_81642e` (12-13/09, e-mails descartáveis yopmail/mailinator/fastmessage/emalupe + timing do deface). Deletadas com segurança. |
| ⚠️ RETIFICAÇÃO (contas da casa) | As contas técnicas `w2s_*` (~19), `wp2_*` (7), `yun_11` (5786 — citada como "publicação interna wp-cli/cron" no mu-plugin `cafezinho-origem-post.php`), `ngx_33` e `id69_a22872` eram **da casa** (esteira de recortes; recado de 08/09 na ponte: «não o hash w2s_… do teste»), e FORAM DELETADAS por cautela durante o incidente ativo. **100% restauráveis do dump forense** `wp_users_usermeta_full.sql`. Fluxo que as usava estava PAUSADO desde 11/09 (agente YouTube) — nada quebrou na hora. Restaurar quando religar a esteira, ou reconstruir o espelho (recomendado). Consequência colateral: 3.328 posts com autor dessas contas foram reassigados p/ James2017 (2018) — muitos eram reassig em massa FEITO PELO ATACANTE (as queries sqlmap dele manipulavam exatamente post_author), mas os recortes legítimos da casa também estavam nesse lote; byline fina se resolve com a reconstrução/sync do canônico. |
| Deface | `blogname`/`blogdescription` no banco + template FSE "Página inicial do blog" (wp_template ID 401401 + revision 401402, criados 12/09 10:52) com HTML de hack inteiro. |
| Posts contaminados | 6 `oembed_cache` com sufixo ` — Ind3xZer0 Quer cafe Admin kkkkk` colado nos atributos alt/title das imagens (em-dash UTF-8). Nenhum post real de matéria foi alterado. |

## 3. Contenção executada (13/09 15:4x-16:1x BRT (18:4x-19:1x UTC))

1. **Backup forense integral** em `/root/forense_hack_20260913/` (binários dos 3 processos copiados de /proc, tgz dos webshells/artefatos, dumps SQL: wp_users+usermeta completo, wp_options completo, posts contaminados, crontab www-data, snapshots ps/ss, MD5SUMS).
2. Kill dos processos `.x`, `sv`, `gost` + remoção de `/var/tmp/.xd`, `/tmp/sv`, `/tmp/.axs`.
3. Remoção dos webshells `ps_2b31ca`/`ps_26929a`.
4. Remoção do crontab inteiro do www-data (4 linhas maliciosas; backup no forense).
5. `blogname`/`blogdescription` restaurados com os valores exatos do canônico.
6. Template do deface (401401+401402) deletado com --force → tema voltou a renderizar a home.
7. REPLACE SQL (charset utf8mb4) limpou os 6 oembed_cache — contagem Ind3xZer0/Anarchy no banco = **0**.
8. `wp config shuffle-salts` — todas as sessões/cookies invalidados (inclusive do atacante).
9. xmlrpc.php bloqueado no nginx (`location = /xmlrpc.php { return 403; }`); brute externo POST → 403 comprovado. Backup da config em `/etc/nginx/backups_pre_edit/` (🔴 .bak fora de sites-enabled — lição da casa re-aplicada após tropeço próprio).
10. Deleção das ~35 contas do atacante (`--reassign=2018`); degradação para subscriber das ambíguas `cafezinho`(5814) e `augustoevercode`(5744, 2022).
11. `wp cache flush`.

**Provas:** home externa 200, título "O Cafezinho – Portal de noticias…", grep Ind3xZer0/hacked = 0; REST posts normal; porta 38081 fechada; nenhum processo www-data suspeito.

## 4. Avaliação de gravidade

- **Alcance:** SÓ o espelho (www-data). Sem evidência de escalada root: nada em /root alterado, authorized_keys intacto (2 chaves = MESMA chave Dell; login "estranho" 142.93.48.252 às 17:42 = droplet utilitário da casa, confirmado no CEREBRO_NODE_ECOSSISTEMA_CANONICO).
- **Vetor primário:** indeterminável (logs de acesso de 14/08 já rotacionados — só 14 dias retidos). Hipótese: wp-login/xmlrpc brute (POSTs 200 de 8 IPs em 12/09 23:18-23:51; xmlrpc martelado até o bloqueio).
- **Dados:** DB é local (3306 só em localhost). Atacante como www-data lia wp-config → credenciais DB, SMTP (gmail-smtp), GA etc. **Tratar TODAS as credenciais do wp-config/options como comprometidas.**
- **Conteúdo editorial:** ilesos os posts reais; só oembed_cache + título/template. Leitores do canônico nem viram (domínio principal intacto).

## 5. O que falta (decisão/pendências Miguel)

- 🔴 **Trocar senhas**: ✅ James2017 canônico TROCADA pelo Miguel 13/09 ~16:3x; ✅ espelho: ZM resetou via wp-cli 16:25 BRT (senha temp 18 chars em ~/.senha_temp_james2017_espelho.txt perm 600, valor nunca no chat, cópia servidor apagada) — Miguel troca pela definitiva no 1º login; ⏳ senha root do droplet (instrução passwd via SSH entregue); app passwords REST se usadas no espelho.
- 🔴 **Reconstrução limpa do espelho** (recomendação ZM): fresh WP + re-sync do canônico (o sync horário repopula posts) — elimina qualquer artefato residual invisível. Alternativa: auditoria diff completa vs canônico.
- 🟠 Atualizar WP core (7.0→7.1) e revisar plugins inactive no espelho.
- 🟠 Firewall DO/UFW: manter só 22/80/443.
- 🟠 fail2ban ou rate-limit wp-login no nginx.
- 🟠 Aumentar retenção de access logs (14 dias não bastaram para forense de vetor).
- 🟡 Considerar Wordfence ativo no espelho (hoje inactive).
- 🟡 A chave ED25519 do Dell está duplicada nas 2 linhas do authorized_keys (migueldorosario@novo + vigia-central = mesmo fingerprint) — rotacionar para chaves distintas em momento calmo.

## 6. Cronologia (UTC)

- 14/08 07:20 — 1ª conta atacante (wp2_931d827f3020); 12:33 — webshells + pasta plugins tocada; 15:28 — miner /var/tmp/.xd
- 21/08 — 2ª instância miner (/tmp/sv)
- 26/08→10/09 — onda de contas w2s_*/wp2_*/James2017s*
- 09/09 02:42 — /tmp/.axs; gost proxy sobe (porta 38081)
- 12/09 10:52 — template do deface criado; 13:31→18:59 — contas steven27/wp2_8633582ba7e4/kacak/wp_service_708090; 23:18-23:51 — 8 IPs com POST 200 em wp-login
- 13/09 13:41→16:45 — contas Hoxxymexs/wp_admin_81642e; deface público (blogname)
- 13/09 ~18:38 — Miguel reporta; ZM diagnostica e contém (este fórum)

## 7. Memória técnica

Ver `Memorias/memoria_hack_cafezinho_news_20260913.md` (comandos, armadilhas: .bak em sites-enabled, charset utf8mb4 no REPLACE, REPLACE sem post_modified p/ não confundir sync, wp2shell = atacante).

## 8. Adendo ~16:4x BRT — PORTÃO ESCONDIDO no espelho (ordem Miguel: «senha baleia, portão de entrada; hackers nem deveriam saber que o espelho existe»)

- **Usuário `mdorosario` (ID 5825)** criado administrator, display "Miguel do Rosário", email mdorosario@cafezinho.news (o @gmail dele já era do James2017), **senha `baleia`** (escolha do Miguel — compensada pelo portão invisível; trocar em Perfil se quiser). Prova wp_check_password=true.
- **Portão nginx** (conf espelho, backup `backups_pre_edit/cafezinho-news.bak_pre_portao_20260913`): `/wp-login.php` → **404** para quem não tem o cookie `portao_baleia=abre`; destranca = **`https://cafezinho.news/destranca-baleia`** (302 → wp-login, cookie 30 dias Secure HttpOnly). Técnica cookie porque o WP POSTa wp-login sem query (gate por query string quebraria o POST).
- **Enumeração fechada**: `/wp-json/wp/v2/users`(+/ID) → 403; `?author=N` → 403 (WAF snippet); xmlrpc → 403 (já era). X-Robots-Tag noindex já ativo (a casa, 20260706) — bots do Google não indexam.
- Provas ao vivo: sem cookie 404 / destranca 302+Set-Cookie / com cookie 200 / REST users 403.
- Senha temporária antiga do James2017 (arquivo .senha_temp no Dell) APAGADA (obsoleta — James2017 do espelho segue com a temp do servidor setada às 16:25 até o Miguel redefinir; com mdorosario admin ele redefine pela tela Usuários).

## 9. Adendo ~17:2x BRT — ESPHELHO DESCONFIGURADO pós-recuperação: causa era do ATAQque original (Miguel: «tá entrando e todo desconfigurado»)

- Sintoma: home no tema default `twentytwentyfive` (blog cru). **Causa: o atacante desativou TODOS os plugins do espelho em 14/08** → tema da casa (`ocafezinho-portal` v2.0) quebra sem o `hello-highlight` (fatal `Call to undefined function get_highlight()` em `cafezinho-real-image-gate.php:206`, chamado por `front-page.php:5`) → ele trocou pro default e o espelho ficou feio desde 14/08 (ninguém via: todos olham o canônico).
- Correção: `wp theme activate ocafezinho-portal` + 15 plugins de renderização ativados (mesma base do canônico: hello-highlight, wordpress-seo(+premium), accelerated-mobile-pages, add-to-any, ad-inserter, ads-txt, ACF, better-youtube-embed, cookie-consent, gtranslate, insert-headers-and-footers, rss-featured-image, widget-options, wp-post-signature, wp-ajaxify-comments).
- Desativados DE PROPÓSITO no espelho (operação/métricas ficam no canônico): GA, wp-statistics, wp-rocket, redis-cache, wpematico, zapier, wptelegram, ai-engine, evermonitor, query-monitor, updraftplus, wordfence, jwt-auth, gmail-smtp, serverdoin-cdn, wpseo-local/news, web-stories, classic-editor, etc.
- Provas: home 200 313KB título «O Cafezinho | Contrainformação é Poder» (= canônico 338KB mesmo título), post individual 200, 0 erros fatais.
- 🔴 Lição: após incidente com desfiguração, conferir TEMA ativo + conjunto de plugins contra o site de referência — não basta o banco/option do título.

