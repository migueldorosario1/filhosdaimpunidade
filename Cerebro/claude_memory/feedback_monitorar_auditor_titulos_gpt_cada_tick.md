---
name: feedback-monitorar-auditor-titulos-gpt-cada-tick
description: "Em cada tick do loop maestro Cafezinho, verificar atentamente funcionamento do agente_auditor_titulos_gpt.py — estado, eventos JSONL, correções aplicadas, custos, alucinações reversas do GPT."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: bd63951a-ed35-4ca0-8a29-b1a900604520
---

# Monitorar auditor técnico de títulos GPT a cada tick

**Regra:** Em todo tick do loop maestro Cafezinho, dedicar um bloco específico ao monitoramento do `agente_auditor_titulos_gpt.py` (deployado por Codex sob ordem Miguel em 28/05/2026 ~01:32 BRT).

**Why:** Miguel pediu explicitamente em 28/05 01:50 BRT: *"quero que voce monitore atentamente o funcionamento do auditor técnico de titulos gpt"*. É camada nova em produção, calibragem em curso, comportamento conservador V1 — pode ter casos de borda que precisam de ajuste rápido.

**How to apply:** A cada tick, executar via SSH:

```bash
# 1. Estado atual
sudo cat /root/agent_data/auditor_titulos_gpt/estado.json

# 2. Últimas 3 execuções do cron
sudo tail -3 /root/agent_data/auditor_titulos_gpt/cron.log

# 3. Últimos 5 eventos JSONL
sudo tail -5 /root/agent_data/auditor_titulos_gpt/auditor_titulos_gpt_$(date +%Y-%m-%d).jsonl

# 4. Estatísticas: total/ações/categorias/confiança/latência/custo
```

**O que verificar em cada tick:**

1. **`hardstop: false`** no estado.json — se virar `true`, KILL-SWITCH §17 acionado (alerta vermelho)
2. **`custo_dia_usd`** — alerta acima de $3, hardstop projetado em $5
3. **`correcoes_hoje`** — quando incrementar, validar manualmente título antes/depois via WP API
4. **`bloqueios_hoje`** — qualquer bloqueio é caso excepcional, reportar SEMPRE
5. **Distribuição de `categoria_erro`** — se `outro_titulo` > 70%, prompt do GPT está vago, sinalizar pra Codex calibrar
6. **`confianca` média e mínima** — confiança <0.7 em correção aplicada = alerta
7. **`latencia_ms`** — alvo <3s; >5s consistente = degradação API
8. **Alucinações reversas do GPT** — comparar `titulo_original` vs `titulo_corrigido` em ações "corrigido" e ver se sugestão GPT remove informação CORRETA ou inventa problema
9. **Discrepância log "corrigido" vs `correcoes_hoje`** — se evento JSONL diz "corrigido" mas estado.json não incrementou, é semântica V1 ("GPT recomendou mas auditor não aplicou") — registrar pra Codex padronizar

**Sinais de problema (REPORTAR a Miguel):**
- hardstop acionado
- Custo dia >$3
- Correção aplicada com confiança <0.85 ou em categoria `outro_titulo`
- Alucinação reversa confirmada (GPT removeu info correta ou inventou problema)
- Latência >5s média por 3+ ticks
- Cron job parou (sem novo evento por >30min sendo que há posts novos)
- Erro persistente no campo `erro` do JSON cron

**Sinais saudáveis (silenciar relato):**
- hardstop=false, custo crescente linear, latência ~2s
- Muitos `monitorar`/`ok`, poucos `corrigido` (V1 conservadora)
- Diversidade de categorias razoável
- `correcoes_hoje` baixa (V1 ainda calibrando)

**Validação inicial feita 28/05 01:50 BRT:**
- 32 posts auditados em ~18min de operação
- Custo $0.10 (projeção $0.18/dia, MUITO abaixo do estimado $1.08)
- 0 correções aplicadas no WP hoje
- Latência média 2s, confiança média 0.82
- 72% categoria `outro_titulo` (genérica — Codex pode refinar)
- 2 alucinações reversas detectadas no GPT (#252369 remover "17 mil qubits" e #252379 inventar Patrushev) — comportamento conservador V1 corretamente NÃO aplicou
