# Ordem Miguel — inventário não destrutivo do token GitHub no computador Laura

```yaml
tipo: ORDEM_MIGUEL
de: MIGUEL_VIA_CODEX_MIGUEL
para: LAURA-CLAUDE-CHEFE
executor_sugerido: LAURA-CODEX
ts_brt: 2026-08-16T08:58:00-03:00
prioridade: SEGURANCA
ack_obrigatorio: true
prazo: 2026-08-16T10:20:00-03:00
```

Claude Laura,

Miguel prepara a rotação sobreposta do token GitHub. No computador Miguel, o
Git do Cérebro já foi migrado para SSH, mas o token continua válido no chaveiro
para `gh`/API. Antes de revogá-lo precisamos saber se algum dos três agentes ou
alguma automação no computador Laura depende da mesma credencial.

Coordene um inventário somente leitura e devolva um relatório sanitizado:

1. protocolo do remote de `cerebro-miguel` em Laura (`SSH`, `HTTPS sem token`
   ou `HTTPS com credencial embutida` — nunca mostre a URL autenticada);
2. existência e tipo de credential helper/chaveiro;
3. se `gh` está autenticado e se a impressão SHA-256 curta do token ativo é
   igual ou diferente de `d2ef4cbfd92f`; nunca imprima o token;
4. quais agentes/launchers/scripts usam `gh` ou API do GitHub, por nome e
   finalidade, sem valores de ambiente;
5. quais usam apenas `git pull/push` e podem migrar para SSH;
6. proposta de teste de leitura e escrita que não altere produção nem abra PR;
7. estado final: `ROTACAO_SEGURA` ou `DEPENDENCIAS_A_MIGRAR`, com lista.

Não trocar remote, token, chaveiro, launcher, configuração ou serviço nesta
ordem. Não executar login/logout/revogação. Se não houver método seguro para
calcular a impressão sem exibir a chave, declare `IMPRESSAO_NAO_COLETADA`.

Isto não autoriza WordPress, SSH de servidor, publish, trash, deploy ou qualquer
mudança de produção.

— Miguel, por Codex Miguel
