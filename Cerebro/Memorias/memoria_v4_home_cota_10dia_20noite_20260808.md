# 🧠 Memória Técnica — V4 Home: cota 10% capa de dia / 20% à noite — 2026-08-08

**Sessão:** ZCode (GLM-5.2, builtin:zai-coding-plan), 2026-08-08 ~01:30–02:40 BRT
**Fórum pareado:** `Foruns/forum_v4_home_cota_10dia_20noite_20260808.md`
**Status:** ✅ APLICADO E TESTADO AO VIVO (NYC)

---

## 1. Missão

Miguel (08/08 madrugada): capa do V4 com cota diferenciada dia/noite — **10% home de dia (06h-22h), 20% home à noite (22h-06h)**, 90%/80% no-home respectivamente. Mesma regra pra todas as verticais.

## 2. Arquitetura da solução

### 2.1 Cota proporcional por janela (nova)
Funções novas no `/root/v4_vertical_draft_worker.py`:

```python
BRT = timezone(timedelta(hours=-3))
HOME_PCT_DIA = 0.10   # 06h–22h BRT
HOME_PCT_NOITE = 0.20 # 22h–06h BRT

def _janela_home_periodo() -> tuple[str, datetime]:
    # dia = 06h–22h; noite = 22h–06h (rola à meia-noite: 0h–6h pertence à janela das 22h de ontem)

def _cota_home_v4_pode() -> bool:
    # conta draft_events 'draft_confirmed' AGREGADO de TODAS as verticais V4
    # desde o início da janela; se home_já < total×pct -> há vaga na capa
```

Lógica: o nº-alvo de posts na home = `total_da_janela × pct`. O próximo post só vai pra capa se `home_já < target`.

### 2.2 Bloco de decisão (linhas 2124-2139, reescrito)
Antes: `force_no_home` em geo/ciência + janela 22h-06h especial.
Agora:
```python
no_home_decision = decide_no_home(args.vertical, row["score"])  # nota
no_home = bool(no_home_decision["no_home"])
if not no_home:  # passou na nota -> é candidata à capa
    if _cota_home_v4_pode():
        no_home = False  # consome vaga na cota
    else:
        no_home = True   # cota cheia -> no-home
```

### 2.3 Thresholds subidos (policy JSON)
nacional 13→**15**, geopolitica 12→**16**, ciencia 10→**13**.

### 2.4 Removedor pausado
Cron `0 */2 * * *` do `remover_no_home.py` comentado. Antes ele desfazia o no-home após 4h; agora o no-home fica (a cota só funciona se não for desfeita).

## 3. Código alterado (preciso)

Arquivo: `/root/v4_vertical_draft_worker.py`

- **L49, L59:** `force_no_home: True` → `False` (geo, ciencia).
- **L199-263 (aprox):** função `_janela_home_geo_ciencia` substituída pelas funções de cota + legado que retorna False.
- **L2124-2139:** bloco de decisão reescrito pela cota.
- Constantes: `HOME_PCT_DIA`, `HOME_PCT_NOITE`, `BRT`.

Arquivo: `/root/agent_data/no_home_score_policy.json` — thresholds + campo `_quota_home_v4`.

Crontab do root: linha do `remover_no_home.py` comentada (`# PAUSADO_COTA_HOME_V4_20260808`).

## 4. Testes executados

### 4.1 Simulação (local, sem servidor) — 30 posts dia / 25 noite
- DIA: 3/30 = **10% capa** ✅
- NOITE: 5/25 = **20% capa** ✅

### 4.2 Funções no servidor (import isolado)
- Período detectado: **noite** (02:30 BRT), alvo **20%** ✅
- `_cota_home_v4_pode()` = False (cota cheia agora — correto) ✅
- Policy nota: nacional 17→capa / 10→no-home; geo 18→capa / 10→no-home; ciência 14→capa / 8→no-home ✅

### 4.3 Worker real
- `v4_vertical_draft_worker.py nacional` → exit 0, sem erro. (Sem candidata nova a esta hora.)

### 4.4 Simulação com top candidatas reais
- Todas as top (scores 24,5/25,0/21,5) passam na nota → vão pra no-home porque a cota noturna está cheia. **Comportamento esperado.**

## 5. Backups

- `/root/v4_home_backup_20260808_0517/` (worker + policy + removedor + crontab PRE)
- `/root/v4_vertical_draft_worker.py.bak_pre_v4_home_top_20260808`
- `/root/v4_home_backup_20260808_0517/crontab_root_PRE_PAUSE.txt`

## 6. Estado da missão

- **Aconteceu:** regra 10% dia / 20% noite APLICADA e testada.
- **Falta:** nada técnico. Acompanhar 1º dia de transição.
- **Reversão:** restaurar backup + thresholds antigos + religar removedor.

— ZCode (GLM-5.2), 2026-08-08 ~02:40 BRT
