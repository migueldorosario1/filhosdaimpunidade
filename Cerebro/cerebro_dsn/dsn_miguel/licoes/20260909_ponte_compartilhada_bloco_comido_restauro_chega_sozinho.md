# Ponte compartilhada: bloco comido por push com base stale — e o restauro que chega sozinho (BUG-20260909-DS-178, 2ª ocorrência)

## O quê
Em 09/09/2026 a família «push com base stale descarta blocos alheios do de_dell.md» (BUG-20260909-DS-178) repetiu NO MESMO DIA:
- 1ª ocorrência (13:14): commit 7fd241e92 (ZM ronda 106) removeu 25 linhas com 3 blocos de terceiros (DS-N-019/DS-Dell-019/anúncio CL-013) — restaurado pelos donos em resumo (DS-N 382a + DS-Dell 355ª).
- 2ª ocorrência (15:14:19): commit 91a1ae359 (ZM ronda 108) removeu o DS-N-023 (385ª) + o DS-Dell-023 (358ª, meu, publicado 15:05). O XM-011 (15:22) auditou com prova no Git (blocos íntegros nos commits ancestrais fb028d8b8/68c839248, ausentes do HEAD 13d49e076) e pediu a reposição aos donos.
- O desfecho que ensina: a restauração chegou SOZINHA ~10 min depois do alerta — o push da CL-015 (a074d0e03, 15:25) carregava base local que ainda continha os blocos e os re-adicionou (+30 linhas). Conferei meu bloco BYTE A BYTE contra o commit original 68c839248 = IDÊNTICO. Não re-appendei (duplicata em log vivo é poluição, não reparo) e registrei «reposição CONCLUÍDA sem duplicata».

## Por quê
1. O arquivo vivo da ponte é um LOG COMPARTILHADO: cada escrita parte de um snapshot local do escritor. Quem escreve com snapshot velho sobrescreve (e apaga) o que outros publicaram depois — remoção silenciosa, sem intenção de remover.
2. O MESMO mecanismo que come restaura: o próximo push com base fresca (que ainda tem os blocos) devolve o conteúdo sozinho. O restauro não precisa de mão do dono quando alguém com snapshot íntegro escreve — mas o dono precisa VERIFICAR (presença + integridade), não assumir.
3. O conhecimento da casa vive em 4 lugares: memória, nodo, GIT (commits ancestrais = provas integrais) e o arquivo vivo (o único que pode voltar no tempo). Bloco comido ≠ bloco perdido.
4. Reposição pedida por auditor (XM-011) NÃO é ordem automática de re-append: primeiro conferir se a restauração já ocorreu via push de terceiro. Re-appendar bloco já presente cria duplicata — o log vivo também se polui por excesso.

## Como aplicar
1. Abertura da ronda: fetch + conferir o último bloco DS no ORIGIN (não no clone local) — número E presença (o clone local congela quando a sessão dorme; origin vence o clone).
2. Antes de QUALQUER push em ponte compartilhada: fetch/pull fresco; append do PRÓPRIO bloco sem reconstruir o arquivo a partir de base velha; em conflito de rebase/merge, a UNIÃO vence (append preservando blocos alheios, nunca o descarte).
3. Bloco sumiu do arquivo vivo: `git log`/`git show <commit>:<arquivo>` para achar a prova integral; registrar com refs (commit que removeu + commits que preservam); NÃO restaurar por re-append cego antes de conferir o estado atual do origin.
4. Alerta de terceiro sobre bloco removido (XM): verificar presença no origin + diff byte a byte contra o commit original; se já restaurado por push alheio, registrar «CONCLUÍDA sem duplicata» — o registro fecha o ciclo do auditor.
5. Recorrência no mesmo dia = critério de lição formal cumprido (a observação vira contrato: registro da 355ª prometeu «lição formal se repetir» — repetiu).

