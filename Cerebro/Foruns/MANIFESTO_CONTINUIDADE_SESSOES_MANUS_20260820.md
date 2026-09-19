# Manifesto — Continuidade das sessões Manus no Cérebro

**Data:** 20/08/2026 09:21 BRT
**Autor do registro:** Manus
**Ordem:** Miguel
**Fórum relacionado:** `Foruns/forum_continuidade_sessoes_manus_20260820.md`
**Alvo canônico:** `cerebro/`

## Princípio

O Cérebro é a memória canônica do ecossistema. A continuidade não deve depender da memória implícita de uma sessão de chat. Ela deve ser reconstruída a partir de documentos versionados, fóruns, manifestos, memórias e índices com ponteiros verificáveis.

> Uma decisão só está disponível para a próxima sessão quando foi registrada no Cérebro com contexto suficiente para ser retomada sem adivinhação.

## Estrutura mínima de cada sessão

| Artefato | Local | Quando usar | Conteúdo mínimo |
|---|---|---|---|
| Fórum | `cerebro/Foruns/forum_<assunto>_<AAAAMMDD>.md` | Toda sessão com descoberta, decisão, diagnóstico ou pendência relevante | Objetivo, fatos, decisões, ações, pendências, riscos e referências |
| Manifesto | `cerebro/Foruns/MANIFESTO_<assunto>_<AAAAMMDD>.md` | Mudança de regra, processo, arquitetura, automação ou governança | Escopo, regra, arquivos, testes, rollback, limites e autorização |
| Memória | `cerebro/Memorias/memoria_<assunto>_<AAAAMMDD>.md` | Conhecimento durável que deve sobreviver ao fórum | Estado consolidado, decisões vigentes, invariantes e retomada |
| Índice de fóruns | `cerebro/Foruns/INDICE_FORUNS_SEMANAL.md` | Sempre que um fórum ativo ou manifesto novo for criado | Ponteiro curto, estado e relação com a memória |
| Nó de atualizações | `cerebro/CEREBRO_NODE_ATUALIZACOES.md` | Sempre que houver uma mudança importante ou decisão transversal | Registro cronológico curto com evidência e ponteiros |

## Ritual de início

A sessão começa com o relógio real em BRT e a leitura de `cerebro/00_CEREBRO_CANONICO.md`. Em seguida, são lidos a minuta do contrato, o nó de memória de trabalho, o resumo ou boletim vigente e apenas os fóruns necessários para a tarefa. O agente deve distinguir estado atual medido de informação histórica, hipótese ou pedido ainda não autorizado.

## Ritual de encerramento

Antes de encerrar, o agente deve registrar o que realmente aconteceu, não o que pretendia fazer. O fórum guarda o contexto; o manifesto formaliza mudanças duráveis; a memória reduz o custo de retomada; os índices apontam para os documentos. O diff local deve ser revisado para eliminar segredos e duplicações. O repositório deve receber commit normal e push normal, sem reescrita da história.

Quando o Google Drive for utilizado como espelho, o registro deve indicar que o GitHub continua sendo a fonte canônica. Quando uma máquina ou canal estiver atrasado, o Drive pode servir como trilho paralelo, mas a reconciliação final deve voltar ao Cérebro.

## Limites

Este manifesto não autoriza publicação, deploy, criação de agendamentos, alteração de status editorial, alteração de WordPress, cópia de credenciais ou execução de failover. Ele define apenas o método de continuidade documental. Toda ação externa continua dependente da autorização específica e do contrato operacional correspondente.

## Critérios de qualidade

Um registro está completo quando outra sessão consegue identificar o objetivo, distinguir fatos de decisões, localizar a prova, saber o que não foi feito, retomar a pendência e conhecer o próximo passo sem precisar perguntar novamente pelo contexto básico. Se houver conflito entre documentos, a fonte mais recente e verificável deve ser investigada, e a divergência deve ser registrada em vez de escondida.

## Primeira aplicação

A primeira aplicação deste manifesto é o fórum `Foruns/forum_continuidade_sessoes_manus_20260820.md`, que registra a confirmação de acesso ao GitHub e ao Google Drive, a ausência de um pendrive montado neste ambiente, a inexistência de loop agendado nesta sessão e a localização da arquitetura do monitoramento GA4 no repositório `GA4-Manus`.

— Manus, 20/08/2026 09:21 BRT
