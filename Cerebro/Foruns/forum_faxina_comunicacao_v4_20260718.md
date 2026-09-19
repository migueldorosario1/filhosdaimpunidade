# Faxina segura da comunicação V4 — 18/07/2026

## Correção e rotação total — 10:23:35 BRT

Por decisão de Miguel, a faxina deixou de ser apenas preventiva e passou a ser total. O Canal de 717 linhas e todos os inboxes foram retirados da área ativa depois de backup integral. Foram reabertos como janelas limpas para a nova rodada.

**Backup canônico com data e hora:** `Backups/rotacao_comunicacao_v4_20260718_102335/`.

O backup contém 165 arquivos e inclui o estado anterior, o Canal completo, todos os inboxes, os índices e a etapa preliminar. Comparações byte a byte do Canal atual anterior e de sua cópia original retornaram igualdade antes da rotação.

**Responsável:** Codex  
**Sessão:** `CODEX-V4-FAXINA-20260718-1030`  
**Princípio:** reorganizar sem apagar e preservar retomada.

## Executado

1. Backup integral anterior a qualquer movimentação: Canal, índice e toda a pasta dos inboxes.
2. Retirada de 58 anexos/artefatos da pasta de mensagens; foram movidos para arquivo recuperável.
3. Rotação preventiva do inbox do Grok, que estava com 500 linhas.
4. Rotação do índice semanal, que estava com 328.462 bytes e 4.992 linhas.
5. Abertura de inbox e índice novos, leves, com ponto de retomada e ponteiros para o histórico.
6. Canal Trindade preservado sem rotação: estava com 37.701 bytes e 717 linhas, abaixo dos limites.
7. Fórum Central convertido em índice leve: uma resenha curta por fórum, sem discussão interna.
8. Fóruns temáticos históricos acima do limite foram marcados no índice como consulta, não continuação.

## Local recuperável

`arquivo_operacional/limpeza_20260718_1030/`

Contém:

- `backup_integral/` — cópia completa do estado anterior;
- `anexos_retirados_do_inbox/` — PDFs, imagens, HTML, código, dados e pesquisas;
- `grok_inbox_pre_rotacao.md` — inbox integral anterior;
- `INDICE_FORUNS_SEMANAL_pre_rotacao.md` — índice integral anterior.
- `forum_central_reforma_v4_pre_indice_leve_20260717.md` — fórum central anterior à conversão em índice puro.

## Regra daqui em diante

Inbox é comunicação Markdown entre agentes. Materiais de trabalho devem ficar em labs, dados, anexos ou fóruns próprios, com apenas um ponteiro no inbox.

O Fórum Central contém somente ponteiro e resenha curta. Cada assunto tem fórum próprio. Ao atingir 30 KB ou 600 linhas, o fórum temático é encerrado com resumo e ganha continuação numerada.
