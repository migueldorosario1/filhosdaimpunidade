# A dose cruza o timeout — e o FLUSHDB deixa de ser suspeito para virar relógio

**Data:** 11/09/2026 (ronda 424ª, bloco DS-Dell-20260911-014)
**Contexto:** BUG-20260911-DS-208 — leitores recebem HTTP 500 porque o object-cache
(Redis) falha FECHADO (`object-cache.php` sem `WP_REDIS_GRACEFUL`, `read_timeout = 1 s`).

## O quê (o achado)

O `SLOWLOG` do Redis reteve **as 6 chamadas de FLUSHDB** desde o boot das 03:31, e elas
formam uma separação limpa, sem exceção, no limiar de **1 s = `read_timeout` do drop-in**:

| hora (BRT) | duração | erros ao leitor |
|---|---|---|
| 04:25:29 | 7.498.582 µs (7,499 s) | **25 × 500** |
| 04:25:37 | 21.468 µs | 0 |
| 05:00:37 | 854.026 µs (0,854 s) | 0 |
| 05:25:35 | 911.211 µs (0,911 s) | 0 |
| **06:25:22** | **1.258.309 µs (1,258 s)** | **5 × 500 (6 `RedisException`)** |
| 06:25:23 | 12.718 µs (0,013 s) | 0 |

Soma dos 6 = **10.556.314 µs**, exatamente o `cmdstat_flushdb usec` do `INFO commandstats`
⇒ **a amostra é completa, não selecionada**. E os dois FLUSHDB de **06:25:22 e 06:25:23**
(1 s de distância) são um **experimento natural**: o longo cruzou o timeout e derrubou 5
leitores (inclusive a **home `/`**); o curto, não.

## Por quê (a lição)

1. **O discriminador não é a frequência nem o comando: é a DURAÇÃO contra o TIMEOUT do
   cliente.** O 04:25:37 (0,021 s) e o 06:25:23 (0,013 s) são FLUSHDB iguais e inofensivos;
   o 1,258 s é o mesmo comando e mata. `O(1)` descreve crescimento de custo, não teto de
   tempo real — e um `flush` de conjunto grande sob swap custa o conjunto, não o comando.
2. **Contraprova na janela saudável.** Na 421ª eu já havia excluído o **RDB save** porque
   ele disparou **10 vezes** em 44 min sem um único erro. A mesma régua agora **promove** o
   FLUSHDB: ele é a única classe de evento medida cuja duração **cruza o timeout do cliente**.
   Candidato ≠ causa: o Redis **não registra quem chama** FLUSHDB; a atribuição segue aberta.
3. **O relógio apareceu.** Três dos seis (04:25:29, 05:25:35, 06:25:22) caem em **:25** —
   lead, não conclusão (n=3). Varredura do inventário de cron do us65: **nenhum job em :25**
   (crontab do root, `/etc/cron.d/*`, timers do systemd e os hooks horários do WP não
   batem); os dois flushes por gatilho (~1–8 s de intervalo) sugerem **dois chamadores**.

## Como aplicar (régua que fica)

- **Quando o sintoma é o cliente morrendo, procure o evento cuja DURAÇÃO cruza o TIMEOUT
  do cliente** — não o evento mais frequente, não o mais caro em média.
- **Toda amostra de "eventos lentos" tem que fechar a soma com o `commandstats`**; se a
  soma bate, a amostra é completa e pode virar tabela; se não bate, é recorte e não prova.
- **Um evento que dispara muitas vezes sem sintoma é CONTROLE, não suspeito** — mas o
  controle só vale se eu medir a janela em que ele dispara e nada acontece.
- **Alavanca do leitor continua de 1 linha** (`WP_REDIS_GRACEFUL true`, dono infra us65/ZM):
  mesmo com a causa raiz em aberto, o leitor para de morrer.
