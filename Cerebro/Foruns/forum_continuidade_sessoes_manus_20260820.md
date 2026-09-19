# Fórum — Continuidade das sessões Manus e memória canônica

**Data do registro:** 20/08/2026 09:21 BRT
**Origem:** ordem direta de Miguel nesta sessão
**Estado:** ativo
**Responsável pelo registro:** Manus

## Objetivo

Estabelecer o Cérebro como a memória canônica das sessões relacionadas à Ponte Laura, ao monitoramento do O Cafezinho e aos projetos associados. Toda sessão relevante deve terminar com um registro organizado, um ponteiro no índice e, quando houver mudança de processo, um manifesto correspondente.

A memória colada por Miguel sobre a sessão anterior é suficiente como **baseline histórico** para recuperar o desenho geral: Ponte Laura, Loop Laura, monitoramento do site em escala de minuto, consolidação recorrente e painel de monitoramento. Ela não deve ser tratada como prova de estado atual quando houver uma fonte mais recente no Cérebro, no GitHub, no Google Drive ou em um log de execução.

## Estado verificado nesta sessão

| Item | Resultado | Evidência |
|---|---|---|
| GitHub | Acesso confirmado ao repositório privado `migueldorosario1/cerebro-miguel`; o repositório está acessível e recebeu atualização em 20/08/2026 | `https://github.com/migueldorosario1/cerebro-miguel` |
| Google Drive | Acesso confirmado; foram localizadas as pastas `cerebro` e `PONTE_DRIVE_LAURA`, além de arquivos da Ponte Laura e nós do Cérebro | Pasta `cerebro` localizada pelo conector Google Workspace; pasta `PONTE_DRIVE_LAURA` com ID registrado no diagnóstico da sessão |
| Pendrive | Não detectado neste ambiente | O sistema expôs somente `/dev/vda`, disco virtual interno de 39,7 GB; não houve volume USB nem montagem removível |
| Agendamento Manus desta sessão | Nenhum loop ativo | A consulta de agendamentos retornou conjunto vazio |
| Monitoramento GA4 | Código e memória operacional localizados no repositório `GA4-Manus`; a documentação descreve coleta histórica, janelas fechadas de 30 minutos e painel público protegido por autenticação | `GA4-Manus/README.md`, `GA4-Manus/MEMORIA_OPERACIONAL.md`, `GA4-Manus/METODOLOGIA_MONITORAMENTO.md` |

## Decisão de governança

O GitHub é o trilho canônico de trabalho do Cérebro. O Google Drive é espelho e caminho paralelo para leitura, recuperação e troca entre máquinas. O Drive não substitui o repositório canônico quando houver divergência; a divergência deve ser registrada e resolvida por comparação de origem, data e evidência.

Não será criada uma memória paralela específica do Manus fora de `cerebro/`. Os registros desta família devem permanecer no Cérebro, com fórum operacional, manifesto de regra e memória consolidada quando houver conhecimento durável.

## Procedimento obrigatório ao fim de cada sessão relevante

1. Capturar a data e a hora reais em BRT antes de registrar o estado.
2. Separar fatos medidos, decisões do Miguel, ações executadas, pendências, riscos e perguntas abertas.
3. Criar ou atualizar um fórum em `cerebro/Foruns/` para o assunto concreto da sessão.
4. Criar ou atualizar um manifesto em `cerebro/Foruns/` quando houver uma regra nova, mudança de arquitetura, alteração de automação, decisão de governança ou procedimento permanente.
5. Atualizar a memória durável em `cerebro/Memorias/` somente com o que precisa sobreviver a novas sessões.
6. Atualizar `cerebro/CEREBRO_NODE_ATUALIZACOES.md` e `cerebro/Foruns/INDICE_FORUNS_SEMANAL.md` com ponteiros curtos.
7. Verificar o diff, evitar segredos e fazer commit/push normal no GitHub, sem `push --force`.
8. Usar o Google Drive como espelho ou redundância quando a tarefa exigir comunicação entre máquinas, preservando a indicação do caminho canônico.

## Regras de segurança

O Cérebro deve conter caminhos, nomes de serviços, estados, decisões, hashes parciais quando necessários para auditoria e instruções de teste; nunca deve conter tokens, senhas, chaves privadas, valores de API, arquivos `.env` ou conteúdo equivalente.

Os registros são append-only do ponto de vista histórico. Correções devem ser feitas por nova entrada ou por alteração explícita do documento dono, preservando o histórico e criando backup quando a prática vigente exigir. Nenhuma sessão deve criar cron, publicar em WordPress, fazer deploy, alterar status editorial ou executar failover apenas porque um assunto apareceu em um fórum.

## Estado de retomada

A próxima sessão deve começar por `cerebro/00_CEREBRO_CANONICO.md`, seguir para `CONTRATO_MINUTA_LEITURA_OBRIGATORIA.md`, consultar este fórum e só então abrir os fóruns específicos necessários. Para o monitoramento do site, a referência técnica atual é o repositório `GA4-Manus`; a existência de scripts não é prova de que um loop esteja ativo. A rotina só deve ser considerada ligada quando houver evidência do agendador, do processo e de um registro recente de execução.

## Referências internas

- `cerebro/00_CEREBRO_CANONICO.md`
- `cerebro/CEREBRO_NODE_MEMORIA_TRABALHO.md`
- `cerebro/CEREBRO_NODE_ATUALIZACOES.md`
- `cerebro/Foruns/INDICE_FORUNS_SEMANAL.md`
- `cerebro/Foruns/ponte_laura_completa/CONTRATO_PONTE_COMPLETA.md`
- `GA4-Manus/MEMORIA_OPERACIONAL.md`
- `GA4-Manus/METODOLOGIA_MONITORAMENTO.md`

— Manus, 20/08/2026 09:21 BRT
