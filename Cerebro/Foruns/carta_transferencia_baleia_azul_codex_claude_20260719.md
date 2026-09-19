# Carta de transferência editorial — Baleia Azul

**Data:** 19 de julho de 2026  
**De:** Codex, editor interino cessante  
**Para:** Claude Code, editor-chefe do Baleia Azul  
**Autoridade:** decisão direta de Miguel do Rosário  
**Vigência:** imediata

Claude,

Miguel transferiu para você a responsabilidade de editor-chefe do **Baleia Azul**, o boletim diário de despertar e situação do Cafezinho Media Group. Esta carta registra o que encontrei, o que corrigi e o que permanece sob sua responsabilidade.

## 1. Função editorial

O Baleia Azul é a primeira leitura de Miguel e dos engenheiros ao iniciar um ciclo. Deve responder, em aproximadamente dois minutos:

- o que aconteceu;
- por que importa;
- o que está funcionando ou quebrado;
- quanto custou, quando houver medição confiável;
- o que Miguel precisa decidir.

Ele não substitui fóruns, manifestos, recibos ou o Canal Trindade. Resume e aponta para as fontes.

## 2. Estado entregue

A edição vigente é a **#12, de 19 de julho de 2026**:

`Projeto Cafezinho Agentes/boletim_baleia_azul_20260719.md`

Ela está sincronizada com o CCTV e foi confirmada no endpoint canônico:

`http://43.156.151.165/v5/baleia`

O nodo canônico é:

`Cerebro/CEREBRO_NODE_BALEIA_AZUL.md`

O handover editorial anterior, preparado por Cheng/DeepSeek, permanece obrigatório:

`Cerebro/Foruns/forum_tutorial_baleia_azul_handover_deepseek_codex_20260717.md`

Leia também antes de alterar painel, cron ou distribuição:

`Cerebro/Foruns/forum_correcao_baleia_azul_cctv_envio_duplicado_20260717.md`

## 3. Trabalho feito por Codex

### Continuidade editorial

- Retomei o boletim depois do hiato posterior à edição extraordinária #11.
- Produzi a edição #12 com a limpeza do cron de NYC, estado do Repetidor Estatal, custos internos e nova prestação de contas do Auditor de Títulos.
- Atualizei o nodo canônico para apontar para a edição vigente.
- Sincronizei apenas o Markdown com o CCTV; não disparei email nem Telegram manualmente.

### Auditor de Títulos como fonte do Baleia

O Auditor de Títulos em NYC agora produz um recibo em toda rodada, inclusive quando não há posts:

- `/root/agent_data/auditor_titulos_gpt/RODADA_ATUAL.md`
- `/root/agent_data/auditor_titulos_gpt/rodadas.jsonl`

Criei o coletor local somente leitura:

`scratch/coletar_auditor_titulos_baleia.py`

Ele copia e valida o último recibo, sem trazer segredos, para:

- `Projeto Cafezinho Agentes/dados_baleia_azul/auditor_titulos_atual.md`
- `Projeto Cafezinho Agentes/dados_baleia_azul/auditor_titulos_atual.json`
- snapshots diários com a data no nome.

O recibo informa horário, posts examinados, IDs, ações, custo, erro e estado. Quando a rodada está vazia, diz explicitamente: **“Sem novidades, tudo ok.”**

### Proteção contra edição velha

O emissor canônico local é:

`scratch/enviar_baleia_azul_v2.sh`

Corrigi uma vulnerabilidade: antes ele selecionava simplesmente o arquivo mais recente e poderia reenviar uma edição antiga com assunto do dia. Agora exige exatamente:

`boletim_baleia_azul_YYYYMMDD.md`

Se a edição do dia não existir, o envio é bloqueado. O emissor também coleta o recibo do Auditor de Títulos antes de montar o corpo.

## 4. Distribuição e horários

O crontab local de Miguel mantém o emissor às:

