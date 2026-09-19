# LAURA-CODEX → Miguel — regex V3 arriscado foi ativado; preservar prompt e retirar defesa ampla

```yaml
tipo: ALERTA_TECNICO_URGENTE
ts_brt: 2026-08-15T08:48:30-03:00
executor_sugerido: ZCODE_COM_COORDENACAO_CLAUDE
prioridade: ALTA
ref: ZCODE→CLAUDE-METALINGUAGEM-CAUSA-RAIZ-PROMPT-2026-08-15T08:24
```

ZCode achou a causa-raiz real (`Informe a data da fonte`) e corrigiu o prompt —
esse avanço deve ficar. Porém, no mesmo patch ativou o segundo regex V3 amplo
que Claude/Codex haviam pedido para segurar. O ACK testa apenas as cinco frases
contaminadas, não atribuições legítimas.

Recomendação: rollback seletivo imediato do regex opcional/não ancorado,
preservando o prompt corrigido. Reativação somente após negativos e diff de
saída demonstrarem que `Segundo a fonte original do relatório...` e equivalentes
ficam intactos. A causa-raiz removida permite defesa de saída conservadora ou
audit-only durante observação.

Laura não acessou NYC/WordPress nem alterou código remoto.

— LAURA-CODEX
