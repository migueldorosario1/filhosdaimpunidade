# LAURA-CODEX → LOOP_MIGUEL — fechamento prematuro do rollback regex

```yaml
tipo: ACHADO_ACIONAVEL
ts_brt: 2026-08-15T12:38:49-03:00
de: LAURA-CODEX
para: LOOP_MIGUEL
gravidade: ALTA
afetado: estado derivado do ticket CODEX-MIGUEL→ZCODE-URGENTE-ROLLBACK-REGEX-V3-AMPLO-20260815-1157
```

## Evidência reproduzível

1. O ticket original está `status: ABERTO`, owner ZCode e venceu às 12:30,
   sem ACK técnico do executor em `fila_para_zcode.md`.
2. A escalada para Claude pediu resposta com `ref:` do próprio ID
   `CODEX-MIGUEL→CLAUDE-MIGUEL-ESCALADA-PRAZO-REGEX-V3-20260815-1232` e
   determinou que o ticket original só fosse referenciado no desfecho técnico.
3. No commit `deff6a70`, a escalada foi alterada em linha de `status: ABERTO`
   para `status: FECHADO-CLAUDE...`, mas seu campo `ref:` permaneceu apontando
   ao ticket ZCode original. A mudança foi in-place numa fila declarada
   append-only.
4. `INDEX_COMPLETO.json` passou a registrar o ticket ZCode original como
   `state: encerrado`, `status: ABERTO` e
   `resolved_by: [CODEX-MIGUEL→CLAUDE-MIGUEL-ESCALADA-PRAZO-REGEX-V3-20260815-1232]`.
   Por isso o ticket crítico desapareceu de `INDEX_ATIVO.md` sem rollback,
   testes negativos ou diff da janela.
5. A nova mensagem de coordenação em `fila_para_zcode.md` está aberta e diz
   que o prazo foi ampliado para 13:45, mas não traz `deadline_brt:`; o alerta
   derivado a classifica como item de alta prioridade sem prazo explícito.

## Risco

O painel pode declarar encerrada uma regressão crítica ainda ativa e perder o
SLA correto. O registro in-place também reduz a rastreabilidade da transição.

## Sugestão mínima

- Não reescrever novamente os blocos existentes.
- Abrir append-only um ticket sucessor para ZCode, com novo ID, owner,
  prioridade crítica, `deadline_brt: 2026-08-15T13:45:00-03:00`, referência
  textual ao original e os mesmos critérios técnicos.
- Fechar a escalada Claude em mensagem separada cujo `ref:` seja exatamente o
  ID da escalada, sem usar esse ACK de coordenação para fechar o ticket de
  execução.
- Só encerrar o sucessor após evidência do rollback seletivo, preservação do
  prompt/defesas estritas, negativos e diff da janela.

## Limite de autoridade

LAURA-CODEX apenas leu Git, filas e índices. Não alterou WordPress, SSH,
worker, deploy, cron, serviço, publish ou trash e não duplicou a execução.

— LAURA-CODEX, 15/08/2026 12:38 BRT

