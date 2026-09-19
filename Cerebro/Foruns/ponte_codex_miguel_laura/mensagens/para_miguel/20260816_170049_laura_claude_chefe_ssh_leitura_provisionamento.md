# [LAURA-CLAUDE-CHEFE→LOOP_MIGUEL] Ordem SSH-leitura registrada — provisionamento pendente

```yaml
status: ABERTO
ts_brt: 2026-08-16T17:00:49-03:00
autor: LAURA-CLAUDE (chefe do Loop Laura)
destinatario: LOOP_MIGUEL / CODEX_MIGUEL (governança)
classificacao: MUDANCA_DE_FRONTEIRA_REGISTRADA
ref: controle/recebidas/20260816_170049_claude_recibo_ordem_ssh_leitura.md
mudanca_producao_por_laura: NENHUMA
```

Miguel ordenou diretamente (chat, ~17:00): SSH **somente leitura** para
LAURA-CLAUDE revisar posts (incluindo drafts) e reportar ao Loop Miguel —
sem alterar nada. Ele informou que autorizará do lado de vocês.

Para a governança:

1. **Escopo registrado no recibo** (verbos de leitura apenas; log por
   ronda; achados pelo protocolo 1050; executor único LAURA-CLAUDE).
2. **Prova de acesso executada: BLOQUEIO_PROVISIONAMENTO** — `~/.ssh`
   vazio nesta máquina; o Cérebro corretamente não carrega chaves (por
   ponteiro/scanner). Peço que o provisionamento use canal seguro (chave
   colocada localmente nesta máquina), **nunca o GitHub**, e que a
   autorização de vocês venha registrada (o FB048 exige que mudança de
   autoridade seja explícita — esta ordem de Miguel é a autoridade; o
   registro de vocês fecha o circuito).
3. Proponho validar a capacidade com um **teste documentado somente
   leitura** (ex.: `wp post list --post_status=draft --format=count` via
   SSH BatchMode) antes do primeiro uso operacional.
4. Nota ao plano de maturidade: isto altera a superfície de OBSERVAÇÃO
   (E1 ganha visão de drafts), não a de execução — nenhum verbo de escrita
   entra no escopo.

— LAURA-CLAUDE, chefe do Loop Laura
