# Lição — 10/09/2026 · O contador que engole o erro conta o erro (e devolve um número plausível)

**O QUÊ (o fato, com data e prova):**
Na abertura da ronda **400ª DS-Dell (10/09, ~16:0x)** rodei a checagem do **BUG-197** («a barreira do BUG-185 existe na física onde o dano nasce?») por uma linha só, a partir do Dell, com o transporte do WP-CLI:

```
ssh cafezinho-wp "find ~/cerebro-miguel/.git/hooks -type f ! -name '*.sample' 2>&1 | wc -l"
```

e ela devolveu **`1`**. Por um instante isso lê como «há 1 hook instalado» — exatamente o que a casa quer saber, e exatamente o oposto do fato. Fui atrás e o `1` tinha três camadas, todas minhas:

1. **`ssh cafezinho-wp` não é o Dell.** O alias cai em **`us65.serverdo.in`** (`hostname`); ali `~` = **`/root`** e **não existe `cerebro-miguel`** — o `find` falhou.
2. **`2>&1` fundiu o erro no fluxo de dados.** A única linha que o `wc -l` contou foi a **mensagem de erro** do `find`.
3. **`wc -l` não distingue conteúdo de falha:** contou 1 e o pipeline fechou com **exit 0** — o número saiu limpo, sem alarme.

**Prova controlada (2 comandos):** `find /caminho/que/nao/existe -type f ! -name '*.sample' 2>&1 | wc -l` = **1**, e o conteúdo contado é literalmente `find: '/caminho/que/nao/existe': Arquivo ou diretório inexistente`. Com `2>/dev/null` e o caminho certo: **hooks reais na física do Dell = 0**.

**POR QUÊ IMPORTA (impacto real, não estético):**
1. **Falso positivo no lugar mais caro possível.** A verificação que responde «a barreira está instalada?» devolveu **sim** quando a resposta é **não**, e devolveu no mesmo dia em que a casa discute instalar o guard (BUG-178/185/197, 25+ remoções em ~38 h). Um «1 hook» relatado de boa-fé teria fechado o BUG-197 sem que nada existisse no disco.
2. **É a 7ª ocorrência da família «o mecanismo responde sem ter feito»** (182 lock que avisa e não barra · 184 pré-condição que não pré-condiciona · 187 alerta cujo gatilho mata o alertador · 190 filtro aceito e ignorado · 191 sticky prependido · 198 medidor read-only que virou a carga) — **e a 2ª do meu próprio instrumento no mesmo dia (198 e agora 200)**. A família deixou de ser sobre o código dos outros e passou a ser sobre o meu.
3. **O caminho não identifica a máquina.** `~/cerebro-miguel`, `$HOME`, `/root`: **a mesma string resolve em físicas diferentes** conforme o transporte. Toda checagem de integridade desta casa é uma pergunta sobre **uma física** — e a pergunta sem `hostname` não é pergunta, é sorte.

**COMO APLICAR (regra operacional, adotada a partir desta ronda):**
- **Nunca `2>&1 | wc -l` em medição.** Separe os fluxos (`2>/dev/null` quando o erro não é o objeto) e **mostre o conteúdo contado** quando o número for a resposta. Se o erro for o objeto, conte-o por **padrão explícito** (`grep -c '^find:'`), nunca por linha total.
- **`set -o pipefail`** (ou `bash -o pipefail`) quando a montante pode falhar: o pipeline não pode fechar verde porque o último elo é `wc`.
- **Nomeie a física em toda medição:** `hostname` no mesmo comando do dado (régua nova, irmã do «carimbo com `date` no mesmo comando que grava»). Um resultado sem host é um resultado sem endereço.
- **Confirme o caminho antes de medir:** `test -d <dir> || echo AUSENTE` — e trate `AUSENTE` como resposta, não como ruído.
- **Regra geral:** um número plausível é o esconderijo perfeito para uma falha; **antes de acreditar no número, pergunte qual linha foi contada.**

**REFERÊNCIAS:** BUG-20260910-DS-200 (novo, meu, esta ronda) · BUG-20260910-DS-198 (`array_merge` × `+`, o medidor como carga) · BUG-20260910-DS-197 (barreira instalada na física errada) · BUG-20260910-DS-185/178 (guard `pre-push`; 25+ remoções de blocos; fix estrutural é a pendência nº 1, dono ZM) · lições irmãs `20260910_medidor_read_only_tambem_e_carga.md`, `20260910_barreira_instalada_na_fisica_errada.md` e `20260910_commit_nao_e_entrega.md` · bloco DS-Dell-20260910-026 (ponte).
