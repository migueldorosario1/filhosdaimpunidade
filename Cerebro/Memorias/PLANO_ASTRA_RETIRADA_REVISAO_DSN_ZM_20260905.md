# Plano Astra — candidatos do Rio para revisão DS-N e execução eventual ZM

> 05/09/2026 · Astra prepara o índice; DS-N Chefe revisa; ZM é o executor de eventual retirada, conforme fluxo escolhido pelo Miguel.
> **Nenhuma retirada executada ou comando de exclusão gerado. Nenhuma despesa nova autorizada por este documento.**
> Este plano complementa o inventário e o backup já validados; não altera o manifesto original nem amplia a lista.

## 1. Conclusão para decisão

Há **17 journals históricos candidatos**, de baixo risco para a execução dos sites/agentes sob as condições abaixo.
Isso não é garantia de ausência de dano: a retirada reduziria o histórico de logs disponível no servidor e pode afetar consultas antigas.
Os 17 têm cópia recuperada byte a byte; continuam fechados nas duas observações recentes e não mudaram desde o inventário.
**Ainda falta validar recuperação de ACLs/xattrs e confirmar com o tutor que nenhum consumidor precisa desses históricos no host.**
Até concluir esses gates, a classificação A significa candidato comprovado para revisão, não liberação de retirada.

O lote tem **432 MiB lógicos (452.984.832 bytes)** e **417.792.000 bytes alocados, cerca de 398,44 MiB**.
O segundo número é a referência nominal de possível ganho em disco, sem garantia de ganho líquido enquanto o host continua escrevendo.
Astra liberou **0 bytes**. O lote isolado não resolve a causa do crescimento do disco.

## 2. Evidências e horário

- Host confirmado por SSH: `Rio-Carta-Agentes`, `159.89.185.209`; chave já existente, BatchMode e verificação estrita do host.
- Base exclusiva: `/var/log/journal/524f4f88ab99d451c9ee123e69fd5010`.
- Inventário inicial às 07:36 BRT: [JSON integral](INVENTARIO_ASTRA_BACKUP_RIO_20260905.json), SHA256 `de44ac2af0c1f55c15c1bebc196946b67140db674a82a03687718adf8f3d8520`.
- Backup: [manifesto e recibo final](MANIFESTO_ASTRA_BACKUP_RIO_20260905.md), linhas 40–58: readback 07:53:50 e decifragem/conferência dos 17 membros 07:54:07 BRT.
- Revalidação 08:26:02–08:26:07 BRT: mesmos 17 caminhos, tamanhos, metadados e SHA256 do inventário inicial; dois hashes coincidentes e duas inspeções completas de descritores/mapeamentos em /proc, sem uso dos candidatos.
- [JSON privado da revalidação](../../ponte_astra/state/rio_20260905/inventory_archived_journals_1788607567364020893.json), SHA256 `37213637c0d46cb93fa53b51c2a5259299c6b8fc22dbe0b2bf6873925aec7f6f`.
- `df` às **08:27:07 BRT**: `/dev/vda1`, montado em `/`, total 24.883.167.232 bytes, usados 23.640.276.992, disponíveis **1.226.113.024 bytes**, ocupação **96%**.
- Metadados adicionais às **08:29:18 BRT**: [complemento ACL/xattrs](COMPLEMENTO_ASTRA_METADADOS_JOURNALS_RIO_20260905.json), 30.361 bytes; SHA256 **`f400b74fad8be24b47c5b7ee1e5530a5ba3668c04bece72031e9cf7e55cdac23`**.

O complemento fixa o SHA do inventário original e o SHA do tar. Captura exclusivamente os dois xattrs autorizados, em base64, e metadados dos 17.
Valores e metadados foram lidos duas vezes; os inteiros de nanosegundos conferem exatamente com o inventário quando nele existentes.
O hash final acima substitui a versão intermediária de serialização; não usar outro hash do complemento.
Não foi feito novo upload B2. Não foram lidos registros de log nesta captura de metadados.

## 3. A — 17 candidatos individuais, sujeitos aos gates

Todos os nomes abaixo são relativos à **base exclusiva** acima; não são padrões para expansão.
As datas são mtime UTC, não início/fim do conteúdo dos journals. Cada SHA/tamanho/inode consta do JSON inicial; cada ACL consta do complemento.

- **H1:** arquivo regular `system@…journal`, nlink 1, mtime e ctime há mais de 15 dias; fechado nas observações inicial e recente.
- **H2:** tamanho/metadados/SHA inalterados; conteúdo cifrado no B2, baixado integralmente, decifrado e conferido por membro.
- **H3:** caminho de journal histórico, fora do código/configuração selecionados; indício de baixo risco para execução, condicionado à confirmação de dependências/retenção pelo DS-N.
- **Gates comuns:** revisão DS-N; prova de recuperação dos metadados; nova checagem de fechamento/integridade imediatamente antes de qualquer ação de ZM.

