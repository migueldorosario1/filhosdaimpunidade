---
name: memoriaintegrada.md — ponte Antigravity ↔ Claude Code (LER SEMPRE)
description: Arquivo-manifesto na raiz do projeto que serve de ponto de encontro entre Antigravity e Claude Code. Ler no início de cada sessão.
type: reference
originSessionId: 73998c67-5991-4ca1-9fce-a85ef4b17e48
---
**Caminho:** `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/memoriaintegrada.md`

**O que é:** manifesto de colaboração entre as duas IAs que operam neste projeto (Antigravity/Gemini local + Claude Code). Criado por Antigravity em 2026-04-21. Contém o plano vivo de integração de memórias e quaisquer atualizações que o Antigravity deixe lá pra você.

**Como usar:**
1. **Ler no início de qualquer sessão nova** — pode conter instruções novas do Antigravity desde o último contato.
2. Comparar com o CLAUDE.md e o MEMORIA_PROJETO_CAFEZINHO.md (ambos na mesma pasta) pra entender o que está em fusão ou em divergência.
3. Se o arquivo pedir execução de plano (como fez em 21/04 com o esquema de rm + symlink), **AUDITAR antes de executar**. Regra da hierarquia vale (feedback_hierarquia_antigravity.md): Antigravity opina, Claude Code audita e codifica, Miguel decide. Auditar sempre.
4. Dúvidas de execução → gravar fórum (`forum<topico>hoje.md`) e aguardar resposta, conforme `feedback_duvida_vira_md_antigravity.md`.

**Histórico de interações registradas aqui:**
- 2026-04-21: Antigravity propôs fundir MEMORIA_PROJETO_CAFEZINHO.md dentro do CLAUDE.md + rm + `ln -s CLAUDE.md MEMORIA_PROJETO_CAFEZINHO.md`. Claude Code pausou, gravou `forumintegracaomemoriashoje.md` apontando 4 riscos (projeto sem git, semântica symlink + write sobrescreve CLAUDE.md, contradição com §9.4 Precaução Máxima, legibilidade). Propôs Proposta A (fusão + backup + redirect, sem symlink). Miguel vai alinhar o plano com Antigravity.

**Lembrete crítico:** ambos arquivos (CLAUDE.md e MEMORIA_PROJETO_CAFEZINHO.md) têm conteúdo exclusivo que NÃO pode ser perdido. Nenhum `rm` sem backup (`.bkp-YYYYMMDD`) em projeto sem git.
