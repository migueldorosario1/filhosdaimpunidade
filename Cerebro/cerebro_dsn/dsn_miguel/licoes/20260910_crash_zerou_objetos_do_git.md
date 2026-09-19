# Lição 20260910 — O crash zerou 26 objetos do git: arquivo vazio com data não é arquivo apagado

**O quê (fato, com prova).** Na abertura da ronda 396ª DS-Dell (10/09/2026 13:35 BRT), encontrei o repo canônico `~/cerebro-miguel` **cego para commit**: `git status`/`log`/`commit` morriam com `fatal: loose object 6c459414c2d8fb6bc0e4725db1700e3188da9dcf is corrupt`. Investigação (só leitura): **26 objetos do `.git/` com 0 byte** (5 commits, 16 trees, 5 blobs) e **5 arquivos de trabalho zerados** — todos com mtime **13:21:53**, numa **rajada de 150 ms**. O commit do **HEAD local** era um deles. `last -x` mostrou **`crash` às 13:26** (2 d 18 h de uptime, sem shutdown registrado); **não há journal persistente** — o boot anterior não existe em `journalctl`. Os objetos zerados são **exatamente os escritos 6 s antes da queda** (a ronda horária da ASTRA, 13:21:19–13:21:47).

**Por quê (causa-raiz).** **Desligamento sujo.** Com ext4 `ordered` + alocação retardada, o **metadado** (mtime/size) chegou ao disco e o **conteúdo** que estava no page cache não → o arquivo existe, datado e vazio. Não é script, não é agente, não é remoção e não é disco defeituoso. O falso amigo do diagnóstico: o `mount` do meu sandbox mostra `/` como **`ro` (`bwrap --ro-bind / /`)** — o «read-only» era **a minha jaula**, não o disco (é o BUG-194).

**Como aplicar (régua).**
1. **Arquivo de 0 byte com mtime recente não é arquivo apagado: é arquivo que nunca chegou ao disco.** Zeragem em rajada (mtime quase idêntico em muitos arquivos) é assinatura de queda, não de remoção.
2. **Cruze os mtimes com o kernel antes de acusar alguém**: `last -x`, `journalctl -b -1`, `uptime`. Se não há recibo de erro no kernel e a máquina reiniciou sozinha, o suspeito é o desligamento.
3. **Antes de declarar perda, verifique o REMOTO objeto por objeto**: clone em scratch + `git cat-file -t <hash>` nos zerados. Aqui deu **26/26 recuperáveis** no `origin/main` — a perda era só da cópia local.
4. **Só depois conserte, e sem apagar**: mover os 0 byte para **quarentena**, `git fetch origin`, `update-ref`/fast-forward, `reset --mixed` (a árvore de trabalho **não** é tocada) e `checkout` dos arquivos zerados. **Nunca `reset --hard` nem `clean`** num repo compartilhado com trabalho não commitado.
5. **Se a sua física não escreve fora do workspace, diga isso e entregue a receita** — o diagnóstico é meu, a aplicação é do dono do host; o meu caminho de escrita é o clone scratch do workspace.

**Ref:** bloco DS-Dell-20260910-022; BUG-20260910-DS-196 (novo) e atualização do BUG-20260910-DS-194.
