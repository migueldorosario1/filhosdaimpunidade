# Relatório de execução local 05 — retirada autorizada da árvore temática legacy

Data: 11/08/2026  
Host: ambiente local do Miguel  
Autorização: Miguel do Rosário, explícita no chat

## Escopo

Foi retirado somente `Projeto Cafezinho Agentes/sites-tematicos_LEGADO_NAO_USAR`. A árvore estava inativa havia mais de 15 dias e continha 95.832 entradas, 3.543.345.181 bytes lógicos, seis repositórios Git e uma alteração local não commitada em `global_south_news`.

Imediatamente antes do corte, as 95.832 entradas foram revalidadas contra o inventário. Caminhos, tipos, tamanhos, links e hashes permitidos coincidiram; os 274 caminhos de nome potencialmente sensível foram conferidos apenas por metadados.

## Preservação e rollback

Snapshot criptografado: `b2:failover-cafezinho1/faxina/local/legacy-sites/2026-08/rodada_20260811_05/sites_tematicos_legacy_full_20260811_05.tar.gz.gpg`  
Tamanho: 2.742.206.182 bytes  
SHA-256: `00cdc4da3a7b0fda1f2f2d03abec47b478534425ca57042c762573afca2c7fc1`

O tar.gz foi criptografado simetricamente com AES-256 porque a árvore contém arquivos sensíveis. A chave não aparece no manifesto; suas três custódias autorizadas — local, NYC e cofre B2 separado — foram comparadas sem expor valor ou hash.

Antes da retirada, o pacote foi descriptografado e extraído integralmente em diretório temporário. A restauração foi comparada recursivamente com a origem, sem diferenças, e a área temporária foi eliminada depois do teste.

O objeto B2 foi relido integralmente por SHA-256 antes e depois da retirada. As duas leituras produziram exatamente o hash esperado.

## Smokes pós-retirada

- registro canônico: oito sites ativos;
- `Projeto Cafezinho Agentes/sites-v4/`: oito repositórios canônicos presentes;
- `agentes_tematicos/v4/orquestrador.py`: compilação aprovada;
- crons ativos do orquestrador V4: presentes;
- Rio Carta, Mapa Rio, Aiatolah, Global South News, Mundo Trilhos, Rail Post, Discover Brazil e Ceará Digital: HTTP 200.

Nenhum repositório `sites-v4`, componente do orquestrador ou projeto visível entrou no corte.

## Restauração

Baixar o objeto, validar o SHA-256, usar uma custódia autorizada da chave para descriptografar e extrair em diretório temporário. Revisar a árvore antes de qualquer recolocação no caminho original; a restauração não deve substituir os repositórios canônicos `sites-v4`.

Manifesto: `MANIFESTO_RETIRADA_TEMATICOS_LOCAL_20260811_05.json`.
