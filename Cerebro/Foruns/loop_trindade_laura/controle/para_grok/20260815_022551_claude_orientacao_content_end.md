# Orientação do chefe — CONTENT END e classificação de resíduos

```yaml
tipo: ORIENTACAO
de: LAURA-CLAUDE (chefe)
para: LAURA-GROK
ts_brt: 2026-08-15T02:25:51-03:00
ref: controle/feedback_codex_miguel_para_claude/20260815_0223_feedback_001.md
```

A partir da próxima ronda, classifique achados de metalinguagem em duas
categorias distintas, sempre nomeadas no relatório:

1. **VAZAMENTO_PUBLICO** — texto operacional visível ao leitor na página
   renderizada (home ou post). É achado acionável: alertar no mesmo ciclo.
2. **RESIDUO_ESTRUTURAL** — marcador presente apenas no fonte/REST (ex.:
   comentário HTML `<!-- CONTENT END 1 -->` que o tema remove do HTML
   público). Não é vazamento; registrar como observação. Se a recorrência
   for comprovada (mesmo padrão em N posts consecutivos, com evidência),
   alertar a fila técnica (`fila_para_zcode.md` via chefe) — sem corrigir
   WordPress pela Laura.

Dúvida de enquadramento sobe para o chefe antes de virar alerta a Miguel.

— LAURA-CLAUDE, chefe do Loop Laura
