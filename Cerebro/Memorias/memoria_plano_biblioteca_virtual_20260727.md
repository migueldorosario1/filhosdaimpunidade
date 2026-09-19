# 🧠 MEMÓRIA — PLANO: Biblioteca Virtual do Miguel (indexação inteligente)

**Criado em:** 2026-07-27 · **Agente:** ZCode/Kimi · **Pedido do Miguel (26/07).**
**Regra de ouro:** toda ideia do Miguel vira plano gravado no Cérebro. Nada se esquece.

## 1. O problema

Os livros do Miguel vivem espalhados: Google Drive (`ReadEra/Books`, `Notas do Google Play Livros/Books`), app Google Play Livros, Kindle/Amazon. Não há índice único. Se um arquivo muda de pasta ou de nome, qualquer índice por caminho quebra.

## 2. Princípios (pedido do Miguel)

1. **NÃO destrutivo:** não mover, não renomear, não reorganizar nada no Drive. Só ler e indexar.
2. **ID imutável por livro:** cada livro ganha um identificador que NÃO é o nome do arquivo. O índice sobrevive a mudanças de pasta/nome.
3. **Título padronizado:** `Sobrenome, Nome — Título (ano)` como forma canônica de exibição.
4. **Links cruzados:** para cada livro, buscar o link na Google Play Livros e na Amazon/Kindle (quando existir edição comercial).

## 3. O ID proposto: `MID`

**MID = Miguel ID**, formato `MID-0001`, `MID-0002`… sequencial, atribuído uma vez e nunca mais alterado. O arquivo de índice registra: `MID | título canônico | autor | ano | sinopse (3-4 linhas) | formato | caminho atual no Drive | hash parcial (primeiros 8 do md5 — identifica o arquivo mesmo se renomeado/movido) | link Play Livros | link Kindle/Amazon | status (lido/lendo/fila)`.

O **hash md5 parcial** é a âncora à prova de mudança de diretório: mesmo que o arquivo mude de pasta, o hash o reencontra em varreduras futuras (dedup).

## 4. Arquivos do índice (a criar, no Drive e no Cérebro)

- `biblioteca/INDICE_MESTRE_BIBLIOTECA.md` — o índice vivo (um bloco por livro, no formato acima)
- `biblioteca/biblioteca_ids.json` — a base estruturada (MID → metadados + hash)
- Local do índice canônico: `Cerebro/` (espelhado no Drive — nunca o contrário)

## 5. Plano de execução (fases)

1. **Fase 1 — Varredura read-only (feita em 27/07):** mapeado `ReadEra/Books` (livros + jornais misturados) e `Notas do Google Play Livros/Books`. Inventariar extensões (.pdf, .epub, .docx), separar LIVROS de JORNAIS/revistas.
2. **Fase 2 — Atribuição de MIDs + metadados:** ler cada arquivo (título/autor da capa ou metadata do PDF/EPUB), atribuir MID, hash, título canônico, sinopse curta.
3. **Fase 3 — Links das lojas:** para cada MID, pesquisar link Google Play Livros e Amazon/Kindle (API pública do Google Books + busca Amazon).
4. **Fase 4 — Dedup contínuo:** cron semanal que re-varre o Drive por hash, detecta livros novos e movimentações, atualiza caminhos sem perder MIDs.
5. **Fase 5 — Integração Play Livros + Kindle:** relatório do que falta em cada loja (o que o Miguel tem em arquivo mas não tem na loja, e vice-versa, onde der para mapear).

## 6. Cuidados

- Jornais/revistas (Folha, Globo, NYT, WSJ) não são livros: índice à parte (`biblioteca/PERIODICOS.md`) ou fora do MID.
- Edições Z-Library/OceanofPDF: registrar origem no metadado, sem julgamento — é o acervo do Miguel.
- Nada de upload/modificação nas lojas nesta fase.

## 7. Pendências de decisão (Miguel)

- [ ] O índice canônico fica em `Cerebro/` (minha sugestão) ou numa pasta `biblioteca/` no Drive?
- [ ] Fase 3 com links das lojas já na primeira leva, ou só depois dos MIDs?
