# Memória — Blocos Regional / Esportes / Digital (log técnico, 27/08/2026)

**Sessão:** ZCode/GLM-5.3 · 27/08/2026 10:22→~11:10 BRT · Fórum irmão: `Foruns/forum_blocos_regional_esportes_digital_20260827.md`

## 1. Movimentação de categoria (post 267872)

```
# WP produção (ServerDo, alias cafezinho-wp = root@190.89.239.65:51439, /var/www/ocafezinho)
wp post term set 267872 category 2403 4986 --by=id --allow-root   # Redação + Regional
# limpeza dos termos espúrios criados sem --by=id (term_id 21190 "2403" e 21191 "4986"):
wp post term remove 267872 category 21190 --by=id; wp post term remove 267872 category 21191 --by=id
wp term delete category 21190; wp term delete category 21191
```
- Prova: `curl` na home → link `barricadas-com-onibus-travam-33-linhas-no-rio` 2× dentro da seção de heading `Regional`; bloco Saúde sem o post.
- ⚠️ LIÇÃO wp-cli: `wp post term set <id> category <termos>` sem `--by=id` cria termos NOVOS usando os números como nome. Sempre `--by=id`.

## 2. Causa raiz do vazamento temático (saúde)

- Post criado pelo job `v41_saude_4a545f987d91` (zizi_job_id), `_v4_versao=4.1`, via REST user 5470, ts 27/08 00:43:59 UTC.
- Pauta candidata no `saude.sqlite3`: título "Criminosos usam ônibus em barricadas contra operação policial no Rio", URL Agência Brasil **geral**, source_name `rss/geral/feed.xml`.
- Filtro real: `heuristic_score()` (coletor.py:631) faz `if normalize_title(kw) in nt` = **substring**, e keywords incluem "sus" → casa "suspeitos"/"suspensas"; o texto extraído também menciona "unidades estaduais de saúde" (ângulo real mas secundário).
- Gates temáticos duros no `v4_vertical_intake.py` existem SÓ para geopolítica (`geo_tech_score < 4` → rejeita) e tecnologia (`technology_title_score == 0` → rejeita). Verticais novas (saude/esporte/meio_ambiente/digital) dependem do substring do coletor + score LLM (não é gate duro).
- **FIX aplicado:** `/root/coletor.py` (NYC) seção `saude.rss_feeds`: `rss/geral/feed.xml` → `rss/saude/feed.xml`. Backup: `/root/coletor.py.bak_pre_feed_saude_20260827`. Feed verificado: HTTP 200, títulos puros de saúde (tabagismo/SUS/Anvisa/Febre do Nilo).
- Risco residual: `meio_ambiente` segue com `rss/geral/feed.xml` (linha ~192 do coletor).

## 3. Esportes — evidências de audiência (GA4)

- Script de análise: `/tmp/ga4_cats.py` no NYC (usa `/root/keys/ga4.json`, PROPERTY_ID 374552425, lib `google.analytics.data_v1beta`); mapeamento slug×categoria gerado do WP (100 posts/cat) em `/tmp/mapa_cats.tsv` (cópias local + NYC).
- Números no fórum irmão. Destaques: esporte 549 views/7d com só 7 posts (~78/post, melhor média das verticais de volume); 30d 485/22 (~22/post, topo junto com regional e digital). Users≈views = leitor único.
- Produção por categoria (7d|30d): esporte 7|22, saude 5|37, tecnologia 25|101, regional 58|82, meio_ambiente 8|38, ciencia 2|70, digital 1|5.
- Top 10 sequestra post novo: 267864 (Vasco, 27/08 01:55, cats 1271+2403+**21169 "Top 10 — agora"**) → `cafezinho_render_top_tendencias($excludes)` (front-page.php:52) → bloco Esporte (query `category__in [1271]` + `post__not_in $excludes`, linha ~704) não pode exibi-lo. By design (ordens 19/08 Top 10 + 23/08 esporte prevalece nos OUTROS blocos).
- Cache Rocket NÃO era o culpado: `wp cache flush` + `rocket_clean_domain()` não mudaram o bloco.

## 4. Digital — destravamento da vertical

- Sintoma: ciclos 26/08 21:15 e 27/08 09:22 terminavam `curadoria_estado: "anti_repeticao:gate_erro:OperationalError"`, `status: "sem_tese_ancorada_nao_escreve"` (v41_ciclo.log).
- Reprodução: `_v4w.anti_repetition_gate()` → `recent_v4_draft_titles(con)` → `SELECT detail FROM draft_events...` → **`no such table: draft_events`**.
- Causa: `digital.sqlite3` (criado 26/08) sem a tabela `draft_events` — todas as verticais irmãs (saude/esporte/meio_ambiente) têm.
- Fix: DDL copiado do saude.sqlite3 e aplicado no digital (tabelas agora: candidates, draft_events, rejections, runs, sqlite_sequence). Gate validado com a pauta do TikTok → `True, sem_suspeito`.
- Ciclo manual: `cd /root/v4_labs && /root/venv/bin/python3 -m codigo.v41_ciclo --vertical digital` → **draft 267929** "Multa contra TikTok mira desenho que expõs menores" (6.557 chars, gpt-5.5, cats 21189+2403, fc_websearch ok — corrigiu valor para R$ 153,7 mi). Aguarda publicadores CM/AGY.
- Diferença Digital×Tecnologia: ver fórum. Digital = internet/cultura digital/plataformas/regulação (Tecnoblog, Canaltech, Olhar Digital, Núcleo, Mobile Time); Tecnologia = IA/chips/ciência/geopolítica da inovação (26 fontes, gate temático próprio, ~101 posts/30d).

## Lições transferíveis

1. **wp-cli term set exige `--by=id`** (senão cria termos com o número como nome).
2. **Classifier por substring é porta de vazamento temático** ("sus" casa "suspeitos") — feeds gerais exigem feed de editoria específica OU gate por palavra inteira (`\b`, como `_termo_hits` do intake).
3. **Banco novo de vertical deve nascer com o esquema COMPLETO** (draft_events incluída) — gate fail-closed transforma tabela faltante em vertical muda, sem erro visível no cron (status "ok": true no log!).
4. **Post no Top 10 não aparece no bloco da própria categoria** ($excludes anti-repetição) — confundir com "bloco parado" é fácil; checar cats do post (21169) antes de diagnosticar.
