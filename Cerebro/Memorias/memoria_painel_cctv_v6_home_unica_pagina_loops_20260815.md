# Memória técnica — Painel CCTV V6: página Loops + Home única + automação 30/30min (15/08/2026)

Sprint ZCode (Kimi K3), ordem do Miguel ~12:00 BRT. Log completo para retomada.

## Topologia confirmada (antes de mexer)

- Painel V6: processo `python3 painel_cctv_v6.py` em `/home/ubuntu/cafezinho/v6/` na Tencent (`china` = 43.156.151.165:38422, user ubuntu), porta 8084, unit systemd **`cctv-v6.service`**.
- Nginx porta 80: `/etc/nginx/conf.d/painel.conf` — `/v6/`→8084, `/v5/`→8082, `/v5/editorial/`→8083, `/midia-ouro/`→8091, `/painel/`→estáticos `/var/www/html/`. Raiz `/` era o "Welcome to nginx!" (ninguém usava).
- Nginx porta 8080: `/etc/nginx/sites-enabled/cctv` (legado v3/mídia).
- `/root/Cerebro` na Tencent está **DESATUALIZADO** (junho) — não usar como fonte.
- A fonte viva dos fóruns no servidor é `/home/ubuntu/cafezinho/v6_data/foruns/`, alimentada pelo cron **local** do PC do Miguel: `7,37 * * * * rsync -a --delete Cerebro/Foruns/ → tencent:v6_data/foruns/` (log `~/log/foruns_v6_sync.log`). Isso já carrega `loop_trindade_laura/` e `ponte_trindade_daemon/` — por isso a página Loops não precisou de sync novo.
- Cópia local `ZCodeProject/painel_fix/painel_cctv_v6.py` estava **velha** (09/08); a viva estava só no servidor (118.645 bytes, 11/08). Baixada para `ZCodeProject/painel_v6_reforma/painel_cctv_v6_SERVIDOR_20260815.py` antes de editar.

## Mudanças no painel (arquivo `/home/ubuntu/cafezinho/v6/painel_cctv_v6.py`)

1. **NAV:** removida entrada `/painel/` ("Home" legada); `/v6/` virou a Home única; adicionadas entradas `🔁 Loops` e `💾 Backup` (backup existia mas não estava no NAV). Em `chrome()`, o botão Home (k=="v6") fica dourado quando não ativo.
2. **`pagina_home()` reescrita:** índice de 13 páginas em 4 grupos (Operação ao vivo / Números / Infraestrutura / Comando) + stats GA4 no topo (inalterados).
3. **Módulo Loops novo** (entre `_backup_wrap` e a seção SERVIDOR):
   - `LOOPS_LAURA_DIR` = `v6_data/foruns/loop_trindade_laura/controle/relatorios_chefe`, `LOOPS_MIGUEL_DIR` = `v6_data/foruns/ponte_trindade_daemon` (ambos com override por env `CCTV_V6_LOOPS_LAURA`/`CCTV_V6_LOOPS_MIGUEL`).
   - `_yaml_solitario()` extrai o bloco ```yaml dos relatórios do chefe (parser linha-a-linha, sem dependência de PyYAML).
   - `_laura_lista()` últimos 13 relatórios; `_miguel_estado()` parseia INDEX_ATIVO.md (tabela), ALERTAS_SLA.md (seções `## ATENCAO/CRITICO — \`ticket\``) e ESTADO_ATUAL.md (tabela Item/Valor).
   - `pagina_loops(query)`: consolidado escolhível por `?rel=NNN`; pill de cadência amarela >45min; pills de prioridade (crítica=vermelho, alta/urgente=amarelo).
   - `api_loops()` e `api_resumo()` → JSON (`/v6/api/loops`, `/v6/api/resumo`) para o relatório Telegram. `api_resumo` reuso de `ga4_serie_diaria(14)` + `wp_posts(20)` (ambos com cache próprio).
4. **Roteamento:** `/loops` com query no `do_GET` (antes do `/foruns`), APIs antes das páginas; `ROUTES["/loops"] = None` (padrão "com query" já existente).
5. **Nginx:** `location = / { return 301 /v6/; }` inserido em painel.conf (backup datado, `nginx -t` + reload).

## Relatório Telegram — `~/bin/cctv_relatorio_30min.py`

