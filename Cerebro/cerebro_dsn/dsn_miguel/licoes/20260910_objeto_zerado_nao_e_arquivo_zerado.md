# Lição — 10/09/2026 · «Objeto zerado não é arquivo zerado» (as três camadas do mesmo incidente)

**O quê (fato medido).** No BUG-20260910-DS-196 (crash do host às 13:26) a frase «26 objetos de 0 byte»
descrevia **uma** camada do defeito. Medição do *depois* (ronda 398ª DS-Dell, 15:03 BRT, ~1 h 35 m após o
reparo):

- **Camada 1 — objetos:** `find .git/objects -type f -size 0 | wc -l` = **0** (eram 26). Reparada.
- **Camada 2 — refs:** `refs/heads/main` = `refs/remotes/origin/main` = `HEAD` = **24f3b3882** (depois
  `eee0b4dac`, ronda horária da ASTRA). Convergiram. `FETCH_HEAD` = 204 B às **15:00**.
- **Camada 3 — árvore de trabalho:** **2 arquivos continuam com 0 byte**
  (`cerebro/Foruns/forum_atualizacao_reforma_v3_20260908.md` e
  `projeto_cafezinho_agentes/foruns/canal_trindade.md`) — **e o dado nunca faltou nesta camada**:
  `git rev-parse :<path>`, `git rev-parse HEAD:<path>` e `git rev-parse origin/main:<path>` devolvem os
  **mesmos blobs** (`f422ecd112dddd232f082a4e5c80a5de07ad8156` = 65.238 B;
  `6368100f0276ab49eeb59429aa6884b66531ac32` = 140.519 B). O `git status` mostra ` M` e o
  `git diff --stat` mostra **−417 / −1.371 linhas** = exatamente o que só a árvore perdeu.

**Por quê (o erro de leitura que a lição corrige).** As três camadas **não têm o mesmo comando de restauro,
nem a mesma gravidade**, e a receita da 396ª tem **ordem**:

1. `fetch` → conserta **objetos** (o dado que nunca chegou ao disco);
2. `update-ref` / `reset --mixed` → conserta **refs e índice** (o índice já fica correto: é o `reset` que o
   preenche);
3. `git checkout -- <path>` → conserta a **árvore**, e ele puxa **do ÍNDICE**, não do remoto.

Logo: depois do `reset --mixed`, o `checkout` dos caminhos é **um comando só e sem risco** (o índice já está
certo e a cópia de 0 byte não tem conteúdo a perder). A receita parou em **5 de 7 caminhos**; os 2 restantes
parecem «perda de dados» quando são apenas **um passo não executado**. Quem lê o estado atual sem separar as
camadas **conclui perda onde há só resíduo** — e quem aplica a receita **fora de ordem** (checkout antes do
reset) restaura do índice velho e **não conserta nada**.

**Como aplicar (régua).** Diante de arquivo de 0 byte, a pergunta não é «perdi o arquivo?», é
**«em qual camada ele está vazio?»**:

- (a) `git cat-file -s :<path>` — se o **índice** responde o tamanho certo, **o dado existe**: o defeito é de
  árvore, e o remédio é `checkout --` (nunca re-`fetch`, nunca reescrever à mão);
- (b) `git rev-parse HEAD:<path>` × `origin/main:<path>` — se os dois batem, **não há divergência de
  conteúdo**, só de materialização;
- (c) `git diff --stat` — o número de linhas «removidas» **é o tamanho do resíduo**, não o tamanho da perda;
- (d) e só se **nenhuma** camada tiver o conteúdo é que se procura no remoto/outro clone (foi o passo certo
  na 396ª: 26/26 objetos recuperáveis — mas ali o defeito **era** de objeto).

**Irmãs:** `20260910_crash_zerou_objetos_do_git.md` (a causa: desligamento sujo, cache perdido — objeto
datado e vazio) · `20260910_barreira_instalada_na_fisica_errada.md` (a mesma pergunta de fundo: **em qual
física/camada o defeito existe?**) · `20260910_maintenance_que_sobrevive_nao_e_removido.md` («o site voltou»
não é «o update terminou»). **Família:** o estado que se lê e o estado que se mede não são o mesmo estado —
três camadas com nomes parecidos («0 byte», «0 byte», «0 byte») e causas diferentes.

**Ref:** bloco DS-Dell-20260910-024 (ronda 398ª) · BUG-20260910-DS-196 (396ª/397ª) · XM-20260910-028.
