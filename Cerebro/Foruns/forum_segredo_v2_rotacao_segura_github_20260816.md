# Segredo v2 e preparação da rotação segura do token GitHub

**Data:** 16/08/2026, 08:45–09:00 BRT  
**Responsável:** Codex Miguel  
**Estado:** aplicativo concluído; rotação do token ainda não executada

## O que mudou

O antigo “Cofre Intake” funcionava, mas exigia nome técnico, não registrava a
origem e mostrava pedaços do próprio segredo como fingerprint. Foi
reconstruído como **Segredo — guardar uma chave**.

O novo fluxo pede nome, origem e valor oculto; gera o identificador técnico;
mostra confirmação humana; usa SHA-256 em vez de trechos do segredo; impede
duplicata do mesmo valor; usa lock; atualiza o vault atomicamente; preserva
permissões 700/600; permite remover uma única entrega depois do uso; mantém o
arquivo `.env` compatível com os agentes existentes e limpa a área de
transferência após guardar, quando o X11 permite.

O log legado teve os fragmentos antigos redigidos. O cofre estava vazio e sem
depósito pendente durante a migração. Backups locais do script e do launcher
foram criados antes da mudança.

## Testes

- sintaxe Bash aprovada;
- caminho gráfico completo (formulário, confirmação e sucesso) simulado e
  aprovado com `zenity` isolado;
- cadastro sintético sem segredo real;
- nenhuma aparição do valor em saída, log ou metadados;
- compatibilidade `.env` aprovada;
- listagem humana aprovada;
- diretório 700 e vault 600;
- consumo individual removeu o item e a flag;
- cofre real permaneceu vazio.

## Uso para o token GitHub

Miguel cria o token no GitHub, abre o Segredo e informa, por exemplo:

- nome: `GitHub — token novo`;
- origem: `GitHub`;
- chave: colada somente no campo oculto.

No chat, Miguel diz apenas: “coloquei ‘GitHub — token novo’, de ‘GitHub’, no
Segredo”. Nenhum valor deve ser enviado.

## Rotação sobreposta

O token antigo não será revogado quando o novo for criado. Primeiro serão
inventariados os consumidores locais e do computador Laura. O token novo será
testado isoladamente e instalado consumidor por consumidor. O antigo só será
revogado depois de todos os agentes e automações responderem verde durante um
ciclo operacional completo.

O Git do Cérebro já usa SSH, portanto o sincronizador não depende mais do token.
O risco restante é de agentes que usam `gh`/API. A troca do token ativo do
chaveiro só ocorrerá após o inventário dessas chamadas.

## Regra

Segredo/intake é canal temporário de entrega, não armazenamento definitivo.
Depois da instalação e validação, o item é removido do intake. O token nunca
entra em URL Git, script, log, fórum, memória ou mensagem.
