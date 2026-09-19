# LAURA-CODEX → Miguel — HOLD no GL-004: reserva apagada pelo sync

```yaml
ts_brt: 2026-08-18T10:27:00-03:00
post_id: 266331
ref: GL-20260818-004
commit_causal: 50d1c4a8
estado: HOLD_RESERVA_INEXISTENTE
wordpress_mutations: 0
```

O sync das 10:22 apagou a reserva ativa do LAURA-GROK para o 266331, junto de
presença/ledger. O pedido imutável permaneceu. O Grok repôs mensagem e ledger
em `283e2cb2`, mas não repôs o livro: o HEAD ainda mostra só a reserva antiga
de GROK, já `APLICADO 266337`.

Portanto `AUTORIZO GL-20260818-004` não deve ser executado até existir reserva
ativa verificável após sync. O pedido também propõe `media-import` por alias
compartilhado, que não supera a ordem ZM-027/ZM-030 de não usar credenciais
expostas. Não editei a reserva nem artefato do Grok.

— LAURA-CODEX
