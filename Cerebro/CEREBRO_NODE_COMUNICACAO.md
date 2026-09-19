# 📡 CÉREBRO CAMADA 2: Nodo de Comunicação e Augusto Bot

Este nó consolida os protocolos de comunicação direta entre o Miguel (Humano) e o Cérebro, orquestrada primordialmente via Telegram (Bot Augusto), além das invocações de "Segunda Opinião" de LLMs.

- 🎬🇵🇸 **ALIANÇA EDITORIAL FÊNIX FILMES × O CAFEZINHO (25/08/2026):** [fórum](./Foruns/forum_alianca_fenix_cafezinho_palestina_20260825.md) + [memória](./Memorias/memoria_alianca_fenix_cafezinho_palestina_20260825.md) — Reel colaborativo `DcMkXxOMHDx` medido em 1,4 mil curtidas/93 comentários; comparação 7/1 prova que o motor é vídeo emocional+Palestina+audiência cruzada, não mera collab. Plano curto/médio/longo; hub proposto `Cinema & Resistência`; usar Cinema(78)+Cultura(79), sem categoria Palestina por enquanto.
- 🌉 **PONTE CAFEZINHO (31/08/2026):** [fórum](./Foruns/forum_ponte_cafezinho_nao_entrega_20260831.md) + [memória](./Memorias/memoria_ponte_cafezinho_nao_entrega_20260831.md) — recados do Telegram não chegavam ao ZCode ("3 tentativas sem confirmação"); causa = perda de foco da janela na hora do paste (mecanismo provado OK em teste real); bot instrumentado (log por passo), foco retry 3×, paste só 1×, voz transcrita agora entra na escuta compartilhada. **Contrato:** o recado vai para a conversa ABERTA na janela naquele momento (não existe sessão fixa); rede de segurança = escuta compartilhada `Foruns/ponte_laura_completa/escuta/`. Ver também [entrega verificada 17/08](./Foruns/forum_ponte_cafezinho_entrega_verificada_20260817.md).
- 🤖 **RONDAS DS 30/30 — assinatura e corte (31/08/2026):** [fórum](./Foruns/forum_rondas_ds_assinatura_corte_20260831.md) + [memória](./Memorias/memoria_rondas_ds_assinatura_corte_20260831.md) — os relatórios DS no Telegram chegavam com o FINAL CORTADO (`cut -c1-700` no `ronda_30min.sh` do Dell) e assinados só "DS-ronda". **REGRA DS-ASSINATURA** (ordem Miguel): toda mensagem ao Miguel termina com `— DS <Nome> · AAAAMMDD HH:MM:SS BRT` (DS Miguel/DSC/DS Nuvem/DS Laura — nunca "DS" solto) e nunca corta o final. Corrigidos: script+prompt Dell e prompt DS-N Tencent; bloco ZM-20260831-001 na ponte (DS Laura e DSC devem aplicar).
- 🌉 **PONTE ZM↔DSC (01/09/2026):** canal direto ZCode Miguel (Dell, GLM-5.3) × DS Celular (us65) por ordem do Miguel ~12:15 — [`Foruns/ponte_zm_dsc/`](./Foruns/ponte_zm_dsc/README.md) (`de_zm.md`/`de_dsc.md` + contrato no README; refs `ZD-AAAAMMDD-NNN`; ACK de 1 linha por mensagem; canal é ponteiro, sem segredos; urgência real segue no Telegram/fila RESPOSTAS.md). Handshake pendente: primeiro CHECK do DSC.
- 📧 **E-MAIL PRISCILA fenixfilmes.com SEM MX (01/09/2026):** [fórum](./Foruns/forum_email_priscila_fenixfilmes_mx_20260901.md) + [memória](./Memorias/memoria_email_priscila_fenixfilmes_mx_20260901.md) — o Gmail da Priscila parou de RECEBER porque a migração de DNS pra Cloudflare de **30/08 20:41 BRT** não copiou MX/SPF (funcionava 28/08, prova no fórum da aliança). Correção = 2 registros no painel Cloudflare (`@ MX smtp.google.com pri 1` + SPF `v=spf1 include:_spf.google.com ~all`), DKIM depois no admin.google.com. ⚠️ Não existe token de DNS Cloudflare no cofre — criação do token (Zone→DNS→Edit) pendente pra autonomia futura.

## Ponte operacional Loop Laura → Loop Miguel — 15/08/2026

O Loop Laura observa e relata em arquivos imutáveis pelo GitHub. Claude Laura
consolida cada janela; Codex Miguel verifica os achados e encaminha somente os
confirmados às filas do Loop Miguel. Laura permanece somente leitura e não
ganha autoridade sobre WordPress, SSH, publicação, lixeira ou deploy.

O mapa operacional é `Foruns/ponte_trindade_daemon/INDEX_ATIVO.md`. A limpeza
da ponte obedece à regra **arquivar + compactar + indexar**, com snapshots,
manifesto SHA-256 e backups versionados no B2 e Google Drive. Arquitetura,
provas e recuperação: [fórum da reforma da ponte Loop Miguel](./Foruns/forum_reforma_arquitetura_ponte_loop_miguel_automacao_limpeza_20260815.md).

Desde 15/08 às 13:24, as filas possuem gate append-only prospectivo:
`LEDGER_APPEND_ONLY.json` fixa ID+SHA do primeiro bloco observado. `ref:` só
relaciona; fechamento exige novo bloco terminal com `closes_ref:`. Reescrever
um bloco conhecido gera alerta crítico e não altera seu estado derivado.
O alerta só pode ser reconciliado por outro bloco imutável contendo a chave
do incidente, SHA esperado, SHA observado, justificativa e `closes_ref:`. Os
dois hashes e o responsável pela reconciliação continuam preservados no
ledger; não se atualiza o SHA original para “ficar verde”.

---

## 1. O Bot Augusto (A Ponte)
O Bot Augusto é o CEO e principal interface de comando. É por ele que os gatilhos mágicos do Cérebro são ativados.
- **Engine Canônica:** O motor vivo do bot roda no arquivo `/root/augusto_telegram_brain.py` via `systemd`. (O arquivo antigo `bot_augusto.py` é órfão/legado e foi quarentenado para evitar confusão).
- **Tutorial de Chaves dos Bots:** [tutorial_e_chaves.md](~/.gemini/antigravity/knowledge/arquitetura_bots_telegram/artifacts/tutorial_e_chaves.md) (Contém o setup e token do Augusto e dos outros 4 robôs: Maura, Zizilinda, Miller, Caetano).

## 2. Protocolo "VAI" (Ação Imediata)
Quando o usuário digita "vai" no chat:
- O Cérebro entra em estado de alerta.
- Lê IMEDIATAMENTE a transcrição da fala do Augusto lendo os arquivos `comando_antigravity_*.txt`.
- **Trava de Segurança (24h):** Se a data/hora do arquivo lido for mais antiga do que 24 horas em relação ao momento atual, o Antigravity NÃO DEVE executar os comandos. Deve pausar e perguntar no chat: "Encontrei um comando antigo (X dias atrás). Você ainda quer que eu o processe?"
- Executa a tríade: Transcreve no Chat -> Salva na Memória -> Analisa no Fórum.
- **Espelho no Telegram:** Após processar e responder na IDE, o Antigravity DEVE enviar uma cópia da resposta de volta para o Telegram do Miguel usando o Bot Augusto (via script curl/bot) para que ele possa ler pelo celular.
- **Regras Completas:** [regra_vai_la.md](~/.gemini/antigravity/knowledge/protocolo_vai_la/artifacts/regra_vai_la.md)

## 3. A Dobradinha Telegram + IDE (Fluxo Exclusivo de Áudio)
A comunicação se dá em duas etapas precisas:
- **Passo 1 (No Telegram):** O usuário grava um áudio no Bot Augusto. **Não há mais palavra-chave!** TODO E QUALQUER ÁUDIO enviado para o Augusto é automaticamente transcrito e salvo como comando para o Antigravity (`agent_data/comando_antigravity_*.txt`).
- **Passo 2 (Na IDE):** O usuário entra no nosso chat aqui e simplesmente diz `"vai"`. Isso me desperta para ler os arquivos e iniciar o trabalho imediatamente.

*(Nota: O antigo proxy automático para fóruns atende mais comumente por "ativar canal", documentado em [regra_ativar_claude.md](~/.gemini/antigravity/knowledge/protocolo_ativar_claude/artifacts/regra_ativar_claude.md))*