| Item | Nome exato na base | MiB lógicos | Mtime UTC | Motivo e situação |
|---|---|---:|---|---|
| A01 | `system@370415200bca4186a213f511ff75317d-000000000022d6f1-0006573c8a1d1987.journal` | 8 | 2026-07-23 | H1 + H2 + H3; gates pendentes |
| A02 | `system@370415200bca4186a213f511ff75317d-000000000022f301-0006573d7a988c9a.journal` | 8 | 2026-07-23 | H1 + H2 + H3; gates pendentes |
| A03 | `system@370415200bca4186a213f511ff75317d-0000000000230fa2-0006573edf22d202.journal` | 8 | 2026-07-23 | H1 + H2 + H3; gates pendentes |
| A04 | `system@370415200bca4186a213f511ff75317d-0000000000232ac8-0006574291b5a679.journal` | 16 | 2026-07-23 | H1 + H2 + H3; gates pendentes |
| A05 | `system@370415200bca4186a213f511ff75317d-0000000000237705-0006574e4c00a563.journal` | 8 | 2026-07-24 | H1 + H2 + H3; gates pendentes |
| A06 | `system@370415200bca4186a213f511ff75317d-00000000002391e5-000657559df62b15.journal` | 8 | 2026-07-24 | H1 + H2 + H3; gates pendentes |
| A07 | `system@370415200bca4186a213f511ff75317d-000000000e42ebf6-000657f0f7900a1c.journal` | 8 | 2026-08-01 | H1 + H2 + H3; gates pendentes |
| A08 | `system@370415200bca4186a213f511ff75317d-000000000e431a39-000657f0f9564a28.journal` | 8 | 2026-08-01 | H1 + H2 + H3; gates pendentes |
| A09 | `system@370415200bca4186a213f511ff75317d-000000000e434c12-000657f104e4f257.journal` | 8 | 2026-08-01 | H1 + H2 + H3; gates pendentes |
| A10 | `system@370415200bca4186a213f511ff75317d-0000000017f9f5b7-00065862e0439795.journal` | 16 | 2026-08-06 | H1 + H2 + H3; gates pendentes |
| A11 | `system@370415200bca4186a213f511ff75317d-0000000017fa458f-00065862e5d6343f.journal` | 48 | 2026-08-08 | H1 + H2 + H3; gates pendentes |
| A12 | `system@370415200bca4186a213f511ff75317d-0000000017fb4296-000658897835a7bc.journal` | 48 | 2026-08-10 | H1 + H2 + H3; gates pendentes |
| A13 | `system@370415200bca4186a213f511ff75317d-0000000017fc3873-000658b95faebe5d.journal` | 48 | 2026-08-12 | H1 + H2 + H3; gates pendentes |
| A14 | `system@370415200bca4186a213f511ff75317d-0000000017fd25f0-000658d19696c7ce.journal` | 48 | 2026-08-14 | H1 + H2 + H3; gates pendentes |
| A15 | `system@370415200bca4186a213f511ff75317d-0000000017fe1f5a-000659053ec2cd72.journal` | 48 | 2026-08-16 | H1 + H2 + H3; gates pendentes |
| A16 | `system@370415200bca4186a213f511ff75317d-0000000017ff179f-0006592fd44a94d5.journal` | 48 | 2026-08-18 | H1 + H2 + H3; gates pendentes |
| A17 | `system@370415200bca4186a213f511ff75317d-000000001800233a-0006594e85fc3383.journal` | 48 | 2026-08-21 | H1 + H2 + H3; gates pendentes |

Não há base para afirmar que um arquivo é dispensável apenas por estar antigo ou fechado.
DS-N deve confirmar a necessidade de investigação, auditoria, retenção e eventuais agentes que consultem histórico via journalctl.
Uma abertura entre duas inspeções não pode ser descartada; o fechamento precisa ser revalidado na janela real de execução.

## 4. B — fora da lista de retirada

| Grupo | Motivo/evidência | Situação |
|---|---|---|
| `system.journal` da base escolhida | Nome ativo excluído do inventário e sem backup neste lote | Preservar; não tocar no arquivo de escrita corrente |
| Os 25 `system@…journal` excluídos por idade | Mtime **ou** ctime não superior a 15 dias; caminhos exatos em `excluded` do JSON | Preservar; não inferir elegibilidade pelo nome de arquivado |
| Qualquer outro machine-ID em `/var/log/journal/` | Não inventariado nem coberto pelos 17 | Incerto/fora do escopo; nenhuma retirada proposta |
| Logs operacionais fora desses 17, bases de dados e filas | Dependências e recuperação não auditadas | Preservar |
| Código, configurações, credenciais, Git, swap, caches e arquivos dos sites/agentes | Sem lista individual aprovada nem prova de dispensabilidade neste trabalho | Preservar; nenhuma limpeza genérica proposta |
| Tar, cifrado, readback, provas e complemento guardados no Dell/Cérebro | Sustentam recuperação e auditoria do lote | Preservar; não são candidatos à limpeza do Rio |

