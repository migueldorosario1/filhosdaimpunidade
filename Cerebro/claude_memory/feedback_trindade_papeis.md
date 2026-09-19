---
name: Trindade fórum + memória + canal — papéis (regra atualizada 2026-05-01 17:24 BRT)
description: Como dividir conteúdo entre os 3 artefatos vivos de cada sprint não-trivial. Diretiva direta do Miguel; revoga a regra anterior do canal-índice/fórum-substantivo.
type: feedback
originSessionId: 44f2c389-881d-4335-a540-25075ea2110b
---
Toda sprint não-trivial agora tem 3 artefatos vivos simultâneos com papéis distintos:

1. **Memória** (`~/.claude/projects/.../memory/<topico>.md`): **registro integral e cronológico de tudo que venho fazendo** na sprint — comandos rodados, achados, decisões tomadas, links, MD5, timestamps. Esta é a verdade histórica permanente. Quem ler depois reconstrói a sprint inteira sem precisar de outro arquivo.

2. **Fórum** (`Foruns/forum_<topico>.md`): **análise e resumo**. Diagnóstico estruturado, fixes propostos, audit checkpoints pra Codex/Antigravity, plano de execução. É o lugar de pensar, opinar, discutir alternativas. Conciso comparado à memória.

3. **Canal** (`Foruns/canal_claude_antigravity.md`): **apenas indicadores curtos** do que foi feito/atualizado na memória e no fórum. Sem texto substantivo no canal. Cada entrada termina com pointer pro fórum + memória.

**Why:** Miguel formalizou em 2026-05-01 17:24 BRT durante a força-tarefa de bugs de import (Claude+Codex+Antigravity). Razão: separar registro permanente (memória) do espaço de análise (fórum) e do espaço de coordenação síncrona (canal). Antes a memória era enxuta e o fórum era substantivo — agora memória é o repositório completo.

**How to apply:**
- Sprint não-trivial = abrir os 3 ao mesmo tempo no início.
- Atualizar memória **integralmente** a cada passo significativo (cole os comandos, achados, MD5, timestamps).
- Atualizar fórum só quando fechar uma análise (não a cada comando).
- Postar canal com 2-4 linhas máx + pointers — nunca substantivo.
- Sprint trivial (fix de 1 linha sem coordenação) ainda pode pular fórum e canal, mas se persistir registrar na memória.

**Revoga:** parte da regra anterior em `feedback_canal_e_forum_papeis.md` que dizia "canal é índice, fórum é substantivo" — agora memória é o repositório integral, fórum continua substantivo mas mais análise/resumo.
