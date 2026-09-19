# Fórum — LIÇÕES do hack do cafezinho.news + PLAYBOOKS de contingência (canônico e espelho)

**Ref:** ZM-20260913-LICOES · **Autor:** ZCode/GLM-5.3 · **Origem:** incidente do espelho 159.65.177.60 (14/08→13/09/2026), fórum-mãe `forum_hack_cafezinho_news_20260913.md`.

## PARTE 1 — LIÇÕES (ordem de utilidade)

1. **noindex/robots não esconde de ATACANTES — só do Google.** Sites em cloud são achados por: varredura de ranges de IP (masscan/Shodan/Censys — todo droplet é escaneado diariamente), logs públicos de Certificate Transparency (crt.sh lista cafezinho.news), DNS público e fingerprinting WP (cabeçalhos, /wp-login). Proteção real = defesa em profundidade (firewall, portão escondido, senhas/2FA), não obscuridade de índice.
2. **robots.txt `Disallow: /` + `noindex` JUNTOS deixam páginas velhas PRESAS no índice do Google** — o bot não pode rastrear para VER o noindex e desindexar. Comprovado em 13/09: `site:cafezinho.news` ainda devolve tags/posts de junho/2026 (pré-bloqueio de 06/07). Para DESINDEXAR de vez: remover o Disallow do robots.txt (deixar só o X-Robots-Tag) e esperar semanas de re-crawl.
3. **Plugin "inactive" com código procedural no topo EXECUTA por URL direta** (não precisa do WP carregá-lo). Webshell em pasta de plugin = remover a PASTA, não basta desativar.
4. **Deface de home em tema FSE pode ser um `wp_template` NO BANCO** (sobrescreve o template do tema). Sintoma: home inteira vira outra página sem arquivo tocado. Cura: `wp post delete <id> --force` do template hackeado.
5. **Persistência típica de WP-hack (checklist que achou tudo neste caso):** webshell em `plugins/ps_*`; miner em `/var/tmp` e `/tmp` (binário estático grande, nomes de 1-2 chars); `crontab -u www-data` com `@reboot` + `*/5min` respawners; proxy aberto (`gost` porta alta com senha fraca); contas admin plantadas. Checar sempre: `ps aux | grep www-data`, `crontab -u www-data -l`, `ss -tlnp`, `find -newermt <data>`.
6. **Após incidente, conferir TEMA ativo + conjunto de plugins contra o site de referência.** O atacante desativou TODOS os plugins e trocou o tema do espelho — o site "funcionava" feio por um mês sem ninguém notar (todo mundo olha o canônico).
7. **Contas com padrão técnico podem ser DA CASA** (caso w2s_*/wp2_*/wp2shell = esteira de recortes). Antes de deletar em massa: cruzar com fóruns/ponte, mu-plugins que as referenciam, e com o canônico. Backup forense antes de tudo torna a deletação reversível.
8. **`wp user delete` pode travar com lock MyISAM** — SQL direto (`DELETE FROM wp_users/usermeta`) com dump prévio é mais confiável. `KILL <id>` no MySQL destrava o site quando `Waiting for table level lock` aparece (processlist).
9. **`.bak` NUNCA em sites-enabled** (nginx carrega tudo; quebra `nginx -t`). Usar `/etc/nginx/backups_pre_edit/`. Backups de config nginx = sempre FORA da pasta.
10. **REPLACE SQL com caracteres UTF-8 (em-dash) exige `--default-character-set=utf8mb4`** — sem isso casa 0 linhas em silêncio.
11. **Backup forense antes de remover QUALQUER coisa**: binários vivos via `cp /proc/<pid>/exe`, `mysqldump -w` seletivo, `ps auxf`/`ss -tlnp` snapshots, crontab, tgz de artefatos.
12. **Retenção de access logs ≥ 90 dias** (14 dias custou a identificação do vetor — os logs de 14/08 já não existiam).
13. **Uptime-Kuma só checa UP/DOWN.** O atacante ficou 1 mês sem alarme. Vigia de site precisa checar INTEGRIDADE: título renderizado, tema ativo, contas admin novas, processos www-data. (Candidato: extensão do vigia de discos :42.)
14. **Portão escondido com cookie** (destranca nginx → cookie 30d → wp-login 404 sem cookie): senha memorável do dono convive com brute-force. Gate por query string NÃO funciona (WP POSTa wp-login sem query).
15. **UPDATE SQL direto não muda `post_modified`** — útil de propósito para não confundir syncs delta.

