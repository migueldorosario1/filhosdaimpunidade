# Carta de handoff para outra sessão do Manus

**Data:** 20/08/2026
**Destinatário:** próxima sessão do Manus que assumir esta tarefa
**Remetente:** Manus, sessão de continuidade do projeto Ponte Laura
**Assunto:** como chegar ao Cérebro, atualizar o Cafedash e preparar o resumo por Telegram

## Leia primeiro

Você está assumindo uma tarefa que já foi organizada no Cérebro. Não trate o histórico implícito do chat como fonte de verdade. Comece pelo repositório privado do GitHub:

`https://github.com/migueldorosario1/cerebro-miguel`

Dentro dele, leia nesta ordem:

1. `cerebro/00_CEREBRO_CANONICO.md`
2. `cerebro/CONTRATO_MINUTA_LEITURA_OBRIGATORIA.md`
3. `cerebro/CEREBRO_NODE_MEMORIA_TRABALHO.md`
4. `cerebro/Foruns/forum_continuidade_sessoes_manus_20260820.md`
5. `cerebro/Memorias/memoria_continuidade_sessoes_manus_20260820.md`
6. `cerebro/Foruns/forum_cafedash_atualizacao_telegram_20260820.md`
7. `cerebro/Memorias/memoria_cafedash_atualizacao_telegram_20260820.md`

A versão de referência desta carta foi registrada no commit `16927d17` do repositório `cerebro-miguel`. Antes de agir, confirme se existe commit mais recente e releia os arquivos correspondentes.

## Como chegar ao Google Drive

O Google Drive está habilitado para a sessão e contém um espelho do Cérebro. Procure a pasta chamada `cerebro` e, separadamente, a pasta `PONTE_DRIVE_LAURA`. A pasta `PONTE_DRIVE_LAURA` é o caminho paralelo da Ponte Laura, não o substituto do GitHub.

A pasta do Cérebro identificada na auditoria tem o ID `1a3wfIXl23JCTZbMMpNjG0w18veQmDEzg`. A pasta `PONTE_DRIVE_LAURA` tem o ID `1kmz3i9zsq5Clgi97sES0ZU9pmWjUkxNZ`. Confirme os nomes e os pais antes de usar qualquer arquivo, pois o Drive contém snapshots e cópias históricas.

O arquivo de entrada do Cérebro é `00_CEREBRO_CANONICO.md`. Na Ponte Laura, os arquivos de mensagem são disjuntos por lado. O lado Dell escreve em `de_dell.md` e o lado Laura escreve em `de_laura.md`. A comunicação deve ser append-only e não deve conter segredos.

## Credenciais necessárias, somente por nome e local seguro

Esta carta não contém tokens, senhas, chaves privadas ou JSON de contas. Você precisa localizar ou solicitar os seguintes itens por um gerenciador de segredos, por uma variável protegida do projeto ou por entrega física controlada. Nunca procure valores dentro do Cérebro, do GitHub, do Drive, desta carta ou do chat.

| Serviço | Nome necessário | Uso | Regra |
|---|---|---|---|
| GitHub | Sessão autenticada com acesso de leitura e escrita ao repositório privado `migueldorosario1/cerebro-miguel` | Ler e indexar o Cérebro | Confirmar conta e repositório. Nunca usar reescrita forçada da história |
| Google Drive | Autorização OAuth da conta que enxerga `cerebro` e `PONTE_DRIVE_LAURA` | Ler espelho e trocar arquivos entre máquinas | Não usar navegador anônimo para arquivos privados |
| Google Analytics 4 | `GA4_PROPERTY_ID` e credencial de conta de serviço em variável protegida ou secret store | Coletar minutos fechados do Realtime | A propriedade documentada é `374552425`. O JSON não entra no GitHub, no Drive ou no chat |
| Telegram | Token novo do bot escolhido para a Ponte e o identificador do chat do Miguel | Enviar resumo e link do painel | O token histórico deve ser considerado comprometido ou obsoleto. Não reutilizar |
| Cafedash | Acesso de edição ao projeto que serve `https://cafedash-kr88khia.manus.space` | Atualizar o painel e seus jobs | A URL responde, mas exige autenticação. O projeto de origem ainda precisa ser localizado |

Se uma credencial não estiver disponível, registre a ausência pelo nome, sem inventar valor e sem copiar valor de documento antigo. A sessão anterior encontrou referências históricas a variáveis Telegram com valores não vazios em documentos versionados. Isso é um alerta de segurança, não uma fonte autorizada de credenciais.

## Estado técnico que você está assumindo

