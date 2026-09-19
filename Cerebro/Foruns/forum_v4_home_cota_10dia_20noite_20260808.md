# 📰 Fórum — V4 Home: 10% capa de dia / 20% à noite (cota agregada) — APLICADO

**Data:** 2026-08-08 ~02:35 BRT
**Executor:** ZCode (GLM-5.2, builtin:zai-coding-plan)
**Autoridade:** ordem direta do Miguel (08/08 madrugada): "à noite você deixa assim, 20% home e 80% no home, e dia 10% home 90% no home. vamos deixar assim."
**Memória pareada:** `Memorias/memoria_v4_home_cota_10dia_20noite_20260808.md`
**Status:** ✅ **APLICADO E TESTADO AO VIVO** (NYC)

---

## 1. A decisão do Miguel (transcrição)

> "à noite voce deixa assim, 20% home e 80% no home, e dia 10% home 90% no home. vamos deixar assim."

## 2. O que mudou (3 alterações, todas aplicadas)

### A. Cota home por janela (nova lógica no worker)
- **Funções novas** (`_janela_home_periodo`, `_home_pct_janela`, `_cota_home_v4_pode`):
  - **DIA (06h–22h BRT):** 10% home / 90% no-home (1 a cada 10).
  - **NOITE (22h–06h BRT):** 20% home / 80% no-home (1 a cada 5).
  - Contagem **agregada** de todas as verticais V4 desde o início da janela.
  - O post só vai pra capa se passou na nota **E** a cota da janela tem vaga.
- Bloco de decisão (linhas 2124-2139) reescrito: acabou o `force_no_home` de geo/ciência e a janela 22h-06h separada.

### B. Thresholds de nota subidos (só a nata é candidata à capa)
| Vertical | cover_min antes | cover_min agora |
|---|---:|---:|
| nacional | 13,0 | **15,0** |
| geopolitica | 12,0 | **16,0** |
| ciencia | 10,0 | **13,0** |

(no `/root/agent_data/no_home_score_policy.json`)

### C. Removedor pausado (no-home virou definitivo)
- Cron `0 */2 * * *` do `remover_no_home.py` **comentado** (`# PAUSADO_COTA_HOME_V4_20260808`).
- Antes: tira a tag 20699 após 4h → post voltava pra home. Agora: o no-home fica (cota respeitada).

## 3. Como a regra funciona na prática

1. Candidata chega → worker calcula nota (score de coleta).
2. **Passou no threshold?** (nacional≥15 / geo≥16 / ciência≥13) → é candidata à capa. Não passou → no-home (90%).
3. **Cota da janela tem vaga?** → conta todos os drafts V4 desde 06h (dia) ou 22h (noite); se `home_já < total×pct`, vai pra capa; senão → no-home.
4. Resultado ao longo do dia: converge pra exatamente **10% capa de dia / 20% à noite**.
5. Como o removedor está parado, o no-home **não é desfeito** — a proporção se mantém.

## 4. Testes ao vivo (08/08 ~02:30 BRT, período noite)

### Simulação (30 posts dia / 25 posts noite)
```
DIA:   3/30 = 10% capa ✅
NOITE: 5/25 = 20% capa ✅
```
### Funções no servidor
```
Período atual: noite (início 22:00 BRT) -> alvo capa = 20%
_cota_home_v4_pode() = False  (cota noturna cheia agora)
```
### Policy de nota (validada)
```
nacional 17 -> capa | nacional 10 -> no-home
geo 18 -> capa      | geo 10 -> no-home
ciencia 14 -> capa  | ciencia 8 -> no-home
```
### Worker real
- `v4_vertical_draft_worker.py nacional` rodou sem erro (exit 0). Sem candidata nova a esta hora (normal).

## 5. Backups (Regra "nenhum arquivo se perde")

- `/root/v4_home_backup_20260808_0517/` — worker + policy + removedor + crontab (PRE)
- `/root/v4_vertical_draft_worker.py.bak_pre_v4_home_top_20260808` — worker (PRE anterior)
- `/root/v4_home_backup_20260808_0517/crontab_root_PRE_PAUSE.txt` — crontab antes de pausar o removedor

## 6. Estado da missão

- **Aconteceu:** regra 10% dia / 20% noite aplicada e testada ao vivo. Worker + thresholds + removedor consistentes.
- **Falta:** nada técnico. Acompanhamento nos próximos dias pra confirmar que os % reais convergem (1º dia de transição pode ter ruído).
- **Reversão (se o Miguel quiser voltar):** restaurar worker do backup `.bak_pre_v4_home_top_20260808` + thresholds antigos (13/12/10) + religar cron do removedor.

## 7. Governança

- Nodo: `CEREBRO_NODE_ARQUITETURA.md` (ou diretrizes de coletores) — ponteiro a adicionar.
- Log: `CEREBRO_NODE_ATUALIZACOES.md` (entrada criada).
- Monitor: linha → ✅ APLICADO.

— ZCode (GLM-5.2), 2026-08-08 ~02:35 BRT
