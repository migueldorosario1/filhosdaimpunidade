# Delegação do chefe — gate visual: inspeção semântica de imagens (ORDEM CRÍTICA)

```yaml
tipo: DELEGACAO
de: LAURA-CLAUDE (chefe)
para: LAURA-GROK
ts_brt: 2026-08-16T18:19:02-03:00
refs:
  - controle/para_claude/20260816_180538_codex_ordem_miguel_gate_visual_fail_close.md
  - controle/feedback_codex_miguel_para_claude/20260816_180538_feedback_061_gate_visual.md
prioridade: CRITICA
```

Nova tarefa permanente de ronda (Ordem Miguel): **inspeção visual
semântica** da imagem destacada dos posts novos.

## Antes de tudo: PROVA DE CAPACIDADE (regra do chefe, FB050)

Na tua primeira ronda com esta delegação, teste: consegues baixar a imagem
destacada (URL pública da mídia) E analisá-la visualmente (descrever o que
há nela)? Registra o resultado:

- **SIM** → o gate roda pleno: por post novo com imagem, responder "a
  imagem mostra X; o post fala de Y; adequada?" →
  `APROVADA`/`REPROVADA`/`INCONCLUSIVA` com uma linha de justificativa.
- **NÃO** (CLI sem visão) → TODO item sai `INCONCLUSIVA` com nota
  "sem capacidade de visão no executor" — **nunca** aprovar por metadado,
  legenda, filename ou cadastro (o 266029 provou que o cadastro mente).

## Regras do gate

1. Metadado NÃO é prova — só a imagem aberta conta.
2. `REPROVADA`/`INCONCLUSIVA` → me avisa na ronda; eu alerto o Loop Miguel
   imediatamente.
3. **Troca de mídia zera o parecer anterior** (re-inspecionar).
4. Nada de alteração de WP; hero 480x360 do YouTube segue não-bug (regra
   antiga), mas o CONTEÚDO da imagem entra no gate igual.

— LAURA-CLAUDE, chefe do Loop Laura
