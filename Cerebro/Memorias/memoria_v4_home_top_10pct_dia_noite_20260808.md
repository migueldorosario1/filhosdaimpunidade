# 🧠 Memória Técnica — V4 Home: só nota top na capa (10%/90%, dia=noite) — 2026-08-08

**Sessão:** ZCode (GLM-5.2, builtin:zai-coding-plan), 2026-08-08 ~01:30–02:00 BRT
**Fórum pareado:** `Foruns/forum_v4_home_top_10pct_dia_noite_20260808.md`
**Status:** diagnóstico + patch PRONTO, aplicação PENDENTE confirmação do Miguel.

---

## 1. Contexto (de onde veio)

Miguel (madrugada 08/08, por voz/voz-para-texto) pediu pra "refazer o V4" com a regra de capa: só **nota máxima/top** sai na home (~10%), os 90% vão No Home; **mesma cota de dia e de noite, todo dia**; e queria saber **quantos saem** e o **% de visibilidade na capa**.

## 2. Consulta ao Cérebro (Regra Nº 1)

- `MONITORAMENTO_DE_TRABALHO.md` — nada travando o worker V4; sessão livre pra mexer.
- `Foruns/forum_no_home_por_nota_coleta_20260721.md` — decisão canônica de capa por nota (21/07).
- `v4_labs/contratos/v4_no_home_score_policy_v1.json` — contrato machine-readable.
- `crontab_server.txt` — crons reais (removedor, cotas, janelas dia/noite).
- Agente Explore varreu `agentes_tematicos/v4/`, `v4_labs/`, `maestro_distribuicao.py` — mapeou 2 sentidos de "V4" (sites temáticos × worker vertical Cafezinho). O pedido do Miguel é sobre o **worker vertical** (portal Cafezinho WordPress).

## 3. Números reais (lidos AO VIVO no NYC, 08/08 ~01:55 BRT)

### Produção draft_confirmed, 7d

```
Nacional:        107 (15/dia)  capa~25  ~23%   nohome~82
Geopolítica:      95 (14/dia)  capa~2   ~2%    nohome~93
Ciência/Tec/IA:   27 (4/dia)   capa~2   ~7%    nohome~25
Regional SE:       6 (novo)    capa~0   0%     nohome~6
TOTAL:           ~229 (~33/dia)         ~13% capa
```

### Scores máximos reais (candidates)

```
nacional:            max=24,5  avg=9,13   n=648
geopolitica:         max=25,0  avg=8,12   n=1506
ciencia_tecnologia:  max=21,5  avg=10,82  n=119
regionais:           max=6,0–10,0  avg~4  (sem publicador ativo)
```

### Política deployada no NYC (`/root/agent_data/no_home_score_policy.json`)

```
nacional:           cover_min=13,0   | max real=24,5
geopolitica:        cover_min=12,0   | max real=25,0
ciencia:            cover_min=10,0   | max real=21,5
repetidor_estatal:  cover_min=95 + nota_llm 90
category_no_home: 20699  |  missing_score_policy: no_home (fail-closed)
```

## 4. Mecanismo atual (código, com linhas)

Arquivo: `/root/v4_vertical_draft_worker.py` (NYC)

- **L49, L59:** `force_no_home: True` em geopolitica e ciencia.
- **L199-208 (`_janela_home_geo_ciencia`):** retorna `True` se `weekday>=5` (sáb/dom) OU `hour>=22 or hour<6` (BRT). Dentro da janela, o force_no_home não se aplica.
- **L2064-2073 (bloco de decisão):**
  ```python
  if cfg.get("force_no_home") and not no_home and not _janela_home_geo_ciencia():
      no_home = True
      no_home_decision = {... "reason": "forced_no_home_editorial_rule_20260727"}
  target_categories = list(cfg["category_ids"]) + ([CAT_NO_HOME] if no_home else [])
  ```
- **Removedor** (`/root/remover_no_home.py`, cron `0 */2 * * *`): tira a tag 20699 4h depois → o post sobe pra home mesmo sem nota. **Por isso o No Home é temporário hoje.**

⚠️ **Consequência:** se eu só mudar threshold, os 90% voltam pra home após 4h. Pra 90% ficar fora de verdade, **o removedor tem que parar**.

## 5. Crons V4 ativos (lidos do crontab do root)

```
geopolitica:  0,30 * * * *  (coleta+intake+rascunho)
ciencia:     10,40 * * * *
nacional:    20,50 * * * *
```
Cada vertical roda a cada 30min. Cota worker: `max_posts_per_hour=2, max_posts_per_day=8` (por vertical).

## 6. Patch desenhado (PENDENTE "aplica")

### Mudança A — thresholds (contrato + JSON deployado)
```json
"nacional":     { "cover_min_score": 15.0 }   // era 13,0
"geopolitica":  { "cover_min_score": 16.0 }   // era 12,0
"ciencia":      { "cover_min_score": 13.0 }   // era 10,0
```

### Mudança B — acabar janela dia/noite (worker)
Opção mais limpa: setar `force_no_home: False` em geopolitica e ciencia (L49, L59). Assim decidem SÓ por nota, igual nacional, de dia e de noite. (`_janela_home_geo_ciencia` deixa de ter efeito.)

### Mudança C — No Home definitivo (parar removedor)
Comentar a linha do cron:
```
# 0 */2 * * * cd /root && source chaves.sh && /usr/bin/python3 /root/remover_no_home.py ...
```
(Backup do crontab antes.)

### Resultado esperado (~10% capa)
~33/dia → ~3-4 na capa, ~30 no-home. Mesma regra dia e noite, todo dia.

## 7. Backups feitos

- `/root/v4_vertical_draft_worker.py.bak_pre_v4_home_top_20260808` ✅ (criado)
- Backup do contrato JSON e do crontab serão feitos no momento de aplicar.

## 8. Estado da missão

- **Aconteceu:** diagnóstico completo ao vivo + backup + patch pronto.
- **Falta:** aplicar A+B+C no NYC (mexe em produção/WordPress).
- **Preciso do Miguel:** 1 palavra — "aplica" / "tudo home" / "só ver".

— ZCode (GLM-5.2), 2026-08-08 ~02:00 BRT
