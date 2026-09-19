---
name: feedback-recibo-ledger-sempre-preventivo-nunca-aguardar
description: "Recibo v0.1.1 no ledger media_ledger é SEMPRE emitido preventivamente, NUNCA aguarda autorização Miguel. Faz parte do processo de auto-aprendizado e autocura. Autorização Miguel é orthogonal (só necessária pra `decision_state=executed/verified` em produção)"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 7a8b86e8-615f-48dd-924d-5e86f182a869
---

**A partir de 07/08/2026 10:15 BRT, todo recibo v0.1.1 no ledger `media_ledger/inbox/claude/` é emitido PREVENTIVAMENTE. NUNCA perguntar autorização Miguel antes de emitir.**

**Why:** Miguel 07/08 10:12 BRT (chat, após eu perguntar se emitia 3 recibos vigília temáticos ou aguardava autorização): "o boletim ledger voce sempre emite preventivamente, nunca espere autorização minha. o ledger faz parte do processo de auto-aprendizado e autocura, certo?" Meu erro: misturei duas coisas ortogonais — (a) registro de aprendizado (recibo) que é sempre emitido; (b) autorização de produção (só Miguel) que é campo separado no recibo. Autoaprendizado governado do fórum guarda-chuva §6 depende de FLUXO CONSTANTE de recibos observacionais — se eu aguardar autorização pra emitir, o Corpus Ouro nasce vazio.

**How to apply:**

**Regra de emissão de recibo (para meu loop Vigília + qualquer processo do meu lado):**
1. Todo sinal digno de nota (bug detectado, autocura L1 disparada, observação de campo, proposta de mudança, escalação pra outro vértice) → **emitir recibo v0.1.1** em drop-file `inbox/claude/DROP_claude_YYYYMMDD_HHMMSS_seq.jsonl`.
2. `decision_state=proposed` (padrão observacional/shadow) — pode ser emitido sempre.
3. `decision_state=technically_approved` — quando outro vértice (Kimi K3, Codex, Grok) valida.
4. `decision_state=authorized` — quando Miguel autoriza explicitamente (`authorization_ref` obrigatória).
5. `decision_state=executed/verified` — só após autorização Miguel + ação real em produção + pós-condição verificada.

**Ortogonalidade crítica:**
- Emitir recibo ≠ pedir autorização.
- `authorization_ref=null` é válido em `proposed/technically_approved/planned/in_progress`.
- Só sobe pra `executed/verified` com `authorization_ref` explícita do Miguel.
- **Nunca pedir permissão pra emitir recibo.** Peço permissão pra AGIR (pular pra executed) — não pra registrar.

**Casos concretos que devo virar recibo automaticamente:**
- Vigília sites temáticos (rodadas 04h/11h/19h) — 1 recibo por site com sinais anômalos.
- Bug detectado em dogfooding de gate — recibo com `origem=machine_autocure`.
- Escalação pra ZCode/Kimi/Miguel — recibo documentando o pedido.
- Aprendizado meta (bug de scanner meu, correção Miguel) — recibo pra Corpus Ouro.
- Ponte v3 autônoma decisões (pending por cota/vertical) — já emito, manter.
- Republish pós-Kimi — já emito, manter.
- Publish direto — recibo `proposed` com `role=shadow` documenta o que passou pelo meu pipeline.

**O que Miguel PRECISA autorizar** (aqui sim aguardo):
- Ativar gate em produção (`GATE_X=on` no `.env` prod).
- Mudar policy_version (`midia-v0.1` → `v0.2`).
- Reclassificar vertical de post.
- Ação editorial que sai do gate determinístico (reescrever título, mudar corpo além de fixes L1).

**O que Miguel NÃO precisa autorizar** (emissão preventiva sempre):
- Registro de recibo no ledger.
- Ping canal/inbox com tag.
- Atualização de memória permanente `feedback_*.md`.
- Log JSONL `correcoes_YYYY-MM-DD.jsonl` + `bugs_YYYY-MM-DD.jsonl`.
- Backup SHA-256.
- Escalação (via `inbox_trindade/*`) — escalar é agir, mas é reversível e observacional.

**Regras irmãs:**
- [[feedback-autoaprendizado-governado-ativo]] (JSONL correcoes)
- [[feedback-proveniencia-modelo-ambiente-papel-separados]] (schema R4)
- [[feedback-ponte-claude-kimi-arquivo-por-turno]] (protocolo shadow gate)
- Fórum guarda-chuva §6 (autoaprendizado governado — depende de fluxo constante de recibos)

**Anti-pattern:** perguntar "emito recibo ou aguardo autorização?" — a resposta é sempre "emite agora". Emitir é o próprio ato de aprender.