Os 26 excluídos estão discriminados no inventário, sem exclusão silenciosa. Novos arquivos criados após a coleta não herdam autorização.
Astra não fez inventário completo do disco nem teste de todas as dependências dos serviços; a lista A não deve ser expandida por analogia.

## 5. Auditoria de recuperação: bytes confirmados, metadados com gate

O [script do backup](../../astra_operacoes/backup_rio_20260905.py), linhas 253–257, usa USTAR com dono numérico.
Sua validação, linhas 155–193, compara nomes, tipo regular, tamanho e SHA; não validava ACLs/xattrs.
Inspeção independente do tar já recuperado confirmou, nos 17, **UID 0, GID 999, modo 0640 e mtime em segundos** iguais ao inventário.
Nenhum membro extra, PAX ou link; os 17 têm a fração de nanosegundos de mtime ausente do tar USTAR.

A verificação no Rio constatou **`system.posix_acl_access` e `user.crtime_usec` em todos os 17**, com **dois padrões de ACL diferentes**.
Esses atributos não estão no tar. Restaurar tudo apenas como 0:999/0640 não recompõe necessariamente os acessos anteriores.
O complemento conserva os valores exatos desses dois atributos, atime_ns/mtime_ns e dono/grupo/modo; não havia outros nomes de xattr nas 17 consultas.
Base64, SHA de cada atributo e estrutura binária POSIX ACL foram conferidos **sem aplicar atributos a qualquer arquivo**.

**Faltas explícitas antes de uma retirada:**

1. DS-N/ZM confirmar acesso durável ao complemento de hash final e ao inventário; registrar sua integração ao Cérebro. A cópia B2 atual não inclui o complemento.
2. Testar em cópias isoladas que os dois padrões de ACL, os xattrs, dono/grupo/modo e tempos são recuperáveis; permissões efetivas devem ser comparadas, não só o nome do atributo.
3. Validar legibilidade/estrutura dos journals recuperados com ferramenta apropriada, sem publicar seu conteúdo; o teste anterior comprovou igualdade dos bytes, não saúde de um serviço.
4. Registrar a conclusão da revisão DS-N e a janela/reserva de ZM. Se qualquer teste exigir cobrança nova, parar e levar o custo ao Miguel.

Inode, device e ctime ficam como referências de auditoria: uma restauração ordinária não recria o mesmo inode nem o ctime original.
Atime_ns representa a captura de 08:29, pois o inventário inicial não o preservou. Mtime_ns pode ser recuperado a partir do complemento.
Layout esparso/alocação de blocos também não é garantido pelo USTAR; restauração pode ocupar mais espaço que os blocos atuais.
Não se promete recuperação perfeita de todo o sistema nem preservação de metadados que não foram capturados.

## 6. Plano de recuperação para ZM — sem sobrepor produção

1. **Localizar provas.** Conferir manifesto, inventário fixado, complemento de hash final e recibos privados. Preferir a cópia local já validada para ensaio; o B2 é a origem independente de recuperação.
2. **Baixar quando necessário e autorizado.** Destino remoto exato: `b2:failover-cafezinho1/faxina/rio-ag/journals/2026-09/astra_20260905_lote01/`. Usar área privada nova, sem sobrepor arquivos existentes; considerar qualquer custo antes de nova transferência.
3. **Conferir cifrado.** `journals.tar.gpg`: 94.203.743 bytes, SHA256 `1d47eb21b0fdc4b8c8f007ac2d777f1f2e929cd9c7c6695afec689d69144e71e`. Conferir também hashes de manifest.json/README no manifesto original.
4. **Decifrar em isolamento.** Usar a chave dedicada pelo alias `ASTRA_RIO_JOURNALS_20260905_PASSPHRASE` no cofre, sem exibir valor. Tar esperado: 452.997.120 bytes, SHA256 `c2bfce6c75aeb0f5653add1cfa45cf839a874bedd23a86c2e53d811ad52f0e94`.
5. **Validar os 17 membros antes de extrair.** Somente nomes exatos da lista, arquivos regulares, sem links/duplicados/extra; conferir cada tamanho/SHA contra inventário. Extração em diretório privado novo, nunca diretamente em `/var/log/journal`.
6. **Recompor e testar metadados nas cópias.** Conteúdo primeiro; depois dono/grupo numéricos e modo, ACL/xattrs específicos de cada caminho, conferência das permissões resultantes e, por último, atime/mtime em nanosegundos. Mudanças de modo após ACL podem alterar a máscara: verificar estado final.
7. **Conferir estrutura e leitores previstos.** Testar journals recuperados em ambiente isolado e a leitura pelas identidades necessárias; não presumir que o GID 999 significa o mesmo grupo em outro host.
8. **Retorno à origem somente se necessário e autorizado no fluxo DS-N→ZM.** Confirmar host/machine-ID e ausência de symlinks nos componentes; só recriar caminho original ausente. Se o arquivo já existir, preservar ambos e consultar DS-N: nenhuma sobrescrita automática.
9. **Conferir o resultado e registrar.** Comparar conteúdo e metadados restauráveis, os sinais funcionais e o espaço. Manter pacote/provas e registrar diferenças inevitáveis de inode/ctime; não declarar rollback completo se ACL/serviços não foram verificados.

