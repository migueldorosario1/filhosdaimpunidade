# 🧭 Memória técnica — Auditoria V4 × V4.1 (26/08/2026, ZCode/Kimi K3)

> Log técnico completo da investigação (ordem Miguel ~20:00). Fórum de decisões: `Foruns/forum_auditoria_v4_x_v41_o_que_parar_20260826.md`. **Nada foi alterado — somente leitura.**

## Comandos e provas

### 1. Crontab NYC (root) — mapa V4×V4.1
- `ssh nyc 'crontab -l'` (nyc = 198.199.121.136, root)
- **V4.1 ativo:** `25 */2` v41_ciclo (nacional) · `35 1-23/2` economia · `45 */2` ciencia · `55 */2` geopolitica · 3verticais (amb 13,19,1 / esp 14,20,2 / sad 15,21,3) · digital (coletor 11,17,23 + ciclo 12,18,0)
- **Coletores V4 vivos com comentário inline `# V4_DESLIGADO_20260824`** (NÃO desativa — gotcha da memória `crontab-comentario-inline-nao-desativa-20260824`): geo `0 *` · pol `20 */6` · eco `35 */4` · cul `5 */4` · amb/esp/sad `15 12/13/14,...` · **tec `10,40 * * * *` (2x/hora)** · FDS boost sab/dom. → alimentam os bancos que o v41_ciclo consome. MANTER.
- **v4_vertical_draft_worker:** só linhas comentadas (`SUBSTITUIDO_KIMI_20260727` / `DESLIGADO_V4_20260824`) — nenhum redator V4 clássico no crontab root. ✔

### 2. Log v41_ciclo (prova de produção ciência)
- `/root/agent_data/v41_ciclo.log` (grep ciencia | tail):
  - `20260826_1748` ciencia "Baidu says Chinese buyers want local AI chips..." → tese_dinamica_aprovada → redator gpt-5.5 → **draft 267808** (7131 chars) → FC websearch ok:true (claims confirmadas c/ fontes The Register/SoylentNews)
  - `20260826_1946` ciencia "OpenAI oficializa operações no Brasil..." → **draft 267834** (8226 chars) → FC ok
- Cadeia íntegra: tese → redator → FC → gates. ✔

### 3. Canônico (cafezinho-wp = 190.89.239.65:51439) — posts nas cats do bloco
- `wp --allow-root db query` (wp-cli pede --allow-root como root; heredoc via `ssh 'bash -s'` p/ escapar aspas):
- **20 posts em 7 dias** com term_id IN (30,735,5008); 13 mais recentes conferidos: **todos `_v4_versao=4.1`**.
- Metas dos rascunhos v41: `zizi_job_id` = `v41_<vertical>_<hash>` (V4.1 grava AMBAS as metas — classificar por prefixo `v41_`, nunca pela presença de zizi_job_id).
- Autor dos drafts/publicados v41: **5470** (o pool 5786 era do V4 clássico; o auditor_titulos advisor mira 5786 janela 4h → não vê v41. Observação registrada.)
- `term_taxonomy_id≠term_id` segue valendo (30→31, 735→740) — consultar por t.term_id.

### 4. V4 antigo vivo — as 3 pontas
1. **`/etc/cron.d/v4_regional`** (não está no crontab root!): intake `7 * * * *` + worker `5 10,13,16,19,22,1` (6 drafts/dia) + `v4_regional.bak_20260807_034728`. Flagrado `ps aux`: PID 2742670 v4_regional_intake.py rodando 23:07 UTC. Bancos `/root/agent_data/v4_verticals/regional_{norte,nordeste,centro_oeste,sudeste,sul}.sqlite3` com WAL quente 23:15. Drafts de hoje (pending, post_date=criação): 267542 16:10 · 267770 13:09 · 267743 10:06 · 267724 07:06 · 267589 25/08. Scripts: `/root/v4_regional_intake.py`, `/root/v4_regional_rodar_worker.sh`, `/root/v4_regional_draft_worker.py`.
2. **Repetidor estatal** `7 */2`: `/root/agent_data/repetidor_estatal.log` — hoje 22:08 UTC pipeline completo (media 267819 ok) → `❌ Falha no WordPress: 400 cafezinho_imagem_sem_checagem` (gate §86). **975 ocorrências** de 400/gate no log. Sem publish do NYC desde 16/08.
3. **v4_tendencias_intake** `*/30` (`V4_TENDENCIAS_INTAKE_20260817`): worker tendencias está `DESLIGADO_V4_20260824` (comentado) → intake sem consumidor.

### 5. Feeds da editoria tecnologia (`/root/config_editorial.py`, linhas 68-97)
26 feeds: technologyreview, arstechnica, techcrunch, theverge, asia.nikkei, globaltimes, tecnoblog, canaltech, **revistapesquisa.fapesp**, restofworld, theregister, **feeds.nature.com**, **science.org**, pandaily, technode, chinadaily, scmp, jiqizhixin, 36kr, techcrunch-IA, arstechnica-IA, venturebeat-IA, blog.google AI, openai.com, **neurosciencenews**, **scitechdaily**, maglev. → Expansão 25/08 (ciência/IA/neuro/medicina) CONFIRMADA implementada.

### 6. Lições novas
- **Faxina de cron tem 2 andares:** crontab do usuário E `/etc/cron.d/`. A faxina "só V4.1" de 24/08 cobriu o 1º; o regional morava no 2º e seguiu vivo 2 dias. Próximas faxinas: `ls /etc/cron.d/` obrigatório.
- v4d_regional pendente tem valor editorial (Quaest estaduais) — a parada do worker deve vir acompanhada de destino para os pendentes (publicar manual) ou migração futura do regional para o v41_ciclo (vertical `regional` nova — receita de 7 pontos da memória `bloco-digital-home-vertical-v41-20260826`).

## Estado da missão
Investigação entregue → **falta:** "vai" do Miguel na tabela de 3 paradas + destino dos 5 pendentes regionais → **preciso de você (Miguel):** aprovar ou ajustar.
