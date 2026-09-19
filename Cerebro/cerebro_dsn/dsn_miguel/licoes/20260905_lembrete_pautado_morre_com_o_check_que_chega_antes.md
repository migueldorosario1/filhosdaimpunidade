# Lembrete pautado morre com o ✓ que chega antes do slot (199ª)

Data: 05/09/2026 · Ronda 199ª (slot 19:00) · DS-Dell

## O quê
O DSC-049 (kill-switch do sync-bug) estava há dias SEM o ✓ do Miguel, com lembrete pautado pelo DS-Dell para o relatório das 20:00 (slot 4/4h). O ✓ chegou ~18:3x (decisão do dono relayada pelo DSH-us65 às 18:40 no INBOX e 18:42 no RESPOSTAS) — ~1h20 ANTES do slot do lembrete. Na abertura da 199ª, a releitura do fim do INBOX/RESPOSTAS encontrou o ✓ e o lembrete das 20:00 foi CANCELADO, nunca repetido.

## Por quê
Pendências com lembrete pautado são agendadas contra o relógio (slot 4/4h), mas o dono resolve no relógio DELE — que não avisa o vigia. Repetir um lembrete de algo já autorizado (a) polui o relatório com ruído obsoleto, (b) faz o dono achar que a casa não leu a resposta dele, (c) desperdiça o slot. A mesma regra vale para o padrão irmão «ordem sem ACK → dono pergunta» (197ª): o fluxo inverso também existe — ✓ chega, o lembrete morre.

## Como aplicar
1. Na abertura de TODA ronda, reler o FIM do INBOX_MIGUEL.md e do RESPOSTAS.md (não só o grep de DSC-*/escuta) — a decisão do dono pode ter chegado por relay (DSH-us65) entre rondas.
2. Antes de repetir qualquer pendência pautada (ex.: DSC-049, lembrete 20:00), verificar se o ✓/decisão já existe no origin — se sim, registrar «✓ concedido (hora/ref) — lembrete CANCELADO» e acompanhar a EXECUÇÃO (quem executa, não a pendência).
3. Pendência resolvida vira acompanhamento de execução: nomear executor (Chefe/ZM), não re-abrir a cobrança.

Referência: bloco DS-Dell-20260905-039 (de_dell.md) · INBOX_MIGUEL relay 18:40 · RESPOSTAS.md 18:42 · commit 8e43bd0d6 (DECISAO Miguel).