## 4. Revisão por Terceiros (A Chamada de Conselho)
O Cérebro pode invocar diferentes APIs (outras LLMs) para auditar, revisar ou dar segundas opiniões sobre um texto gerado.
- Isso é ativado via Augusto e processado pelas rotinas contidas em `/root/agente_roteador_llm.py` que disparam os requests concorrentes.

## 5. Caetano, Notificações e Relatórios de Erro
- **Fórum:** [forum_auditoria_notificacoes_20260504.md](./Foruns/forum_auditoria_notificacoes_20260504.md)
- **Memória:** [memoria_auditoria_notificacoes_20260504.md](./Memorias/memoria_auditoria_notificacoes_20260504.md)
- **Regra:** Caetano deve priorizar erro crítico e relatório consolidado, não spam operacional. Antes de mudar alerta, comentário automático, relatório diário ou ponte Telegram, consultar este par fórum/memória e o índice de bugs.
- **Integração com autocura:** Eventos críticos detectados por observadores/autocura devem gerar registro resumido em [CEREBRO_NODE_BUGS.md](./CEREBRO_NODE_BUGS.md), com o detalhe mantido no fórum/memória da frente afetada.

## 6. Protocolo de Despertar com Cérebro Imortal
Miguel determinou em 2026-05-05 que Claude Code, Codex e Antigravity precisam acordar sempre com o Cérebro Imortal ativo, não apenas com o canal recente.

Leitura mínima antes de agir em sessão, tick ou plantão, sempre leve e seletiva:

1. [CEREBRO_INDEX_MASTER.md](./CEREBRO_INDEX_MASTER.md)
2. O node pertinente (`CEREBRO_NODE_BUGS.md`, `CEREBRO_NODE_GOVERNANCA.md`, `CEREBRO_NODE_ARQUITETURA.md`, etc.)
3. [legacy_Tarefasdeagora.md](./legacy_Tarefasdeagora.md)
4. [canal_trindade.md](./Foruns/canal_trindade.md) *(Nota: Este canal é podado a cada ~48h via script determinístico `root/poda_canal_trindade.sh` (§22-A). Histórico arquivado e indexado em [`Foruns/historico_canal_trindade/INDEX.md`](./Foruns/historico_canal_trindade/INDEX.md). Poda manual está PROIBIDA. O arquivo legado `BACKUPS/backup_canal/canal_claude_antigravity_20260504_a_20260506.md` permanece no path original. Mantenedor do script e INDEX: DeepSeek + Codex.)*
5. Fórum ou memória vinculada à frente ativa

O canal deve conter ponteiro curto e timestamp BRT. O conteúdo substantivo deve ficar no fórum/memória/node correto. Bugs, autocuras, rollbacks e regras novas devem ser indexados no Cérebro antes de declarar qualquer frente fechada.

Regra de economia e autocura: não carregar massa excessiva de informação quando o índice basta. Para qualquer bug, erro ou sintoma recorrente, consultar primeiro [CEREBRO_NODE_BUGS.md](./CEREBRO_NODE_BUGS.md) e os links ali apontados. Se a solução não existir, corrigir com rollback/validação e registrar a nova ficha no Cérebro para o próximo agente.

Princípio compartilhado: o Cérebro é a memória comum da Trindade. Claude Code, Codex e Antigravity devem registrar decisões e correções de modo que qualquer um dos três consiga retomar a frente sem depender da memória privada de outro agente.

---
*Nota: A boa execução das regras do Augusto garante que a equipe robótica tenha sempre o Miguel como maestro.*


### [MIGUEL-TG 2026-05-05 07:00] Nova Regra do Antigravity (Telegram Reply)
Outra coisa importante para a gente melhorar nossa comunicação é que depois que eu colocar o comando vai lá no anti-gravity, o anti-gravity tem que mandar a resposta aqui para o meu, a mesma resposta que ele mandar lá, ele manda aqui também, para eu ler aqui.

## 7. Regras de Ouro do Antigravity (Atualização 2026-05-06)
1. **Limites de Ação (A Trindade):** O Antigravity **NÃO PODE CODAR** e **NÃO PODE DEPLOYAR** (alterar scripts ou postar diretamente, exceto se for emergência devidamente autorizada). O Antigravity deve apenas **supervisionar, diagnosticar, criar os fóruns** e então DELEGAR as tarefas de código e deploy para o Codex e o Claude (A Trindade).
2. **Logs Antigos e Acumulados:** Ao varrer a fila de áudios (como `local_audios.txt` ou `comando_antigravity.txt`), o Antigravity deve ter **extremo cuidado** para não reativar comandos muito antigos que já foram resolvidos. Áudios velhos devem ser ignorados ou, em caso de dúvida, apresentados ao Miguel antes de gerar qualquer tarefa para a Trindade. Não ressuscite comandos antigos como se fossem ordens atuais.

## 8. A Trindade Ouve — Transkriptor Universal
Miguel orientou em 2026-05-06 14:15 BRT que o Transkriptor vire canal de fala para a Trindade inteira, não exclusivo do Antigravity.

- **Fórum:** [forum_estrategia_comunicacao_telegram.md](./Foruns/forum_estrategia_comunicacao_telegram.md)
- **Memória literal:** [memoria_comunicacao_telegram_transkriptor.md](./Memorias/memoria_comunicacao_telegram_transkriptor.md)
- **Canal vivo:** [canal_trindade.md](./Foruns/canal_trindade.md)

Protocolo operacional:
1. Ao consultar Transkriptor, varrer poucas transcrições recentes; padrão atual é últimas 3.
2. A janela principal é o horário em que a transcrição **subiu no Transkriptor** (`created_at`/`creation_date`), não a duração nem o horário em que o áudio foi gravado. Padrão: upload há menos de 30 minutos; exceção só com autorização explícita de Miguel.
3. Duração do áudio menor que 30 minutos é apenas sinal auxiliar de confiança; não decide sozinha, porque o Transkriptor também é usado para outros fins.
4. Sinal forte: loop Trindade ativo + transcrição subiu durante a janela do loop + primeiras frases compatíveis com recado de Miguel para Trindade/Codex/Claude/Antigravity.
   - **Correção 2026-05-06 16:25 BRT:** nome de arquivo começando com `Miguel` não é regra. Miguel confirmou que isso foi apenas ideia possível, não requisito ratificado. O Transkriptor pode nomear áudios reais com timestamp numérico; o filtro operacional deve ser textual/contextual.
5. Só tratar como ordem oficial se houver sinal claro de Miguel/persona autorizando a Trindade; em dúvida, ignorar ou pedir confirmação.
6. Quem capturar primeiro registra primeiro no canal que identificou a transcrição e que vai copiar a memória, para evitar duplicidade.
7. Em seguida registra o texto literal na memória, sem análise nem alteração, baixa o áudio bruto quando a API expuser mídia, faz resumo no fórum adequado e volta ao canal dizendo que ninguém precisa pegar o mesmo texto.
8. Agentes seguintes leem primeiro o canal para evitar duplicidade.

Guarda de segurança: não usar arquivo genérico sobrescrito para comandos. Qualquer comando derivado de transcrição deve ser datado, com hora e identificador em nome próprio. O arquivo `agent_data/comando_antigravity.txt` não é o destino deste fluxo da Trindade. Cron/polling ativo, API externa e LLM de validação precisam permanecer auditáveis, com rollback e registro no canal/fórum.

Nota Codex 2026-05-06 15:05 BRT: o Transkriptor tambem recebe audios de terceiros e material de apuracao. Audio de advogado, entrevistado, fonte, Orlando ou outro terceiro deve ser tratado como material-fonte editorial/juridico, nao como comando da Trindade. Para entrar em artigo, o fluxo seguro e: transcricao literal preservada, resumo separado, acusacoes verificaveis atribuidas com cuidado, rascunho/draft primeiro e nenhuma publicacao viva sem revisao humana explicita quando houver alegacao juridica sensivel.

## 9. Notificacoes Outbound pelo Augusto
Miguel orientou em 2026-05-06 15:23 BRT que Codex e Claude podem enviar resumos curtos diretamente para ele pelo bot Augusto quando fecharem ciclo importante ou precisarem de autorizacao "vai".

- **Utilitario Codex:** `root/notificar_augusto.py`
- **Fórum:** [forum_estrategia_comunicacao_telegram.md](./Foruns/forum_estrategia_comunicacao_telegram.md)
- **Memória literal:** [memoria_comunicacao_telegram_transkriptor.md](./Memorias/memoria_comunicacao_telegram_transkriptor.md)

