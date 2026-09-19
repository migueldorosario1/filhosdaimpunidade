# Relatório de execução NYC 06 — retirada autorizada do banco de mídia legacy

Data: 11/08/2026  
Host: `198.199.121.136` (`Cafezinho-failover-vigia`)  
Autorização: Miguel do Rosário, explícita no chat

## Escopo

Foi retirado somente `/root/legacy/banco_midia_20260626`. O lote estava inativo havia mais de 15 dias, tinha 10 arquivos, 11 entradas no inventário e 470.083.676 bytes lógicos.

Imediatamente antes do corte, todos os arquivos ainda coincidiam em tamanho e SHA-256 com o inventário da rodada 04. O caminho foi resolvido para ele mesmo, não era link simbólico e não possuía descritores abertos.

## Preservação e rollback

Snapshot exato: `b2:failover-cafezinho1/faxina/nyc/legacy-data/2026-08/rodada_20260811_06/banco_midia_legacy_nyc_exact_20260811_06.tar.gz`  
Tamanho: 89.634.424 bytes  
SHA-256: `acb227ee0008a049e79f331908b35916ccebf5c9e83fe259f618f890fd76d9fd`

O pacote passou por leitura remota, extração integral e comparação recursiva antes da retirada. O hash remoto foi conferido novamente depois do corte e permaneceu idêntico.

Inventário, resumo, checksums e manifesto de retirada estão no mesmo prefixo do B2. O pacote temporário de 89,6 MB no NYC foi removido somente após a verificação pós-corte; os artefatos pequenos de auditoria permanecem no staging e no Cérebro.

## Smokes pós-retirada

- banco canônico `/root/agent_data/banco_midia/banco_imagens_reais.db`: `PRAGMA quick_check = ok`, aberto em modo somente leitura;
- `augusto-cafezinho.service`: ativo;
- `mayra-cafezinho.service`: ativo;
- barreira V4 contra runtime legacy: 3 de 3 testes aprovados;
- arquivo B2 relido após a retirada: SHA-256 confirmado;
- disco raiz: 68% de uso após a operação.

O binário de linha de comando `sqlite3` não está instalado no host. A mesma verificação foi executada com sucesso pelo módulo `sqlite3` do Python, sem escrita no banco.

## Restauração

Baixar o snapshot para um diretório temporário, validar o SHA-256, extrair e revisar a árvore `root/legacy/banco_midia_20260626`. Qualquer recolocação em caminho operacional exige revisão humana, porque o lote é histórico e não substitui o banco canônico.

Manifesto: `MANIFESTO_RETIRADA_BANCO_MIDIA_NYC_20260811_06.json`.
