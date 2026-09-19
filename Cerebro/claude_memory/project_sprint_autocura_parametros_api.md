---
name: Sprint — Autocura de parâmetros API (temperatura, contexto, compatibilidade de modelo)
description: Nenhum sistema detecta automaticamente quando um modelo começa a falhar por incompatibilidade de parâmetros. Montar um loop de autocura específico pra isso.
type: project
originSessionId: 44f2c389-881d-4335-a540-25075ea2110b
---
# Sprint: Autocura de parâmetros e compatibilidade de modelos

**Why:** O incidente de 03/05 (claude-opus-4-7, temperature deprecated) revelou um gap arquitetural: o roteador absorve erros 400 de parâmetro silenciosamente, mas nenhuma camada retroalimenta isso pro validador ou pro `modelos_vivos.json`. O problema fica ativo até alguém notar manualmente.

**How to apply:** Sprint médio. Implementar depois do validador_temperature (pré-requisito lógico).

## Gap identificado

```
agente_validador (03:00) → aprova modelo → modelos_vivos.json
     ↑ não recebe feedback                    ↓
roteador tenta modelo → 400 temperature → loga ⚠️ e pula → Mistral
     ↑ retroalimentação INEXISTENTE
```

Nenhum sistema fecha o loop.

## O que montar

### Componente 1: `_auto_blocklistar_modelo` com campo `sem_temperature`

Expandir a função pendente (Codex Q5, ainda não deployada) para distinguir:
- **Bloqueio permanente**: modelo morto (404, "not a chat model", "only v1/responses")
- **Restrição de parâmetro**: modelo vivo mas com limitações (temperature, max_tokens format)

Para restrições, ao invés de blocklistar, gravar em `modelos_vivos.json` sob a chave do modelo:
```json
"anthropic_luxo": {
  "provider": "anthropic",
  "model": "claude-opus-4-7",
  "sem_temperature": true,
  "detectado_em": "2026-05-03T09:30:00"
}
```

### Componente 2: Contador de falhas por modelo no roteador

No `_gerar_texto_interno`, quando um modelo falha com erro 400/parameter, incrementar um contador em memória compartilhada (`/root/config/falhas_modelos_runtime.json`). Se modelo X atingir N falhas do mesmo tipo em 1h:
- Escrever a flag correspondente em `modelos_vivos.json` atomicamente (via `os.replace`)
- Logar evento

### Componente 3: Autocura V4 monitora `falhas_modelos_runtime.json`

`agente_autocura_v4.py` já roda a cada `:17`. Adicionar uma invariante nova:
- Se `falhas_modelos_runtime.json` tiver modelo com ≥3 falhas do mesmo tipo nas últimas 2h → acionar correção automática (setar flag em `modelos_vivos.json`)
- Reportar via Augusto (Telegram) com sumário: modelo, tipo de erro, flag aplicada

### Padrões de erro a tratar (além dos já cobertos)

| Erro | Ação |
|------|------|
| `temperature is deprecated` | Setar `sem_temperature: true` |
| `max_tokens` not supported, use `max_completion_tokens` | Setar `usa_max_completion_tokens: true` |
| `not a chat model` | Blocklistar permanentemente |
| `only supported in v1/responses` | Blocklistar permanentemente |
| HTTP 404 / model not found | Blocklistar permanentemente |
| HTTP 429 / rate limit | NÃO blocklistar — transitório |
| HTTP 500-504 / server error | NÃO blocklistar — transitório |

## Arquivos envolvidos
- `/root/agente_roteador_llm.py` (adicionar contador de falhas)
- `/root/agente_autocura_v4.py` (nova invariante)
- `/root/config/falhas_modelos_runtime.json` (novo — criado pelo roteador)
- `/root/config/modelos_vivos.json` (expandir schema com flags de parâmetro)
- `/root/agente_validador_modelos.py` (integrar com flags)

## Pré-requisito
Sprint `validador_modelos_temperature` deve ser feito primeiro (estabelece o schema de flags).
