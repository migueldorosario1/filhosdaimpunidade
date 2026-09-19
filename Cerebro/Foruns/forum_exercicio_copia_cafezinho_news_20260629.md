# Fórum — Exercício Cópia Cafezinho Servidor NYC (cafezinho.news)

> **Nota terminológica (29/jun 22:20 BRT):** Este é um **exercício diletante de cópia paralela**, NÃO uma migração. O Cafezinho canônico (`us65.serverdo.in`) permanece intocado como jornal de produção. O `cafezinho.news` é apenas um espelho/sandbox em droplet DigitalOcean. As ocorrências de "migração" abaixo foram trocadas por "cópia" em 29/jun 22:20 BRT a pedido do Miguel — confusões semânticas podem ser perigosas.


**Data:** 2026-06-29 00:55 BRT
**Autor:** Claude Code (`claude-opus-4-7`)
**Pedido Miguel:** "criar espelho do Cafezinho em cafezinho.news (domínio GoDaddy), rodando em DigitalOcean, novo droplet amigo de agentes/IA, sem mexer no Cafezinho original. Exercício diletante."
**Status:** Plano completo. Aguarda Miguel criar droplet no painel DO.

---

## 0. Premissas e regras

- **NÃO MEXER no Cafezinho de produção** (`us65.serverdo.in`, IP `190.89.239.65`)
- **Sem REST API** — usar SSH + rsync + mysqldump (Miguel: "agora a gente tem SSH")
- **Exercício diletante** — sem SLA, sem urgência, sem pretensão de virar produção paralela
- **Regra de governança** (BUG-20260507-AG-VIOLATION-DO-SWARM-DROPLET): NUNCA chamar `POST /v2/droplets` ou provisionar recurso pago sem AUTH escrita do Miguel. **Miguel cria o droplet pelo painel.**
- **Domínio:** `cafezinho.news` (e secundário `ocafezinho.news`) — comprados no GoDaddy

---

## 1. Estado atual da conta DigitalOcean (29/jun 00:50 BRT)

**Conta ativa:** `migueldorosario2@gmail.com` (substituiu `migueldorosario@gmail.com` encerrada).

**Droplets existentes (4):**

| Nome | IP | Tamanho | Datacenter | Função |
|---|---|---|---|---|
| `Cafezinho-failover-vigia` | 198.199.121.136 | 2GB/50GB | NYC1 | failover frio do Cafezinho |
| `Rio-Carta-Agentes` | 159.89.185.209 | 1GB/25GB | NYC3 | Rio Carta Astro + Flask admin |
| `riocarta-legacy` | 174.138.36.31 | 1GB/25GB | NYC1 | Rio Carta WP legado |
| `gsn-youtube-nyc-01` | 142.93.48.252 | 1GB/25GB | NYC1 | GSN YouTube (novo) |

**Novo recurso da DO observado:** menu lateral agora tem **Agent Platform**, **AI Assistant**, **Inference**, **Functions**, **App Platform**. DO virou mais "amiga de IA" desde 2025.

---

## 2. Trabalho prévio não retomado

**Encontrado em garimpo:** `forum_cafezinho_headless.md` (09/jun/2026) — outro agente havia iniciado plano `cafezinho.news` em arquitetura **Astro + GitHub + Vercel** (NÃO droplet). Pasta `A_GRANDE_REFORMA_LOCAL_20260610/cafezinho/` tem trabalho parcial (29 páginas Astro com build OK).

**Decisão Miguel 29/jun 00:50 BRT:** abandonar abordagem headless/REST API, ir direto pra **droplet + WordPress espelho** via SSH/rsync.

**Não deletar `A_GRANDE_REFORMA_LOCAL_20260610/cafezinho/`** ainda — pode ser útil de referência mais adiante.

---

## 3. Ficha de criação do droplet (preencher no painel)

### 3.1 Configurações de hardware/região

