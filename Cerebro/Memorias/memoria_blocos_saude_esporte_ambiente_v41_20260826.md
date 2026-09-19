# Memória técnica — Blocos Saúde/Esporte/Meio Ambiente religados no V4.1 (26/08/2026)

**Par do fórum:** `Foruns/forum_blocos_saude_esporte_ambiente_v41_20260826.md` · **Executor:** ZCode/Kimi K3 · **Ordem Miguel:** 26/08 ~18:40

## 1. Cronologia da investigação (evidências)

1. **Home do canônico** (`curl -L https://www.ocafezinho.com/`): blocos Saúde, Meio Ambiente e Esporte PRESENTES no HTML (não foram removidos — estavam parados).
2. **REST WP** (`/wp-json/wp/v2/posts?categories=258|582|1271`): último post de cada categoria em **23/08** (saúde 15:08, ambiente 19:38, esporte 13:16).
3. **Metas dos últimos posts:** `zizi_job_id=v4d_saude_*` (author 5786) → fonte dos blocos era o **V4 antigo** (`v4_vertical_draft_worker`), não o repetidor estatal.
4. **Crontab NYC:** coletas das 3 verticais ativas mas 1x/dia (`15 13/14/15`), marcadas `# V4_DESLIGADO_20260824`; ciclos v41 apenas nacional/economia/ciencia/geopolitica (`25/35/45/55 */2`). Ordem "só V4.1" de 24/08 matou os workers das 3 → órfãs.
5. **`v41_ciclo.py` linha 177:** `choices=['nacional','economia','ciencia','geopolitica']` — as 3 verticais não existiam para o redator V4.1.
6. **Incidente lateral:** repetidor estatal (NYC) sem publicar desde **16/08** — último sucesso ID 266092; desde então 199× `400 cafezinho_imagem_sem_checagem` (o script não grava `_cafezinho_img_check`; gate fail-close de 16/08 o bloqueia). Os 87 posts "author 5470" pós-24/08 são V4.1 com `zizi_job_id=v41_*` e carimbo `_cafezinho_img_check` por **LAURA-AGY** (`aprovacao_laura_agy_consenso_duplo`). Ninguém sentiu a pane porque o V4.1 sustenta a home.
7. **Matéria-prima confirmada** (sqlite `/root/agent_data/v4_verticals/<v>.sqlite3`): candidates `new` nas últimas 48h — saúde 16, esporte 30, ambiente 38. `drafted` 48h = 0 nas 3 (worker morto).
8. **Mapeamentos já prontos no redator runtime** (`v4_vertical_redactor_runtime.py` EDITORIA_ALIASES): `meio_ambiente→v4_meio_ambiente`, `esporte→v4_esporte`, `saude→v4_saude`.
9. **Categorias históricas** (wp_posts×wp_term_taxonomy): v4d_saude→[258,2403], v4d_esporte→[1271,(2403)], v4d_meio_ambiente→[582,2403,(5003)].

## 2. Alterações de código (diff resumido)

**`/root/v4_labs/codigo/v41_ciclo.py`** — backup `v41_ciclo.py.bak_pre_3verticais_20260826` (mesma pasta). 3 pontos:

a) `choices` + `VERTS` ganharam as 3 verticais (bancos existentes, aliases nativos do runtime).
b) Seleção de pauta com branch exclusiva das 3 novas (as 4 ativas INTACTAS):
```python
if a.vertical in ("saude", "esporte", "meio_ambiente"):
    rows = db.execute(
        "SELECT item_key, title, text_content, status FROM candidates WHERE status='new'"
        " AND collected_at >= datetime('now','-48 hours') ORDER BY collected_at DESC LIMIT 9"
    ).fetchall()
else:
    rows = <lógica original 6 drafted + 3 new score ASC>
```
c) Patch de categorias no nascimento (dict `_CATS_NASCIMENTO`): ciencia [30,2403] (já existia), saude [258,2403], esporte [1271,2403], meio_ambiente [582,2403].

