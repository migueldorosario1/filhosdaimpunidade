# [LAURA-CODEX→MIGUEL] Alerta: autoria Git compartilhada atribui Claude/Grok a Codex

```yaml
status: ABERTO
ts_brt: 2026-08-15T01:57:49-03:00
autor: LAURA-CODEX
destinatario: MIGUEL
prioridade: MEDIA
tipo: ALERTA_TECNICO
ref: loop_trindade_laura/mensagens/codex/20260815_015749_codex_ronda_006.md
executor_sugerido: LAURA-CODEX, somente apos decisao de MIGUEL/LAURA-CLAUDE-CHEFE
```

## Achado

O clone LAURA possui identidade fixa no `.git/config`:

```text
user.name=Codex Laura
user.email=codex-laura@cerebro-miguel.local
```

Assim, commits cujos assuntos e arquivos identificam `LAURA-CLAUDE` ou
`LAURA-GROK` aparecem no historico como autor `Codex Laura`. Evidencias
recentes:

- `71b3238e` — ronda 005 de Claude;
- `67febd07` — ronda 004 de Grok;
- `da875ea7` — ronda 004 de Claude.

O conteudo dos relatorios preserva as assinaturas corretas, mas a trilha Git
fica ambigua e pode contrariar o requisito de identidade propria do contrato.

## Correcao proposta

Fazer cada launcher/agente fornecer sua identidade somente no comando de
commit, sob o lock, por exemplo com `git -c user.name=... -c user.email=...
commit`. Evitar alternar o `.git/config` compartilhado entre sessoes, pois isso
introduziria nova corrida.

Nao alterei launchers nem configuracao: o alerta depende de decisao de Miguel
e coordenacao de `LAURA-CLAUDE-CHEFE`.

— LAURA-CODEX, 15/08/2026 01:57 BRT
