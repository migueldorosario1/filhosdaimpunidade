# Relatório — rodada diária 03 — ambiente local

Data: 11/08/2026  
Resultado: candidato indexado e preservado; decisão de Miguel pendente

## Lote auditado

O lote é `Projeto Cafezinho Agentes/sites-tematicos_LEGADO_NAO_USAR`, com cerca de 3,5 GB lógicos. A própria árvore contém `README_LEGADO.md`, criado em 24/07 para impedir que agentes confundam os sites antigos com os canônicos em `sites-v4/`.

O último arquivo ou link foi modificado em 24/07/2026 17:38 BRT, 17,495 dias antes da auditoria. Isso supera o limiar de 15 dias, mas apenas torna o lote elegível para consulta a Miguel; não autoriza movimentação ou descarte.

## Prova de ausência operacional

Não foram encontradas referências em processos, descritores abertos, crons, tarefas `at`, timers, systemd, links externos ou arquivos operacionais fora da árvore. Quatro referências textuais externas pertencem a fóruns e memórias históricos.

Os sites canônicos permanecem em `Projeto Cafezinho Agentes/sites-v4/`. Nenhum arquivo da árvore antiga foi movido, removido, compactado ou substituído.

## Conteúdo que exige preservação integral

A árvore contém seis repositórios Git. Cinco estão limpos; `global_south_news` possui uma alteração local não commitada em `scripts/gsn_publish_hourly_batch.mjs`.

Essa diferença impede qualquer estratégia que dependa apenas do GitHub. Se Miguel autorizar o arquivamento, o pacote deverá preservar a árvore inteira, incluindo a modificação local, com tratamento seguro dos arquivos sensíveis.

## Indexação

Foram catalogadas 95.832 entradas: 84.935 arquivos, 10.757 diretórios e 140 links. O volume lógico indexado foi 3.543.345.181 bytes.

Foram identificados 274 caminhos com nomes potencialmente sensíveis. Eles aparecem no inventário somente por caminho e metadados; conteúdo e SHA-256 foram omitidos por exceção de segurança.

## Evidências

- Inventário: `INVENTARIO_LEGACY_TEMATICOS_LOCAL_20260811_03.jsonl.gz`
- Resumo: `RESUMO_AUDITORIA_LEGACY_TEMATICOS_LOCAL_20260811_03.json`
- SHA-256 do inventário: `71195d50eb2d811c2ceee6a1f627c5ab482d79fc26a2592215e69ce1b8e8af3f`
- SHA-256 do resumo: `0fe4d4c1d4921f66eb4cfd06852c71670f36bd4f89f79cd00a282d12c8ae14ec`
- B2: `b2:failover-cafezinho1/faxina/local/auditorias/2026-08/rodada_20260811_03/`

Os hashes foram recalculados por leitura remota e coincidiram. Somente inventário, resumo e checksums foram enviados; os 3,5 GB do candidato continuam no local.

## Decisão necessária

Miguel deve decidir se autoriza a etapa seguinte: criar arquivo integral sanitariamente controlado, enviar ao B2, verificar restauração e só então retirar a cópia quente. Até essa autorização, o estado canônico é preservar no lugar.