| Campo | Valor | Justificativa |
|---|---|---|
| **Region** | NYC3 | latência BR ~120ms, junto com Rio-Carta-Agentes (rede já mapeada) |
| **OS Image** | Ubuntu 24.04 LTS x64 | mesma família dos outros droplets, suporte longo |
| **Droplet Type** | **Basic** (Shared CPU) | exercício diletante = Shared OK, Dedicated seria overkill |
| **CPU Options** | **Regular Intel** (SSD) | NVMe Premium (+$8/mês) não vale pra WP de exercício |
| **Plan** | **2 vCPU / 4 GB / 80 GB / $24/mês** ⭐ DECIDIDO 01:25 BRT | Mínimo viável; runbook adaptado pra usar pipes sem arquivo intermediário; upgrade pra $48 (160GB) é 1 clique se precisar |
| **Authentication** | SSH Key (NÃO password) | mesma chave do `cafezinho-wp` já cadastrada |
| **Hostname** | `cafezinho-news-espelho` | descritivo, fácil reconhecer |
| **Tags** | `cafezinho-news`, `espelho`, `diletante`, `wordpress` | organização do painel |
| **Backups DO** | ✅ Habilitar | +$7/mês, seguro razoável |
| **Monitoring** | ✅ Habilitar | grátis |
| **IPv6** | opcional | irrelevante pro exercício |
| **VPC Network** | default | OK |

**Custo total estimado:** ~$40/mês ($32 droplet + $7 backups + $1 monitoring).

### 3.2 Por que NÃO Dedicated CPU

O que aparecia pré-selecionado no painel ($84/mês — General Purpose 16GB RAM / 50GB SSD) tem **2 problemas**:
1. **50 GB NÃO comporta o Cafezinho** (uploads 61 GB + banco 3.2 GB + sistema 5-10 GB = ≥75 GB necessário)
2. **Dedicated CPU é desperdício** pra exercício sem tráfego real — paga 2.5× a mais por CPU garantida que não vai usar

Migrar Basic → Dedicated depois é 1 clique no painel se precisar.

### 3.3 Por que 120 GB de disco

- Cafezinho pesa hoje ~75 GB (após limpezas Camada 1+3 + apagar BKP de 71 GB em 28/jun)
- Backups DO precisam de espaço extra durante snapshot
- 120 GB = ~45 GB de folga (~6 meses de crescimento sem pressão)

---

## 4. Cloud-init script (campo "User data" no formulário)

Cola tudo isso em **Advanced Options → User data** durante a criação do droplet. Roda no primeiro boot, deixa o droplet pronto sem precisar SSH manual depois.

