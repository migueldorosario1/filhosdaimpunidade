---
name: feedback-hiperlink-fonte-95
description: §95 Hiperlink pra fonte original obrigatório em todo publish. util_hiperlink_fonte.py + safety net Camada 7 no motor (2026-06-09). Resolve bug top-1 da Cláudia Beatriz (72 ocorrências/15d).
metadata: 
  node_type: memory
  type: feedback
  originSessionId: ad62e53a-7337-4799-84ba-ed7ccefc1122
---

🔗 **§95 Cérebro:** TODO post publicado DEVE ter hiperlink pra fonte original. Defesa em camadas (Opção D — Miguel vetou fonte única no motor pra no-home; aqui o motor é só safety net redundante).

**Why:** Cláudia Beatriz registrou 72 ocorrências de "Hiperlink ausente" em 15 dias de monitoramento (32% de todos os bugs editoriais — o maior buraco). Miguel: "faz a correção estrutural. esse é um erro grave."

**How to apply:**
- `util_hiperlink_fonte.garantir_hiperlink_fonte(payload, url_original, fonte_jornal, log)` — helper compartilhado fail-open. Não duplica se url_original já está no html.
- Reutiliza `util_fonte.nome_amigavel_fonte` (já existe).
- Detecta Twitter/X com handle @ → "Via @handle".

**Estado verificado 2026-06-09 23:30 BRT (após patch Camada 7):**
- ✅ `util_hiperlink_fonte.py` deployado em `/root/util_hiperlink_fonte.py` + 3/3 smoke tests PASS (Caso A injeta, B não duplica, C fail-open url vazia).
- ✅ `motor_publicador.py` linhas 2101 + 2253 + **NOVA Camada 7 em ~2628** — safety net antes do `requests.post(WP_URL, ...)`. Backup em `motor_publicador.py.bak_pre_safety_net_95_20260609_2330_claude` (148014 bytes).
- ⚠️ Memória anterior afirmava "agente_sobrenatural patchado + 5 agentes-gap pra Kimi" — **verificado 2026-06-09: NENHUM agente importa `util_hiperlink_fonte`**. Integração nos agentes foi perdida ou nunca chegou em produção. Agora coberto pelo safety net no motor (cobre TODOS os caminhos que usam `iniciar_publicacao_especializada`).
- ⏳ Causa raiz por que linhas 2101/2253 não disparam em alguns caminhos — Kimi precisa investigar (provável early-return ou re-write de html). Safety net é redundância, não substituto.
- ⏳ Camada 1 preventiva nos 11 agentes-produtores (master_geopolitica, master_nacional, master_discursos, china, lula, latam, sheinbaum, soberania, militar, eleicoes, eleicoes_produtor) — Kimi.

**Validação produção em loop §53:** próxima publicação por sheinbaum/soberania/latam DEVE ter `<a href=URL_FONTE rel="noopener">FONTE</a>` no final. Falsificação visível em ≤1h.

**Rollback:** `sudo cp /root/motor_publicador.py.bak_pre_safety_net_95_20260609_2330_claude /root/motor_publicador.py` (restaura estado pré-patch sem efeito colateral).

**Fórum vivo:** `Foruns/forum_monitoramento_claudia_beatriz_20260607.md` — atualizado a cada rodada.

Relacionado: [[project_no_home_opcao_d_descentralizada]] (mesma filosofia), [[reference_doc_claudia_beatriz_monitoramento]], §86, §93, §94, §97. Cérebro §95 (CEREBRO_NODE_GOVERNANCA_REGRAS_VIVAS.md) tem a entrada técnica completa.
