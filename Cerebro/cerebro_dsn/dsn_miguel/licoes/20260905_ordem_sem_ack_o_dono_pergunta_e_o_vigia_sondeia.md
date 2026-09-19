# Lição 2026-09-05 — Ordem sem ACK: o dono pergunta e o vigia sondeia até resolver (197ª)

## O quê
No 05/09, a cadeia Chefe→ZM do painel da Baleia Azul (ordem DS-N 200º, 16:34: copiar as 8 edições 02/09→05/09 + sync estrutural no /v6/baleia) encontrou o executor sem ACK no canal dele: a ronda 36ª do ZM (17:12) saiu LIMPA, sem citar a ordem. ~15 min depois o DONO perguntou pela escuta (FALA 17:27:27): «você já pediu direto ao ZM? ele ouve direto? bota na ponte e ele te ouve? monitora isso para mim até resolver». O monitoramento virou missão do DS-Dell: sonda #1 (17:36) e sonda #2 (18:02) mostram o acervo SEGUINDO parado em 01/09 — ordem sem efeito visível por ~1h30, com o dono no circuito.

## Por quê
- Quando a ordem ao executor não tem ACK no canal dele (ronda limpa sem citar), o desenho não distingue «não recebeu» de «recebeu e não fez» — e o dono, que enxerga o painel atrasado, vira o 3º elo da cadeia e pergunta.
- O vigia não tem o poder de fazer o ZM executar (física/cadência de cada agente), mas tem o que a cadeia precisa para fechar: a PONTUALIDADE DO REGISTRO do não-avanço — 1 linha de prova por ronda (sonda com hora + estado do acervo) até o executor ou o dono agirem.
- A FALA do dono com destino claro («monitora até resolver») transforma observação passiva em MISSÃO com régua de fechamento objetiva: acervo sair de 01/09.

## Como aplicar
- Ordem de terceiro em aberto = sonda com estado verificável em TODA ronda minha (endpoint do painel + data da «Edição mais recente» + hora da sonda), registrada no bloco e no nodo — mesmo quando o número não muda (o registro do não-avanço É o dado).
- Nomear no relatório quem detém a execução (ZM), quem monitora (DS-Dell) e o que falta (ACK/execução do ZM na próxima ronda dele ~18:12) — sem duplicar a cobrança formal, que é do Chefe.
- Fala do dono pedindo monitoramento = assumir a parcela que cabe ao vigia e dizer «assumido» na ponte (regra missões especiais), nunca prometer executar o que é do executor.
- Sonda que não muda de resultado por várias rondas não é falha do vigia: é o padrão «ordem sem ACK» em curso — escalar quando o DONO pedir ou quando a régua de tempo do Chefe (cobrança) indicar.

## Ref
- FALA 17:27:27 (INBOX_MIGUEL, commit ca7fedb2e) · ordem DS-N 200º (16:34) · ZM ronda 36ª (17:12 LIMPA) · sondas DS-Dell 17:36 e 18:02 (painel /v6/baleia acervo 01/09) · blocos DS-Dell-20260905-036/037 (de_dell.md) · obs da 196ª (candidata, agora formalizada no 2º ciclo).
