---
name: consulta-kimi-k3-3h-autonomia-claude
description: "Loop Sentinela consulta Kimi K3 a cada 3h; Claude tem autonomia total pra decidir com Kimi qual fix aplicar sem consultar Miguel, desde que protocolos sejam seguidos"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: a0935816-574e-4c24-a84b-340dede75e48
---

**Regra:** o loop Sentinela do Claude (`*/30 * * * *`) roda script `~/ferramentas/sentinela/consulta_kimi_k3_3h.py` no início de cada tick. Script tem check interno: só chama Kimi K3 (`kimi-k3` via `api.moonshot.ai/v1`, chave `KIMI_PAYGO_API_KEY` em `Projeto Cafezinho Agentes/Outros/chaves/kimi_paygo.env`) se última consulta foi >3h atrás. Custo ~$0.10/consulta (~19k tokens), ~$0.80/dia. Respostas em `Cerebro/Foruns/consultas_kimi_k3_3h/consulta_kimi_k3_YYYYMMDD_HHMM.md`; minha réplica em `resposta_claude_a_kimi_YYYYMMDD_HHMM.md`. Kimi recebe system prompt dando liberdade total pra opinar/codar/auditar/discordar. Claude tem autonomia total pra aceitar, refutar ou escalar qualquer ponto — Miguel não precisa aprovar cada decisão.

**Why:** Miguel 2026-07-25 01:30 BRT: *"pode escolher sempre. não vou ter tempo para decidir isso. o que o kimi e voces decidirem tudo bem. desde que voces cumpram os protocolos de segurança, registrem tudo no cérebro, mantenham sempre a chance de rollback, mantenham o foco na qualidade e rigor de qualidade no texto"*. Contexto: Kimi K3 tinha acabado de fechar 3 bugs upstream V4 (24/07 11:00 BRT) + auditar 2 FPs meus no ciclo temáticos (17:35 BRT). Confiança mútua estabelecida. Miguel prefere velocidade + rigor documental > microgerência.

**How to apply:** ao receber consulta Kimi K3, para cada ponto levantado:
1. **Verificar no código** antes de aceitar — Kimi pode se enganar (caso #3 fal_ai 404 na consulta #1, refutado com base em comentário do código linhas 549-550 `sentinela_ciclo.py`).
2. **Aplicar fix se baixo/médio risco** (backup .bak_ SHA-256 → patch → `py_compile` → smoke test) sem consultar Miguel.
3. **Escalar SÓ se mudança estrutural** que muda natureza editorial ou arquitetural do site (ex: proposta cap 2h escalonado 2-6h da consulta #1 — Kimi explicitamente disse "não implementar sem Miguel"; eu concordei e propus fase shadow-mode).
4. **Sempre registrar em 3 camadas:** (a) `bugs_YYYY-MM-DD.jsonl` instância, (b) `Outros/manual_de_bugs.md` padrão novo se aplicável (numerar sequencialmente #27, #28…), (c) `CEREBRO_NODE_ATUALIZACOES.md` linha do dia + memória feedback quando regra estrutural.
5. **Rollback SEMPRE possível** — backup nomeado `<arquivo>.bak_pre_claude_<slug>_<ts>` com SHA-256 registrado antes do patch. Nunca patch sem backup.
6. **Escrever resposta no fórum** — `resposta_claude_a_kimi_YYYYMMDD_HHMM.md` no mesmo diretório da consulta, formato: ✅ aceito+aplicado / ❌ refutado com evidência / 🟨 escalado Miguel. Termina com "combustível pra próxima consulta" — sinais/perguntas específicas que quero que Kimi comente na próxima.
7. **Qualidade textual > velocidade.** Se qualquer fix tocar prompt ou pipeline editorial (charges, fontes, títulos, corpo) exige teste extra: leitura manual de 1 post gerado pelo pipeline pós-fix antes de considerar aplicado.

**Case fundador (consulta #1 · 25/07 01:20 BRT):** Kimi levantou 4 pontos. Aplicados #1 (incoerência 262819 → bug #28) e #2 (zoneinfo → bug #27). Refutado #3 (fal_ai 404 documentado). Escalado #4 (cap 2h escalonado). Registro completo em `consulta_kimi_k3_20260725_0120.md` + `resposta_claude_a_kimi_20260725_0140.md`.

**Regras irmãs:** [[protocolo-memoria-bugs-ler-antes-agir]] (3 camadas), [[ciclo-tematicos-3h-manual-via-loop]] (rotina similar mas alvo temáticos), [[kimi-bugs-upstream-v4-fechados-20260724]] (histórico de colaboração Claude↔Kimi).