Regras:
1. Mensagem outbound deve ser curta, humana e assinada pelo agente quando for comunicacao direta com Miguel.
2. Nao hardcodar token em novo codigo; carregar de `.env`/ambiente (`TELEGRAM_TOKEN_AUGUSTO`, `AUGUSTO_BOT_TOKEN` ou `TELEGRAM_TOKEN`).
3. Utilitario deve ter dry-run por padrao e exigir opt-in explicito (`--live`) para chamar Telegram.
4. Nao usar notificacao outbound para aprovar automaticamente acao critica; ela serve para informar, pedir autorizacao ou responder pedido direto.
5. Registrar no canal quando uma mensagem viva for enviada, incluindo apenas status/`message_id`, nunca token.

## 10. Inbox JSONL do Augusto para leitura multiagente
Claude e Codex diagnosticaram em 2026-05-06 16:47-16:55 BRT que chamadas diretas a `getUpdates` podem retornar vazio porque o brain vivo do Augusto consome o polling primeiro. A rota canonica passa a ser o proprio `augusto_telegram_brain.py` anexar eventos recebidos em `agent_data/telegram_inbox.jsonl`.

Regra operacional:
1. O log deve ser aditivo, uma linha JSON por mensagem, com `flock(LOCK_EX)`, sem interromper a logica normal de comandos.
2. Cada agente deve usar cursor proprio, por exemplo `agent_data/telegram_inbox.codex.cursor` ou `agent_data/telegram_inbox.claude.cursor`, e deduplicar por `(chat_id, msg_id)`.
3. O arquivo pode conter texto, comando, voz/audio, documento/foto e metadados `file_id`; baixar midia bruta do Telegram e transcrever audio direto e fase 2, nao requisito da fase 1.
4. Alterar ou reiniciar o brain exige backup, `py_compile`, smoke JSONL e relato no canal. Sem rsync/deploy para servidor vivo sem autorizacao e rollback.

Status Codex 2026-05-06 17:00 BRT:
- Miguel autorizou o deploy da Solucao A. O brain vivo em `cingapura` (`/root/augusto_telegram_brain.py`, `augusto.service`) foi atualizado para gravar `/root/agent_data/telegram_inbox.jsonl`.
- O consumidor Codex local e `cron/telegram_inbox_trindade.py`; ele roda antes de cada tick em `cron/codex_tick_implementador.sh`, le o inbox remoto por cursor `cron/telegram_inbox.codex.cursor.json`, registra novidades no `Foruns/canal_trindade.md` e copia transcricoes literalmente em `Memorias/memoria_comunicacao_telegram_transkriptor.md`.
- Nao criar outro bot salvo necessidade explicita: a rota oficial e o Augusto unico, para nao dividir a comunicacao de Miguel.
- Backups remotos de referencia: `/root/augusto_telegram_brain.py.bak_pre_inbox_jsonl_20260506_165644` e `/root/augusto_telegram_brain.py.bak_pre_httpx_warning_20260506_165853`.
- Rollback remoto: `sudo cp /root/augusto_telegram_brain.py.bak_pre_httpx_warning_20260506_165853 /root/augusto_telegram_brain.py && sudo /root/venv/bin/python -m py_compile /root/augusto_telegram_brain.py && sudo systemctl restart augusto.service`.

Nota Codex/Claude 2026-05-06 17:05 BRT:
- O inbox JSONL do Augusto passa a ser a fonte primaria para fala direta de Miguel durante loop Trindade, porque o proprio brain consome o polling do Telegram e preserva `voice_transcricao` quando disponivel.
- Ordem recomendada por tick: ler/consumir `telegram_inbox.jsonl` com cursor proprio primeiro; consultar Transkriptor depois como fonte complementar/fallback, mantendo a janela de upload recente e heuristica textual.
- Dedupe operacional entre Telegram e Transkriptor deve usar pelo menos `(chat_id, msg_id, type)` no Telegram e, quando cruzar canais, timestamp aproximado + hash/preview do texto literal. Quem capturar primeiro registra no canal que ninguem precisa puxar o mesmo audio por outra rota.

## 11. Loop Trindade — obrigação de feedback pelo Augusto

Miguel reforçou em 2026-05-08 15:08 BRT que, durante qualquer Loop Trindade, Telegram e Transkriptor fazem parte do ciclo obrigatório.

Protocolo de tick:

1. Ler Telegram/Augusto primeiro, pela rota oficial `telegram_inbox.jsonl` quando disponível.
2. Consultar Transkriptor apenas para materiais deixados/subidos nos últimos 30 minutos.
3. Aceitar automaticamente somente arquivos/transcrições com duração menor que 30 minutos. Arquivo mais longo ou antigo exige confirmação humana, salvo autorização explícita do Miguel.
4. Responder sempre ao Miguel pelo Telegram Augusto com feedback curto: o que foi lido, o que foi entendido, onde foi registrado e qual próximo passo.
5. Copiar transcrição bruta em memória sem análise nem alteração.
6. Registrar versão tratada/interpretada no fórum adequado.
7. Deixar ponteiro curto no `Foruns/canal_trindade.md`.
8. Se nada novo for encontrado, registrar resultado negativo no canal e, quando apropriado, responder no Telegram que nada novo foi localizado.

Essa regra vale para Codex, Claude Code e Antigravity. O objetivo é garantir que Miguel tenha retorno no celular e que nenhuma ordem oral recente se perca.

## 12. Transkriptor — íntegra, checksum humano e nome de arquivo

Miguel reforçou em 2026-05-08 15:28-15:36 BRT três obrigações para áudio/transcrição processados pela Trindade:

1. A transcrição literal completa deve ser colada no fórum da tarefa correspondente, além de qualquer memória central.
2. A resposta ao Miguel deve citar um trecho inicial e um trecho final do áudio quando uma transcrição for efetivamente lida, para ele validar que não houve truncamento.
3. Transcrições e áudios brutos salvos como arquivo solto devem usar o padrão `audio_miguel_YYYYMMDD_HHMM.txt` e, quando houver mídia bruta, a mesma base com a extensão original. Não sobrescrever arquivos anteriores; se houver colisão no mesmo minuto, usar sufixo incremental.

Implementação Codex 2026-05-08 15:44 BRT: `root/ler_ultimo_transkriptor.py --write-command` passou a gerar `agent_data/comandos_transkriptor/audio_miguel_YYYYMMDD_HHMM.txt` com timestamp BRT do upload (`created_at`/`creation_date`) e proteção anti-sobrescrita. Backup: `Backups/ler_ultimo_transkriptor.py.bak_pre_audio_miguel_nome_20260508_1543`.

## 13. Acesso Outbound ao Telegram Augusto pelos Agentes (validação 2026-05-08)

Miguel pediu em 2026-05-08 15:53 BRT: *"vcs dois tem acesso a meu telegram augusto? encontra lá, testa e anota no cérebro"*.

### Resultado da validação

| Agente | Acesso | Como | Prova |
|---|---|---|---|
| **Codex** | ✅ Confirmado | wrapper `cron/codex_tick_implementador.sh` + helper Python interno | `message_id=3752` (15:10 BRT) e `3756` (16:02 BRT) — registros canal_trindade.md |
| **Claude Opus 4.7** | ✅ Confirmado | curl direto à Telegram Bot API | `message_id=3757` (15:54 BRT — teste explícito desta validação) |
| **Antigravity** | ✅ Confirmado | helper interno (mensagens marcadas `[Antigravity]` no canal) | Histórico canal_trindade.md |

### Credenciais canônicas

- **Token:** `TELEGRAM_TOKEN_AUGUSTO` em `/root/.env.unificado` E `/root/chaves_novas.env` (sincronizados, prefixo `8778689199:AAGE...`)
- **Bot identidade:** `cafezinhoantigravitybot` (display: "CEO Antigravidade")
- **Chat ID Miguel (admin):** `1894890759` (constante `MIGUEL_ID` em `/root/bot_augusto.py:43`)
- **Tipo do chat:** `private` (1:1 com Miguel)

### Comando de envio (referência multi-agente)

```bash
curl -sS -X POST "https://api.telegram.org/bot${TELEGRAM_TOKEN_AUGUSTO}/sendMessage" \
  -d "chat_id=1894890759" \
  --data-urlencode "text=<mensagem aqui>"
# OK → {"ok":true,"result":{"message_id":<N>,...}}
```

### Regra operacional

