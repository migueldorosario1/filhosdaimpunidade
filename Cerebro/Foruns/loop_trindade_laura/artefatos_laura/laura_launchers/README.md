# Lançadores da Trindade LAURA

Scripts para iniciar os três agentes do computador LAURA já dentro do
cérebro (`C:\Users\migue\cerebro-miguel`), retomando a última sessão e
disparando `loop laura` automaticamente.

| Script | Agente | Comando usado |
|---|---|---|
| `laura_claude.cmd` | LAURA-CLAUDE (chefe) | `claude --continue "loop laura"` |
| `laura_codex.cmd` | LAURA-CODEX | `codex resume --last "loop laura"` |
| `laura_grok.cmd` | LAURA-GROK | sessão interativa (capas V4 + observador) |
| `loop_laura_grok.ps1` | LAURA-GROK | ronda 1h :51 (Task Scheduler `LoopLauraGrok`) |
| `laura_trindade.cmd` | os três de uma vez | abre três janelas, com 5 s de intervalo |

## Comportamento

1. Cada script entra no diretório do cérebro antes de abrir o CLI — assim o
   agente lê seu arquivo de instruções (`CLAUDE.md`, `AGENTS.md`, `GROK.md`)
   e sabe onde está tudo.
2. `--continue` / `resume --last` retoma a conversa anterior com todo o
   contexto. Se não existir sessão anterior (primeira vez, ou histórico
   limpo), o script cai no modo novo com o mesmo prompt `loop laura`.
3. O prompt `loop laura` segue o protocolo canônico de
   `cerebro/Foruns/loop_trindade_laura/README.md`: o agente confere os três
   ACKs `PRONTO`, roda um ciclo real e ativa a recorrência de 30 minutos.
   Além do contexto da sessão retomada, o estado das tarefas vive no Git
   (rondas, caixas `controle/`), então nada se perde entre sessões.
4. O intervalo de 5 s no `laura_trindade.cmd` reduz disputa pelo lock
   `%USERPROFILE%\.ponte-laura-git.lock` na largada.
5. **Loop de capas (Emenda 4):** Task Scheduler `LoopLauraGrok` dispara
   `loop_laura_grok.ps1` a cada hora na marca :51. O script pula se o
   heartbeat de `grok_laura.md` tiver menos de 40 min (o `/loop` Grok
   já rodou). Runbook em
   `cerebro/Foruns/loop_trindade_laura/controle/loop_laura_grok_RUNBOOK.md`.

## Opcional: iniciar com o Windows

Para a Trindade abrir sozinha no logon, copie um atalho de
`laura_trindade.cmd` para a pasta de inicialização
(`Win + R` → `shell:startup`). Não fazemos isso por padrão — decisão de
Miguel.
