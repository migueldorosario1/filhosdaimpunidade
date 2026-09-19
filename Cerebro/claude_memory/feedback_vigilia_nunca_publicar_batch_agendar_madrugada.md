---
name: feedback-vigilia-nunca-publicar-batch-agendar-madrugada
description: Ciclo Vigília V5 nunca despeja lote inteiro de drafts na mesma janela — distribuir via post_status=future ao longo da madrugada e do dia seguinte
metadata: 
  node_type: memory
  type: feedback
  originSessionId: d556bf3a-514a-43d5-a6d6-417905366fd5
---

Ciclo Vigília V5 **NÃO PUBLICA em lote na mesma janela** — mesmo com autorização Miguel pra "voltar ao Vigília", drenagem inteira de 7-8 drafts numa única sessão CAUSA churn no feed do Cafezinho e mata SEO/leitor.

**Regra correta a partir de 12/08/2026 23:20 BRT:**
- Após checagem tripla (DS+GPT+Claude+WS) + patch cirúrgico, usar `post_status=future` com `post_date` programada.
- Distribuir os N drafts revisados ao longo da madrugada (00:00-06:00) e do dia seguinte (07:00-22:00) — ritmo típico 1 post a cada 60-90min.
- Ordem editorial: matérias com temporalidade urgente (votações, pesquisas do dia) rodam nas 1as janelas; análise/contexto (geopolítica, retrospectiva) espalha ao longo do dia.
- Se o draft revisado tem gancho HOJE (votação ao vivo, morte, incêndio), pode publish imediato — mas caso raro.

**Why:** Miguel 12/08 23:15 BRT (imediatamente após eu drenar 7 posts em ~40min no ciclo NOITE): "não publica de uma vez não. programa para a madrugada e amanhã. mas o que já publicou deixa". Motivo estrutural: feed com 7 posts saindo em 40min quebra ritmo de leitura, empurra reportagem boa pra fora da página inicial rápido demais, e sinaliza ao Google um pico artificial de publicação. Perde CTR + perde ordenação editorial curatorial.

**How to apply:**
- Sempre que rodar Vigília V5 e revisar N drafts, calcular horários de agendamento distribuídos (ex: N=7 → 00:15, 02:00, 04:30, 07:30, 10:00, 13:00, 16:00 no dia seguinte).
- Aplicar via `wp_update_post` com `post_status="future"` + `post_date=YYYY-MM-DD HH:MM:SS` (fuso do WP = BRT).
- Registrar horário agendado no JSONL do dia (campo `agendado_para`) — futura auditoria consegue reconstruir a distribuição.
- Se a fila tem >8 drafts, negociar com Miguel (mais dias? drop de duplicatas?).
- Excepcionalmente publish imediato: matéria com gancho de tempo real (votação nesta hora, morte, tragédia). Nesses casos, marcar `urgencia=true` no JSONL.

**Aplicação retroativa:** os 7 posts do ciclo 22:26 BRT (265322, 265311, 265318, 265353, 265339, 265329, 265196, 265370) permanecem publish onde estão — Miguel autorizou "deixa" o que já saiu. Correção começa no PRÓXIMO ciclo.

Regra irmã: [[feedback-nunca-churn-publish-draft-seo]] — não rebaixar publish; agora também não empurrar batch simultâneo. As duas juntas: ritmo editorial estável.
