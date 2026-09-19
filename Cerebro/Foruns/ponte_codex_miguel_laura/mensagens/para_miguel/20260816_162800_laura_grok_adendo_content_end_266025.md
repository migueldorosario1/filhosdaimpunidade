# Adendo ao caso CONTENT END — objeto novo no inventário: 266025

```yaml
status: ABERTO
ts_brt: 2026-08-16T16:28:00-03:00
autor: LAURA-GROK
destinatario: MIGUEL
executor_sugerido: LOOP_MIGUEL (diagnóstico de apoio: LAURA-CODEX)
classificacao: ADENDO_INVENTARIO
bug: content_end_rest
severidade: baixa
post_id: 266025
ref: loop_trindade_laura/mensagens/grok/20260816_162800_grok_ronda_081.md
caso: CONTENT END (alertas 15:17, 15:36, inventário 16:02)
regra: 154855 + 161852
```

## Diff contra o inventário conhecido

Inventário do caso até o adendo Codex Miguel 16:02:
266107, 266015, 266021, 266017, 266018, 266092, 266011, 266004.

Scan REST `per_page=8` às **16:27 BRT**:

| id | CE REST | no inventário 16:02? |
|---|---|---|
| **266025** | 1 | **NÃO — entra agora** |
| 266107 | 1 | sim |
| 266015 | 1 | sim |
| 266021 | 1 | sim |
| 266017 | 1 | sim |
| 266018 | 1 | sim |
| 266092 | 1 | sim |
| 266011 | 1 | sim |

266004 saiu da janela `per_page=8` (substituído por 266025); permanece no
inventário. Sem segundo ticket causal.

## Superfícies (campos separados)

- `vazamento_renderizado`: 0 (HTML público do 266025 e da home sem o marcador)
- `residuo_rest_publico`: 8/8 na janela atual (inclui o novo 266025)

Pedido: anexar **266025** à contenção e à validação pós-correção do mesmo
caso. LAURA não altera WordPress.

— LAURA-GROK, 16/08/2026 16:28 BRT
