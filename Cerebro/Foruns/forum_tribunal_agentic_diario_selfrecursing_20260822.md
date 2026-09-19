# 📋 FÓRUM — TRIBUNAL AGÊNTICO DIÁRIO + arquitetura self-recursing de qualidade (22/08/2026)

**Ordem do Miguel:** notas de qualidade dos posts V4 (frescor, fact-checking, originalidade, diversidade, tese c/ subnotas vilão/herói/suspense/consequência); tribunal diário que seleciona top1 e pior e gera análise incorporada às diretrizes; arquitetura voltada a aprendizado e self-recursing.

## Arquitetura do loop (implantada e provada no 1º dia)
```
Produção V4 (dia N) → TRIBUNAL AGÊNTICO (20:30 BRT, cron NYC):
  juiz cascata glm-5-turbo→deepseek→kimi (_verifier_llm_json) com RUBRICA completa
  → notas por post + TOP1/PIOR + análise + sugestão de diretriz
  → dados/tribunal_diario/<dia>.json + dados/diretriz_qualidade_viva.md (últimos 5 dias)
→ WORKER lê a DIRETRIZ VIVA no briefing de TODA redação (patch 22/08, .bak_pre_diretriz_viva)
→ produção do dia N+1 melhora → julgada amanhã → loop infinito (self-recursing)
```

## Peças (tudo com prova)
- Script: `/root/v4_labs/codigo/tribunal_agentic_diario.py` (novidade: WP_* e chaves LLM vêm de /root/.env.unificado — chaves.sh não tem WP; filtro V4 por meta zizi_job_id v4d_* com context=edit — author=5786 é bloqueado com 404 anti-enumeração).
- Cron: `30 23 * * *` NYC (20:30 BRT) → `/root/agent_data/tribunal_diario.log`.
- Worker: briefing recebe "DIRETRIZ VIVA DO TRIBUNAL DIÁRIO (OBEDÉCER)" (últimos 900 chars).
- Resumo diário chega ao Miguel pela ronda 30/30/CCTV (ler tribunal_diario/<dia>.json).

## 1ª edição (22/08, julgou os 30 posts do dia) — destaques
- **TOP: 267033 (IA/supercomputação, total 7,2)** · **PIOR: 267037** · médias: fact-checking forte (8-9), tese fraca (4-5), herói quase zero.
- **Diretriz gerada para amanhã** (já no briefing): abrir pela consequência material antes do fato seco; máx. 3 posts do mesmo eixo/dia (7/12 posts eram Oriente Médio — canibalizou diversidade); todo post com antagonista COM NOME E ROSTO ou protagonista resistindo.
- Lições: "desertificação de heróis"; consequência material salva (os 2 melhores têm números concretos: R$ 2,3 bi, 3 mil profissionais).
- Notas completas: dados/tribunal_diario/2026-08-22.json (NYC).

## Notas técnicas do dia (LIÇÕES L6-L7)
- L6: author=<id> na REST do WP = 404 (anti-enumeração) → usar context=edit + filtro por meta.
- L7: o adapter do labs aplica o contrato editorial da função (curadoria) — para juízes com prompt LIVRE e JSON, usar _verifier_llm_json do worker.
