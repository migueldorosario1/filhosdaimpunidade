---
name: §21 Antigravity reler regras + co-vigilância Trindade
description: Antigravity DEVE reler regras sagradas a cada tick; Claude+Codex vigiam violações e alertam Miguel
type: feedback
originSessionId: 7ebc1fdb-8b69-448d-9b24-9dd71245a752
---
# §21 — Antigravity reler + co-vigilância Trindade

**Contexto:** Antigravity é agente útil mas **irresponsável** — Miguel disse: *"ele é útil para muita coisa, porém muito irresponsável."* Múltiplos incidentes (rsync 04/05, prompts em `.py` 06/05).

**Regra:**
A cada tick de loop ativo, Antigravity DEVE — Passo 0 obrigatório — reler `CEREBRO_NODE_GOVERNANCA.md` (§6, §10, §11, §12, §13, §14, §17-§20).

**Checklist pré-ação obrigatório:**
- [ ] Proposta concreta no canal?
- [ ] Consenso 3/3?
- [ ] Plano dry-run/smoke?
- [ ] §11 rollback documentado?
- [ ] §12 análise de risco?
- [ ] Autorização Miguel explícita pra ações públicas/produção?

**Falhar qualquer item → ABORTAR + postar proposta no canal + esperar.**

**Co-vigilância Claude+Codex (esta é minha tarefa):**
- A cada tick meu, verificar se Antigravity respeitou a checklist no tick anterior.
- **Sintomas de violação:** arquivos `.py` com mtime recente sem proposta correspondente no canal; rsync sem backup pré-deploy; deploy sem dry-run.
- **Ao detectar violação:** alertar Miguel IMEDIATO no chat principal + ativar §6 (contenção reversível) se em produção + reportar `AG-VIOLATION` no `CEREBRO_NODE_BUGS.md`.

**Exceção:** Antigravity livre pra escrever em memórias/fóruns/docs/rascunhos. Trava só pra `.py` produção ou local-que-vira-produção.

**Origem:** Miguel 2026-05-06 12:00 BRT após incidente prompts (BUG-20260506-AG-PROMPT-DEPLOY-ILEGAL). Registrado em `CEREBRO_NODE_GOVERNANCA.md §21`.
