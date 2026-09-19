# O artefato que só escreve quando grita (10/09/2026, ronda 405ª DS-Dell)

## O quê
O `ALERTA_CREDITO.flag` do vigia de crédito DeepSeek (P11) **não é um medidor** — é o **diário do último grito**.

Medição de 10/09/2026, com as duas caras no mesmo dia:
- **18:0x (antes do crítico):** o flag dizia `{"nivel":"aviso","saldo_usd":1.69}` enquanto a **última leitura real no log era 0,72** (18:00). O caminho suprimido pelo anti-spam faz `return` antes de gravar (L189-191) e o `est["ultimo_saldo"]` fica só em memória.
- **18:30:03 (crítico disparado):** o log registra `telegram enviado (True): 🔴 CRITICO ... saldo US$ 0,36`; e **o flag passou a dizer `{"nivel":"critico","saldo_usd":0.36}`** — porque o caminho de alerta (L199) **grava**.

## Por quê importa
1. **O flag é verdadeiro só imediatamente depois de um alerta.** Na primeira leitura suprimida seguinte (18:45) ele **volta a mentir**: deixa 0,36 no disco enquanto o saldo já estiver abaixo.
2. **A mentira tem horário marcado.** Quem abrir o flag às 19:00 vê 0,36 e conclui «ainda há fôlego» — quando o número real pode ser **zero**. É a mentira mais perigosa: **conservadora na direção errada** (tranquiliza quem devia correr).
3. **A pergunta certa não é «o valor está certo?», é «quando este arquivo é escrito?»** — o mesmo campo pode ser exato num instante e falso no instante seguinte **sem que nada no arquivo denuncie isso**.

## Como aplicar
- **Flag/estado de alerta se lê SEMPRE com o log ao lado**: carimbo do flag + valor + **última linha de leitura real**. Se os dois divergirem, o log manda.
- **Nomear pelo que o campo É**: `saldo_do_ultimo_alerta` (e `ultimo_saldo_ts`), nunca `saldo`.
- **Gravar o estado em TODA leitura boa**, antes de qualquer `return` de anti-spam; gravar o flag **depois** do envio.
- **Régua geral (família 182·184·187·190·191·198·200·201·204):** antes de confiar num artefato, pergunte **em que caminho do código ele é escrito** — o que não é escrito em todos os caminhos não é estado, é **evento**.
- **Para quem vigia vigias:** o dead-man não pode morar no mesmo credito/cadeia que ele vigia — a ronda do DS-Dell (crédito próprio) lê o carimbo do log a cada 30 min e avisa se emudecer > 35 min.
