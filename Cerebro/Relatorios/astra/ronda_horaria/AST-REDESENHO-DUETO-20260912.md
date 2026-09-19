# AST-REDESENHO-DUETO-20260912

Implantação da ordem direta de Miguel em 12/09/2026. Corte deste relatório: 2026-09-12T19:16:27.815234-03:00.

## Resultado

Agenda nova instalada, relida e serviço cron ativo. Luna gpt-5.6-luna desperta em 00/30 de cada hora (48 oportunidades/dia). Astra gpt-6-astra desperta no minuto 05 das horas pares (12 oportunidades/dia), mas sai sem chamar modelo nem consultar WordPress quando não há handoff Luna válido. Minuto 05 evita disputa com a triagem do minuto zero. Doze despertares são mais que os nove antigos; o ganho de custo depende do filtro antes da inferência, não de chamar isso de redução de frequência.

As duas entradas editoriais antigas (Loop Miguel 17/47 e ronda Astra de nove horários) foram substituídas por duas entradas do dueto: uma Luna, uma Astra. Os demais jobs foram preservados. Configuração do runner antigo disabled; o atendimento e os controles de pausa permanecem. A entrada pessoal run_loop_codex_miguel.sh encaminha ao scheduler Luna, sem abrir outro executor nem chamar modelo fora do slot. Não há terceira rotina editorial cara em paralelo.

## Execução e integridade

Wrapper: astra_operacoes/dueto/run_scheduled.sh. Implementação scheduled.py, config scheduled.json. O pai mantém as travas Loop/runner durante a vida do processo Codex. Cada worker recebe identidade própria ROLE-AUTO-data-hora; despacho, titular anterior, modelo, autoridade e aceite do handoff são registrados. Não é reuso de identidade interativa ou ACK por colega. Rondas manuais bridge.py continuam compatíveis.

Luna registra pendências na fila existente; finish e handoff dos complexos são gravados na mesma transação, sem janela que possa perder a escalada. Astra trabalha só nos IDs encaminhados e pode concluir uma ronda com IDs explicitamente pendentes. Esses IDs continuam no bloco duet_scheduled do mesmo state.json. Fingerprints e resultados ficam no mesmo bloco, para reconhecer versões inalteradas. Campos históricos não foram removidos e nenhuma fila paralela foi criada.

Pausa manual, handoff, silêncio e travas são gates antes do modelo. Oportunidade recusada não vira compensação automática. Timeout/falha não fabrica finish: mantém owner/recibo incerto para reconciliação, impedindo repetir escrita de resultado desconhecido. Isso protege integridade, mas requer atendimento do alerta; não prometo autocura completa de qualquer falha.

## Publish e future

Prompt comum e prompts por papel autorizam auditoria/correções pontuais nos dois status. O coletor snapshot.py busca todos os future, publicados novos/modificados desde a última coleta concluída com sobreposição de cinco minutos, e IDs pendentes. Na primeira passagem usa três dias de publicados. Não filtra só autor 5470; conta compartilhada não prova origem. Não perder IDs fora da primeira página ou deduzir modelo pela data.

Future preserva post_date/post_date_gmt, status, autor, URL, taxonomia, imagem e gates. Verificação usa salvo e preview autenticado, sem exigir HTTP 200 público. Menos de três minutos para disparo impede escrita; transição normal para publish exige releitura, nunca reversão a future. Correção confirmada exige evidência privada, backup, reserva, hashes, readback, campos protegidos e preview/página conforme status. Autoria humana/incerta continua protegida sem ordem específica do dono.

Luna só aplica o básico inequívoco pela porta LUNA; Astra usa AST. Casos factuais complexos, imagem duvidosa, legenda ausente, sigla/nome raro e SEO warning são escalados com evidência. Títulos preservam clareza: 60 caracteres é referência, não gate mecânico (CM-20260912-009). Sem edição de mu-plugin por AST nesta implantação: ZM tem tarefa paralela expressa.

## Provas e limites do vivo

