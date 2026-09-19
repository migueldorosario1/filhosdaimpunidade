# LAURA-CODEX → Miguel — regex da 5ª variante pode apagar conteúdo legítimo

```yaml
tipo: ALERTA_TECNICO
ts_brt: 2026-08-15T07:46:50-03:00
executor_sugerido: ZCODE_COM_REVISAO_CLAUDE
prioridade: ALTA_ANTES_DE_UPSTREAM
ref: CLAUDE→ZCODE-METALINGUAGEM-5A-VARIANTE-PROMPT-WORKER-20260815-0736
```

O novo caso 265908 (`Até a data da fonte original`) prova que a regex V2 ainda
é incompleta. O segundo regex proposto no ticket, porém, torna o artigo opcional
e aceita `fonte original` no meio da frase; ele também apagaria atribuições
legítimas como `Segundo a fonte original do relatório, ...`, possivelmente
deixando texto órfão.

Sugestão: não promover esse padrão amplo ao worker sem testes negativos e diff
de saída. Conter o caso exato ou regenerar; estruturalmente, usar instrução
negativa + validador pré-persistência + regeneração/bloqueio e outcome. O
paliativo aplicado por Claude também merece o mesmo teste antes de novos posts.

Laura não acessou NYC/WordPress nem alterou código remoto.

— LAURA-CODEX
