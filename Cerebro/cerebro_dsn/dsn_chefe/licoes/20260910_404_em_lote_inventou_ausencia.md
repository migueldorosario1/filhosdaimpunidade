# Lição DS-N Chefe · 10/09/2026 · O 404 em lote inventou ausência seis vezes e nenhuma era verdade

## O QUÊ (com prova)
Às 18:01 desta ronda (435ª, 10/09/2026), um lote de sondas `curl -o /dev/null -w '%{http_code}'` em
`https://www.ocafezinho.com/?p=<id>` devolveu **404 para os SEIS IDs testados**:
269772 · 269705 · 269713 · 269768 · 269727 · 269735.
O 269772 tinha subido às **17:45:00** (15º disparo pós-BUG-184 em ponto) e o **269700 estava no ar desde
17:15** — os dois apareciam como `publish` no REST (`X-WP-Total` = 79099). Trinta segundos depois, o
**mesmo lote** devolveu **200 para 269700 e 269772** e 404 **só** para os que de fato ainda não subiram;
repeti 2× e o resultado correto se manteve. **Não houve despublicação de nada.**

## POR QUÊ (a lição)
O instrumento não errou o número: errou **o significado do número**. Um 404 tem várias causas
(propagação/cache, rajada de requisições, topo de hora) e **só uma delas é "não publicado"**.
Na ronda anterior, um 404 no 269772 era lido como prova de "ainda não subiu"; se a rajada tivesse
acontecido no sentido oposto (um post publicado atrás de um 404 transitório), eu teria reportado
**falha de disparo que não existiu** — ou, pior, teria "confirmado" um alerta de grade com dado falso.
Família: **o mecanismo que responde sem ter feito** (BUG-182 · 184 · 187 · 190 · 191 · 198 · 200 · 201 · 203).

## COMO APLICAR (régua)
1. **404 único não é prova de não-publicação.** Antes de virar alerta, **reconfirmar**: (a) REST canônico
   (`/wp-json/wp/v2/posts/<id>` com `status` e `date`), e (b) **repetir a sonda** com intervalo.
2. **Horário de disparo se lê no REST `date`** (`17:45:00`), não no código HTTP da home — o HTTP só diz
   "existe/não existe agora", não diz quando subiu.
3. **Sonda em lote é amostra, não censo:** se o lote inteiro devolver o mesmo código para IDs de estados
   diferentes (um publicado há 45 min e cinco futuros), **o lote está errado**, não os IDs.
4. Vale para qualquer contagem de disponibilidade: **um código HTTP se confirma contra o estado no dado**,
   nunca contra a nota anterior (prima de `20260910_porcentagem_herdada_da_nota_nao_e_medicao.md`).

Física: Tencent (nuvem). Dono: DS-N Chefe (a lição é minha, do meu instrumento).
