---
name: Auto-alocar em slot livre + reportar mapa de slots no início da sessão
description: Múltiplas sessões Claude Code rodam em paralelo (slots abertos 1, 2, 3, ... N). Cada sessão lê `Projeto Cafezinho Agentes/Tarefasdeagora.md`, auto-aloca num slot livre/concluído ou abre um novo, e reporta o mapa antes de tocar código.
type: feedback
originSessionId: 3fe330c3-19fc-40ae-a8cb-5d6a13d594a3
---
## Regra (atualizada 2026-04-26)

No início de **toda** sessão, **antes de tocar em qualquer arquivo**, seguir o ritual de despertar:

1. Ler `Projeto Cafezinho Agentes/Tarefasdeagora.md`.
2. Auto-alocar num slot 🟢 LIVRE ou ✅ CONCLUÍDO (reciclável). Se todos tomados, **abrir um slot novo** (próximo número disponível).
3. Reportar mapa: *"Slot 1 é X. Slot 2 é Y. Slot 3 ✅ concluída — assumi o lugar e proponho Z. Slot 4 é W. Vou tocar Z, ok?"*
4. Marcar o slot como 🔵 EM ANDAMENTO + carimbar timestamp + nome curto.
5. Antes de codar, ler o **fórum md** vinculado ao slot (sempre em `Foruns/` na raiz).

## Why

Diretiva Miguel 2026-04-25 ~10:50 BRT durante sessão da Tarefa 3 (agente comentaristas). Múltiplas sessões Claude Code rodam em paralelo. Sem coordenação explícita há risco de:
- Duas sessões tocando o mesmo arquivo simultaneamente
- Atravessar a "ordem de execução" definida por Miguel pra outro slot
- Antigravity já cria conflito o suficiente (memória `coordenacao_crontab_deploy.md`); somar mais sessões Claude sem identificação seria caótico

**Atualização 2026-04-26 09:12 BRT:** Miguel aboliu o cap de 4 slots. Sistema passa a ter **slots abertos** (1, 2, 3, ... N). Quando todos os existentes estão tomados, abre-se um novo número.

## How to apply

1. **Primeira ação obrigatória da sessão:** ler `Tarefasdeagora.md` E auto-alocar num slot disponível (ou abrir um novo).
2. Reportar o mapa de cara — Miguel pode redirecionar.
3. Focar SÓ no escopo do slot atribuído.
4. Quando avançar passos, **atualizar `Tarefasdeagora.md`** marcando ✅ e movendo cursor pra próximo.
5. NÃO atravessar pra outro slot sem alinhar com Miguel.
6. Quando uma tarefa concluir: registrar em `memory/Tarefas_Legacy.md` + mover fórum dela pra `Foruns/legacy/` (resgatável a qualquer momento).

## Exceções

Auditoria/diagnóstico transversal ("o que o Antigravity fez essa noite?", "como tá o crontab?") não exige slot — Miguel pede direto. Nesses casos, avisar modo investigativo e não auto-alocar.
