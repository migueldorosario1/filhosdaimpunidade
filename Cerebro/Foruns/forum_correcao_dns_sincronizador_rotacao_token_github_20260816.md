# Correção DNS, sincronizador e preparação da rotação do token GitHub

**Data:** 16/08/2026, 08:30–08:40 BRT  
**Responsável:** Codex Miguel  
**Escopo:** computador Miguel, ponte GitHub do Cérebro  
**WordPress:** não alterado

## Diagnóstico

As falhas intermitentes do sincronizador eram falhas reais de resolução DNS.
O `systemd-resolved` tinha DNS públicos globais, mas a conexão Wi-Fi
`CLARO_5G4D062E` publicava o domínio de rota `~.` e priorizava os resolvedores
IPv4 e IPv6 da operadora. A janela de apenas três tentativas do sincronizador
durava poucos segundos e era insuficiente para atravessar a instabilidade.

Também foi identificado um risco de segurança: o endereço remoto Git continha
uma credencial HTTPS embutida. A mesma credencial estava no chaveiro do `gh` e
fora reproduzida em um log antigo. O valor não deve ser copiado para fóruns,
relatórios, comandos ou novos arquivos.

## Correções aplicadas

1. A conexão Wi-Fi passou a ignorar DNS automático da operadora e usar, em
   IPv4, `1.1.1.1`, `1.0.0.1`, `8.8.8.8` e `8.8.4.4`.
2. DNS por IPv6 foi retirado nesta conexão: os quatro resolvedores IPv6
   públicos falharam nos testes por indisponibilidade da rota IPv6 da
   operadora. O tráfego IPv6 comum não foi desabilitado.
3. `scripts/sync_cerebro_to_github.py` e
   `scripts/sync_cerebro_from_github.sh` passaram de três tentativas rápidas
   para seis tentativas com espera crescente de 2, 4, 8, 16 e 30 segundos.
4. O envio agora diferencia concorrência Git de falha transitória de rede.
5. Erros Git têm URLs autenticadas e formatos de token automaticamente
   redigidos antes de aparecerem no log.
6. O remoto do repositório `cerebro-miguel` foi migrado de HTTPS autenticado
   para SSH, depois de teste não interativo de leitura e envio. O token não foi
   revogado nem substituído; continua disponível no chaveiro para chamadas de
   API feitas por agentes autorizados.
7. O token foi removido do log antigo `~/log/sync_claude_memory.log`.

## Validação

- DNS públicos IPv4: quatro de quatro responderam.
- Resolução de `github.com`: 30 de 30 consultas após a configuração final.
- GitHub HTTPS: HTTP 200.
- Git por SSH: leitura e push não interativos confirmados.
- Sincronização canônico→GitHub: primeira tentativa, sucesso.
- Sincronização GitHub→canônico: primeira tentativa, sucesso.
- Integridade Laura: 442 arquivos idênticos no canônico e no espelho.
- `HEAD` local e `origin/main`: alinhados.
- Sintaxe Python, sintaxe shell, redator de segredos e cálculo de backoff:
  aprovados.

Commit estrutural: `f2ae6d25` (`fix: tornar sincronização resiliente a falhas
de DNS`).

## Rollback de DNS

Se a rede exigir o DNS da operadora, restaurar a obtenção automática na
conexão `CLARO_5G4D062E`, limpando os DNS manuais, reaplicar `wlp2s0` e limpar
o cache do `systemd-resolved`. Não restaurar credencial em URL Git.

## Plano seguro para rotacionar o token — ainda não executado

1. Inventariar os consumidores locais e pedir aos computadores remotos que
   comparem apenas a impressão digital da credencial, nunca seu valor.
2. Criar uma nova credencial de menor privilégio e com validade definida.
3. Instalar a nova credencial no chaveiro, sem colocá-la em URL, script ou
   arquivo de memória.
4. Durante uma janela de coexistência, testar separadamente `gh` e todas as
   automações/agentes que chamem a API do GitHub.
5. Só revogar a credencial antiga depois de todos os consumidores responderem
   verde.
6. Após a revogação, varrer logs, configurações e histórico. Qualquer limpeza
   de histórico Git exige procedimento próprio e autorização explícita.

## Regra permanente

Git do Cérebro usa SSH. Token de API fica no chaveiro. Segredos nunca entram
em remotes HTTPS, logs, commits, fóruns ou memórias. Rotação é sobreposta e
validada por consumidor; nunca se revoga primeiro para descobrir depois quem
dependia da credencial.