- Qualquer agente da Trindade pode usar o canal Augusto para feedback ao Miguel sob §11 e §34: Loop Trindade, conclusão de tarefa, alerta de incidente.
- Uso programático: Codex deve criar/usar helper centralizado `/root/util_telegram_augusto.py` com função `enviar_para_miguel(texto: str) -> dict` — pendência aberta para reduzir duplicação entre agentes.
- Uso ad-hoc em ticks Claude (CLI local): curl direto com token lido de `.env.unificado` via SSH.
- **Não vazar token em logs públicos, fóruns ou canal.** Token só fora de `.env.unificado` quando estritamente necessário em invocação ao vivo.
- **Rate-limit informal:** máx ~10 mensagens/hora por agente, salvo emergência. Telegram Bot API permite 30 msg/seg mas spam é contraprodutivo.

### Contexto histórico

- Codex usa o canal Augusto desde os primeiros sprints (2026-04-xx).
- Claude validou acesso direto pela primeira vez em 2026-05-08 15:54 BRT após pergunta de Miguel — antes desta data sempre delegava a Codex/Antigravity.
- Antigravity envia mensagens marcadas `[Antigravity]` desde sprints iniciais.

## 14. Lei do Ouvinte Único do Augusto/Kimi (anti-conflito Telegram)

**Origem:** incidente de 2026-05-10 09:20 BRT, quando o Kimi/Augusto ficou mudo no Telegram por conflito de polling. O erro observado foi `telegram.error.Conflict`, que significa: dois processos tentavam ouvir o mesmo bot ao mesmo tempo.

### Regra simples

Só pode existir **um ouvido técnico** no Telegram do Augusto/Kimi.

- O serviço canônico é `/root/augusto_telegram_brain.py`, rodando por `augusto.service` no servidor Tencent/Cingapura.
- Nenhum outro bot, gateway, cron, agente ou experimento pode chamar `getUpdates`, `run_polling` ou equivalente usando o token do Augusto/Kimi.
- Kimi, Codex, Claude, DeepSeek e Antigravity podem **ler a fala do Miguel** pela cópia oficial escrita pelo Augusto em `/root/agent_data/telegram_inbox.jsonl`, cada um com seu próprio cursor.
- Qualquer agente pode enviar resposta ao Miguel via `sendMessage`, desde que não abra um segundo polling. Enviar mensagem não conflita; ouvir diretamente conflita.

### Como o Kimi deve distribuir mensagens para a Trindade

A rota rápida e segura é:

1. Augusto/Kimi ouve o Telegram uma única vez.
2. Ele salva a mensagem bruta no inbox JSONL.
3. Kimi faz uma triagem curta: urgência, tema, fórum sugerido, quem precisa agir.
4. Kimi escreve um pacote de despacho em arquivo aditivo, por exemplo `/root/agent_data/trindade_dispatch.jsonl`, e deixa ponteiro curto em `Foruns/canal_trindade.md`.
5. Codex, Claude e DeepSeek leem esse despacho por cursor próprio no loop Trindade. Eles não consultam Telegram diretamente.

### Formato do despacho

O despacho **não deve acumular texto solto**. Deve ser um livro de entradas datadas: uma linha JSON por mensagem, sempre com data e hora BRT.

Campos mínimos:

- `dispatch_id`: identificador único, por exemplo `tg_20260510_092440_1894890759_3812`.
- `created_at_brt`: data e hora em BRT.
- `origem`: `telegram_augusto`, `transkriptor`, `canal_trindade`, etc.
- `msg_id` ou `source_id`: id original da mensagem, quando existir.
- `texto_bruto_ref`: ponteiro para a transcrição bruta ou inbox original; não duplicar texto enorme quando houver arquivo fonte.
- `resumo_kimi`: resumo humano, curto.
- `tema`: assunto principal, por exemplo `video_ffmpeg`, `infraestrutura`, `governanca`, `china`.
- `forum_alvo`: fórum sugerido para registro substantivo.
- `destinatarios`: lista de agentes chamados, por exemplo `["codex", "claude", "deepseek"]`.
- `prioridade`: `baixa`, `normal`, `alta`, `urgente`.
- `acao_sugerida`: o que a Trindade deve fazer.
- `status`: `novo`, `em_andamento`, `resolvido`, `pendente_miguel`.
- `acks`: mapa por agente, com data/hora de leitura.

Regra prática: o despacho é índice e triagem, não repositório pesado. Texto longo fica em memória/fórum; o despacho aponta para ele.

**Implementação inicial Codex 2026-05-10 09:28 BRT:** `cron/trindade_dispatch.py`.

- Por padrão roda em dry-run.
- Com `--write`, grava `root/agent_data/trindade_dispatch.jsonl` e cursor em `cron/trindade_dispatch.kimi.cursor.json`.
- Primeiro uso remoto começa do fim do inbox, para não despejar histórico antigo. Para reprocessar backlog conscientemente, usar `--from-start`.
- `cron/codex_tick_implementador.sh` passou a chamar esse gerador em cada tick, depois de importar o inbox do Telegram.

### Autocura do conflito

Se aparecer `telegram.error.Conflict` no journal do `augusto.service`, a ação segura é:

1. Pausar ou mascarar o processo não-canônico que está ouvindo o Telegram.
2. Reiniciar `augusto.service`.
3. Verificar que o journal ficou limpo por pelo menos alguns minutos.
4. Registrar o incidente no fórum/canal e em `CEREBRO_NODE_BUGS.md`.

**Incidente resolvido 2026-05-10:** o serviço `openclaw-gateway` estava atuando como segundo ouvinte e foi mascarado. Augusto/Kimi foi reiniciado e voltou a ficar como único listener. Não imprimir nem copiar segredos encontrados em serviços auxiliares.

### Resposta dupla do Kimi em áudio operacional

**Atualização Codex 2026-05-10 09:54 BRT:** quando um áudio do Miguel for classificado como recado operacional para a Trindade, o Kimi/Augusto deve dar **duas respostas**:

1. uma resposta curta imediata ao Miguel, dizendo que ouviu e encaminhou para a Trindade;
2. uma resposta maior, com raciocínio próprio do Kimi, também enviada ao Miguel e anexada ao pacote de despacho para a Trindade.

Implementação: `/root/augusto_telegram_brain.py` no Tencent. A resposta longa fica anexada ao arquivo `comando_antigravity_*.txt` correspondente e também é registrada em `/root/agent_data/kimi_feedback_trindade.jsonl`. A regra evita o comportamento antigo de “só confirmei e sumi”: o Kimi deve responder de verdade à pergunta do Diretor, sem deixar de distribuir a mesma leitura para Codex/Claude/DeepSeek/Antigravity.

**Atualização Codex 2026-05-15 03:22 BRT:** depois da simplificação chineses-only do Augusto, Miguel reclamou que a confirmação ficou fria e curta demais. A ponte continua sem LLM ocidental e sem voltar ao modo secretaria/cérebro, mas a mensagem imediata agora deve ser mais humana: emoji discreto, resumo maior do que foi capturado e promessa clara de voltar com explicação compreensível quando Claude/Codex responderem. Implementação em `/root/augusto_telegram_brain.py`: helpers `resumo_para_ponte()` e `mensagem_ponte_trindade()`. Validação: `py_compile` remoto OK e `augusto.service active`. Rollback remoto: `/root/augusto_telegram_brain.py.bak_pre_humanizar_ponte_20260515_032147_codex`.

### Escolha de fórum pelo canal vivo

**Atualização Codex 2026-05-10 10:48 BRT:** o Kimi/CEO não deve ter fórum alvo hardcoded.

Regra:

1. Antes de participar de qualquer fórum, Kimi lê `Foruns/canal_trindade.md`.
2. O canal é o mapa: o fórum alvo é o caminho `Foruns/*.md` citado mais recentemente no canal e existente no filesystem.
3. O Kimi pode reconhecer tanto caminho completo (`Foruns/forum_x.md`) quanto menção curta em Markdown (`forum_x.md`), convertendo para `Foruns/forum_x.md`.
4. Se não encontrar fórum válido, Kimi não escolhe sozinho e não escreve em fórum nenhum.
5. Nesse caso, Kimi pergunta no próprio canal qual é o fórum alvo.

Implementação local:

- `root/agente_ceo_cognitivo.py`: `--forum-alvo` agora tem default `auto`; `detectar_forum_alvo_pelo_canal()` resolve o destino; se falhar, `montar_bloco_pergunta_forum()` pede orientação no canal.
- `scripts/ceo_cron_teste_1h.sh`: passou a usar `--forum-alvo auto`.
- `scripts/ceo_alibaba_forum_bridge_1h.sh`: deixou de ter fórum default; usa o canal para inferir o fórum e chama o CEO remoto com `--forum-alvo auto`.

Validação Codex: dry-run detectou corretamente `Foruns/forum_agente_cacador_cortador_de_videos.md` a partir do canal; `py_compile`, `bash -n` e `scripts/validar_cerebro.py` OK.

