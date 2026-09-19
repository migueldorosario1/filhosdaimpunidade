# Memória — V4 gate de tema Geopolítica × Tecnologia (18/08)

**Sessão:** ZCode/DeepSeek (conversa "Ponte Claude - Z Code"). **Horário:** 18/08/2026 ~13:15→14:00 BRT.
**Ordem Miguel:** corrigir estruturalmente a classificação errada (266468 tech → Geopolítica).

## Causa raiz (provas)

- Post 266468: `zizi_job_id = v4d_geopolitica_3185e3f647244ec9` (vertical geopolitica); candidata no `geopolitica.sqlite3`: source_name `https://www.scmp.com/rss/91/feed`, título SCMP "The next silicon? AI data centre material faces price spike amid China supply crunch" (seção /tech/tech-trends).
- `config_editorial.py::RSS_FEEDS["geopolitica"]` tinha o rss/91; verificação empírica: rss/91 = **"News - South China Morning Post"** (feed GERAL; rss/4 = China, rss/3 = Asia, rss/12 = Global Economy, rss/10 = Companies; não há feed Tech dedicado ativo).
- `v4_vertical_intake.py::import_section`: geopolitica SEM gate de tema (só politica tem veto lula e tecnologia tem nexus ≥4).

## Patches (NYC)

1. `config_editorial.py` (backup `.bak_pre_scmp_feeds_20260818`): geopolitica rss/91→rss/4 c/ comentário; tecnologia rss/4 removido. Patch via scp+exec (script com asserts de âncoras).
2. `v4_vertical_intake.py` (backups `.bak_pre_tema_gates_20260818`, `.bak_pre_gate_veto_v2_20260818`, `.bak_pre_fold_acentos_20260818`):
   - `technology_title_score(title)` + gate `missing_tech_term_in_title` na seção tecnologia (item PENDENTE do bug 0315 de 17/08 — agora aplicado).
   - `GEOPOLITICA_NON_GEO_TITLE_VETO` (esporte/entretenimento/negócios/saúde/cultura, EN/PT/ES) + gate `off_theme_title_veto` na geopolitica: rejeita se `veto_titulo ≥1 E geo_titulo == 0` (fail-open).
   - `GEOPOLITICAL_EVENT_TERMS` estendido (plurais + ES: strikes/explosiones/misiles/tarifaco/embajada...; SEM nomes de país/ator — senão o veto não pega "Kanye performs in Russia").
   - `_termo_hits()` com dobra de acentos via `_fold` (pré-existente no arquivo) + `\b` (regex palavra inteira — evita "war" em "warsaw").
3. DB `geopolitica.sqlite3` (backup `.bak_pre_gate_tema_20260818`): 77 rejeitadas pelo gate v1 (sobrerejeição) RESTAURADAS para `new` + rejections deletadas; veto v2 vetou só 6 (`off_theme_title_veto`). Estado final: 234 new legítimas.
4. WP canônico: 266468 → `wp post term remove category 5003` + `add category 30` + primary 30.

## Lições

1. **Gate v1 (exigir nexo geo) sobrerejeita**: geopolítica real chega em ES/FR/plural e sem termo do dicionário (Ucrânia/Gaza/Venezuela rejeitadas). Para notícias, gate deve ser FAIL-OPEN com veto de fora-tema de alta precisão, não exigência de presença.
2. Nomes de país/ator NÃO servem de tie-breaker em veto (anulam o veto).
3. Acentos quebram matching de keywords PT — sempre dobrar com NFKD+strip de combining (`_fold` já existia no intake).
4. Feed "News" geral de veículo grande (SCMP rss/91) em seção vertical = entrada de fora-tema; feeds por SEÇÃO do veículo (China/Asia/Economia) são o padrão certo.
5. O gate tech `title_tech>0` (pendente desde o bug 0315) agora exige termo no TÍTULO — com _fold, "inteligência artificial" (PT acentuado) casa com "inteligencia artificial".

## Verificação

py_compile OK; unit 8 casos (esperado×real OK); intake REAL rodado (seen 37/accepted 27/rejected 10 só frescor; 0 erros); WP conferido (cat única 30).
