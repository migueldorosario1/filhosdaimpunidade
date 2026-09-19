# 2026-09-10 — Reformatar o arquivo inteiro esconde a mudança real (e o diff é quem avisa)

**O quê:** ao atualizar 3 campos (`atualizado`, `autor`, `nota`) do `reforma_v3_status_SEED.json` na ronda 441a, gravei com `json.dump(..., indent=4)`. O arquivo original usa `indent=1`. O resultado: **614 linhas alteradas para 3 campos de conteúdo** — o diff virou ruído e, se tivesse passado, qualquer auditoria futura (humana ou bot) teria de reconstruir o que mudou de verdade no meio da reformatação.

**Por quê:** gravador que não preserva o formato do original transforma uma edição pequena numa reescrita aparente. É primo do "artefato que não chega ao leitor" (440a): a edição foi feita, mas o **registro da edição** deixou de ser legível. E a falha é silenciosa: o JSON continua válido.

**Como aplicar (barreira):** antes de regravar qualquer arquivo versionado de 1 campo, ler o formato atual (indent, ordem de chaves, newline final) e reproduzi-lo; **checar o `git diff --stat` logo depois** — edição de N campos não pode virar edição de centenas de linhas. Se virou, desfazer e regravar. No caso concreto: `indent=1` + `\n` final → 4 inserções / 4 deleções.

**Evidência:** ronda 441a, 10/09/2026 23:3x; primeiro `--stat` deu 614 linhas, corrigido para 4/4 na mesma ronda.