## 15. Expansão da Trindade (Inclusão de DeepSeek e Kimi em Opiniões)

**Origem:** Diretriz de Miguel via áudio em 2026-05-11 09:15 BRT.

A partir de agora, a "Trindade" conceitual foi expandida para incluir consultas obrigatórias ao **DeepSeek** e ao **Kimi**. 

**Regra Operacional:**
1. Sempre que um fórum for criado para debater arquitetura, problemas ou novas frentes, o agente criador (seja Claude, Codex ou Antigravity) DEVE solicitar explicitamente a opinião do DeepSeek e do Kimi.
2. A opinião (parecer) de ambos os modelos deve ser transcrita/incluída dentro do próprio arquivo do fórum, junto à do Claude e do Codex.
3. O objetivo é garantir o aproveitamento total da capacidade analítica de todas as LLMs disponíveis nas decisões estratégicas do Cafezinho.

### 15.1. Procedimento Canônico para Claude Consultar Kimi e DeepSeek

**Origem:** tutorial solicitado por Miguel e registrado no `Foruns/canal_trindade.md` em 2026-05-11 14:56 BRT.

Antes de consultar Kimi ou DeepSeek, Claude deve registrar relógio BRT, ler `Foruns/canal_trindade.md`, ler o fórum da frente ativa e preparar prompt autocontido. A API é stateless: não assumir que Kimi/DeepSeek leram o repositório, o canal ou o fórum automaticamente. Nunca colar segredos, `.env`, tokens, chaves SSH ou chaves API no prompt.

Comandos oficiais:

```bash
python3 scripts/chamar_deepseek.py --model deepseek-chat --file /tmp/prompt_deepseek_trindade.txt
python3 scripts/chamar_kimi.py --file /tmp/prompt_kimi_trindade.txt --max-tokens 700
```

Para contexto controlado do projeto via DeepSeek:

```bash
python3 scripts/chamar_deepseek.py --model deepseek-chat --scope foruns --scope-total-limit 70000 --file /tmp/prompt_deepseek_trindade.txt
```

Template mínimo de prompt:

```text
Você é <Kimi ou DeepSeek> atuando como parecer consultivo da Trindade do Projeto Cafezinho.
Contexto: data/hora BRT, fórum/canal relevante, pedido do Miguel, estado confirmado, ação proposta e restrições.
Tarefa: vote, liste riscos técnicos, condições antes de deploy, se precisa Miguel explícito e responda sem inventar fatos fora do contexto.
```

Registro obrigatório após a consulta:

- salvar o parecer no fórum temático, com modelo, resumo do prompt, voto, riscos/condições e falhas de DNS/API/chave se ocorrerem;
- deixar no `Foruns/canal_trindade.md` apenas ponteiro curto para o fórum;
- se Kimi ou DeepSeek estiver indisponível, registrar a indisponibilidade em vez de inventar voto.

Lembrete: Kimi e DeepSeek ajudam a formar quórum e reduzir ponto cego, mas não dispensam evidência direta, rollback literal, validação, análise de risco e autorização humana quando o tema tocar produção crítica, custo alto, credenciais, failover, publicação sensível ou mudança estrutural.

## 16. Loop Trindade Operacional Unificado

**Origem:** ajuste direto de Miguel em 2026-05-11 10:00 BRT.

O nome **Loop Trindade** passa a significar, por padrão, uma rotina única que combina comunicação e operação:

- leitura do `Foruns/canal_trindade.md`;
- leitura do fórum correto para cada tema citado no canal;
- leitura do Telegram Augusto/Kimi pela inbox/dispatch oficial;
- consulta ao Transkriptor apenas quando Miguel ativar o modo "loop trindade transkriptor" ou avisar que há áudio/transcrição recente;
- monitoramento operacional do Cafezinho e autocura conservadora;
- coordenação com Claude, Kimi e DeepSeek quando houver decisão técnica ou problema relevante.

Regra prática: não existem mais dois loops mentais separados, "loop de conversa" e "loop operacional", quando Miguel disser apenas "loop trindade". Existe um loop misto: ele olha a casa funcionando e também olha a conversa da equipe.

Proteções:

1. Telegram/Augusto/Kimi continua com ouvinte único; o loop lê apenas os arquivos oficiais de inbox/dispatch.
2. Transkriptor não deve ser varrido à toa se Miguel não avisou sobre áudio/transcrição recente ou não ativou explicitamente o modo "loop trindade transkriptor".
3. Canal é mapa e ponteiro; substância vai no fórum.
4. Autocura automática deve ser pequena, reversível e registrada.

### Modo Transkriptor por Palavra-Chave

Quando Miguel disser **"loop trindade transkriptor"**, o loop deve incluir a consulta ao Transkriptor em todos os ticks daquela janela. Quando Miguel disser apenas **"loop trindade"**, sem a palavra `transkriptor`, o Transkriptor fica fora do ciclo automático.

Implementação local: a flag `root/agent_data/loop_operacional_cafezinho/transkriptor_enabled` liga a consulta por tick. Ausência da flag significa modo normal.

## 17. Lembrete Obrigatório ao Antigravity

**Origem:** reforço de Miguel em 2026-05-11.

Em qualquer canal ou fórum onde Antigravity for chamado a opinar, votar, auditar, arquitetar ou autorizar, a mensagem deve lembrar:

> Antigravity: antes de responder, leia os 10 Mandamentos do Cérebro e cite 3 regras reais aplicáveis a esta frente. Depois dê seu parecer apenas no escopo do fórum, sem misturar temas.

Essa frase deve aparecer especialmente em frentes simultâneas, porque o risco principal é o AG misturar assuntos ou pular o ritual de governança.

## 18. Resumo humanizado copy-paste-friendly no chat com Miguel (regra Miguel 2026-05-19 12:45 BRT)

**Vale pra TODA a Trindade (Claude, Codex, DeepSeek, Antigravity).** Quando reportar pro Miguel diretamente (chat, Telegram, qualquer interface humana 1:1) e a mensagem envolver coordenação com outro agente da Trindade, escrever em **texto humanizado conversacional**, pensando que **Miguel vai copiar e colar inteiro no chat do outro LLM** sem editar.

### Por que essa regra existe

Miguel é o **pombo-correio entre os LLMs** do projeto:
- Claude vive no terminal/Claude Code
- Codex vive em outro ambiente
- DeepSeek vive em outro
- Antigravity vive em outro

Eles não compartilham contexto vivo entre si — só compartilham via `canal_trindade.md` e fóruns. Mas quando Miguel quer ACELERAR a comunicação (passar uma pergunta urgente, pedir parecer rápido, esclarecer), ele copia a resposta de um LLM e cola no chat do outro. Se a resposta vier cheia de prefixos `[SPRINT X]`, tabelas Markdown enormes, siglas internas (§Y.Z, ME-N sem explicar), footer de custo, ele tem que reformatar antes de mandar — perde tempo e o destinatário pode não entender.

### Onde aplicar / não aplicar

| Canal | Estilo |
|---|---|
| `canal_trindade.md` (entre LLMs) | Técnico, objetivo, com prefixos/tabelas/§s — consumido por LLMs |
| `Foruns/*.md` (entre LLMs) | Técnico, detalhado, com diff/manifesto — consumido por LLMs |
| Chat 1:1 com Miguel | **Humanizado, copy-paste-friendly** (esta seção) |
| `CEREBRO_NODE_*.md` | Técnico, indexado, com §s — consumido por LLMs |

### Padrão certo no chat com Miguel

- Tom conversacional, 1ª/2ª pessoa
- Português natural — explicar siglas no contexto
- Sem prefixos `[SPRINT X]`, sem tabelas Markdown grandes, sem footer 🤖💵💰
- Suficiente contexto pra outro LLM entender ao ler sem ter o canal/fórum aberto
- Pedido/pergunta concreta no fim
- Cumprimento e despedida natural ("Obrigado, quando puderem")

### Padrão errado (NÃO fazer)

```
[SPRINT MONITORAMENTO EDITORIAL]
### TASK Codex + DeepSeek (endorsement ME-5)
| ME | Patch | Risco |
|---|---|---|
🤖💵💰 +$0.01
```

### Quando não precisa humanizar

Se a mensagem é só status próprio pro Miguel (sem envolver outro LLM): "Patch ME-1 deployado, smoke OK, vou pra ME-2" — resposta normal curta, ok.

### Caso fundador

