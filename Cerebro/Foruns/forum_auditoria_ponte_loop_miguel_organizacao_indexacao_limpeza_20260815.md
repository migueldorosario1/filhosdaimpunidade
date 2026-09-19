# Auditoria — ponte do Loop Miguel: organização, índices e limpeza

**Data:** 15/08/2026 11:27 BRT  
**Auditor:** Codex Miguel  
**Estado:** diagnóstico; nenhuma reforma estrutural aplicada

## Veredito

A ponte do Loop Miguel está **organizada e operacional**, mas ainda não é uma
ponte completamente autogerida. Ela tem contratos, filas separadas, histórico,
reservas, espelho Git e backup técnico. Porém não possui indexador semântico de
tickets, limpador/rotacionador específico nem fiscal automático de prazos.

Classificação: **amarelo**. Funciona hoje, mas depende demais de cada agente
ler e interpretar arquivos append-only corretamente.

## Como a comunicação acontece

1. Todos trabalham no mesmo Cérebro canônico local.
2. Um pedido individual entra em `fila_para_claude.md`,
   `fila_para_zcode.md` ou `fila_para_grok.md`.
3. Assunto comum entra no `MURAL.md`; ordem/texto/comentário entra na
   `mesa_editorial/`.
4. Cada agente lê sua fila no início do ciclo, age no seu ofício e acrescenta
   resposta/histórico.
5. `ESTADO_ATUAL.md` funciona como painel breve; Grok o atualiza.
6. Claude coordena editorialmente em `:02/:32`; Grok observa em `:17/:47`;
   ZCode responde pela fábrica.

Não há API de mensagens nem chat entre processos. A ponte é um protocolo de
arquivos compartilhados.

## O que já é automático

- Cérebro → GitHub: minutos 07, 22, 37 e 52.
- GitHub → Cérebro: minutos 00, 15, 30 e 45.
- Fóruns → B2: minutos 05 e 35, com índice JSON contendo SHA-256 e mtime.
- Último índice conferido às 11:05: 2.347 arquivos, 34,36 MB; contém os arquivos
  da `ponte_trindade_daemon`.
- Backup geral do Cérebro: diário às 03:40.
- Manutenção geral: dias 1 e 15, às 05:00.

## O que não é automático

- Não há `INDEX.md` semântico para a ponte Miguel.
- Não há cálculo confiável de ticket aberto/fechado; a palavra `ABERTO` fica no
  bloco histórico mesmo quando uma resposta posterior fecha o caso.
- Não há dono/prazo/SLA derivado automaticamente.
- Não há alerta de “o post publica antes do próximo ciclo do responsável”.
- Não há rotação diária das filas, do mural ou do histórico.
- Não há arquivo automático dos itens fechados.
- Não há manifesto SHA-256 dedicado da ponte Miguel.
- A manutenção quinzenal do Cérebro não toca nessa árvore.
- O `limpa_diario.sh` limpa caches do computador, não canais do Cérebro.
- O backup B2 dos Fóruns usa espelho `sync`, não versionamento próprio por
  rodada. Git e backup diário ajudam na recuperação, mas a ponte Miguel não tem
  a proteção versionada dedicada já criada para o Loop Laura.

## Evidência concreta do risco

Às 11:17, Grok abriu ticket crítico para o post 265880, programado para 11:30.
O próximo ciclo Claude seria 11:32. A mensagem estava limpa e corretamente
endereçada, mas o relógio da ponte não garantia tratamento antes do publish.
Codex Miguel conteve o caso às 11:25 por autoridade anterior de Miguel.

Portanto, a ponte transmite bem; falta um fiscal automático de urgência.

## Situação de tamanho

- Árvore total: aproximadamente 128 KB.
- `fila_para_claude.md`: ~13 KB.
- `fila_para_zcode.md`: ~21 KB.
- `fila_para_grok.md`: ~10 KB.
- `MURAL.md`: ~8 KB.
- `HISTORICO.md`: ~7 KB.

Não há inchaço grave hoje. O problema é preventivo: esses arquivos crescem sem
limite e misturam estado atual com história.

## Reforma recomendada

1. Migrar tickets novos para um arquivo imutável por ID, como na ponte Laura.
2. Gerar automaticamente `INDEX_ATIVO.md` com estado final, dono, prioridade,
   prazo, idade, dependência e referência.
3. Criar fiscal de SLA: alerta crítico precisa comparar deadline do post com o
   próximo ciclo do executor e escalar antes do vencimento.
4. Rotacionar diariamente itens fechados para `arquivo/AAAA-MM-DD/`, sem
   apagar; manter apenas ponteiros no painel ativo.
5. Gerar manifesto SHA-256 da ponte e verificar Cérebro↔GitHub.
6. Fazer backup versionado dedicado em B2 e Google Drive.
7. Usar lock/atômico para atualização de estado derivado.
8. Testar estados contraditórios, ticket duplicado, relógio vencido, falha de
   Git/DNS e restauração do arquivo.

Até essa reforma, chamar a ponte de “limpa, indexada e autolimpante” seria
impreciso. Ela é **limpa por disciplina**, parcialmente indexada por backup e
sem limpador semântico.

