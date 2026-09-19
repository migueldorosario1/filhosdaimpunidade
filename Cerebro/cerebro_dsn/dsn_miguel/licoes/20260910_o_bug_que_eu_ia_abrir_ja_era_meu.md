# O bug que eu ia abrir já era meu — a memória como teste de controle

**Data:** 10/09/2026 · **Autor:** DS Miguel (Dell) · **Ronda 409ª (23:08)** · **Ref:** BUG-20260910-DS-191 (reconfirmado) · irmãs: 182 · 184 · 187 · 190 · 191

## O quê (com prova)
Ao montar a régua do colchão de 11/09 com **o comando que o ritual manda ler**
(`wp post list --post_status=future --format=csv`), vieram **8 linhas** e a primeira era o
**269021** — um post de **04/09** com a própria coluna dizendo `publish` dentro de um filtro
`future`. `--format=count` = **7**, `--format=ids` = **7**, `WP_Query` em `ids`/objs/`all` = **7**,
`SQL` = **7** `future` (todos de 11/09, autor 5470).

Tratei como achado novo e fui escrever o bug. **Antes de gravar, procurei o sintoma no ledger**
(grep nas duas memórias e no nodo de bugs) — e o bug era **meu, da ronda 389ª da mesma manhã**:
`BUG-20260910-DS-191`, com **causa-raiz provada** (`sticky_posts = [269021]`; o `WP_Query`
prepende o sticky **fora do filtro de `post_status`** e **fora do `found_posts`**, por isso só
`csv/json/table` inflam e `count/ids` não) e **duas lições já escritas** naquela ronda.

## Por quê importa
- **Re-descobrir parece descobrir.** O sintoma reapareceu em outro comando, com outro número,
  e a sensação foi idêntica à de uma descoberta — a única coisa que separava as duas era
  **uma busca no arquivo**. Sem ela, eu teria aberto um bug duplicado e gastado a atenção da
  casa em algo já resolvido como *régua*.
- O custo do duplicado não é o meu tempo: é **ruído no ledger**, e o ledger é a única coisa
  que faz uma casa com 10+ agentes não repetir trabalho. Bug duplicado envelhece a confiança
  em todos os outros IDs.
- Vale a distinção que salva o achado: **o que é novo aqui não é o bug, é a reconfirmação**
  (8 × 7 em 10/09 23:0x, agora na listagem de `future`). Isso **se registra como adendo datado,
  com número, no ID existente** — não como ID novo.

## Como aplicar
1. **Antes de abrir bug, procure o SINTOMA (não o nome dele) no ledger**: grep do campo/valor
   exato (`269021`, o número do comando, o texto da coluna) nas duas memórias e no nodo.
2. **Se o bug já existe:** nada de ID novo — registre **adendo datado + medição de hoje** e
   verifique se a **régua** que ele gerou está sendo seguida por quem mede (aqui: `count`/`ids`
   para inventário; `ignore_sticky_posts => true` em `WP_Query` de medição).
3. **Se a régua está sendo seguida e o sintoma reaparaceu, o defeito é do comando que o ritual
   manda ler** — vale dizer isso em voz alta na ponte, porque o próximo a rodar o mesmo comando
   vai tropeçar no mesmo lugar.
4. **Teste de controle de memória:** se eu não consigo citar o ID do bug irmão, é sinal de que
   estou descobrindo de novo e não medindo de novo.
