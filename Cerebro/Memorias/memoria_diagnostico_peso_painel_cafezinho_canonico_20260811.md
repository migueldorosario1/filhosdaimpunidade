# Memória — Diagnóstico do Peso do Painel Cafezinho Canônico (log técnico)

**Data:** 2026-08-11, 08:50 BRT
**Autor:** ZCode (GLM-5.2 Z.ai)
**Par:** `Foruns/forum_diagnostico_peso_painel_cafezinho_canonico_20260811.md` (decisões resumidas)
**Missão:** diagnóstico read-only do porquê do "painel" (wp-admin + home pública) ser pesado.
**Servidor:** `cafezinho-wp` = `root@190.89.239.65:51439` (us65.serverdo.in), VPS QEMU 8 cores / 8 GB RAM.
**Acesso:** via alias `cafezinho-wp` (BatchMode, chave instalada).
**Filosofia:** tudo abaixo é **read-only** e **reprodutível** — qualquer agente pode re-executar pra validar.

---

## 1. Sequência de comandos executada (todos read-only)

### 1.1 Medições externas (do PC do Miguel, sem SSH)

```bash
# TTFB e tamanho da home (3 tentativas — 1 OK, 2 timeout)
for i in 1 2 3; do
  curl -s -o /dev/null -w "tentativa $i: HTTP %{http_code} | total %{time_total}s | TTFB %{time_starttransfer}s | tamanho %{size_download}\n" -L "https://www.ocafezinho.com/"
done

# Comparativo: AMP, single, estático, API, wp-admin
curl -s -o /dev/null -w "%{http_code} %{time_total}s TTFB %{time_starttransfer}s %{size_download}b\n" -L "https://www.ocafezinho.com/?amp"
curl -s -o /dev/null -w "%{http_code} %{time_total}s TTFB %{time_starttransfer}s %{size_download}b\n" -L "https://www.ocafezinho.com/2026/08/10/lula-reconquista-as-capitais/"
curl -s -o /dev/null -w "%{http_code} %{time_total}s TTFB %{time_starttransfer}s %{size_download}b\n" -L "https://www.ocafezinho.com/2026/08/10/lula-reconquista-as-capitais/amp/"
curl -s -o /dev/null -w "%{http_code} %{time_total}s TTFB %{time_starttransfer}s %{size_download}b\n" "https://www.ocafezinho.com/wp-json/wp/v2/posts?per_page=3"
curl -s -o /dev/null -w "%{http_code} %{time_total}s TTFB %{time_starttransfer}s\n" -L "https://controle.ocafezinho.com/wp-admin/"

# Anomalia: robots.txt e sitemap dão timeout HTTP 000
curl -s -o /dev/null -w "robots: %{http_code} %{time_total}s\n" "https://www.ocafezinho.com/robots.txt"
curl -s -o /dev/null -w "sitemap: %{http_code} %{time_total}s\n" "https://www.ocafezinho.com/sitemap_index.xml"

# Recursos externos da home (scripts/trackers)
HTML=$(curl -sL "https://www.ocafezinho.com/")
echo "$HTML" | grep -oE '<script[^>]*src="[^"]*"' | sed 's/.*src="//;s/"//'
echo "$HTML" | grep -oiE 'googletagmanager|gpt\.js|adsbygoogle|doubleclick|teads|360yield|mgid|taboola|outbrain|criteo|comscore|hotjar|clarity|gtag' | sort | uniq -c
```

### 1.2 Recursos do servidor (via SSH, BatchMode)

```bash
ssh cafezinho-wp 'uptime; free -h; df -h /; nproc; ps aux --sort=-%cpu | head -11'
ssh cafezinho-wp 'ps aux | grep "php-fpm: pool" | grep -v grep | awk "{sum+=\$6; n++} END {printf \"Workers: %d RSS medio: %.0f MB Total: %.0f MB\n\", n, sum/n/1024, sum/1024}"'
```

### 1.3 Banco de dados (credenciais lidas do wp-config — SEM expor valores)

