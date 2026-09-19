# [LAURA-CLAUDE-CHEFE→MIGUEL] Atualização única — rollback do regex amplo sem ACK há 2 janelas

```yaml
status: ABERTO
ts_brt: 2026-08-15T09:48:47-03:00
autor: LAURA-CLAUDE (chefe do Loop Laura)
destinatario: MIGUEL (decisão)
tipo: ATUALIZACAO_DE_ESCALADA_LIMIAR_60MIN
refs:
  - para_miguel/20260815_084957_laura_claude_chefe_rollback_seletivo_regex_urgente.md (primeira escalada)
  - loop_trindade_laura/controle/para_claude/20260815_084830_codex_regex_v3_ativo_rollback_seletivo.md
```

Conforme o limiar de formação sugerido no Feedback 011 (risco URGENTE de
alteração silenciosa de conteúdo + duas janelas sem ACK do executor), esta é
a **única** atualização direta — não haverá re-ping por ronda.

- **Primeira escalada:** 08:49 (endosso à auditoria de Codex de 08:48).
- **Exposição:** o segundo regex amplo (opcional/não ancorado) está ativo em
  produção desde **08:24** — ~85 minutos até esta atualização, sem ACK.
- **Evidência disponível:** análise estática de Codex (risco de apagar
  atribuições como "Segundo a fonte original do relatório, ..."); nenhum
  sintoma público detectado por Grok até 09:26 — o que não prova ausência de
  dano, pois o erro é silencioso.
- **Ação mínima recomendada:** desativar apenas o segundo padrão amplo (ou
  movê-lo para audit-only), preservando o fix causal do prompt; depois,
  auditar por diff os textos processados desde 08:24.

Decisões que só você pode tomar: (a) executar/ordenar o rollback seletivo;
(b) confirmar se o limiar de 2 janelas vira regra permanente de escalada
(classifiquei como `DEPENDE_MIGUEL`).

Laura permanece somente leitura; nada foi tocado.

— LAURA-CLAUDE, chefe do Loop Laura
