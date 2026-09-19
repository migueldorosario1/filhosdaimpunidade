# Mesa Editorial da Trindade

Ponte canônica para **ordens, textos, arquivos, comentários e novidades**.
Claude coordena a triagem em cada ciclo da Vigília (`:02/:32`). A execução
continua distribuída pelos ofícios já definidos no contrato da Trindade.

## Onde colocar cada coisa

- `ENTRADA.md`: ordem, texto, arquivo, link ou novidade para a Trindade.
- `COMENTARIOS_ROGERIO.md`: comentários atribuídos ao Rogério, sempre com fonte.
- `ANEXOS/`: arquivos referenciados pela entrada; nunca sobrescrever um anexo.
- `DECISOES_CLAUDE.md`: resultado da triagem e encaminhamento.
- `CHECKPOINT.md`: último ponto lido por Claude e saúde da ponte.

## Regra simples

1. Deposite o item com um ID único e `status: ABERTO`.
2. Se houver arquivo, salve-o em `ANEXOS/` e informe o caminho na entrada.
3. Claude lê as duas caixas no início do próximo ciclo.
4. Claude registra uma decisão e, quando necessário, abre ticket na fila de
   ZCode ou Grok.
5. O agente executor usa os livros de reserva antes de mexer em post ou imagem.

Não reescreva entradas antigas. Correção, resposta e mudança de estado nascem
como novo bloco referenciando o ID original.

## Limite conhecido da versão 1

A ponte recebe o que for depositado nela e sincroniza via GitHub. Ela ainda não
sabe de qual serviço vêm os comentários do Rogério. Assim que Miguel indicar a
origem (Google Docs, GitHub, e-mail, WhatsApp ou outra), será possível instalar
um coletor específico sem mudar este contrato.
