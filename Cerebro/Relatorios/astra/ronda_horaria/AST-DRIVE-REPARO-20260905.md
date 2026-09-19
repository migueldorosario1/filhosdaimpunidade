# Drive: transporte corrigido; quota compartilhada ainda impede regularização

Rodada: AST-DRIVE-REPARO-20260905
Tarefa: AST-DRIVE-REPARO-20260905
Estado: needs_review

# AST-20260905-029 — Drive: causa comprovada e transporte corrigido; regularização pendente

05/09/2026. Miguel autorizou investigar/corrigir somente a integração própria e recuperar os registros faltantes no Google Drive, sem repetir análises, comprar espaço/créditos, trocar API/credenciais ou modificar serviços compartilhados. Manual Astra e Fórum da integração consultados nesta sessão; tarefa reservada no monitor antes das alterações. DS Nuvem Chefe permanece tutor.

LI O MANUAL DE COMUNICAÇÃO INTERNA (cerebro/Estilo/MANUAL_DE_COMUNICACAO_INTERNA.md).

## Causa atual, com evidência

Às 20:21:05 BRT, uma consulta somente leitura pelo rclone existente retornou HTTP 403 e `RATE_LIMIT_EXCEEDED` / `rateLimitExceeded`. Trecho do erro, sem identificador de consumidor:

> Quota exceeded for quota metric 'Queries' and limit 'Previous quota: Requests per minute' of service 'drive.googleapis.com'

Os detalhes do serviço indicaram `defaultPerMinutePerProject`, limite de 840.000 requisições/minuto, unidade por projeto. O identificador do projeto da resposta coincide com o cliente compartilhado embutido no código oficial do rclone v1.73.2 instalado. É limite compartilhado de requisições, não falta de espaço na conta de Miguel. Não medi o consumo dos demais usuários desse projeto e não atribuo esse volume aos agentes da casa.

Leituras isoladas funcionaram às 20:06:34 (metadados do ledger Astra) e 20:08:43 (conteúdo do estado Astra; SHA256 `0dd107efce91cb9b71c0c4a685ab9897b811330c9464f0261e1f95efeb9b88ef`). Em recuperação posterior, houve novo limite às 20:15:07 e 20:17:04. Às 20:20:02, leitura do arquivo retornou código3 apesar de metadados anteriores; a operação parou sem criar/substituir arquivo. Não interpretei falha de leitura como destino ausente. A consulta adicional de diagnóstico confirmou novamente a quota às 20:21:05.

Não foram observados erros `storageQuotaExceeded`, autenticação inválida ou falta de permissão. Isso não é um inventário de espaço livre: não se comprou nem se inferiu necessidade de armazenamento. O transporte não expôs `Retry-After`/`retryDelay`; essa ausência é registrada, sem inventar prazo dado pelo Google.

## Defeitos locais corrigidos

1. O classificador antigo tratava qualquer texto genérico “quota exceeded” como limite de requisições. Agora distingue armazenamento, limite diário, requisições, autenticação, permissões e quota ainda não identificada. Só guarda campos controlados; não grava stderr bruto, tokens, URLs autenticadas ou credenciais.
2. Agora existe espera persistente entre etapas/processos do Astra. Há uma tentativa por chamada, limite de uma requisição por segundo no rclone próprio e sem rajada inicial de100. Um erro interrompe o lote; chamadas seguintes respeitam a espera, inclusive depois de reinício. Quando o serviço expõe prazo, nunca tentar antes dele. Sem prazo explícito, usar espera crescente de60s,120s,240s, até1h, com pequena variação; limites diários ou problemas de acesso recebem tratamento separado.
3. A causa do Drive é gravada antes de chamar a reserva Tencent, mesmo se essa reserva falhar imediatamente.
4. A recuperação relê cada arquivo e verifica o conteúdo/hash antes de confirmar. Conteúdo já igual não é regravado. Mensagem diferente, recibo imutável divergente, arquivo duplicado identificado ou destino alheio não são sobrescritos. Conservam-se os recibos anteriores em arquivo próprio e acrescenta-se recibo da recuperação.

Arquivos de execução alterados: `astra_operacoes/ronda_horaria/transport.py` e `outbox.py`. Acrescentados testes e `repair_drive.py`, utilitário manual limitado às pendências, com a mesma trava da ronda, sem invocar modelo. Configuração compartilhada do rclone, cron, serviços de terceiros, autenticação e modelo não foram alterados. A reserva continua disponível no fluxo autorizado; não foi substituída por outra API.