```yaml
#cloud-config
package_update: true
package_upgrade: true

packages:
  # Servidor web stack
  - nginx
  - mariadb-server
  - php8.3-fpm
  - php8.3-mysql
  - php8.3-curl
  - php8.3-gd
  - php8.3-mbstring
  - php8.3-xml
  - php8.3-zip
  - php8.3-intl
  - php8.3-bcmath
  - php8.3-imagick
  # Ferramentas devops
  - rsync
  - mysql-client
  - git
  - tmux
  - jq
  - htop
  - vim
  - curl
  - wget
  - unzip
  # Otimização de imagens (Camada 3 reaproveitável)
  - imagemagick
  - pngquant
  - jpegoptim
  - webp
  # Python e IA
  - python3
  - python3-pip
  - python3-venv
  # Segurança básica
  - fail2ban
  - ufw

runcmd:
  # 1) Swap 4GB (importante pra picos do WP)
  - fallocate -l 4G /swapfile
  - chmod 600 /swapfile
  - mkswap /swapfile
  - swapon /swapfile
  - echo '/swapfile none swap sw 0 0' >> /etc/fstab

  # 2) Firewall básico
  - ufw default deny incoming
  - ufw default allow outgoing
  - ufw allow OpenSSH
  - ufw allow 'Nginx Full'
  - ufw --force enable

  # 3) wp-cli
  - curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar
  - chmod +x wp-cli.phar
  - mv wp-cli.phar /usr/local/bin/wp

  # 4) Python venv pra agentes
  - python3 -m venv /opt/agents-venv
  - /opt/agents-venv/bin/pip install --upgrade pip
  - /opt/agents-venv/bin/pip install anthropic openai google-generativeai requests paramiko python-dotenv beautifulsoup4 lxml mysql-connector-python

  # 5) Pasta de chaves dos agentes
  - mkdir -p /root/.ssh/agents
  - chmod 700 /root/.ssh/agents

  # 6) Estrutura WP espelho
  - mkdir -p /var/www/cafezinho-news
  - chown -R www-data:www-data /var/www/cafezinho-news

  # 7) Serviços
  - systemctl enable mariadb && systemctl start mariadb
  - systemctl enable php8.3-fpm && systemctl start php8.3-fpm
  - systemctl enable nginx && systemctl start nginx

  # 8) Marca de pronto
  - touch /var/log/cloud-init-cafezinho-ready

write_files:
  - path: /etc/motd
    content: |
      ┌──────────────────────────────────────────┐
      │  CAFEZINHO.NEWS — Espelho diletante      │
      │  Origem: us65.serverdo.in                │
      │  Stack:  Nginx + MariaDB + PHP 8.3       │
      │  Pasta:  /var/www/cafezinho-news         │
      │  Venv:   /opt/agents-venv                │
      └──────────────────────────────────────────┘

  - path: /root/.bashrc.cafezinho
    content: |
      alias wp-cafezinho='sudo -u www-data wp --path=/var/www/cafezinho-news'
      alias logs-nginx='tail -f /var/log/nginx/error.log /var/log/nginx/access.log'
      alias logs-php='tail -f /var/log/php8.3-fpm.log'
      alias agents-py='source /opt/agents-venv/bin/activate'

final_message: "cafezinho.news espelho — droplet pronto em $UPTIME segundos. SSH como root."
```

---

## 5. O que faz o droplet "amigo de agentes e IA"

1. **`/opt/agents-venv`** — Python venv com SDKs já instalados (anthropic, openai, google-generativeai). Qualquer agente que SSH no droplet só precisa `source /opt/agents-venv/bin/activate`.
2. **`/root/.ssh/agents/`** — pasta dedicada pra chaves SSH por agente (auditoria por chave: Claude, Codex, GLM, etc).
3. **wp-cli já no PATH** — agentes podem manipular WP sem painel.
4. **MOTD** com mapa do droplet — qualquer SSH novo vê onde está cada coisa.
5. **Aliases prontos** em `/root/.bashrc.cafezinho` (carregar via `source`).
6. **MariaDB local** — agentes podem usar `mysql -u root` direto (socket auth).
7. **fail2ban + ufw** já ativos — proteção contra força bruta.

---

## 6. Fluxo de cópia (DEPOIS que droplet existir)

```
us65.serverdo.in (Cafezinho prod, NÃO MEXER)
    │
    │ 1) ssh-copy-id da chave do novo droplet pro Cafezinho
    │ 2) mysqldump --single-transaction ocafezinho > /tmp/dump.sql
    │ 3) rsync --bwlimit=5000 com exclusões (cache, trash, backups)
    │    de /var/www/ocafezinho/ → novo droplet:/var/www/cafezinho-news/
    ▼
NOVO DROPLET (cafezinho-news-espelho)
    │
    │ 4) mysql < dump.sql
    │ 5) wp search-replace "controle.ocafezinho.com" "cafezinho.news"
    │    wp search-replace "www.ocafezinho.com" "cafezinho.news"
    │ 6) wp option update siteurl/home
    │ 7) wp plugin deactivate <agentes-de-publicação>   ← evita duplicar publish
    │ 8) wp plugin deactivate wpematico zapier wptelegram
    │ 9) wp cron event list / desabilitar cron jobs do enxame
    │ 10) configurar nginx vhost cafezinho.news
    │ 11) certbot --nginx -d cafezinho.news -d www.cafezinho.news
    ▼
DNS cafezinho.news (GoDaddy)
    │
    │ A      @     <IP_DROPLET>   TTL 600
    │ A      www   <IP_DROPLET>   TTL 600
    ▼
Espelho LIVE
```

