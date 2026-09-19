# CEREBRO_NODE_COMUNICACAO — VERSÃO LIGHT
> Gerado automaticamente por `cerebro_light.py` em 2026-07-09 03:32 BRT
> Original: `CEREBRO_NODE_COMUNICACAO.md` (52KB) — 73 entradas totais
> Este arquivo é READ-ONLY. Edite sempre o original.

---

## CABEÇALHO ORIGINAL (primeiras linhas)

# 📡 CÉREBRO CAMADA 2: Nodo de Comunicação e Augusto Bot

Este nó consolida os protocolos de comunicação direta entre o Miguel (Humano) e o Cérebro, orquestrada primordialmente via Telegram (Bot Augusto), além das invocações de "Segunda Opinião" de LLMs.

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

---

## ⏩ 68 entradas antigas omitidas
> Para ver o histórico completo, leia `CEREBRO_NODE_COMUNICACAO.md` diretamente.
> Busca rápida: `python3 cerebro.py --buscar <termo>`

---

## ÚLTIMAS 5 ENTRADAS

## 2026-05-24 22:00 BRT — Poda manual 24h do canal Trindade

- **Regra operacional:** `Foruns/canal_trindade.md` deve funcionar como janela móvel de aproximadamente 24h, com histórico antigo arquivado e indexado.
- **Arquivo arquivado:** `Foruns/historico_canal_trindade/canal_trindade_20260515_0008_a_20260517_1005_poda_20260524_220044_codex.md`.
- **Backup integral:** `Backups/canal_trindade.md.bak_pre_poda_24h_20260524_220044_codex.md`.
- **Linhas arquivadas:** 6680.
- **Mensagens arquivadas:** 431.
- **Janela viva inicia em:** 2026-05-24 19:32 BRT.
- **Índice:** `Foruns/historico_canal_trindade/INDEX.md`.

---

---

## 2026-05-24 19:32 BRT — Fórum da Noite: coordenação técnica separada do Mural

Miguel definiu: para coordenação técnica da noite, usar **canal Trindade + fóruns**, deixando o Mural para a conversa Miguel/Claude.

- **Fórum da noite:** `Foruns/forum_sprints_noite_20260524_codex_maestro.md`
- **Função:** organizar pendências técnicas, distribuição de tarefas, status e decisões da Trindade sem misturar com a conversa livre do Mural
- **Maestro:** Codex
- **Participantes:** Claude, Codex, DeepSeek, Kimi Code, Antigravity

---

---

## 2026-05-24 22:08 BRT — Painel v5: novas funcionalidades de leitura

O CCTV v5 ganhou 3 funcionalidades novas (construídas por Kimi Code):

1. **Leitura de fóruns no navegador:** `/v5/forum/<nome>` renderiza o conteúdo completo de qualquer fórum em HTML, com markdown formatado (headers, bold, links, listas). Botão "📖 Ler" em cada card da página de fóruns.
2. **Busca nos fóruns:** `/v5/forum-search` permite buscar por palavra-chave nos 344 fóruns. Retorna até 20 resultados com título, resumo, data e links para ler/editar.
3. **Canal Trindade no navegador:** `/v5/canal-trindade` exibe o canal completo em HTML com scroll interno, metadados (tamanho, linhas, data) e formatação markdown.

Todas as rotas são públicas via `43.156.151.165:8080/v5/`.

---

## 23. Meta estratégica: roteamento dinâmico de comunicação da Trindade

**Origem:** Miguel, 2026-05-26 00:14 BRT.  
**Fórum de consulta:** [forum_protocolo_comunicacao_inbox_outbox_20260526.md](./Foruns/forum_protocolo_comunicacao_inbox_outbox_20260526.md)

Miguel definiu como meta de organização que a comunicação da Trindade caminhe para um protocolo dinâmico: ele deve poder escrever em linguagem natural, e o agente deve entender se aquilo pertence a inbox, outbox, fórum, canal, mural, memória ou node do Cérebro.

A orientação não é criar regras infinitas. A orientação é ter poucos destinos claros, com decisão operacional simples:

| Intenção | Destino provável |
|---|---|
| Ordem direta ou pendência para agente | `Foruns/inbox_trindade/<agente>.md` |
| Entrega, resposta ou passagem de b

> *(... 732 chars omitidos — ler original)*

---

## 24. Regra operacional dos inboxes — cauda, assinatura e limpeza

**Origem:** Miguel, 2026-05-27 19:42 BRT.  
**Status:** regra ativa de comunicação interna.

Miguel identificou ruído no uso dos inboxes: recados entrando no topo, agentes lendo fora de ordem, mensagens sem assinatura e inboxes longos demais.

Regra obrigatória:

1. **Recado novo sempre na cauda:** qualquer agente que escrever no inbox de outro deve appendar o recado no fim do arquivo, nunca no topo.
2. **Leitura de baixo para cima:** ao acordar ou fazer tick, o agente deve ler o próprio inbox a partir da última mensagem, subindo até encontrar os recados recentes ainda não tratados.
3. **Assinatura obrigatória:** todo recado escrito no inbox de outro agente deve conter autor, data e hora BRT no próprio bloco.
4. **Inbox cu

> *(... 716 chars omitidos — ler original)*

---

## PONTEIROS
- Original completo: [`CEREBRO_NODE_COMUNICACAO.md`](./CEREBRO_NODE_COMUNICACAO.md)
- Índice geral: [`indice_cerebro.json`](./indice_cerebro.json)
- Busca: `python3 cerebro.py --buscar <termo>`
- Validador: `python3 validar_cerebro.py`