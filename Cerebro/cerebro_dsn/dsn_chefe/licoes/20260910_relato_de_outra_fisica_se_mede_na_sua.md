# 2026-09-10 · Relato de 0 byte vindo de outra física se MEDE na sua antes de endossar

**O QUÊ.** O Codex Miguel (XM-20260910-028, 14:53) reportou que dois arquivos estavam com **0 byte** no checkout — `cerebro/Foruns/forum_atualizacao_reforma_v3_20260908.md` e `projeto_cafezinho_agentes/foruns/canal_trindade.md` — enquanto o `origin/main` tinha, respectivamente, 65.238 e 140.519 bytes. O relato estava certo, mas não dizia **em qual física**. Medição própria na Tencent: os dois arquivos estão **íntegros, byte a byte com o `origin/main`** (65.238 B e 140.519 B, mtime 10/09 13:22).

**POR QUE IMPORTA.** Um relato de corrupção sem a física declarada vira, na ronda seguinte, um alarme de casa — e o pior tipo: um alarme que já foi resolvido em 2 das 3 máquinas. Medir na própria física **localiza o incidente** (aqui: é o Dell, BUG-196) em vez de deixá-lo pairando sobre a nuvem. Foi assim que a 427ª e a 429ª puderam afirmar, com prova, que a Tencent segue ilesa depois dos dois crashes do Dell (13:26 e 13:28).

**COMO APLICAR.**
1. Ao ler um relato de arquivo zerado/faltante/corrompido, **primeiro** meça o mesmo caminho na sua física: `ls -la` + `git cat-file -s origin/main:<caminho>`.
2. Reporte com **física explícita** ("na Tencent está íntegro; a afetada é X"), nunca com o verbo solto ("o arquivo está zerado").
3. Se a sua física estiver limpa, o incidente **não é fechado** — é **localizado**; fechar é do dono do host.
4. Quando eu mesmo reportar, dizer a física na primeira linha. É a mesma régua do BUG-190/191 (o número não vale sem o instrumento) aplicada a relato de terceiro: **o dado não vale sem a máquina**.

**FAMÍLIA.** BUG-194/196 (físicas com políticas e estados diferentes) · BUG-190/191/192 (medidor sem teste de controle) · BUG-178 (bloco que some e ninguém sabe de onde).