O repositório `GA4-Manus` documenta a arquitetura de monitoramento. A coleta deve preservar minutos fechados do GA4 Realtime, fazer deduplicação pela chave UTC e consolidar uma janela completa de 30 minutos. Para não perder minutos da janela transitória do Realtime, a coleta histórica deve ocorrer a cada 15 minutos. O painel deve emitir um relatório a cada 30 minutos somente quando houver 30 pontos disponíveis.

Na auditoria de 20/08, o último minuto disponível no CSV local era `2026-08-19T17:00:00Z`, equivalente a 14:00 BRT de 19/08, com atraso aproximado de 19 horas. O painel respondia, porém exigia autenticação. Não havia agendamento ativo nesta tarefa do Manus. Portanto, não declare que o loop está ligado apenas porque a documentação registra uma ativação anterior.

## Roteiro seguro de retomada

Primeiro, registre a hora real em BRT e leia o Cérebro. Depois, confirme o estado do GitHub e do Google Drive em modo somente leitura. Em seguida, localize o projeto autenticado que serve o Cafedash. Não crie um projeto novo e não publique uma alteração antes de descobrir se o projeto original ainda existe.

Depois, valide a credencial GA4 sem imprimir o valor. Faça uma consulta Realtime mínima. Confirme que a propriedade correta responde, que o minuto em andamento não é incluído e que os minutos fechados são gravados em UTC. Gere uma janela real de 30 minutos e confira os quatro componentes documentados do painel: usuários ativos por minuto, visualizações por minuto, ranking de páginas e diversidade de páginas por minuto.

Em seguida, verifique a atualização do painel. A prova mínima é formada por uma execução recente do coletor, um log recente do job, uma nova janela no histórico e uma página ou API do Cafedash refletindo essa janela. Se qualquer uma dessas provas faltar, registre o bloqueio no fórum e não anuncie que o painel está atualizado.

Para o Telegram, configure primeiro o bot por uma integração segura. Confirme o chat de destino sem expor o token. Faça um teste controlado com um texto mínimo ou, se o ambiente exigir aprovação separada, deixe o envio preparado e peça confirmação ao Miguel. Só depois envie o resumo completo com período BRT, média de usuários ativos, visualizações, pico, página de maior presença e link do Cafedash.

Não use um agendamento de sessão do Manus para uma verificação de 15 em 15 minutos. O monitoramento frequente deve rodar no próprio ambiente persistente do painel, com seu job interno e logs. A sessão do Manus deve ser usada para análise, correção orientada, auditoria e atualização do Cérebro, não para simular um daemon de minuto em minuto.

## Formato recomendado do Telegram

Quando o canal estiver validado, o resumo deve seguir este modelo, sem dados pessoais ou identificadores individuais:

```text
O Cafezinho — monitoramento GA4
Janela: DD/MM/AAAA HH:MM–HH:MM BRT
Média de usuários ativos: N
Visualizações: N
Pico: N às HH:MM
Página de maior presença: título
Painel: https://cafedash-kr88khia.manus.space
```

A mensagem deve indicar explicitamente quando a janela for incompleta, quando a média móvel ainda for uma prévia ou quando o painel estiver indisponível. Nunca enviar token, senha, identificador de conta de serviço ou caminho secreto.

## Como encerrar o trabalho

Ao terminar, crie ou atualize um fórum em `cerebro/Foruns/`, crie um manifesto se houver mudança permanente de arquitetura ou automação, atualize a memória em `cerebro/Memorias/`, atualize `cerebro/Foruns/INDICE_FORUNS_SEMANAL.md` e `cerebro/CEREBRO_NODE_ATUALIZACOES.md`, revise o diff e faça commit/push normal. Registre com clareza o que foi feito, o que foi apenas testado, o que ficou bloqueado e qual é o próximo passo.

Se o trabalho envolver Telegram ou credencial nova, escreva somente o nome do segredo, o local protegido e o resultado do teste. Nunca escreva o valor no Cérebro.

## Referências

- [Cérebro canônico](https://github.com/migueldorosario1/cerebro-miguel/blob/main/cerebro/00_CEREBRO_CANONICO.md)
- [Fórum de continuidade das sessões](https://github.com/migueldorosario1/cerebro-miguel/blob/main/cerebro/Foruns/forum_continuidade_sessoes_manus_20260820.md)
- [Auditoria do Cafedash e Telegram](https://github.com/migueldorosario1/cerebro-miguel/blob/main/cerebro/Foruns/forum_cafedash_atualizacao_telegram_20260820.md)
- [Repositório técnico do monitoramento GA4](https://github.com/migueldorosario1/GA4-Manus)
- [Cafedash](https://cafedash-kr88khia.manus.space)

— Manus, sessão de continuidade, 20/08/2026
