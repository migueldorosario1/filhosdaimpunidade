# Lição 20260911 — O comando não explica o engasgo (quem engasga é o substrato)

**Ronda:** 423ª (11/09/2026 ~06:2x BRT) · **Casos:** BUG-20260911-DS-208 (cache Redis que mata a página), ADENDO-6.
**Antecedentes da mesma caçada:** ADENDO-3 (acertei o gatilho errado) → ADENDO-4 (o save excluído por contraprova) → ADENDO-5 (dose-resposta: 7,5 s → 22 × 500; 0,911 s → nada) → **ADENDO-6 (o comando não é o suspeito)**.

## O quê (o fato medido)
`redis-cli slowlog get 128` (log saturado) na sessão de boot das 03:31, janela **03:36:18 → 06:04:25 BRT**:

- por comando: **MGET 116 · GET 7 · FLUSHDB 4 · SET 1**;
- por duração: **≥1 s = 1** (FLUSHDB 7.498,6 ms, 04:25:29 — o único que matou leitor) · **≥500 ms = 5** (3 FLUSHDB + **SET 627,6 ms** às 04:03:29 + **MGET 603,6 ms** às 06:00:01) · ≥10 ms = **128/128**.

O **SET** e o **MGET** acima de 0,6 s são **operações de UMA chave** — O(1) no Redis. E o slowlog mede **execução no servidor, excluindo I/O de cliente**.

## Por quê (a interpretação)
Um comando O(1) de uma chave não tem trabalho interno que dure 0,6 s. Se a duração aparece, **não foi o comando que demorou: foi a thread única que ficou suspensa** (page-in de página em swap, reclaim do kernel, compactação). Medição do substrato na mesma hora: **Redis com ~28,5 MB em swap** (`VmSwap` 28.520 kB sobre `VmRSS` 484 MB), host com **150 MB livres**, swap do host **1,56 GB/10 GB**, **`vm.swappiness = 60`**, **`vm.overcommit_memory = 0`** (com o aviso do próprio Redis no boot), `maxmemory` 1 GB × `used_memory` 464 MB, `evicted_keys 0`, `st=0` no `vmstat` (sem steal de hipervisor). **Candidato medido, causalidade NÃO provada.**

E o efeito continua sendo de **limiar, não de tipo**: o engasgo de 0,604 s às 06:00:01 deu **zero 5xx** (hora 05 = 0/12.808; hora 06 = 0), enquanto o FLUSHDB de 7,498 s deu **22 × 500** — porque só ele cruzou o `read_timeout` de 1 s do drop-in.

## Como aplicar (a régua)
1. **Não escolha o culpado pelo nome do comando; escolha pelo trabalho que ele faz.** Se uma operação O(1) aparece lenta no slowlog, o problema **não está no comando** — está na máquina que o executa. Vá para o substrato antes de acusar o código.
2. **Quando o sintoma é o cliente morrendo, a pergunta é sempre MAGNITUDE × LIMIAR**, nunca frequência: multiplique a duração medida pelo timeout do cliente. Foi isso que separou o save (longo, mas outro cliente) do FLUSHDB (7,5 s, mesmo cliente).
3. **Distribuição de um log saturado vale mais que o maior registro dele.** O topo (FLUSHDB 7,5 s) sugeria um culpado; a distribuição (4 tipos de comando no mesmo engasgo) provou cenário. Um log cheio é uma amostra: conte os tipos antes de eleger o suspeito.
4. **Meça o substrato na mesma janela do sintoma**, não depois: `VmSwap` do processo, memória livre, `swappiness`, `overcommit_memory`, `st` do `vmstat`. Se o processo tem páginas em swap, "latência do comando" é uma medida enganosa.
5. **Declare o limite:** `VmSwap` é foto e não série; o slowlog ignora comandos abaixo de 10 ms e não registra quem chama o comando. **Correlação de substrato não é sentença.**

## Fecho
Três rondas para chegar aqui: **ADENDO-3 errou o gatilho; ADENDO-4 excluiu o save por contraprova; ADENDO-5 achou a dose; ADENDO-6 tirou o comando do banco dos réus.** O que sobrou de pé não é um culpado — é um **limiar** (1 s) e um **substrato** (memória/swap). A cura do leitor continua sendo a alavanca de 1 linha fora do WordPress: `WP_REDIS_GRACEFUL true`.

**Refs:** ponte `DS-Dell-20260911-013` · `CEREBRO_NODE_BUGS_ATIVOS.md` ADENDO-6 · lições irmãs `20260911_a_dose_separa_a_causa_do_cenario.md` · `20260911_o_save_nao_era_o_gatilho.md`.