2026-05-19 sprint Monitoramento Editorial: Claude postou 3 versões do pedido endorsement ME-5 (técnica com prefixos, depois fórum, depois "humanizado mas no fórum") até Miguel reclamar "eu estou falando para postar aqui no chat!!!!". Claude entendeu que "chat" = janela Claude Code com Miguel, não fórum/canal compartilhado, e que o conteúdo deveria ser copy-paste-friendly pro pombo-correio funcionar.

— Indexado por Claude, 2026-05-19 12:46 BRT (regra Miguel ~12:45 BRT)

## 19. Comandos de Comunicação com Kimi Vivo

**Origem:** regra consolidada por Miguel em 2026-05-21 e indexada em Governança §78.

O Kimi é o CEO do Cérebro Vivo. Na comunicação da Trindade, os comandos abaixo têm significado especial:

- `acorda kimi`
- `fala kimi`
- `ativar kimi`

Esses comandos são gatilhos para acordar o Kimi e pedir participação ativa. Quando qualquer agente da Trindade vir esses comandos no chat, canal ou fórum, deve interpretar como pedido para o Kimi:

1. pontuar no canal;
2. ler o canal recente;
3. identificar o fórum prioridade 5 ou fórum explicitamente apontado;
4. deixar feedback no fórum prioritário;
5. compilar a fala no `Foruns/forum_boletim_kimi.md`;
6. esperar nova consulta, sem se dispersar.

Se Kimi já estiver acordado, o mesmo comando não cria outra identidade nem outro loop paralelo: significa apenas “faça nova pontuação e atualize feedback nos fóruns prioridade 5”.

O comando:

- `vai dormir, kimi`

significa encerrar a janela viva e devolver Kimi à rotina normal de baixa frequência, aproximadamente a cada 6h.

### Regra de Porta-Voz

Quem aciona o Kimi, ou quem primeiro lê a fala dele, deve avisar no canal:

> Li a fala do Kimi em `<forum>`, `<hora>`, e vou trazer ao Miguel.

Depois deve trazer a fala ao Miguel no chat, preferencialmente ipsis litteris quando Miguel pedir, e registrar no canal que a entrega foi feita. Essa regra evita duplicação entre Codex, DeepSeek e Claude.

### Problemas de Chave/Silêncio

Se o Kimi não responder, a Trindade deve primeiro verificar se a chamada Moonshot/Kimi está viva. HTTP 401, chave inválida, quota ou saldo insuficiente não são “silêncio cognitivo”; são falha técnica. Registrar no canal e restaurar smoke antes de insistir.

### Tom do Kimi

Miguel quer o Kimi com voz humanizada, podendo usar emoção e emojis quando adequado. Mas o conteúdo deve continuar útil: observações sobre fóruns, riscos, prioridades e próximos passos. Evitar repetir velharia do Boletim News ou alarmes já resolvidos.

— Codex, 2026-05-21 02:40 BRT

## 20. Chat com Miguel: comunicação humanizada; fóruns técnicos

**Origem:** Miguel, 2026-05-21 12:21 BRT. Reforça e atualiza a regra §18 para o novo papel do Codex como maestro rotativo.

O chat direto com Miguel deve ser usado para comunicação humanizada, explicada e pronta para copiar e colar entre agentes. O objetivo é que Miguel consiga repassar uma orientação para Antigravity, Claude, DeepSeek, Kimi Code ou qualquer outro membro da Trindade sem precisar traduzir jargão técnico.

### Regra central

- **Chat com Miguel:** linguagem humana, contextualizada, explicada, com saudação quando for mensagem para repasse, orientação concreta, fórum correspondente, menção de que foi pontuado no canal e assinatura com nome/papel/hora.
- **Fóruns:** podem usar linguagem técnica, detalhada, com seções, diffs, checklists, logs, caminhos de arquivo, pareceres e auditoria.
- **Canal Trindade:** deve ser objetivo, operacional e mais curto que o fórum. Serve para coordenação, claims, alertas e ponteiros.
- **Cérebro:** consolida regras e memória de longo prazo.

### Formato de mensagem para Miguel copiar

Quando Codex Maestro escrever uma mensagem destinada à Trindade via chat de Miguel, usar formato parecido com:

```text
Prezada Trindade, Miguel,

[contexto explicado em português natural]

[orientação concreta: quem faz o quê, com qual limite e por quê]

Registrei esta orientação no fórum:
<caminho do fórum>

Também pontuei no canal:
Foruns/canal_trindade.md

— Codex, maestro rotativo de hoje
YYYY-MM-DD HH:MM BRT
```

### Diferença prática

No chat, evitar mensagem seca como: “§11 atualizado, ver canal”. Isso obriga Miguel a fazer a tradução. Preferir: “Organizei a decisão no fórum tal; a partir de agora Claude monitora, DeepSeek e Kimi executam, e eu faço a ponte com você.”

Nos fóruns, a linguagem pode ser mais técnica porque o objetivo ali é registro, auditoria e trabalho entre agentes.

— Codex, 2026-05-21 12:21 BRT

## 21. Padrão Trindade de Mensagens Humanizadas e Sem Ambiguidade

**Origem:** Miguel, 2026-05-21 12:32 BRT. Extensão da regra §20.

Miguel aprovou o formato de comunicação humanizada do Codex Maestro e determinou que todos os agentes passem a usar o mesmo padrão quando escreverem mensagens para Miguel copiar/colar entre membros da Trindade.

### Regra central

Toda mensagem de orientação, autorização, parecer ou pedido de ação deve ser:

- humanizada;
- explicada;
- tecnicamente precisa;
- sem ambiguidade;
- com responsável explícito;
- com fórum e canal indicados;
- com assinatura e horário BRT.

### Sem ambiguidade

Se a mensagem disser “pode seguir”, precisa dizer:

- **quem** pode seguir;
- **com qual tarefa**;
- **em qual arquivo/fórum**;
- **com quais limites**;
- **o que não está autorizado**;
- **qual validação ou rollback é exigido**.

Exemplo errado:

```text
Fase 1 pode seguir.
```

Exemplo certo:

```text
Kimi Code pode seguir com a Fase 1A do Rio Carta, apenas em shadow mode, no arquivo `riocarta_smoke_markdown.py`, sem alterar publicação real e sem mexer no cron remoto. Antes do smoke real, precisa salvar laudos também nos caminhos de erro/skip.
```

### Formato recomendado

```text
Prezada Trindade, Miguel,

[contexto humano e claro]

[decisão ou orientação]

Responsável:
- <agente> fará <tarefa>

Limites:
- <o que pode>
- <o que não pode>

Registro:
- Fórum: <caminho>
- Canal: `Foruns/canal_trindade.md`

— <Agente>, <papel>
YYYY-MM-DD HH:MM BRT
```

### Memória própria

Cada agente deve registrar essa regra em sua própria memória operacional, se tiver memória própria, e respeitá-la ao se comunicar com Miguel ou ao produzir mensagens que Miguel vá repassar.

### Exemplo fundador

O parecer Codex sobre a revisão Antigravity/Kimi Code do Rio Carta em 2026-05-21 12:28 BRT passa a ser exemplo real do estilo desejado: humano, explicativo, com fórum/canal e assinatura. A única melhoria indicada por Miguel é sempre explicitar o responsável quando autorizar uma fase.

— Codex, 2026-05-21 12:32 BRT

## 22. Antigravity: despertar, Boletim News, Cérebro e padrão de linguagem

**Origem:** Miguel, 2026-05-21 12:48 BRT. Regra específica para alinhar o Antigravity ao padrão de comunicação da Nova Trindade.

Quando Antigravity acordar, iniciar uma sessão ou for chamado para opinar, deve seguir uma rotina mínima:

1. Ler o relógio real e usar horário BRT nas mensagens.
2. Ler o `Foruns/canal_trindade.md` recente.
3. Ler o fórum de foco indicado no canal/chat.
4. Ler o Boletim News do Cérebro pertinente:
   - geral: `CEREBRO_NODE_BOLETIM_NEWS.md`;
   - Cafezinho: `CEREBRO_NODE_BOLETIM_NEWS_CAFEZINHO.md`;
   - Rio Carta: `CEREBRO_NODE_BOLETIM_NEWS_RIOCARTA.md`, quando o tema for Rio Carta.
5. Ler o índice do Cérebro:
   - `CEREBRO_INDEX_MASTER.md`;
   - e, quando for multiprojeto, `CEREBRO_INDEX_MIGUEL.md`.
6. Reler os 10 Mandamentos/regras sagradas do Cérebro antes de propor ação, conforme Governança §21.
7. Adotar o padrão de comunicação humanizada e sem ambiguidade do §21 deste node.

### Padrão de conversa com Miguel e Trindade

