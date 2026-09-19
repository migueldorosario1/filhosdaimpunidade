# ⚙️ Failover LLM automático — fórum do sistema

> Sistema: `~/.zcode/hooks/llm_fallback.py` · Log de eventos: `fallback_llm_eventos.md` · Estado: `~/.zcode/hooks/fallback_estado.json`
> Cadeia: Kimi K3 → Qwen Token Plan → GLM-5.3 → DeepSeek (pay-as-you-go, último recurso).

## Como funciona

- Cron `*/15` roda `--check` (com rede); hook UserPromptSubmit roda `--rapido` (só cache).
- Troca automática em ≥90% da cota (janela 5h ou semanal) ou 403; reversão automática abaixo de 75% (hysteresis).
- Camadas: automações (tasks-index.sqlite) → sessão viva → modelo default CLI.
- Eventos auditáveis em `fallback_llm_eventos.md` (1 linha por troca).

## 🔧 INCIDENTE 16/08 20:07–22:52 — automações mortas após failover (RESOLVIDO)

**Sintoma:** relatório CCTV 30/30min parou no Telegram (último 19:48); Caçadora de imagens e Vigília também paradas (desde ~17:07/~17:22 — ninguém viu porque não mandam Telegram por ordem do Miguel 15/08).

**Causa-raiz (2 camadas):**
1. O failover troca o `model` da automação mas NÃO trocava o `thought_level` (ficou `max`).
2. `qwen3.8-max` NÃO tem declaração de capacidade de raciocínio em lugar nenhum do app (nem catálogo embutido `/opt/ZCode/resources/model-providers/*.json`, nem heurística por nome, nem config) — então QUALQUER thought_level falha no despacho com `Unsupported reasoning effort`. Kimi/GLM funcionavam com `max` porque o catálogo resolve por ID de modelo (kimi-k3→moonshot-kimi; GLM-5.x→zai-coding-plan, ambos com níveis low/high/max).

**Fix aplicado (ZCode, 22:52–23:08, ordem "vai" do Miguel):**
1. Backup: `tasks-index.sqlite.bak_pre_thought_qwen_20260816_2252` + `config.json.bak_pre_thought_qwen_20260816_2252`.
2. `~/.zcode/v2/config.json` → chave `overrides["2d084035-…/qwen3.8-max"].reasoning = {enabled, levels:["enabled","disabled"], defaultLevel:"enabled"}` (mecanismo oficial `applyModelCatalogOverrides` do app; nível `enabled` = provado empiricamente: sessão viva já rodava com variant `enabled` no qwen).
3. 5 automações Qwen: `thought_level='enabled'` + estado de falha de despacho limpo.
4. `llm_fallback.py`: tabela `THOUGHT_POR_PROVEDOR = {kimi:max, qwen:enabled, glm:max, deepseek:enabled}` — toda troca/reversão de automação agora ajusta `thought_level` junto e limpa `dispatch_status`.
5. Prova: disparos 23:07 de CCTV + Caçadora `dispatched/running` (antes: `failed_to_dispatch`). Ciclo 30/30min restaurado sem restart do app.

**Lições:** (a) falha de despacho fica registrada em `automation_runs.error` + `automations.last_error` — olhar PRIMEIRO lá quando automação parar; (b) modelo custom fora do catálogo embutido precisa de `overrides` de reasoning no config; (c) Caçadora/Vigília paradas são INVISÍVEIS (sem Telegram) — o relatório CCTV deve incluir contagem de disparos falhos das automações (melhoria pendente).

**Pendências:** nenhuma. Kimi reverte sozinho quando a janela 5h renovar (hysteresis <75%).

---

## RECORRÊNCIA 17/08 ~11:50 — deepseek + thought_level 'enabled' quebrava o despacho

O mesmo bug do thought_level voltou em outro provedor: o failover de 16/08 23:23
mandou as automações para o DeepSeek com `thought_level='enabled'` (mapa errado no
`THOUGHT_POR_PROVEDOR` — a prova empírica de 'enabled' era do QWEN). O catálogo
oficial do app define deepseek-v4-pro com níveis **off/high/max** (default max),
então todo despacho morria com "Unsupported reasoning effort: enabled" —
CCTV sem relatório desde 16/08 23:07. **Fix (ZCode/DeepSeek, 17/08 11:59):**
(1) 5 automações → `thought_level='max'` + estado de erro limpo
(backup `.bak_pre_deepseek_max_20260817`); (2) `llm_fallback.py`:
`THOUGHT_POR_PROVEDOR["deepseek"]` = `"max"` (era "enabled"). **Prova:** despacho
CCTV 12:00:00 `dispatched/running` sem erro; next_run 13:00 (cron do Miguel
`0 2,6,8-21,22` — 1/1h dia, 4/4h noite). Lição reforçada: nível por provedor
tem que vir do CATÁLOGO de cada modelo, não de outro provedor.
