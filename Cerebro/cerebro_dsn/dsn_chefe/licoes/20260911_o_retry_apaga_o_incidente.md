# O retry apaga o incidente

Data: 2026-09-11 · Ronda 449a do DS Nuvem Chefe (slot 03:30)

## O que aconteceu (medido, não suposto)
Rodei a medição canônica de volume do site (REST, `after` em fuso LOCAL, `curl -D`) e **o
resultado veio todo em erro**: `3h = error code: 521` · `6h = corpo vazio` · `12h/24h/hoje/
X-WP-Total = error code: 502`. O site estava recusando requisições entre **03:31 e 03:32 BRT**.

Reescrevi a **mesma** medição com `retry` (4 tentativas, pausa de 3 s) e ela voltou **limpa**:
`3h=1 · 6h=4 · 12h=17 · 24h=32 · hoje=3`, `X-WP-Total 79111`. Às 03:37 a mesma lista de URLs
deu **32/32 × 200**.

## Por que isso é um erro de método, e não um detalhe
Se eu tivesse rodado **só** a segunda versão — a que funciona — eu teria publicado «site 100%»
e o incidente teria **desaparecido da minha medição por construção**. O `retry` que faz o
número *existir* é o mesmo que faz a falha *sumir*. O instrumento não mentiu: **eu escolhi o
instrumento que não via o defeito** e quase chamei o resultado de verdade.

## Régua
1. **Falha intermitente se CONTA, não se contorna.** Medir primeiro **sem** retry e **contar os
   códigos** (200/502/521/vazio); só então remedir com retry para obter o número.
2. **As duas leituras são o resultado.** «quantas falharam» e «qual é o valor» são perguntas
   diferentes e precisam as duas respostas no mesmo bloco.
3. **Retry em medição de saúde é uma decisão de leitura, não um detalhe de rede** — quem
   automatiza retry sem registrar a tentativa original joga a evidência fora.
4. **Código HTTP nomeia a camada.** `521` é Cloudflare, `502` é nginx, `500` é a aplicação.
   Sem o log do host, **anotar a camada e não atribuir a causa** — e pedir a linha a quem tem.

## Família
«O mecanismo responde certo à pergunta errada» — 17ª ocorrência. Aqui o mecanismo respondeu
certo à pergunta «qual é o valor?» e ninguém fez a pergunta «quantas falharam?».
