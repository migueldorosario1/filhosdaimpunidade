# 📰 FÓRUM — Portal "parado" / Bloco Nacional vazio: diagnóstico + fix estrutural (30/08/2026)

**Ordem do Miguel (30/08 ~17:10, com link do post 268236):** "não tem nenhuma matéria no Bloco Nacional de hoje, o portal está incrivelmente parado… resolve isso, usa esses agentes para destravar."
**Dono:** ZM (ZCode/GLM-5.3, sessão Dell 17:14→17:29 BRT). Estado: **✅ RESOLVIDO E PROVADO** (bloco Nacional com 5 posts de hoje na home pública).

## O que aconteceu (análise em 1 parágrafo)

O portal **não estava parado em produção**: o ciclo V4.1 escreveu **21 rascunhos hoje** (um a cada ~30–40 min, último 16:36), 19 foram publicados e 3 estão agendados (18:00/19:30/21:00). A percepção de "parado" era real porém **específica do Bloco Nacional da home**, que consulta **somente a categoria 22 (Política)** — e hoje só 1 post tinha nascido com essa categoria. Causa raiz: o mapa `_CATS_NASCIMENTO` do `v41_ciclo.py` cobre ciência/saúde/esporte/meio-ambiente/cultura/digital, **mas nunca ganhou as verticais `nacional`, `economia` e `geopolitica`** — matérias dessas casas nascem só com "Redação (2403)" e nenhum bloco da home as encontra. Agravante de domingo: os editores CM/AGY não reclassificaram na publicação (nos dias úteis isso mascarava o buraco). Gargalo secundário: **capa** — todo post publicado hoje tem capa; os 10 rascunhos na fila estão parados à espera de imagem (a esteira AGY/CL já estava no caso: AGY-052 destravou a Petrobras 16:30).

## Decisões e fixes aplicados (todos com prova)

1. **FIX CAUSA RAIZ — patch `v41_ciclo.py` (NYC):** `_CATS_NASCIMENTO` agora tem `"nacional": [22, 2403]`, `"economia": [43, 2403]`, `"geopolitica": [5003, 15, 2403]` — mesmo remédio da ordem do Miguel de 26/08 ("nascem já na categoria do bloco"), estendido às 3 casas originais que ficaram de fora. Backup `.bak_pre_cats_nac_eco_geo_20260830` + `py_compile` OK. Rascunhos de amanhã nascem no bloco certo.
2. **RETRO-FIX de hoje (WP canônico, `wp post term add --by=id`):** Política+22 → 268295 (Alckmin), 268300 (Barqueata), 268310 (Baptista Jr), 268287 (Vídeo PL), 268323 (agendado 19:30); Economia+43 → 268336, 268326, 268320, 268350, 268299; Geopolítica 5003+15 → 268305, 268324, 268255, 268266, 268337, 268334, 268348; Saúde 258 → 268301; IA 5008 → 268322, 268333; Meio Ambiente 582 → 268325, 268349; Esporte 1271 → 268330. Cache Rocket + object cache purgados.
3. **VAZAMENTO GEO CORRIGIDO (família do caso 27/08):** post 268299 (Casas Bahia/Mercado Livre, reestruturação nacional do varejo) estava em **Bahia/Nordeste/Regional** — o geo-tagger se iludiu com o NOME da empresa. Removidas as cats geo, adicionada Economia 43.
4. **BUG-DS-098 ASSUMIDO PELO ZM (sugestão CL-032):** wp-cron externo apertado de */5 → **1 min** no cafezinho-wp (`cron event run --due-now` por minuto; backup `crontab.bak_pre_wpcron_1min_20260830`). Os 3 `publish_future_post` da noite (18:00/19:30/21:00) agora disparam com atraso máximo de ~1 min.
5. **PROVA (home pública + query do tema):** bloco Nacional passou de 1 → **5 posts de hoje** (Baptista Jr 13:30 em destaque; Quaest, Barqueata, Alckmin e Vídeo PL nos laterais/Top 10). curl na home confirma títulos no ar.

## ⚠️ Pegadinha registrada (para todos os agentes)

`wp post term add <id> category 22` **cria uma categoria NOVA chamada "22"** em vez de ligar ao term_id 22 — precisa **`--by=id`** (mesma lição do caso 27/08 com o `term set`). Criei 8 termos falsos (21195–21201), corrigi todos os vínculos com `--by=id` e **deletei os termos falsos** — zero sujeira deixada.

## O que falta / próximos passos

- **Fila de capa/publicação (dono: esteira AGY + gates CL):** 10 rascunhos de hoje já com categoria certa, aguardando capa + publicação (mais velho: 268320 Copacabana, 08:38). Grade noturna já cobre 18:00/19:30/21:00.
- 268291 (Vasco x Cruzeiro, jogo de ontem) segue sem capa e **FRESCOR morto** — sugestão: não publicar como notícia.
- Vigiar amanhã (31/08): primeiro ciclo após o patch deve mostrar rascunhos nacional/economia/geopolitica nascendo com bloco (prova: `_v4_versao=4.1` + cats de bloco no nascimento).
- Recomendação ZM: editoria considerar separador "Nacional (Política + Economia)" ≠ query real (só cat 22) — se o Miguel quiser economia no bloco Nacional, é 1 linha no front-page (não feito sem ordem).

— ZM · ZCode/GLM-5.3 · 30/08/2026 17:29 BRT · repo canônico + NYC (v41_ciclo.py patch 422) + cafezinho-wp
