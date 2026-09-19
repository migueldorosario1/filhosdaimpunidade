# 🧠 Memória — Build da Central de Alertas (06/08/2026)

> **Fórum (decisões/resumo):** `Foruns/forum_central_alertas_20260806.md`
> **Sessão:** ZCode (Kimi K3), chat direto. Host: `142.93.48.252` (ex-gsn-youtube-nyc-01).

## Linha do tempo do build

1. **Docker 29.7.2** instalado (repo oficial Docker, Ubuntu noble).
2. **Container:** `docker run -d --restart=always -p 127.0.0.1:3001:3001 -v uptime-kuma:/app/data --name uptime-kuma louislam/uptime-kuma:1` — bind **localhost** (segurança; acesso via túnel SSH).
3. **Setup do admin:** o assistente web (Vue SPA) não aceitou submit pelo backend de navegador do ZCode (cliques/Enter/coordenada — todos falharam; servidor nunca recebia o POST). **Solução de contorno:** criar o user direto no SQLite do container:
   - bcrypt via `/app/node_modules/bcryptjs` do próprio container + `sqlite3` CLI do container
   - `INSERT INTO "user" (username, password, active) VALUES ('miguel', '<hash bcrypt>', 1)`
   - **restart do container obrigatório** (o servidor cacheia "No user, need setup" do boot).
   - Senha gerada e gravada no cofre `Outros/chaves/uptime_kuma_central_alertas.env` (600, nunca impressa). Foi exposta acidentalmente em snapshot de página DENTRO da sessão local (visível só ao Miguel na máquina dele); canônica é o arquivo do cofre.
4. **Monitores + notificação semeados via SQL** (mesma rota DB): 15 monitores iniciais + `notification` + `monitor_notification` links → restart → heartbeats em ~60s.
5. **Bugs encontrados e fixes (lições permanentes):**
   - `type='tcp'` → **"Unknown Monitor Type"**; o correto no Kuma v1 é **`type='port'`** (TCP Port). Atenção: update inline via SSH+sqlite com aspas escapadas executou `SET type=port` **sem aspas** → SQLite copiou o valor da COLUNA `port` (443) para `type` — bug silencioso descoberto com SELECT diagnóstico. **Regra: SQL não-trivial SEMPRE via arquivo (.read), nunca inline em SSH.**
   - `notification.config` exige `"type":"telegram"` **dentro** do JSON — sem ele, down events logam "Cannot send notification … Notification type is not supported". Fix: `json_set(config, '$.type', 'telegram')`.
   - Deletar monitor via DB com ele rodando em memória → heartbeat posterior dá FK constraint error (benigno; evitar — preferir `active=0` + restart).
   - `df --output=pcent /`: a linha de cabeçalho `Use%` quebra parse ingênuo (vigia_discos v1 → 6 falsos "sem resposta SSH"; fix: filtrar só valores numéricos).
6. **Moka API 8420:** curl externo a partir da central = timeout (000/8s) → **não pública** (correto). Monitor desativado com nota; v2 via SSH interno.
7. **Prova fim-a-fim Telegram:** monitor TESTE2 (port 127.0.0.1:9) → DOWN `ECONNREFUSED` → notificação enviada sem erro nos logs → removido.

## Vigia de Discos

- `/root/vigia_central/vigia_discos.py` (stdlib puro) + `telegram.env` (600) + `estado.json` + cron `42 * * * * # VIGIA_DISCOS_CENTRAL_20260806`.
- Alvos (SSH chave própria da central, já instalada nos 5): NYC-failover root@198.199.121.136 · Rio-ag root@159.89.185.209 · Espelho root@159.65.177.60 · Tencent ubuntu@43.156.151.165:38422 · ServerDo root@190.89.239.65:51439 · + local.
- Limiares: 85% 🟠 / 95% 🔴 / 🟢 normalização / ⚠️ SSH falha; lembrete 24h.
- 1ª execução real: `{"NYC-failover":79, "Rio-ag":87, "Espelho":20, "Tencent":64, "ServerDo":47, "Central":27}` → 1 alerta (🟠 rio-ag 87%).

## Estado final validado (06/08 17:35 UTC)

13 monitores ativos TODOS UP (9×200, 1×401 aceito, TCP 443 up, 2×ping up), 0 erros de envio/tipo nos logs, cron do vigia ativo. Credenciais: cofre local. DB: volume docker `uptime-kuma` (`/app/data/kuma.db`).
