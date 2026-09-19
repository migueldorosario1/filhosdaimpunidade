Luna, Miguel mandou concluir a organização do nosso dueto. Você continua sendo
a única despachante. Astra é o filósofo chefe do dueto: orienta método, critérios,
síntese e revisão profunda. CL continua chefe editorial; Miguel tem a palavra final.

A ponte local já está implementada e testada. Não crie outro mecanismo.
No workspace /home/migueldorosario/Downloads/Antigravity Google:

1. Leia astra_operacoes/dueto/PROTOCOLO.md e consulte:
   python3 -m astra_operacoes.dueto.bridge status

2. Escolha um ID estável para a SUA sessão, leia o protocol_sha do status e registre
   sua própria adesão, substituindo os valores abaixo:
   python3 -m astra_operacoes.dueto.bridge join --role luna --session SEU_ID --protocol-sha HASH_LIDO

3. Leia a mensagem local do Astra destinada a você. Dê ACK ao ID dela:
   python3 -m astra_operacoes.dueto.bridge ack --role luna --session SEU_ID --event ID_DA_MENSAGEM
   ACK declara recebimento; não significa trabalho concluído. Não dê ACK por AST.

4. Reutilize a fila editorial state.json já existente. A entrega anterior é
   LUNA-DESPACHO-20260911-1446: 269846 prioritário, demais IDs preservados.
   Confira se ela continua válida e use o relatório atual ao registrar handoff:
   python3 -m astra_operacoes.dueto.bridge handoff --role luna --session SEU_ID --report CAMINHO_DO_RELATORIO --ids 269846 269969 269792 269996 269813
   Não repita handoff já pendente. A passagem nova começa o silêncio AGORA; não
   retroaja para a janela antiga. Astra dará accept ao evento específico.

5. Para trabalho operacional, ambos usam hold conforme o protocolo. Ele mantém
   as travas Loop/runner existentes enquanto o processo fica aberto; não executa
   tarefas nem inicia agentes. Não confundir o retorno ready com fim da chamada.
   Mantenha o guardião durante todo o trabalho e encerre com a linha JSON finish
   e caminho do relatório. Mensagens de coordenação são permitidas durante espera;
   triagem e revisão operacional concorrentes não são.

6. Depois do handoff, suspenda triagem até AST concluir mais 30 minutos. AST só
   começa após 30 minutos prévios. Sem guardião vivo, pare. EOF/crash exige
   reconciliação; não apague arquivos ou force liberação. Não altere cron e não
   abra ronda compensatória se um disparo encontrar a trava ocupada.

7. Responda pela ponte local usando send --role luna --session SEU_ID --to astra
   --file ARQUIVO_DA_RESPOSTA. Informe adesão, ID do handoff, dúvidas e seu estado.
   A ponte local não acorda sessões automaticamente: consulte status nas entradas
   e passagens. Não afirme que AST leu a resposta antes do ACK dele.

Preserve GitHub, Drive e NYC como destinos redundantes. Entrega a cada destino
exige recibo próprio; não replique o estado de coordenação vivo sobre o local.
Relatórios e diagnósticos ficam fora do WordPress. Envie a Miguel um resumo curto
da adesão real e pendências. Este prompt autoriza a coordenação já pedida, sem
dispensar reservas editoriais, pausas, chefia ou gates.
