---
name: vigilancia-alvo-canonico-registry
description: "Vigília de sites/serviços NUNCA infere alvo por convenção de nome — sempre ler de registry canônico. Detector de regressão ciclo-a-ciclo pega falso positivo em 1 iteração. Lição fundada em 2 FPs de \"alvo errado\" em 24h (Mapa Rio URL, 4 sites repo)."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 641d1199-de3b-4e78-b57b-33f2ee48c505
---

**Regra:** Qualquer agente de vigília/monitoramento (Sentinela Cafezinho, Sentinela Temáticos futuro, healthcheck) DEVE ler alvo (URL canônica + fonte_repo + limiar esperado) de um **registry declarativo** (JSON versionado no cérebro), NUNCA inferir por convenção de nome (`sites-v4/{nome_com_underscore}`) nem por memória do agente.

**Why:** Em 24/07/2026, 2 falsos positivos de "alvo errado" em <8 horas, mesma família:
- **Manhã (~10:55 BRT):** Ponto de retomada anterior reportou Mapa Rio como "esqueleto Vite SPA 429 bytes". Causa: checou `mapario.vercel.app` (URL canonical default Vercel) em vez do domínio real `mapario.com.br`. Realidade: 349KB, título populado, Vercel 200.
- **Tarde (14:10 BRT):** Meu ciclo temáticos reportou 4 sites internacionais (GSN, Mundo Trilhos, Rail Post, Discover Brazil) como "estagnados 10-15 dias". Causa: meu grep `find` retornou pastas `sites-tematicos/{nome_snake_case}` (repos LEGADOS, dormentes desde a migração V4) em vez de `sites-v4/{slug_canonico_sem_underscore}` (repos ATIVOS). Nomes: `global_south_news` (legado) vs `globalsouth` (v4). Kimi K3 auditou às 17:35 BRT e refutou o diagnóstico — hashes citados no meu ciclo (`57f76bf`, `9314c29`, `bc17f9c`, `b32268c`) eram HEADs dos legados, enquanto os v4 têm commits 23-24/07 batendo com posts vivos nas homes.

**Padrão comum:** convenção implícita de nome ≠ realidade estrutural. LLM ou script preenche o "espaço em branco" na convenção mais plausível e mede o alvo errado com confiança. Nenhum alerta dispara porque nenhum invariante estrutural é violado — o site retorna 200, o repo existe, o git log responde. Só um humano notando a incoerência pega.

**How to apply:**
1. **Todo novo agente de vigília começa por definir o registry canônico** (`site_registry.json`, `service_registry.json`, etc) antes de qualquer código. Se ainda não existe, escreve o registry primeiro, mesmo que só pra 1 alvo.
2. **JSONL de vigília DEVE ter campo `fonte_repo` (ou equivalente) explícito** vindo do registry — nunca inferido em runtime.
3. **Detector de regressão ciclo-a-ciclo:** se `last_commit_git` ou `data_max_conteudo_home` REGRIDE (fica mais velho) entre ciclos do mesmo dia, isso é fisicamente impossível e dispara alerta P3 imediato. Teria pego ambos FPs em 1 iteração.
4. **`data_max_conteudo_home` (data do post mais recente publicado)** é a verdade última, mais confiável que `last_commit_git` — git é proxy. Conteúdo novo sem commit = deploy por fora; commit novo sem conteúdo = build/ISR quebrado. Ambos merecem P3.
5. **Árvore legada arquivada:** `sites-tematicos/` deveria virar `sites-tematicos_LEGADO_NAO_USAR/` ou ganhar README no topo alertando que é dormente. Zero risco de dual-publish, mas alto risco de novo agente medir errado (aconteceu comigo).

**Registry canônico proposto** (arquivo pendente `Cerebro/config/site_registry.json`, esqueleto no fórum):
```json
{
  "id": "mundo_trilhos",
  "url": "https://www.mundotrilhos.com",
  "repo": "Projeto Cafezinho Agentes/sites-v4/mundotrilhos",
  "cadencia": "diario",
  "limiar_horas": 48,
  "status": "ativo"
}
```

**Referências:**
- Fórum canônico: `Cerebro/Foruns/forum_kimi_diagnostico_tematicos_e_loop_20260724.md` §A (refutação) + §B.6 (proposta registry)
- JSONL com correção: `Cerebro/monitoramento_horario/tematicos/tematicos_2026-07-24.jsonl` (última linha, ts 17:35 BRT, autor kimi_k3)
- Memória irmã: [[ciclo-tematicos-3h-manual-via-loop]] (regra ganha um invariante estrutural agora)
- Bug irmão (mesma família de "alerta silencioso não chega"): `feedback_cron_silencioso_e_bug_scp_baleia_azul.md`

**Autoria da lição:** Kimi K3 (auditoria + proposta arquitetural), Claude Code (validação independente + registro).