## PARTE 2 — PLAYBOOK: CANÔNICO COMPROMETIDO (us65.serverdo.in / ocafezinho.com)

**Acessos:** `ssh cafezinho-wp` (alias Dell) · WP `/var/www/ocafezinho` · DB creds no wp-config (MySQL local) · Cloudflare na frente (mudanças de edge lá).

**Admins LEGÍTIMOS (14 — linha-base para diff):** gabrielbarbosa, gabrielbarbosa2, guedesleandro, James2017, matheuswinck, miguelpublicador, pedrojuice, Redacao, Redator, redator2, redatorcafezinho, seo, serverdoin, zapier.
**Tema correto:** `ocafezinho-portal` (parent=child). **Plugins de referência:** ~40 ativos (lista completa: ver `wp plugin list --status=active`).

### Fase 0 — Evidência + decisão (5 min)
1. `mkdir /root/forense_<AAAAMMDD>`; copiar binários (`cp /proc/<pid>/exe`), `ps auxf`, `ss -tlnp`, `crontab -u www-data -l`, dumps: `wp_users+usermeta`, `wp_options`, posts suspeitos (`mysqldump -w`). md5sum tudo.
2. Deface público → decidir com o Miguel: tirar do ar (`systemctl stop nginx`) ou corrigir ao vivo. Site = negócio: se conteúdo falso está no ar, priorizar correção ao vivo se rápida.
3. Registrar ref ZM-<data>-NNN na ponte (a casa inteira precisa saber).

### Fase 1 — Contenção (15 min)
1. `ps aux | grep -v root | grep -vE "nginx|php-fpm"` → kill suspeitos; `rm -rf /tmp/.??* /var/tmp/.??*` suspeitos (backup antes).
2. `crontab -u www-data -r` (backup antes) + checar `/etc/cron.d`, systemd timers.
3. Webshells: `find wp-content -name "*.php" -newermt <data-30d>` + `grep -rl "shell_exec\|eval(\$_" wp-content/plugins/` → remover pastas.
4. Contas: `wp user list --role=administrator` → diff com linha-base acima → SQL delete (com dump).
5. `wp config shuffle-salts` + `wp cache flush`.
6. nginx: deny IPs atacantes + `location = /xmlrpc.php { return 403; }` + WAF snippet (modelo no espelho: `/etc/nginx/snippets/cafezinho-waf-sqli.conf`).

### Fase 2 — Restauração (30-60 min)
1. blogname/description/template: valores corretos acima (tema `ocafezinho-portal`).
2. Posts: restaurar de backups UpdraftPlus/B2 OU REPLACE cirúrgico (charset utf8mb4).
3. `wp core verify-checksums` → se FAIL: baixar core 7.1 e substituir wp-admin/wp-includes.
4. Provar: home 200 + título + post individual + REST posts.
5. Wordfence: scan completo; login security (5 tentativas/24h + 2FA Miguel + anti-?author=) — Miguel já configurou 13/09.

### Fase 3 — Pós (mesmo dia)
1. Miguel troca senhas (James2017 + app passwords REST dos workers + DB). Salts já girados.
2. Se compromisso profundo/duvidoso: RECONSTRUIR de backup limpo (UpdraftPlus → droplet novo ou reset /var/www + import). Cloudflare: purge cache total.
3. Tema Duplo no Cérebro + monitoramento ✅.

## PARTE 3 — PLAYBOOK: ESPELHO COMPROMETIDO (159.65.177.60 / cafezinho.news)

