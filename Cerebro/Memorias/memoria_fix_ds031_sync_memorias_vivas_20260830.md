# Memória — Fix DS-031: log técnico completo (30/08/2026, ZM/GLM-5.3)

## Contexto e diagnóstico

- **Gatilho:** ordem do Miguel ~10:00 30/08 ("pedido importante na ponte, o bugDS031, encarregamos você de consertar"). Registro formal: `CEREBRO_NODE_BUGS_ATIVOS.md` BUG-20260829-DS-031 (linha ~1644), dono designado ZM.
- **Sintoma reportado pelos DS:** sync ~:07/:37 "reescreve" `memoria_ds_n_viva.md` para 44 linhas, apagando a ronda commitada minutos antes; DS recupera via `git show <âncora>` toda ronda; 28 reincidências até 10:00 de 30/08.

## Causa raiz (provada por git log)

Sequência no `git log -- cerebro/memorias_provisorias/memoria_ds_n_viva.md`:

```
10:02 Ubuntu  DS-N-20260830-021 ronda 10:00 (300 linhas)
10:07 Miguel  sync: 8964 arquivos (44 linhas)  ← REGRESSÃO
```

Mecanismo no `sync_cerebro_to_github.py` (cron Dell `7,22,37,52 * * * *`):

1. `integrate_remote()`: fetch+rebase → repo correto (300 linhas).
2. `copy_tree(SOURCE/Cerebro → TARGET/cerebro)`: copia a FONTE local por cima — fonte atrasada (44 linhas) porque o pull `sync_cerebro_from_github.sh` (cron `0,15,30,45`) roda ANTES do commit do DS (:02/:32).
3. `git add -A` + commit + push → **regressão publicada**.

Reconciliações append-only existiam apenas para árvores LAURA (`LAURA_MEMORY_DIRS`/`LAURA_OUTPUT_ROOTS`); `memorias_provisorias` não tinha proteção nenhuma. A semântica de prefixo puro (LAURA) NÃO serve aqui: o DS-N edita linhas do corpo da memória (ex.: linha 26 caminho do FAROL, linha 29 "DESTRAVADA ~19:43") — não é append puro.

**Donos por arquivo** (git log por `*_viva.md`): só `memoria_ds_n_viva.md` (autor `Ubuntu` = DS-N na Tencent) e `memoria_ds_ceo_viva.md` (autor `DS Dell`) são commitadas por agentes; outras 11 são fonte-local via sync.

## Correção implementada

`scripts/sync_cerebro_to_github.py` (+100 linhas, commit `946f7281c` — patch escrito pelo ZM às 10:19, commitado pelo AGY-M às 10:20 ao encontrar o worktree editado; backup commitado pelo ZM em `4f65e75df`):

- Constantes: `LIVE_MEMORY_DIRS` = [(Cerebro/memorias_provisorias, cerebro/memorias_provisorias)], `LIVE_MEMORY_RE` = `.*_viva\.md`, `LIVE_MEMORY_HISTORY_DEPTH` (env `CEREBRO_LIVE_MEMORY_DEPTH`, default 40).
- `reconcile_live_memories(source, target)` chamada no `sync_locked()` após `reconcile_laura_outputs`, ANTES do `copy_tree`. Para cada vivo divergente:
  - `_is_known_revision()`: conteúdo da fonte == alguma das últimas N revisões git do arquivo → **repo vence** (fonte curada, `shutil.copy2` repo→fonte).
  - OU `mtime(fonte) < epoch(último commit do arquivo)` (`_last_commit_epoch()`) → **repo vence**.
  - Senão → edição local nova: **preservada** (sobe pelo copy_tree normal).
  - `is_sensitive(repo_text)` → RuntimeError fail-closed.
- Log: linha `🧬 Memórias vivas: N curadas pelo Git, N com edição local nova, N já alinhadas` + `♻️` por arquivo curado.

## Testes e provas

- Sandbox `/tmp/teste_ds031.py` com mini-repo git real (3 revisões, datas 2026-08-29): **6/6 cenários passaram** (cura por histórico; edição local preservada; unchanged; cura por mtime com utime 2020; nova-no-repo não removida + nova-na-fonte intocada; segredo → fail-closed).
- Pré-validação: 13/13 `*_viva.md` em UTF-8 strict.
- Cura do estado real: `git show dec7fcc5e:...memoria_ds_n_viva.md` (300 linhas, ronda DS-N-021) → repo + fonte + commit `4f65e75df` + push origin + nyc (paridade HEAD=origin=nyc= `4f65e75df`, 3/3).
- CEO conferida: atual 268 ≥ último commit DS Dell 266 linhas — íntegra, sem ação.
- Incidente operacional: `.bak` untracked em `scripts/` sujou o worktree → ciclos 10:22 recusaram (`ensure_clean_worktree` fail-closed, correto) → resolvido commitando o .bak (padrão do repo; lição ".bak no repo trava sync" já conhecida — o .bak tem que ser rastreado ou ficar fora).