79 testes offline passaram: bridge anterior, novo scheduler, runner e integração dos controles/Telegram. Incluem exclusão real por flock em outro processo, vazio sem modelo, pausa/silêncio, não repetição de slot, falha sem finish, handoff atômico, preservação da fila, future sem mudança de status e exigência de preview/página. Bash e módulos Python passaram na conferência de sintaxe. O rollback em dry-run preservou todas as linhas do cron anterior (só a posição das entradas antigas muda).

Cron atual SHA-256 6faa9e024ce4a615382b18623629f8b10fa38e2a327425049a316271edeaf719; contagens: Luna=1, Astra=1, Loop antigo=0, Astra antigo=0. Fuso conferido America/Sao_Paulo. Evidência privada: /home/migueldorosario/Downloads/Antigravity Google/astra_operacoes/state/ronda_horaria/editorial/AST-REDESENHO-DUETO-20260912/validation.json e installation/receipt.json.

Primeira execução real iniciada explicitamente às 19:10:21 BRT: ASTRA-AUTO-20260912-191021, modelo gpt-6-astra, guardião PID 208793. Usa o handoff legado 90637328427c4ea5b6c4873f9f89ecb5 (269846/269969/269792/269996/269813), preservado sem conclusão fictícia. Snapshot WordPress autenticado obtido às 19:11:05 BRT; cinco publish. No corte das 19:15:39, owner vivo e execution.json=started: nenhuma conclusão ou correção desta ronda certificada por este relatório. A execução continua sob o pai independente desta sessão interativa.

PENDÊNCIA TÉCNICA COM ZM: o snapshot retornou cafezinho_revisores_editoriais=["AST"]. Isso não comprova porta LUNA ou edição future. Pedido inicial e evidência específica entregues em de_astra e Trindade. Até prova da porta própria, Luna audita e propõe, sem usar identidade AST nem remover proteção. Não afirmo que uma correção future tenha sido executada em produção. A primeira ronda Luna completa ainda não foi observada; ela aguarda conclusão AST + silêncio, pelo protocolo.

## Arquivos e rollback

Código e prompts em astra_operacoes/dueto/: scheduled.py, snapshot.py, install_schedule.py, scheduled.json, run_scheduled.sh, PROMPT_COMUM.md, PROMPT_LUNA_AUTO.md, PROMPT_ASTRA_AUTO.md, ADENDO_AUTOMATICO_20260912.md e test_scheduled.py. bridge.py ganhou finish+handoff atômico, compatível com a chamada antiga. control.py ganhou apresentação correta do dueto no status, mantendo as pausas. README antigo recebeu indicação de supersessão.

Backups privados em /home/migueldorosario/Downloads/Antigravity Google/astra_operacoes/state/ronda_horaria/editorial/AST-REDESENHO-DUETO-20260912/backup. Snapshot original do cron em installation/crontab.rollback. A cópia de control.py foi reconstruída pelo inverso exato do patch e conferida por sintaxe; não a apresento como backup anterior ao patch. Código novo pode permanecer desabilitado no rollback.

Rollback revisável: executar, do workspace, python3 /home/migueldorosario/Downloads/Antigravity Google/astra_operacoes/state/ronda_horaria/editorial/AST-REDESENHO-DUETO-20260912/rollback.py sem argumentos para mostrar proposta; --apply somente quando não houver guardião/owner pendente. O script preserva jobs alheios, desativa o novo scheduler, restaura as entradas antigas, configuração enabled anterior e wrapper anterior. Não restaura snapshots da fila, pausas ou coordenação e não apaga histórico. Não executei rollback no vivo, pois os testes/instalação passaram.

Mandato, retomada, fórum e memória receberam o adendo. Relatório/ponte/Trindade terão recibo de entrega separado; entrega não prova leitura/ACK. Novo worker automático entrega seu relatório por GitHub com recibo, sem repetir modelo caso o transporte falhe. Drive/NYC não certificados por esta implantação. Próximo passo: acompanhar o primeiro finish real, a primeira triagem Luna e a confirmação ZM da porta future/LUNA.

LI O MANUAL DE COMUNICAÇÃO INTERNA (cerebro/Estilo/MANUAL_DE_COMUNICACAO_INTERNA.md).

— Astra (AST) · gpt-6-astra · 20260912 19:16:27 BRT
