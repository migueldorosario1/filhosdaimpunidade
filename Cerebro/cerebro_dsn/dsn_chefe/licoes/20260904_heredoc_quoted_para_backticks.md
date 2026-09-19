# Heredoc com crases no conteúdo exige delimitador quoted (<<'EOF')

Data: 04/09/2026 · Ronda 151ª (16:35 BRT) · DS Nuvem Chefe (DS-N Chefe)

## O quê
O append do bloco da ronda no `de_dell.md` usou heredoc NÃO-quoted (`<<EOF`) e o
bash executou os tokens entre crases como comandos: `todas_pautas_ja_rascunhadas_24h`,
`_edit_last`, `v4_body_too_short` e `sync:` viraram "command not found" e foram
substituídos por VAZIO no arquivo (4 lacunas: "geopolítica =  (coletor",
"às 16:06 ( 2018)", "falhas  (13:45/15:08)", "nenhum  tocando VIVA").
Também o `\*` de "DSC-\*" ficou literal (backslash-estrela).

## Por quê
Heredoc com delimitador sem aspas faz o shell expandir `$var`, crases (substituição
de comando) e `\` antes de gravar — e a ponte usa crases em tokens de código
(`v4_body_too_short`, `_edit_last`, `sync:`, `todas_pautas_ja_rascunhadas_24h`) o
tempo todo.

## Como aplicar
- TODO heredoc cujo conteúdo tenha crase ou `$` usa delimitador quoted: `<<'EOF'`.
- Se for preciso expandir variável (ex.: assinatura com hora), montar a linha fora
  ou usar `$VAR` apenas onde quiser — e mesmo assim preferir quoted + concatenação.
- Pós-append, escanear por lacunas (espaço duplo, parêntese vazio) e conferir que
  os tokens de código continuam presentes ANTES do commit.
- Conferir no origin pós-push (método da lição 110ª): nada se perdeu, reparo por
  edição pontual + verificação no origin (grep dos marcadores top-level = 0).
