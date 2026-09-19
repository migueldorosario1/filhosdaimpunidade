# Memória canônica — origem do desvio `agente_controlado` e missão diária de faxina legacy

**Data:** 11/08/2026  
**Ordem:** Miguel do Rosário  
**Estado:** missão diária ativa

## Correção histórica fundamental

`agente_controlado.py` nunca foi o publicador canônico do Cafezinho. Ele era uma ferramenta controlada vinculada ao bot Zizilinda: recebia `briefing_execucao.json`, executava a redação solicitada e devolvia rascunho/auditoria ao fluxo do bot.

O fato de o arquivo conter uma função `publish_post()` e conseguir escrever no WordPress dentro desse fluxo supervisionado não o transforma no publicador oficial do sistema. Sua identidade declarada sempre foi “integrado com bot Zizilinda” e “acionado pelo bot”.

## Cronologia forense

### Até 08/04/2026 — ferramenta da Zizilinda já existia

Os snapshots nomeados `agente_controlado.py.bak*_20260408` declaram no cabeçalho:

- “Agente Controlado do O Cafezinho — V2 (integrado com bot Zizilinda)”;
- “sempre controlado — acionado pelo bot `bot_zizi_linda.py` via `briefing_execucao.json`”.

Os mtimes atuais foram alterados por migrações posteriores, portanto o sufixo de backup é evidência nominal, não timestamp forense independente. Mesmo assim, o conteúdo prova a finalidade original e não contém identidade V4.

### 31/05/2026 — promoção explícita dentro da Zizilinda

O backup `agente_controlado.py.bak_pre_promote_zizi_v2_teste_20260531_0516_codex` preserva o estado anterior à promoção Zizi v2. A cópia de 07/06 no legado passa a se chamar no próprio cabeçalho “Agente Zizi Linda v2 — backend editorial integrado ao bot Zizilinda”.

### 19/07/2026 — início do desvio V4

Na ativação real das verticais Geopolítica e Ciência, uma sessão Codex instalou `v4_vertical_draft_worker.py` usando o backend da Zizilinda como atalho de redação. A primeira cópia preservada do worker, criada em `19/07/2026 22:48:57 UTC`, já contém:

`AGENT = "/root/agente_controlado.py"`

e executa esse caminho por subprocesso. O docstring chamava a dependência de “redator real de produção”, apagando indevidamente sua identidade de ferramenta do bot.

O banco V4 confirma que o desvio já existia nos primeiros canários:

- Geopolítica: início `19/07/2026 22:21:18 UTC` (`19:21 BRT`), draft WP `262195`;
- Ciência: início `19/07/2026 22:23:51 UTC` (`19:23 BRT`), draft WP `262196`.

Os logs dos dois subprocessos começam com “AGENTE CONTROLADO V2 INICIADO (integrado com Zizilinda)”. O backup do crontab de `22:50 UTC` já mostra os dois workers horários.

O canal técnico atribui a ativação do worker real e desses canários à sessão Codex. Como não existe commit Git preservado para a criação, não há autoria de linha verificável por commit; há, porém, atribuição operacional forte nos registros da sessão.

### 26/07/2026 — o erro já havia sido percebido, mas não corrigido

O fórum `forum_kimi_webverify_e_brave_desativado_20260726.md` classificou corretamente:

- `v4_vertical_draft_worker.py` = produtor principal V4;
- `agente_controlado.py` = backend do bot, legado/paralelo.

Também registra que Miguel já havia corrigido um agente por confundir o controlado com o produtor principal. Apesar disso, a chamada executável permaneceu no worker até 09/08.

### 09/08/2026 — corte

O subprocesso foi substituído por `codigo.v4_vertical_redactor_runtime`. Em 10/08, as cópias e backups do backend Zizilinda foram colocados em quarentena legacy e surgiu o teste automatizado contra reintrodução.

## Conclusão causal

A “maldição” não começou quando a ferramenta da Zizilinda foi criada. Começou em 19/07/2026, quando o piloto V4 reutilizou essa ferramenta como atalho em vez de implementar um runtime de redação próprio.

Foi uma violação arquitetural de origem. Ela durou do primeiro canário real em 19/07 até o corte de 09/08, cerca de três semanas.

## Missão diária de faxina legacy