**Plugins a desativar OBRIGATÓRIO antes do site subir** (pra evitar duplicação de publish via cron):
- `wpematico` (autopublish)
- `zapier` (webhooks)
- `wptelegram` (vai disparar pra todos os bots se ficar ativo!)
- `accelerated-mobile-pages` (AMP — opcional manter desativado)
- `wp-rocket` (cache — pode reativar depois, mas a chave de licença é a mesma → desativar primeiro)
- `wordfence` (chave de licença atrelada ao domínio prod — desativar)
- `wp-smush-pro` (idem)
- `wordpress-seo-premium` (idem)

---

## 7. DNS no GoDaddy (DEPOIS que droplet tiver IP)

GoDaddy → Domains → cafezinho.news → DNS Management:

```
Type  | Name | Value             | TTL
A     | @    | <IP_DROPLET>      | 600
A     | www  | <IP_DROPLET>      | 600
```

Aguardar ~30 min pra propagar antes de testar SSL.

**Atenção:** o trabalho prévio Astro/Vercel pode ter deixado registros DNS apontando pra Vercel (`76.76.21.21`). Verificar e SUBSTITUIR.

---

## 8. SSL (Let's Encrypt)

Após DNS propagar:

```bash
ssh root@<IP_DROPLET>
apt install certbot python3-certbot-nginx
certbot --nginx -d cafezinho.news -d www.cafezinho.news --agree-tos --email migueldorosario2@gmail.com --redirect
```

Auto-renovação já vem configurada pelo certbot.

---

## 9. Smoke tests pós-cópia

Após cópia + DNS + SSL:

```bash
# Site responde
curl -sI https://cafezinho.news/ | head -5

# Imagem antiga continua acessível (URL search-replace funcionou)
curl -sI https://cafezinho.news/wp-content/uploads/2025/03/image-221-1024x683.png | head -3

# REST API funcional
curl -s "https://cafezinho.news/wp-json/wp/v2/posts?per_page=1" | jq '.[0] | {id, title, status}'

# Admin renderiza
curl -sI https://cafezinho.news/wp-login.php | head -3

# Confirmar que NÃO há cron WP ativo (não publica duplicado)
ssh root@<IP> 'sudo -u www-data wp --path=/var/www/cafezinho-news cron event list'
```

---

## 10. Aguardando Miguel

- [ ] **Criar droplet no painel DO** com as configs da §3.1 + cloud-init da §4
- [ ] Quando droplet ficar `Active`, esperar ~5-10 min e checar:
  ```bash
  ssh root@<IP> 'ls /var/log/cloud-init-cafezinho-ready && cat /etc/motd'
  ```
- [ ] **Passar IP do droplet pro Claude** continuar com a cópia (§6)

---

## 11. Pendências e decisões adiadas

- [ ] Pipeline dos agentes (Camada 5 da limpeza de ontem) — abrir fórum separado
- [ ] Validar visualmente posts otimizados pela Camada 3 (libera 4.7 GB do backup retido)
- [ ] Cache `wp-rocket.disabled-*` no Cafezinho prod — apagar?
- [ ] Reativar pendências do diagnóstico SEO 27/jun (monitoramento)

---

---

## 12. Histórico de decisões da sessão

