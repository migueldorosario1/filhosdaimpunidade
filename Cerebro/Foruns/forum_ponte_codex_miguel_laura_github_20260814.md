# Fórum — Ponte Codex MIGUEL ↔ Codex LAURA via GitHub

**Pedido de Miguel:** 14/08/2026, 09:57 BRT.

## O que já existia

O Cérebro já registrava os dois computadores e o transporte pelo repositório
privado `cerebro-miguel`: MIGUEL envia automaticamente e LAURA recebe por
`git pull`. Também existia a ponte Claude↔Grok, com filas append-only. Não havia,
porém, uma caixa própria e um contrato operacional Codex↔Codex para os dois
computadores.

## O que foi criado

A ponte vive em:

`Cerebro/Foruns/ponte_codex_miguel_laura/`

Em vez de ambos alterarem uma fila única, cada recado é um arquivo novo e
imutável. MIGUEL escreve em `mensagens/para_laura/`; LAURA escreve em
`mensagens/para_miguel/`. Respostas referenciam o arquivo anterior. Esse desenho
reduz conflitos de merge e permite que qualquer sessão nova recupere o contexto
somente com `git pull` e leitura da pasta.

## Fase atual

Fase 1 é manual e segura: pull, leitura, nova mensagem, commit e push. Nenhum
cron foi autorizado em LAURA. A automação só será avaliada depois do primeiro
teste ponta a ponta.

O primeiro pedido já foi criado para LAURA. A ponte será considerada homologada
quando a resposta aparecer em `mensagens/para_miguel/` por um commit feito no
computador LAURA.

## Adendo — Trindade completa em LAURA, 11:34 BRT

Após a homologação Codex↔Codex, Miguel ampliou a ponte para os três CLIs de
LAURA: Codex, Claude e Grok. A versão 2 mantém mensagens imutáveis e acrescenta
identidade por agente, executor único por tarefa, commit contendo somente o
arquivo próprio e lock PowerShell para serializar qualquer operação Git no
clone compartilhado. Carta canônica:
`carta_trindade_ponte_laura_github_20260814.md`.

## Adendo — sincronização contínua blindada, 23:29 BRT

Após os três ACKs chegarem, foi corrigida a corrida dos crons MIGUEL↔GitHub. As
duas direções agora usam lock comum e horários defasados; commits locais são
enviados mesmo sem nascer um commit novo na rodada, e falha temporária de DNS
não impede que o último clone confirmado chegue ao Cérebro. Validação final:
divergência `0/0` e três ACKs de LAURA presentes no canônico. Detalhes em
`forum_correcao_sync_cerebro_github_20260814.md`.
