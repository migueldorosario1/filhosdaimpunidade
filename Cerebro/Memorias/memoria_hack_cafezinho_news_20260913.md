# Memória — Hack cafezinho.news: log técnico completo (13/09/2026, ZCode/GLM-5.3)

Companion do `Foruns/forum_hack_cafezinho_news_20260913.md`. Servidor: root@159.65.177.60 (alias direto por IP; NÃO é o alias `cafezinho-wp`). WP: `/var/www/cafezinho-news`, DB `cafezinho_news` (MySQL local, senha em `/root/.cafezinho_news_db_pass`), tema twentytwentyfive, WP 7.0, **todos os plugins inactive** (mu-plugins da casa à parte).

## Sequência executada (comandos-chave)

```bash
# Backup forense (ANTES de qualquer remoção)
F=/root/forense_hack_20260913
cp /proc/<pid>/exe $F/…        # binários dos processos vivos
mysqldump -u cafezinho_news -p"$P" cafezinho_news wp_users wp_usermeta > wp_users_usermeta_full.sql
mysqldump … -w "post_content LIKE '%Ind3xZer0%'" wp_posts > wp_posts_contaminados.sql
mysqldump … wp_options > wp_options_full.sql
tar czf webshehlls_ps_plugins.tgz -C wp-content/plugins ps_2b31ca ps_26929a
crontab -u www-data -l > $F/crontab_www_data.bak

# Contenção
kill -9 <pids .x sv gost>; rm -rf /var/tmp/.xd /tmp/.axs /tmp/sv wp-content/plugins/ps_*
crontab -u www-data -r                       # crontab TODO era do atacante (4 linhas)
wp option update blogname "O Cafezinho"; wp option update blogdescription "…multipolar!"
wp post delete 401401 401402 --force         # wp_template do deface + revision → tema volta a renderizar
wp config shuffle-salts                      # derruba sessões do atacante
wp cache flush
# posts: mysql --default-character-set=utf8mb4 → UPDATE … REPLACE(post_content,' — Ind3xZer0 Quer cafe Admin kkkkk','')
# nginx: location = /xmlrpc.php { return 403; } inserido após linha server_name + nginx -t + reload
```

## Armadilhas pegas ao vivo (lições)

1. **🔴 .bak NUNCA em sites-enabled** — regra já conhecida da casa, tropeçada de novo: `cp conf conf.bak` DENTRO de sites-enabled quebra `nginx -t` (nginx carrega todos os arquivos do diretório). Correto: `/etc/nginx/backups_pre_edit/`.
2. **REPLACE SQL com em-dash UTF-8 exige `--default-character-set=utf8mb4`** — sem isso o literal do cliente vira latin1 e não casa (ROW_COUNT 0 silencioso). HEX() do trecho (E28094) confirmou o em-dash antes do REPLACE.
3. **UPDATE direto no post_content NÃO muda post_modified** — de propósito: o sync espelho←canônico (`/root/sync_from_cafezinho.sh`, */10min, delta por modified/cutoff) não confundiria estado.
4. **Deface de home em tema FSE (twentytwentyfive) pode ser um wp_template no banco** (post_type=wp_template sobrescreve o template do tema) — deletar o post do template devolve a home original, sem tocar em arquivos.
5. **Plugin "inactive" com shell no topo do arquivo AINDA EXECUTA** se acessado por URL direta (o código procedural roda standalone). Remoção da pasta é a única cura.
6. **`wp db search "<string>"`** acha a agulha no palheiro; depois `wp db query`/mysql para cirurgia.
7. **ps aux por usuário**: processos www-data escondidos em /tmp e /var/tmp com nomes de 1-2 chars (`.x`, `sv`) e binário estático de 32MB = miner; `gost` na porta alta com senha hardcoded = proxy de abuso. `ss -tlnp` confirma a porta no mundo.
8. **crontab do www-data** não aparece em `crontab -l` do root — examinar `crontab -u www-data -l` e `/var/spool/cron/crontabs/`.
9. Logs nginx rotacionam em 14 dias — vetor de entrada de 14/08 perdido. Recomendado aumentar retenção.
10. Duplicar a mesma chave SSH com dois comentários (authorized_keys) impede identificar qual linha logou — manter chaves distintas por função.

## Diff contas espelho×canônico — RETIFICAÇÃO CRÍTICA

🔴 **RETIFICAÇÃO (16h3x BRT / 19h3x UTC):** as contas `w2s_*`, `wp2_*`, `yun_11` (5786), `ngx_33` eram **TÉCNICAS DA CASA** (esteira de recortes; prova: recado 08/09 na ponte de_dell «Autor do post: "Redação Cafezinho" (não o hash w2s_… do teste)» + mu-plugin `cafezinho-origem-post.php` lista 5786 como «publicação interna wp-cli/cron»). Foram deletadas DURANTE o incidente ativo por cautela (padrão wp2shell parecia atacante + data 14/08 = data dos webshells). **Tudo restaurável do `wp_users_usermeta_full.sql`** (INSERTs por user_login). As `James2017s*` (impersonam o Miguel) ficam SUSPEITAS até confirmação — não restaurar sem ordem.

- Deletadas atacantes confirmadas: kacak, steven27, wp_service_708090, Hoxxymexs, wp_admin_81642e (e-mails descartáveis, 12-13/09).
- Deletadas técnicas da casa (restauráveis): yun_11, ngx_33, id69_a22872(?), wp2_×7, w2s_×19.
- Degradadas subscriber: cafezinho (5814), augustoevercode (5744).
- Admins finais: 13 legítimos (espelho nunca teve Redacao — bate com canônico 14 − 1).
- 3.328 posts reassig→2018 (o atacante manipulava post_author em massa via SQLi; recortes legítimos da casa também estavam no lote — byline fina resolve na reconstrução/sync).

## Estado final (16h2x BRT / 19h2x UTC)

Home externa 200/título correto/0 sinais; post individual 200/0 sinais; canônico 200; `wp core verify-checksums` SUCCESS; PHP modificados desde 14/08 = só .l10n.php (traduções); processlist 0 queries longas; porta 38081 fechada; crontab www-data vazio; WAF anti-SQLi provado (SLEEP→403, UNION SELECT→403); xmlrpc POST→403; 4 IPs denied (103.8.27.26, 209.50.61.117, 62.141.43.241, 194.5.49.102); salts girados. SQLi do processlist veio DE DENTRO (sem rastro HTTP nos logs — via webshell antes da remoção); vetor primário de 14/08 indeterminável (logs de 14 dias).

## Pendências abertas

Ver §5 do fórum (senhas, reconstrução limpa, core 7.1, firewall, fail2ban, retenção logs, rotação de chaves, restaurar contas técnicas da casa ao religar esteira de recortes).
