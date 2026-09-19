---
name: Trigger "retomar" — carrega último estado_fim_sessao e segue roteiro
description: Quando Miguel disser "retomar" (ou variações), Claude lê o último estado_fim_sessao_*.md e executa o roteiro de retomada que está lá.
type: feedback
originSessionId: 7c7867b0-668d-4c9f-9f68-fd2bf7f1ba99
---
Quando Miguel digitar **`retomar`** (ou variações: "retomar tarefa", "retomar onde paramos", "continuar"), Claude deve:

1. **Achar o estado mais recente:** procurar `estado_fim_sessao_*.md` mais novo na pasta `~/.claude/.../memory/`. Pode usar `ls -t` ou checar pelo `MEMORY.md` (último listado é o mais recente).

2. **Ler o arquivo completo** com a ferramenta `Read`.

3. **Reportar ao Miguel em 5-7 linhas:**
   - Marco principal da última sessão (1 linha)
   - 3-5 pendências mais importantes (com números/letras pra Miguel escolher por número)
   - Estado dos loops e sistema (1 linha)
   - Pergunta direta: "Por onde quer começar?"

4. **NÃO reativar loops automaticamente.** Esperar Miguel decidir se quer "ativar loop trindade" ou trabalhar on-demand.

5. **Antes de codar qualquer coisa**, Miguel precisa autorizar a frente específica que quer retomar.

**Why:** Sessão Claude Code não tem memória entre execuções. O arquivo `estado_fim_sessao_<DATA>.md` é o salvamento da partida — começou a ser usado em 2026-05-09 e tem 6 pendências numeradas + roteiro de retomada. Sem trigger formal, Miguel teria que digitar comandos detalhados toda vez.

**How to apply:**
- Variações que devem disparar: "retomar", "retomar onde paramos", "continuar de onde paramos", "voltar pra tarefa", "qual era a próxima coisa".
- A leitura é leve (1 arquivo de ~3KB), sem rituais pesados.
- Não confundir com "vai"/"vai lá" (que força ler canal e responder Trindade). "Retomar" é mais alto nível: dá visão da sessão anterior.
- Combinação útil: depois de "retomar", Miguel pode dizer "ativar loop trindade 10 em 10 min" se quiser modo autônomo.
