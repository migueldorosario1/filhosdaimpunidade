# Índice — SSH read-only do Loop Laura

**Estado atual:** HOMOLOGADO_READ_ONLY
**Autorizado por Miguel:** 16/08/2026, 17:04 BRT  
**Homologado tecnicamente:** SIM — decisão Codex Miguel, 16/08/2026, 18:24 BRT  
**Executor SSH inicial:** LAURA-CODEX  
**Chefe:** LAURA-CLAUDE

## Regra vigente

- Protocolo: `cerebro/Foruns/forum_protocolo_ssh_read_only_loop_laura_20260816.md`
- A autorização é apenas leitura editorial de `draft`, `pending`, `future` e
  `publish`.
- A leitura inclui categorias e tags vinculadas ao post (ID, nome e slug),
  e a avaliação de sua correção editorial, conforme adendo direto de Miguel
  às 17:19; não inclui alteração taxonômica.
- O acesso administrativo existente em MIGUEL não pode ser copiado ou usado.
- Depois da homologação, somente LAURA-CODEX executa a interface fixa de
  leitura. A homologação não concede shell, WP-CLI livre, SQL, transferência,
  edição, publicação, troca de mídia, cron, deploy ou serviço.
- `HOMOLOGADO` só pode ser escrito aqui por Codex Miguel depois dos testes
  positivos e negativos do canal restrito.

## Evidências

- Auditoria MIGUEL 16/08 17:04: alias administrativo existente; leitor
  dedicado ausente; Cérebro sem chave privada/senha literal versionada.
- Inventário LAURA: CONCLUÍDO por Claude Laura em 16/08 17:00 — diretório SSH
  vazio, sem alias/chave e sem tentativa de WordPress.
- Chave pública dedicada/fingerprint: INSTALADA; fingerprint conferido nos
  dois lados (`SHA256:nOEQQcIO3FmaIZZLGfD72RLJPwxwyfzRICjzXyKXNEc`).
- Usuário remoto dedicado: INSTALADO, senha bloqueada, sem grupos adicionais.
- Forced command e leitor com lista positiva: INSTALADOS no servidor.
- Teste local de leitura pelo usuário dedicado: OK (`health`, `pending`,
  `future`).
- Teste local de bloqueio: OK para comando de escrita pela gateway e WP-CLI
  direto pelo usuário dedicado.
- Defesa SSH por usuário: ATIVA — somente chave pública, senha/keyboard
  interactive negados, `ForceCommand` ativo, forwarding e TTY negados.
- Log servidor: ATIVO via tag `cafezinho-wp-ro`, com operação e resultado,
  sem corpo do post nem segredo.
- Teste SSH ponta a ponta com chave descartável MIGUEL: OK para `health` e
  `taxonomy 265876`; tentativa de escrita negada.
- Teste de revogação da chave descartável: OK (conexão recusada após retirada).
- Teste SSH ponta a ponta com a chave Laura: OK em 16/08/2026 17:59 BRT
  (`health`, `list pending`, `taxonomy 265876`; todos em
  `editorial_read_only`).
- Teste negativo com a chave Laura: OK — tentativa de escrita recusada pelo
  forced command, exit 1 e `command_denied`; sem alteração no WordPress.
- Teste de revogação da chave Laura: PENDENTE.

## Histórico de estado

- 16/08/2026 17:04 BRT — `AUTORIZADO_NAO_HOMOLOGADO`.
- 16/08/2026 17:00 BRT — inventário de Claude Laura recebido:
  `ACESSO_AUSENTE`; provisionamento solicitado sem segredo no Git.
- 16/08/2026 17:13 BRT — corredor remoto instalado e testes locais positivos;
  estado `AGUARDANDO_CHAVE_PUBLICA_LAURA`.
- 16/08/2026 17:19 BRT — Miguel incluiu expressamente categorias na leitura;
  a interface `taxonomy <post_id>` já atendia ao escopo. Laura pode avaliar se
  estão corretas e recomendar ajuste ao Loop Miguel, sem aplicá-lo.
- 16/08/2026 17:22 BRT — defesa SSH em profundidade e logging ativados; chave
  descartável leu saúde/taxonomia, teve escrita negada e foi revogada com
  sucesso.
- 16/08/2026 17:28 BRT — chave pública exclusiva de Laura recebida, fingerprint
  conferido e instalada na conta restrita; estado
  `CHAVE_INSTALADA_AGUARDANDO_TESTE_LAURA`.
- 16/08/2026 17:59 BRT — LAURA-CODEX concluiu o teste ponta a ponta: leituras
  permitidas funcionaram e a escrita foi negada; zero alteração no WordPress.
- 16/08/2026 18:24 BRT — Codex Miguel aceitou formalmente as evidências e
  declarou `HOMOLOGADO_READ_ONLY`, sem ampliar o escopo autorizado.


## Nota de honestidade técnica

O servidor consegue impedir shell e escrita editorial, mas os três CLIs de
LAURA hoje compartilham o mesmo usuário Windows. Portanto, “Codex é o executor
único” é uma regra de governança comprovada pelo relatório e pelo log da
sessão, não isolamento criptográfico entre os três CLIs. A chave dedicada
continua separada de todas as identidades MIGUEL e pode ser revogada sozinha.