Planejar espaço antes do ensaio: pacote cifrado + tar + extração podem se aproximar de 1 GiB, além da margem de operação.
**Não usar o Rio a 96% como área improvisada para todas essas cópias.** Preferir o ambiente local já reservado ou volume apropriado, sem contratação implícita.
Os originais existem hoje: qualquer ensaio deve ficar isolado. Este plano não solicita restauração sobre eles.

## 7. Verificação funcional e critérios de parada

**Antes da eventual execução de ZM:** atualizar Monitoramento/reserva; DS-N indicar a lista real de serviços/sites/agentes afetáveis e os testes leves de leitura.
Registrar host, df/inodes, estado do journald e dos serviços identificados, saúde HTTP de rotas de consulta e últimos heartbeats/rodadas já produzidos.
Não forçar geração, coleta paga ou publicação para testar; não reiniciar serviço para fabricar prova.
Revalidar os 17 caminhos, nlink/tipo/idade, metadados/hash e uso em /proc imediatamente antes; qualquer diferença devolve o item à revisão.

**Depois de cada item ou lote pequeno autorizado:** repetir os mesmos sinais, comparar disponibilidade/erros e medir ganho efetivo em df.
Ausência de falha imediata não elimina dependência de consulta histórica; acompanhar pelo menos uma rodada natural pertinente definida pelo DS-N.
Comparar com a linha de base para não atribuir um problema preexistente à operação.

**Parar e consultar DS-N/Miguel** se houver candidato aberto/mapeado, hash ou metadado divergente, arquivo novo/symlink, destino diferente, chave/prova ausente, recuperação de ACL falha, dependência histórica descoberta, queda funcional ou margem de disco insuficiente.
Não ampliar escopo, trocar por limpeza genérica, alterar retenção global ou reiniciar serviços como reação automática.
Uma nova despesa depende do Miguel; aprovação técnica do DS-N não concede autorização financeira.

## 8. Encaminhamento e responsabilidades

- **Miguel:** define o objetivo e limites; despesas continuam sob sua decisão.
- **Astra:** entrega índice, evidências e plano; não remove, move, trunca, faz vacuum, git gc ou reinicia.
- **DS-N Chefe:** revisa necessidade histórica/dependências, recuperação e prioridade; devolve decisão por item.
- **ZM:** executor eventual escolhido pelo Miguel; fecha gates e registra o que foi autorizado e realmente realizado.

**O que aconteceu:** revalidação dos 17 e do disco, inspeção de metadados do tar e captura limitada de ACL/xattrs para completar o índice.
**O que falta:** ensaio de recuperação de metadados/legibilidade e revisão DS-N antes de atuação de ZM. O complemento foi integrado ao Cérebro/GitHub, conforme recibo abaixo; DS-N/ZM ainda precisam confirmar que conseguem acessar as provas.
**O que preciso do Miguel:** nenhuma compra agora; manter o fluxo combinado. Qualquer ampliação ou cobrança nova volta à sua decisão.

## 9. Recibo de registro e encaminhamento — 08:42 BRT

Índice publicado no GitHub pelo commit `abbe370114a6a27b00298ca3b30cf8582766cbba`; complemento final publicado pelo commit `ecd19767a678709d496d16cb2f228f5f1c524415`, sem reserializar seus inteiros. Isso registra o complemento no Cérebro remoto, mas não o acrescenta ao pacote B2 original. Nenhum upload extra nesta rodada.

Novo recado informado enviado somente ao Telegram privado do Miguel, confirmação `message_id=40`, para mediação com o DS-N. Não é resposta, aprovação ou ordem de execução do tutor. Revisão independente do recado: sem erro material. Nenhum arquivo retirado.
