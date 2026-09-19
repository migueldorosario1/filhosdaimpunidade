# 🔴 Fórum — INCIDENTE: ataque SQLi time-based derrubou o espelho cafezinho.news (03/09/2026)

> Descoberto DURANTE a análise do V4.2 Investimento (ordem Miguel ~07:2x). Execução do plantão: ZM Dell (ZCode/Kimi K3). Memória-irmã: `Memorias/memoria_incidente_sqli_espelho_20260903.md`.

## O que aconteceu (linha do tempo, BRT)

1. **Desde 02/09 ~06:58** (nascimento do mariadbd atual): MariaDB acumulando CPU — 1.514 min (>25h) até 07:55 de 03/09. Ondas de esgotamento do php-fpm nos avisos de log: 06:21, 06:24, 09:53 (02/09?) e 10:29 UTC de 03/09 (=07:29 BRT, dentro da janela da minha análise).
2. **05:25-05:31:** as 3 execuções do V4.2 Investimento falharam — a primeira com o 400 do GATE-IMG (ver fórum do V4.2 §adendo 1), o cenário de banco sob ataque pode ter contribuído para a lentidão geral, mas o 400 é do gate (prova T5 com site saudável).
3. **~07:45:** espelho 100% inacessível (nem home) do Dell e do tencent; GETs REST que às 07:25 ainda davam 200.
4. **~07:5x-08:0x — plantão ZM (com provas em cada passo):**
   - `SHOW PROCESSLIST`: 3 queries `SELECT SQL_CALC_FOUND_ROWS wp_posts.* ... post_author NOT IN (0) OR IF(1...` em estado **User sleep** (~28 min) = SQLi time-based (SLEEP injetado EXECUTANDO); + UPDATE guid 400317 e SELECT por IDs **Waiting for table level lock** (wp_posts é **MyISAM**) = publicações do Estatística também travadas.
   - KILL das 3 → nasceram 3 NOVAS em segundos = ataque contínuo.
   - Flagrante: única conexão estabelecida :443 = **195.178.110.247**; família **195.178.110.22** no log 10:24 UTC caçando `/cafezinho.news_db.sql`, `/cafezinho.zip` etc.
   - **Cura:** `iptables -I INPUT -s 195.178.110.247/32 -j DROP` (+ .22) · KILL de todos os "User sleep" · `ss -K dst .247` (conexão residual). 
   - **Prova de recuperação:** localhost 200 (3,0s) → home 200 (3,5s) e REST 200 (0,85s) do Dell. Processlist limpo, 0 sleeps.
   - Access log do nginx PAROU às 10:40 UTC: requests pendurados só logam ao completar (o atacante ficava invisível no log — lição de caça: usar `ss`/processlist em queda com log mudo).

## O que é grave (PRECISA MIGUEL — junto com ZD-20260903-001)

1. **O SLEEP injetado RODOU no banco** — não é scan batendo na porta: a injeção (`OR IF(...SLEEP...)`) entrou numa query real do WP_Query (cláusula do `post_author`). Existe superfície REAL de SQLi em tema/plugin do espelho — **o canônico provavelmente compartilha o mesmo código e o mesmo buraco**. Auditoria do vetor é prioridade de segurança (preciso da palavra para escanear access logs arquivados + diff de plugins/tema).
2. **Fragilidades que amplificaram:** `wp_posts` MyISAM (table locks derrubam escrita), `pm.max_children=5` (5 requests lentos = site fora), sem fail2ban/WAF/rate-limit.
3. **Cura estrutural proposta (aguarda "vai"):** fail2ban ou rate-limit nginx p/ padrões SQLi (`IF(`, `SLEEP(`, `BENCHMARK(`) · converter wp_posts e wp_postmeta MyISAM→InnoDB · revisar pm.max_children · (opcional) bloqueio geográfico/allowlist da REST p/ robôs.

## Rollback do plantão

- Remover 2 regras: `iptables -D INPUT -s 195.178.110.247/32 -j DROP` e idem .22 (não persistem após reboot).

— ZCode/Kimi K3 (ZM, Dell) · 03/09/2026 08:0x BRT

---

## ADENDO 1 — 2ª onda + plantão de timeouts + allowlist (aplicada e REVERTIDA por ordem) (03/09 ~08:5x→09:5x BRT)

1. **2ª onda** ~08:50: 3 sleeps novos (payload `OR IF(1,SLEEP(SLEEP(3)),0)-- -` — sqlmap) — atacante rotaciona IP; KILLs + flagrante via `ss` ($4, não $5 — lição de parsing). Depois o droplet **exauriu** (nem SSH; ~09:0x-09:3x) e **voltou sozinho** ~09:39 (load 0.28, 0 sleeps).
2. **Cura estrutural de plantão (mantida):** `fastcgi_read_timeout 120→25s` (vhost, backup `.bak_pre_timeout25_20260903`) + `request_terminate_timeout = 30s` (fpm www.conf, backup) — pedido lento não segura mais o site por 20 min. 2 DROPs iptables dos IPs atacantes mantidos.
3. **ALLOWLIST por ordem do Miguel ~09:4x** ("fecha o espelho, deixa só Dell/iPad/celular"): aplicada às ~09:4x com backups (`ufw_backup_pre_allowlist_20260903.txt`, `iptables_backup_...`) — 3 IPs da casa (Dell/casa 179.165.183.103 · tencent 43.156.151.165 · NYC 198.199.121.136) × portas 22/80/443, regras Anywhere removidas, provas: casa 200 + nós externos (CA/DE/IL/UA) "Connection timed out" via check-host.net. **Efeito colateral descoberto na hora:** o Tribunal de Mídia perdeu o acesso à imagem (qwen-vl baixava a URL pública) → curado com base64 inline.
4. **REVERSÃO por ordem do Miguel ~09:5x** ("o ataque já passou, relaxa, não faz loucura de allowlist"): ufw restaurado ao original (OpenSSH + Nginx Full abertos), 9 regras removidas. **Mantidos:** 2 DROPs dos atacantes + timeouts 25/30s (não fecham nada, só cortam pedidos parados).
5. **IPs entregues ao Miguel** p/ bloquear no plugin de defesa do CANÔNICO: **195.178.110.0/24** (bloco inteiro do atacante — recomendado; IPs vistos: .22 e .247) · opcional 78.153.140.148 (sondador de .env). ⚠️ NÃO bloquear 43.156.151.165 (tencent) nem 179.165.183.103 (casa).
6. **Canônico: INTACTO** — única ação foi 1 GET de leitura (200) para confirmar saúde; zero mudanças (ordem "deixa o canônico em paz" respeitada).
7. **PENDÊNCIA B segue aberta:** auditoria do vetor (tema/plugin que deixa o SLEEP entrar) no espelho E no canônico + remendo.

— ZCode/GLM-5.3 (ZM, Dell) · 03/09/2026 09:5x BRT
