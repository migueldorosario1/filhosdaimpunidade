---
name: feedback-proveniencia-modelo-ambiente-papel-separados
description: "Em todo recibo/cartinha/log JSONL, separar campos model_identity (modelo real) + environment (zcode/claude-code/codex/etc, é ambiente não autor) + actor_role (proposer/reviewer/authorizer/executor/verifier). ZCode NÃO é modelo — é ambiente que roda Qwen 3.8, GLM 5.2, Kimi K3"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 7a8b86e8-615f-48dd-924d-5e86f182a869
---

**A partir de 07/08/2026 01:55 BRT, todo recibo/cartinha/log/report meu separa 3 dimensões da proveniência: MODELO (Claude/Grok/Qwen/GLM/Kimi/Codex) + AMBIENTE (zcode/claude-code/codex/antigravity/telegram_kimi_bot) + PAPEL (proposer/technical_reviewer/authorizer/executor/verifier).**

**Why:** Codex R4 07/08 01:22 BRT ("Nova carta ao Claude e à Trindade — Revisão de proveniência e prontidão da autocura V4 Mídia") revelou que respostas R1-R3 assinadas como "Kimi K3/ZCode" no fórum guarda-chuva `forum_banco_midia_v4_real_vision_autoaprendizado_20260806.md` foram na verdade do **Qwen 3.8 rodando no ZCode**. ZCode é ambiente/CLI (assim como claude-code é meu ambiente), não é modelo. Eu segui a assinatura literal e reproduzi o erro nas minhas cartas + memórias + reports das últimas horas. Miguel/Codex: "Se não sabemos qual modelo propôs, revisou ou aprovou uma regra, não temos um ledger confiável."

**How to apply:**

**Schema mínimo obrigatório em cada evento estruturado:**
```json
{
  "actor_roles": {
    "proposer": ["<modelo>"],
    "technical_reviewer": ["<modelo>"],
    "authorizer": ["miguel"],
    "executor": ["<modelo>"],
    "verifier": ["<modelo>"]
  },
  "decision_state": "proposed|technically_approved|authorized|executed|verified|rolled_back",
  "authorization_ref": "chat_miguel_2026-08-07T01:22-03:00" | null,
  "delivery_state": "planned|in_progress|delivered|accepted",
  "model_identity": {
    "model": "claude-opus | grok | qwen3.8 | glm5.2 | kimi-k3 | codex | max",
    "environment": "zcode | claude-code | codex | antigravity | telegram_kimi_bot | wp_admin_miguel",
    "session_ref": "<slug identificador de sessão>"
  }
}
```

**Regras derivadas:**
1. **ZCode não é autor** — é ambiente. Escritas via ZCode devem indicar qual modelo estava rodando naquela sessão (Qwen 3.8 / GLM 5.2 / Kimi K3).
2. **`technically_approved` ≠ `authorized`** — aprovação técnica de um modelo NÃO autoriza deploy. Só `authorizer=miguel` + `authorization_ref` explícita autorizam.
3. **`executed` exige executor identificado por modelo real**, não por ambiente.
4. **`verified` exige pós-condição comprovada** (link 200, hash SHA-256, teste passando, etc.) — não basta modelo dizer "verifiquei".
5. **README ou promessa NÃO contam como delivery_state=delivered.** Só código executável + testes passando + rollback documentado.
6. **Cada modelo assina o que realmente escreveu.** Se atribuo trabalho a modelo errado (como eu fiz na R1 atribuindo a "Kimi K3" o que era Qwen 3.8), **retificação obrigatória por supersessão** (novo evento com `reason_code=proveniencia_incorreta`), nunca delete.

**Casos concretos do meu turno 06-07/08/2026:**
- ❌ Errei atribuindo "fix Kimi §17" ao Kimi K3 — era **Qwen 3.8 via ZCode**.
- ❌ Meu `feedback_ponte_imagens_v3_regime_autonomo.md` diz "Kimi K3 (ZCode)" — termo NÃO EXISTE como autor.
- ✅ Ponte Autônoma inaugural (06/08 17:31 aderido + 06-07/08 entrega lote 6 fotos) foi genuinamente **Kimi K3 Desktop** — este atribuí corretamente.

**Retificação aplicada:**
- Nova cartinha `cartinha_claude_R4-PROVENIENCIA-PRONTIDAO-AUTOCURA-V4-MIDIA_20260807_0155.md` reconhece erro na R1.
- Próxima passagem: atualizar `feedback_ponte_imagens_v3_regime_autonomo.md` trocando "Kimi K3 (ZCode)" por menções específicas (Qwen 3.8 via ZCode para o helper `v4_hero_cota.py`; Kimi K3 Desktop para a Ponte Autônoma).
- JSONL bugs recebe retificação por supersessão (novo evento tag `retificacao_proveniencia`, não delete histórico).

**Autoridade e limites:**
- Minha opinião técnica NÃO autoriza produção — nem meu "ACEITO" numa cartinha significa "faça".
- Nenhum gate será obrigatório no meu loop Vigília antes de decisão explícita do Miguel (formato `[MIGUEL-AUTORIZA-GATE-X-YYYY-MM-DD-HH:MM]` no canal).
- Nenhuma reescrita editorial será tratada como L1 — só reposicionamento HTML/link determinístico é L1.
- Publish é telemetria (`evidence: weak_telemetric`), não gold. Gold só via aceite humano explícito ou hash oficial.

**Regras irmãs:**
- [[feedback-autoaprendizado-governado-ativo]] (JSONL correcoes ativo)
- [[feedback-ponte-imagens-v3-regime-autonomo]] (será atualizado corrigindo autoria)
- [[feedback-ponte-claude-kimi-arquivo-por-turno]] (Kimi K3 Desktop, correto)

**Anti-pattern a evitar:**
- Copiar assinatura literal de outros documentos sem verificar (foi o meu erro).
- Usar "ZCode" ou "AGY CLY" como autor — sempre pedir/registrar o modelo real por trás.
- Apresentar aspiração como compromisso (foi meu erro no `gate_pre_publish.py v0.1 - 48h`). Se planned, dizer planned.
