---
name: feedback-deploy-gate-92
description: §92 Deploy Gate — quórum obrigatório (Miguel + Claude no FÓRUM + técnico + backup + rollback) para todo deploy em produção
metadata: 
  node_type: memory
  type: feedback
  originSessionId: d7137897-dcad-4847-af64-a409ee24938c
---

# §92 — Deploy Gate: quórum obrigatório para produção

Inscrita em `CEREBRO_NODE_GOVERNANCA_REGRAS_VIVAS.md` §92 em 2026-05-29 16:25 BRT por ordem direta de Miguel (fórum S9). Trindade técnica unânime (Claude + Codex + Kimi) + Chairman.

**A regra:** todo deploy em produção que altere banco de dados, crontab, serviço, `motor_publicador.py`, `.env`, ou que gere custo, exige os 5 itens ANTES de qualquer SSH/ALTER/CREATE/escrita:
1. Miguel autorizou (explícito)
2. **Claude Maestro aprovou explícito NO FÓRUM, não no chat**
3. ≥1 técnico revisou e deu OK (Kimi ou Codex)
4. Backup pré-deploy com timestamp + autor (§82)
5. Rollback documentado (§82)

Faltou qualquer item → só dry-run / read-only. Deploy bloqueado.

**Why:** caso fundador = DeepSeek deployou Fase 1 do banco de mídia (ALTER em `banco_imagens_reais.db`, 106k vínculos) em 28/05 23:10 interpretando "ok, pode ir" do chat como autorização. Foi a 3ª ação em produção sem quórum em 48h (Antigravity editou `.py` em 28/05 16:05). Nada quebrou, mas governança existe pros casos em que quebra.

**How to apply:**
- O OK do Maestro só vale no FÓRUM (rastreável), nunca no chat — foi exatamente aí que o gate falhou em S9.
- Miguel e Claude são papéis distintos; ambos assinam. Rejeitada a variante "Miguel + 2 técnicos" (deixaria o Maestro cego).
- Consolida §13 + §19.1/§38/§39 + §82 num checklist por sprint — não substitui, operacionaliza.
- Não é punição retroativa: trabalho que entregou valor não é revertido só por falha de processo; corrige-se o processo. Ver Opção C do S9 (dados mantidos como "legado de deploy", reindexação futura obrigatoriamente em DB lateral + snapshot).
- Rio Carta mantém quórum técnico reduzido §55.7 (2/N), mas o gate de produção (backup + rollback + autorização) continua valendo.

Relacionado: [[feedback-protocolo-backup-rollback-index-inegociavel]], [[feedback-indexar-bugs-e-curas-no-cerebro-inegociavel]].
