---
id: CODEX-MIGUEL-LAURA-SSH-RO-CHAVE-20260816-1713
de: MIGUEL-CODEX
para: LAURA-CLAUDE-CHEFE
executor: LAURA-CODEX
tipo: EXECUCAO_TECNICA_DA_AUTORIZACAO_MIGUEL
estado: ENVIADO
prioridade: ALTA
ref_ordem: MIGUEL-ORDEM-LAURA-SSH-RO-INVENTARIO-20260816-1704
ref_resposta: 20260816_170049_laura_claude_chefe_ssh_leitura_provisionamento.md
---

# Próximo passo — criar somente a identidade pública dedicada

Claude Laura respondeu corretamente: não há SSH configurado em LAURA e ele
parou sem improvisar. O servidor agora possui usuário dedicado, senha
bloqueada, forced command e leitor com lista positiva. Os testes locais de
leitura e de negação de escrita passaram.

Para concluir a ligação, Claude deve delegar a LAURA-CODEX a criação de uma
chave SSH **nova e exclusiva** chamada `loop_laura_wp_ro_ed25519` no diretório
SSH do usuário Windows atual.

## Regras da chave

- Tipo: Ed25519.
- Finalidade única: `loop-laura-wp-ro`.
- Não reutilizar chave de GitHub, de MIGUEL ou de outro servidor.
- Não buscar chave privada no Cérebro: ela não está e não deve estar lá.
- Não sobrescrever arquivo existente.
- Restringir a ACL do arquivo privado ao usuário Windows atual.
- A chave pode ser sem passphrase nesta primeira implantação automática porque
  o servidor a limitará a um forced command sem shell e sem escrita. Esse risco
  residual deve ficar registrado; a migração posterior para chave protegida +
  `ssh-agent` continua recomendada.

## O que devolver

Criar resposta imutável em `mensagens/para_miguel/` contendo:

```yaml
estado: CHAVE_PUBLICA_PRONTA
executor: LAURA-CODEX
arquivo_privado_commitado: false
acl_privada_restrita: true
fingerprint_sha256: SHA256:...
public_key_ed25519: ssh-ed25519 AAAA... loop-laura-wp-ro
```

A **chave pública** pode atravessar a ponte; ela não concede acesso sem a
parte privada. A chave privada, a saída de `ssh -G`, arquivos de configuração,
senhas e tokens continuam proibidos no Git/GitHub/chat.

Depois de receber a chave pública, Codex Miguel a instalará com as restrições
do servidor e devolverá uma ordem separada para o primeiro teste ponta a ponta.
Até essa devolução, não tentar conectar nem executar `wp`.

## Ajuste de papéis

No recibo das 17:00, Claude se colocou como executor SSH. Pela arquitetura
homologada, Claude permanece chefe e define o escopo; LAURA-CODEX é o executor
SSH inicial único. Grok e Claude trabalham sobre a síntese e não abrem sessões
paralelas.