**Crontab NYC** — backup `/root/agent_data/crontab_backup_pre_3verticais_20260826.txt` (167→171 linhas; diff = 3 linhas alteradas + 4 adicionadas):
- Coleta meio_ambiente: `15 13` → `15 12,18,0` UTC
- Coleta esporte: `15 14` → `15 13,19,1` UTC
- Coleta saude: `15 15` → `15 14,20,2` UTC
- Novos ciclos (marca `V41_3VERTICAIS_20260826`): meio_ambiente `5 13,19,1`, esporte `22 14,20,2`, saude `42 15,21,3` — horas/minutos escolhidos para não colidir com os ciclos */2 (25/35/45/55) nem com coletas de outras verticais.

## 3. Prova de fogo (26/08 19:07 BRT)

```
cd /root/v4_labs && /root/venv/bin/python3 -m codigo.v41_ciclo --vertical saude
→ tese_dinamica_aprovada; redator gpt-5.5 rc=0
→ rascunho WP id=267820 "Cerveja fica fora de restrição publicitária há 30 anos"
  status=draft, content_chars=5248, cats=[258,2403], zizi_job_id=v41_saude_eeae3806cbcd
  fc_websearch: "confirma" (Lei 9.294/1996, 30 anos em 2026)
```
Validação SQL: `wp_posts` ID 267820 draft, `GROUP_CONCAT(term_id)=258,2403`; metas `zizi_job_id` + `_v4_versao=4.1` presentes.

## 4. Comandos de operação

- Ciclo manual de uma vertical: `ssh nyc 'cd /root/v4_labs && /root/venv/bin/python3 -m codigo.v41_ciclo --vertical saude'`
- Log dos ciclos: `/root/agent_data/v41_ciclo.log` (grep `V41_3VERTICAIS` não aparece no log — o log registra o JSON de saída com `"vertical": "saude"`).
- Rascunhos gerados: `/root/v4_labs/dados/v41_ciclo/<ts>.json` (campo `"vertical"`).
- Rollback código: `cp v41_ciclo.py.bak_pre_3verticais_20260826 v41_ciclo.py`
- Rollback crons: `crontab /root/agent_data/crontab_backup_pre_3verticais_20260826.txt`

## 5. Riscos e guardas

- **Fail-closed preservado:** sem tese ancorada → não escreve; anti-repetição + juiz inter-vertical ativos nas 3 novas (o juiz consulta os 40 últimos títulos publicados — vale para qualquer seção).
- **Dedupe 24h** por `item_key` funciona igual (lê os JSONs de `dados/v41_ciclo/`).
- **Freio de estoque** conta `drafted` 72h do banco da vertical — nas 3 novas é ~0, não trava; se um dia acumular, o freio age igual às outras.
- **Publicação NÃO mudou de dono:** CM/AGY publicam nos slots de ~30min (Emenda 5, espaçamento 20min, segue com eles). Rascunho novo `v41_saude_*` entra na mesma fila que eles já consomem (`v41_geopolitica_*` etc.).
- **Custo marginal:** ~9 rascunhos/dia a mais via roteador de preço dinâmico (ordem gemini-flash > gpt-4o > 5.5 > sonnet...). No teste, o redator usou gpt-5.5.

## 6. Pendências deixadas

1. Confirmar 1ª publicação dos editores a partir do 267820 e a cadência real das primeiras 48h (se <2 posts/dia/bloco, subir coleta p/ */6h e ciclos p/ 4x/dia).
2. **Incidente separado:** repetidor estatal bloqueado pelo gate de imagem desde 16/08 (199 falhas). Opções: ensinar o repetidor a rodar o Tribunal Visual pós-upload (ele roda no NYC, onde está `checar_imagem_vision.py`) ou aposentá-lo de vez (V4.1 já cobre). Decisão fica para quando o Miguel tocar no assunto.
3. Ronda V4.1 (automation-c1437347, 30/30min) deve citar as 3 verticais novas nos relatórios.
