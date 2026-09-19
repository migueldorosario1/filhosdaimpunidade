# FRESCOR — critério técnico de 1 a 5 (proposta do Miguel, desenho da Laura)

```yaml
tipo: PROPOSTA_DE_DIRETRIZ
origem: ORDEM_MIGUEL 20/08/2026 ~13:10 (voz) — "critério técnico de frescor, nota de 1 a 5, por vertical; entra na coleta, na seleção e no V5"
desenho: LAURA-CLAUDE (chefe do Loop Laura)
estado: PROPOSTA — para os 8 ofícios opinarem antes de virar diretriz
motivacao_medida: 3 casos em 12h (266189, 266685, 266751) — texto correto, mal datado
```

## 1. O problema que o frescor resolve (com os três casos de hoje)

| post | defeito | idade do fato na publicação |
|---|---|---|
| **266189** | "iniciam campanha" | lançamento coberto **3 dias antes** |
| **266751** | "firmam pacto" | assinatura em **7/08** — **13 dias** |
| **266685** | juízo no título | (defeito de enquadramento, não de idade) |

Nenhum tinha **erro factual**. Os dois primeiros tinham **erro de tempo** — e não existia campo nenhum no processo onde esse erro pudesse ser pego. **Frescor cria esse campo.**

## 2. A nota não se opina: calcula-se

Frescor é **relação**, não impressão: `idade_do_fato = publicação − data do fato`. A nota sai de uma tabela, e por isso é auditável.

| nota | idade do fato |
|---|---|
| **5** | menos de 6 horas |
| **4** | menos de 24 horas |
| **3** | menos de 72 horas |
| **2** | menos de 7 dias |
| **1** | mais de 7 dias |

**Consequência prática:** para dar a nota, alguém precisa **descobrir a data do fato** — que é exatamente o que faltou nos três casos. A nota é o subproduto; o valor está em obrigar a pergunta.

## 3. O mínimo muda por vertical (a parte que o Miguel definiu)

| vertical | frescor mínimo | por quê |
|---|---|---|
| Nacional, Política, Eleições | **4** | fato de ontem já compete com o de hoje |
| Geopolítica factual | **4** | idem — a menos que seja análise (ver §4) |
| Economia e mercado | **4** | número velho vira número errado |
| Ciência, Tecnologia, IA | **2** | descoberta não perde valor em dias; ganha em explicação |
| História, Religião, Cultura | **1** | o tempo é matéria-prima, não defeito |
| Vídeos / agregação | **3** | depende do gancho, não do ineditismo |

## 4. A exceção que o Miguel abriu, com trava

Geopolítica com fato antigo **pode** ir ao ar — **se for análise**. Mas análise disfarçada de notícia é o pior dos mundos: foi o 266751.

**Trava proposta:** frescor abaixo do mínimo da vertical só passa cumprindo **as duas** condições:
1. a peça se declara **análise** (marcador no post e ângulo analítico no título — não verbo de acontecimento no presente);
2. a **data do fato aparece no lead**, explícita.

Sem as duas, o gate barra. Com as duas, o leitor sabe o que está lendo — que é a única coisa que realmente importa aqui.

## 5. Onde o campo entra (as três etapas do Miguel)

- **Coleta:** cada item entra com `data_do_fato` e `fonte_da_data`. Item sem data de fato **não é coletado** — é devolvido para apuração.
- **Curadoria:** calcula `frescor`, compara com o mínimo da vertical, decide. Registra **critério e nota antes** de qualquer texto existir.
- **Produção:** recebe a ficha fechada. Se o texto pronto contradisser a nota (ex.: descobre-se que o fato é mais velho), volta para a curadoria — não se ajusta a nota para caber no texto.

## 6. O risco do V5, dito antes de acontecer

Um produtor que **dá a nota e escreve** tende a inflar a nota do que ele já quer escrever. A separação em etapas só funciona se a **ficha de curadoria for congelada antes** da produção começar — com artefato datado, não com intenção.

**Sugestão de forma:** cada etapa deixa um arquivo próprio — `coleta.jsonl` → `curadoria.md` (notas + critérios + descartes) → matéria. Auditoria de 30 min do AGY confere uma coisa só: **a nota é anterior ao texto?** Se o carimbo da curadoria for posterior ao do rascunho, a etapa foi teatro.

## 7. O que o frescor NÃO resolve

Não mede **relevância** nem **originalidade**. Um fato de duas horas pode ser irrelevante; um de dez dias pode ser a melhor pauta da semana. Frescor é **uma** coordenada — proponho que entre ao lado das que já existem (aderência à vertical, originalidade, qualidade da fonte), nunca no lugar delas.

— LAURA-CLAUDE, chefe do Loop Laura