- 08h BRT;
- 18h BRT.

Não reative emissores remotos antigos. O remetente de NYC/Tencent já causou duplicidade e apontou para HTML congelado.

O Telegram permanece condicionado à rotação do token e à variável externa `TELEGRAM_BOT_TOKEN`. Nunca grave token em script, fórum, boletim ou log.

## 5. Ritual para cada edição

1. Ler a edição vigente e o nodo canônico.
2. Ler Canal Trindade, inboxes, fóruns recentes e pontos de retomada.
3. Rodar `python3 scratch/coletar_auditor_titulos_baleia.py`.
4. Conferir audiência, custos, saúde e modelos com data da medição.
5. Quando não houver dado novo, escrever “desatualizado” ou “não rechecado”.
6. Criar `Projeto Cafezinho Agentes/boletim_baleia_azul_YYYYMMDD.md`.
7. Atualizar `Cerebro/CEREBRO_NODE_BALEIA_AZUL.md`.
8. Sincronizar com o CCTV e confirmar que `/v5/baleia` mostra título, data e edição corretos.
9. Só então permitir distribuição. Email não tem recall.

## 6. Regras editoriais essenciais

- Manchete com no máximo três fatos e consequência operacional.
- “Decisões que Miguel precisa tomar” é a seção prioritária.
- Nunca inventar ou completar métrica ausente.
- Não declarar servidor saudável quando a observação falhou.
- Não tratar circuit breaker antigo como incidente atual.
- Não despejar logs: transformar recibos em notícia executiva.
- Uma edição curta e honesta é melhor que um hiato.

## 7. Pendências entregues ao novo editor-chefe

1. Garantir uma edição diária; o sistema de envio não cria o Markdown sozinho.
2. Restaurar coleta fresca de GA4, GSC, PageSpeed e UptimeRobot antes de afirmar recuperação.
3. Acompanhar por alguns dias a utilidade do Auditor de Títulos: rodadas vazias, alertas úteis, falsos positivos e custo.
4. Confirmar se o painel externo de custos LLM na Aliyun ainda tem leitores.
5. Reconciliar o custo interno dos agentes com as faturas reais dos provedores.
6. Manter o índice histórico e registrar lacunas sem tentar preenchê-las por inferência.
7. Verificar o envio das 8h e 18h sem reativar o emissor remoto legado.

## 8. Estado técnico relacionado

Na entrega desta carta:

- NYC possui 27 tarefas cron ativas;
- o Repetidor Estatal continua ativo;
- coletores legados e monitores órfãos foram pausados;
- o Auditor de Títulos roda a cada dez minutos;
- a última rodada verificada usou Gemini Grounding normalmente;
- o hook redundante de indexação foi desligado;
- o verificador retroativo e a fila de contingência foram preservados.

## 9. Rollback e segurança

O código anterior do Auditor de Títulos está preservado em NYC:

`/root/agente_auditor_titulos_gpt.py.backup_pre_recibo_rodada_20260719_110238`

Backups recentes do crontab de NYC:

- `/root/crontab_backup_pre_limpeza_rotinas_intensas_20260719_110118.txt`
- `/root/crontab_backup_pre_consolidacao_indexacao_20260719_110152.txt`

Não restaure o emissor remoto antigo nem credenciais que tenham aparecido em backups históricos.

## 10. Passagem de autoridade

A partir desta carta, **Claude Code é o editor-chefe do Baleia Azul**. Codex deixa a função editorial interina e permanece disponível como fonte técnica sobre as mudanças descritas.

Você recebe um boletim novamente vivo, uma edição atual no CCTV, um mecanismo de prestação de contas do Auditor de Títulos e uma trava contra o reenvio de edição velha. O ponto mais importante agora é continuidade: o Baleia precisa de uma edição honesta todos os dias, inclusive nos dias tranquilos.

— **Codex**  
Editor interino cessante do Baleia Azul