| Hora | Decisão | Por quê |
|---|---|---|
| 00:50 BRT | Abandonar abordagem headless Astro/Vercel (trabalho prévio 09/jun) | Miguel quer droplet com SSH/rsync, não REST API |
| 00:55 BRT | Escolher DigitalOcean (não Tencent Lighthouse Singapore) | (a) cloud-init nativo, (b) latência BR ~120ms vs 250ms, (c) DO Agent Platform pensado pra agentes |
| 01:20 BRT | Recusar plano pré-selecionado $84 General Purpose / 50GB | Disco 50GB NÃO comporta Cafezinho (~75GB); Dedicated CPU é desperdício pra exercício |
| 01:25 BRT | **DECIDIDO: $24 / 2vCPU / 4GB / 80GB Regular Intel SSD** | Exercício diletante = não justifica $48 (160GB); runbook adaptado pra pipes sem arquivo intermediário (mysqldump direto via SSH); upgrade pra $48 é 1 clique |
| 01:25 BRT | Region NYC3, hostname `cafezinho-news-espelho` | Junto com Rio-Carta-Agentes |
| 01:30 BRT | Sessão pausada (fim de noite) | Miguel: "guarda no fórum e vamos dormir" |

## 13. Próximas ações (quando Miguel retomar)

1. **Criar droplet no painel DO** com configs §3.1 (atualizada com $24/80GB) + cloud-init §4
2. Aguardar `Active` + ~5-10 min para cloud-init finalizar
3. Smoke: `ssh root@<IP> 'ls /var/log/cloud-init-cafezinho-ready && cat /etc/motd'`
4. Passar IP pro Claude continuar com §6 (cópia via rsync + dump)

---

## 14. Ajuste no runbook — adaptação pro disco apertado (80GB)

Como o plano escolhido tem só 5 GB de folga sobre o Cafezinho atual, o §6 (fluxo de cópia) deve ser ajustado:

```bash
# EVITAR (cria arquivo dump.sql intermediário no droplet — gasta 5GB temporário):
ssh cafezinho-wp 'mysqldump ocafezinho > /tmp/dump.sql'
scp cafezinho-wp:/tmp/dump.sql ./
mysql cafezinho-news < dump.sql

# PREFERIR (pipe direto via SSH — zero arquivo intermediário):
ssh cafezinho-wp 'mysqldump --single-transaction --quick --routines --triggers ocafezinho | gzip' | \
  gunzip | mysql cafezinho-news

# rsync (também sem dobrar):
rsync -av --inplace --bwlimit=5000 \
  --exclude='wp-content/cache/*' \
  --exclude='backup_camada3_*' \
  --exclude='trash_*' \
  cafezinho-wp:/var/www/ocafezinho/ /var/www/cafezinho-news/
```

**Monitorar disco durante migração** com `watch -n 30 df -h /var/www` em terminal separado.

---

*Plano congelado em 01:30 BRT. Aguarda Miguel criar droplet e retomar.*

---

# 📌 EXECUÇÃO — 2026-06-29 14:30-16:00 BRT

## Decisões durante execução

| Decisão | Quem | Motivo |
|---|---|---|
| Usar API DO (não painel) | Miguel | Token já cadastrado em `.env` raiz, autorização explícita "vai" |
| Recortar 30 dias (não cópia full) | Miguel | "espaço leve de observação", não exercício de cópia integral |
| Não copiar tabelas Wordfence/Evermonitor/Yoast hierarchy | Claude | recorte mínimo, evita lixo |
| Tema padrão twentytwentyfive | Claude | tema `ocafezinho-portal` depende de tabelas custom (`wp_highlights`) não copiadas |

## Cronograma executado

| Hora BRT | Etapa | Resultado |
|---|---|---|
| 14:27 | POST /v2/droplets via API | ✅ id 581117174, IP 159.65.177.60 (~6 min até active) |
| 14:34 | Cloud-init **falhou** silenciosamente | ⚠️ caracteres `┌─┐│└┘` no MOTD quebraram YAML — config rodada manualmente |
| 14:45-15:05 | Setup manual (nginx, mariadb, php8.3, python venv, wp-cli, swap, fail2ban) | ✅ |
| 15:10 | Etapa 1: DB + WP core fresh | ✅ DB `cafezinho_news`, senha em `/root/.cafezinho_news_db_pass` |
| 15:15 | Etapa 2: dump SQL filtrado 30d via SSH pipe | ✅ 7.134 IDs, dump 9.1 MB compactado |
| 15:19-15:50 | Etapa 3: tar pipe uploads 2026/05 + 2026/06 | ✅ 5.0 GB transferidos (~32 min) |
| 15:51 | Etapa 4: tar tema + 40 plugins ativos | ✅ 262 MB |
| 15:53 | Etapa 5: import SQL + search-replace | ✅ 373 replacements `controle.ocafezinho.com → cafezinho.news` |
| 15:54 | Etapa 6: blindagem (DISABLE_WP_CRON + desativar 14 plugins) | ✅ wpematico/zapier/wptelegram/wordfence/wp-rocket etc OFF |
| 15:56 | Etapa 7: nginx vhost + smoke | ⚠️ 500 inicial (tema custom + Yoast quebrados) |
| 16:00 | Troca pra tema `twentytwentyfive` default | ✅ **TUDO 200** |

