---
id: MIGUEL-ORDEM-LAURA-SSH-RO-INVENTARIO-20260816-1704
de: MIGUEL
para: LAURA-CLAUDE-CHEFE
executor_sugerido: LAURA-CODEX
prioridade: ALTA
tipo: ORDEM_MIGUEL
estado: ENVIADO
data_brt: 2026-08-16 17:04
ref_protocolo: cerebro/Foruns/forum_protocolo_ssh_read_only_loop_laura_20260816.md
---

# Ordem de Miguel — iniciar a etapa SSH read-only do WordPress

Miguel autoriza o Loop Laura a acessar por SSH o WordPress canônico do
Cafezinho **somente para leitura editorial** de rascunhos, pendentes,
agendados e publicados.

Esta primeira ordem é exclusivamente de **inventário seguro**. Ela não
autoriza usar uma conta ampla nem executar WP-CLI antes da homologação.

## Ação do chefe

Claude Laura deve:

1. acusar recebimento desta ordem;
2. ler integralmente o protocolo citado no cabeçalho;
3. delegar o inventário a LAURA-CODEX como executor único;
4. impedir que Grok ou o próprio Claude façam conexão SSH paralela;
5. incluir o estado desta implantação no próximo relatório de 30 minutos.

## Inventário de LAURA-CODEX

Sem mostrar segredos, Codex Laura deve verificar:

1. se existe alias local destinado ao WordPress do Cafezinho;
2. qual classe de usuário ele tentaria usar: `administrativo`, `root`,
   `dedicado_read_only` ou `desconhecido`;
3. se existe chave pública que possa ser dedicada a `loop-laura-wp-ro`;
4. somente o fingerprint SHA256 da chave pública, nunca a chave privada;
5. se a conexão, em modo não interativo, já oferece forced command/restrição.

### Regra de parada

Se o alias usar `root`, conta administrativa, shell comum ou restrição não
comprovada:

- registrar `ACESSO_AMPLO_NAO_HOMOLOGADO`;
- não conectar para executar WordPress;
- não rodar `wp`, `mysql`, `sudo`, PowerShell remoto, SCP ou SFTP;
- aguardar Codex Miguel preparar a identidade restrita.

Se não houver alias/chave, registrar `ACESSO_AUSENTE`; não copiar credencial do
GitHub, Cérebro, chat ou outro computador.

## Resposta obrigatória

Criar mensagem imutável em
`ponte_codex_miguel_laura/mensagens/para_miguel/` com `ref` para esta ordem e:

```yaml
estado: INVENTARIO_CONCLUIDO | BLOQUEADO_COM_EVIDENCIA
alias_local: PRESENTE | AUSENTE
classe_usuario: administrativo | root | dedicado_read_only | desconhecido
chave_publica_dedicavel: SIM | NAO
fingerprint_publico_sha256: <fingerprint ou AUSENTE>
forced_command_comprovado: SIM | NAO | NAO_TESTADO
shell_generico_possivel: SIM | NAO | NAO_TESTADO
wp_cli_executado: false
segredo_exposto_no_relatorio: false
proximo_passo: <uma linha>
```

Não incluir host, IP, senha, token, chave, `IdentityFile`, conteúdo do
`~/.ssh/config`, `wp-config.php` ou saída bruta de autenticação.

## Autoridade que permanece negada

Laura não pode editar, criar, publicar, reagendar, desagendar, trocar imagem,
alterar taxonomia/status, mandar à lixeira, instalar, fazer deploy ou executar
SQL/código. Todo achado continua subindo ao Loop Miguel para confirmação e
eventual correção por agente autorizado.

