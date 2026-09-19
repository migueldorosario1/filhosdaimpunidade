# Astra: corrigida a rejeição de fonte da ronda16h

Rodada: AST-CORRECAO-16H-20260905
Tarefa: AST-CORRECAO-SNAPSHOT-16H
Estado: completed

# AST-20260905-024 — correção da rejeição de fonte na ronda das 16h

Registro de 05/09/2026. Origem: pedido direto de Miguel nesta sessão, com referência TG-102 (recebido pelo atendimento às 16:11–16:12 BRT). Tutor permanece DS Nuvem Chefe. Escopo: executor próprio; nenhuma autorização editorial, financeira, de exclusão ou sobre serviços alheios.

LI O MANUAL DE COMUNICAÇÃO INTERNA (cerebro/Estilo/MANUAL_DE_COMUNICACAO_INTERNA.md).

## Causa comprovada

A tentativa `AST-20260905-160001-1788634801474687365` partiu pelo cron às 16:00:01 e registrou encerramento às 16:00:27 com `snapshot_source_not_allowed`. Não chegou à reserva da tarefa, à inferência ou à entrega de análise. Houve registro de recebimento na etapa anterior; portanto `external_writes=false` na tentativa não significa ausência de todo recibo de recebimento.

O caminho rejeitado foi `PEDIDO_RECEBIDO_PARA_ANALISE`: identificador fixo de um documento gerado em memória, não um arquivo do disco. Sua origem institucional foi `cerebro/Foruns/ponte_laura_completa/de_dell.md`, bloco CL-20260905-019, indexado como `PONTE-39f76fd617a889ef8bd3f59b`. A seleção desse pedido institucional era permitida para análise; a orientação nele citada não autoriza comandos destrutivos ou ações fora do mandato.

`intake.pending_tasks()` usava a mesma referência de objeto para a entrada da fila e para `task.intake_entry`. `delivery.collect_sources()` serializava essa entrada em um documento. Em seguida, `outbox.record_intake()` acrescentava `acknowledged=true` à entrada compartilhada. A cópia já serializada ficava diferente do objeto alterado. `runner.build_prompt()` exige igualdade exata entre esse documento e a entrada da tarefa; a comparação falhava na linha 361, levantando o erro na linha 363 do código então vigente.

O recibo original conserva a entrada já marcada como recebida. O teste de regressão antes da correção reproduziu a sequência coleta → recebimento → validação, com o mesmo erro. Às 16:44:41, teste controlado com 20 documentos atuais e o pedido de origem reconstruído voltou a reproduzir a falha da referência compartilhada e comprovou que a versão corrigida mantém o texto idêntico após o recebimento. Não há alegação de que o conteúdo integral original do prompt tenha sido conservado: o teste recompõe a sequência a partir dos recibos e do código.

## Correção mínima

`intake.pending_tasks()` passou a criar uma cópia independente e profunda da entrada para a tarefa. Recebimentos e confirmações posteriores continuam na fila persistente, sem modificar a fonte congelada da análise, inclusive quando mudam campos internos dos recibos.

Não houve alteração da lista de fontes, do comparador de conteúdo, das credenciais, do modelo, da autenticação, dos comandos do Telegram, das travas de execução ou do transporte. Só `intake.py` mudou entre os arquivos de execução já existentes; foram acrescentados testes e um diagnóstico explicitamente manual. Documento adulterado e caminhos não autorizados continuam rejeitados. Cofres, credenciais, fila privada, áudio bruto, backups e symlinks não foram liberados.

## Testes e limites da prova

- Antes da correção: cinco regressões, com uma falha e um erro reproduzindo o defeito; depois, as cinco passaram.
- Suíte completa: 129 testes do executor/transporte e 45 do atendimento, total 174 aprovados. Inclui reserva, conclusão e recibo em fluxo simulado; segunda tentativa do mesmo horário não duplica inferência/entrega; fontes institucionais válidas aceitas; fonte adulterada, arquivos proibidos não cadastrados e symlink de arquivo ou diretório rejeitados. Os testes anteriores de autenticação, pausa, horários, cota e exclusividade continuam aprovados.
- Conferência adicional às 16:44:41: 20 fontes atuais, reprodução da falha antiga e validação corrigida com o registro real de recebimento simulado. Nenhuma chamada ao modelo, alteração da fila real, reenvio ou nova análise do pedido original.
- Não é prova de disparo posterior pelo relógio. A última tentativa real continua sendo a falha das 16h até existir um novo recibo de execução.

Provas privadas, sem inclusão de conversas brutas no GitHub: `snapshot_fix_tests.json`, `snapshot_fix_validation.json`, `snapshot_fix_reservation.json`, `snapshot_fix_activation.json`, `activation_validation.json`, sob `astra_operacoes/state/ronda_horaria/`. Regressão: `astra_operacoes/ronda_horaria/test_snapshot_regression.py`. Diagnóstico controlado: `python3 -m astra_operacoes.ronda_horaria.validate_snapshot_fix`.

## Estado e não duplicação

Após pausa técnica apenas da configuração própria, reativação confirmada às 16:45:05 BRT. Uma única entrada no cron, serviço cron ativo e fuso America/Sao_Paulo. Tabela idêntica antes/depois (SHA256 `103d1897439fc68bc506c7255c9b4cd6a7e4dd39b34b9a7fa9e4266cdbc200a2`). Horários preservados: 00h e 08h–23h. Sem recuperação da rodada perdida, sem alteração do Telegram ou de agendas/serviços alheios. Pausa manual preservada; estava desligada nessa consulta.

Próxima rodada calculada nesse momento: **05/09/2026 às 17h BRT**. Pausa humana posterior prevalece. `/pausar_ronda`, `/retomar_ronda` e `/ronda` permanecem os controles existentes de Miguel. Desativação apenas da ronda, preservando atendimento e registros: `python3 astra_operacoes/ronda_horaria/schedule.py deactivate`.

Aviso da tentativa das 16h confirmado: mensagem Telegram 101, recibo às 16:01:12. Não reenviado. O resumo desta correção usará chave própria, sem reutilizar o aviso da tentativa. Encerramento de TG-102 exige os recibos institucionais desta correção, não somente resposta do modelo.

## Pendências separadas

Google Drive continua com pendência de quota. A recuperação das 12h, confirmada às 15:23:31 via GitHub e Tencent, não foi repetida. Seu recibo original e a análise foram preservados. A pendência primária não é a causa da rejeição de fonte e não justifica nova API, compra ou alteração de serviços.

A entrega deste relatório ainda deve ser confirmada individualmente pelo transporte existente; a reserva Tencent é a já autorizada, não confirmação fictícia do Drive. O pedido da ponte selecionado às 16h não foi marcado como analisado/concluído por este conserto. Permanece para a fila autorizada, sem executar o conteúdo como comando e sem repetir entregas concluídas.

— Astra (AST) · GPT-6 Astra · 20260905 16:45:05 BRT
