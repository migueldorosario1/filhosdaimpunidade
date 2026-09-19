# Memória — Modelo k3-256k como econômico do Kimi + top-up bridge de cota

**Data:** 2026-08-07 ~18:15 BRT
**Sessão:** ZCode (GLM-5.2, builtin:zai-coding-plan) — workspace ZCodeProject
**Tipo:** Log técnico completo (Tema Duplo — fórum irmão: `Foruns/forum_k3_256k_modelo_economico_kimi_topup_20260807.md`)

---

## Especificação técnica do modelo `k3-256k` (doc Kimi Code)

| Campo | Valor |
|---|---|
| Model ID | `k3-256k` |
| Model version | Kimi K3 (256k) |
| Context window | 256k (262144) |
| Reasoning | low / high / max (default high) |
| Multimodal input | **Image only** (sem vídeo — diferencial vs `k3` 1M) |
| Quota consumption | ~metade do `k3` (1M) |
| Disponibilidade | Todos os membros Moderato+ |

Citação da doc: *"k3-256k is now available. Within 256k context, it delivers the same results. k3 (1M) consumes about twice as much quota as k3-256k."*

## Mapeamento de reasoning effort (K3)

```
# default
null / undefined       → high
any other unknown       → HTTP 400 error

# → max
ultra / max / xhigh     → max

# → high (recomendado)
high / medium           → high

# → low
low / minimum / light   → low

# → thinking disabled
none                    → thinking.type disabled
```

⚠️ K3/K2.7 com Thinking OFF roteia para K2.6 — manter thinking ligado.

## IDs de modelo válidos no seletor/API

- `k3` (1M)
- `k3-256k` (256k) ← NOVO, adicionado nesta sessão
- `kimi-for-coding` (K2.7 Code)
- `kimi-for-coding-highspeed` (K2.7 HighSpeed, 6× velocidade, 3× quota)

NÃO usar nomes de versão ("Kimi K3", "K2.7 Code") — causa erro.

## Base URLs (protocolos suportados)

| Protocolo | Base URL |
|---|---|
| OpenAI compatible | `https://api.kimi.com/coding/v1` |
| Anthropic compatible | `https://api.kimi.com/coding/` |

(O provedor "Kimi 3" no ZCode usa o endpoint OpenAI compatible.)

## Mudança aplicada no `~/.zcode/v2/config.json`

### Provedor afetado
- ID: `abc953f0-69af-46c9-bd91-6cb53f7edc2c`
- Name: "Kimi 3"
- kind: `openai-compatible`
- baseURL: `https://api.kimi.com/coding/v1`

### Antes (modelos)
- `kimi-k3` (1M, reasoning max default)

### Depois (modelos)
- `kimi-k3` (1M) — **mantido intacto**
- `k3-256k` (256k) — **adicionado**:
```json
"k3-256k": {
  "reasoning": {
    "enabled": true,
    "variants": ["low", "high", "max"],
    "defaultVariant": "high"
  },
  "limit": {
    "context": 262144,
    "output": 131072
  },
  "modalities": {
    "input": ["text"],
    "output": ["text"]
  }
}
```

### Backup
`~/.zcode/v2/config.json.bak_pre_k3-256k_20260807_1812` (10007 bytes, original preservado).

## Comando de teste ao vivo (prova)

```bash
curl -s -X POST "https://api.kimi.com/coding/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-kimi-7NUid…(no cofre)" \
  -d '{
    "model": "k3-256k",
    "messages": [{"role":"user","content":"Diga só: PING OK"}],
    "max_tokens": 50
  }'
```

Resultado: HTTP 200, `"model":"k3-256k"`, usage reportado. **Crédito extra do Miguel funcionando.**

## Cenário de crédito (state)

- Assinatura Kimi vigente até 23/08/2026.
- Cota semanal esgotou rápido (Miguel reporta "acabou muito rápido").
- Assinaturas novas em fila de espera (fechadas).
- Miguel aplicou **crédito extra (top-up pay-as-you-go)** para cobrir ~5 dias até renovação semanal.
- Decisão: usar só `k3-256k` no top-up → dobra a duração do mesmo crédito.

## Cadeia de failover (vigente, não alterada)

Kimi K3 (`k3-256k` default) → Qwen Code (Token Plan, `qwen3.8-max`) → GLM-5.2 (Z.ai coding plan, modelo atual desta sessão).

Definida no `~/.zcode/AGENTS.md` (VIGÍLIA DE CRÉDITO) e implementada no `~/.zcode/hooks/credito_vigilia.py`.

## Próximos passos

1. Miguel reinicia o ZCode → seleciona `k3-256k` no seletor Kimi 3.
2. Testa uma tarefa real de código/gestão.
3. Se atender → segue no 256k como default econômico.
4. Se não → volta no `kimi-k3` (1M) com um clique no seletor.

## Pendências / decisões futuras

- Quando a assinatura semanal renovar: avaliar se mantém `k3-256k` como default (provável sim — economia sem perda de qualidade para o padrão de uso) ou volta ao 1M.
- Considerar adicionar `k3-256k` como modelo preferencial explícito na Vigília de Crédito (`credito_vigilia.py`) — hoje a cadeia só fala "Kimi K3" genericamente.

## Refs

- Doc Kimi Code (Model Configuration) — fonte canônica dos specs.
- Fórum irmão: `Foruns/forum_k3_256k_modelo_economico_kimi_topup_20260807.md`.
- Vigília: `~/.zcode/hooks/credito_vigilia.py` + `~/.zcode/AGENTS.md`.
- Config: `~/.zcode/v2/config.json` (provedor `abc953f0-…` "Kimi 3").
