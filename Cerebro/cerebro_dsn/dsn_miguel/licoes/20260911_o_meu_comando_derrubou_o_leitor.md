# O MEU COMANDO DERRUBOU O LEITOR — o instrumento de medição virou a carga que mata a página

**Data:** 2026-09-11 (ronda 426ª DS-Dell) · **Refs:** BUG-20260911-DS-208 (adendo novo), BUG-20260910-DS-190 (adendo grave), BUG-20260910-DS-191, lição `20260911_o_save_nao_era_o_gatilho.md`, lição `20260911_o_instrumento_quebrado_mora_no_ritual.md`.

## O QUE ACONTECEU

Na ronda 426ª, entre **07:33:19 e 07:34:01**, o site devolveu **44 respostas 5xx a leitores** (39 no minuto 07:33, 5 no 07:34) — e a causa medida **foi o meu próprio comando de medição**.

A cadeia, medida no `SLOWLOG` do Redis:

- **07:32:54** — `MGET wp:post_meta:269770` → **930 ms** (abaixo do timeout, sem erro);
- **07:33:19** — `MGET wp:terms:9387` → **1.487 ms** ⟂ **cruza o `read_timeout` de 1 s** do drop-in ⟂ primeiro 5xx;
- **07:34:01** — `MGET wp:posts:269770 …` com **79.083 chaves em um único comando** → **16.390 ms (16,39 s)** ⟂ janela de 44 5xx em 16 s.

O MGET de 79.083 chaves veio de um **`wp post list --post_status=publish --after="2026-09-11 00:00:00"`**. O `--after` **não existe** nesta instalação do WP-CLI e **não gera erro** (é o **BUG-190**, aberto na 411ª): a opção é ignorada em silêncio, o comando lista **todos os publicados** e o `WP_Query` então chama `_prime_post_caches()` → `_get_non_cached_ids()` → **um `MGET` com dezenas de milhares de chaves**, que ocupa a **thread única** do Redis por 16 segundos.

**A assinatura bate em três pontos independentes:** (a) o **stack trace do meu próprio comando que morreu** mostra exatamente `_get_non_cached_ids()` → `_prime_post_caches()`; (b) o **tamanho** 79.083 ≈ 79.113 publicados − ~30 já em cache; (c) a **ordem das chaves é data-descendente** (269770, 269719, 269758, 269716, 269852, 269735…), isto é, uma **listagem integral por data**, que nenhuma página do site pede em 79 mil itens.

**Limite declarado:** o `SLOWLOG` **não registra quem** emitiu o comando; a atribuição ao meu instrumento é a hipótese **melhor sustentada**, não uma prova. E **eu não vou reproduzir o teste** — a contraprova custaria outra janela de leitor derrubado.

## POR QUE IMPORTA (o que muda no BUG-208)

O ADENDO-7 tinha fechado a **dose-resposta do FLUSHDB** (comandos acima de 1 s matam; abaixo, não). Isso continua verdadeiro. O que esta ronda acrescenta é que **o FLUSHDB não é a única classe**: **um `MGET` legítimo, emitido por um cliente legítimo, cruzou o mesmo limiar e matou o mesmo leitor**.

**A causa-raiz não é o comando — é o acoplamento:** cliente com `read_timeout` de **1 s** + servidor de **thread única** + um cache que **falha FECHADO** (`WP_REDIS_GRACEFUL` não definido em `wp-config.php` ⇒ `show_error_and_die()` ⇒ `wp_die()` ⇒ HTTP 500). Qualquer operação cuja **cauda de latência** passe de 1 s derruba todos os leitores concorrentes: FLUSHDB de 7,5 s, MGET de 16,4 s, ou o próximo comando que aparecer.

**Consequência prática:** a alavanca de 1 linha `define('WP_REDIS_GRACEFUL', true)` deixa de ser só um remédio para o flush e passa a ser **a única defesa que não depende de adivinhar o próximo comando culpado**.

## RÉGUAS QUE FICAM

1. **Medir contagem não é listar.** Para contar, usar `wp db query` (SQL direto, sem object cache), `WP_Query` com `fields=ids`, ou REST com `X-WP-Total`. **Nunca** `wp post list` sem filtro efetivo numa instalação de 85 mil posts.
2. **Comando que não dá erro não é comando que é seguro.** O `--after` ignorado devolveu exit 0 e um número plausível — e, agora, **também** uma parada de 16 s. O modo de falha silencioso escalou de «número errado» para «leitor derrubado».
3. **Antes de rodar um comando de medição em produção, perguntar: quanto ele pode custar ao servidor?** Um instrumento deve ser mais leve que o sistema que ele mede.
4. **Quando o sintoma é o cliente morrendo, o suspeito é qualquer comando que cruze o TIMEOUT do cliente** — e a lista de suspeitos inclui **os meus**.
5. **Registrar a própria suspeita antes de acusar terceiros.** Nesta ronda o primeiro impulso foi atribuir a janela ao FLUSHDB/cron; o `SLOWLOG` mostrou que o comando tinha a **minha cara**.

## FRASE DE BOLSO

**O termômetro que eu encosto no paciente pode ser a febre.** Se o instrumento de medição tem o mesmo timeout do paciente e o mesmo servidor de thread única, medir errado é o menor dos danos — o maior é medir e derrubar.
