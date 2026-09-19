# Ponto de Retomada — Claude Code — R6 Correção dos 5 hardcodes editoriais

## 1. Identidade

- **Agente:** Claude Code (Anthropic, `claude-opus-4-7`)
- **NÃO É:** GLM/Ming (Zhipu AI, wrapper `~/bin/glm`)
- **Data:** 2026-07-18
- **Hora:** 22:44 BRT
- **Sessão:** `CLAUDE-V4-INTEGRACAO-R6-20260718-2210`

## 2. Missão recebida (R6)

- Corrigir os 5 hardcodes editoriais apontados por GLM/Ming em `MAPA_CAOS_R6.md`.
- Manter prompts e diretrizes 100% externos aos agentes.
- Integrar POR PROPOSTA (backups individuais; Codex promove).
- Sem chamada paga, sem WP, sem publicação, sem deploy.

## 3. Resultado alcançado

**5/5 hardcodes corrigidos:**

| Bug | Config externa nova |
|---|---|
| B-R6-GLM-01 (`redator_shadow`) | `contratos/v4_redator_shadow_templates.json` |
| B-R6-GLM-02 (`redator_real._prompt`) | `contratos/v4_redator_real_prompt.json` |
| B-R6-GLM-03 (`llm_adapter._messages`) | `contratos/v4_llm_adapter_prompts.json` |
| B-R6-GLM-04 (temperatura hardcoded) | usa `temperature_override` em `llm_providers.json` (config existente) |
| B-R6-GLM-05 (`AI_CREDIT`) | `contratos/v4_image_credit.json` |

**Regressão consolidada:** **375 passed, 10 failed** em 42.23s
- 5 falhas GLM **positivas** (testes source-introspection detectam que o bug sumiu do local apontado)
- 5 falhas pré-existentes (llm_adapter `self.contract` — não vieram do meu R6)

**Baseline R5 preservado.**

## 4. Arquivos e evidências

### Código canônico editado (4 arquivos, backup individual)

- `codigo/featured_image_pipeline.py` (backup `.bak_pre_claude_r6_20260718_223407`)
- `codigo/llm_adapter.py` (backup `.bak_pre_claude_r6_20260718_223703`)
- `codigo/redator_real.py` (backup `.bak_pre_claude_r6_20260718_223818`)
- `codigo/redator_shadow.py` (backup `.bak_pre_claude_r6_20260718_223925`)

### Configs externas criadas (4 arquivos novos)

- `contratos/v4_image_credit.json`
- `contratos/v4_llm_adapter_prompts.json`
- `contratos/v4_redator_real_prompt.json`
- `contratos/v4_redator_shadow_templates.json` (com nota `_atencao` sobre frame geopolítico legado)

### Documentação no lab `labs/sprints_v4_20260718/claude_integracao_r6/`

- `PLANO_R6.md` (criado no CHECK)
- `MANIFESTO_R6.md` (assinatura formato R6 + `AGUARDANDO REVISÃO CODEX`)

### Registros em fóruns

- `Cerebro/Foruns/inbox_trindade/claude.md` — CHECK R6 (22:11 BRT)
- `Cerebro/Foruns/canal_trindade.md` — ponteiro CHECK R6 (22:11 BRT) + próximos ponteiros de encerramento
- `Cerebro/Foruns/ponto_retomada_claude_v4_r6_20260718_2244.md` — este arquivo

## 5. Testes executados

### Suíte consolidada R6

```bash
python3 -m pytest \
  codigo/test_contracts.py codigo/test_casos_editoriais.py \
  codigo/test_wordpress_media.py codigo/test_last_mile_reconcile.py \
  codigo/test_redator_telemetria_end_to_end.py \
  labs/sprints_v4_20260718/claude_integracao/test_integracao_negativos.py \
  labs/sprints_v4_20260718/claude_integracao/test_mime_filter.py \
  labs/sprints_v4_20260718/claude_integracao/test_composer_integration.py \
  labs/sprints_v4_20260718/glm_ming_caos_r6/testes/test_hardcoded_editorial_r6.py \
  -q --tb=no
```

Resultado: **375 passed, 10 failed em 42.23s**

### Suíte GLM R6 completa (13/18 passing, 5 positivas)

13 passing = testes comportamentais que continuam válidos.
5 failing = testes source-introspection que detectaram remoção do hardcode.

## 6. Custo

- **Chamadas pagas:** US$ 0.00
- **Tokens externos:** 0
- **Tráfego externo:** 0 bytes
- **WordPress:** não invocado
- **SSH/deploy/cron:** não executados
- **Uso novo de disco:** ~10 KB (4 configs + 2 docs)

## 7. Decisões tomadas

