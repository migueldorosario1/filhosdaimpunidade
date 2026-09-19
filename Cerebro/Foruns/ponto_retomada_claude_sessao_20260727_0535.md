# Ponto de Retomada — Claude Code / sessão 27/07/2026 05:35 BRT

**Timestamp:** 2026-07-27 05:35 BRT
**Sessão:** continuação micro (~12 min) da retomada 05:23 BRT
**Autor:** Claude Code (Anthropic, `claude-opus-4-7`)
**Motivo do ponto:** Miguel vai fechar essa sessão e abrir NOVA via `~/bin/claude` limpo pra desativar env vars GLM contaminadas (fix delegação Sonnet/Haiku).

---

## 1. O que fiz nessa micro-sessão

1. ✅ **Assinei §4 do CONTRATO_PONTE_CLAUDE_KIMI.md** em `Cerebro/ponte_kimi/`. Ajuste proposto: canal ganha tag `[FACT-CHECK-DESCARTE]` no momento do 1º gate ativo bug #37. Kimi pode aceitar/rebater editando direto.
2. ✅ **Registrei assinatura em HISTORICO.md da ponte** (linha nova 2026-07-27 05:31).
3. ✅ **Postei ponteiro no canal_trindade** com tag `[PONTE-KIMI-SENTINELA-ASSINADA]`.
4. ❌ **Falhei em testar delegação Sonnet** — env vars GLM contaminantes fizeram `model: sonnet` resolver pra `glm-5-turbo` (inexistente na Anthropic API). Erro claro: "There's an issue with the selected model (glm-5-turbo)".

---

## 2. Diagnóstico definitivo do bug PATH

**Fix bashrc do 26/07 16:20 BRT NÃO propagou nessa sessão porque:**

- Nova sessão foi iniciada com `~/.local/bin` no PATH antes de `~/bin` (verificado: `PATH=/home/migueldorosario/.kimi-code/bin:/home/migueldorosario/.local/bin:...:/home/migueldorosario/bin:...`)
- Miguel provavelmente rodou `claude` de terminal já aberto ANTES do bashrc ser recarregado
- Consequência: `which claude` → `~/.local/bin/claude` (wrapper GLM) em vez de `~/bin/claude` (wrapper limpo)
- Env vars ativas nessa sessão: `ANTHROPIC_DEFAULT_SONNET_MODEL=glm-5-turbo`, `ANTHROPIC_DEFAULT_HAIKU_MODEL=glm-4.5-air`, `ANTHROPIC_DEFAULT_OPUS_MODEL=glm-5.2`
- `unset` via Bash tool não resolve — as env vars pertencem ao processo pai (o Claude Code), não afeta

---

## 3. Passo-a-passo pra Miguel

Na próxima sessão:

```bash
# 1. Fechar sessão atual: Ctrl+D ou /exit

# 2. Recarregar shell (crítico — pega o novo PATH do bashrc)
exec bash -l

# 3. Confirmar PATH correto
which claude
# Esperado: /home/migueldorosario/bin/claude
# Se ainda /home/migueldorosario/.local/bin/claude → PATH ainda sujo, chamar Claude pra investigar

# 4. Confirmar env vars limpas
env | grep -E "ANTHROPIC_DEFAULT_(SONNET|HAIKU|OPUS)_MODEL"
# Esperado: vazio (unsetadas pelo wrapper)

# 5. Abrir Claude Code
claude
```

Se `which claude` NÃO retornar `~/bin/claude`, é bug adicional no bashrc (talvez outro export sobrescrevendo depois do fix). Nesse caso Claude nova sessão precisa investigar `~/.bashrc` linha a linha.

---

## 4. O que a nova sessão Claude deve fazer

1. Rodar `date`, `which claude`, `env | grep ANTHROPIC_DEFAULT` — CONFIRMAR limpeza
2. Se OK: fazer teste mínimo de delegação Sonnet (echo 3 linhas: model_id + date + tail ciclo)
3. Se OK: ligar `/loop 30m` com ciclo Sentinela delegado ao Sonnet, reportando economia BRL a cada retorno (regra `feedback_reportar_economia_em_real_ao_delegar_sub_agent.md`)
4. Continuar o que ficou pendente do ponto anterior 05:23:
   - Aguardar manifesto Kimi §17 (coleta enriquecida)
   - Aguardar manifesto Kimi §12 (V4 Geopolítica cartoon órfão — ETA ~06:30 BRT)
   - Rodar checkup temáticos se >2.5h desde último ciclo

---

## 5. Estado operacional (05:35 BRT)

- Loop Sentinela cron: `*/30 6-21` + `0 22-05` ativo (último `20260727_0508` 🟢).
- Loop Temáticos cron: `0 3,13` + `30 2,12` YouTube + `0 */8` ceará + `10 */8` riocarta ativo.
- Health 10/10 estável.
- Nenhuma ação Sentinela nos últimos 3 ciclos (esteira limpa).
- Bug V4 Geopolítica cartoon órfão: Kimi ETA manifesto 06:30 BRT.
- Coleta enriquecida (§17): manifesto Kimi pendente.

---

## Assinatura

Ponto de retomada gravado por Claude Code (Anthropic, `claude-opus-4-7`), 2026-07-27 05:35 BRT.
