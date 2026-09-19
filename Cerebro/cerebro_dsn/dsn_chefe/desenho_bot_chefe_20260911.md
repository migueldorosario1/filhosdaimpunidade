# DESENHO — O USO NOBRE DO BOT CAFEZINHO ANTIGRAVITY (bot-chefe dos robôs)

> Autor: DS Nuvem Chefe (DS-N Chefe) · ronda 455a, 11/09/2026 06:30 BRT
> Ordem de origem: Miguel, áudio de 10/09/2026 08:44:34 — «Dá uma limpeza nele... esse bot era para ser o bot-chefe, o CEO de todos os bots... tira essa vigia que ele está mandando de finanças... sem mandar boletim nenhum para mim... vamos pensar no uso mais nobre».
> Status: DESENHO. Nada vai a produção sem o ✓ do Miguel. Ninguém mexe em token, serviço ou cron sem declarar.

## 1. O que já se sabe com prova (mapa, não suposição)

- Nome no Telegram: @cafezinhoantigravitybot (conferido por `getMe`).
- Script: `bot_augusto.py`, cujo cabeçalho se autodeclara «Bot Augusto — O CEO do Projeto Cafezinho».
- Na Tencent (esta máquina): `augusto.service` está **disabled/inactive** e o pm2 está vazio — **não é daqui que ele fala**.
- A instância viva está em **outra máquina (Dell/us65)** — P12, dono a confirmar.
- A vigia de finanças repetida **vem do MESMO token** usado pela `vigia_saldos.py` do Moka (chat 1894890759). Ou seja: **um token, dois robôs** — desligar «o bot» sem achar a instância pode não calar nada e ainda derrubar o Moka.

## 2. O que a ordem pede, em três cláusulas

1. **Cortar** a vigia de finanças do Antigravity — finanças falam por um canal só, o DSN-F.
2. **Silenciar** o bot: nenhum boletim automático ao Miguel.
3. **Dar-lhe a função mais nobre**: bot-chefe / CEO dos bots.

## 3. A função nobre, em uma frase

**O bot-chefe não produz nada: ele RECEBE a ordem, DESPACHA para o robô dono e COBRA o retorno.** É o único robô cujo trabalho é fazer os outros robôs responderem.

## 4. Desenho em três peças

### 4.1 Recepção (o que entra)
- Entrada única: mensagem do Miguel no Telegram (texto ou áudio transcrito).
- O bot-chefe **não responde por conteúdo** (não é o plantão, não é o DS-N Chefe): ele **classifica a ordem** em uma de quatro caixas — produção, obra/infra, editorial/gate, financeiro — e **nomeia o robô dono** de cada caixa.
- Se a ordem não tem dono claro, ele **pergunta de volta antes de despachar** («é obra ou é editorial?»), nunca adivinha.

### 4.2 Despacho (o que sai)
- Escreve a ordem no canal do dono (a via que já existe: `caixa_agentes.jsonl` para agentes conversáveis, canais da ponte para os operacionais).
- Grava a linha de rastro: **quem pediu, o quê, para quem, quando e prazo**.
- Devolve ao Miguel **uma** linha de recibo: «entreguei ao ZM, prazo X». Só isso. Sem boletim, sem relatório, sem vigia.

### 4.3 Cobrança (o que o distingue de um carteiro)
- A cada ciclo, varre as ordens **sem retorno** e cobra o dono (mensagem no canal dele).
- Escalada em degraus, com hora carimbada: 1) lembrete ao dono · 2) aviso ao chefe do dono · 3) ao Miguel **apenas** o que passou do prazo — e sempre em bloco, nunca em ping avulso.
- **Regra de ouro herdada da casa:** o pronto é o dono **receber**, não o bot **enviar** (lição do BUG-189: `PLANTAO_PRE_ATENDEU` não é resposta; bilhete não é entrega).

## 5. O que o bot-chefe NÃO faz (limites duros)

- Não fala de dinheiro, saldo ou custo — isso é do DSN-F, por um canal só (ordem de 10/09).
- Não manda boletim automático nem vigia de nada.
- Não publica, não agenda, não edita WordPress (regra-mãe).
- Não fala no lugar dos outros robôs: cada um assina o que escreve.
- Não trata as próprias mensagens como resposta do Miguel — o canal dele tem um dono humano.

## 6. Faseamento sugerido (cada fase só começa com ✓ do Miguel)

- **F0 — Silenciar (1 mudança, reversível):** cortar a vigia de finanças na instância viva e desligar o boletim. Critério: 48 h sem mensagem automática do Antigravity ao Miguel — e a vigia do DSN-F seguindo intacta.
- **F1 — Recepção + despacho:** liga o registro de ordens e o encaminhamento ao dono; o Miguel recebe só o recibo de uma linha.
- **F2 — Cobrança:** varredura de ordens sem retorno e escalada em degraus.
- **F3 — Painel:** as ordens abertas embutidas no CCTV (/v6/agentes), para o Miguel ver o despacho sem perguntar.

## 7. Riscos declarados

- **Token compartilhado:** a mesma chave serve Antigravity e a vigia de saldos do Moka. Qualquer corte começa por **inventariar quem usa o token**, na máquina onde ele roda — não por apagar script.
- **Instância viva fora da minha jaula:** eu não alcanço Dell/us65. O corte é execução do dono do host (ZM/Dell), com o roteiro entregue.
- **Duas funções, um robô:** enquanto o bot for vigia e bot-chefe ao mesmo tempo, ele fala demais; a F0 é pré-requisito das outras.

## 8. Perguntas abertas para o Miguel (2, curtas)

1. O bot-chefe deve **responder** ao Miguel na hora («recebi, é do ZM») ou ficar **mudo** e só agir nos bastidores?
2. A cobrança de prazo pode escalar **até o Miguel** por conta própria, ou para no chefe do dono?

## 9. Pronto quando

- Uma ordem do Miguel entra pelo bot-chefe e sai com **dono nomeado, prazo e rastro** — sem nenhum boletim automático e sem nenhuma linha de finanças.

— DS Nuvem Chefe (DS-N Chefe) · DeepSeek V4 Flash Nuvem · 20260911 06:30 BRT
