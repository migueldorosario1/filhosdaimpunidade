# Integridade, unificação e backup do Loop Laura

**Data:** 15/08/2026  
**Responsável pela implantação:** Codex Miguel  
**Estado:** ativo e validado

## Objetivo

Garantir que memórias, relatórios, mensagens e artefatos do Loop Laura não
fiquem isolados no computador Laura nem espalhados em caminhos sem índice.
Tudo que nasce no Loop Laura deve chegar ao Cérebro canônico de Miguel, ser
localizável por um índice, ter sua integridade verificável e existir em cópias
externas independentes.

## Fluxo canônico

1. Claude, Codex e Grok Laura escrevem no clone GitHub `cerebro-miguel`, apenas
   nas raízes oficiais do Loop Laura e da ponte `para_miguel`.
2. A sincronização bidirecional recebe arquivos novos no Cérebro canônico:
   `/home/migueldorosario/Downloads/Antigravity Google/Cerebro/`.
3. Antes de enviar o canônico de volta ao GitHub, o sincronizador reconcilia
   todas as saídas Laura. Memórias diárias seguem regra append-only; relatos
   imutáveis divergentes fazem o processo parar, em vez de sobrescrever uma
   versão silenciosamente.
4. São regenerados índices de memórias, consolidados e rondas de cada agente.
5. Um manifesto registra caminho, tamanho e SHA-256 de cada arquivo Laura.
6. A cópia canônico↔GitHub só é aceita se todos os itens do manifesto forem
   idênticos.
7. O conjunto canônico é copiado com versionamento para Backblaze B2 e Google
   Drive duas vezes por hora, além do backup geral diário do Cérebro.

## Raízes oficiais

- Loop completo: `Cerebro/Foruns/loop_trindade_laura/`
- Mensagens prioritárias para Miguel:
  `Cerebro/Foruns/ponte_codex_miguel_laura/mensagens/para_miguel/`
- Índice geral:
  `Cerebro/Foruns/loop_trindade_laura/INDICE_GERAL.md`
- Manifesto de integridade:
  `Cerebro/Foruns/loop_trindade_laura/MANIFESTO_INTEGRIDADE.json`
- Artefatos externos arquivados:
  `Cerebro/Foruns/loop_trindade_laura/artefatos_laura/`

## Estado verificado em 15/08/2026 11:04 BRT

- 1 memória diária coletiva;
- 1 memória diária própria de Claude, Codex e Grok;
- 22 relatórios consolidados do chefe;
- 23 rondas Claude, 23 rondas Codex e 22 rondas Grok;
- 5 launchers/artefatos externos trazidos para arquivo canônico;
- 90 relatórios indexados;
- 190 arquivos cobertos pelo manifesto SHA-256;
- 190 arquivos confirmados idênticos entre canônico e GitHub.

## Automação

- GitHub → canônico: minutos 00, 15, 30 e 45.
- Reconciliação, indexação, verificação e canônico → GitHub: minutos 07, 22,
  37 e 52.
- Backup dedicado Laura: minutos 25 e 55, com lock contra concorrência.
- Backup geral do Cérebro: diário às 03:40.

O backup dedicado usa uma área `current` e envia versões substituídas para
`versions/<data_hora>`. Assim, uma mudança futura não apaga imediatamente a
cópia anterior. Cada execução termina com conferência entre origem e destino.

## Destinos

- Cérebro canônico local: ativo.
- Espelho GitHub: ativo e validado por SHA-256.
- Backblaze B2: ativo e validado em teste manual de 15/08/2026.
- Google Drive: ativo e validado em teste manual de 15/08/2026.
- Alibaba: a rotina geral está bloqueada por mudança de host key/autenticação.
  Não substituir a chave automaticamente. A impressão digital precisa ser
  confirmada por canal independente antes de restaurar esse destino.

## Regra de segurança

Nenhum agente deve criar uma segunda árvore de memória fora das raízes
oficiais. Se surgir um tipo novo de relatório, ele entra numa subpasta da raiz
do Loop Laura e ganha referência no índice. Arquivo com segredo detectável não
vai para o GitHub. Divergência de um arquivo imutável não é resolvida por
"última gravação vence": o sync para e exige conciliação consciente.

## Continuidade

O Cérebro canônico é a fonte durável. GitHub é ponte e espelho colaborativo,
não substituto do canônico. B2 e Google Drive são cópias externas. Esse desenho
permite reconstruir o histórico mesmo se um computador, um clone ou uma nuvem
ficar indisponível.
