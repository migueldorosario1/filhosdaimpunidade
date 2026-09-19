# A dose separa a causa do cenário — a frequência não

**Data:** 11/09/2026 · **Ronda 422ª (DS-Dell, 05:30 BRT)** · **Família:** método de investigação / contraprova (irmã de `20260911_o_save_nao_era_o_gatilho.md`, `20260911_o_log_nomeia_o_proxy_como_cliente.md`, `20260911_o_rotulo_do_meu_proprio_grafico.md`)

## O quê

Duas medições no mesmo incidente (BUG-208, `RedisException` → HTTP 500 para o leitor):

1. **Exclusão por contraprova de frequência.** O candidato «RDB save» foi apontado como gatilho porque 7 de 9 minutos com exceção caíam dentro de uma janela de save. Na janela saudável de 44 min (depois 70 min) o Redis **salvou 10 vezes** — com `rdb_last_bgsave_status:ok` — e **não houve uma única exceção**. **Evento que também dispara quando o sintoma não acontece é cenário, não causa.**

2. **Confirmação por dose.** O outro candidato — `FLUSHDB` — ganhou os dois pontos que faltavam:
   - **7.498.582 µs = 7,5 s** (04:25:29) → **22 × HTTP 500**;
   - **911.211 µs = 0,911 s** (entre 05:05 e 05:35) → **zero 5xx** na hora, `error.log` parado em 193.
   O **`read_timeout` do cliente é 1 s**. **O ponto positivo cruzou o limiar por 7,5×; o negativo ficou abaixo — e o sintoma seguiu a dose, não a frequência.**

3. **Errata de taxa.** `dbsize` 19.182 (05:01) → 98.063 (05:09) foi lido como «~9.860 chaves/min». A segunda janela deu 98.063 (05:09) → 157.065 (05:35) = **~2.270/min — 4,3× menor**. O Redis confirma pelo outro lado: `rdb_changes_since_last_save` = **7.613**, abaixo do limiar de 10.000 da regra `60 10000` ⇒ o save de 60 s **não estava armado naquele momento**.

## Por quê

- **Co-ocorrência produz candidatos; só o contraste produz causas.** O teste é sempre: *o candidato dispara quando o sintoma NÃO acontece?* Se sim, cai.
- **Quando o sintoma é o cliente morrendo, o que importa é a duração do evento contra o timeout do cliente** — não o evento mais frequente nem o mais longo em abstrato (o save de 102,7 s não produziu nada).
- **Dose-resposta é o que correlação não tem:** um ponto acima e um ponto abaixo do limiar, com o resultado mudando de lado, é evidência de mecanismo; N ocorrências simultâneas é evidência de cenário.
- **Uma janela única não é uma taxa.** Se a grandeza é «por minuto», ela precisa de **duas janelas** — senão o número descreve o intervalo, não o regime. (Errata minha, 2ª na mesma noite, seguindo a mesma disciplina da 416ª e da 421ª: **registro a errata, não defendo o número**.)

## Como aplicar

1. Antes de publicar um candidato, **medir a janela saudável** do mesmo tamanho e procurar o candidato nela. Achou? É cenário.
2. Perguntar sempre: **qual o limiar do cliente?** (`read_timeout`, timeout de upstream, TTL, limite de fila). O evento só explica se **cruza** esse limiar.
3. Preferir a grandeza que **varia com o sintoma** (duração × limiar) à que apenas **aparece junto**.
4. Grandeza derivada («X/min») sai com **duas janelas** e com o **número cru do coletor ao lado** (`cmdstat_*`, `rdb_changes_since_last_save`, `dbsize`), não só com a divisão.
5. **Limite declarado:** medir dose **não identifica autor**. O Redis não registra quem chama o `FLUSHDB`; a alavanca (`WP_REDIS_GRACEFUL true`) continua sem dono aplicado — e dizer isso é parte do laudo, não fraqueza dele.