```bash
ssh cafezinho-wp 'DBN=$(awk -F"'\''" "/DB_NAME/{print \$4; exit}" /var/www/ocafezinho/wp-config.php); DBU=$(awk -F"'\''" "/DB_USER/{print \$4; exit}" /var/www/ocafezinho/wp-config.php); DBP=$(awk -F"'\''" "/DB_PASSWORD/{print \$4; exit}" /var/www/ocafezinho/wp-config.php); export MYSQL_PWD="$DBP"

# Top tabelas por tamanho + engine + linhas
mysql -u"$DBU" "$DBN" -e "SELECT table_name, engine, ROUND((data_length+index_length)/1024/1024,1) mb, table_rows FROM information_schema.tables WHERE table_schema=\"$DBN\" AND (data_length+index_length) > 10*1024*1024 ORDER BY (data_length+index_length) DESC LIMIT 12;"

# Total DB
mysql -u"$DBU" -e "SELECT ROUND(SUM(data_length+index_length)/1024/1024,0) total_mb FROM information_schema.tables WHERE table_schema=\"$DBN\";"

# wp_options autoload (pesado — carregado em todo request)
mysql -u"$DBU" "$DBN" -e "SELECT option_name, ROUND(LENGTH(option_value)/1024,1) kb FROM wp_options WHERE autoload=\"yes\" ORDER BY LENGTH(option_value) DESC LIMIT 15;"

# Processos ativos agora
mysql -u"$DBU" "$DBN" -e "SHOW PROCESSLIST;"'
```

### 1.4 Stack e cache

```bash
ssh cafezinho-wp 'php -v | head -1; mysql --version; nginx -v 2>&1
grep -E "^(pm |pm\.)" /etc/php/7.4/fpm/pool.d/www.conf
redis-cli ping; redis-cli info memory | grep used_memory_human
mysql -u"$DBU" -e "SHOW VARIABLES LIKE \"slow_query%\"; SHOW VARIABLES LIKE \"long_query_time\";"
php -i 2>/dev/null | grep -E "memory_limit|opcache.enable"'
```

---

## 2. Resultados brutos (snapshot 11/08 08:45-08:55 BRT)

### 2.1 Latência externa

```
home non-AMP:   200 (1/3) | 5,8s total | 5,7s TTFB | 200 KB    🔴
home AMP:       200 | 0,9s | 0,9s | 200 KB                       🟢
single non-AMP: 200 | 0,9s | 0,7s | 215 KB                       🟡
single AMP:     200 | 0,6s | 0,5s | 129 KB                       🟢
estático logo:  200 | 0,3s | 0,3s | 7 KB                         🟢
API REST:       200 | 1,4s | 1,3s | 76 KB                        🟡
wp-admin login: 200 | 1,8-2,9s | 1,8-2,9s                        🟡
robots.txt:     000 | 25s timeout                                🔴 ANOMALIA
sitemap:        000 | 21s timeout                                🔴 ANOMALIA
```

### 2.2 Recursos servidor

```
uptime:   load average 4,31 / 3,79 / 3,78   (8 cores QEMU)
RAM:      7,8 GB total | 4,2 GB used | 663 MB free | 2,9 GB buff/cache
Swap:     2,5 GB em uso de 9,9 GB (swap.img 1,9G + swapfile 8G)
MySQL:    PID 832 | 203% CPU | 19,8% MEM (1,6 GB) | 647 min CPU acumulados em 5h
PHP-FPM:  65 workers ativos | 97 MB RSS médio | 6,3 GB total
Disco:    335 GB total | 149 GB usado (47%) | /uploads 62 GB / 823.337 arquivos
```

### 2.3 Stack

```
PHP:      7.4.33 (EOL nov/2022) — PHP 8.3 instalado mas não usado pelo site
MySQL:    5.7.44 (EOL out/2023)
nginx:    1.28.0
Redis:    PONG | 256 MB used
OPcache:  enabled
WP Rocket: ativo
slow_query_log: OFF (long_query_time=10)
```

### 2.4 Top tabelas DB (3,2 GB total)

```
wp_wffilemods              InnoDB  855 MB  1.289.305 linhas  (Wordfence)
wp_posts                   MyISAM  545 MB  201.765
wp_wfknownfilelist         InnoDB  393 MB  1.333.427         (Wordfence)
wp_postmeta                MyISAM  325 MB  1.316.119
wp_comments                MyISAM  305 MB  625.265
wp_evermonitor_event_queue InnoDB  234 MB  159.381
wp_commentmeta             MyISAM  153 MB  988.575
wp_wpr_rocket_cache        InnoDB  117 MB  227.715
wp_yoast_indexable         InnoDB  104 MB  94.722
wp_yoast_seo_links         InnoDB   75 MB  148.851
```

### 2.5 wp_options autoload (top)

```
rewrite_rules           165 KB
colabs_template         158 KB    ← plugin inexistente (ressíduo)
yst_ga_top_pageviews    124 KB
wpts_compat             102 KB
wp_installer_settings   102 KB
ABCCtop                  64 KB
ad_inserter              48 KB
redux_builder_amp        44 KB
```

### 2.6 wp_posts por tipo

```
attachment  114.037
post         80.613
oembed_cache  3.816
revision        834
nav_menu_item   708
page            675
```

---

## 3. Vilões ranqueados (causa → efeito)