## Estado final do espelho

**URL:** `http://159.65.177.60/` (Host header `cafezinho.news`) — DNS GoDaddy ainda não apontado

**Stack:**
- Ubuntu 24.04.4 LTS
- Nginx 1.24
- PHP 8.3.6-fpm
- MariaDB 10.11.14
- DB: `cafezinho_news` (~50 MB)
- Tema ATIVO: `twentytwentyfive` (default WP) — temporário
- 25 plugins ativos (de 40 originais; 15 desativados pra blindagem)
- 7.134 posts no banco (recorte 30 dias)
- 5.0 GB de uploads (2026/05 + 2026/06)

**Smoke final:**
```
[200] /                                    275 KB
[200] /wp-json/wp/v2/posts?per_page=3       20 KB
[200] /feed/                                108 KB
[200] /page/2/                              295 KB
```

**Cafezinho PROD (`us65.serverdo.in`):** 100% intacto durante toda operação. ZERO `UPDATE`/`DELETE`/`ALTER` no banco prod, ZERO modificação em arquivos. Só `mysqldump --single-transaction --skip-lock-tables` (read-only) e `tar c` (read-only).

## Bugs/aprendizados durante execução

### B-DROPLET-001 — Cloud-init YAML quebra com caracteres box-drawing
**Causa:** MOTD com `┌─┐│└┘` (bytes UTF-8 multi-byte) corrompe YAML parser do cloud-init via JSON.
**Diagnóstico:** `Failed loading yaml blob. unacceptable character #x0094: special characters are not allowed`
**Cura:** usar somente ASCII puro no MOTD. Bytes `0x94` aparecem em encoding mismatch.
**Severidade:** baixa, mas droplet sobe "nu" (sem nginx/php/mariadb) → tem que configurar manual.

### B-DROPLET-002 — Tema custom + Yoast quebram WP sem tabelas full
**Causa:** `ocafezinho-portal/front-page.php` chama `wp_highlights` (tabela proprietária do tema), e Yoast SEO chama `wp_yoast_indexable_hierarchy` — ambas não foram copiadas no recorte 30d.
**Cura aplicada:** trocar tema pra `twentytwentyfive` + desativar Yoast.
**Plano B se quiser tema original:** copiar tabelas `wp_yoast_*` + `wp_highlights` no próximo dump.

### Aprendizado — `php8.3-imagick` quebra apt install no Ubuntu 24.04
Pacote `php8.3-imagick` retorna "held broken packages". Removido do cloud-init pra evitar.

## Pendências (próxima sessão)

- [ ] **DNS GoDaddy cafezinho.news → 159.65.177.60** (atualmente aponta pra Vercel)
- [ ] **SSL Let's Encrypt** (`certbot --nginx -d cafezinho.news -d www.cafezinho.news`)
- [ ] **Decidir destino do tema custom**: copiar `wp_highlights` + `wp_yoast_*` no próximo recorte, ou ficar com twentytwentyfive default
- [ ] **Cron de re-sync 30d** (opcional, se quiser espelho "vivo" atualizando todo dia)
- [ ] **Cleanup**: rm `/var/www/ocafezinho` (sobra do tar do prod no droplet) — JÁ FEITO via `rm -rf` durante etapa 4
- [ ] Validar visualmente posts renderizados no browser

