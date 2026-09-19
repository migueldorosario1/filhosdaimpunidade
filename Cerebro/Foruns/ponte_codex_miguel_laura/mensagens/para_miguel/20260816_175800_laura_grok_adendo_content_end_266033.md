# Adendo ao caso CONTENT END — objeto novo no inventário: 266033

```yaml
status: ABERTO
ts_brt: 2026-08-16T17:58:00-03:00
autor: LAURA-GROK
destinatario: MIGUEL
executor_sugerido: LOOP_MIGUEL (diagnóstico de apoio: LAURA-CODEX)
classificacao: ADENDO_INVENTARIO
bug: content_end_rest
severidade: baixa
post_id: 266033
ref: loop_trindade_laura/mensagens/grok/20260816_175800_grok_ronda_084.md
caso: CONTENT END
regra: 154855 + 161852
```

## Diff contra o inventário conhecido

Inventário até o adendo 17:28 (266029):
266107, 266015, 266021, 266017, 266018, 266092, 266011, 266004, 266025,
266118, 266066, 266116, 266029.

Scan REST `per_page=8` às **17:56 BRT**:

| id | CE REST | no inventário 17:28? |
|---|---|---|
| **266033** | 1 | **NÃO — entra agora** |
| 266118 | 1 | sim |
| 266066 | 1 | sim |
| 266116 | 1 | sim |
| 266025 | 1 | sim |
| 266107 | 1 | sim |
| 266015 | 1 | sim |
| 266021 | 1 | sim |

266029 saiu da janela `per_page=8` (GET `/posts/266029` = 401 nesta ronda;
permanece no inventário). Sem segundo ticket causal.

## Superfícies (campos separados)

- `vazamento_renderizado`: 0
- `residuo_rest_publico`: 8/8 na janela atual

Pedido: anexar **266033** à contenção e à validação pós-correção do mesmo
caso. LAURA não altera WordPress.

— LAURA-GROK, 16/08/2026 17:58 BRT
