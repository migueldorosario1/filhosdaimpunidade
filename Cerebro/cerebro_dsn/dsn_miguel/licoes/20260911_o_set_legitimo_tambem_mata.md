# O SET legítimo também mata — a terceira classe de gatilho do BUG-208

**Data:** 11/09/2026 (ronda 429ª do DS-Dell, 09:05 BRT)
**Origem:** medição read-only na torneira `ssh cafezinho-wp` (us65)

## O quê

O cluster de **7 respostas 500 às 09:00:20–23 de 11/09** não tinha **nenhum `FLUSHDB`** por perto:
o `cmdstat_flushdb` seguia em `calls=10, usec=15.644.365` — **exatamente o mesmo número da ronda anterior**,
cuja última chamada datada foi às **08:25:25**. O `SLOWLOG` datou, no mesmo segundo dos erros, um comando
de outra natureza:

```
id 271 | 1789128022 (= 11/09 09:00:22 BRT) | 2.689.559 µs | SET wp:post-queries:wp_query-f7c5f398… | 127.0.0.1:39916
```

Um **SET legítimo do próprio WordPress** — gravação do cache de resultado de uma `WP_Query` — durou
**2,69 s** e derrubou **7 leitores**. Horas: **05 = 0 · 06 = 6 · 07 = 59 · 08 = 19 · 09 = 7 `RedisException`**.

## Por quê (e o que isso muda)

Até aqui o BUG-208 tinha **duas** classes de gatilho medidas: o `FLUSHDB` (ADENDO-7/9: ≥1 s mata, <1 s não mata)
e o `MGET` de 79.083 chaves, que era **meu** (ADENDO-8). Agora há **três** — e a terceira é a mais desconfortável:
o comando que matou o leitor desta vez **não era de ninguém de fora**, era a **própria camada que existe para
deixar o site rápido**. O que discrimina continua sendo **a duração cruzar o `read_timeout` de 1 s do drop-in**,
não o tipo de comando.

**Contexto medido (não causa):** há um **burst de crawler no topo de cada hora** — requisições nos 3 primeiros
minutos: **07:00–02 = 673 · 08:00–02 = 799 · 09:00–02 = 1233** (crescendo), dominado por um UA falso
`Firefox/155.0` (504 de 846 no burst das 09) e pelo `ImageBot/1.0` (17.319 no arquivo), vindo de **190.89.239.244/.31**;
a linha de erro registra `serverdoin-if-carga load=12.59 limit=24`. **Mas o burst não basta:** o mesmo burst
das 08:00 (≈793 req) produziu **zero** 5xx e nenhum comando cruzado; o das 09:00 (1233 req) produziu um.
Ou seja: o burst é **contexto que enfileira**; a causa suficiente segue sendo **um comando cuja cauda cruza 1 s**.

## Como aplicar

1. **Não procure só o suspeito da vez.** Ao investigar 500 de cache, varra o `SLOWLOG` **inteiro** e classifique
   por **duração**, não por nome do comando — a lista de classes já tem três (FLUSHDB, MGET, SET) e o próximo
   será outro.
2. **Antes de atribuir, confira se o suspeito anterior se mexeu.** `cmdstat_flushdb` inalterado provou que o
   flush **não era** o gatilho desta janela. O contador acumulado é a contraprova mais barata que existe.
3. **Dose, não frequência.** Sempre que a hipótese for «X causa Y», procure a janela em que X aconteceu
   **abaixo do limiar** e confirme que Y **não** aconteceu (foi assim que a hora 05 fechou a régua do flush,
   e é assim que o burst das 08:00 impede que eu chame o crawler de causa).
4. **Contagem de HTTP só com âncora** (`HTTP/[0-9.]+" 5[0-9][0-9] `) e correlação sempre com o **timestamp
   convertido** (`date -d @epoch`) — não comparar hora de log com hora de relógio por analogia.

**Ref:** BUG-20260911-DS-208 ADENDO-10 · bloco `DS-Dell-20260911-019` (429ª) · ADENDO-9 (428ª) · ADENDO-8 (426ª).
