# Memória técnica — LUMINA v2: Umami self-hosted no tencent (26/08/2026, ZCode/Kimi K3)

**Fórum irmão:** `Foruns/forum_plano_telemetria_urgencia_painel_ao_vivo_20260824.md` (adendo 🌙🌙 LUMINA v2).
**Estado:** ✅ NO AR e provado. O que falta / preciso do Miguel: ver adendo do fórum (limpeza .bak sites-enabled, futuro do Matomo, updates exigem tag compatível Node 18).

## Componente por componente (tencent = ssh tencent, 43.156.151.165:38422, ubuntu)

1. **PostgreSQL 16.15** (`apt install postgresql postgresql-contrib`; `systemctl enable --now postgresql`). Role `umami` + db `umami` (owner). Senha aleatória; verificador SCRAM do pg_shadow NÃO serve como senha — reset via `ALTER USER` com texto puro.
2. **Umami v2.20.2** em `/opt/umami` (git checkout tag; master 20/08 = Next 16 = Node 20+, incompatível c/ Node 18.20.8 global — NÃO mexer no Node global). `npm install --legacy-peer-deps` (1488 pkgs, 7min) · `npm run build` (check-env→prisma→check-db→tracker→recorder→geo→next --turbo; NODE_OPTIONS max-old-space 3072) · migrações aplicadas no build (12 tabelas).
   - `.env`: `DATABASE_URL=postgresql://umami:***@localhost:5432/umami`, `PORT=3000`, `TRACKER_SCRIPT_NAME=lumina.js` (anti-bloqueador).
3. **systemd** `/etc/systemd/system/umami.service` (User ubuntu, `npm start`, Restart=always, log `/var/log/umami.log`, enabled). Health: `:3000` → 307 redirect login; `/lumina.js` 200.
4. **Contas via API** (login retorna `token` no corpo; usar header `Authorization: Bearer`): admin default admin/umami **trocado** (nova senha em `/root/.umami_admin`, 600); usuário leitor `lumina` role **user** (cria/visualiza apenas o website dele); website `O Cafezinho` / domain `ocafezinho.com` (backend normaliza `www.`). Config do leitor em `/home/ubuntu/cafezinho/v6/.lumina_umami.json` (600): base/website_id/api_user/api_password.
5. **Nginx tencent** `/etc/nginx/conf.d/painel.conf` (+`bak_lumina_20260826`): `location = /luz/lumina.js` e `location = /luz/api/send` → `127.0.0.1:3000` (só isso público pela :80; dashboard NÃO exposto; :3000 segue fechada no ufw).
6. **Nginx site** (cafezinho-wp) `/etc/nginx/sites-enabled/ocafezinho.com.conf` (backup em `/etc/nginx/backups/…bak_lumina_20260826` — nunca em sites-enabled): `/luz/lumina.js` e `^~ /luz/api/` → `http://43.156.151.165/luz/...` (porta 80). Cloudflare na frente: entrada 404 da janela de transição expirou sozinha (~4min); hoje URL limpa 200 HIT.
7. **WordPress:** mu-plugin `/var/www/ocafezinho/wp-content/mu-plugins/cafezinho-lumina-umami.php`: snippet `wp_head` (`async src="/luz/lumina.js" data-website-id=1217245a-… data-host-url="/luz"`) + filtro `rocket_delay_js_exclusions` (lição das ~20h: delay_js do WP Rocket segurava beacons).
8. **Painel CCTV** `painel_cctv_v6.py` (backup `.bak_lumina_20260826`; ast.parse antes do restart; 6826→6935 linhas): helpers `_umami_cfg/_umami_token/_umami_api/_umami_svg_24h` + `pagina_lumina` reescrita (Umami). Helpers Matomo (_lumina_resumo/_lumina_series/_lumina_svg_audiencia) INTACTOS (Baleia/vertices). Página: ONLINE grande (API `/active`), cards do dia (`/stats` startAt=meia-noite BRT), gráfico 24h (`/pageviews?unit=hour&timezone=America/Sao_Paulo`), cards FAROL/GA4.

## API v2.20 (rotas usadas)
- `POST /api/auth/login {username,password}` → `{token,user}` (Bearer depois)
- `GET /api/websites/:id/active` → `{visitors}`
- `GET /api/websites/:id/stats?startAt&endAt` → `{pageviews:{value,prev}, visitors, visits, bounces, totaltime}` (não existe mais /api/website/:id/stats antigo)
- `GET /api/websites/:id/pageviews?startAt&endAt&unit=hour&timezone=America/Sao_Paulo` → `{pageviews:[{t,y}],sessions:[{t,y}]}`
- `POST /api/websites/:id` não usado; criação: `POST /api/websites {name,domain}` como dono leitor
- Beacon: `POST /api/send {"type":"event","payload":{website,hostname,url,...}}` (schema NOVO com type/payload)

## Provas (26/08 ~21:05-21:13 BRT)
interno `:8084/lumina` 200 (ONLINE 17, 21 pv hoje, 19 pessoas, 18 visitas) · público `http://43.156.151.165/v6/lumina` 200 · `https://www.ocafezinho.com/luz/lumina.js` 200 · beacon 200 → stats subiram · snippet na home provado · 8 rotas do painel + `/api/audiencia-vertices` 200 · sem erros no journal do cctv-v6 · segredos 600.

## Scripts de suporte no tencent (/opt/umami)
`lumina_provision2.js` (contas/website), `lumina_admin_reset.js` (reset admin via bcrypt no banco), `lumina_apitest.js` (prova stats/pageviews). Podem ser reaproveitados em rerun (idempotentes).
