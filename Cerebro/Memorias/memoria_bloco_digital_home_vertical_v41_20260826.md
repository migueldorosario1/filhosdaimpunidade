# Memória técnica — Bloco DIGITAL + vertical V4.1 digital (26/08/2026)

**Par do fórum:** `Foruns/forum_bloco_digital_home_vertical_v41_20260826.md` · **Executor:** ZCode/Kimi K3 · **Ordem Miguel:** 26/08 ~19:35

## 1. Mapa de criação de uma vertical V4.1 nova (receita completa, reutilizável)

Para criar a vertical `digital` do zero foram necessários **7 pontos de código** (ordem segura):

| # | Arquivo (NYC salvo indicado) | O que muda |
|---|---|---|
| 1 | WP (`cafezinho-wp`) | `wp term create category Digital --slug=digital` → **term_id 21189** |
| 2 | `/root/coletor.py` | `_NOVAS_FONTES["digital"]` (rss_feeds + google_queries + classifier_keywords) + label/short em `SECTIONS` + entrada na lista do comprehension + `abrev` `"dig"` |
| 3 | `/root/v4_vertical_intake.py` | `DATABASES["digital"]="digital.sqlite3"` + `POLICY["digital"]=48` (o `choices` do argparse deriva de DATABASES.keys() — automático) |
| 4 | `/root/v4_labs/codigo/v41_ciclo.py` | `choices` + `VERTS` + inclusão na branch de pauta fresca `new` 48h + `_CATS_NASCIMENTO["digital"]=[21189,2403]` |
| 5 | `/root/v4_labs/codigo/v4_vertical_redactor_runtime.py` | `EDITORIA_ALIASES["digital"]="v4_digital"` |
| 6 | `/root/v4_labs/contratos/mapa_v4_contexto_llm.json` | `aliases["digital"]="v4_digital"` + `editorias.v4_digital` (label, diretriz, nobre:true, funcoes luxo irmãs) |
| 7 | `/root/v4_labs/contratos/v4_digital_v1.md` | diretriz editorial (escopo / fora de escopo / tom) |

+ crons (coleta 3x/dia + ciclo 3x/dia) + bloco no `front-page.php` do tema `ocafezinho-portal` + semente de categoria.

**Backups datados:** `coletor.py.bak_pre_digital_20260826`, `v4_vertical_intake.py.bak_pre_digital_20260826`, `mapa_v4_contexto_llm.json.bak_pre_digital_20260826`, `v4_vertical_redactor_runtime.py.bak_pre_digital_20260826` (todos no NYC) + `front-page.php.bak_pre_bloco_digital_20260826` (cafezinho-wp) + crontab em `/root/agent_data/crontab_backup_pre_3verticais_20260826.txt` (anterior às 2 mudanças do dia).

## 2. Escolhas e porquês

- **Feeds (validados 200 + nº itens em 26/08):** Tecnoblog (50), Canaltech (50), Olhar Digital (10), Núcleo (6), Mobile Time (20). Escolhidos por cobrirem cultura digital/plataformas BR sem sobrepor o hard-tech da vertical tecnologia (que rejeita a maior parte desse material no gate próprio — a digital pesca o que a tec reprova, sem canibalizar).
- **Separação editorial Digital×Tecnologia:** digital = internet vivida (plataformas, redes, creators, regulação, golpes, inclusão); tecnologia = hard tech (chips, IA, infra). Registrado na diretriz `v4_digital_v1.md` §Fora de escopo.
- **Semente via SQL direto** (`INSERT IGNORE INTO wp_term_relationships` + update do `count`): 5 posts on-theme dos últimos 14 dias (seleção manual sobre lista de 12 candidatos por LIKE; descartados falsos positivos "golpe político", apostas — Emenda 11 — e IA-fronteira). Neste caso `term_taxonomy_id`==`term_id`==21189 (confirmado por query — o gotcha `tt_id≠term_id` continua valendo para categorias antigas).
- **Posição do bloco:** após Esporte (último temático), antes dos banners/Recentes — não desloca bloco aprovado em reformas anteriores. Mudar de posição = mover o trecho entre `SEPARADOR — Digital` e `</section>`.
- **Cache WP Rocket:** home ficou congelada até limpar; `wp rocket` NÃO é comando wp-cli registrado nesta instalação — removido `/var/www/ocafezinho/wp-content/cache/wp-rocket/www.ocafezinho.com/index.html*` + curl 200 regenerou. Procedimento vale para qualquer troca de template da home.

## 3. Provas de fogo

1. Coleta dig (22:44 UTC): 17 extraídas/55s → intake 17/17 aceitas em `digital.sqlite3`.
2. Ciclo v41 digital (19:52 BRT): pauta "Pontaltech RCS" → `sem_tese_ancorada_nao_escreve` (fail-closed OK; pauta B2B fraca corretamente reprovada).
3. Home pós-cache: separador Digital + 5 posts corretos (grep `>Digital<` = SIM).
4. `php -l` no front-page.php: sem erros. `py_compile` nos 4 python: OK. JSON do mapa: validado com asserts.

## 4. Operação

- Ciclo manual: `ssh nyc 'cd /root/v4_labs && /root/venv/bin/python3 -m codigo.v41_ciclo --vertical digital'`
- Coleta manual: `ssh nyc 'cd /root && . chaves.sh && /root/venv/bin/python3 coletor.py dig && /root/venv/bin/python3 v4_vertical_intake.py digital'`
- Log coleta/intake: `/root/agent_data/v4_verticals/digital_cron.log`; ciclos: `/root/agent_data/v41_ciclo.log` + JSONs `/root/v4_labs/dados/v41_ciclo/`.
- Crons: coleta `15 11,17,23` UTC; ciclo `8 12,18,0` UTC (marca `V41_DIGITAL_20260826`).

## 5. Pendências

1. 1ª matéria inédita da vertical (tese aprovada → rascunho → CM/AGY publicam); vigilar primeiras 48h; se magro, coleta → */6h.
2. Repetidor estatal segue bloqueado no gate de imagem desde 16/08 (incidente separado registrado no fórum das 3 verticais).
3. Ronda V4.1 (30/30min) deve passar a citar a vertical digital nos relatórios.
