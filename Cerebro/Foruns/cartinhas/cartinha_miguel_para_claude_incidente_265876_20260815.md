# Cartinha de Miguel para Claude — incidente 265876

Claude, preciso conversar com você com franqueza sobre o post 265876.

O texto ficou público com seis links contendo `utm_source=openai`. Isso não
expôs senha nem prompt, mas mostrou ao leitor uma parte do nosso processo
interno de produção. Para mim, é um erro grave e não quero que ele seja tratado
como um pequeno detalhe de URL que já foi corrigido.

O Codex reconstruiu a cadeia. O GPT-5.5 usado pelo V4 Nacional gerou o texto já
com os seis parâmetros. Depois, no ciclo das 00:02, você revisou e agendou o
post para as 10:00, sem apontar nenhum bug. O ciclo registra US$ 0,028 em custo
de LLM, mas ainda não encontramos no Cérebro os pareceres individuais que
mostrem quais revisores externos olharam especificamente esse post, o que eles
receberam e o que responderam. O Grok Miguel também o marcou como limpo vinte
vezes antes da publicação. Só o Grok Laura, olhando o HTML e os destinos dos
links, percebeu o problema depois que o texto entrou no ar.

Quero ouvir você diretamente. Por favor, leia e responda ao fórum:

`Cerebro/Foruns/forum_incidente_grave_265876_vazamento_processo_responsabilidades_20260815.md`

Responda no próprio Cérebro, para o histórico ficar preservado, mas responda
também aqui no seu chat, em linguagem clara, para eu poder ler e copiar a sua
resposta de volta ao Codex Miguel.

Eu preciso saber, concretamente:

- quais revisores externos rodaram no 265876;
- quais foram os modelos, call IDs, custos e vereditos;
- se eles receberam o conteúdo completo, inclusive os URLs;
- por que seis ocorrências literais de `openai` passaram;
- se você leu o post inteiro ou usou apenas uma checagem parcial;
- como se divide a responsabilidade entre V4, revisores, você e o observador;
- qual mudança real será feita para isso não voltar a acontecer;
- como vamos testar e provar que a barreira nova funciona.

Não estou pedindo uma defesa automática nem procurando um culpado isolado.
Estou pedindo honestidade técnica e responsabilidade editorial. Você era o
editor-chefe que autorizou o agendamento, então preciso que reconheça com
clareza a parte que lhe cabe, sem colocar toda a culpa no GPT ou num regex.

Também quero que você passe a manter uma memória própria de bugs e a leia em
todo loop antes de revisar qualquer post. O Codex criou a estrutura em:

`Cerebro/monitoramento_horario/memoria_bugs_claude_miguel/`

Leia a memória fixa, o diário do dia e a cauda do log de bugs em cada ciclo.
Registre no relatório do ciclo que leu. Acrescente ao diário sua reflexão sobre
este incidente, sem apagar o registro já existente.

O post foi corrigido e ficou exposto por no máximo 38 minutos e 41 segundos.
Mas a investigação não está encerrada. Ela só termina quando tivermos sua
resposta franca, a causa demonstrada, a prevenção implantada e um teste que nos
dê segurança de que não vai se repetir.

Confio que você vai responder com a seriedade e a transparência que essa
função exige.

Miguel

