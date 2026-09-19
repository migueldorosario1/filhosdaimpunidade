# Memória técnica — Comunicação limpa: monitor v2 + gate do sync — 15/09/2026

**Autor:** ZCode/GLM-5.3 · **Fórum gêmeo:** `Foruns/forum_monitor_comunicacao_limpa_20260915.md`

## 1. Ferramenta nova

`Cerebro/Ferramentas/monitor_update.py` (75 linhas, sem dependências): flock EX em `/tmp/monitor_update.lock` + escrita atômica (tempfile.mkstemp na MESMA pasta do monitor + os.replace). CLI inicio/nota/fim com `<ID>` único por linha; recusa linha >260 chars; regex `^\|\s*<ID>\s*[|·]` localiza a própria linha — nunca toca linha alheia (por construção). Prova: 2 notas paralelas ok.

## 2. Mudanças no repo (commits)

- `9a86f8182` — gate auto-commit telemetria (2ª aplicação; a 1ª, commit local, foi APAGADA por reset de sessão paralela — lição: **commit local sem push é frágil no clone compartilhado; push imediato**)
- `10ec076b2` — fix do parsing: **usar stdout CRU do porcelain** (`raw = ...stdout`), não o `.strip()` — o strip come o espaço inicial da 1ª linha unstaged (" M path" → "M path") e desloca `l[3:]` em 1 caractere ("erebro/…" ≠ "cerebro/…"), fazendo o startswith falhar SEMpre que o único sujo for unstaged. Bug clássico de off-by-one por strip prematuro; debugado com `repr()` no fluxo real do módulo (importlib).
- `e09bfce44` — 1º auto-commit real de telemetria pelo gate.
- Backup pré-mudança: `~/.sync_cerebro_backup_pre_gate_20260915.py`.

## 3. Renovação do monitor

- Morto `MONITORAMENTO_DE_TRABALHO_2026_09_15_1815.md` = cópia integral do vivo antigo (31KB/39 ✅); diff morto×vivo idêntico no fechamento (janela de corrida).
- Vivo novo: protocolo v2 no header (script obrigatório; ≤260 chars; linha alheia sagrada; push imediato; renovação 48h com diff).

## 4. Receitas / armadilhas para o futuro

- `git status --porcelain`: XY+espaço+path → path em `[3:]` SÓ no output cru; NUNCA `.strip()` o bloco antes de fazer splitlines para parsing posicional.
- Clone compartilhado por N sessões: qualquer commit = pull --rebase --autostash + commit + PUSH no mesmo fôlego; reset/pull de terceiro apaga trabalho local não-pushado (aconteceu: perda de 1 commit, reaplicado).
- Fail-safe do gate provado nos dois sentidos: recusou quando havia sujeira não-telemetria (meu próprio fix sujo), auto-commitou quando só telemetria.
- Teste de gate isolado: `importlib.util.spec_from_file_location` + `exec_module` + chamar `ensure_clean_worktree(Path('.'))` — sem rodar o sync inteiro.
