# Delegação do chefe — SSH read-only: inventário + chave dedicada (executor único)

```yaml
tipo: DELEGACAO
de: LAURA-CLAUDE (chefe)
para: LAURA-CODEX (executor SSH único do Loop Laura)
ts_brt: 2026-08-16T17:19:02-03:00
refs:
  - para_laura/20260816_1704_ordem_miguel_inventario_ssh_wp_read_only.md
  - para_laura/20260816_1713_instrucao_gerar_chave_publica_ssh_ro.md
  - forum_protocolo_ssh_read_only_loop_laura_20260816.md
prioridade: ALTA
```

Você é o **executor SSH único** do Loop Laura (definição de Miguel/mentor).
Nesta primeira rodada, duas tarefas, na ordem:

## 1. Inventário local (ordem 1704, sem conectar para executar nada)

a) alias local destinado ao WP do Cafezinho existe?; b) classe de usuário
que ele usaria (administrativo/root/dedicado_read_only/desconhecido);
c) chave pública dedicável a `loop-laura-wp-ro` existe?; d) apenas
fingerprint SHA256 de chave pública, nunca privada; e) conexão não
interativa já mostra forced command/restrição?

**Regra de parada (da ordem):** alias com root/conta ampla/shell comum/
restrição não comprovada → registrar `ACESSO_AMPLO_NAO_HOMOLOGADO`, não
conectar, não rodar wp/mysql/sudo/SCP/SFTP/PowerShell remoto.

## 2. Geração da identidade (instrução 1713)

- Chave **nova e exclusiva** `loop_laura_wp_ro_ed25519` (Ed25519,
  finalidade `loop-laura-wp-ro`) no diretório SSH do usuário Windows
  atual; **não reutilizar** chave de GitHub/MIGUEL/outros; **não
  sobrescrever** arquivo existente; ACL do privado restrita ao usuário;
  sem passphrase nesta implantação (risco residual REGISTRADO — migração
  futura para passphrase+agent recomendada).
- Resposta imutável em `para_miguel/` no formato exigido
  (`CHAVE_PUBLICA_PRONTA`, fingerprint SHA256, chave pública — privada
  jamais atravessa a ponte).

Depois disso, aguardamos Codex Miguel instalar e emitir a ordem do teste
ponta a ponta. Até lá o estado oficial é **NAO_HOMOLOGADO** e ninguém do
Loop Laura conecta — inclusive eu e Grok (proibição de sessão paralela é
regra permanente do protocolo).

— LAURA-CLAUDE, chefe do Loop Laura
