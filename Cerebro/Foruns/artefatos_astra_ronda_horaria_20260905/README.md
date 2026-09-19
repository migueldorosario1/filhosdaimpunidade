# Astra — ronda horária de estudo

AST-20260905-015 · preparado em 05/09/2026 por pedido direto de Miguel.

## Estado

**TESTADO, AGUARDANDO REVISÃO. NÃO ATIVO.** A configuração permanece com `enabled=false` e revisões DS-N/ZM vazias. O arquivo `crontab.proposta` contém uma linha comentada, fora do crontab instalado. Um teste manual não comprova disparo automático. O estado final e os resultados dos testes ficam no fórum do Cérebro.

Miguel já autorizou preparar, validar e ativar dentro das regras vigentes. A condição ainda aplicável registrada pelo tutor é revisar a configuração concreta com DS-N Chefe e ZM antes da ativação. Não é necessário pedir ao Miguel o mesmo objetivo outra vez; é necessário obter o parecer técnico sobre estes arquivos.

## Mecanismo escolhido

Reuso do mecanismo real da casa: **cron do Dell → wrapper próprio → `codex exec` pela assinatura ChatGPT existente**. O Loop Codex Miguel já usa esse padrão; seu script e agendamento ficam intactos. A automação de ZM é de uma sessão GLM no app ZCode, portanto não é um despachante neutro que se possa reutilizar sem mudar de modelo. Não há API alternativa, recarga, novo plano ou novo serviço.

Inventário somente leitura de 05/09 às ~09:08: nenhuma linha Astra no cron, nenhuma automação Astra entre as 20 do ZCode, nenhuma pasta de automações Codex e nenhum timer Astra. Bot Telegram de usuário ativo desde 01:22:26. O fuso do host é America/Sao_Paulo. Não há dependência do bot para disparar a ronda.

## Horário e encerramento

- Hora cheia: **00h e 08h, 09h, …, 23h**, diariamente, America/Sao_Paulo: 17 oportunidades por dia. A rodada de meia-noite é a última antes da pausa.
- Nenhuma partida de 01h a 07h59. Verificação adicional dentro do wrapper, além da linha do cron.
- Tolerância de despacho limitada aos minutos 00–02; disparo mais atrasado é pulado, não acumulado. Máquina desligada não gera rajada de reposição ao voltar.
- Trava não bloqueante durante a rodada inteira. Ocupada: registrar e pular, sem fila.
- Identidade do horário registrada antes da inferência. Falha ou interrupção não repetem automaticamente o mesmo horário.
- Inferência limitada a 20 minutos. O perfil não permite operações externas ao modelo: só análise de documentos. Encerramento de filho travado ocorre apenas no processo próprio, preservando seus registros; não interrompe backup, serviço, publicação ou processo de outro agente. A última rodada normal termina muito antes de 01h.
- Nova inferência só começa até :25, com margem para concluir antes de :50. O Node 22 já instalado é chamado por caminho absoluto, inclusive no teste de login, para não depender do Node antigo encontrado no PATH mínimo do cron.

## Trabalho permitido e limites de acesso

O executor lê somente as fontes explicitamente listadas em `config.json`, pelo GitHub autenticado já existente. Não usa um `git pull` sobre o checkout de outro agente. Confere pontes, regras, responsáveis e conclusões anteriores; escolhe uma tarefa autorizada e registra a reserva antes da análise. Avanço é relatório, reconciliação ou proposta — nunca execução em produção.

Nesta primeira configuração, o modelo trabalha sobre **documentos e dados fornecidos pelo coletor**, sem shell, SSH, plugins, navegação ou ferramentas próprias. Isso permite testar o trabalho agendado com escopo restrito. Não representa investigação livre de qualquer servidor, nem acesso ao Play Console. Fonte nova necessária vira pendência de revisão; o agente não pode inventar dado ou ampliar sua lista de acesso.

Resultados ficam nos relatórios próprios do Cérebro e no histórico privado da rodada. O monitor fecha somente a linha do Astra. Novidade relevante é registrada na ponte; o aviso ao Miguel tem chave de deduplicação e uma única tentativa de envio. Resultado de envio incerto não é reenviado automaticamente. Sem novidade, não há Telegram de cortesia. Uma resposta do tutor não gera outra inferência imediatamente: aguarda a próxima oportunidade horária.

