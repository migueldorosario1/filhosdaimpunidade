---
name: feedback-ponte-canonica-cerebro-miguel-20260829
description: PONTE OFICIAL da Trindade vive em cerebro-miguel/cerebro/Foruns/ponte_laura_completa/ (repo canônico) — JAMAIS escrever em Antigravity Google/Cerebro/Foruns/ponte_laura_completa/ (sync bloqueado)
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 9597853d-470e-434b-a836-f9a921a9a387
---

**REGRA:** Toda escrita em canais de ponte da Trindade (de_dell.md, de_laura.md, canal_trindade.md, estado/, ledger/, baleia_azul/, ponte_imagens_RESERVA.md) deve ser feita em `/home/migueldorosario/cerebro-miguel/cerebro/Foruns/ponte_laura_completa/` e pushada via `git push origin main` no repo `github.com/migueldorosario1/cerebro-miguel` (private). **JAMAIS** escrever em `/home/migueldorosario/Downloads/Antigravity Google/Cerebro/Foruns/ponte_laura_completa/` — o repo `filhosdaimpunidade` (deploy-main) NÃO é canal de ponte válido, mesmo tendo os arquivos localmente. Fluxo obrigatório: `cd ~/cerebro-miguel && git pull --rebase origin main && Edit + git add SELETIVO (nunca -A, cofres em Cerebro/Cofres/ e Outros/chaves/ não podem subir mesmo em repo privado) + git commit + git push origin main`.

**Why:** O script `~/cerebro-miguel/scripts/sync_cerebro_to_github.py` (cron `7,22,37,52 * * * *`) tem exclusão EXPLÍCITA no código:
```python
if any(x in f.parts for x in [..., "ponte_laura_completa", "ponte_trindade_daemon", "ponte_manus_miguel"]):
    continue  # pontes = append-only por GIT exclusivo (bug ZL-027)
```
A exclusão é proposital (bug ZL-027 15/08: sync apagou 36 linhas do RESERVA porque cópia local estava atrasada). Efeito colateral: quem escreve em `Antigravity Google/Cerebro/Foruns/ponte_laura_completa/` escreve pro nada — nunca sobe. Em 28/08 eu (CM) escrevi CM-003/004/005/006 (recado Baleia + ordem ZL editor + assunção Loop Miguel + delegação publish) neste path errado. Ficaram 14h invisíveis à Trindade Laura. DS diagnosticou em 18 rondas seguidas (DS-005 03:30 → DS-023 11:45); só descobri quando Miguel perguntou 29/08 11:00 "como funciona a ponte hoje?". Miguel ordenou migração 12:10 e formalizei via CM-20260829-001 (bloco em ambos os canais + 2 cartas ao DS).

**How to apply:**
1. **Antes de escrever qualquer bloco de ponte:** confirmar `pwd` está em `~/cerebro-miguel` E path do arquivo começa com `cerebro/Foruns/ponte_laura_completa/`.
2. **Antes de commit:** `git diff --cached --stat` — validar que só os arquivos da ponte estão staged. Se aparecer algo de `Cerebro/Cofres/`, `Outros/chaves/`, `.env*`, ABORTAR e refazer add seletivo.
3. **Se ferramenta/hábito antigo escrever em `Antigravity Google/Cerebro/Foruns/ponte_laura_completa/`:** PARAR, mover conteúdo pro canônico, commit no canônico, deletar do path antigo.
4. **Path antigo é espelho passivo apenas** (recebe REVERSE sync do cerebro-miguel via `sync_cerebro_from_github.sh` cron `0,15,30,45`). Ler dele é OK — mas até 15min defasado. Escrita = zero.
5. **Se outro agente (DS, AGY-M, futuras sessões CM) me sinalizar "path errado" ou perguntar "por que não vejo teu bloco?":** confirmar hipótese IMEDIATAMENTE, não descartar. Foi o DS quem viu antes de mim.
6. **Regra do Miguel (Emenda TENSÃO 26/08 aplicada aqui):** erro repetido pelo mesmo agente é mais grave que original — esta memória é o gate visível [[feedback-gate-visivel-para-toda-licao-20260818]] contra reincidência. Se detectar-me escrevendo no path errado numa sessão futura, esta memória deve barrar.

**Cerebro-miguel = ecossistema Cafezinho canônico.** Filhosdaimpunidade = repo do livro do Miguel ("Filhos da Impunidade"), nada a ver com operação Cafezinho — foi confusão minha durante meses.

Ver também: [[feedback-tensao-constante-autoaprendizado-memoria-bugs-20260826]] · [[feedback-check-cm-ponte-laura-a-cada-loop-20260822]] · [[project-credenciais-em-cerebro-miguel-repo-privado-arquitetura-autorizada-20260818]] (cofres no mesmo repo, mesma razão de não subir cegamente).
