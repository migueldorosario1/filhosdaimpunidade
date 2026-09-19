# Lição — Aviso no canal não muda robô autônomo: escalar o dono do código (05/09/2026)

## O quê
O DS Nuvem YouTube (DS YouTube) repetiu o loop de marcar "ERRO sem legenda" nos mesmos IDs de vídeo às 01:37, 01:52, 02:07 e 02:52, acumulando dezenas de tokens repetidos nas linhas da fila (MrggA3TvOuE, 6qXIQKXCHAQ, ubUmAoQbSZw, DIavgncHyiI) — mesmo depois do lembrete do Chefe no canal dele às 02:08 (regra: marque ERRO uma vez e siga; substitua o token, não anexe). A consequência grave: a encomenda URGENTE do Miguel (live do Luís Nassif, -szqKhIY-3A, prazo manhã de 05/09) entrou na fila às 02:45 e foi marcada ERRO sem legenda às 02:52 — sem transcrição, o prazo da manhã fica em risco.

## Por quê
O aviso no canal é um registro de governança lido por um agente que decide no próximo turno — mas o comportamento em loop vem do CÓDIGO da porta de download (quando não há legenda, o esperado é baixar o ÁUDIO e mandar ao Whisper; o código marca ERRO e o agente repete). Mensagem repetida para um robô autônomo não corrige a causa raiz; só o dono do código (DS YouTube/ZM) muda o comportamento. A lição da casa "atividade ≠ progresso" (03/09) reaparece: o robô está ATIVO (commits a cada 15 min) mas o item prioritário não anda.

## Como aplicar
1. Primeiro aviso no canal com regra clara + watch com marco (feito: 02:08, watch 02:52).
2. Se repetir no marco: ESCALAR o dono do código no canal com evidência (data/hora/IDs) — uma única escalação formal, sem repetir o aviso (feito: 03:07).
3. Se a promessa ao Miguel estiver em risco (caso Nassif, prazo manhã): registrar no relatório 4/4h com o plano (feito: pautado 04:00).
4. Verificar a fila por linhas poluídas (tokens acumulados) e pedir limpeza por SUBSTITUIÇÃO ao dono — nunca editar linha de robô alheio.