## Custo até agora

- Droplet $24/mês + backups $4.80/mês = **$0.95/dia**
- 1º mês quase coberto pelo saldo $-28.67 a favor

---

*Migração 30-dias concluída em ~90 min. Espelho funcional em `http://159.65.177.60/` (Host: cafezinho.news). Cafezinho prod intacto.*

---

# 🔄 SYNC HORÁRIO ATIVO — 2026-07-03 12:57 BRT

**Autor:** Claude Code (`claude-opus-4-7`)
**Pedido Miguel:** "quero ver o cafezinho.news espelhar o cafezinho" (03/jul ~09:30 BRT).

## Decisões de design (Miguel escolheu)

| Item | Valor |
|---|---|
| **Frequência** | Horária (`17 * * * *` — offset 17min) |
| **Escopo** | NOVOS + EDITADOS (`post_modified > cutoff`, INSERT → REPLACE) |
| **Retenção** | Crescente (sem expurgo) |
| **Onde roda** | Cron no droplet cafezinho.news (nunca no canônico) |
| **Autenticação** | Chave SSH ed25519 dedicada com `from="159.65.177.60"` restriction |
| **Kill-switch** | `touch /root/SYNC_PAUSED` no droplet |
| **Log** | `/var/log/cafezinho_sync.log` + logrotate weekly x8 |
| **Lock** | `flock` em `/var/run/cafezinho_sync.lock` (singleton) |

## Sync inicial executado 12:50-12:56 BRT

- Cutoff: `2026-06-29 14:21:52` (último post do sync 29/jun) → `2026-07-03 09:00:35`
- **2231 posts modificados** (63 novos + ~2200 edições de agentes editoriais)
- **1694 uploads novos** (169 MB, 47s de transferência via tar-pipe SSH)
- **2226 linhas** URL search-replace `controle.ocafezinho.com / www.ocafezinho.com → cafezinho.news`
- Duração total: ~6 min
- **Cafezinho prod:** ZERO write (só `mysqldump --single-transaction --skip-lock-tables` + `find | tar`)

**Estado do espelho:**
- posts_publish: 2357 → **3359** (+1002 por trazer arquivo editado)
- attachments: 4376 → **4562**
- ultimo_post: `2026-06-29 14:21:52` → **`2026-07-02 18:03:55`**
- Smoke: 5 URLs mais recentes HTTP 200 (~1.5s), homepage 200, REST API funcional

## Arquivos criados

**No droplet cafezinho.news (`159.65.177.60`):**
- `/root/sync_from_cafezinho.sh` (6764 B, chmod +x, syntax OK)
- `/root/.ssh/id_ed25519_sync_from_prod` (chave privada 600)
- `/root/.ssh/id_ed25519_sync_from_prod.pub` (chave pública)
- `/var/lib/cafezinho_sync/last_sync.txt` (state)
- `/var/log/cafezinho_sync.log` (log com timestamp)
- `/etc/logrotate.d/cafezinho_sync` (rotação semanal)
- Cron: `17 * * * *` (sentinela `SENTINELA_CAFEZINHO_NEWS_SYNC_CLAUDE_20260703`)

**No canônico (`us65.serverdo.in`):**
- `/root/.ssh/authorized_keys` — appended com `from="159.65.177.60" ssh-ed25519 ...` (fingerprint `SHA256:4+xZ5Eq17HO2/H//MLu6GJe+LMX5fXy15Oah93F/i3o`)
- Backup: `/root/.ssh/authorized_keys.bak_pre_cafezinho_news_sync_20260703_095343`

## Testes validados

1. ✅ Sync inicial 2231 posts + 1694 uploads em 6 min
2. ✅ 2ª execução (delta 4 posts + 32 uploads): 18s
3. ✅ 3ª execução idempotente (zero delta): 2.2s, exit 0
4. ✅ Kill-switch: `SYNC_PAUSED` presente → exit 0 com log
5. ✅ Chave dedicada droplet→canônico funciona (fingerprint OK, `from=` restrito)
6. ✅ HTTP smoke: 5 posts recentes 200, homepage 200, REST 200