- Flags: `--dry-run` (só imprime), `--no-send` (health+log, sem Telegram).
- Health-check: GET /v6/, /v6/loops, /v6/api/loops. Se falhar → restart SSH (`sudo -n systemctl restart cctv-v6`) com cooldown 20min (estado em `~/log/cctv_relatorio/estado.json`).
- Coletas: loops via `/v6/api/loops`; audiência+publicações via `/v6/api/resumo`; online = painel + www.ocafezinho.com + cafezinho.news (retry único após 4s em falha de rede — DNS local soluça); erros = críticos da fila + arquivos datados do dia/ontem em `Cerebro/monitoramento_horario/bugs_encontrados/`; créditos = parse do `--status` da vigília (regex `= (\d+)%\)`) + GLM via import do hook `credito_vigilia.py` (`glm_quota({})` → `j5h.pct`).
- Emoji geral: 🟢 tudo ok · 🟡 algo menor (bugs/críticos zerados mas alertas) · 🟠 crítico ou site fora · painel fora também 🟠.
- Envio: `ponte_cafezinho.py --send`. Log: `~/log/cctv_relatorio/relatorio.log`.
- **Gotcha corrigido:** `_delta_pct` do painel devolve HTML — o script limpa com `re.sub(r"<[^>]+>")` antes de mandar pro Telegram.

## Automação ZCode

- **`automation-e3465bb3-312f-4583-9a72-7f69711fc147`** — a cada 30min, recorrente. Roda o script, verifica frescor do rsync (arquivo mais novo de v6_data/foruns < ~45min) e serviço ativo; se falhar e não conseguir corrigir, registra em `bugs_encontrados/` + avisa no Telegram. Não edita o painel.

## Testes feitos

- Local: parsers com dados reais (13 relatórios Laura; Miguel 5 itens/4 alertas/1 crítico/11 linhas de estado); página 21KB; `?rel=020` OK; servidor local na 8084 com env-vars — `/loops`, `/api/loops` 200; `/` 200 em 32s (GA4 sem credencial local = lento; no servidor é cacheado).
- Servidor: `py_compile` (com `PYTHONPYCACHEPREFIX` — /tmp/__pycache__ é root), restart, todas as 9 rotas 200, raiz 301→/v6/.
- Telegram: 1º envio real 12:36 BRT ✅ rc=0.

## Gotchas para futuras sessões

- O painel cria `V6_CACHE.mkdir(parents=True)` no import — para testar local, exportar `CCTV_BASE=/tmp/...` senão estoura permissão em `/home/ubuntu`.
- PORT é hardcoded `8084` (sem env).
- `py_compile` na Tencent: usar `PYTHONDONTWRITEBYTECODE=1 PYTHONPYCACHEPREFIX=/tmp/pyc_ubuntu` (gotcha conhecido).
- O rsync `7,37` introduz até ~30min de defasagem nos consolidados da Laura exibidos — estrutural, aceito.
- v5 (:8082) e `/painel/` estáticos seguem vivos por URL direta; aposentar = ordem futura do Miguel.

## Estado da missão

**O que aconteceu:** página Loops no ar, Home V6 única com índice, redirect da raiz, relatório Telegram 30/30min funcionando (1º envio 12:36), automação permanente criada, backups datados.
**O que falta:** homologação visual do Miguel; eventual ajuste de recorte/cadência do relatório.
**O que preciso de você (Miguel):** abrir http://43.156.151.165/v6/loops e dizer se o recorte do Telegram está bom assim.


## Adendo 2 (~13:35 BRT) — Telegram, telemetria, críticos

- Vigília (`automation-647b2f13`) e faxina (`automation-a7be3a1e`) SEM Telegram rotineiro (ordem Miguel 13:00: Ponte = relatório CCTV humanizado + conversa). Bug: `thought_level=''` da vigília derrubava CronList — fix UPDATE 'max' em `~/.zcode/v2/tasks-index.sqlite` (bak_pre_thought_fix2_20260815).
- Protocolo de críticos (ordem 13:05): automation-e3465bb3 agora AGE antes de reportar (ler ticket na fila, executar no escopo zcode, responder com ref:, mensagem humana c/ resolução + "Miguel precisa fazer algo?").
- Telemetria: monitor de chaves morto desde 01/07 → cron `*/15` reinstalado; GLM entrou (quota GET, chave espelhada no /root/.env.unificado — Regra Nº 4); parser do painel agnóstico a ordem de label + notação científica `1.78e+09` (bug do frescor); coluna "último check"; servidores sem Beijing, com espelho+ServerDo. Kimi API do servidor suspensa (saldo) e Gemini sem crédito agora VISÍVEIS como "falha no teste".
- Críticos fechados: regex V3 (verificação+testes 7/7+auditoria 15 drafts/0 dano) e 20699 (0 sistêmico; origem = válvula §119/§120 do agendador V6 — conflito de regra p/ Claude). Respostas na fila com ref: exato.
- Gotcha novo: heredoc SSH com aspas simples come literais SQL ('' vira coluna) — usar aspas duplas ou tratar None em Python; timestamps draft_events são ISO UTC com 'T' (BETWEEN com espaço falha silenciosamente).
