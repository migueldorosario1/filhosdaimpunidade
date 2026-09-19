---
name: Sprint — validador_modelos testa temperature + flag sem_temperature
description: agente_validador_modelos aprova modelos sem testar temperatura, causando quebra silenciosa em produção (incidente claude-opus-4-7 03/05/2026)
type: project
originSessionId: 44f2c389-881d-4335-a540-25075ea2110b
---
# Sprint: validador_modelos testa temperature + flag sem_temperature

**Why:** O `agente_validador_modelos.py` (smoke test 03:00) aprovou `claude-opus-4-7` como `anthropic_luxo`, mas o modelo rejeita o parâmetro `temperature` com HTTP 400 `"temperature is deprecated"`. Em produção, toda chamada Anthropic falhava silenciosamente e degradava para Mistral. O problema ficou ativo de 03:00 até ~08:18, causando falhas no auditor e no fact-check failsafe. Diagnóstico feito em 2026-05-03.

**How to apply:** Implementar nas próximas sessões antes de qualquer outro sprint de roteador.

## O que implementar

### 1. `agente_validador_modelos.py` — testar com temperature explícito

No smoke test de cada modelo Anthropic, incluir `temperature=0.4` igual ao payload de produção. Se retornar 400 com `"temperature" + "deprecated"`:
- Marcar o modelo com flag `"sem_temperature": true` em `modelos_vivos.json`
- NÃO rejeitar o modelo como morto — ele é válido, só precisa de parâmetro diferente
- Logar: `"⚠️ {modelo} não suporta temperature — marcado sem_temperature"`

### 2. `agente_roteador_llm.py` — `_anthropic_payload` lê a flag

Em `_anthropic_payload`, receber os dados do modelo (ou ler `modelos_vivos.json` via cache) e omitir `temperature` se `sem_temperature=True`:
```python
def _anthropic_payload(modelo, sys_prompt, prompt, max_tokens, temperature, sem_temperature=False):
    payload = {...}
    if not sem_temperature:
        payload["temperature"] = temperature
    return payload
```

E nas chamadas, passar a flag lida do `vivos`:
```python
sem_temp = config.get("sem_temperature", False)
json=_anthropic_payload(modelo, sys_prompt, prompt, max_tokens, temperature, sem_temperature=sem_temp)
```

### 3. Workaround atual (já deployado 03/05)

O retry sem temperature já está em `agente_roteador_llm.py` via `_anthropic_temperature_deprecated()`. Isso funciona como seguro, mas o ideal é a flag proativa acima para evitar o round-trip desnecessário.

## Arquivos envolvidos
- `/root/agente_validador_modelos.py`
- `/root/agente_roteador_llm.py` (função `_anthropic_payload`, linha ~29)
- `/root/config/modelos_vivos.json` (adicionar campo `sem_temperature`)