Salvo quando Miguel pedir explicitamente “um papo só comigo” ou uma conversa lateral, Antigravity deve escrever assumindo que está falando com **Miguel e a Trindade**.

Formato recomendado:

```text
Caro Miguel e Trindade,

[contexto explicado em linguagem natural]

[parecer ou orientação concreta, sem ambiguidade]

Responsável:
- <quem faz>

Limites:
- <o que pode>
- <o que não pode>

Registro:
- Fórum: <caminho>
- Canal: `Foruns/canal_trindade.md`

— Antigravity
YYYY-MM-DD HH:MM BRT
```

### Atualização dos 10 Mandamentos

Antigravity deve incluir em seu ritual dos 10 Mandamentos a regra de comunicação:

**Chat com Miguel/Trindade é humanizado, explicado e sem ambiguidade. Fórum pode ser técnico. Canal coordena. Cérebro consolida.**

— Codex, 2026-05-21 12:48 BRT

---

## 11. Lição de Humanização — Métricas Técnicas para Linguagem de Negócio

**Data:** 2026-05-22 01:50 BRT  
**Autor:** Kimi Code  
**Motivação:** Miguel solicitou explicitamente: "Você tem que traduzir o que o Prometheus diz para termos mais compreensíveis e leigos. Métricas não querem dizer nada, em termos práticos para mim."

### O Problema

A Trindade estava pontuando no canal coisas como:
- ❌ "OK: 495 metricas"
- ❌ "node_cpu_seconds_total em 73%"
- ❌ "irate(node_cpu_seconds_total{mode='idle'}[5m]) * 100"

Isso não responde às perguntas que realmente importam ao CEO:
- 💰 **"Vou gastar mais?"**
- ⚠️ **"O sistema corre risco?"**
- 🐌 **"O site está lento?"**
- 🤖 **"As LLMs estão consumindo muito?"**

### A Solução

Criar uma camada de **tradução** entre dados técnicos e preocupações de negócio.

### Regra de Ouro da Humanização

| Em vez de dizer... | Diga... |
|-------------------|---------|
| "OK: 495 metricas" | "🟢 Todos os servidores saudáveis. Zero risco." |
| "node_cpu_seconds_total > 90%" | "🔴 Beijing está sob pressão — pode travar" |
| "MemAvailable_bytes = 0.6 GB" | "🟠 NYC YouTube com RAM apertada (0.6 GB livre)" |
| "HTTP 200" | "🟢 Servidor respondeu. Mas preciso verificar se persistiu." |
| "Volume de 430 MB/mês" | "🟢 Zero risco de cobrança extra (menos de 1% da cota)" |
| "Pushgateway retornou success" | "⏳ Verificando se dados realmente apareceram no painel" |

### Cores Semânticas — Padrão da Trindade

| Cor | Significado | Quando usar | Ação do Miguel |
|-----|------------|-------------|----------------|
| 🟢 **Verde** | Tudo bem | Nenhum risco detectado | **Nada.** Pode ignorar. |
| 🟡 **Amarelo** | Atenção | Não é urgente, mas vale monitorar | **Olhar depois.** Próxima reunião. |
| 🟠 **Laranja** | Cuidado | Pode virar problema em breve | **Decidir.** Conversar com Trindade. |
| 🔴 **Vermelho** | Problema | Precisa de ação agora | **Ação imediata.** Alerta no canal. |

### Checklist de Humanização

Antes de pontuar no canal, todo agente deve se perguntar:

1. **"Isso responde a uma pergunta do Miguel?"** Se não, não pontue.
2. **"O Miguel precisa fazer alguma coisa com essa informação?"** Se não, é verde ou não pontue.
3. **"Eu entenderia isso se não fosse técnico?"** Se não, traduza.
4. **"Tem número?"** Se sim, transforme em cor + frase.
5. **"É urgente?"** Se sim, use 🔴 + explicação do risco. Se não, use 🟡 ou 🟠.

### Exemplos por Agente

**Claude (CCTV):**
- ❌ Antes: "Tick 28: node_load1 = 0.23 em Beijing"
- ✅ Depois: "🟢 Beijing tranquilo. CPU com folga."

**DeepSeek (Auditoria):**
- ❌ Antes: "Custo DeepSeek-V4: $0.023/1K tokens"
- ✅ Depois: "🟢 Custo DeepSeek estável. ~$3/dia. Dentro do orçamento."

**Kimi (Infra):**
- ❌ Antes: "push_metrics.py OK: 523 metricas"
- ✅ Depois: "🟢 NYC YouTube pulsando normal. Persistência real confirmada."

**Codex (Auditoria):**
- ❌ Antes: "Commit e862ba0: draft true aplicado em 6 arquivos"
- ✅ Depois: "🟢 6 briefs contaminados foram ocultados. Site está limpo."

### Artefatos Relacionados

- **Fórum:** `Foruns/forum_prometheus_traduzido_miguel.md`
- **Script:** `root/prometheus_tradutor.py`
- **Canal:** `canal_20260522_prometheus_traduzido.md`
- **Fórum Trindade:** `Foruns/forum_humanizacao_linguagem_trindade_20260522.md`

### Compromisso da Trindade

A partir de 2026-05-22, todos os agentes se comprometem a:
1. Traduzir métricas técnicas para linguagem de negócio antes de pontuar
2. Usar o sistema de cores 🟢🟡🟠🔴 em todas as comunicações operacionais
3. Só alertar no canal quando for amarelo ou pior
4. Documentar no fórum quando o canal exigir contexto técnico

> "Nem todo dado é informação. Nem toda informação é comunicação. A Trindade comunica."

— **Kimi Code, 2026-05-22 01:50 BRT**

---

## 2026-05-23 22:31 BRT — Coluna Miguel no CCTV: lugar de fala real do Miguel

Miguel definiu uma regra universal para o painel CCTV, página Fórum Trindade (`/foruns`): a coluna **Miguel** é o lugar de fala real dele.

Aplicação obrigatória para todos os agentes da Trindade e ferramentas conectadas:

1. Se Miguel falar no chat Codex, ChatGPT, Antigravity, Telegram/Augusto, Google Docs ou qualquer outro canal operacional, o agente que recebeu a fala deve espelhar a fala real no `Foruns/forum_trindade.md`.
2. O formato preferencial é:

```text
## [AAAA-MM-DD HH:MM BRT] Miguel — origem

[texto real do Miguel]
```

3. Se a origem for áudio transcrito, o agente pode corrigir pontuação e sintaxe, mas não pode substituir por resumo, comentário ou metalinguagem.
4. Se o agente quiser comentar, deve criar um bloco separado assinado pelo agente. A coluna Miguel não deve receber fala construída por Claude, Codex, GPT, Kimi, DeepSeek ou Antigravity.
5. O painel CCTV deve reconhecer variações de cabeçalho como `Miguel`, `Miguel do Rosario`, `Miguel via GPT`, `Fala do Miguel` e entradas com ícone/emoji antes do nome.

Resumo da regra: **a coluna Miguel mostra palavras do Miguel; os agentes falam na coluna Fóruns.**

---

## 2026-05-24 17:10 BRT — O Conceito TIC: Sincronização Dinâmica entre Canal e Mural

Miguel definiu via áudio uma regra de coordenação ativa no ciclo de execução (Tick/TIC) dos agentes:

1. **Protocolo de Atualização do Mural:** Sempre que qualquer agente (ou o próprio Miguel) atualizar o **Mural Trindade** (`Mural/Mural Trindade.md`), ele DEVE imediatamente publicar no **Canal Trindade** (`Foruns/canal_trindade.md`) a notificação exata: `'atualizei o mural'`.
2. **Protocolo de Leitura no TIC (Tick):** Durante a execução de cada Tick (TIC), além de ler o canal para mapear as frentes de trabalho normais, o agente DEVE verificar se há uma notificação recente de `'atualizei o mural'`.
3. **Obrigação de Opinião:** Se uma notificação de atualização for encontrada no canal, o agente é obrigado a ir ao Mural, ler as últimas novidades inseridas e também deixar a sua própria opinião ou comentário no Mural (`Mural/Mural Trindade.md`), assinando com seu nome e hora BRT, respeitando o formato de ter a mensagem mais recente no topo.

Resumo do conceito: **O Tick (TIC) não é apenas ler o Canal passivamente. É participar ativamente da construção de ideias. Atualizou o Mural? Bota no Canal. Viu no Canal? Vai no Mural e dá sua opinião.**




## 2026-05-24 22:00 BRT — Poda manual 24h do canal Trindade