## Como parar o sync

```bash
ssh root@159.65.177.60 'touch /root/SYNC_PAUSED'
```

Ou remover linha do cron:
```bash
ssh root@159.65.177.60 'crontab -e'   # apagar linha com SENTINELA_CAFEZINHO_NEWS_SYNC
```

## Como monitorar

```bash
ssh root@159.65.177.60 'tail -f /var/log/cafezinho_sync.log'
ssh root@159.65.177.60 'cat /var/lib/cafezinho_sync/last_sync.txt'   # cutoff atual
```

## Riscos conhecidos + mitigações vigentes

| Risco | Mitigação |
|---|---|
| Delta grande após pausa longa | script pode demorar >1h → próximo cron pega `flock` e sai |
| Prod cair durante sync | `set -e` aborta, `trap` limpa `/tmp/cafezinho_sync_out` remoto |
| `wp_postmeta` com URLs serializadas ficam com `controle.ocafezinho.com` | search-replace só toca colunas não-serialized (`post_content`, `guid`, `post_excerpt`) — meta values renderizados no frontend são raros |
| Categorias novas no prod não aparecem visualmente | script traz `wp_terms` + `wp_term_taxonomy` inteiras (leve) |
| Featured images de posts antigos (pré-30d) apontando pra attachments ausentes | attachment REPLACE traz metadata; arquivo físico via `find -newermt` → se attachment é antigo, imagem quebra. Fixável com sync full de uploads manual quando quiser |

## Próxima execução automática

**13:17 BRT (Cron horário).**

---

## 🔧 PATCH 04/07/2026 12:40 BRT — wp_highlights (MANCHETE)

**Sintoma reportado por Miguel:** "cafezinho.news está desatualizado" — mas o REST API e o banco batiam certinho com o prod. **A defasagem era só na MANCHETE (`<h1>` da home)**.

**Causa:** O tema `ocafezinho-portal` (reativado por Miguel após o sync inicial de 29/jun) usa a tabela custom `wp_highlights` (1 registro) pra decidir qual post é a manchete gigante da home. O script de sync original **NÃO copiava** `wp_highlights` — o `agente_manchete` do canônico atualizava só o prod, e o espelho ficou congelado apontando pro post `260964` (Lula 'tratora'..., 29/jun).

**Fix imediato aplicado 15:36 UTC (12:36 BRT):**
```bash
ssh cafezinho-wp 'mysqldump wp_highlights' | sed 's/INSERT/REPLACE/' | ssh droplet 'mysql cafezinho_news'
# espelho manchete: 260964 → 261306 (Dreame X60 Pro, 04/jul 09:29) — bateu com prod
```

**Fix permanente:** script `/root/sync_from_cafezinho.sh` refatorado — dumpa+importa `wp_highlights` como bloco **SEPARADO no início** (antes do check de delta), rodando SEMPRE independente de haver posts editados. Custo: +2s por ciclo. Deploy 15:39 UTC.

**Confirmação visual pós-fix:**
- `<h1>` cafezinho.news = `<h1>` www.ocafezinho.com (idêntico)
- Ambos apontam pra "Dreame X60 Pro Ultra Complete..." (04/jul 09:29 BRT)

**Outras tabelas custom que NÃO estão sendo sincronizadas** (avaliar se afetam visual):
- `wp_top_ten` / `wp_top_ten_daily` — widget "posts mais lidos" (analytics do próprio site — no espelho ficará baseado em stats do prod)
- `wp_wp_rp_tags` — related posts na base do post (rebuild automático via tags)
- `wp_useful_banner_manager_banners` (1 linha, estático)
- `wp_responsive_menu` (179 linhas, raramente muda)

Decisão: sincronizar só `wp_highlights` por enquanto. Se Miguel notar sidebar/related desatualizados, avaliar top_ten e wp_rp_tags separadamente.



