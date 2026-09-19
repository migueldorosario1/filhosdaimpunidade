# O mesmo comando, três saídas, três números — e a que a casa lê é a que mente

**Data:** 11/09/2026 (ronda 414ª DS-Dell, ~01:35 BRT)
**Autor:** DS Miguel (Dell)

## O quê

Ao inventariar a fila de agendados de 11/09 rodei **o mesmo comando** (`wp post list --post_status=future`), no mesmo minuto e contra o mesmo banco, em três formatos:

| formato | número devolvido | certo? |
|---|---|---|
| `--format=count` | **9** | correto |
| `--format=ids` | **9** | correto |
| `--format=csv` | **10 linhas** (9 `future` + 1 `publish`) | **contaminado** |

A linha a mais é o **post sticky 269021** (`post_status = publish`, `post_date` 04/09 12:00), que o `WP_Query` **prepende fora do filtro de status**. Ele vem **com a coluna de status escrita na própria linha** — o canário se denuncia, mas só para quem lê a coluna; quem **conta linhas** lê 10 peças onde há 9.

E no meio da mesma medição eu ainda produzi um **quarto número**: `--format=ids | tr ' ' '\n' | wc -l` devolveu **8**, porque o `wp` não terminou a saída com newline e o **`wc -l` conta quebras, não itens**. O verdadeiro era 9 — confirmado pelo `--format=count`.

**Quatro números (8 · 9 · 9 · 10) para uma verdade única: 9.**

## Por que importa

- A casa **lê CSV**: é o formato que aparece nos relatórios de fila. Quem contar linhas do CSV herda **um agendado fantasma** — e, sendo sticky de uma semana antes, o fantasma tem cara de **peça que nunca disparou** (falso alarme de atraso na grade).
- `wc -l` sobre saída sem newline final **subconta em 1** — o erro vai na direção de «faltou uma peça», que é exatamente o alarme de seca de esteira que a casa teme.
- **Nenhum dos quatro números veio com erro**, exit ≠ 0 ou aviso: todos «responderam com sucesso».

## Como aplicar (régua)

1. **Contar por `--format=count`; ler por `--format=csv`.** O número que vai ao relatório sai do **contador**, nunca da contagem de linhas.
2. **Teste de controle embutido:** a soma dos itens lidos **tem de fechar com o contador**. Divergiu → **imprimir a chave** (ID + `post_status`) antes de escrever qualquer número.
3. **`wc -l` só conta linha terminada.** Para contar itens de saída de ferramenta, use `--format=count` ou `grep -c` — nunca `wc -l`.
4. **Dois instrumentos que discordam por 1 valem mais que um que concorda consigo mesmo:** foi a discordância **8 × 9** que revelou o newline e a discordância **9 × 10** que localizou o sticky.

## Família

**14ª ocorrência** da família «o mecanismo responde certo à pergunta errada» (182 · 184 · 187 · 190 · 191 · 198 · 200 · 201 · 202 · 203 · 204 · 205 · 206) e **6ª aplicação do BUG-20260910-DS-191** — com a forma nova: **não é o sticky que mudou; é o formato de saída que decide se ele contamina o número.**
