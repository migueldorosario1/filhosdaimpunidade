# 🔴 Memória técnica — SQLi time-based derrubou espelho cafezinho.news + plantão ZM (03/09/2026 ~07:45-08:03 BRT)

Fórum-irmão: `Foruns/forum_incidente_ataque_sqli_espelho_20260903.md`. Executor: ZM Dell (ZCode/Kimi K3). Contexto: descoberto durante a análise do V4.2 Investimento (ordem Miguel).

## Evidências (comandos e saídas-chave)

1. Sintoma: HTTP 000/timeout de TODOS os pontos (Dell + tencent) para https://cafezinho.news; DNS aponta direto 159.65.177.60 (sem Cloudflare); curl --resolve no IP também pendurava → problema na origem.
2. SSH root@159.65.177.60 OK. `ps`: mariadbd PID 1199627 nascido **Sep 2 06:58:26**, TIME **1514:59** (~96% médio de CPU contínua). Load baixo (travas em espera, não CPU no instante).
3. `information_schema.processlist`: 3× `Query / User sleep / ~28min` com `SELECT SQL_CALC_FOUND_ROWS wp_posts.* FROM wp_posts WHERE 1=1 AND post_author NOT IN (0) OR IF(1...` (= SQLi time-based via SLEEP; estado "User sleep" = SLEEP() do atacante) + `UPDATE wp_posts SET guid='...400317'` e `SELECT ... ID IN (400317,...)` em **Waiting for table level lock** (wp_posts = **MyISAM**, confirmado em information_schema.tables).
4. KILL inicial das 3 → 3 novas em <5s (ataque contínuo; matar conexão não cura).
5. Flagrante: access.log nginx mudo após 10:40 UTC (request pendurado só loga ao completar — LIÇÃO DE CAÇA) → `ss -tn state established '( sport = :443 )'` = **única** conexão: 195.178.110.247:49948. Log 10:24 UTC: 195.178.110.22 sondando `/cafezinho.news_db.sql`, `/cafezinho.zip`, `/cafezinho.sql`, `/2026.zip` (301s).
6. php-fpm: `pm.max_children=5` atingido nas ondas (fpm log 06:21, 06:24, 09:53, 10:29 UTC) — 5 requests dormindo = site fora.

## Curas aplicadas (plantão, com rollback documentado)

```
iptables -I INPUT -s 195.178.110.247/32 -j DROP   # atacante ativo
iptables -I INPUT -s 195.178.110.22/32 -j DROP    # scanner da mesma rede
mysql: KILL de todos os processlist.state='User sleep' (3+3)
ss -K dst 195.178.110.247                         # matou conexão residual ESTAB (iptables não derruba established)
```
Provas de recuperação: localhost 200/3,0s → Dell home 200/3,5s · REST /wp-json/wp/v2/posts 200/0,85s · processlist limpo. Rollback: `iptables -D INPUT -s <ip>/32 -j DROP` ×2 (regras não persistem reboot).

## Lições

1. **Log mudo ≠ sem tráfego:** em queda com access.log parado, o atacante mora no `ss state established` + `processlist` (os pendurados não logam).
2. **iptables DROP não mata established:** sempre complementar com `ss -K dst <ip>`.
3. **MyISAM + 5 workers = queda em cascata:** 3 SLEEPs seguraram locks de tabela e pararam o site inteiro (e as publicações do V4.2 Estatística, ex.: guid do 400317 preso no lock).
4. **O SLEEP EXECUTOU = SQLi real** (não só scan): vetor entra pela cláusula post_author do WP_Query → tema/plugin vulnerável a identificar; canônico pode compartilhar o mesmo código. Auditoria pendente de "vai" do Miguel.
5. Telemetria r.raise_for_status() sem r.text custou o diagnóstico do 400 (T5 teve que reproduzir) — sempre logar corpo do erro.

## Pendências

- PRECISA MIGUEL: auditoria do vetor SQLi (espelho + canônico) e plano de endurecimento (fail2ban/rate-limit, MyISAM→InnoDB, pm.max_children) — detalhes no fórum.

— ZCode/Kimi K3 (ZM, Dell) · 03/09/2026 08:0x BRT