1. **PHP-FPM `pm.max_children=110`** → 65 workers × 97 MB = 6,3 GB → swap 2,5 GB → lentidão em tudo (home, wp-admin, API)
2. **Wordfence 1,2 GB** (`wp_wffilemods` 855 MB + `wp_wfknownfilelist` 393 MB) → MySQL 203% CPU
3. **4 tabelas críticas em MyISAM** (`wp_posts`/`wp_postmeta`/`wp_comments`/`wp_commentmeta`) → lock de tabela em escrita trava leitura (625K comentários = muita escrita)
4. **`wp_evermonitor_event_queue` 234 MB** → plugin sem rotação, cresce p/ sempre
5. **PHP 7.4 EOL** → 20-30% mais lento que 8.x disponível
6. **`wp_wpr_rocket_cache` 228K linhas no banco** → anormal, cache deveria ser filesystem
7. **15 plugins inativos** no disco → lixo
8. **823K arquivos em `/uploads`** (62 GB) → I/O pesado, backup pesado

---

## 4. Pontos saudáveis (NÃO mexer)

- ✅ Redis object cache (PONG, 256 MB)
- ✅ WP Rocket ativo
- ✅ OPcache ligado
- ✅ Home non-AMP sem `gpt.js`/`adsbygoogle` (ads quase só AMP — ver mapa ads)
- ✅ Disco com espaço (47%)
- ✅ CDN (serverdoin) serve estáticos em 0,3s

---

## 5. Anomalias de segurança observadas (bônus)

1. **Exploração ativa** IP `176.65.132.53` → `POST /device.rsp` tentando baixar `data_arm7` (malware ARM). Várias tentativas em 08:23/08:33/08:40/08:50. Wordfence aparentemente não bloqueia.
2. **Requests a `timthumb.php`** (theme `arthemia` antigo, vulnerabilidade RCE histórica) — theme não ativo mas requests chegam.
3. **Warning PHP:** `wp-smush-pro ... Undefined array key "2016/06/Parente.png" in class-media-item-query.php:200`.

---

## 6. Backups feitos

Nenhum — **zero escrita no servidor/DB**. Esta memória documenta apenas leituras. Quando o Miguel autorizar Tier 1, farei backups datados (`.bak_pre_<tema>_<ts>`) antes de cada mudança.

---

## 7. Lições técnicas (reaproveitáveis)

1. **VPS de 8 GB NÃO suporta `pm.max_children=110`** com WP pesado — fórmula segura: `(RAM_total - RAM_reservada_OS_e_MySQL) / RAM_por_worker`. Aqui: `(8 - 4) / 0,15 ≈ 26`. Recomendar 30-40 com margem.
2. **Wordfence em site grande vira vilão** — `wffilemods` e `wfknownfilelist` crescem sem parar; em sites com 80K+ posts, compensa **agendar limpeza mensal** ou desativar o scan de integridade.
3. **MyISAM em WP com muitos comentários = contenção** — `wp_comments` com 625K linhas sofrendo INSERT a cada novo comentário trava SELECTs concorrentes. Conversão p/ InnoDB é uma das alavancas mais subestimadas.
4. **`wp_options` autoload** carrega em **todo request** — `colabs_template` (158 KB) de plugin que nem existe mais é puro desperdício.
5. **WP Rocket com cache no banco (228K linhas)** é sinal de má configuração — cache de página deve ser filesystem; o que está no DB provavelmente é logs ou cache de metadados.
6. **PHP 7.4 EOL** sem patches há quase 4 anos = risco de segurança além de performance. Migração 8.3 deve ser **priorizada** (mas com staging — alguns plugins antigos quebram).
7. **`slow_query_log=OFF`** impede diagnóstico fino — primeira coisa a ligar (custo ~zero).
8. **Robots.txt/sitemap dando timeout** é sintoma clássico de WP Rocket + Yoast em conflito ou PHP travando na geração — investigar depois de ligar slow log.

---

## 8. Estado da missão (pra retomar)

- **O que aconteceu:** diagnóstico 100% read-only entregue. 8 vilões identificados com prova. Plano de ação em 3 tiers (12 itens) priorizado por risco no fórum par.
- **O que falta:** decisão do Miguel sobre qual tier aplicar. Tier 1 (6 ações de baixo risco) devolve a performance do servidor sem mexer em código/tema.
- **O que preciso do Miguel:** (a) confirmar escopo ("painel" = wp-admin + home pública?); (b) autorizar Tier 1 ou pedir detalhamento de cada item antes.

---

## Assinatura

**ZCode (GLM-5.2 Z.ai)** — sessão fallback final
Workspace: `ZCodeProject`
Timestamp: 2026-08-11 08:55 BRT

_Documento vivo. Par de decisões no `Foruns/forum_diagnostico_peso_painel_cafezinho_canonico_20260811.md`._
