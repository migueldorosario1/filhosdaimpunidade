# Relatório — rodada diária 04 — Nova York

Data: 11/08/2026  
Resultado: lote antigo indexado e preservado; decisão de Miguel pendente

## Lote auditado

O lote é `/root/legacy/banco_midia_20260626`, com 470.083.676 bytes lógicos e 449 MB em disco. Ele reúne cinco bancos de mídia declarados órfãos, quatro sidecars SQLite vazios ou pequenos e o README de rollback.

O último arquivo foi modificado em 29/06, 42,969 dias antes da auditoria. O lote supera o limiar de 15 dias, mas permanece apenas elegível para consulta.

## Prova operacional

Não foram encontrados processos, descritores abertos, crons, serviços, referências externas ao caminho ou referências externas aos nomes dos bancos. O banco canônico ativo é `/root/agent_data/banco_midia/banco_imagens_reais.db`, modificado em 11/08.

Os cinco arquivos `.db` passaram em `PRAGMA quick_check` usando conexão imutável e read-only. Nenhum arquivo do lote foi alterado, movido, removido ou compactado.

## Backup histórico conferido

O backup citado no README não existe mais em `/root/backups`, mas foi localizado no B2 em `faxina/tencent/backups-locais/2026-08/limpeza_bancos_midia_orfos_20260626_004335.tar.gz`. Seu SHA-256 é `4301dfff381f48178deb688d86320607cc85735645fc04ee54c1726167b3726e`.

Os cinco membros correspondentes do tar foram lidos em fluxo e comparados com os cinco bancos de Nova York. Tamanho e SHA-256 coincidem para todos eles.

O backup histórico não contém o README nem todos os sidecars atuais. Se Miguel autorizar a retirada, será criado um snapshot novo da pasta exata, com manifesto e teste de restauração, antes de remover a cópia quente.

## Indexação da rodada

- Inventário: `INVENTARIO_BANCO_MIDIA_LEGACY_NYC_20260811_04.jsonl`
- Resumo: `RESUMO_AUDITORIA_BANCO_MIDIA_LEGACY_NYC_20260811_04.json`
- SHA-256 do inventário: `fcf8c3cd5ff506fc1e7dd966faace9cd42d59f4b234225dfce12d23f7047ea2d`
- SHA-256 do resumo: `43b6583d9eaf69a9ea7e8e7cf9843fdb72489c783404420861f3d465ced0d175`
- B2: `b2:failover-cafezinho1/faxina/nyc/auditorias/2026-08/rodada_20260811_04/`

Os hashes do inventário e do resumo foram conferidos por leitura remota. O lote original continua presente e o banco canônico segue ativo.

## Decisão necessária

Miguel deve decidir se autoriza criar o snapshot completo verificado e retirar `/root/legacy/banco_midia_20260626` de Nova York. A recuperação estimada é de 449 MB.
