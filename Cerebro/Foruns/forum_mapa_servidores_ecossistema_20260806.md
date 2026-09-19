# 🗺️ Fórum — Mapa de Servidores do Ecossistema (auditoria ao vivo 06/08/2026)

> **Pedido do Miguel (06/08 ~12:30 BRT):** "pesquisa o que está sendo usado DE FATO em Nova York intensamente e no Alibaba — faz um mapa completo dos servidores usados no nosso ecossistema, investiga a fundo".
> **Método:** auditoria SSH **read-only** ao vivo em todas as máquinas conhecidas (uptime, load, processos, crontabs, serviços systemd, portas, disco, logins) + DNS dos domínios + confronto com `CEREBRO_NODE_ARQUITETURA.md` e `CEREBRO_NODE_CUSTOS_REAIS_MENSAL.md`.
> **Memória técnica (logs completos):** `Memorias/memoria_mapa_servidores_ecossistema_20260806.md`.

---

## 🎯 Resposta direta ao Miguel

### Nova York — o que está sendo usado INTENSAMENTE de fato

**Dois droplets carregam o ecossistema nas costas:**

1. **`198.199.121.136` — `Cafezinho-failover-vigia`** — o nome mente: não é failover dormente, é **a máquina de produção do enxame V4 do Cafezinho**. ~30 crons ativas: coletores V4 (geopolítica/ciência/nacional) + intake + draft workers a cada 30 min, comentarista V4, auditor de títulos GPT, manchete, repetidor estatal, SEO pruning, indexador Google, PageSpeed/GSC/GA4, mídia (promoter/expander), Ceará hourly, fiscal de tokens, coletor de custos. Bots Telegram **Augusto** e **Mayra** como serviços systemd. Stack WP completo (nginx+php8.3+MariaDB) dormente para failover. **Disco 94% — alerta.**

2. **`159.89.185.209` — `Rio-Carta-Agentes`** — a **fábrica dos satélites**: Cícero/Ceará Digital (a cada 30 min + publicador :23), GSN coleta (:12) e publicação (1/9/17h), agente ferroviário (Mundo Trilhos/Rail Post) 2 em 2h, agente turismo (Discover Brazil) 4×/dia, indexador Google :30, painel admin Cícero (:5000) + Caddy. **Disco 100% CHEIO — emergência.**

### Alibaba — a verdade

**O Alibaba (`39.106.184.215`) está MORTO.** 100% de perda de pacote (ping) e SSH timeout em duas tentativas (06/08 ~15:15 UTC). Confirma o nodo de custos: marcado LEGACY em 29/07 ("desligar"). **Pergunta que segue aberta: a cobrança parou de fato?** Verificar console/fatura Alibaba — se ainda cobra, é dinheiro jogado fora (~US$ 10–20/mês).

---

## 🗺️ O mapa completo (11 máquinas + nuvem gerenciada)

### 🇺🇸 DigitalOcean NYC (conta migueldorosario2@gmail.com)

| # | IP | Hostname | Papel DE FATO (06/08) | Intensidade |
|---|---|---|---|---|
| 1 | `198.199.121.136` | `Cafezinho-failover-vigia` | **Produção enxame V4 Cafezinho** + bots Augusto/Mayra + failover WP + banco_custos | 🔴 INTENSA (~30 crons; disco 94%) |
| 2 | `159.89.185.209` | `Rio-Carta-Agentes` | **Fábrica satélites**: Ceará/Cícero, GSN, ferroviário, turismo | 🔴 INTENSA (crons 30min; disco 100% 🚨) |
| 3 | `159.65.177.60` | `cafezinho-news-espelho` | Espelho cafezinho.news (sync horário :17), nginx+MariaDB | 🟡 LEVE (1 cron) |
| 4 | `142.93.48.252` | `gsn-youtube-nyc-01` | Era executor YouTube GSN; **só Prometheus a cada 5 min** | 💤 OCIOSO (candidato a desligar) |
| 5 | `174.138.36.31` | `riocarta-wordpress` (legacy) | — | ⛔ MORTO/inacessível (100% perda) |

