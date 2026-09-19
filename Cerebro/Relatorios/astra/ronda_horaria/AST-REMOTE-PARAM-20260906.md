# AST-20260906-034 — remoto exclusivo parametrizado e leitura validada; cópias ainda pendentes

Rodada: AST-REMOTE-PARAM-20260906
Tarefa: AST-REMOTE-PARAM-20260906
Estado: completed

# Astra — remoto exclusivo do Google Drive

AST-20260906-034 · 06/09/2026, 20:55 BRT  
Tarefa: AST-REMOTE-PARAM-20260906. Estado: parametrização concluída; reconciliação das cópias continua pendente.

## Resultado comprovado

A configuração própria seleciona `drive_remote: gdrive-astra`. O transporte da ronda, da fila institucional e do reparo explícito lê essa opção. Campo ausente mantém `gdrive`; qualquer outro nome é recusado sem reproduzir o valor recebido. Destinos continuam restritos aos arquivos próprios do Astra. Não alterei remotos, cron, bot, serviços de colegas, modelo ou assinatura.

A infraestrutura informou projeto Google exclusivo `Astra-Drive-Sync`. Conferi localmente a existência de cliente próprio diferente do legado, credenciais presentes sem mostrar valores, mesma pasta raiz, escopo drive e ausência de unidade compartilhada. A identidade do projeto/cota no Console é relato AGY/ZM; não fiz nova auditoria no Console.

Leitura real pelo transporte corrigido, 20:53:29–20:53:52 BRT: quatro pastas institucionais esperadas e diretório de entregas encontrados. Arquivo `gdrive-astra:ponte_laura_completa/estado/astra.md`: 8.972 bytes, SHA256 `87331aa6ecea0ac6d2e8f69cc9b32c89e2fe6595d65513a0a0eada511ccfe59c`. Isso comprova leitura, não envio das cópias pendentes.

## Segurança e testes

253 testes offline aprovados: 208 da ronda (21 novos sobre remotos) e 45 do atendimento Telegram. Cobrem lista restrita, propagação a todos os caminhos do executor, recibos antigos, releitura no remoto novo, igualdade sem regravação, pausa, exclusividade e cooldown. Testes de escrita foram simulados. Zero uploads/reenvios reais e zero chamadas de análise nesta manutenção.

Uma trava compartilhada continua protegendo os dois transportes. O projeto novo mantém espera em `drive_transport_state_gdrive-astra.json`; o histórico legado fica em `drive_transport_state.json`, preservado byte a byte. Não existe fallback automático para furar espera. Remotos legados, cron e caixa de saída também tiveram hashes iguais antes/depois da leitura. Arquivo de pausa manual segue ausente, com padrão não pausado; não foi criado nem modificado.

Configuração de agenda conferida: uma entrada, 00h e 08h–23h, America/Sao_Paulo. A trava de manutenção desta sessão é temporária, não uma ronda ativa. Ao liberá-la, a próxima partida prevista é 06/09 às 21h, sem recuperar horários perdidos. O cron poderá fazer a recuperação limitada já existente; não foi disparado manualmente nesta tarefa.

## Pendências, fontes e reversão

Inventário às 20:53: 28 entregas da caixa de saída com Drive pendente, mais o preflight não confirmado e o recibo avulso AST023-REGISTROS-FINAIS: 30 itens por reconciliar. Recibos históricos e cópias GitHub/Tencent não foram alterados pelo teste. Nenhum item antigo foi declarado recuperado.

O avulso tem fonte imutável conferida: commit `1ff8b65861905cd8752adaa64dd8565a571659bf`, arquivo `cerebro/Relatorios/astra/ronda_horaria/AST023-REGISTROS-FINAIS.md`, 25.340 bytes, SHA256 `b83e68bb13eef92bbe1d61d08ade58d0c980f6df35ff40f02060ac441be79f6c`. Manifesto preparado em `drive_external_manifests/AST023-REGISTROS-FINAIS.json`, privado e sem envio automático. O reparador atual ainda não inclui esse avulso; não fabricar entrega antiga na fila.

Próximo passo coordenado com ZM: recuperar apenas cópias faltantes, sob trava/pausa/cooldown, ler conteúdo e conferir hash por arquivo. O reparador existente cobre caixa de saída e preflight; incluir o avulso exige passo específico conferido. Não repetir análise, GitHub ou Tencent.

Reversão simples, sob trava própria: mudar somente `drive_remote` para `gdrive` no config do Astra. O estado de espera antigo volta a valer. Backup privado anterior: `configuration_backups/remote_param_before_20260906.json`. Não restaurar cron nem configuração rclone de outros serviços.

Prova privada: `astra_operacoes/state/ronda_horaria/drive_remote_migration/validation_20260906.json`. Código: `transport.py`, `runner.py`, `outbox.py`, `repair_drive.py`, `test_drive_remote.py`, `config.json` e README do pacote próprio. Drive ainda não declarado regularizado.

— Astra · gpt-6-astra · 20260906 20:55 BRT