Toda rodada começa por `CEREBRO_NODE_ECOSSISTEMA_CANONICO.md`. A face visível e a infraestrutura que a sustenta formam uma única área protegida; ausência de exposição pública nunca basta para classificar um componente como legacy.

### Regra de elegibilidade e decisão humana

Um item só pode ser tratado como possível lixo depois de mais de 15 dias contínuos de inatividade comprovada. Com 15 dias ou menos, ele é recente e deve permanecer intacto, ainda que esteja pausado, sem cron ou aparentemente substituído.

Ultrapassar 15 dias não autoriza ação. O item vira apenas candidato, e qualquer retirada do ambiente quente, movimentação para legacy ou descarte exige consulta e autorização explícita de Miguel.

Tudo deve ser indexado antes de qualquer ação, inclusive o que vier a ser classificado como lixo. A indexação precisa cobrir cada arquivo, diretório e link, com caminho e metadados; segredos entram por existência e classificação, nunca por valor exposto.

Todos os dias, a missão deve executar uma rodada pequena e verificável nos ambientes acessíveis:

1. inventariar arquivos, serviços, crons, processos, imports, subprocessos, filas e espelhos;
2. classificar cada candidato como ativo canônico, dependência compartilhada, legacy, backup, cache ou desconhecido;
3. nunca declarar legacy apenas por nome, idade ou localização;
4. provar ausência de uso antes de mover: cron, systemd, processo, chamadas de código, banco/filas e documentação operacional;
5. gerar inventário integral e manifesto com caminho original, tamanho, datas, SHA-256, classificação, justificativa, destino B2 e forma de restauração;
6. compactar quando apropriado e copiar para o bucket correto;
7. verificar no B2 por hash quando disponível, ou por tamanho e contagem documentados;
8. somente depois da verificação e da autorização explícita de Miguel retirar a cópia quente, preferindo quarentena antes de exclusão definitiva;
9. validar novamente os sistemas ativos e o espaço em disco;
10. registrar a rodada no Cérebro, inclusive o que ficou pendente ou inacessível.

## Destinos

- Código, backups e artefatos de produção: `b2:failover-cafezinho1/faxina/<servidor>/<classe>/<aaaa-mm>/`.
- Memórias e histórico do Cérebro: bucket `Cerebro-Memorias`, com manifesto e ponteiro de restauração.
- Arquivo ainda necessário para rollback imediato: quarentena local/servidor por prazo declarado, nunca misturado à raiz operacional.

## Guardas

- Nada ativo é removido para “ganhar limpeza”.
- Falha de upload ou verificação deixa o original intacto.
- Host inacessível vira pendência, não “saneado”.
- Segredos, cofres e credenciais não entram em tar comum nem em manifesto público.
- A automação começa read-only/shadow e só ganha ação por classe após canário.
- Cada rodada deve ser pequena o bastante para permitir auditoria e rollback claros.
- Inatividade inferior ou igual a 15 dias impede a classificação como lixo.
- Mais de 15 dias torna o item elegível apenas para consulta; não constitui autorização automática.

## Rodada zero

O backend Zizilinda foi isolado em Nova York e no espelho local em 10/08. Tencent permaneceu pendente por recusa de SSH; é o primeiro alvo quando voltar a responder.

## Rodada diária 01 — 11/08/2026

Primeiro canário executado em Nova York: oito códigos explicitamente legacy, sem qualquer processo, cron, serviço, symlink, import ou chamada por caminho, foram empacotados com manifesto individual e hashes, enviados a `failover-cafezinho1/faxina/nyc/legacy-code/2026-08/rodada_20260811_01/`, lidos de volta para verificação e somente então retirados de `/root`.

O pacote B2 continuou íntegro após a retirada. V4 3/3 verde; Augusto e Mayra ativos. Relatório e manifesto: `Memorias/faxina_diaria_20260811/`.

## Rodada diária 02 — rio-ag — 11/08/2026

O repositório GSN antigo parecia inativo, mas seu último commit e a pausa operacional são de 07/08. Por decisão de Miguel, material tão recente não pode ser tratado como lixo; o lote permaneceu integralmente no lugar e não houve remoção, movimentação nem arquivo de código.

Foi produzida somente uma indexação não destrutiva de 13.502 entradas: 12.036 arquivos, 1.445 diretórios e 21 links. O índice e o resumo foram espelhados no B2 e verificados por SHA-256; o segredo rastreado em `.env.local` foi indexado apenas por caminho e classificação, sem valor e sem hash.

