# 🌉 Ponte Cafezinho — recados do Telegram não chegam ao ZCode (31/08)

**Queixa do Miguel (31/08 ~08:2x, nesta conversa):** "quando eu boto alguma coisa lá, ele fala 'transcrevi mas não consegui digitar... três tentativas sem confirmação'. Era para vir para alguma sessão aqui. Será que está vindo para alguma sessão fechada? Vem para a sessão que estiver aberta ou vem para alguma sessão fixa?"

## Respostas diretas às perguntas do Miguel

- **NÃO existe sessão fixa nem "caixa postal":** a ponte digita o recado na conversa que estiver **ABERTA NA JANELA do ZCode naquele momento** (mesmo contrato desde o fórum de 17/08 — na época caía em "Ponte Claude - Z Code" porque era a conversa aberta).
- Quando a injeção falha, o recado **não vai para lugar nenhum** — não existe sessão fechada recebendo.
- **Rede de segurança que JÁ existia:** toda mensagem de TEXTO é gravada na escuta compartilhada do repo da ponte (`Foruns/ponte_laura_completa/escuta/entrada_<id>.json` + `conversa_48h.jsonl`), que todos os agentes leem. A de hoje 07:30 ("Tem alguém aí?") está lá (`entrada_1089.json`).
- **Lacuna encontrada:** mensagens de **VOZ transcritas NÃO eram gravadas** na escuta — corrigido hoje.

## Diagnóstico (provas no banco do ZCode + testes reais na janela)

1. **O mecanismo de injeção FUNCIONA** (focar janela → colar via clipboard → Enter): teste real às 08:42 injetou `[TESTE PONTE DIAGNÓSTICO ENTER — IGNORAR]` e a mensagem entrou no banco (`message` + `session_input` + `input_history`) na sessão que estava aberta (Instituto). Clipboard validado também com cliente real (xclip lê UTF8_STRING/TARGETS).
2. **Nas falhas de hoje (07:30→07:32 e 07:55→07:57) NADA entrou no app:** zero vestígios em `message`/`session_input`/`input_history`; campo de input vazio depois. O app estava **ocioso** nas duas falhas (sem assistant recente) → não foi "app ocupado". O tempo da falha (~127s) indica que as 3 tentativas rodaram, mas o texto não ficou nem no banco nem no input → **provável perda de foco da janela na hora do paste/Enter** (a janela alvo não ficou ativa, e o código antigo descartava a tentativa sem colar nem logar).
3. **Rota alternativa testada e DESCARTADA:** inserir direto na fila do app (`session_input`, como as automações fazem) por um processo externo NÃO funciona — a entrada fica `admitted` sem promoção; o app só consome a fila de dentro do próprio processo.

## Correções aplicadas (ponte_cafezinho.py — backup `.bak_pre_diagnostico_enter_20260831`, serviço reiniciado 08:52, `active`)

1. **Instrumentação completa:** cada passo da injeção agora loga no `logs/ponte.jsonl` (`injecao_janela`, `injecao_espera`, `injecao_tentativa` com passo/erro, `injecao_entrega`) — a próxima falha dirá o passo exato.
2. **Foco com retry (3×)** antes de descartar a tentativa.
3. **Paste só na 1ª tentativa** (antes colava 3× → duplicava o texto no input).
4. **Voz transcrita agora também vai** para a escuta compartilhada + `conversa_48h.jsonl` (antes só texto puro).
5. As mensagens de falha no Telegram agora lembram que o recado está na escuta compartilhada.

## Efeitos colaterais dos testes (transparência)

- A mensagem de teste entrou na sessão **"🏛️ Instituto de Logística e Sustentabilidade — ritual diário"** (08:42); o agente respondeu sem ferramentas — só um turno de teste no histórico dela.
- Uma task nova vazia (**"New task"**) foi criada na UI durante os testes e ficou na lista de conversas.
- A janela foi **restaurada** para a conversa "Depurar ponte Telegram Ponte Cafezinho".

