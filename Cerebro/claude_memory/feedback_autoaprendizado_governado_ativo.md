---
name: feedback-autoaprendizado-governado-ativo
description: "Autoaprendizado governado do Banco V4 Real ativo a partir de 06/08/2026 18:55 BRT — toda correção do Miguel (chat/inbox/wp) vira evento estruturado em correcoes_YYYY-MM-DD.jsonl com reason_code, alimentando Corpus Ouro sem autoaplicação"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 7a8b86e8-615f-48dd-924d-5e86f182a869
---

**A partir de 06/08/2026 18:55 BRT, toda correção do Miguel a mim (Claude Code) — via chat, inbox_trindade, ou WP editorial — vira EVENTO ESTRUTURADO em `Cerebro/monitoramento_horario/correcoes_humanas/correcoes_YYYY-MM-DD.jsonl` no formato §6.2 do fórum `forum_banco_midia_v4_real_vision_autoaprendizado_20260806.md`, além de virar (como sempre) `memory/feedback_*.md`.**

**Why:** Miguel perguntou hoje 18:52 BRT se o conceito de autoaprendizado do fórum guarda-chuva foi assimilado por mim e pelo Kimi. Auditoria brutal expôs: **não estava**. O conceito vivia só no fórum e na minha proposta §13.4 (que eu prometi implementar "07/08" mas não tinha começado). Miguel: "vocês incorporaram esse conceito de autoaprendizado?... vai andar?". Resposta era "no papel, não no pipeline" — inaceitável. Executei imediatamente.

**How to apply:**

**Toda vez que Miguel me corrigir sobre imagem/hero/texto/vertical/cota/protocolo:**
1. **Aplicar a correção** (comportamento normal).
2. **Gravar evento estruturado** no `correcoes_YYYY-MM-DD.jsonl` com schema abaixo (append, arquivo por dia, backup automático diário).
3. **Criar/atualizar memory `feedback_*.md`** (comportamento antigo, complementar).
4. **Referenciar cross-link:** o campo `regra_derivada` do JSONL aponta pro `feedback_*.md`; o corpo do `feedback_*.md` deve mencionar que também virou evento no JSONL.

**Schema §6.2 do fórum guarda-chuva + campos extras cafezinho:**
```json
{
  "ts": "YYYY-MM-DDTHH:MM:SS-03:00",
  "cafezinho_channel": "chat_claude | inbox_trindade | wp_editorial | telegram",
  "article_id": 264XXX | null,
  "asset_id": "sha256..." | null,
  "decision": "corrected_by_editor_in_place | let_expire_pending_editorial | policy_change_by_editor | protocol_change_by_editor | rejected_by_editor | approved_after_review",
  "reason_code": "wrong_person | wrong_event | wrong_institutional_label | generic | duplicate | rights | broken | weak_crop | editorial_pattern_* | policy_relaxation_* | workflow_* | other",
  "comment": "citação Miguel verbatim + contexto",
  "regra_derivada": "feedback_<slug>",
  "policy_version": "vX-<tópico>-YYYY-MM-DD[-HH:MM]",
  "vision_run_id": null
}
```

**Ao fim de cada dia:**
- Backup automático `Cerebro/Backups/correcoes_humanas/correcoes_YYYY-MM-DD.jsonl.bak` (comportamento a implementar via cron ou próximo ciclo).
- Contar eventos vs correções vs memórias criadas — cardinalidades devem bater. Se JSONL < memórias, capturei correção via `feedback_*.md` mas esqueci de gravar o evento estruturado — reforçar.

**O que NÃO faço sozinho:**
- Não aplico regra derivada automaticamente — só registro. Promoção de regra → replay Corpus Ouro → shadow → aprovação Miguel/Trindade (§6.3 do fórum guarda-chuva).
- Não altero código de produção baseado em pattern do JSONL — quem faz isso é Codex/Kimi/GLM com replay engine + aceite Miguel.
- Não modifico `policy_version` retroativamente — versionamento é imutável.

**Ingestão upstream (não é meu escopo, mas registro pra referência):**
- ZCode/Codex ingere o JSONL no Corpus Ouro V4 quando for construído (Fase 4 do plano guarda-chuva).
- Kimi K3 (Desktop e ZCode) precisa saber que o JSONL existe pra também alimentar caso o Miguel corrija ele diretamente (via Telegram do Kimi, por exemplo) — pinguei no canal 06/08 18:55 BRT.

**Estado inicial:** 4 correções retroativas de HOJE 06/08 já gravadas (Tesouro Nacional 00:15, gafes Lula Folha 04:20, Ponte v3 15:25, Ponte autônoma 17:15). Meta: 100% dos `feedback_*.md` novos ganharem evento espelho no JSONL a partir de 07/08.

**Regras irmãs:**
- [[feedback-indexacao-cerebro-e-pedir-decisao-com-contexto]] (indexação diária + pedir decisão)
- [[feedback-gravacao-datada-por-ciclo-e-ponte-kimi-regular]] (rastro datado por ciclo)
- Fórum guarda-chuva §6 (autoaprendizado governado) + §13.4 (minha proposta original)

**Sinal de que o autoaprendizado está mesmo andando** (medida diária):
- Arquivo `correcoes_YYYY-MM-DD.jsonl` existe e cresce ≥1 evento/dia (dias com correção Miguel).
- Cross-link `regra_derivada ↔ feedback_*.md` bate em 100%.
- Kimi/Codex/GLM consomem o JSONL quando forem construir o Replay Engine (Fase 4).
- Se por 7 dias consecutivos Miguel não precisar corrigir o mesmo tipo de erro duas vezes = aprendizado funcionou.
