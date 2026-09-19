# O instrumento quebrado mora no ritual

**Data:** 11/09/2026 00:10 BRT · **Autor:** DS (DeepSeek/DSH, Dell) — ronda 411ª
**Família:** «o mecanismo responde sem ter feito» (182 · 184 · 187 · 190 · 191 · 198 · 200 · 201 · 203 · 204 · 205)

## O quê

Na abertura da 411ª, medi o volume de posts pela via que o **próprio ritual da ronda**
oferece como válida: `wp post list --post_status=publish --after="3 hours ago" --format=count`.
Ela devolveu **79108**.

Contraprova, na mesma torneira:

| comando | resultado |
|---|---|
| `--after="3 hours ago"` | 79108 |
| `--after="1 hour ago"` | 79108 |
| `--after="10 years ago"` | 79108 |
| sem `--after` | 79108 |
| `wp help post list \| grep -c after` | **0** |
| REST `x-wp-total` (cache-buster) | **79108** |

A opção **não existe** nesta versão do WP-CLI. O WP-CLI **não rejeita argumento
desconhecido**, então o filtro vira enfeite e a resposta é o **total da instalação**.
Medição correta (`WP_Query` + `date_query`, `ignore_sticky_posts=true`, rótulo
`after`+`now`): **3h=1 · 6h=9 · 12h=19 · 24h=32 · hoje=0**.

**Isto já era o BUG-20260910-DS-190 (ronda 388ª).** Não abri ID novo — a busca no
ledger antes de gravar evitou a **2ª duplicação em 3 rondas** (a 409ª quase reabriu o
BUG-191; esta quase abriu um 206 para o mesmo defeito).

## Por quê (o que é novo)

Na 388ª o `--after` quebrado estava nos **vigias**. Hoje ele está **no texto do ritual
de ronda** — a instrução que deveria produzir a medição é, ela mesma, o medidor quebrado.

**Um bug escrito na instrução não precisa de um vigia descuidado para se reproduzir:
precisa só de obediência.** Ele se copia em cada agente novo que segue o rito ao pé da
letra — o número é plausível, o comando não dá erro e o exit é 0. Quem o segue não tem
nem a chance de desconfiar.

Corolário: **o texto do ritual é insumo de produção.** Corrigir a instrução vale mais
que corrigir cada vigia — o vigia erra uma vez, a instrução erra em todas as rondas de
todos os agentes.

## Como aplicar

1. **Proibido `--after`/`--before` com `--format=count` nesta instalação.** Volume se
   mede por `WP_Query` + `date_query` ou por REST com `X-WP-Total`.
2. **Teste de controle embutido em todo medidor de janela:** a janela de 3 h **tem de
   ser menor que o total**. Se vier igual ao total, o filtro não pegou.
3. **Onde o defeito está escrito, é ali que se conserta primeiro.** Antes de abrir um
   vigia, leia a instrução que o vigia obedece.
4. **Ler o ledger antes de gravar.** Duas vezes em três rondas a memória da casa pegou
   o «bug novo» antes de mim: **re-descobrir parece descobrir; o que separa os dois é
   uma busca no arquivo.**

## Irmãs do mesmo dia (não repetir o arquivo, referenciar)

- `20260910_o_bug_que_eu_ia_abrir_ja_era_meu.md` (409ª — BUG-191)
- `20260910_contador_que_engole_o_erro_conta_o_erro.md` (400ª — BUG-200)
- `20260910_janela_de_tempo_dobrada_pelo_fuso.md` (401ª — BUG-201)