## Linha do tempo da sessão (BRT)

- ~09:50 — ordem do Miguel; leitura do monitor (Regra 2) + nodo de bugs (Regra 1).
- 10:0x — git log prova o padrão; leitura dos 2 scripts (to_github + from_github) + crontab.
- 10:16 — estado: fonte=repo=44 linhas (28ª destruição às 10:07); dec7fcc5e=300.
- 10:19 — backup `.bak_pre_ds031_20260830` + patch aplicado.
- 10:21-25 — sandbox 6/6 ✅; ciclo cron 10:22 recusou (worktree sujo pelo .bak).
- 10:20 — **commit `946f7281c` do meu patch pelo AGY-M** (anunciado no AGY-20260830-040 como "FIX DS-031 INTEGRADO").
- 10:2x — descoberta da colisão benigna com AGY-M/outra sessão ZM (debate ponte 2+2); leitura de ZM-004/ZM-005/AGY-040 no repo (fonte atrasada — pull 10:15 anterior).
- 10:3x — restauração 44→300 na fonte+repo; commit `4f65e75df` (.bak + memória); push origin+nyc.
- 10:37 — 1º ciclo automático com o fix (adendo com resultado).
- 11:07 — prova de fogo (ronda DS-N 11:00 + sync 11:07; adendo).

## Adendos de verificação

### ADENDO 1 — Ciclo 10:37 (1ª rodada do fix em produção): CURA AO VIVO CONFIRMADA ✅

Log do ciclo (10:37:43): `🧬 Memórias vivas: 1 curadas pelo Git, 0 com edição local nova, 12 já alinhadas` + `♻️ cerebro/memorias_provisorias/memoria_ds_n_viva.md`.

Sequência real: 10:27 ZM restaura 300 (commit `4f65e75df`) → 10:32 DS-N commita ronda 10:30 = **310 linhas** (`9377ab83b`, autor Ubuntu) → 10:37 sync: fetch+rebase põe o repo em 310, reconcile vê a fonte em 300 (revisão antiga presente no histórico) → **cura a fonte para 310**; copy_tree copia 310==310 → o commit de sync `70284a961` NEM TOCA no arquivo (git log do arquivo pula de `9377ab83b` para `4f65e75df`). Push concorrente com o ACK da ponte (`a0fb537b9`) resolvido por rebase na tentativa 2/6.

**Antes do fix esse cenário exato (:32+:37) era a 29ª destruição em potencial.** DS-Dell ACKnou o fix no commit da ronda 10:30 (`6f326a0f2`, 10:35: "fix DS-031 curado").

### ADENDO 2 — Prova de fogo 11:0x (ronda DS-N 11:00 → sync 11:07): APROVADA ✅ + CEO curada de bônus

- 11:02 — DS-N commita ronda 11:00: **319 linhas** (`0b5d1f3db`, autor Ubuntu).
- 11:07 — sync: `🧬 Memórias vivas: 2 curadas pelo Git, 11 já alinhadas` — curou `memoria_ds_ceo_viva.md` (DS-Dell tinha commitado a ronda dele e a fonte estava atrasada; outro ♻️ ao vivo) e manteve a ds_n alinhada via pull. **O commit de sync `11:07 — 8979 arquivos` NÃO TOCOU na ds_n** (log do arquivo termina no commit do DS-N).
- Curva final no git log da `memoria_ds_n_viva.md`: 247→[sync 44]→267→[sync 44]→280→[sync 44]→290→[sync 44]→300→[sync 44] (7 regressões até 10:07) → **300 (cura ZM 10:27) → 310 (DS-N 10:32, atravessou o :37 intacta) → 319 (DS-N 11:02, atravessou o :07 intacta)**. Zero destruições pós-fix em 2 ciclos completos do padrão do bug.
- Working tree 11:10: ds_n=319, ds_ceo=285. Estado íntegro nas duas memórias que o bug atingia.

**Conclusão: DS-031 corrigido e provado em produção. Monitoramento 24h de cortesia segue (rondas 30/30); nenhuma ação esperada.**

## O que falta / próximos passos

- Monitorar 24h de rondas 30/30; se qualquer `*_viva.md` regredir, reabrir DS-031.
- Registro no `CEREBRO_NODE_BUGS_ATIVOS.md` → ✅ CORRIGIDO-AGUARDANDO-24H; linha no `CEREBRO_NODE_ATUALIZACOES.md`; linha no `MONITORAMENTO_DE_TRABALHO.md`; ACK na ponte (de_dell via commit git).
- DS-N/DS-Dell podem aposentar o ritual de recuperação por `git show` (a fonte auto-cura); manter o hábito de conferir o append no início da ronda é barato e recomendável por 24h.

— ZCode Miguel (GLM-5.3) · 30/08/2026 · repo `cerebro-miguel` branch `main`
