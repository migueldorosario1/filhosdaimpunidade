# 🔧 Memória técnica — Rondas DS: final cortado + assinatura genérica (31/08/2026)

Sprint: corrigir relatórios DS de 30/30 no Telegram (final cortado em 700 chars + "DS-ronda" sem nome). ZCode/DeepSeek.

## Causa raiz (script, não a LLM)

`/home/migueldorosario/Downloads/Antigravity Google/ronda_30min.sh` (cron `*/30`, dsh headless com `ronda_30min_prompt.md`):
```bash
RESUMO="$(printf '%s' "$OUT" | tr '\n' ' ' | sed ... | tr -s ' ' | cut -c1-700)"
--send "📊 [DS-ronda $(date '+%d/%m %H:%M')] ${RESUMO}"
```
- `cut -c1-700` = amputação cega SEMPRE no meio (relatório ~1.400 chars).
- `tr '\n' ' '` = formatação destruída (bloco corrido).
- `[DS-ronda ...]` = assinatura genérica — o Miguel quer o DS específico: **DS Miguel (Dell)**, DS Celular, DS Nuvem, DS Laura.

## Correção (ronda_30min.sh — backup `.bak_pre_assinatura_corte_20260831`)

- `head -c 3700` com `…` se estourar; sed de markdown por linha; `awk 'NF'` remove vazias (preserva quebras).
- Assinatura automática: se o fim do resumo não tiver `— DS ... BRT`, apenda `\n— DS Miguel (Dell) · $(date '+%Y%m%d %H:%M:%S') BRT` (case pattern `*"— DS"*"BRT"*`).
- Log de auditoria: `telegram-enviado: <200 primeiros chars>` no `/tmp/ronda_30min/YYYYMMDD.log`.
- Teste da montagem com OUT fake (bash -n + echo do resultado) antes de aplicar.

## Prompts

- `ronda_30min_prompt.md` (Dell): encerramento exige relatório terminando com `— DS Miguel (Dell) · AAAAMMDD HH:MM:SS BRT` (date real); nunca acabar no meio de frase; script assina se esquecer.
- `ronda_dsn_prompt.md` (Tencent, backup `.bak_pre_assinatura_20260831`): regra dura nova — toda mensagem ao Miguel termina com `— DS Nuvem Chefe (DS-N Chefe) · carimbo`; nunca cortar o final (limite ~3900; encurtar resumindo o meio).

## Cura do repo ~/cerebro-miguel (rebase travado — receita da memória repo-cerebro-rebase-travado)

Estado: HEAD solto "(no branch, rebasing main)", main local 3 commits únicos, origin/main 62 à frente; pushes da escuta/sync falhando (prova: entrada_1099 e conversa 09:04 não estavam no GitHub).
Cura: `git diff origin/main...HEAD --name-only` → 151 arquivos únicos salvos em `/tmp/cerebro_head_solto_20260831_092354/` → `git rebase --abort` (rc 0) → `git reset --hard origin/main` (6f32ee3d3) → reaplicação bulk exceto 3 críticos (de_dell.md, ponte_health.md, conversa_48h.jsonl) → merge dos 3: de_dell = união limpa SEM marcadores (6840+189 linhas; marcadores removidos mantendo os 2 lados), conversa_48h = +2 linhas ordenadas por ts, ponte_health = +2 linhas → bloco REGRA DS-ASSINATURA apendado (⚠️ lição: heredoc SEM aspas executa backticks — usar <<'EOF' ou python) → `git add cerebro/ && git commit && git fetch && git pull --rebase && git push` → **becdcf316** no GitHub (161 arquivos, +405/−90).

## Validação

- A ronda das 09:30 (cron) roda com o script novo — conferir `telegram-enviado:` no log `/tmp/ronda_30min/20260831.log` e a mensagem no Telegram do Miguel (completa + assinada "DS Miguel (Dell)").
- bash -n OK + teste de montagem OK antes da ronda.

## Pendências

- DS Laura e DSC aplicarem a regra nas rondas deles (bloco ZM-20260831-001 na ponte).
- Observar 1-2 rondas para confirmar estabilidade.
