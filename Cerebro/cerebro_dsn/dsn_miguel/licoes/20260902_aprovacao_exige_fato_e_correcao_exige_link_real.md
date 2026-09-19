# Aprovação exige fato verificável — e correção exige link REAL (caso Angeli, do R1)

Data: 02/09/2026 · Observado no feedback nº 6 da CL-076 (CL-20260902-076, ronda 15:42) sobre o ciclo do R1 às 15:05.

## O quê
O R1 pediu "corrigir" o post do Angeli (268547) de "2022" para "abril de 2018", citando dois links (Folha e O Globo) que não sustentam a correção — o diagnóstico de afasia progressiva primária e a aposentadoria foram divulgados em 20/04/2022, quando ele tinha 65 anos (nascido em 1956: 1956+65 = 2021/22, não 2018). No mesmo ciclo, o R1 APROVOU o 268567 (cookies da Liga Saudita) — texto sem evento, sem data e sem fonte — que o Miguel mandou para a lixeira ~30 minutos depois ("muito estranho aquilo").

## Por quê
Link inventado é o pior erro de um fact-checker: a "correção" com fonte falsa corrompe um texto que estava CERTO — o erro entra pela porta da verificação. E "nada a corrigir" não é "aprovado": aprovar exige fato verificável (quem / o quê / quando / fonte), não ausência de erro visível. O revisor tem duas armadilhas simétricas: corrigir o que está certo (com link que não existe) e passar o que está vazio (sem fato para checar). Uma terceira, de ferramenta: não achar um fato coberto por 10 veículos (TMZ/Rolling Stone/E! no caso Richie) é problema da perna de busca — marcar INCERTO_POR_FERRAMENTA, nunca INCERTO do fato.

## Como aplicar (minha régua de vigia e de CEO em treinamento)
1. Antes de "corrigir" uma data ou fato com fonte: abrir o link (existe? o conteúdo bate com o que eu cito?) e conferir a aritmética (1956 + 65 anos = 2021/22; um link de 2018 não prova um fato de 2022). Link que não abre = não citar; dúvida real = marcar INCERTO, nunca "corrigir" no escuro.
2. Dois níveis de leitura: "sem erro visível" ≠ "aprovado" — aprovação exige fato com fonte; se o problema é a ferramenta e não o fato, o rótulo certo é INCERTO_POR_FERRAMENTA.
3. Vale para a minha própria verificação: toda sonda que eu cito (REST, WP-CLI, feed, endpoint) tem que existir e bater — número fora de escala numa janela pequena (78.786 numa janela de 3h = total do acervo, filtro --after ignorado) é régua errada, não dado.
4. O custo do "aprovado" vazio é a confiança do dono no gate: o Miguel desmontou o 268567 em minutos — um selo dado sem fato queima o selo, não só o post.

Ref.: CL-20260902-076 (feedback nº 6, canal revisao/) · bloco DS-20260902-025 da ponte (de_dell.md 16:06).
