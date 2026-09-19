# 2026-09-11 — O SAVE NÃO ERA O GATILHO: A CORRELAÇÃO QUE EXPLICA A COINCIDÊNCIA NÃO É A QUE EXPLICA O CONTRASTE

**O quê (ronda 421ª, 05:0x BRT — correção da minha própria conclusão da 420ª sobre o BUG-20260911-DS-208).**
Na ronda 420ª eu declarei causa do incidente de leitura (500 ao leitor) o **RDB save do Redis** disparado por
`save 900 1 300 10 60 10000`: o site escreve >10.000 vezes por minuto, o Redis salva a cada ~60 s, e 7 dos 9
minutos com exceções caíam **dentro** de uma janela de save (o caso vivo: save 04:25:04→04:25:37, exceções às
04:25:29). A correlação era real. A conclusão era fraca — e a ronda 421ª mediu o **grupo de controle** que eu
não tinha medido:

- **04:25:29 → 05:09:32 = 44 minutos sem uma única `RedisException`** (total no `error.log` parado em **193**),
  com **hora 05 = 0 respostas 5xx** — e nesse mesmo intervalo o Redis **salvou ~10 vezes**:
  04:52:17 (**8,75 s**) · 04:53:26 (9,57 s) · 04:54:36 (9,90 s) · 04:55:46 (**15,90 s**) · 04:57:03 (10,29 s) ·
  04:58:14 (9,56 s) · 04:59:24 (11,13 s) · 05:00:37 (0,11 s), com `rdb_last_bgsave_status:ok`.
- Ou seja: **o mesmo evento (RDB save) que eu apontei como gatilho disparou 10 vezes no intervalo saudável sem
  produzir nada.** E a duração também não discrimina: um save de **15,9 s** não derrubou ninguém, um de **33,3 s**
  derrubou 25 páginas, e o de **102,7 s** (04:02) não derrubou nenhuma. **Frequência e duração do save estão
  excluídas como causa suficiente.** O que sobrou como candidato capaz de explicar o contraste é o **FLUSHDB**:
  `cmdstat_flushdb: calls=3, usec=8.374.076` desde o boot das 03:31 ⇒ **~2,79 s por chamada**, contra o
  **`read_timeout` de 1 s** do drop-in `object-cache.php` — a única classe de evento medida cuja duração
  **atravessa o timeout do cliente**.
- **E o achado que fecha a cadeia por baixo:** `dbsize` foi de **19.182 chaves (05:01)** para **98.063 (05:09)**
  = **~9.860 chaves novas por minuto**. É *isso* que faz o Redis dizer «10000 changes in 60 seconds» a cada
  minuto: **o save é SINTOMA da taxa de escrita, não um ator independente.** A alavanca real está a montante
  (taxa de escrita), não no `save`.

**Por quê importa.** Eu tinha em mãos uma correlação verdadeira e a transformei em causa — o erro clássico.
O que separa as duas não é mais medição do mesmo lado: é **medir a janela em que o efeito NÃO aconteceu**.
O save não explica o contraste (dispara nos dois lados); o flush explica (só ele cruza o timeout de 1 s).
O custo do erro: se eu tivesse entregado o laudo com «a causa é o save», o dono da infra teria aplicado
`config set save ""` e o leitor continuaria vendo `wp_die` — a alavanca certa é `WP_REDIS_GRACEFUL true`
(falhar aberto), que independe da causa.

**Como aplicar (régua).**
1. **Toda causa achada por co-ocorrência precisa de contraprova no intervalo saudável.** Se o candidato
   dispara também na janela limpa, ele não é a causa — no máximo é cenário.
2. **Quando o sintoma é o cliente morrendo, procure o evento cuja DURAÇÃO cruza o TIMEOUT do cliente** —
   não o evento mais frequente nem o mais vistoso.
3. **Contraste > coincidência.** Um `grep` que só olha os minutos doentes sempre acha uma causa; a causa
   de verdade é a que **está ausente nos minutos saudáveis**.
4. **Procure o sintoma do sintoma:** o save a cada 60 s não era o problema e sim a **leitura** da taxa de
   escrita (9.860 chaves/min medidas por `dbsize` em dois instantes). Dois números que não fecham escondem
   um terceiro comando que fecha.

**Limite declarado, sem inferência:** o Redis **não registra quem faz FLUSHDB nem quando**; 3 flushes desde o
boot produziram 1 aglomerado de erros (04:25), não 3 ⇒ **FLUSHDB é o candidato com melhor suporte, não causa
provada**. O que está provado é a exclusão: **save (frequência e duração) não é causa suficiente.**
