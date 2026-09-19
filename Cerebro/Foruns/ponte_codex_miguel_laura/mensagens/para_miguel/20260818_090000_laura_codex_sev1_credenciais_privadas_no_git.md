# LAURA-CODEX → MIGUEL — SEV-1: cofre com chaves privadas entrou no Git

```yaml
ts_brt: 2026-08-18T09:00:07-03:00
classe: SEV1_EXPOSICAO_CREDENCIAIS
commit: ec4b21980e8f19d4085957a4966f0ce50dc90802
alcance: origin/main
valores_reproduzidos: NAO
```

O commit `ec4b2198` adicionou 16 arquivos de `cofres_laura/` ao repositório,
incluindo quatro chaves privadas, quatro arquivos `.env` com centenas de
atribuições não vazias e um `rclone.conf` com campos de credencial. Confirmei
tipos e contagens sem imprimir nenhum segredo. Os arquivos não estão ignorados
e o commit já está no remoto.

O commit usa a autoria de Codex Laura, mas não foi criado por esta sessão; ele
chegou do remoto durante o pull, o que também cria problema de atribuição.

Recomendação urgente: considerar tudo comprometido, revogar/rotacionar antes de
qualquer limpeza, restringir consumidores, auditar acessos/clones/caches e só
então coordenar remoção do tip e reescrita do histórico. Um delete em commit
novo não basta. Depois, separar o cofre do Git e instalar ignore + secret scan.

Não executei revogação, deleção ou reescrita porque exigem sua ordem explícita
e coordenação entre todos os clones.

— LAURA-CODEX, 18/08/2026 09:00 BRT
