# O RUÍDO ERA O INCIDENTE — a metade do log que ninguém leu

**Data:** 11/09/2026 · **Autor:** DS Miguel (Dell/DSH) · **Ronda:** 415ª · **Ref:** BUG-20260911-DS-208

## O quê

Na madrugada de 11/09, entre **02:00 e 02:04 BRT**, o site devolveu **135 erros a leitores**
(129 × HTTP 500 e 10 × HTTP 503), com **33% de falha no minuto 02:02** (110 de 332 requisições),
incluindo a **home** e **feeds**. A causa, colhida literal no `error.log` do nginx:

```
RedisException: read error on connection to 127.0.0.1:6379
  in /var/www/ocafezinho/wp-content/object-cache.php:1936
  → :1938 handle_exception() → :2935 show_error_and_die() → :3002 wp_die()
```

O drop-in **não degrada: mata a requisição**. O cache está configurado para **falhar fechado**.

## Por quê (a parte que dói)

**Isto já estava no ledger — classificado como «ruído transitório».** O item **O2** (31/08) dizia:

> «RedisException no shutdown do WP-CLI (ruído transitório) … MAS `redis-cli ping` = PONG»

Duas falhas de método nessa frase:

1. **Amostra de um lado só.** Olhou-se o log do **WP-CLI**; o outro lado — o **log de acesso do
   leitor** — mostrava o **mesmo** erro derrubando página pública. O WP-CLI foi apenas quem
   falhou **primeiro** (02:0x nesta ronda); o leitor veio **4 minutos depois**.
2. **Prova pelo instrumento errado.** `redis-cli ping` responde do **servidor**; o cliente PHP
   falha no **MGET/multi-get** sob carga. Nesta ronda: `ping` = **0,00 s em 5 de 5** tentativas
   **enquanto o `mget()` morria** na mesma máquina.

**Escala que passou despercebida:** em **10/09** foram **3.512 respostas 5xx em 311.337 requisições
= 1,13% de tudo**, com picos de **294/min às 11:08** e três das cinco piores horas **em pleno
expediente**. O monitor da casa mede **audiência**; não mede **erro**.

## Como aplicar

- **Saúde de dependência compartilhada se mede no caminho em que o cliente falha** — não no
  `ping`. Se o cliente usa `MGET`, `pipeline` ou conexão persistente, é isso que se testa sob carga.
- **Log de aplicação conta metade da história.** A outra metade está no **log de acesso de quem
  foi derrubado** (`awk '$9 ~ /^5/'`). Cruzar as duas torneiras é obrigatório antes de chamar
  algo de «ruído».
- **Ruído com sintoma assimétrico não é ruído.** Se o erro aparece só num consumidor (CLI, cron,
  beacon) e não em outro, a pergunta certa não é «é inofensivo?» — é **«por que o outro ainda não
  mostrou?»**.
- **Antes de arquivar um achado como transitório, escrever QUAL evidência o promove a incidente.**
  Sem esse critério, o item nunca é reaberto.
- **Falhar fechado em cache é escolha, não destino.** O próprio código dispara
  `do_action('redis_object_cache_error')` **antes** do `show_error_and_die`: existe gancho para
  degradar ao banco e ninguém o usa — então quem paga a indisponibilidade do cache é o leitor.

## Frase para levar

> O ruído era o incidente — e ele estava arquivado com nome de ruído desde 31/08.
> **Quem mede o servidor não mede o cliente; quem lê o log da ferramenta não vê o log da vítima.**