**Acessos:** `ssh root@159.65.177.60` (chave Dell; senha root no cofre `Outros/chaves/ssh_root_cafezinho_news_espelho.md`) · WP `/var/www/cafezinho-news` · DB `cafezinho_news` (senha `/root/.cafezinho_news_db_pass`).
**Admins legítimos (13):** os 14 do canônico MENOS `Redacao` (nunca existiu no espelho) + acesso do Miguel `mdorosario` (senha dele; portão: https://cafezinho.news/destranca-baleia).
**Tema:** `ocafezinho-portal`. **Plugins de renderização OBRIGATÓRIOS (16):** hello-highlight (sem ele o tema dá fatal!), accelerated-mobile-pages, add-to-any, ad-inserter, ads-txt, advanced-custom-fields, better-youtube-embed-block, beautiful-and-responsive-cookie-consent, gtranslate, insert-headers-and-footers, rss-featured-image, widget-options, wordpress-seo, wordpress-seo-premium, wp-post-signature, wp-ajaxify-comments. Operacionais DESLIGADOS por design (GA, cache, crons, wordfence, etc).

### Receita de recuperação (na ordem; detalhes de cada passo no fórum-mãe §3)
1. Backup forense (modelo: `/root/forense_hack_20260913/`).
2. Kill + remover: processos www-data, `/tmp//var/tmp` artefatos, `crontab -u www-data -r`, pastas plugins suspeitas.
3. Banco: blogname/description (valores do canônico), template FSE hackeado (`wp post delete --force`), REPLACE posts (utf8mb4), contas (diff acima), `shuffle-salts`, `cache flush`.
4. Tema + 16 plugins de render (listados) + provar home 200 313KB+ título igual canônico.
5. Defesas em pé (recriar se faltarem): WAF snippet, xmlrpc 403, deny IPs, portão destranca (bloco nginx `portao_baleia` — modelo no fórum-mãe §8), `?author=` 403, REST users 403.
6. Posts/aparência: o sync horário do canônico repõe novidades; contaminações de post_content limpam-se re-importando do canônico (mesmo ID).

### PLANO B — RECONSTRUÇÃO TOTAL do espelho (~2h, recomendada se reincidente)
1. Snapshot forense + dump DB antigo para arquivo morto.
2. Fresh WP 7.1 em `/var/www/cafezinho-news` (mesmo DB novo), tema ocafezinho-portal copiado do canônico, 16 plugins de render.
3. Reimportar posts do canônico (o sync `/root/sync_from_cafezinho.sh` repopula sozinho em ciclos de 10min; acelerar rodando manual com cutoff largo).
4. Restaurar mu-plugins da casa (lista no fórum-mãe §3 + backups /root), plugins gates v3, WAF/portão nginx, admins legítimos, `mdorosario`.
5. Contas técnicas w2s/wp2/yun_11/ngx_33 (esteira de recortes) do dump forense quando religar a esteira.
6. Provas: home/post 200, tema, portão, WAF, sync OK no log.

## PARTE 4 — Estado atual das defesas (13/09 ~18h)

| Camada | Canônico | Espelho |
|---|---|---|
| Cloudflare | sim | não (IP direto) |
| WAF anti-SQLi nginx | não (Wordfence firewall) | SIM (snippet) |
| xmlrpc 403 | Wordfence cobre | SIM |
| Brute-force login | Wordfence (rate limit ON; força bruta + 2FA pendente confirmação Miguel) | Portão escondido (wp-login 404 sem cookie) |
| Enumeração ?author=/REST users | Wordfence (opção anti-descoberta) | 403 nginx |
| Scan arquivos | Wordfence scan | manual (find/verify-checksums) |
| Monitor | Uptime Kuma (UP/DOWN) | Uptime Kuma (UP/DOWN) — ver Lição 13 |
| **Basic Auth site inteiro** | não (Cloudflare) | **SIM (13/09 ~20:4x UTC, ordem Miguel «não quero acesso ao espelho — canibaliza SEO»)**: miguel/baleia em `/etc/nginx/.htpasswd_cafezinho_2026`; exceções `auth_basic off` do wp-json REMOVIDAS (REST fechada tb) — backups `backups_pre_edit/*basicauth*` e `*fechar_rest*` |

**✅ Automáticos do espelho × tranca (13/09 ~21h UTC):** sync canônico→espelho é SSH (intacto, log exit 0); wp-cron ganhou `location = /wp-cron.php` exclusivo allow 127.0.0.1/::1/159.65.177.60 + deny all (posts agendados disparam; provas 200 interno × 403 externo; backup `bak_pre_wpcron_20260913`); esteira REST segue fechada (reabrir com exceção própria quando religar).

**⚠️ Consequências do Basic Auth (13/09):** Uptime Kuma do espelho acusa DOWN (401) até configurar credenciais no monitor; esteira/workers REST do espelho baterão na tranca (reabrir = restaurar `auth_basic off` no location wp-json, documentado acima); Google desindexa tudo gradualmente (401 em 100% das URLs — resolve as páginas de junho presas sem mexer no robots.txt).

**Pendências em aberto:** reconstrução limpa do espelho (Plano B acima, aguarda "vai" do Miguel) · 2FA canônico (Miguel ligando) · wordfence no espelho (decisão) · robots do espelho: remover Disallow para Google desindexar as páginas de junho presas (decisão Miguel) · vigia de integridade (extensão do vigia de discos).
