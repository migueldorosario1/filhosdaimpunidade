# Entrega de mecanismo exige o teste que o REPROVA — rodado por quem entrega, antes de entregar

- **Data:** 2026-09-10 (02:33 BRT) · ronda 381ª DS-Dell
- **Família:** BUG-20260909-DS-178 (enforcement no push) · BUG-20260909-DS-182 (lock que avisa e não barra) · BUG-20260910-DS-184 (guard §86) — todas a mesma pergunta: **o que a casa desenhou para impedir já impede?**

## O quê (fato datado)
Entreguei no bloco DS-Dell-20260910-005 (ronda 380ª, 02:05) um prompt com o hook `pre-push` que deveria bloquear qualquer push que removesse linha existente no `de_dell.md`. O auditor (XM-20260910-005, 02:22:50) rodou o fixture e **reprovou**: `$2` no pre-push é a **URL do remoto**, não a branch — o `git fetch` recebia refspec inválido — e o `|| exit 0` **liberava** o push quando o fetch falhava. O guard **nunca bloquearia nada**.

## Por quê (causa)
Entreguei o mecanismo pelo **desenho** (o que ele pretende fazer) e não pelo **comportamento** (o que ele faz quando executo). Não rodei o caso que o mecanismo existe para reprovar. Quem testa primeiro é o auditor, e nesse intervalo a casa acredita ter um guard que é decoração.

## Como aplicar (régua)
1. **Antes de escrever «pronto», rode o teste que REPROVA.** Guard que nunca bloqueou nada não é guard — é decoração. A prova é a saída do teste recusando.
2. **Teste mínimo de 4 casos para qualquer trava:** (T1) o caso que deve ser **bloqueado**; (T2) o caso **válido** que deve **passar** (senão a trava vira obstáculo); (T3) a **falha do próprio mecanismo** (aqui: fetch falha) — deve **fechar** (fail-closed), nunca abrir; (T4) **controle** com a trava desligada (`--no-verify`) para provar que a barreira é ela, e não outra coisa.
3. **Fail-open é o defeito silencioso:** todo `|| exit 0` / `|| true` num caminho de verificação transforma falha em permissão. Em trava, falha = bloqueio.
4. **Sintaxe de hook não se adivinha:** no `pre-push`, `$1` = nome do remoto, `$2` = URL; os refs vêm por **stdin** (`local_ref local_sha remote_ref remote_sha`). Confirmar antes de escrever o prompt.

## Prova desta ronda (fixture `.ds_guard_test`, workspace)
- T1 remoção de 1 linha → `PUSH BLOQUEADO ... perderia 1 linha(s) de origin/main: linha B` + exit 1
- T2 UNIÃO (linha restaurada + nova) → push passa, exit 0
- T3 fetch falha → `GUARD: fetch ... FALHOU — BLOQUEANDO (fail-closed)` + exit 1
- T4 `--no-verify` → a remoção passa = controle

## Ref
Bloco DS-Dell-20260910-006 (ponte) · BUG-20260910-DS-185 · XM-20260910-005 (reprovação) · memória viva 381ª.

## ADENDO (02:36 BRT) — 3º defeito, achado por mim ao testar no insumo REAL
`sort` com `LC_ALL=C` e `comm` sob o locale ambiente (`pt_BR.UTF-8`) comparam em ordens diferentes: o `comm` acusa «arquivo não está ordenado» e devolve lixo — no `de_dell.md` real deu **254 falsos positivos** (com `LC_ALL=C`: 0). **Guard com falso positivo bloqueia todo push legítimo e é desligado no primeiro dia — a outra forma de virar decoração.** Correção: `export LC_ALL=C` no topo do hook. **Lição adicional: fixture ASCII não cobre arquivo real com acento — teste o mecanismo no INSUMO REAL antes de declarar pronto.** Provas: fixture T1/T2/T3/T4 + dry-run do hook contra `origin/main` no repositório real (exit 0, zero falso positivo).
