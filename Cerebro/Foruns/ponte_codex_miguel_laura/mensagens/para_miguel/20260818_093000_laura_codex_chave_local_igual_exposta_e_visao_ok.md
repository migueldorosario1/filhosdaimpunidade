# LAURA-CODEX → MIGUEL — chave local é o blob exposto; Codex tem visão

```yaml
ts_brt: 2026-08-18T09:30:52-03:00
classe: ALERTA_SEV1_E_CORRECAO_CAPACIDADE
escrita_wordpress_por_codex: NAO
```

Verificação cega a valores: `C:\Users\migue\.ssh\laura_ed25519` tem o mesmo
blob Git da chave privada versionada em `ec4b2198` (`ec45f06d…`). Portanto os
testes feitos pela chefia às 09:28 usaram a chave exposta, salvo rotação que
não aparece no estado local. IDs inexistentes evitaram alteração de post, mas a
credencial foi autenticada.

Recomendação: congelar o alias, revogar/rotacionar, reinstalar por meio seguro e
só então retestar. A exclusão do HEAD não saneia histórico nem a chave.

Correção operacional adicional: LAURA-CODEX consegue abrir pixels quando há
URL/arquivo recuperável. Detectei visualmente o erro do 266372 e validei o
266381. O que falha é o subcomando E1 `media`, não a capacidade de visão.

Nenhuma chave ou escrita foi usada por esta sessão.

— LAURA-CODEX, 18/08/2026 09:30 BRT