### 🇨🇳 China / Singapura

| # | IP | Hostname | Papel DE FATO | Intensidade |
|---|---|---|---|---|
| 6 | `43.156.151.165:38422` | Tencent Singapura `VM-0-6-ubuntu` | **Painéis** (CCTV v5/v6, editorial, mídia-ouro) + **Banco Ouro MASTER** + **Moka pontos_api (:8420)** + pulse 10min | 🔴 INTENSA (uptime 16 semanas; disco 64%) |
| 7 | `82.156.167.218` | Beijing "Alfândega" (GSN) | Era executor agentes GSN — função já migrada p/ Rio-Carta-Agentes | ⛔ INACESSÍVEL (100% perda) |
| 8 | `39.106.184.215` | **Alibaba Beijing** | Era "Cérebro Vivo/Oficina"; LEGACY 29/07 | ⛔ **MORTO — confirmar fim da cobrança** |

### 🇧🇷 Brasil

| # | IP | Hostname | Papel DE FATO | Intensidade |
|---|---|---|---|---|
| 9 | `190.89.239.65:51439` | `us65.serverdo.in` (ServerDo.in) | **WordPress canônico ocafezinho.com** (Cloudflare na frente); nginx+MySQL+PHP7.4/8.3+Redis+Zabbix | 🔴 INTENSA (load 19, mysqld 202% CPU; **reboot diário ~03:31** — investigar se é proposital) |
| 10 | `159.89.237.100` | (GSN WordPress, DO) | Pinga, mas SSH negado e HTTP sem resposta; globalsouth.news hoje é Vercel | 👻 ZUMBI (provável legacy) |

### ☁️ Sem servidor próprio (Vercel/GitHub/B2)

- **Vercel** (76.76.21.21 / 216.150.1.65 / 216.198.79.1): globalsouth.news, mundotrilhos.com, railpost.news, discoverbrazil.news, mapario.com.br, mokareader.com (Moka + Moka Writer)
- **Cloudflare**: frente do ocafezinho.com (104.21.15.101) → origem ServerDo
- **Backblaze B2 + Google Drive**: backups (sem máquina)
- **Domínios sem DNS ativo:** riocarta.com.br, riocarta.news, cearadigital.com.br, moka.mokareader.com

## 🚨 Alertas operacionais (ordem de urgência)

1. **🚨 Rio-Carta-Agentes DISCO 100%** (24G/24G, 0 livre) — agentes podem falhar silenciosamente; rsyslogd a 44% CPU. Maiores: cicero_remote 4.1G, riocarta_remote 3.8G, gsn_remote 1.8G, logs 1.4G, zip votação 553M.
2. **⚠️ NYC principal DISCO 94%** (45G/48G) — backups locais 8G + venv 7.7G são os maiores; mesma doença chegando.
3. **💰 Alibaba morto — confirmar que a fatura parou** (era alavanca de economia nº 2 do nodo de custos).
4. **💰 gsn-youtube-nyc-01 ocioso** (~US$ 6/mês) e **riocarta-wordpress morto** (~US$ 6/mês) — destruir no painel DO se confirmados.
5. **🔍 ServerDo reboot diário 03:31** — uptime nunca passa de 24h; checar se é cron do provedor ou crash.
6. **👻 GSN WP (159.89.237.100)** — zumbi; decidir destino.

## Custos de servidor (do nodo de custos, cruzado)

| Máquina | US$/mês |
|---|---|
| NYC failover-vigia | 6 |
| Rio-Carta-Agentes | 6–12 |
| cafezinho-news-espelho | 6–12 (4GB → provável 12) |
| gsn-youtube (ocioso) | 6 |
| riocarta-wp (morto) | 6 |
| Tencent Singapura | 15–25 |
| Alibaba | 0 **se desligado de fato** |
| ServerDo.in | 10–30 (R$ 50–150) |

**Decisões pendentes do Miguel:** (a) confirmar fim cobrança Alibaba; (b) autorizar faxina de disco nos 2 NYC lotados; (c) destruir droplets mortos/ociosos; (d) GSN WP zumbi; (e) reboot diário ServerDo.