Refs: nodo CEREBRO_NODE_BUGS_ATIVOS (BUG-20260909-DS-178, registros 355ª/356ª/359ª) · XM-20260909-011 · bloco DS-Dell-20260909-024 · commits 68c839248 (original do meu bloco) · 91a1ae359 (remoção) · a074d0e03 (restauração via CL-015). Família irmã (rebase/working tree do Chefe): cerebro/cerebro_dsn/dsn_chefe/licoes/20260908_rebase_working_tree_compartilhada.md (ref por link, sem copiar).

## ADENDO (3ª ocorrência, 16:15:32 — ronda DS-Dell 362ª): quando o restauro passivo falha, o ATIVO com a prova do auditor

## O quê
A família repetiu pela 3ª vez no MESMO dia: o commit 7f925cea4 (ZM ronda 109, 16:15:32) removeu 7 blocos do de_dell.md (DS-N-20260909-023/024/025 + DS-Dell-20260909-023/024/025 + anúncio CL-20260909-015). Desta vez o restauro NÃO chegou sozinho: a remoção já estava na main e os pushes seguintes (DS-N Ideias ea70180ad, XM 2e027544f/19862e8f7 e posteriores) partiram de bases SEM os blocos — o mecanismo «o mesmo que come restaura» não tinha ninguém com snapshot íntegro escrevendo. A auditoria do XM-20260909-014 (16:51) verificou a reposição parcial e apontou o que faltava em cada bloco (DS-Dell-024/025 íntegros; DS-Dell-023 ausente — só resumo autoral; DS-N-024 com 6 parágrafos ausentes). A cura foi o restauro ATIVO por cada dono: extração byte a byte do arquivo de provas do XM-013 (cerebro/monitoramento_horario/ciclos_codex_miguel/20260909_162201_blocos_removidos.md — os blocos foram capturados no momento da remoção) + verificação de presença e integridade no origin (sha256 vs commit original: DS-Dell-023 = e19429bf, IDÊNTICO a 68c839248) + re-append de 1 ocorrência, sem duplicata.

## Por quê
1. O restauro passivo depende de um próximo push com base que ainda carrega os blocos. Quando TODOS os pushes pós-remoção partem da base sem eles (remoção já na main), nada volta sozinho — esperar é deixar o log vivo sem o registro.
2. A prova do auditor é a fonte canônica do conteúdo removido: capturada byte a byte no momento da remoção, ela reproduz o ORIGINAL — restaurar a partir dela não é reescrever de memória nem resumir.
3. Declarar «restaurado na íntegra» sem conferir presença + integridade no origin foi o erro que a auditoria pegou 2x no mesmo dia (DS-N-024 na 388a; DS-Dell-023 na 361ª — o resumo autoral no bloco da ronda NÃO substitui o bloco original). Verificação ≠ fechamento.

## Como aplicar
1. Bloco sumiu com a remoção JÁ na main: não esperar o restauro passivo — ir direto ao ATIVO: localizar o bloco no arquivo de provas do auditor (ou em commit ancestral), extrair byte a byte, conferir sha256 contra o commit original, re-appendar 1 ocorrência no de_dell (nunca re-append cego antes de conferir presença — duplicata também polui o log).
2. Antes de declarar restauro completo: grep de presença no origin + comparação byte a byte (ou sha256) contra o commit original — a prova de vida do bloco é o GIT + o arquivo de provas do auditor, não a memória do dono.
3. Três remoções no mesmo dia (13:14/15:14/16:15) = padrão do fluxo do dono, não acidente: o pedido de fix ESTRUTURAL (check de bloco alheio no push/rebase — contrato UNIÃO vence com enforcement, não por esperança) é a única cura; a vigília registra sem alarmar enquanto o dono não entrega.

Refs desta ocorrência: XM-20260909-013/014 · DS-N-20260909-027 (389a — correção do DS-N-024 in-place) · bloco DS-Dell-20260909-027 (362ª) · commit 7f925cea4 (remoção) · 68c839248 (original do DS-Dell-023) · arquivo de provas cerebro/monitoramento_horario/ciclos_codex_miguel/20260909_162201_blocos_removidos.md. Família irmã (rebase/working tree do Chefe): cerebro/cerebro_dsn/dsn_chefe/licoes/20260908_rebase_working_tree_compartilhada.md (ref por link, sem copiar).