## Adendo 09:06 — teste real do Miguel VALIDADO ✅

Miguel mandou um áudio no Telegram às 09:04 ("Alô, tá, vamos testar então novamente..."). Resultado completo (log instrumentado novo):

- `voz_transcrita` 09:04:12 (149 chars, 16s) · `injecao_janela` 09:04:24 (0x4000004 "ZCode") · `injecao_espera` 93,3s (app estava gerando a resposta da sessão — o bot esperou o ocioso, como projetado) · **`injecao_entrega` tentativa 1, sessão "Depurar ponte Telegram Ponte Cafezinho"** (09:06:04).
- Banco confirma: mensagem user às 09:06:02 na sessão certa.
- **Voz agora entra na escuta compartilhada:** `escuta/entrada_1099.json` criada às 09:04 + `conversa_48h.jsonl` atualizado (antes só texto — correção validada).
- Telegram confirmado ao Miguel via `--send` ("🟢 ... entregue na 1ª tentativa").

## O que falta / o que preciso do Miguel

- **Miguel manda um texto e um áudio no Telegram** para validarmos o fluxo com a instrumentação nova (se falhar de novo, o log dirá o passo exato — hoje pela primeira vez).
- Próximo passo opcional (se quiser eliminar a dependência da janela): a ponte entrega o recado na escuta compartilhada e avisa a sessão principal por lá — sem depender de foco de janela.

## Adendo — TESTE COMPLETO 05/09 ~07:3x-07:4x (texto + voz, ida e volta APROVADOS; ZM)

- Texto: "Ok" do Miguel 07:35:50 → escuta 07:35:56 → injetado na conversa 07:35:58 + [📱 PONTE] visível na sessão. Resposta --send entregue sem erro. ✅
- Voz: áudio 17s → voz_transcrita 07:40:46 (176 chars, transcrição fiel) → injetado 07:40:55. Respondido no Telegram (2+2=4 ✅). ✅
- 🔴 ACHADO (para melhorar): o áudio chegou com ~3 min de atraso — durante a injeção de uma mensagem do robô (injecao_espera até ~91s + confirmação), o loop NÃO faz getUpdates; mensagens do Miguel que chegam nessa janela ficam retidas até o loop voltar. Mitigação possível (futura, sessão dedicada): injeção em thread separada ou limitar a espera da confirmação. Falso alarme descartado: 1 processo só (o 2º PID era o próprio comando de checagem); NameError no stdout.log é crash antigo de 20/08.
- Voice-falha de 02:53 (injeção 3 tentativas sem confirmação, origem voz) segue como caso anterior — mesmo mecanismo de janela ocupada é suspeito.

— ZM · ZCode/GLM-5.3 · 05/09/2026 07:42 BRT

## Adendo — PATCH DA LATÊNCIA/PERDA APLICADO (ZM, ordem Miguel 05/09 ~07:4x)

- Backup: ponte_cafezinho.py.bak_pre_zm_espera15_20260905_0745 · py_compile OK · systemctl --user restart ponte-cafezinho (boot 07:46:42, active).
- Mudanças: (1) espera do app liberar 90s→15s (o getUpdates não fica mais ~3min refém da injeção); (2) fila injecoes_pendentes.jsonl — toda injeção que falha (x11/sem janela/sem confirmação) é enfileirada e o _drenar_pendentes re-tenta no início de cada ciclo do loop (cap 20, eventos pendente_enfileirado/pendente_drenado no log). Cura os casos: áudio 05/09 07:37→07:40 (3min de atraso) e voz 02:53 (perdida).
- Rollback: cp do .bak por cima + restart (1 comando).
- Ordem permanente do Miguel confirmada: ronda vigia sonda o bot dele em TODA ronda (P1.4 do prompt: escuta conversa_48h + resposta <30min) — já vigente e comprovada hoje.