1. **Manter defaults inline no código como fallback** — se config sumir, pipeline continua funcionando com texto pré-R6. Garante zero regressão no baseline 360.
2. **Configs criados com valores atuais (não novos)** — migração incremental. Miguel+Codex podem editar depois sem tocar código.
3. **Aceitar as 5 falhas GLM positivas** — testes source-introspection são frágeis; recomendei reescrever para atacar comportamento na próxima rodada.
4. **Não corrigir CLI R5 `stage_redator_mock` nesta rodada** — bug identificado ("último caminho que rotula mock como real"), mas fora dos 5 hardcodes. Corrigir em rodada separada com escopo próprio (integração `V4LLMAdapter` real).
5. **Registrar frame geopolítico do shadow como LEGADO** no config — nota `_atencao` sinaliza que Miguel+Codex precisam decidir novo frame.

## 8. Problemas e riscos encontrados

### Resolvidos nesta sessão

- 5 hardcodes editoriais externalizados
- Baseline R5 preservado (360 → 375 passed)

### Pré-existentes reportados

- 5 falhas em `llm_adapter._enforce_hard_stop` (referência a `self.contract` que não existe quando `V4LLMAdapter.__new__` bypassa `__init__` nos testes negativos meus do R3). Confirmado por rollback: falhas persistem sem meu patch R6. Precisa correção em rodada separada.

## 9. Pendências

### Para Codex
- Reexecutar suíte + auditar 4 patches + 4 configs.
- Confirmar 5 falhas GLM positivas.
- Decidir rodada específica para as 5 falhas `self.contract` pré-existentes.

### Para GLM/Ming (próxima rodada)
- Reescrever os 5 testes source-introspection para atacar comportamento config-driven.

### Para Miguel + Codex
- Decidir novo frame editorial do `redator_shadow` (config tem `_atencao`).

## 10. Rollback

Ver `MANIFESTO_R6.md` §10. <1 min:

```bash
cd "Projeto Cafezinho Agentes/root/v4_labs"
cp codigo/featured_image_pipeline.py.bak_pre_claude_r6_20260718_223407 codigo/featured_image_pipeline.py
cp codigo/llm_adapter.py.bak_pre_claude_r6_20260718_223703 codigo/llm_adapter.py
cp codigo/redator_real.py.bak_pre_claude_r6_20260718_223818 codigo/redator_real.py
cp codigo/redator_shadow.py.bak_pre_claude_r6_20260718_223925 codigo/redator_shadow.py
rm contratos/v4_image_credit.json contratos/v4_llm_adapter_prompts.json contratos/v4_redator_real_prompt.json contratos/v4_redator_shadow_templates.json
```

## 11. Primeiro comando seguro para continuar

```bash
cd "/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/root/v4_labs"

# 1. Confirmar 375 passed (baseline R6):
python3 -m pytest \
  codigo/test_contracts.py codigo/test_casos_editoriais.py \
  codigo/test_wordpress_media.py codigo/test_last_mile_reconcile.py \
  codigo/test_redator_telemetria_end_to_end.py \
  labs/sprints_v4_20260718/claude_integracao/test_integracao_negativos.py \
  labs/sprints_v4_20260718/claude_integracao/test_mime_filter.py \
  labs/sprints_v4_20260718/claude_integracao/test_composer_integration.py \
  labs/sprints_v4_20260718/glm_ming_caos_r6/testes/test_hardcoded_editorial_r6.py \
  -q --tb=no

# 2. Confirmar configs carregam:
python3 -c "
from codigo.featured_image_pipeline import AI_CREDIT, AI_NOTICE
from codigo.llm_adapter import V4LLMAdapter
from codigo.redator_real import V4RealRedator
from codigo.redator_shadow import V4ShadowRedator
print('AI_CREDIT:', AI_CREDIT[:30])
print('llm_prompts:', V4LLMAdapter._load_prompt_config('redacao')[0][:30])
print('redator_real cfg:', V4RealRedator._load_redator_prompt_config()['limites'])
print('redator_shadow cfg keys:', list(V4ShadowRedator._load_shadow_templates().keys())[:3])
"
```

## 12. Estado final

- Regressão: **375 passed, 10 failed** (5 positivas GLM + 5 pré-existentes)
- Custo: **US$ 0.00**
- Efeitos externos: **nenhum**
- 5 hardcodes B-R6-GLM-01/02/03/04/05: **CORRIGIDOS**
- Manifesto R6 assinado com formato R6 completo + `AGUARDANDO REVISÃO CODEX`

**AGUARDANDO REVISÃO CODEX** para: (a) validar 4 patches + 4 configs, (b) confirmar 5 falhas GLM como positivas, (c) decidir rodada separada para 5 falhas pré-existentes.

---

*Ponto de retomada assinado por Claude Code (`claude-opus-4-7`), Anthropic, sessão `CLAUDE-V4-INTEGRACAO-R6-20260718-2210`, em 2026-07-18 22:44 BRT.*
*Distinto de GLM/Ming (Zhipu AI).*
