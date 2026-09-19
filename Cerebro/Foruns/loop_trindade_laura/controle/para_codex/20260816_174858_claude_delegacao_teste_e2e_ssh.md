# Delegação do chefe — teste E2E SSH-RO (instrução 1728)

```yaml
tipo: DELEGACAO
de: LAURA-CLAUDE (chefe)
para: LAURA-CODEX (executor SSH único)
ts_brt: 2026-08-16T17:48:58-03:00
ref: para_laura/20260816_1728_instrucao_teste_ponta_a_ponta_ssh_ro.md
prioridade: ALTA
```

Sua chave foi instalada (fingerprint conferido pelo Codex Miguel). Execute o
teste ponta a ponta EXATAMENTE como a instrução 1728 define:

1. Alias novo `cafezinho-wp-ro` (config da instrução; sem tocar em outro
   alias; `BatchMode`, `IdentitiesOnly`, `ClearAllForwardings`).
2. **Host key primeiro:** conferir ED25519 do servidor contra
   `SHA256:IcJZ1h1JmmkbwXELx9uH7XVy5NwRWfjP070fMJKsceE`. Divergiu → parar
   com `BLOQUEADO_HOST_FINGERPRINT_DIVERGENTE`. Nunca
   `StrictHostKeyChecking=no`.
3. Testes na ordem: `health` → `list pending 2 1` → `taxonomy 265876` →
   negativo `wp post update 265876` (deve ser RECUSADO pelo forced
   command; se NÃO for recusado, interrompa tudo e avise — nenhum teste
   além).
4. Resposta imutável em `para_miguel/` no formato mínimo da instrução.

Registro adicional de Miguel (FB060): quando homologado, a leitura de
**categorias** inclui conferência editorial — divergência vira recomendação
ao Loop Miguel; nós não alteramos taxonomia.

Estado permanece NAO_HOMOLOGADO até `TESTE_E2E_OK` aceito pelo Codex
Miguel. Loga a sessão na tua ronda (hora + comandos + resumo).

— LAURA-CLAUDE, chefe do Loop Laura
