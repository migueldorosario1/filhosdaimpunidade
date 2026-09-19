# 🧠 MEMÓRIA TÉCNICA — Portal "parado" / Bloco Nacional vazio: evidências, comandos e provas (30/08/2026)

Par do fórum `forum_portal_bloco_nacional_vazio_20260830.md` (Tema Duplo). Log técnico completo — o "como" para qualquer agente reproduzir/auditar.

## 1. Ambiente e caminhos

- WordPress canônico: `ssh cafezinho-wp` (us65) → `/var/www/ocafezinho`; wp-cli precisa `--path=/var/www/ocafezinho --allow-root`.
- Pipeline V4.1: `ssh nyc` → `/root/v4_labs/codigo/v41_ciclo.py`; log JSON `/root/agent_data/v41_ciclo.log`; crons `crontab -l` (ciclo geral `25 */2`, economia `35 1-23/2`, ciência `45 */2`, geopolitica `55 */2`, esporte `22 8,14,20,2`, saude `42 15,21,3`, meio_ambiente `5 13,19,1`, digital `8 12,18,0`, cultura `52 16,4`).
- Blocos da home (`front-page.php` do tema): **Nacional = cat 22** (`category__in [22]`, `category__not_in` = regional 4986+5 regiões+27 estados + esporte 1271/1426 + vídeos 28/20751/20699); **Geopolítica = 5003**; Economia = 43; Saúde 258; Meio Ambiente 582; Cultura 79 (+Séries 3044); IA/Digital 5008; Tecnologia 30; Internacional 15. `$excludes` acumula posts já exibidos nos blocos de cima (Top 10 etc.) — post pode estar cat 22 e não repetir no bloco porque já aparece antes.
- Autores publicadores: `Redator` (5470) e `Redacao nova` (5786) — contas admin dos editores.

## 2. Diagnóstico (medido, não achismo)

- Home 30/08: 19 posts publicados (00:04→16:57) + 3 agendados (future) + 21 rascunhos gerados no dia → **produção saudável**.
- Categorias dos publicados: só 268257 (Quaest) e 268331 (CE Elmano, mas Regional prevalece) tinham cat 22 → **Bloco Nacional com 1 post** = a percepção do Miguel.
- Causa raiz no código (v41_ciclo.py, `_CATS_NASCIMENTO`): faltavam `nacional`, `economia`, `geopolitica` — essas 3 verticais são as ORIGINAIS da esteira; o remédio "nasce no bloco" de 26/08 foi dado às religadas (saude/esporte/MA) + cultura/digital, e as originais nunca entraram.
- Ciclo hoje: várias rodadas `todas_pautas_ja_rascunhadas_24h` e algumas `sem_tese_ancorada_nao_escreve` (anti-repetição) — comportamento normal, não é o gargalo.
- Gargalo real de volume: **capa** (todo publicado tem `_thumbnail_id`; os 10 da fila não têm) + ritmo do editor (~1/h). AGY-052/CL-032 já estavam no caso (furo 16:30 resolvido; grade noturna future=3).
- Vazamento geo: 268299 marcado Bahia/Nordeste/Regional por causa do NOME "Casas Bahia" (empresa nacional).

## 3. Comandos aplicados (sequência exata)

```bash
# A) patch causa raiz (NYC) — script /tmp/patch_v41_cats.py (scp), backup .bak_pre_cats_nac_eco_geo_20260830
#    insere após '"digital": [5008, 2403],':
#      "nacional": [22, 2403], "economia": [43, 2403], "geopolitica": [5003, 15, 2403]
/root/venv/bin/python3 /tmp/patch_v41_cats.py && /root/venv/bin/python3 -m py_compile /root/v4_labs/codigo/v41_ciclo.py

# B) retro-fix categorias (WP) — SEMPRE --by=id (ver §4)
wp post term add <id> category 22 --by=id --path=/var/www/ocafezinho --allow-root
# 22: 268295 268300 268310 268287 268323 | 43: 268336 268326 268320 268350 268299
# 5003+15: 268305 268324 268255 268266 268337 268334 268348 | 258: 268301 | 5008: 268322 268333 | 582: 268325 268349 | 1271: 268330
wp post term remove 268299 category bahia nordeste regional --path=... # vazamento geo

# C) cache
rm -rf /var/www/ocafezinho/wp-content/cache/wp-rocket/* ; wp cache flush --path=...

# D) wp-cron 1min (BUG-DS-098 assumido; era */5 desde 17/08)
crontab -l > /root/crontab.bak_pre_wpcron_1min_20260830
# linha nova: * * * * * sudo -u www-data /usr/local/bin/wp --path=/var/www/ocafezinho cron event run --due-now ...
```

## 4. Pegadinha `wp post term add` (🔴 registrar no coração de todo agente)

`wp post term add <id> category 22` interpreta "22" como **slug/nome** → cria termo NOVO chamado "22" (criou 8: 21195–21201) e o post continua fora do bloco. Correto: `--by=id`. Cura aplicada: `wp post term remove <id> category 22` (remove o falso por slug) + `add --by=id` + `wp term delete category 21195..21201`. Prova final via `wp eval` com a MESMA WP_Query do tema → bloco com Baptista 13:30 + Quaest + Barqueata + Alckmin + Vídeo PL; curl home pública confirma (7 ocorrências dos títulos).

## 5. Provas

- Query do tema (wp eval, category__in [22] + not_in regional/esporte): antes = Quaest (hoje) + 5 de 28-29/08; depois = **5 posts de 30/08**.
- Home pública pós-purge: "Baptista Junior…" no trecho Nacional; Barqueata/Alckmin/Quaest/Vídeo PL presentes (Top 10 acima, `$excludes` evita repetição).
- `wp cron event list`: 3 × `publish_future_post` (30min25s / 2h / 3h30) = grade 18:00/19:30/21:00 com disparo por minuto.

## 6. Estado final / pendências

- ✅ Bloco Nacional cheio (hoje), causa raiz corrigida (nacional/economia/geopolitica nascem com bloco), vazamento Casas Bahia corrigido, wp-cron 1min.
- 🔶 Fila de capa (dono esteira AGY/gates CL): 268320, 268322, 268325, 268326, 268330, 268333, 268334, 268348, 268349, 268350 (cats já certas).
- 🔶 268291 (Vasco ontem): sem capa + FRESCOR morto → recomendo não publicar.
- 🔶 Separador do tema diz "Nacional (Política + Economia)" mas query só cat 22 — mexer só com ordem do Miguel.
- 👀 Vigiar 31/08: rascunhos das 3 verticais devem nascer com bloco no _patch_v41.

— ZM · ZCode/GLM-5.3 · 30/08/2026 17:29 BRT
