# Leitura da ponte em HOLD non-ff — e os dois erros simétricos da conferência de presença

**Data:** 10/09/2026 · **Autor:** DS Miguel (Dell) · **Ronda:** 385ª DS-Dell
**Família:** BUG-20260909-DS-178 (blocos comidos) + lição `20260910_presenca_de_bloco_le_se_cabecalho_nao_a_tag.md`

## O quê (vivido na mesma abertura, em ~3 minutos)

1. **A árvore de trabalho não é a casa quando o clone está em HOLD non-ff.** Às 05:30 o `tail` do `de_dell.md` da minha árvore terminava nos blocos das 05:22 e **não continha** o `DS-Dell-20260910-010` (ronda 384ª, 05:04) nem os blocos dos vizinhos que existiam no `origin/main`. O clone local estava num ramo divergente do remoto (base comum `4b20bd9c5`) — a ronda anterior existia, tinha sido publicada e eu não a via.

2. **A conferência de presença errou nos DOIS sentidos, no mesmo dia:**
   - **Falso POSITIVO (ronda 382ª):** buscar a *tag* (`DS-Dell-20260910-006`) devolveu «presente» — mas a ocorrência era **a citação da tag dentro do alerta de remoção do XM**. O bloco havia sido removido; a tag aparecia exatamente porque alguém denunciava a remoção.
   - **Falso NEGATIVO (esta ronda):** buscar o **cabeçalho** com padrão `^\[10/09/2026 [0-9:]+ BRT\]` declarou **001–005 AUSENTES** — porque os meus próprios cabeçalhos informais usam `00:0x` e `02:0x`, que **não casam** com `[0-9:]+`. Os **12 cabeçalhos estavam presentes** no `origin/main`. Foi a **busca literal do id** que desfez o erro — antes de eu «restaurar» o que nunca faltou.

## Por quê importa

- Um leitor que só lê a árvore acha que a casa é menor do que é: **repete a ronda do vizinho (e a própria) pensando que é nova** e reporta estado atrasado ao dono.
- Uma régua de presença que mente **nos dois sentidos** é pior que régua nenhuma: o falso positivo faz restaurar/re-appendar bloco que já está lá (polui o log vivo e pode duplicar); o falso negativo faz **restaurar o que não falta** ou **deixar passar a remoção real** por já ter «conferido».
- Em HOLD de git, o risco deixa de ser só «alguém apagou»: passa a ser **«eu li a fonte errada e agi sobre ela»**.

## Como aplicar

1. **Na abertura da ronda, em HOLD non-ff:** `git fetch` e ler `git show origin/main:<arquivo>` (ou `git log -p origin/main -- <arquivo>`). O `tail` no arquivo da árvore é **hipótese**, não estado.
2. **Presença se confere em duas passadas, na origem:** (a) **busca literal do id** (conta ocorrências e inspeciona as linhas — citação não é bloco); (b) **cabeçalho datado com padrão PERMISSIVO** que reconheça o formato real do emissor (aceitar `0x`, `~`, prefixos e datas aproximadas dos nossos blocos).
3. **Ausência só se declara depois de as duas passadas falharem.** Antes de restaurar, provar a ausência com a busca literal; restaurar a partir de leitura da árvore é proibido.
4. **Não empurrar histórico alheio em HOLD:** quando a árvore local tem commits não publicados de outro agente (ex.: a linhagem local do XM), a minha escrita sai **em cima do `origin/main`** (worktree/commit próprio), nunca de um rebase que arraste os commits do vizinho para o remoto sem a decisão dele.
