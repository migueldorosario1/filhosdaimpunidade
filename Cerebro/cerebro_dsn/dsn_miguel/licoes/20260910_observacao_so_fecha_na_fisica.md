# Observação só fecha na física: registrar não é resolver

**Data:** 10/09/2026 · **Ronda:** 408ª DS-Dell · **Ref:** bloco DS-Dell-20260910-034 · observação «duas contas Miguel» (rondas 402ª/403ª) · BUG-20260910-DS-202

## O quê
Em 10/09 as medições das **402ª/403ª** acharam o mesmo nome de autor em **duas contas** — «Miguel do Rosário» = **`2018`** (`James2017`, administrator) × **`5486`** (`ocafezinho_2`, **subscriber**) — e o pacote da soja **dividido** entre elas, inclusive uma quase-duplicata (**269630** × **269789**) que o **dedupe por título exato não vê** (os títulos divergem em três palavras). Registrei como **observação, com o dono**, e **não toquei em nada**. Na **408ª**, reli os mesmos IDs: os três posts da série **saíram publicados às 20:01:42 / 20:01:48 / 20:01:54 sob o autor `a2018`** (na primeira medição eram `5486`) e a gêmea **269630 ficou retida em rascunho** (`post_modified` 20:20:42). **A observação fechou** — sem eu mexer em nada e sem ninguém precisar me avisar.

## Por quê
O registro de um risco é um **ato de linguagem**: ele responde «alguém anotou?» sem responder «alguém resolveu?». É a mesma família do «mecanismo que responde sem ter feito» (BUG-182 · 184 · 187 · 190 · 191 · 198 · 200 · 201 · 204 · 205) — **o quadro de observações também é um mecanismo, e também pode responder sem ter feito.** Duas armadilhas concretas: **(a) silêncio não é prova de cura** — a observação sai do radar de todo mundo justamente por estar registrada; **(b) declaração do dono não é prova** — o que fecha é o **campo medido** (aqui: `post_author` + `post_status`), não a frase.

## Como aplicar
1. **Toda observação sem `closes_ref` volta na rotina de abertura** com uma medição barata do **campo exato** que a originou — mesmos IDs, mesmos campos.
2. **Perguntar «o que mudaria no dado?»** antes de considerar fechado: se a resposta for «nada», a observação está **confirmada, não resolvida** — mudou de lugar, não de estado.
3. **Verificar de novo, não cobrar de novo:** a ronda **mede** e só então fala; abrir chamado sobre o que ainda não releu é ruído.
4. **Fechar por escrito, com o número:** «269789/90/91 agora `a2018`; 269630 em `draft`» fecha; «acho que já resolveram» não.
5. **A lição invertida, para o dono:** o ciclo **registrar → esperar → conferir** funcionou porque quem observou **não agiu** em produção — **anotar bem é o que torna a cura verificável.**

**Irmãs por link:** `20260909_ponte_compartilhada_bloco_comido_restauro_chega_sozinho.md` (o restauro que chega sozinho: verificar no origin, não re-appendar) · `20260910_estado_lido_vence_estado_herdado.md` · `20260905_verificacao_de_presenca_nao_e_fechamento.md` (família: **verificação ≠ fechamento**).
