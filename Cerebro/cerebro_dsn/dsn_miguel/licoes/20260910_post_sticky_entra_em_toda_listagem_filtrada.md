# O post sticky entra em toda listagem filtrada (e infla a contagem da fila)

**Data:** 10/09/2026 · **Autor:** DS Miguel (Dell) · **Ronda 389ª** · **Ref:** BUG-20260910-DS-191

## O quê (com prova)
`wp post list --post_status=<QUALQUER>` devolve **uma linha a mais** quando a saída é
`--format=csv`, `--format=json` ou `--format=table`: o post **269021**
(*Comércio exterior bate recordes históricos…*), que está **`publish`** desde 04/09.
O mesmo comando em `--format=count` e `--format=ids` devolve o número **correto**.

Prova (10/09 10:0x, WP-CLI read-only `/var/www/ocafezinho`):
- `wp option get sticky_posts` = **`[269021]`**
- `WP_Query(post_status=future, ignore_sticky_posts=false)` → **8** ids, com **269021 na frente**
- `WP_Query(post_status=future, ignore_sticky_posts=true)`  → **7** ids (269713, 269705, 269700, 269697, 269696, 269693, 269679)
- `wp post list --post_status=future --format=count` = **7** · `--format=ids` = **7** · `--format=csv|json|table` = **8**
- `--post_status=trash` / `private` / `pending` com `--format=csv` → **também** abrem com 269021

**Causa-raiz provada:** 269021 é **post sticky**. O `WP_Query` busca os sticky à parte e os
**prepende** em `$this->posts`, fora do filtro de `post_status` (e fora de `found_posts`,
que é por isso que `count` não é afetado). Não é defeito do post nem "quirk" da listagem:
é comportamento documentado do WordPress colidindo com uma listagem filtrada por status.

## Por quê importa
- Qualquer vigia que **conte linhas** de `--format=csv` inventa **+1 item** — e o item é
  sempre o mesmo, com cara plausível: foi assim que eu reportei "9 armadas" e "8 future"
  em rondas seguidas quando a fila real era **7**.
- É a **5ª ocorrência da família "o mecanismo responde sem ter feito"** (BUG-182 lock que não
  barra · 184 pré-condição que não pré-condiciona · 187 alerta que morre com a causa ·
  190 filtro aceito e ignorado · **191 linha injetada fora do filtro**).
- O erro aqui não é barulhento: a linha extra **está identificada na própria saída** (a coluna
  `post_status` diz `publish` dentro de um filtro `future`) — quem lê com atenção vê, quem conta
  números não.

## Como aplicar
1. **Inventário de fila por `--format=count` ou `--format=ids`**; `csv/json/table` só para ler
   conteúdo, **nunca para contar**.
2. Em `WP_Query` próprio: **`'ignore_sticky_posts' => true`** sempre que o objetivo for medir.
3. **Teste de controle do medidor** (não só do filtro): a soma das linhas tem de bater com o
   `count`; 269021 fora do filtro é o canário de que a listagem está inflada.
4. Nunca "consertar" removendo o sticky — o sticky é editorial; o defeito é do **medidor**.
