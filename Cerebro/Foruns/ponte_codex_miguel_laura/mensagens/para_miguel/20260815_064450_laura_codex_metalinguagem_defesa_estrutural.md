# LAURA-CODEX → Miguel — metalinguagem 265903: contenção funcionou, upstream incompleto

```yaml
tipo: ALERTA_TECNICO
ts_brt: 2026-08-15T06:44:50-03:00
executor_sugerido: ZCODE_COM_REVISAO_CLAUDE
prioridade: MEDIA
ref: CLAUDE→ZCODE-METALINGUAGEM-VARIANTE-NOVA-20260815-0607
```

O post 265903 nasceu às 06:02 com `A fonte original desta pauta é`, variante
posterior ao fix upstream 02:25. Claude removeu a frase antes da publicação e
Grok confirmou residual zero: não há vazamento público atual.

O risco restante é de desenho. Ampliar o regex resolve esta frase, mas uma lista
de adjetivos tende a perseguir variantes do LLM. Sugiro manter o patch imediato
e exigir também: instrução negativa no redator, validador pré-persistência do
conceito de processo interno, regeneração/bloqueio com outcome e testes que
preservem atribuições jornalísticas legítimas. Apagar silenciosamente pode
deixar quebra de coesão e esconder a taxa de recorrência.

Laura não acessou NYC/WordPress nem alterou o worker.

— LAURA-CODEX
