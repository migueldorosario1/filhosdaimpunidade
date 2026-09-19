---
name: feedback-biblioteca-nao-sobrescreve-identidade-agente
description: "Biblioteca compartilhada JAMAIS pode gravar telemetria com sua própria identidade — deve preservar identidade do agente chamador. Caso `motor_coletor:curadoria` mascarou 11 robôs distintos e 141k chamadas LLM em julho."
metadata: 
  node_type: memory
  type: feedback
  author: "Claude Code (Anthropic, claude-opus-4-7)"
  written_at: 2026-07-19 10:28 BRT
  originSessionId: b3501857-e7d4-49f4-83bd-74804874c770
---

**⚠️ ATENÇÃO: memória escrita por Claude Code (Anthropic), NÃO por GLM/Ming (Zhipu AI).**

## Regra

**Toda chamada LLM registrada em telemetria DEVE identificar o agente REAL chamador (não a biblioteca compartilhada).** Formato canônico obrigatório:

- `caller_agent` (identidade real do robô — ex: `robo_coleta_soberania`, NÃO `motor_coletor:curadoria`)
- `module` (biblioteca usada — ex: `motor_coletor.py`)
- `pipeline` (nome do pipeline)
- `pipeline_version` (V3/legado, V4, Repetidor Estatal, site temático)
- `host` (NYC, Tencent, ServerDo.in, etc.)
- `session` / `run_id` / `call_id`
- `model_requested` / `model_effective` / `fallback` (se houve)
- `tokens_input` / `tokens_output` / `cost_usd_estimated`
- `content_id_or_item` (post WordPress, arquivo JSON, etc.)
- `result` (sucesso/descarte/publicação)

**Why:** Caso fundador em 2026-07-01 → 2026-07-19. O `motor_coletor.py` é biblioteca compartilhada usada por 11 robôs de coleta distintos (`robo_coleta_soberania.py`, `_militar`, `_latam`, `_sheinbaum`, `_ia`, `_matriz_energetica`, `_flavio_bolsonaro`, `_fantastico`, `_turismo`, `_sobrenatural`, `coletor_eleicoes.py`). Todos gravavam telemetria com `agente_nome="motor_coletor:curadoria"`.

Consequência: quando Miguel viu R$ 98 gastos em Gemini no 18/07 e pediu auditoria (2026-07-19 08:43 BRT), Codex identificou que 1.946 chamadas foram atribuídas ao "motor_coletor:curadoria" (88,7% do custo Gemini do dia) — mas NÃO conseguiu dizer QUAL robô, QUAL tema, QUAL cron, QUAL feed, QUAL item foi responsável por cada chamada. A identidade real foi destruída pela biblioteca.

Foram necessários DIAS de investigação forense (`raio_x_motor_coletor_legado_nyc_20260719.md`) pra descobrir que 11 coletores V3 haviam sido reativados no failover 01/07 mas seus consumidores no `maestro_distribuicao.py` estavam pausados — filas cresciam, LLM triava, ninguém consumia, gasto acumulado invisível.

**How to apply:**

1. **Ao escrever nova biblioteca compartilhada (ex: `util_llm.py`, `chamador_openai.py`, `wrapper_gemini.py`):**
   - JAMAIS hardcode `agente_nome = "util_llm"` ou similar
   - Aceitar `caller_agent: str` como parâmetro OBRIGATÓRIO na função
   - Se caller não passar → **failure ruidosa** (não default silencioso). Ex: `raise ValueError("caller_agent obrigatório na telemetria")`
   - Ou, se compatibilidade retroativa é vital, aceitar `caller_agent=None` mas gravar `caller_agent="UNIDENTIFIED_<módulo>_<linha>"` (nunca fingir identidade)

2. **Ao auditar telemetria existente:**
   - `SELECT DISTINCT agente_nome FROM telemetria` — se aparecer nome de biblioteca (`_motor_`, `_util_`, `_wrapper_`, `_helper_`, `_base_`) → BUG. Refatorar chamadas.
   - Investigar quais scripts importam essa biblioteca (`grep -rn "from <biblioteca> import" .`)

3. **Ao investigar custo suspeito:**
   - Nunca aceitar "biblioteca X gastou US$ N" como resposta suficiente
   - Sempre exigir: qual robô, qual pipeline, qual conteúdo produzido
   - Se telemetria não consegue responder → é FALHA DE TELEMETRIA, não "custo bem gasto"

4. **Ao promover pipeline pra produção:**
   - Verificar que TODOS os pontos de chamada LLM identificam caller real
   - Adicionar teste que quebra se algum `caller_agent` vier como string vazia ou como nome de biblioteca

## Regra derivada — biblioteca de wrapper CLI

Aplicar também aos wrappers `~/bin/claude`, `~/bin/glm`: se algum wrapper for chamado por daemon/cron, DEVE registrar `MAESTRO_CICLO=N`, `caller=maestro-heartbeat`, etc., no ambiente e telemetria — pra não confundir Claude engenheiro-chefe do Maestro com Claude worker de sprint (risco R-T-01 do `forum_maestro_local_20260719.md`).

## Casos históricos

- **motor_coletor:curadoria** (2026-07-01 → 2026-07-19) — 141k chamadas mascaradas, 11 robôs indistinguíveis, R$ 98 Gemini sem origem
- **agente_repetidor_estatal.py** (2026-07-14) — bug de path silencioso porque importava `AGENT_DATA_DIR` mas não usava — variável fantasma que só apareceu no deploy NYC. Ver [[feedback-variavel-importada-nao-usada-bug-silencioso]]

## Relacionadas

- [[claude-engenheiro-chefe-ecossistema-20260719]]
- [[feedback-cron-como-codigo-producao]]
- [[feedback-variavel-importada-nao-usada-bug-silencioso]]
- [[project-failover-nyc-definitivo-20260701]]
- Carta canônica §17 em `Cerebro/Foruns/carta_passagem_autoridade_codex_claude_20260719.md`
- Investigação forense: `Cerebro/Foruns/raio_x_motor_coletor_legado_nyc_20260719.md`
- Auditoria custo: `Cerebro/Foruns/auditoria_gasto_gemini_98_reais_20260719.md`

## Assinatura

Registro escrito por Claude Code (Anthropic, `claude-opus-4-7`), sessão `CLAUDE-CHEFE-ECOSSISTEMA-20260719-1020`, 2026-07-19 10:28 BRT.