Evidências: `Memorias/faxina_diaria_20260811/RELATORIO_RODADA_RIO_AG_02.md` e `INVENTARIO_GSN_RIO_AG_20260811_02.jsonl.gz`.

## Rodada diária 03 — local — 11/08/2026

A árvore `Projeto Cafezinho Agentes/sites-tematicos_LEGADO_NAO_USAR` foi auditada sem alteração. O último arquivo é de 24/07, há mais de 15 dias, e não foram encontrados processos, descritores, crons, timers, serviços, links ou referências operacionais externas.

Foram indexadas 95.832 entradas, somando 3.543.345.181 bytes lógicos. O inventário foi espelhado no B2 e verificado por SHA-256; 274 caminhos potencialmente sensíveis foram registrados somente por metadados.

O lote não foi tratado como lixo e continua no local aguardando consulta. Um dos seis repositórios, `global_south_news`, possui alteração local não commitada, portanto eventual arquivo autorizado deve preservar a árvore integral e não pode depender apenas do GitHub.

Relatório: `Memorias/faxina_diaria_20260811/RELATORIO_RODADA_LOCAL_03.md`.

## Rodada diária 04 — Nova York — 11/08/2026

`/root/legacy/banco_midia_20260626` reúne 470.083.676 bytes de bancos órfãos e sidecars, sem alteração desde 29/06. Não há consumidor operacional, os cinco SQLite passam no `quick_check` e o banco canônico continua ativo em `/root/agent_data/banco_midia/banco_imagens_reais.db`.

Os cinco bancos coincidem por tamanho e SHA-256 com os membros do backup histórico já presente no B2. O lote exato foi integralmente indexado, mas continua em Nova York aguardando autorização explícita de Miguel; eventual retirada ganhará antes um snapshot novo com README e sidecars.

Relatório: `Memorias/faxina_diaria_20260811/RELATORIO_RODADA_NYC_04.md`.

## Execução autorizada 06 — Nova York — 11/08/2026

Miguel autorizou explicitamente a retirada de `/root/legacy/banco_midia_20260626`. Foi criado um snapshot exato de 89.634.424 bytes, enviado ao B2, verificado por SHA-256, restaurado integralmente em área temporária e comparado com a origem antes da retirada.

O lote original foi então removido do NYC. O banco canônico passou no `quick_check`, Augusto e Mayra permaneceram ativos, os três testes anti-legacy do V4 passaram e o snapshot B2 foi relido depois do corte com o mesmo SHA-256 `acb227ee0008a049e79f331908b35916ccebf5c9e83fe259f618f890fd76d9fd`.

Relatório: `Memorias/faxina_diaria_20260811/RELATORIO_EXECUCAO_NYC_06.md`.

## Execução autorizada 05 — local — 11/08/2026

Miguel autorizou explicitamente a retirada de `Projeto Cafezinho Agentes/sites-tematicos_LEGADO_NAO_USAR`. A árvore inteira, inclusive seis repositórios e a alteração local não commitada de `global_south_news`, foi compactada e criptografada antes do envio ao B2.

O pacote de 2.742.206.182 bytes foi restaurado integralmente e comparado sem diferenças. A origem voltou a coincidir com as 95.832 entradas do inventário imediatamente antes do corte; o objeto B2 foi relido por SHA-256 antes e depois da retirada, sempre com `00cdc4da3a7b0fda1f2f2d03abec47b478534425ca57042c762573afca2c7fc1`.

Os oito repositórios V4 permaneceram presentes, o registry manteve os oito sites ativos, o orquestrador compilou, seus crons continuaram ativos e todos os oito sites responderam HTTP 200. Relatório: `Memorias/faxina_diaria_20260811/RELATORIO_EXECUCAO_LOCAL_05.md`.

## Referências

- `Foruns/forum_missao_faxina_diaria_legacy_20260811.md`
- `Foruns/forum_plano_faxina_continua_droplets_20260807.md`
- `Foruns/backup_limpeza_20260724_143159/inbox_trindade/deepseek.md`
- `Foruns/backup_limpeza_20260724_143159/canal_trindade.md`
- `Foruns/forum_kimi_webverify_e_brave_desativado_20260726.md`
- `Memorias/memoria_arquitetura_v4_canonica_pos_cutover_20260810.md`