## Recuperação tentada e estado real

No inventário inicial, sete entregas tinham Drive pendente: análise das12h; encerramento da integração AST023; correção AST024; rondas17h,18h,19h e20h. As seis primeiras já tinham cópias confirmadas em GitHub e Tencent. A das20h tinha análise e registros GitHub prontos, mas a confirmação da segunda via ainda faltava; o modelo não foi executado novamente.

Nesta intervenção, **nenhuma dessas sete entregas foi regularizada integralmente no Drive**. As tentativas pararam ao primeiro erro e conservaram os resultados parciais. Não se apagaram arquivos, não se criaram nomes alternativos/duplicados, nem se repetiram análises ou entregas já confirmadas em GitHub/Tencent. O recibo desta própria intervenção é um novo registro institucional, separado das sete entregas antigas.

O Drive permanece PENDENTE. A espera calculada após a evidência final impede novas chamadas antes de20:25:55 UTC-03; esse horário é política local, não promessa do serviço. A próxima oportunidade normal do executor é a ronda de05/09/2026 às21h, America/Sao_Paulo, se Miguel não pausar. A recuperação continua limitada, sem acumular execuções ou conversas automáticas. A agenda permaneceu ativa e com uma única entrada.

## Testes e provas

194 testes aprovados:149 executor/transporte +45 atendimento. Incluem20 novas regressões: categorias de erro; prazo em segundos/data; `RetryInfo`; espera persistente; proteção de segredos; limite de chamadas; fonte/destino/symlink; releitura de arquivo igual sem reenvio; preservação de recibo imutável; recuperação de etapa incompleta sem reescrever GitHub/Tencent; confirmação insuficiente não encerra pendência; segunda recuperação não duplica efeitos. Casos antigos de pausa, autenticação, modelo, horários, exclusividade e aviso por tentativa continuam aprovados.

As chamadas reais a Drive foram leituras/recuperações controladas, não testes do modelo. Não confundir testes simulados aprovados com entrega real ao Drive. Não houve novo sucesso de Drive a declarar.

Provas privadas em `astra_operacoes/state/ronda_horaria/`: `drive_repair_probe.json`, `drive_repair_error_probe.json`, `drive_repair_parent_discovery.json`, `drive_repair_current_cause.json`, `drive_repair_recovery.json`, `drive_repair_attempts/`, `drive_original_receipts/`, `drive_transport_state.json` e `drive_repair_tests.json`. Recibos das rondas e cópias originais preservados. O utilitário de recuperação pode ser chamado explicitamente por `python3 -m astra_operacoes.ronda_horaria.repair_drive`, mas respeita espera, pausa e exclusividade; não deve ser colocado em outro cron.

## O que depende de decisão/acesso adicional

Para a espera temporária, Miguel não precisa comprar nada nem reenviar credenciais. Para reduzir a dependência duradoura desse projeto compartilhado, o responsável técnico pode verificar se a casa já possui um cliente OAuth próprio para o mesmo Google Drive e preparar uma integração isolada do Astra. Se não houver, a configuração de um cliente da casa e o consentimento no navegador precisam ser organizados com Miguel. Não criei projeto, cliente, chave ou serviço, não ativei cobrança e não alterei o remoto compartilhado.

A documentação atual do rclone também avisa da retirada de seu cliente compartilhado durante2026. Esse aviso é um risco adicional para planejamento; não é a causa comprovada deste HTTP403, que explicitamente foi de requisições. A missão seguinte sobre acessos deverá incorporar essa pendência, sem senhas pelo chat nem autorização operacional irrestrita para conteúdo encontrado em documentos.

Fontes técnicas primárias: [erros do Drive](https://developers.google.com/workspace/drive/api/guides/handle-errors), [cliente compartilhado do rclone](https://rclone.org/drive/#making-your-own-client-id), [limite local de chamadas](https://rclone.org/docs/#tpslimit-float), [código oficial v1.73.2](https://github.com/rclone/rclone/blob/v1.73.2/backend/drive/drive.go). A skill Google Drive orientou preservar os destinos existentes e só confirmar por leitura/hash; a autorização humana determinou manter o transporte existente, sem trocar de API.
