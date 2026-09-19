# A hora em que nada quebrou — e por isso ela é a prova

**Data:** 11/09/2026 · **Ronda:** DS-Dell 428ª (08:30 BRT) · **Tema:** BUG-208 / dose-resposta do FLUSHDB
**Ref:** ponte `DS-Dell-20260911-018` · nodo de bugs ADENDO-9

## O quê

Fechei a tabela dose-resposta do BUG-208 com **9 amostras de `FLUSHDB`** datadas no `SLOWLOG` (leitura de 08:30 na torneira `ssh cafezinho-wp`, read-only), cruzadas com as respostas 5xx por minuto no `access.ocafezinho.com.log`:

| FLUSHDB (SLOWLOG) | duração | 5xx no minuto |
|---|---|---|
| 04:25:29 | 7,499 s | 22 |
| 04:25:37 | 0,021 s | 0 |
| 05:00:37 | 0,854 s | 0 |
| 05:25:35 | 0,911 s | 0 |
| 06:25:22 | 1,258 s | 5 |
| 06:25:23 | 0,013 s | 0 |
| 07:25:32 | 3,237 s | 7 |
| 07:25:36 | 0,010 s | 0 |
| 08:25:25 | **1,832 s** | **15** ← amostra nova desta ronda |

**9 de 9, sem uma única exceção:** toda chamada **acima de 1 s** produziu 5xx (4 de 4); toda chamada **abaixo de 1 s** produziu zero (5 de 5). O limiar não é o comando, não é a hora, não é a carga: é o **`read_timeout` de 1 s do drop-in do object cache**.

**E a prova mais forte é a hora que não tem nada:** a **hora 05 é a única do dia com ZERO 5xx** — e é exatamente a hora cujo flush das `:25` mediu **0,911 s**, ou seja, **89 milissegundos abaixo do limiar**. Não é o erro que confirma a régua; é a **ausência** de erro no único caso em que a régua previa ausência.

## Por quê (importa)

1. **O caso negativo é o dado.** Eu já tinha 4 casos acima do limiar matando leitor; isso mostra que a hipótese **serve**, não que ela **discrimina**. O que a transforma em régua é o caso que **deveria** ter falhado e não falhou — e ele existia, na hora 05.
2. **A margem é desconfortavelmente fina.** 0,911 s × 1,000 s = **89 ms** separam «site inteiro de pé por uma hora» de «15 leitores derrubados». Um sistema cujo estado saudável depende de 89 ms de folga não está saudável: está **com sorte**.
3. **A cadência horária ficou visível.** As 9 chamadas se agrupam em **pares separados por 1–11 s** (04:25:29/37 · 06:25:22/23 · 07:25:32/36) → **dois chamadores distintos**, e **5 das 9 caem no minuto `:25`**. A ronda anterior já havia varrido crontab/systemd/hooks do WP e não achou job em `:25`; o padrão **aumenta** sem que a origem apareça.
4. **O `cmdstat` dá a média que o caso isolado esconde:** `cmdstat_flushdb: calls=10, usec=15.644.365` → **1,564 s por chamada em média** — acima do limiar de 1 s. A média está do lado perigoso. `cmdstat_get`: 5.699.728 chamadas a 13,93 µs.

## Como aplicar

- **Régua de dose-resposta:** ao propor que um **limiar** (timeout, quota, MTU, rate limit) explica um sintoma, procure ativamente **a janela em que o evento ficou do lado seguro** — se ela existir e estiver limpa, a hipótese vira régua; se não existir, você tem correlação, não limiar.
- **Régua de folga:** quando o limite é um timeout, **a folga saudável medida** (89 ms aqui) é mais informativa que o pior caso. Reporte a folga, não só o pico.
- **Régua de instrumento (repetida de propósito):** contagem de 5xx por **regex ancorada** (`HTTP/[0-9.]+" 5[0-9][0-9] `), nunca por `awk -F'"'`/`grep ' 5.. '` — a minha primeira tentativa desta ronda deu **368 5xx na hora 00** onde o número correto era **0**. O instrumento solto inflou o defeito em duas ordens de grandeza.
- **Ação que continua pendente (não é minha):** **P1** `define('WP_REDIS_GRACEFUL', true)` — 1 linha no `wp-config.php`, dono **infra us65/@ZM**. É a única defesa que não depende de adivinhar o próximo comando culpado.
