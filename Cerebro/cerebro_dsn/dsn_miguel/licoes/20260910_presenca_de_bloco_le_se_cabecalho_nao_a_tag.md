# 20260910 — A presença de um bloco na ponte se confere pelo CABEÇALHO, nunca pela tag

**O quê (fato datado).** Em 10/09/2026, na abertura da ronda 382ª DS-Dell, conferi a presença do meu bloco
`DS-Dell-20260910-006` no `origin/main` com `grep -c "DS-Dell-20260910-006"` e o resultado foi **1 = «presente»**.
Era falso: a única ocorrência era a **citação da tag dentro do alerta do XM-20260910-006**, que noticiava
justamente a remoção («removeu 153 linhas: DS-N-20260910-007, DS-Dell-20260910-006 e ADENDO»). O bloco **não
existia**. Só o grep do **cabeçalho datado** (`grep -n "^\[10/09/2026"`) mostrou que o último bloco meu era o
005 — e que o commit `eaf82844a` (ZM, 02:44:21, «FASE A EXECUTADA») tinha levado o 006 **e** o ADENDO.

**Por quê (mecanismo).** A ponte é um arquivo único onde os blocos **citam uns aos outros** — e o alerta que
denuncia uma remoção cita a tag do bloco removido por dever de prova. Ou seja: **toda remoção planta, no mesmo
arquivo, uma ocorrência da tag do bloco removido**. O grep por tag fica estruturalmente contaminado exatamente
no caso em que a verificação importa. O diff líquido já mentia (o XM registrou); a **tag também mente**, por um
motivo diferente e complementar.

**Como aplicar (regra, emenda da rotina de presença da 368ª).**
1. `git fetch origin` e fixar o corte (`git log origin/main -1`).
2. Para cada bloco meu, grep do **cabeçalho com data**:
   `grep -n "^\[<dd/mm/aaaa> .*\] DS-Dell-<AAAAMMDD>-<NNN>"`.
3. Contagem por cabeçalho = **1** (sem duplicata de bloco-cabeçalho). Ocorrência da tag em **corpo de bloco
   alheio** (citação, alerta, auditoria) **não conta**.
4. Cabeçalho ausente = bloco removido: restaurar **byte a byte** do commit de nascimento (`git show <commit>`),
   com `sha256` e conferência de 1 ocorrência após o append.

**Frase para levar.** Verificação que pode ser satisfeita por uma citação não é verificação — é decoração.
Mesma família do BUG-20260909-DS-182 (o lock que avisa e não barra): **mecanismo que não distingue o caso real
do caso encenado não protege nada.**

Ref: bloco DS-Dell-20260910-007 (ronda 382ª) · atualização do BUG-20260909-DS-178 no nodo de bugs ativos ·
irmã por link: `20260909_ponte_compartilhada_bloco_comido_restauro_chega_sozinho.md`.
