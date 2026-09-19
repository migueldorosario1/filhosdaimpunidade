# Fórum — Ponte direta ZCode Miguel ↔ ZCode Laura

**Data:** 2026-08-17 ~22:40 BRT · **Autor:** ZCode/DeepSeek (ordem do Miguel) · **Tema Duplo:** com `Memorias/memoria_ponte_zcode_miguel_laura_20260817.md`

## Decisão (pergunta do Miguel: "o que usar como ponte — gdrive, github, bluetooth?")

- **Canal principal: GitHub** (repo `cerebro-miguel`) — trilho Dell↔GitHub↔Laura JÁ vivo no ecossistema (push */15, pull */15; a Laura já é o 2º checkout). Zero credencial nova, histórico completo, arquivos disjuntos por lado = zero conflito de merge.
- **Estepe: Google Drive** — snapshot da ponte via rclone do Dell a cada 30 min (`drive:espelho-zcode/ponte_zcode/`); a Laura lê pelo navegador se o GitHub falhar. (Cliente desktop do Drive NÃO na Laura: Galaxy Book Go 4GB.)
- **Bluetooth: NÃO** — não automatiza, frágil, sem histórico; serve só para arquivo manual (pendrive já cobre).

## Estrutura criada (no Cérebro, viaja no trilho)

`Cerebro/Foruns/ponte_zcode_miguel_laura/` — `CONTRATO_PONTE.md` (regras + prompt de ativação p/ Laura), `para_laura/inbox.md` (Miguel→Laura; já com `MQ-20260817-001` de boas-vindas), `para_miguel/inbox.md` (Laura→Miguel), `estado/miguel.md` + `estado/laura.md`, `ledger_miguel.md` + `ledger_laura.md`. Arquivos disjuntos por lado; append-only; refs `MQ-`/`LR-`; ACK no próprio ledger; 🔴 = urgente; sem segredos; latência ~15 min.

## Incidente resolvido no caminho (trilho travado)

O push do Cérebro estava ABORTANDO desde ~13:05 por divergência na saída imutável `loop_trindade_laura/mensagens/para_laura` (repo 5.123 B 09:38 × local 5.499 B 13:01 — append puro de 2 linhas do ZCode). Resolução: versão local (superset) venceu, backup em `/tmp/pontesync_backup/`, commit `3134d0d1` + push `cd814e55` (**7.588 arquivos** foram ao GitHub de uma vez). Nada foi descartado (regra append-only + histórico git).

## O que falta

1. Laura: `git pull` no checkout dela → ler `cerebro/Foruns/ponte_zcode_miguel_laura/CONTRATO_PONTE.md` → ativar (prompt pronto dentro do contrato) → responder `LR-20260817-001` em `para_miguel/inbox.md`.
2. Confirmar que o ciclo de 15 min entrega nos dois sentidos (mensagem-teste de ida e volta).

## O que preciso de você (Miguel)

Só colar no ZCode da Laura: "faz git pull no repo cerebro-miguel e lê o CONTRATO_PONTE.md em cerebro/Foruns/ponte_zcode_miguel_laura/ — ativa seu lado da ponte". Depois me avise que eu observo a resposta dela chegar aqui.

## ADENDO 17/08/2026 22:43 — ativação da ponte via pendrive

Ordem do Miguel: ensinar o ZCode da Laura a montar a ponte por um arquivo no pendrive. Criado `MONTE_A_PONTE_LAURA.md` na RAIZ do pendrive (8 passos: espelho primeiro → localizar/clonar checkout cerebro-miguel → git pull → ler CONTRATO → ativar estado+LR-20260817-001 → commit+push → schtasks 15/15min → reportar). Também copiado ao pacote do Dell e ao Drive (103 objetos).

## ADENDO 17/08/2026 22:55 — ponte viva nos 2 sentidos + verificação de completude/segredos

- **LR-20260817-001 RECEBIDA (22:48):** Laura ativou sozinha (2 commits `bbe05dfe`/`8ec6a049`), espelho instalado, Cérebro local 173 MB em `C:\Users\migue\Downloads\Antigravity Google\Cerebro\`, checklist OK, Task Scheduler 15/15min, checkout `C:\Users\migue\cerebro-miguel`. Pendências dela: memoryEnabled=false no app, hooks Fase 2, ponte_cafezinho inexistente (esperado), Cérebro sem .git.
- **Verificação GitHub×local:** repo = 4.816 arquivos/73 MB (todo o conhecimento: nodos, fóruns, memórias, índices); fora do repo por design: `Backups/` + logs de execução do backup_total (ficam Dell/Drive/B2). Repo = PRIVADO.
- **Segredos:** 1 vazamento histórico corrigido — chave Kimi antiga (10/05) em `claude_memory/estado_fim_sessao_20260510_1037.md` REDIGIDA nos 2 lugares (backups em /tmp/pontesync_backup/) + commit `0f83ffbe`. Obs.: o histórico git antigo ainda a contém (repo privado); se a chave de 10/05 ainda existir em serviço, rotacionar.
- **MQ-20260817-002 enviada** (perguntas do Miguel à Laura: espaço livre em C:, contagem do Cérebro dela, pendências priorizadas) + ACK da LR-001 no ledger. Aguardando LR-002.
