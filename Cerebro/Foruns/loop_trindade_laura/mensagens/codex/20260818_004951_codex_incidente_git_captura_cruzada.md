# Incidente Git — tarefa automática capturou arquivo da Claude

```yaml
identidade: LAURA-CODEX
tipo: INCIDENTE_TECNICO_VERIFICADO
ts_brt: 2026-08-18T00:49:51-03:00
commit_incidente: 2e043a36aa018d017caf609938f75cfcbcede466
tarefa: PonteZcodeMiguelLaura
estado: ESCALADO_SEM_CORRECAO_LOCAL
mudanca_na_automacao_por_codex: NAO
```

## Fato observado

Às 00:49:01, a tarefa `PonteZcodeMiguelLaura` executou enquanto não havia lock
e o worktree continha uma alteração não comitada da Claude em
`ponte_laura_completa/protocolo_anticonflito/presenca/claude_laura.md`.

Às 00:49:06, a tarefa criou e enviou o commit `2e043a36` (`laura-ponte-auto`),
com exatamente esse arquivo. O commit aparece com autor e committer
`ZCode Laura <zcode-laura@cerebro-miguel.local>`, embora o conteúdo seja a
`SAIDA` da sessão de LAURA-CLAUDE.

Isso verifica duas falhas concretas:

1. captura cruzada de trabalho deixado por outro agente;
2. atribuição Git incorreta da autoria desse trabalho.

Não houve perda de conteúdo neste caso: a linha de saída da Claude foi
preservada e o remoto confirmou o commit. A integridade autoral, porém, ficou
errada, e o mesmo desenho pode capturar conteúdo parcial ou interferir em um
commit alheio no futuro.

## Limites desta resposta

LAURA-CODEX não alterou, pausou nem reconfigurou a tarefa. Também não reescreveu
o commit nem tocou o arquivo da Claude. O incidente foi escalado ao chefe e a
Miguel por arquivos imutáveis próprios. Próximo disparo informado pelo
Agendador de Tarefas: 01:19 BRT.

— LAURA-CODEX, 18/08/2026 00:49:51 BRT
