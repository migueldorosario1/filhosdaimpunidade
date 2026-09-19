# Fórum — Comunicação limpa: Protocolo v2 do monitor + cura do gate do sync — 15/09/2026

**Autor:** ZCode/GLM-5.3 · **Ordem Miguel 15/09 ~18:1x:** "encontra uma solução para impedir esses tropeços no monitor de trabalho. A comunicação precisa ser limpa. Está meio bagunçado, com agentes brigando entre si."
**Memória gêmea:** `Memorias/memoria_monitor_comunicacao_limpa_20260915.md`

## 1. Os tropeços (diagnóstico com prova na sessão)

1. **Edições simultâneas no monitor** (2× na sessão: "File has been modified since read") — N sessões editam o mesmo arquivo sem lock; última escrita apaga a anterior.
2. **Quadro virou mural**: renovação 48h vencida desde 31/08; 39 linhas ✅ acumuladas; linhas de até 2.002 caracteres — leitura improdutiva.
3. **Gate do sync travando por telemetria** (incidente ZM-20260915-008, recorrente a cada 30min): porta_voz_zm escreve `cerebro/monitoramento_horario/*.jsonl` direto no repo sem commitar → `ensure_clean_worktree` recusa → sync 15min falha até intervenção manual.
4. **Commit local não-pushado é frágil** (caso ao vivo na sessão): 1ª cura do gate commitada localmente foi **apagada por reset/pull de sessão paralela** (correção editorial 271172 trabalhando no mesmo clone). Push imediato é obrigatório.

## 2. Soluções implantadas (todas provadas)

### 2.1 monitor_update.py — escrita segura no monitor (protocolo v2)

- `Cerebro/Ferramentas/monitor_update.py`: **flock exclusivo** (`/tmp/monitor_update.lock`) + **escrita atômica** (tmp + `os.replace` — nunca meio escrito).
- CLI: `inicio <ID> "<quem/modelo>" "<o que faz>"` · `nota <ID> "<texto>"` · `fim <ID> "<resultado>"`.
- Formato: 1 linha/sessão com ID curto único; ≤260 chars (script RECUSA linha longa); detalhe em fórum próprio; **só toca a linha do próprio ID** (linha alheia intocável por construção).
- Prova: 2 `nota` simultâneas disparadas em paralelo — as duas "ok" (serializadas pelo lock), arquivo íntegro.

### 2.2 Renovação do quadro (a vencida + a formativa)

- Morto: `MONITORAMENTO_DE_TRABALHO_2026_09_15_1815.md` (cópia integral do anterior, 31KB, histórico preservado; diff morto×vivo conferido idêntico no fechamento).
- Vivo novo: header com o **PROTOCOLO v2** (script obrigatório, ≤260 chars, linha alheia sagrada, push imediato, renovação 48h) + quadro só com ativos.

### 2.3 Cura do gate do sync (incidente ZM-20260915-008 RESOLVIDO)

- `scripts/sync_cerebro_to_github.py` — `ensure_clean_worktree`: se TODOS os sujos forem `cerebro/monitoramento_horario/**` → **auto-commit restrito** ("telemetria: auto-commit monitoramento_horario") e segue; qualquer outro caminho → recusa como antes (fail-safe intacto — provado: recusou quando o próprio fix estava sujo).
- 🔴 **bug sutil curado no caminho**: o `dirty = stdout.strip()` (herança do código original) comia o espaço inicial da linha unstaged `" M path"` → path deslocado ("erebro/…") → auto-commit nunca disparava. Parsing agora no output CRU.
- Commits: `9a86f8182` (gate v1, apagado por sessão paralela, reaplicado), `10ec076b2` (fix parsing), `e09bfce44` (1º auto-commit real de telemetria). Prova final: "Gate: auto-commit de telemetria (1 arquivo)" + "GitHub alinhado" + "Espelho NYC alinhado" na mesma corrida.
- Backup da versão anterior: `~/.sync_cerebro_backup_pre_gate_20260915.py`.

## 3. Estado / o que falta / o que preciso do Miguel

- **Pronto e provado:** tudo acima no ar. Nada pendente de engenharia.
- **Adoção pela casa:** avisada na ponte (bloc ZM com o protocolo v2). Agentes que ainda editarem o monitor na mão não quebram nada (arquivo continua markdown), só não ganham a proteção do lock.
- **Preciso do Miguel:** nada obrigatório. Opcional — quem mantiver hábito manual pode ser cobrado pela regra nova (a casa aprende pela ponte).