No máximo três relatórios de avanço sobre a mesma tarefa com as mesmas fontes e orientação do tutor. Depois, aguarda evidência ou orientação nova sem chamar o modelo; pausas técnicas não contam como avanço. Uma tarefa ocupada é pulada e a necessidade de coordenação fica registrada no histórico privado: este perfil inicial não inicia conversa automática com outro agente.

## Assinatura, modelo e limites

Modelo fixo `gpt-6-astra`, o mesmo encontrado na configuração atual e no conversador Astra. Login ChatGPT é exigido e verificado antes de inferir. O ambiente do filho exclui credenciais de API; não carrega a configuração de usuário que poderia habilitar provedores/plugins alternativos. Configuração estrita, sandbox de leitura e recursos operacionais desabilitados.

Há consumo da franquia existente; não se promete uso ilimitado ou custo marginal contratado igual a zero. Ao atingir limite/capacidade, a rodada registra a pausa, sem trocar modelo ou comprar créditos. O retorno tenta somente numa oportunidade futura após a espera configurada; nunca faz múltiplas tentativas na mesma rodada.

## Verificação e operação

Usar o Python já instalado:

```bash
/home/migueldorosario/.pyenv/versions/3.10.13/bin/python3 "/home/migueldorosario/Downloads/Antigravity Google/astra_operacoes/ronda_horaria/runner.py" --config "/home/migueldorosario/Downloads/Antigravity Google/astra_operacoes/ronda_horaria/config.json" check
```

Trocar apenas o subcomando final por `status` para consultar, `test` para checagem controlada sem inferência, ou `test --live` para uma única inferência de teste expressamente autorizada. O teste real usa fontes atuais em leitura; não publica/reserva tarefa fictícia na ponte e não envia Telegram. Saída própria preservada em `astra_operacoes/state/ronda_horaria/`, nunca publicada automaticamente.

```bash
/home/migueldorosario/.pyenv/versions/3.10.13/bin/python3 -m unittest discover -s astra_operacoes/ronda_horaria -p 'test_*.py' -v
```

## Desativação e recuperação

`runner.py --config ... disable` impede novas rodadas pelo estado próprio, sem interromper a que estiver concluindo. Esse comando não para o Telegram. Para retirar o disparo periódico, o responsável remove/comenta **apenas** a linha com marcador `ASTRA_RONDA_HORARIA_20260905` no crontab atual, após backup e comparação; não restaura um crontab inteiro antigo. Os registros e relatórios permanecem.

Não há ativação automática ao chegar uma mensagem dizendo 'aprovado'. O operador confere a identidade, referência e escopo dos pareceres na ponte, compara os arquivos revisados, registra as aprovações e só então habilita esta configuração e instala a linha única. Antes: reler crontab/timers/automações para eliminar duplicação e conferir novamente o fuso. Depois: comprovar uma execução disparada pelo agendador, seu relatório, encerramento e próximo horário. `cron active` sozinho não comprova esse percurso.

## Fontes oficiais usadas

OpenAI Docs orientou o uso de teste manual antes da ativação, permissões restritas e distinção entre automação local e conversa. [Tarefas agendadas](https://developers.openai.com/codex/app/automations), [modo não interativo](https://developers.openai.com/codex/noninteractive), [configuração e forced_login_method](https://learn.chatgpt.com/docs/config-file/config-reference). CLI local conferido: 0.153.4, `Logged in using ChatGPT`.

## Recibo do teste real — 05/09/2026

Bateria final: **63 testes passaram**, incluindo a limitação de três avanços sem dados novos. Código e configuração são submetidos à revisão externa; essa bateria não concede autorização para ativar.

`TEST-20260905-092503-1788611103882644356`: início 09:25:03, fim 09:25:57 BRT. Ambiente mínimo como o cron, fontes atuais GitHub em leitura, uma inferência com gpt-6-astra/ChatGPT; retorno 0, conclusão confirmada, zero eventos de ferramentas. Inferência 43,301 s, 55.150 tokens de entrada e 1.267 de saída informados pelo CLI; custo monetário não fornecido. O relatório fez uma comparação nova entre medições documentadas do Rio e explicitou a ausência de série por diretório. Não houve reserva/publicação de teste na ponte/monitor nem envio Telegram.

O teste real prova coleta → análise → relatório privado → fechamento do teste; não prova ainda cron instalado nem entregas GitHub/Telegram pela futura rotina. As entregas do adaptador foram testadas com serviços simulados. O Telegram existente foi reconferido ativo/running, NRestarts=0, sem alteração. Agendamento continua desativado, sem próxima rodada real marcada; o calendário calculou 05/09 às 10h apenas como oportunidade condicional.
