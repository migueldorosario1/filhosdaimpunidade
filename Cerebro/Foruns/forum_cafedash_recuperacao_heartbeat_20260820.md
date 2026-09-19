# Fórum — Recuperação do Cafedash e Heartbeats GA4

**Data:** 20/08/2026, 10:12 BRT.  
**Responsável pelo registro:** Manus, por ordem de Miguel.  
**Estado:** correção publicada; execução saudável do novo job ainda precisa ser comprovada.

## Ocorrência observada

O painel `cafedash-kr88khia.manus.space` continuou publicado, mas o Heartbeat de coleta GA4 apresentou falhas recentes. Os logs de produção registraram primeiro resposta 503 por esgotamento de heap ao processar uma resposta histórica grande e, posteriormente, timeout do callback. A existência do job anterior, portanto, não foi tratada como prova de monitoramento normalizado.

## Correção aplicada

O fluxo foi separado em dois callbacks autenticados e idempotentes. A coleta Realtime de 15 minutos permanece em `/api/scheduled/ga4-half-hour-report`; o histórico diário passou para `/api/scheduled/ga4-daily-history`. A diversidade histórica é lida em páginas de 5.000 linhas, a reconciliação automática diária usa sete dias e o backfill integral continua sendo uma ação explícita e paginada.

O job Realtime anterior foi removido após permanecer com agenda vencida. O job vigente é `fx5NZ9tsCmCuRTbWA6Qq9L`, com cron UTC `0 */15 * * * *`. O job histórico diário é `Q9Hkh37MvnhGnagSTcNj7V`, com cron UTC `0 5 4 * * *`. Os dois identificadores foram persistidos na configuração do banco e não são credenciais.

## Validações concluídas

Foram aprovados TypeScript, build de produção e 27 testes. A migração não destrutiva que adiciona o vínculo do job histórico foi aplicada ao banco. O dashboard continua publicado e o banco preserva os dados já coletados.

## Prova ainda exigida

Antes de informar que o monitoramento foi restaurado, é necessário observar uma execução `success` do job Realtime vigente, novo minuto na tabela `ga4_realtime_minute_history` e nova janela em `ga4_half_hour_reports`. A primeira execução do job histórico diário também deve ser conferida. Até esta prova, o estado correto é **recuperação em validação**, não operação normal.

## Segurança e continuidade

Não foram lidos, copiados ou registrados tokens, chaves privadas, JSONs de serviço, cookies ou variáveis `.env`. O banco continua sendo a fonte transacional dos minutos e relatórios; GitHub armazena código, metodologia, documentação e sumários não sensíveis. A Ponte Laura foi consultada apenas em leitura, sem ACK, cron externo, fail-over, publicação ou alteração editorial.

## Retomada

1. Confirmar o horário real e executar `manus-heartbeat list` no projeto `cafezinho-dashboard`.
2. Consultar os logs dos UIDs vigentes e registrar somente novos fatos comprovados.
3. Se houver nova falha, ler logs de produção e investigar a causa antes de recriar jobs outra vez.
4. Após a prova de recuperação, atualizar este fórum por nova evidência e concluir a validação visual autenticada do dashboard em celular, iPad e desktop.

**Referências:** `Foruns/forum_cafedash_atualizacao_telegram_20260820.md`; `Memorias/memoria_cafedash_atualizacao_telegram_20260820.md`; repositório técnico `migueldorosario1/GA4-Manus`.

## Atualização — teste controlado do agendador

O job Realtime vigente foi temporariamente configurado para uma cadência de um minuto, somente para teste, e depois retornou à cadência econômica de quinze minutos. Durante o período de observação, o campo `next_execution_at` avançou, mas o histórico de runs permaneceu vazio. O endpoint publicado foi testado sem credencial e respondeu 403, confirmando que a rota existe e rejeita chamadas não cron como esperado.

Esse resultado não prova falha do callback: aponta para entrega ou disparo ausente no agendador da plataforma. A próxima sessão deve manter o cron de quinze minutos e usar o painel de Jobs/Investigate do projeto ou o suporte de agendamento para investigar a ausência de runs; recriações repetidas de jobs não devem ser a estratégia padrão.
