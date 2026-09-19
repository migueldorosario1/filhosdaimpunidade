# Memória — Painel CCTV V6: audiência temáticos + página Moka (log técnico, 18/08/2026)

**Missão (ordem do Miguel):** audiência por site na página Temáticos + página /v6/moka com e-mails e audiência/uso detalhado.

## Arquivo e mudanças (Tencent `/home/ubuntu/cafezinho/v6/painel_cctv_v6.py`)

- `ga4_site_30d(prop)` — resumo 30d fechados (activeUsers/screenPageViews/sessions) por propriedade, cache `ga4_site_{prop}.json` 30min.
- `pagina_tematicos()` — linha 📈 30d em cada card + seção tabela com TOTAL (7 sites com GA4; Mapa Rio sem).
- `moka_inbox()` — IMAP `imap.secureserver.net:993` (info@mokareader.com), senha do `.env` do pontos_api, `decode_header` em From+Subject, cache `moka_inbox.json` 10min.
- `moka_pontos()` — sqlite3 em `/home/ubuntu/moka/pontos_api/moka_pontos.db`, cache 10min.
- `moka_ga4()` — totais 30d + country (top12) + deviceCategory + engajamento; exige `MOKA_GA4_PROPERTY = os.environ.get("GA4_PROPERTY_MOKA", "")`; cache `moka_ga4.json` 30min.
- `pagina_moka()` + NAV `("/v6/moka","☕ Moka","moka")` + `ROUTES["/moka"]` + CSS `.tabela`/`.num`.

## Comandos/provas

- Backup servidor: `painel_cctv_v6.py.bak_pre_tematicos_audiencia_moka_20260818`.
- Fluxo: scp local↔servidor; `python3 -m py_compile` no servidor (3.12.3) ✅ — local 3.10 NÃO compila o arquivo (f-strings PEP 701 pré-existentes, ex. linha ~3550 `f"{i["mult"]}×"`); usar sempre o py_compile do servidor.
- `sudo -n systemctl restart cctv-v6` (unit `/etc/systemd/system/cctv-v6.service`, User=ubuntu, WorkingDirectory=/home/ubuntu/cafezinho/v6, sem Environment hoje).
- Provas: `/tematicos` 200, TOTAL 604 usuários (MT 12 · RC 261 · Aiatolah 60 · GSN 164 · RailPost 43 · Discover 14 · Ceará 50); `/moka` 200, e-mails decodificados, aviso GA4 correto. 1ª carga 13s/10s; quente 2ms.
- Cache em arquivo sobrevive a restart (`V6_CACHE = AGENT_DATA/cctv/v6`) — apagar JSON manualmente ao mudar lógica de dado.

## Descobertas de contexto

- IDs numéricos GA4 dos 7 temáticos já estavam no dict TEMATICOS ("ga4": 546667776 Mundo Trilhos, 546673810 RioCarta, 546675625 Aiatolah, 546677232 GSN, 546679970 RailPost, 546669474 Discover, 546675232 Ceará).
- O ga4.json **canônico do painel** é `BASE_DIR/root/ga4.json` (BASE_DIR=`/home/ubuntu/cafezinho/Projeto Cafezinho Agentes`) — o de cing_sync/root_copy DÃO 401 na Admin API; o canônico funciona na Data API para TODOS os temáticos + Cafezinho (147.946 usuários 30d).
- Admin API (`google-analytics-admin`, instalada com --break-system-packages) falha UNAUTHENTICATED com a SA — criação de propriedade só no console.
- E-mail da SA p/ concessões: `augusto-arquivista@gen-lang-client-0200069757.iam.gserviceaccount.com`.

## Pendências (atualizado 19/08 01:35)

1. ~~Miguel colar o ID numérico GA4 do Moka~~ ✅ **FEITO:** `550658820` (conta `a405267492`, separada da do Cafezinho); env na unit + daemon-reload + restart + página acesa com dados.
2. ~~Se 403: Miguel adiciona a SA~~ ✅ **FEITO:** SA já estava como **Editor** na conta do Moka (o Miguel adicionou antes do teste) — leitura OK.
3. **Gotcha de métrica:** `averageEngagementTimePerSession` não existe na Data API (400) — usar `averageSessionDuration`.
4. RailPost: tag G- não encontrada no site (grep) mas propriedade tem 43 usuários — conferir alinhamento tag×propriedade.
5. Mapa Rio sem GA4 (instalar = propriedade nova + tag no site).

**Tema Duplo:** `Foruns/forum_painel_v6_tematicos_audiencia_moka_20260818.md` · catalogado em OBSERVABILIDADE + ATUALIZACOES + monitor.
