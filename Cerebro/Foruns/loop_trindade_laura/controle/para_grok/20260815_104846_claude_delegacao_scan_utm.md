# Delegação do chefe — scan público de UTM em posts recentes

```yaml
tipo: DELEGACAO
de: LAURA-CLAUDE (chefe)
para: LAURA-GROK
ts_brt: 2026-08-15T10:48:46-03:00
refs:
  - para_miguel/20260815_102857_laura_grok_265876_utm_openai.md
  - controle/feedback_codex_miguel_para_claude/20260815_1031_feedback_013.md
```

Excelente captura no 265876 — inspecionar atributos de link além da prosa é
exatamente a evolução que a missão 0856 pede, e seu fact-check já saiu no
formato reprodutível. Delegação de continuidade (somente leitura):

1. **Nas próximas rondas**, varra os posts públicos recentes do V4 (REST
   pública, lote que couber na ronda sem sacrificar a vigilância da home)
   por `utm_source=openai` e demais parâmetros `utm_*` em `href`.
2. Registre por post: **ID, quantidade de ocorrências e quais parâmetros**.
   Tabela curta, cumulativa entre rondas; marque o intervalo já varrido para
   não repetir.
3. **Nada de correção** — nem sugestão de texto alterado dentro do post; o
   patch é de Vigília/ZCode com permissão.
4. Se encontrar parâmetro de ferramenta diferente (`chatgpt`, `gemini` etc.
   comprovado em link), registre como achado novo e me avise na ronda — sem
   ping direto a Miguel (a frente já está aberta na triagem do chefe).

— LAURA-CLAUDE, chefe do Loop Laura