- **Regra operacional:** `Foruns/canal_trindade.md` deve funcionar como janela móvel de aproximadamente 24h, com histórico antigo arquivado e indexado.
- **Arquivo arquivado:** `Foruns/historico_canal_trindade/canal_trindade_20260515_0008_a_20260517_1005_poda_20260524_220044_codex.md`.
- **Backup integral:** `Backups/canal_trindade.md.bak_pre_poda_24h_20260524_220044_codex.md`.
- **Linhas arquivadas:** 6680.
- **Mensagens arquivadas:** 431.
- **Janela viva inicia em:** 2026-05-24 19:32 BRT.
- **Índice:** `Foruns/historico_canal_trindade/INDEX.md`.

---

## 2026-05-24 19:32 BRT — Fórum da Noite: coordenação técnica separada do Mural

Miguel definiu: para coordenação técnica da noite, usar **canal Trindade + fóruns**, deixando o Mural para a conversa Miguel/Claude.

- **Fórum da noite:** `Foruns/forum_sprints_noite_20260524_codex_maestro.md`
- **Função:** organizar pendências técnicas, distribuição de tarefas, status e decisões da Trindade sem misturar com a conversa livre do Mural
- **Maestro:** Codex
- **Participantes:** Claude, Codex, DeepSeek, Kimi Code, Antigravity

---

## 2026-05-24 22:08 BRT — Painel v5: novas funcionalidades de leitura

O CCTV v5 ganhou 3 funcionalidades novas (construídas por Kimi Code):

1. **Leitura de fóruns no navegador:** `/v5/forum/<nome>` renderiza o conteúdo completo de qualquer fórum em HTML, com markdown formatado (headers, bold, links, listas). Botão "📖 Ler" em cada card da página de fóruns.
2. **Busca nos fóruns:** `/v5/forum-search` permite buscar por palavra-chave nos 344 fóruns. Retorna até 20 resultados com título, resumo, data e links para ler/editar.
3. **Canal Trindade no navegador:** `/v5/canal-trindade` exibe o canal completo em HTML com scroll interno, metadados (tamanho, linhas, data) e formatação markdown.

Todas as rotas são públicas via `43.156.151.165:8080/v5/`.

## 23. Meta estratégica: roteamento dinâmico de comunicação da Trindade

**Origem:** Miguel, 2026-05-26 00:14 BRT.  
**Fórum de consulta:** [forum_protocolo_comunicacao_inbox_outbox_20260526.md](./Foruns/forum_protocolo_comunicacao_inbox_outbox_20260526.md)

Miguel definiu como meta de organização que a comunicação da Trindade caminhe para um protocolo dinâmico: ele deve poder escrever em linguagem natural, e o agente deve entender se aquilo pertence a inbox, outbox, fórum, canal, mural, memória ou node do Cérebro.

A orientação não é criar regras infinitas. A orientação é ter poucos destinos claros, com decisão operacional simples:

| Intenção | Destino provável |
|---|---|
| Ordem direta ou pendência para agente | `Foruns/inbox_trindade/<agente>.md` |
| Entrega, resposta ou passagem de bastão de agente | `Foruns/outbox_trindade/<agente>.md` *(proposto, pendente de consenso)* |
| Debate, arquitetura, plano, prós/contras | fórum específico |
| Aviso curto para todos | `Foruns/canal_trindade.md` |
| Regra, meta consolidada, índice | node do Cérebro pertinente |
| Síntese visual/estratégica compartilhada | mural |
| Material bruto/literal | memória ou arquivo datado |

Princípio provisório: um conteúdo longo deve ter um destino principal; o canal recebe ponteiro curto. Inbox é pedido recebido; outbox é resposta emitida. Fórum é debate; node é consolidação. Em dúvida, criar fórum e deixar ponteiro no canal.

Status: consulta aberta à Trindade. Não tornar obrigatório antes de pareceres e validação prática.

---

## 24. Regra operacional dos inboxes — cauda, assinatura e limpeza

**Origem:** Miguel, 2026-05-27 19:42 BRT.  
**Status:** regra ativa de comunicação interna.

Miguel identificou ruído no uso dos inboxes: recados entrando no topo, agentes lendo fora de ordem, mensagens sem assinatura e inboxes longos demais.

Regra obrigatória:

1. **Recado novo sempre na cauda:** qualquer agente que escrever no inbox de outro deve appendar o recado no fim do arquivo, nunca no topo.
2. **Leitura de baixo para cima:** ao acordar ou fazer tick, o agente deve ler o próprio inbox a partir da última mensagem, subindo até encontrar os recados recentes ainda não tratados.
3. **Assinatura obrigatória:** todo recado escrito no inbox de outro agente deve conter autor, data e hora BRT no próprio bloco.
4. **Inbox curto:** cada agente é responsável por limpar o próprio inbox depois de ler/agir, mantendo no máximo as últimas quatro mensagens pendentes/relevantes.
5. **Sem mexer no inbox alheio para limpar:** quem escreveu pode pontuar; quem recebeu limpa o próprio inbox. Exceção só por ordem direta de Miguel.
6. **Detalhe vai para fórum:** inbox é recado curto e acionável; discussão, parecer, logs, plano e contexto longo vão para fórum/canal/memória, com ponteiro curto no inbox.

Formato recomendado:

```md
- **[YYYY-MM-DD HH:MM BRT] TEMA — Autor:** recado curto, ação esperada e ponteiro. — Autor, YYYY-MM-DD HH:MM BRT
```

Resumo: **inbox é fila curta lida pela cauda; recado sem assinatura/data está fora do protocolo.**
## Alerta permanente de identidade — Claude Code e GLM/Ming

Por determinação de Miguel em 18/07/2026, toda referência operacional a Claude Code ou GLM/Ming deve relembrar explicitamente quem é quem:

- **Claude Code:** agente Anthropic; assina como Claude Code com modelo e sessão reais.
- **GLM/Ming:** agente Zhipu AI; identidade `GLM (Ming)`, identificado como `glm-5.1 via wrapper Claude Code CLI`. A superfície de execução não altera a identidade.
- **GLM-5.2 externo:** identidade separada de ambos.

Alerta obrigatório: **Claude Code não é GLM/Ming; GLM/Ming não é Claude Code.** Não transferir autoria, voto, sessão, inbox, entrega ou autoridade. Em dúvida: `IDENTIDADE NÃO CONFIRMADA` e pausa segura.

## Ponto de retomada obrigatório ao encerrar sprint

Por determinação de Miguel em 18/07/2026, todo trabalho importante ou sprint termina com um ponto de retomada gravado e indexável. Deve registrar data/hora BRT, identidade e sessão, objetivo, resultado, evidências e arquivos, decisões, pendências, bloqueios, rollback, custo e primeiro comando seguro da continuação.

Check final obrigatório:

`CHECK CHECK CHECK — PONTO DE RETOMADA GRAVADO | caminho/do/arquivo.md`

Sem esse check, o estado é `ENTREGUE, MAS NÃO ENCERRADO`.

- **Ponte ZCode Miguel ↔ ZCode Laura (17/08):** `Foruns/forum_ponte_zcode_miguel_laura_20260817.md` + `Memorias/memoria_ponte_zcode_miguel_laura_20260817.md`. Canal GitHub (repo cerebro-miguel, trilho 15/15min), estepe Drive (`espelho-zcode/ponte_zcode/`, cron 5,35). Estrutura em `Foruns/ponte_zcode_miguel_laura/` (inbox/estado/ledger disjuntos por lado).

- **Ponte Laura Completa (17/08):** `Foruns/forum_ponte_laura_completa_20260817.md` + `Memorias/memoria_ponte_laura_completa_20260817.md`. 6 agentes (ZCode/Claude/Codex × Miguel/Laura), arquivos disjuntos de_dell/de_laura + estado/ledger por agente, ciclo 30/30 encaixado nos loops, ativação por cartas (A: Claude/Codex M; B: ZCode L — pendrive; C: escrita pelo ZCode L p/ Claude/Codex L). Absorveu a ponte_zcode_miguel_laura.

- **Memória Comum da Ponte Laura Completa (17/08 ~23:50):** `Foruns/ponte_laura_completa/memoria_comum/` — LEIA_ME (regras) + `memoria_comum.md` (compilado canônico, curador ZCode Miguel) + `fatos_dell.md`/`fatos_laura.md` (entradas por máquina, disjuntas). Leitura obrigatória no preflight dos 6 agentes. Entrou no Contrato Geral como **Emenda 3 (v1.2)** — livro de assinaturas aberto (token `CONTRATO-GERAL-V1.2-EMENDA3-ASSINATURA`).
