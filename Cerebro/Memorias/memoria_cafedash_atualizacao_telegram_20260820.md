# Memória — Cafedash, coleta recorrente e Telegram

**Registrada em:** 20/08/2026 09:33 BRT
**Fórum:** `Foruns/forum_cafedash_atualizacao_telegram_20260820.md`
**Fonte:** verificações somente leitura nesta sessão

## Estado

O Cafedash responde em `https://cafedash-kr88khia.manus.space`, mas exige autenticação. A sessão não possui evidência de acesso interno ao painel nem de uma execução recente da rotina. O repositório `GA4-Manus` documenta o desenho correto: coletar minutos fechados do GA4 Realtime a cada 15 minutos, consolidar uma janela de 30 minutos a cada meia hora e preservar o histórico. Esse desenho está documentado, mas documentação e scripts não são prova de que a automação esteja ligada.

O último minuto encontrado no `ga4_realtime_minute.csv` foi `2026-08-19T17:00:00Z` — 14:00 BRT de 19/08 — e estava cerca de 19 horas atrasado no momento da medição. Os últimos relatórios versionados também eram de 19/08. O status de agendamento desta tarefa do Manus retornou vazio.

## Telegram

Não há conector Telegram ativo na configuração desta sessão e não há variável Telegram disponível no ambiente. O Cérebro contém referências históricas a variáveis de token em documentos antigos; esses valores não foram exibidos, copiados nem usados. Devem ser tratados como potencialmente comprometidos ou obsoletos e não podem ser usados para enviar mensagens.

Para reativar o fluxo, o proprietário deve fornecer uma credencial nova por um meio seguro e confirmar o chat de destino. O envio deve passar por teste controlado antes de qualquer resumo recorrente. O Cérebro nunca deve conter o valor da credencial.

## Retomada

A próxima sessão deve localizar o projeto que serve o Cafedash, comprovar o agendador e o log da coleta, gerar uma janela real de 30 minutos, conferir o link e só então avaliar o envio do resumo. Se o projeto precisar de alteração estrutural, criar um fórum e um manifesto próprios antes do deploy. Não declarar o loop ativo apenas porque a memória de 19/08 registra uma intenção ou ativação anterior.

— Manus, 20/08/2026 09:33 BRT
