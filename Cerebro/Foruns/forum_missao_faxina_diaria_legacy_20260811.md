# Fórum — origem do desvio `agente_controlado` e missão diária de faxina legacy

**Data:** 11/08/2026  
**Decisão de Miguel:** fazer diariamente uma faxina cuidadosa, levando legacy para o Backblaze e mantendo local e servidores limpos.

## Decisão histórica

O `agente_controlado.py` era backend da Zizilinda, não publicador canônico do Cafezinho. O desvio começou no primeiro piloto real do worker V4 em 19/07/2026, quando essa ferramenta foi chamada por subprocesso como atalho de redação.

Os primeiros eventos V4 e os primeiros logs do subprocesso confirmam a ligação às 19:21–19:23 BRT. A atribuição operacional dos registros aponta para a sessão Codex que ativou Geo/Ciência; não há commit Git preservado que permita atribuição autoral mais fina.

## Missão aprovada

A faxina deixa de ser mutirão ocasional e passa a ser missão diária. O objetivo não é apagar: é retirar do ambiente quente o que foi comprovadamente aposentado, preservando história, rollback e encontrabilidade no B2.

Ritual obrigatório:

`inventário integral → prova de inatividade → mais de 15 dias → consulta a Miguel → manifesto+hash → B2 → verificação → quarentena/retirada autorizada → smoke → Cérebro`

Qualquer dúvida mantém o item no lugar e abre pendência. Nenhum script diário pode apagar automaticamente por glob, idade, nome “legacy” ou pressão de disco.

Material com 15 dias ou menos de inatividade é recente e não pode ser tratado como lixo. Depois de mais de 15 dias, ele é apenas elegível para consulta e continua dependendo de autorização explícita de Miguel.

Nada desaparece sem índice. O inventário deve alcançar inclusive o lixo autorizado, item por item; segredos são registrados como existência classificada, sem revelar valor.

## Prioridades iniciais

1. Tencent: localizar e isolar a cópia antiga do backend Zizilinda quando o SSH voltar.
2. Nova York: varrer backups, snapshots e scripts soltos fora de diretórios canônicos.
3. Local: reduzir duplicatas em `scratch`, espelhos divergentes e cópias históricas fora de `legacy`/Dados Frios.
4. Demais droplets: identificar repos mortos, logs infinitos e backups não enviados ao B2.
5. Consolidar um manifesto diário único, com ponteiros de restauração.

## Estado

Missão persistente criada em 11/08/2026. A rodada zero já isolou o `agente_controlado` em Nova York e local; Tencent continua pendente e explicitamente não saneado.

## Primeira rodada diária executada

Em 11/08, o canário NYC retirou oito códigos legacy da raiz após prova de inatividade em seis dimensões. Pacote, manifesto e checksums foram armazenados no B2 e seus SHA-256 foram conferidos por leitura remota antes e depois da retirada.

Smokes pós-faxina: V4 3/3, sintaxe dos componentes canônicos, Augusto ativo e Mayra ativa. Evidências em `Memorias/faxina_diaria_20260811/RELATORIO_RODADA_NYC_01.md`.

## Segunda rodada: correção de segurança no rio-ag

O GSN antigo havia sido selecionado por ausência de processo, cron e serviço, mas a última atividade era de 07/08. Miguel vetou corretamente a classificação: quatro dias de pausa não são antiguidade suficiente.

Nenhum dado do candidato foi movido ou apagado. A rodada virou auditoria integral, gerou índice de 13.502 entradas e deixou o lote em observação, preservado no caminho original.

## Terceira rodada: árvore temática antiga local

`sites-tematicos_LEGADO_NAO_USAR` superou 15 dias desde a última alteração de arquivo e passou nas provas de ausência operacional. Isso a torna consultável, não descartável automaticamente.

A árvore inteira, com 95.832 entradas e 3,5 GB lógicos, foi indexada. Miguel autorizou depois a retirada; um snapshot integral criptografado preservou inclusive a alteração Git local não commitada e foi restaurado, comparado e relido do B2 por hash antes do corte.

Após a retirada, os oito sites, repositórios, registry, crons e orquestrador V4 permaneceram verdes. O snapshot B2 foi relido novamente com o mesmo SHA-256; relatório final em `Memorias/faxina_diaria_20260811/RELATORIO_EXECUCAO_LOCAL_05.md`.

## Quarta rodada: bancos de mídia órfãos em Nova York

O lote `/root/legacy/banco_midia_20260626`, parado desde 29/06, tem 449 MB em disco e zero consumidor detectado. Os cinco bancos estão íntegros e coincidem exatamente com membros do backup histórico localizado no B2.

Inventário e verificação foram registrados, e Miguel autorizou depois a retirada. Um snapshot exato foi enviado ao B2, relido por hash, restaurado e comparado antes do corte; o original foi removido e os serviços, o banco canônico e a barreira anti-legacy do V4 permaneceram verdes.

O snapshot foi relido novamente depois da retirada. Relatório final: `Memorias/faxina_diaria_20260811/RELATORIO_EXECUCAO_NYC_06.md`.
